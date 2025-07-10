from components.simulation import get_features, get_conversation, create_prompt, generate_question, get_answer, save_conversation
from helpers.utils import load_llm
from helpers.CustomException import CustomException

def end_simulation():
    prompt = f"""
    Generate a very small script thanking the interviewee and ending the interview process
    """
    llm = load_llm()
    end_script = llm.invoke(prompt)
    return end_script
    
def simulation_pipeline():
    features = get_features()
    for question_idx in range(0,5):
        previous_conversation = get_conversation()
        master_prompt = create_prompt(previous_conversation, features)
        question = generate_question(master_prompt)
        answer = get_answer()
        save_conversation(previous_conversation, question, answer)
    print(end_simulation())
    
