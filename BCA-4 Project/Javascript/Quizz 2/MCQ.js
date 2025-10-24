document.addEventListener('DOMContentLoaded', function() {
    const questionCount = parseInt(sessionStorage.getItem('questionCount'));
    const subject = sessionStorage.getItem('subject');

    if (isNaN(questionCount) || !subject) {
        alert("Questions not found. Please select a subject and question count.");
        window.location.href = "number of Questions.html";
        return;
    }

    const quizArea = document.getElementById('quiz-area');
    const questionNumberElement = document.getElementById('question-number');
    const questionTextElement = document.getElementById('question-text');
    const answerOptionsElement = document.getElementById('answer-options');
    const nextButton = document.getElementById('next-button');

    let currentQuestionIndex = 0;
    let userAnswers = [];
    let randomizedQuestions = [];

    // Construct the URL for the JSON file based on the subject.
    const jsonUrl = `https://raw.githubusercontent.com/HirvaJobanputra/Javascript-Quiz-/refs/heads/main/${subject}.json`; 

    // Fetch the JSON data.
    fetch(jsonUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(questions => {
            // Function to shuffle an array
            function shuffleArray(array) {
                for (let i = array.length - 1; i > 0; i--) {
                    const j = Math.floor(Math.random() * (i + 1));
                    [array[i], array[j]] = [array[j], array[i]];
                }
                return array;
            }

            // Randomly select questions based on question count.
            randomizedQuestions = shuffleArray(questions).slice(0, questionCount);

            function displayQuestion() {
                if (currentQuestionIndex < randomizedQuestions.length) {
                    const question = randomizedQuestions[currentQuestionIndex];
                    questionNumberElement.textContent = `Question ${currentQuestionIndex + 1}/${randomizedQuestions.length}`;
                    questionTextElement.textContent = question.question;

                    answerOptionsElement.innerHTML = ''; // Clear previous options
                    question.answers.forEach(answer => {
                        const button = document.createElement('button');
                        button.classList.add('answer-button');
                        button.textContent = answer;
                        button.addEventListener('click', () => selectAnswer(answer));
                        answerOptionsElement.appendChild(button);
                    });

                    nextButton.style.display = 'none'; // Hide next button initially
                } else {
                    showResults();
                }
            }

            function selectAnswer(selectedAnswer) {
                // Extract 'a', 'b', 'c', or 'd' from the selected answer.
                const selectedLetter = selectedAnswer.charAt(0);
                userAnswers[currentQuestionIndex] = selectedLetter;

                // Highlight selected answer and remove highlights from others
                const buttons = answerOptionsElement.querySelectorAll('.answer-button');
                buttons.forEach(button => {
                    if (button.textContent === selectedAnswer) {
                        button.style.backgroundColor = 'lightblue'; // Highlight selected
                    } else {
                        button.style.backgroundColor = 'rgba(255, 255, 255, 0.1)'; // Reset others
                    }
                });

                nextButton.style.display = 'block'; // Show next button
            }

            nextButton.addEventListener('click', () => {
                currentQuestionIndex++;
                displayQuestion();
            });

            function showResults() {
                let score = 0;
                randomizedQuestions.forEach((question, index) => {
                    if (userAnswers[index] === question.correctAnswer) {
                        score++;
                    }
                });

                quizArea.innerHTML = `<h2>Quiz Completed!</h2><p>Your Score: ${score}/${randomizedQuestions.length}</p>`;
                if (score === randomizedQuestions.length) {
                    quizArea.innerHTML += `<p>Perfect score! You are a genius!</p>`;
                } else if (score >= randomizedQuestions.length / 2) {
                    quizArea.innerHTML += `<p>Great Job!</p>`;
                } else {
                    quizArea.innerHTML += `<p>Better luck next time!</p>`;
                }
            }

            displayQuestion(); // Start the quiz
        })
        .catch(error => {
            console.error('Error fetching JSON:', error);
            alert('Failed to load questions. Please try again.');
            window.location.href = "index.html"; // send user back to start.
        });
});