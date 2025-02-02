# Classes no Python

Uma classe é um objeto que cria uma instância alocada em memória toda vez que invocamos a classe. Dessa forma podemos usar essa instância de forma única para invocar seus métodos ou acessar seus atributos, abstraindo a complexidade e tornando seu uso mais simples.

Além disso, o paradigma de OOP garante a posibilidade de criarmos classes mais ou menos genéricas, além de classes herdadas, dessa forma diminuindo a quantidade de código e simplificando a manutenção e testes.

A necessidade de criar uma classe, extender uma classe já existente ou ainda encapsular classes é algo complexo e que necessita de análise, porém é função do desenvolvedor, engenheiro de dados ou cientista entender o escopo do desenvolvimento e buscar a solução que traga maior valor e menor repetição, lembre-se **DRY! (Don't repeat yourself)**

## Estrutura de uma Classe

Uma classe no Python tem uma estrutura com o nome reservado `class` e por padrão segue o formato **PascalCase**. Além disso, tem o método especial `__init__`, que é o método contrutor da classe, sendo que qualquer método é escrito com a palavra reservada `def`, assim como funções comuns no Python.

As classes também usam em seus métodos o `self` para referenciar a instância da classe, ou seja, o local em memória alocado para aquele objeto criado com a classe.

Diferente de uma classe JavaScript, para invocarmos um objeto com a classe usamos apenas seu nome, como no exemplo abaixo:

```py
  class GenericETL:

    def __init__(self, datasource):
      self.datasource = datasource

    def save(self, path):
      self.datasource.to_csv(path)

  etl = GenericETL(df)
  etl.save('./df.csv')
```

## Herança

Classes não precisam existir no vácuo, podemos ter classes mais genéricas ou mais específicas para cada caso. Podendo criar classes que herdam outras, dessa forma já tendo métodos e atributos que recebem dessa classe original. Além disso, podemos invocar qualquer método ou atributo da classe que fazemos a herança usando o termo `super()`, sendo essa a palavra reservada que usamos para referenciar a classe herdada.

```py
  class SalesETL(GenericETL):
    def save(self, path, region):
      super().save(f'{region}/{path}')

  etl = SalesETL(df)
  etl.save('./df.csv', 'SP')
```

Importante lembrar, nos casos em que queremos que uma classe use exatamente o mesmo comportamente da classe herdada podemos apenas omitir a definição, pois dessa forma o método não será sobrescrito e usaremos o que foi herdado.

Além disso, é sempre bom lembrar que a classe que será herdada precisa ser definida no `class`, como em `SalesETL(GenericETL)`

## Encapsulamento

Assim como podemos fazer com que uma classe herde outra classe, podemos fazer com que uma classe possa usar outras classes e essa mais genérica varie seu comportamento com base na classe determinada.

Com isso teremos comportamentos customizados e fluxos padrões independente de qual classe expecífica for usada. Um exemplo disso são classes relacionadas com Bancos de Dados. Mesmo tendo muitas opções e formas de conexão podemos criar um Database genérico e sua forma de conexão, e outros métodos podem variar, mas de uma forma que não seja necessário nenhum conhecimento de quem apenas quer usar a classe Database.

Um exemplo disso pode ser encontrado nos arquivos em `3_encapsulamento`

## Polimorfismo

Conceito que é usado de forma teórica dentro de OOP para termos classes que tem uma mesma base abstrata e variam seus comportamentos internos dependendo da especificidade de cada objeto, ou do caso que deve será aplicado.

Para casos desse tipo é comum termos uma classe abstrata base, que não terá a implemtação dos métodos e atributos, mas deixará claro o que deve ser implementado para que uma classe "filha" possa herdar a classe abstrata.

Então como teremos diferentes funções com essas mesmas propriedades, mas comportamentos diferentes dependendo do contexto aplicado para a classe, podemos entender como um comportamento polimórfico.

Exemplo de classe abstrata:

```py
from abc import ABC, abstractmethod

class AbstractDataSource(ABC):
    @abstractmethod
    def start(self):
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def get_data(self):
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def transform_data_to_df(self):
        raise NotImplementedError("Método não implementado")

    @abstractmethod
    def save_data(self):
        raise NotImplementedError("Método não implementado")

    def hello_world(self):
        print('Hello World')
```

A classe ABC é uma classe própria do Python usada para criação de classes abstratas.

Mais exemplos podem ser encontrados em `4_heranca_e_polimorfismo`
