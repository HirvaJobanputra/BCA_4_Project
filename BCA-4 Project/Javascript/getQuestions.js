// Add classes to the setup elements
document.querySelector('h2').classList.add('setup-section');
document.querySelector('.button-container').classList.add('setup-section');
document.getElementById('question-container').classList.add('question-section');

let score = 0; // Initialize score variable

function startQuiz(numQuestions) {
    // Hide setup elements
    document.querySelectorAll('.setup-section').forEach(element => {
        element.style.display = 'none';
    });

    // Show question container
    document.querySelector('.question-section').style.display = 'block';

    fetch(`get_questions.php?numQuestions=${numQuestions}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(questions => {
            displayQuestions(questions);
        })
        .catch(error => {
            console.error('Error fetching or parsing questions:', error);
            document.getElementById('question-container').innerHTML = '<h2>Error loading questions. Please try again.</h2>';
        });
}

function displayQuestions(questions) {
    let currentQuestionIndex = 0;
    const questionContainer = document.getElementById('question-container');

    function showNextQuestion() {
        if (currentQuestionIndex < questions.length) {
            const question = questions[currentQuestionIndex];
            questionContainer.innerHTML = `
                <h2>${question.question}</h2>
                <div id="answer-options">
                    <button class="option-button" data-answer="${question.option1}">${question.option1}</button>
                    <button class="option-button" data-answer="${question.option2}">${question.option2}</button>
                    <button class="option-button" data-answer="${question.option3}">${question.option3}</button>
                    <button class="option-button" data-answer="${question.option4}">${question.option4}</button>
                </div>
            `;

            // Handle answer selection
            document.querySelectorAll('.option-button').forEach(button => {
                button.addEventListener('click', () => {
                    const selectedAnswer = button.dataset.answer;
                    if (selectedAnswer === question.answer) {
                        score += 10; // Increment score for correct answer
                        console.log('Correct!');
                    } else {
                        console.log('Incorrect!');
                    }
                    currentQuestionIndex++; // Move to the next question
                    showNextQuestion(); // Display the next question
                });
            });
        } else {
            questionContainer.innerHTML = `<h2>Quiz Completed! Your score is: ${score}</h2>`;
        }
    }

    showNextQuestion();
}

document.querySelectorAll('.question-button').forEach(button => {
    button.addEventListener('click', () => {
        const numQuestions = parseInt(button.textContent);
        startQuiz(numQuestions);
    });
});