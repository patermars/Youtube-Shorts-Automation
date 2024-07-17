const generateBtn = document.getElementById('generate-btn');
generateBtn.addEventListener('click', (e) => {
    e.preventDefault();
    const heading = document.getElementById('heading').value;
    const comment = document.getElementById('comment').value;
    const imageFile = document.getElementById('image').files[0];

    if (!heading || !comment || !imageFile) {
        alert('Please fill in all fields and select an image.');
        return;
    }

    const formData = new FormData();
    formData.append('image', imageFile);
    formData.append('heading', heading);
    formData.append('comment', comment);

    fetch('/generate', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert(data.message);
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Error generating video. Please try again.');
    });

    console.log('Generate button clicked!');
});
