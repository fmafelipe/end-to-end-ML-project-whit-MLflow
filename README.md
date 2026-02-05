# end-to-end-ML-project-whit-MLflow


## Workflows



1. Update config.yaml 
2. Update schema.yaml<!-- archivo con informacion de las columnas y data type de la data -->
3. Update params.yaml <!-- Hiperparametros del modelo  -->
4. Update the entity
5. Update the configuration manager in src config
6. Update the components    <!-- como data validaion, data transformation,  -->
7. Update the pipeline      <!-- donde se integran y orquestan los components  -->
8. Update the main.py
9. Update the app.py




# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/fmafelipe/end-to-end-ML-project-whit-MLflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.11.9 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

import dagshub
dagshub.init(repo_owner='fmafelipe', repo_name='end-to-end-ML-project-whit-MLflow', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/fmafelipe/end-to-end-ML-project-whit-MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=fmafelipe 
```