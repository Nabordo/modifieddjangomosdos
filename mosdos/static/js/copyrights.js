// Get the current year
const currentYear = new Date().getFullYear();

// Find the element with id "copyRightsDate"
const copyRightsDateElement = document.getElementById("copyRightsDate");

// Set the inner text of the element to the current year
copyRightsDateElement.innerText = currentYear;

document.addEventListener('DOMContentLoaded', function() {
  var togglePassword = document.querySelector('.toggle-password');
  var passwordField = document.querySelector('#id_password');

  togglePassword.addEventListener('click', function() {
    var passwordFieldType = passwordField.getAttribute('type');

    if (passwordFieldType === 'password') {
      passwordField.setAttribute('type', 'text');
      togglePassword.classList.remove('fa-eye');
      togglePassword.classList.add('fa-eye-slash');
    } else {
      passwordField.setAttribute('type', 'password');
      togglePassword.classList.remove('fa-eye-slash');
      togglePassword.classList.add('fa-eye');
    }
  });
});
