const currentYear = new Date().getFullYear();
const copyRightsDateElement = document.getElementById("copyRightsDate");
copyRightsDateElement.innerText = currentYear;

(function () {
        'use strict';
        // Fetch the form element
        const form = document.getElementById('id_basic_information_form');
        const saveButton = document.getElementById('id_basic_information_save');

        // Add event listener to the save button's click event
        form.addEventListener('click', function (event) {
            // Check if the form is valid
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            } else {
                // Submit the form
                form.submit();
            }

            // Add Bootstrap's was-validated class to show validation feedback
            form.classList.add('was-validated');
        }, false);
    })();
