## ScoreWise

This is a end-to-end project focused on building pipelines, predicting scores, and give outputs. The achieved accuracy is 88% of this project.

Used Concept: 
- DVC(Data Version Control)
- MLFlow

Libraries used:
- numpy 
- pandas
- python-dotenv
- mysql-connector-python
- pymysql
- scikit-learn
- ipykernel
- seaborn
- catboost
- xgboost
- Flask
- dill
- mlflow

### How to run?
Fork and git clone it into your space

1. Create an environment
```bash
conda create -p "env. name" (tip: name it venv)
```

2. Activate environment
```bash
conda activate venv/
```

3. Either run one of these
```bash
pip install -r requirements.txt
```

OR

```bash
python setup.py install
```


This will create a build of the project, then run app.py with command
```bash
python app.py
```
