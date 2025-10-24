<?php

    $servername="localhost";
    $username="root";
    $password="";
    $dbname="Quiz";

    $conn = new mysqli($servername,$username,$password,$dbname);
    if($conn->connect_error)
    {
        die("Connection failed: ".$conn->connect_error);
    }
    else{
        echo "Connection done";
    }

    $table="Questions";
    // $query="CREATE TABLE $table(
    //     id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    //     question VARCHAR(1000) NOT NULL,
    //     option1 VARCHAR(100) NOT NULL,
    //     option2 VARCHAR(100) NOT NULL,
    //     option3 VARCHAR(100) NOT NULL,
    //     option4 VARCHAR(100) NOT NULL,
    //     answer VARCHAR(100) NOT NULL
    // )AUTO_INCREMENT=101;";

    // $sql=mysqli_query($conn,$query);
    // if($sql){
    //     echo "Table $table is created";
    // }
    // else{
    //     echo "Table $table is not created";
    // }
    $questions = [
        ["What does AI stand for?", "Artificial Intelligence", "Automated Intelligence", "Augmented Intelligence", "Analytical Intelligence", "Artificial Intelligence"],
        ["Who is considered the 'father of AI'?", "Alan Turing", "John McCarthy", "Marvin Minsky", "Claude Shannon", "John McCarthy"],
        ["What is the Turing Test used for?", "Measuring AI performance", "Testing machine learning algorithms", "Evaluating AI's ability to mimic human intelligence", "Determining if a machine can think", "Evaluating AI's ability to mimic human intelligence"],
        ["What is machine learning?", "A type of AI", "A programming language", "A hardware component", "A statistical method", "A type of AI"],
        ["What is deep learning?", "A subset of machine learning", "A type of database", "A hardware architecture", "A programming paradigm", "A subset of machine learning"],
        ["Name a popular deep learning framework.", "Java", "Python", "TensorFlow", "C++", "TensorFlow"],
        ["What is a neural network?", "A type of algorithm", "A hardware component", "A programming language", "A data structure", "A type of algorithm"],
        ["What is supervised learning?", "Learning with labeled data", "Learning without data", "Learning with reinforcement", "Learning with unlabeled data", "Learning with labeled data"],
        ["What is unsupervised learning?", "Learning with unlabeled data", "Learning with labeled data", "Learning with reinforcement", "Learning with a teacher", "Learning with unlabeled data"],
        ["What is reinforcement learning?", "Learning through trial and error", "Learning with a teacher", "Learning with labeled data", "Learning with unlabeled data", "Learning through trial and error"],
        ["What is natural language processing (NLP)?", "AI related to text and speech", "AI related to images", "AI related to robotics", "AI related to games", "AI related to text and speech"],
        ["What is computer vision?", "AI related to images and videos", "AI related to text", "AI related to speech", "AI related to robotics", "AI related to images and videos"],
        ["What is a chatbot?", "A program that simulates human conversation", "A type of robot", "A machine learning algorithm", "A search engine", "A program that simulates human conversation"],
        ["What is an AI algorithm used for image recognition?", "Recurrent Neural Network (RNN)", "Convolutional Neural Network (CNN)", "Generative Adversarial Network (GAN)", "Linear Regression", "Convolutional Neural Network (CNN)"],
        ["What is an AI algorithm used for sequential data like text?", "Convolutional Neural Network (CNN)", "Recurrent Neural Network (RNN)", "Support Vector Machine (SVM)", "Decision Tree", "Recurrent Neural Network (RNN)"],
        ["What is a generative adversarial network (GAN)?", "A type of neural network", "A type of robot", "A type of database", "A type of programming language", "A type of neural network"],
        ["What is the difference between narrow/weak AI and general/strong AI?", "Narrow AI is specialized, general AI is human-level", "Narrow AI is weak, general AI is strong", "Narrow AI is fast, general AI is slow", "Narrow AI uses less data, general AI uses more data", "Narrow AI is specialized, general AI is human-level"],
        ["What are some ethical concerns surrounding AI?", "Job displacement, bias, privacy", "Cost, speed, accuracy", "Hardware limitations, software bugs", "Lack of funding, lack of research", "Job displacement, bias, privacy"],
        ["What is AI singularity?", "The hypothetical point where AI surpasses human intelligence", "The point where AI becomes widely used", "The point where AI is no longer useful", "The point where AI is regulated", "The hypothetical point where AI surpasses human intelligence"],
        ["What is the difference between AI and automation?", "AI involves decision making, automation follows pre-defined rules", "AI is faster, automation is slower", "AI is more expensive, automation is cheaper", "AI requires programming, automation doesn't", "AI involves decision making, automation follows pre-defined rules"],
        ["Which programming language is commonly used in AI development?", "Java", "Python", "C++", "JavaScript", "Python"],
        ["What is data mining in the context of AI?", "Extracting useful information from large datasets", "Storing data in a database", "Cleaning and preprocessing data", "Visualizing data", "Extracting useful information from large datasets"],
        ["What is the role of big data in AI development?", "Provides large datasets for training AI models", "Reduces the need for AI", "Makes AI development easier", "Is not important for AI development", "Provides large datasets for training AI models"],
        ["What is an expert system?", "An AI system that mimics the decision-making of a human expert", "A type of robot", "A machine learning algorithm", "A database system", "An AI system that mimics the decision-making of a human expert"],
        ["What is a knowledge base in AI?", "A repository of information used by an AI system", "A type of database", "A machine learning algorithm", "A programming language", "A repository of information used by an AI system"]
    ];

    foreach ($questions as $question) {
        $question_text = $question[0];
        $option1 = $question[1];
        $option2 = $question[2];
        $option3 = $question[3];
        $option4 = $question[4];
        $answer = $question[5];
    
    
        $stmt = $conn->prepare("CALL que_insert(?, ?, ?, ?, ?, ?)"); 
        $stmt->bind_param("ssssss", $question_text, $option1, $option2, $option3, $option4, $answer);
        $stmt->execute();
    
        if ($stmt->affected_rows > 0) {
            echo "New record created successfully<br>";
        } else {
            echo "Error: " . $stmt->error;
        }
    
        $stmt->close();
        
    }
    $conn->close();
?>