<?php
    $servername="localhost";
    $username="root";
    $password="";

    $conn = new mysqli($servername, $username, $password);
    if($conn->connect_error)
    {
        die("Connection failed: ".$conn->connect_error);
    }
    else{
        echo "Connection done";
    }

    $dbname="Quiz";
    $query="CREATE DATABASE $dbname";
    $sql=mysqli_query($conn,$query);
    if($sql){
        echo "Database $dbname is created";
    }
    else{
        echo "Database $dbname is not created";
    }
?>