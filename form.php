<?php

if (isset($_POST['submit'])) {
    $to = "contact@chainimpact.io";
    $subject = $_POST['name'];
    $message = getRequestURI();
    $from = "contact@chainimpact.io";
    $headers = "From:" . $from;

    if (mail($to, $subject, $message, $headers)) {
        echo "Mail Sent.";
    }
    else {
        echo "failed";
    }
}

?>
