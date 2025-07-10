from components.preprocessing import get_resume, get_job_description, get_features
from tqdm import tqdm

def preprocessing_pipeline(resume_path=r"dummy_data\resume.pdf", job_description_path=r"dummy_data\job_description.pdf"):
    try:
        resume = get_resume(resume_path)
        job_description = get_job_description(job_description_path)
        features = get_features(resume=resume, job_description=job_description)
        return features
    except Exception as e:
        raise CustomException(e)

if __name__ == "__main__":
    print(preprocessing_pipeline())
