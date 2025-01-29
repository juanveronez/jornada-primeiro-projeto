from etl import pipeline_sales_etl

pipeline_sales_etl(input_folder='../data', 
                   output_folder='../processed',
                   load_format=['csv'])