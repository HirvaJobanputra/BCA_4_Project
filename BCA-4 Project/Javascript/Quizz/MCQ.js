document.addEventListener('DOMContentLoaded', function() {
    const questionNumberDisplay = document.getElementById('question-number');
    const questionTextDisplay = document.getElementById('question-text');
    const answerButtons = document.querySelectorAll('.answer-button');
    const nextButton = document.getElementById('next-button');
    const quizArea = document.getElementById('quiz-area');
    const timerDisplay = document.getElementById('timer');

    let currentQuestionIndex = 0;
    let score = 0;
    let selectedAnswer = null;
    let questions = [];
    let timeInterval;
    let timeLeft = 60;
    let answered = false;

    const urlParams = new URLSearchParams(window.location.search);
    const subject = urlParams.get('subject');
    const questionCount = parseInt(urlParams.get('questions')) || 10;

    async function loadQuestions(subject) {
        try {
            let url;
            if (subject === "ai") {
                url = "https://raw.githubusercontent.com/HirvaJobanputra/BCA_4/refs/heads/main/ai.json";
            } else if (subject === "ar") {
                url = "https://raw.githubusercontent.com/HirvaJobanputra/BCA_4/refs/heads/main/ar.json";
            } else if (subject === "gaming") {
                url = "https://raw.githubusercontent.com/HirvaJobanputra/BCA_4/refs/heads/main/gaming.json";
            } else {
                return null;
            }

            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            return data;
        } catch (error) {
            console.error("Error loading questions:", error);
            return null;
        }
    }

    function generateQuestions(allQuestions, count) {
        let selectedQuestions = [];
        let questionCopy = [...allQuestions];

        for (let i = 0; i < count; i++) {
            if (questionCopy.length === 0) {
                break;
            }
            const randomIndex = Math.floor(Math.random() * questionCopy.length);
            selectedQuestions.push(questionCopy[randomIndex]);
            questionCopy.splice(randomIndex, 1);
        }
        return selectedQuestions;
    }

    async function initQuiz() {
        const allQuestions = await loadQuestions(subject);
        if (allQuestions) {
            questions = generateQuestions(allQuestions, questionCount);
            displayQuestion();
        } else {
            quizArea.innerHTML = "<p>Failed to load questions.</p>";
        }
    }

    function displayQuestion() {
        if (currentQuestionIndex < questions.length) {
            const currentQuestion = questions[currentQuestionIndex];
            questionNumberDisplay.textContent = `Question ${currentQuestionIndex + 1} of ${questions.length}`;
            questionTextDisplay.textContent = currentQuestion.question;

            answerButtons.forEach((button, index) => {
                button.textContent = currentQuestion.answers[index];
                button.dataset.answer = String.fromCharCode(97 + index);
                button.disabled = false;
                button.classList.remove('correct', 'incorrect', 'selected');
            });

            selectedAnswer = null;
            nextButton.style.display = 'none';
            startTimer();
            answered = false;
        } else {
            endQuiz();
        }
    }

    function startTimer() {
        clearInterval(timeInterval);
        timeLeft = 60;
        updateTimerDisplay();

        timeInterval = setInterval(() => {
            timeLeft--;
            updateTimerDisplay();
            if (timeLeft <= 0) {
                clearInterval(timeInterval);
                if (!answered) {
                    if(questions[currentQuestionIndex]) { // Check if questions[currentQuestionIndex] is valid
                         checkAnswer(questions[currentQuestionIndex]);
                    }
                }
                nextQuestion();
            }
        }, 1000);
    }

    function updateTimerDisplay() {
        timerDisplay.textContent = `Time left: ${timeLeft} seconds`;
        if (timeLeft <= 10) {
            timerDisplay.style.color = 'red';
            timerDisplay.style.fontSize = '1.2em';
        } else {
            timerDisplay.style.color = '';
            timerDisplay.style.fontSize = '';
        }
    }

    function nextQuestion() {
        if (!answered && selectedAnswer) {
            if (questions[currentQuestionIndex - 1]) { // Check for valid question before calling checkAnswer
              checkAnswer(questions[currentQuestionIndex - 1]);
            }
        }
        currentQuestionIndex++;
        displayQuestion();
    }


    answerButtons.forEach(button => {
        button.addEventListener('click', () => {
            if (answered) return;

            answerButtons.forEach(btn => btn.classList.remove('selected')); // Remove previous selections

            selectedAnswer = button.dataset.answer;
            button.classList.add('selected');
            nextButton.style.display = 'block';

            const currentQuestion = questions[currentQuestionIndex]; // Capture the current question

             if(currentQuestion) {
                button.onclick = () => checkAnswer(currentQuestion); // Pass to checkAnswer
            }

        });
    });

    function checkAnswer(currentQuestion) { // Accept currentQuestion as a parameter
      console.log("checkAnswer() called!");

       if (!currentQuestion) { // Check if currentQuestion is valid
            console.error("currentQuestion is undefined in checkAnswer!");
            return; // Exit the function to prevent errors
        }

        const isCorrect = selectedAnswer === currentQuestion.answer;

        console.log(`selectedAnswer: ${selectedAnswer}, correctAnswer: ${currentQuestion.answer}, isCorrect: ${isCorrect}`);

        answerButtons.forEach(button => {
            button.disabled = true;
            if (button.dataset.answer === currentQuestion.answer) {
                button.classList.add('correct');
            } else if (button.dataset.answer === selectedAnswer) {
                button.classList.add('incorrect');
            }
        });

        if (isCorrect) {
            score++;
            console.log(`Score incremented! New score: ${score}`);
        }
        answered = true;
        clearInterval(timeInterval);
    }

    nextButton.addEventListener('click', () => {
        nextQuestion();
    });

    function endQuiz() {
        let message = "";
        if (score === questions.length) {
            message = "You're a quiz master! Perfect score!";
        } else if (score >= questions.length / 2) {
            message = "Great job! You did really well!";
        } else {
            message = "Nice try! You'll get them next time!";
        }
        quizArea.innerHTML = `<h2>Quiz Complete!</h2><p>Your score: ${score} out of ${questions.length}</p><p>${message}</p>`;
    }

    initQuiz();
});