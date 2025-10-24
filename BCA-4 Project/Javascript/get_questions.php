<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "Quiz";

$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$numQuestions = isset($_GET['numQuestions']) ? intval($_GET['numQuestions']) : 10;

$sql = "SELECT question, option1, option2, option3, option4, answer FROM Questions ORDER BY RAND() LIMIT $numQuestions";
$result = $conn->query($sql);

$questions = [];
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $questions[] = $row;
    }
}

$conn->close();

header('Content-Type: application/json');
echo json_encode($questions);
?>