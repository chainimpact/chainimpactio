<?php

if (isset($_POST['submit'])) {
    $to = $_POST['email'];
    $subject = $_POST['name'];
    $message = getRequestURI();
    $from = "zenphoto@example.com";
    $headers = "From:" . $from;

    if (mail($to, $subject, $message, $headers)) {
        echo "Mail Sent.";
    }
    else {
        echo "failed";
    }
}

?>
