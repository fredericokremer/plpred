from setuptools import setup, find_packages

setup(
    name="plpred",
    version="0.0.1",
    packages=find_packages(),
    author="Frederico Schmitt Kremer",
    author_email="fred.s.kremer@gmail.com",
    description="plpred: a protein subcellular location prediction program",
    keywords="bioinformatics",
    entry_points = {
        'console_scripts':[
            'plpred-preprocess = plpred.preprocessing:main',
            'plpred-train = plpred.training:main',
            'plpred-predict = plpred.prediction:main'
        ]
    }
)