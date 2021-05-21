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
- `tests/`: conjunto de testes unitários para os componentes do Plpred.

## Command line interface (CLI)

### `plpred-preprocess`

```
usage: plpred-preprocess [-h] -m MEMBRANE_PROTEINS -c CYTOPLASM_PROTEINS -o OUTPUT

plpred-preprocess: data preprocessing tool

optional arguments:
  -h, --help            show this help message and exit
  -m MEMBRANE_PROTEINS, --membrane_proteins MEMBRANE_PROTEINS
                        path to the file containing membrane proteins (.fasta)
  -c CYTOPLASM_PROTEINS, --cytoplasm_proteins CYTOPLASM_PROTEINS
                        path to the file containing cytoplasm proteins(.fasta)
  -o OUTPUT, --output OUTPUT
                        path to the output file (.csv)
```

### `plpred-train`

```
usage: plpred-train [-h] -p PROCESSED_DATASET -o OUTPUT [-r]
                    [-a {random_forest,neural_network,gradient_boosting,svm}]

plpred-train: model training tool

optional arguments:
  -h, --help            show this help message and exit
  -p PROCESSED_DATASET, --processed_dataset PROCESSED_DATASET
                        processed dataset generated by plpred-preprocess (.csv)
  -o OUTPUT, --output OUTPUT
                        path to the output trained model (.pickle)
  -r, --report          show classification report
  -a {random_forest,neural_network,gradient_boosting,svm}, --algorithm {random_forest,neural_network,gradient_boosting,svm}
                        machine learning algorithm
```

### `plpred-predict`

```
usage: plpred-predict [-h] -i INPUT -o OUTPUT -m MODEL

plpred-predict: subcellular location prediction tool

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input file (.fasta)
  -o OUTPUT, --output OUTPUT
                        output file (.csv)
  -m MODEL, --model MODEL
                        trained model (.pickle)
```