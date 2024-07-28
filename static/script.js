document.getElementById('generate-btn').addEventListener('click', function(event) {
    event.preventDefault();
    const form = document.getElementById('automation-form');
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
        body: formData
    })
    .then(response => {
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        const logTextarea = document.getElementById('progress-log');

        function read() {
            reader.read().then(({ done, value }) => {
                if (done) {
                    return;
                }
                logTextarea.value += decoder.decode(value);
                logTextarea.scrollTop = logTextarea.scrollHeight;
                read();
            });
        }

        read();
    })
    .catch(error => console.error('Error:', error));
});