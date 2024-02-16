document.addEventListener('DOMContentLoaded', function() {
    const newPostForm = document.querySelector('#new-post-form');

    newPostForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        const formData = new FormData(newPostForm); // Get form data
        const content = formData.get('content');

        fetch('/new_post', {
            method: 'POST',
            body: JSON.stringify({ content }),
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken // Assuming you have CSRF token setup
            }
        })
        .then(response => response.json())
        .then(data => {
            // Handle response from server, update UI as needed
        })
        .catch(error => console.error('Error:', error));
    });
});
