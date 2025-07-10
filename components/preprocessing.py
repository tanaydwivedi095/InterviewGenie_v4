import fitz
from helpers.CustomException import CustomException
from helpers.utils import load_llm

def get_resume(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        CustomException(e)

def get_job_description(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        CustomException(e)

def get_features(resume, job_description):
    prompt = f"""
    You are an intelligent assistant that reads a candidate's resume and a job description, and extracts **only the most relevant information** from the resume that matches the job description.

    ### Task:
    Given:
    1. A **candidate's resume text**.
    2. A **job description**.

    Your job is to analyze the job description and fetch the most relevant parts from the resume that align with the job role. You must also extract identifying and contextual information.

    ### Inputs:
    RESUME:
    \"\"\"{resume}\"\"\"

    JOB DESCRIPTION:
    \"\"\"{job_description}\"\"\"

    ### Output:
    Provide the following fields in structured bullet-point format:

    1. **Candidate Name**: Extracted from resume.
    2. **Current Designation**: Candidate's current role (from resume).
    3. **Target Job Designation**: Role mentioned in the job description.
    4. **Company Name (from JD)**: The company mentioned in the job description.
    5. **Job Description**: A cleaned summary of the provided JD (5-10 lines).
    6. **Relevant Skills (from Resume)**: Only include skills matching those asked in JD.
    7. **Relevant Projects (from Resume)**: Projects from resume closely related to the JD.
    8. **Relevant Experience (from Resume)**: Work experience sections that match the JD.
    9. **Relevant Certifications (from Resume)**: Certifications (if any) related to the JD.

    ### Notes:
    - Keep the output factual and extractive, not generative.
    - Do not invent any information.
    - If something is missing in the resume, mention it as `Not Found`.
    - The features should be well described, no relevant information from resume or job description should be missing.
    - The projects and the experience should be well described.
    """
    llm = load_llm()
    features_extracted = llm.invoke(prompt)
    return features_extracted.content
