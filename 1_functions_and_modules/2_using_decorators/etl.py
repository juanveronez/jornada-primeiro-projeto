import pandas as pd
import os
import glob
from utils_log import log_decorator

@log_decorator
def extract_json_folder(folder_path: str) -> pd.DataFrame:
  # glob get all files that matchs with pathname pattern
  # path join join two (or more) path names (for exemple: data, *.json = data/*.json)
  json_files = glob.glob(os.path.join(folder_path, '*.json'))

  df_list = [pd.read_json(json_file) for json_file in json_files]
  df_total = pd.concat(df_list, ignore_index=True)
  return df_total

@log_decorator
def calculate_total_sales_kpi(df: pd.DataFrame) -> pd.Series:
  return df['Quantidade'] * df['Venda']

@log_decorator
def load_df(df: pd.DataFrame, folder: str, load_format: list[str] = ['csv']):
  try:
    os.mkdir(folder)
  except FileExistsError:
    print(f'Folder {folder} already exists')
  
  if 'csv' in load_format:
    df.to_csv(os.path.join(folder, 'data.csv'), index=False)
  if 'parquet' in load_format:
    df.to_parquet(os.path.join(folder, 'data.parquet'), index=False)

@log_decorator
def pipeline_sales_etl(input_folder: str, output_folder: str, load_format: list[str]):
  df = extract_json_folder(input_folder)
  df['Total'] = calculate_total_sales_kpi(df)
  
  load_df(df, output_folder, load_format)

# use this dunder (double under) name to just execute this code when is the main module
if __name__ == '__main__':
  json_folder = 'data'
  output_folder = 'processed'
  load_type = ['csv', 'parquet']
  
  pipeline_sales_etl(json_folder, output_folder, load_type)
  