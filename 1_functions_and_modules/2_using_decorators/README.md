# Projetos mais complexos

Quando começamos um projeto complexo, entender as necessidades e como resolver o problema é importante. Porém, também é importante entendder como dar manutenção da melhor forma e validar o que foi feito da melhor forma. Para isso, ferramentas de qualidade e integração (CI) são importantes. Para que dessa forma o código não apenas funcione, mas continue funcionando a longo prazo.

## Ferramenta de processamento

Quando começamos um projeto, o primeiro passo é entender que ferramenta usaremos para processar os arquivos, no caso conseguir ler e escrever em diferentes formatos.

- Pandas
- Polars
- DuckDB
- Dask

## Ferramenta de Qualidade

Além disso, precisamos definir qual ferramenta vamos usar para garantir a qualidade do projeto. Para isso temos duas escolhas:

- Pydantic (Linha a linha ou API (objetos))
- Pandera (SQL e DataFrames)

Então usamos o Pydantic para casos mais simples, como leitura de arquivos linha a linha (csv.DictReader por exemplo) e o Pandera em outros casos.

Com isso teremos a vantagem de podermos mexer com estruturas mais complexas, como DataFrames.
