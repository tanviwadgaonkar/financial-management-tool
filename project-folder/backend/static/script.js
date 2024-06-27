// static/js/script.js

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded');

    // Example: Show an alert when a form is submitted
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent actual form submission for demonstration
            alert('Form submitted!');
            // Add your form submission logic here
        });
    }

    // Example: Toggle visibility of an element
    const toggleButton = document.querySelector('.toggle-btn');
    const toggleElement = document.querySelector('.toggle-element');
    if (toggleButton && toggleElement) {
        toggleButton.addEventListener('click', function() {
            if (toggleElement.style.display === 'none') {
                toggleElement.style.display = 'block';
            } else {
                toggleElement.style.display = 'none';
            }
        });
    }

    // Example: Fetch and display user data (mock example)
    const userDataButton = document.querySelector('.fetch-user-data-btn');
    if (userDataButton) {
        userDataButton.addEventListener('click', function() {
            // Replace this with an actual fetch request
            const userData = {
                name: 'John Doe',
                email: 'john.doe@example.com'
            };
            displayUserData(userData);
        });
    }
});

function displayUserData(userData) {
    const userDataContainer = document.querySelector('.user-data-container');
    if (userDataContainer) {
        userDataContainer.innerHTML = `
            <p>Name: ${userData.name}</p>
            <p>Email: ${userData.email}</p>
        `;
    }
}
