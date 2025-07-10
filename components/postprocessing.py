from helpers.utils import load_llm, load_previous_conversation
from helpers.CustomException import CustomException

def get_conversation():
    conversation = load_previous_conversation()
    return conversation

def split_conversation(conversation):
    questions = conversation.split("Question: ")
    return questions

def get_report_per_question(questions):
    llm = load_llm()
    prompt = """
        You are an expert evaluator. You will receive a Question and its proposed Answer. Your task is to:
        
        1. State whether the Answer is Correct or Incorrect.
        2. Provide concise, constructive feedback: highlight any missing points and suggest how to improve the Answer.
        
        Respond with ONLY the following, no extra text:
        
        Correctness: <Correct/Incorrect>
        Feedback: <your feedback>
        
        Question: {question}
        Answer: {answer
        """

    report = dict()
    for document in questions:
        question, answer = document.split("Answer")
        formatted_prompt = prompt.format(question=question, answer=answer)
        report[question] = {
            "Feedback":llm.invoke(formatted_prompt).content,
            "Answer": answer
        }
    return report

def create_report_pdf(report: dict, filename: str = r"artifacts/report.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for question, data in report.items():
        pdf.set_font("Arial", "B", 12)
        pdf.multi_cell(0, 8, f"Question: {question.strip()}")
        pdf.set_font("Arial", size=12)
        answer = data.get("Answer", "").strip()
        pdf.multi_cell(0, 8, f"Answer: {answer}")
        feedback = data.get("Feedback", "").strip()
        pdf.multi_cell(0, 8, f"Feedback: {feedback}")
        pdf.ln(5)
    pdf.output(filename)
