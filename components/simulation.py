from pipelines.preprocessing_pipeline import preprocessing_pipeline
from helpers.CustomException import CustomException
from helpers.utils import load_llm, load_previous_conversation, humanify

def get_features(resume_path=None, job_description_path=None):
    try:
        features = preprocessing_pipeline(resume_path, job_description_path)
    except Exception as e:
        CustomException(e)
    return features

def get_conversation():
    try:
        conversation = load_previous_conversation()
    except Exception as e:
        CustomException(e)
    return conversation

def create_prompt(conversation, features):
    try:
        prompt = f"""
        You are an expert interviewer whose only job is to ask one targeted question.
        
        Your question must:
        - Be based on the candidate’s summarized resume and job description (the “Features”).
        - Incorporate the last exchange if a previous conversation exists; otherwise rely solely on the Features.
        - Read like a human speaking in a script format (for example:  
            Interviewer: “…”).
        - Contain no extra commentary or explanations—only the question itself.
        
        Features: {features}
        Previous Conversation: {conversation}
        """
    except Exception as e:
        CustomException(e)
    return prompt

def generate_question(prompt):
    try:
        llm = load_llm()
        question = llm.invoke(prompt)
        return question.content
    except Exception as e:
        CustomException(e)

def get_answer():
    try:
        answer = input("Enter the answer:\n")
    except Exception as e:
        CustomException(e)
    return asnwer
    
def save_conversation(previous_conversation, current_question, current_answer=""):
    try:
        conversation = f"{previous_conversation}\n\nQuestion: {current_question}\nAnswer: {current_answer}"
        with open(r"artifacts\previous_conversation.txt", "w") as f:
            f.write(conversation)
    except Exception as e:
        CustomException(e)
