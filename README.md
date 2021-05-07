# plpred

By Frederico Schmitt Kremer

a protein subcellular location prediction program

## Setup

```
$ make setup
```

## Project Structure

- `environment.yml`: configurações do ambiente do conda
- `requirements.txt`: bibliotecas a serem instaladas no Python
- `Makefile`: centralizar comandos através de regras (rules)
- `data/`: diretório de dados. Os dados brutos são guardados na pasta `data/raw/`,os dados preprocessados na pasta `data/processed` e os modelos treinados na pasta `data/models`.
- `plpred/`: diretório principal do pacote, com as função da aplicação.
- `plpred/models`: disponibiliza modelos preditivos baseados em *Random Forest*, *Gradient Boosting*, SVM e redes neurais (MLP).
