<?php
    if($SERVER["REQUEST_METHOD"]=="POST"){
        $email = $_POST["email"];
        $username = $_POST["username"];
    $password = $_POST["password"];

    setcookie("email",$email,time()+(10 * 365 * 24 * 60 * 60));
    setcookie("username",$username,time()+(10 * 365 * 24 * 60 * 60));
    setcookie("password",$password,time()+(10 * 365 * 24 * 60 * 60));
    exit();
    }   
?>
