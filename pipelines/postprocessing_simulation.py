from helpers.CustomException import CustomException
from components.postprocessing import get_conversation, split_conversation, get_report_per_question, create_report_pdf

def postprocessing_pipeline():
    try:
        conversation = get_conversation()
        questions = split_conversation(conversation)
        report_dict = get_report_per_question(questions)
        create_report_pdf(report_dict)
    except Exception as e:
        raise CustomException(e)
