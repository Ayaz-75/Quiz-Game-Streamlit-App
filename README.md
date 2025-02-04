# Python Quiz Game with Streamlit

Welcome to the **Python Quiz Game** repository! This project is a fun interactive quiz game built using **Streamlit** where users can answer true/false questions, see their score, and track their progress throughout the game.

## Features:
- **Multiple-Choice Questions**: The quiz consists of true/false questions.
- **Real-time Scoring**: The score is updated after each answer.
- **Quiz Restart**: After completing the quiz, users can restart the quiz and track their progress again.
- **Streamlit Interface**: Simple and interactive UI powered by Streamlit.

## Project Structure:
The project is divided into the following files:
- **main.py**: The main functionality that runs the quiz and manages the user interactions.
- **data.py**: Contains the list of questions and answers.
- **question_model.py**: Defines the `Question` class to store question text and answer.
- **quiz_brain.py**: Handles the quiz logic and keeps track of the user's score and progress.

## Requirements:
To run the project, you need the following Python packages:
- streamlit

You can install the required dependencies using `pip`:

```bash
pip install streamlit
```

## Running the Quiz App:
To run the quiz game app locally, use the following command:

```bash
streamlit run streamlit_app.py
```

## How the Quiz Works:
1. The user is presented with a true/false question.
2. They select an answer and click "Submit Answer."
3. The app will check if the answer is correct, update the score, and display the next question.
4. The quiz continues until all questions have been answered.
5. After completing the quiz, the user can see their final score and has the option to restart the quiz.

## Future Enhancements:
- Add a timer to each question.
- Implement a high score feature.
- Add more question categories (e.g., general knowledge, science, etc.).

## Contributing:
Feel free to contribute by opening issues or submitting pull requests for any improvements or bug fixes.

## License:
This project is licensed under the MIT License.
```
