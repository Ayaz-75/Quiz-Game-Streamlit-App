import streamlit as st
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Set up the quiz
question_bank = [Question(q['text'], q['answer']) for q in question_data]
quiz = QuizBrain(question_bank)

# Initialize session state variables if they don't exist
if 'question_no' not in st.session_state:
    st.session_state.question_no = 0
    st.session_state.score = 0

# Function to update score and question number
def update_quiz(user_answer):
    current_question = quiz.question_list[st.session_state.question_no]
    correct_answer = current_question.answer
    if user_answer.lower() == correct_answer.lower():
        st.session_state.score += 1  # Increment score if answer is correct
    st.session_state.question_no += 1  # Move to the next question

# Display the current question and score
st.title("Quiz Game 🧩")
st.write(f"Score: {st.session_state.score}/{st.session_state.question_no}")

# Check if there are still questions left
if st.session_state.question_no < len(quiz.question_list):  # Ensure within range
    current_question = quiz.question_list[st.session_state.question_no]
    st.write(f"Q{st.session_state.question_no + 1}: {current_question.text}")

    # Allow user to answer the question
    user_answer = st.radio("Your answer:", ["True", "False"], key="answer")

    # When the user selects an answer, update the quiz state
    if st.button("Submit Answer"):
        update_quiz(user_answer)  # Update score and question number
        st.rerun()  # Refresh the page to show the next question
else:
    st.write("You've completed the quiz!")
    st.write(f"Your final score is {st.session_state.score}/{len(quiz.question_list)}")
    restart_button = st.button("Restart Quiz")
    
    if restart_button:
        # Reset session state and restart the quiz
        st.session_state.clear()  
        st.rerun()
