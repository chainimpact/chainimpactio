<?php
if(isset($_POST['submit'])){
    $to = "contact@chainimpact.io";
    $from = $_POST['email'];
    $first_name = $_POST['name'];
    $subject = "Contact ChainImapact";
    $message = $name . "\n\n" . $_POST['message'];

    $headers = "From:" . $from;
    mail($to,$subject,$message,$headers);
    }
?>
