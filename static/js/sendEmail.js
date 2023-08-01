// This file has been entirely copied from the Code Institute course
// It links the contact form to the emailjs services

function sendEmail(contactForm) {
    emailjs.send("service_mj1syoq", "template_iaa3sqx", {
        from_name: contactForm.first_name.value,
        from_email: contactForm.email.value,
        message: contactForm.message.value,
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
}