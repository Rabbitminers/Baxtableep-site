const postData = () => {
    const form = document.getElementById('form') as HTMLFormElement;
    const formData = new FormData(form);
  
    fetch('/submit', {
      method: 'POST',
      body: formData
    })
      .then(response => {
        if (response.ok) {
          response.text().then(text => {
            alert(text)
            const message = document.createElement('div');
            message.textContent = text;
            document.body.appendChild(message);
          });
          form.reset();
        } else {
          console.error(response.body);
          alert('Submission failed.');
        }
      })
      .catch(error => {
        console.error(error.body);
        alert('Submission failed: ' + error);
      });
  };
  