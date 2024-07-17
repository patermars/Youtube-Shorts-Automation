const fileInput = document.querySelector('#image');

fileInput.addEventListener('change', () => {
    console.log('File selected:', fileInput.files[0]);
});

const generateBtn = document.getElementById('generate-btn');
generateBtn.addEventListener('click', (e) => {
    e.preventDefault();
    const heading = document.getElementById('heading').value;
    const comment = document.getElementById('comment').value;
    const imageFile = fileInput.files[0];

    if (!heading || !comment || !imageFile) {
        alert('Please fill in all fields and select an image.');
        return;
    }

    const formData = new FormData();
    formData.append('image', imageFile);
    formData.append('heading', heading);
    formData.append('comment', comment);

    // Example: Sending form data to a server (endpoint not provided)
    /*
    fetch('your-server-endpoint', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    */

    console.log('Generate button clicked!');
});
