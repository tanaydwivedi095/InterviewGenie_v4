from pipelines.preprocessing_pipeline import preprocessing_pipeline
from helpers.CustomException import CustomException
from helpers.utils import load_llm

def get_features(resume_path=None, job_description_path=None):
    features = preprocessing_pipeline(resume_path, job_description_path)
    return features

def generate_question():
    pass
    