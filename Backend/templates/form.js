function uploadFile() {
    const fileInput = document.getElementById('file');
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('file', file);

    fetch('/contacts', {
      method: 'POST',
      body: formData
    })
    .then(response => {
      if (response.ok) {
        console.log('File uploaded successfully');
      } else {
        console.error('Error uploading file');
      }
    })
    .catch(error => {
      console.error('Error uploading file', error);
    });
  }


// var input = document.querySelector('input[type="file"]')

// var data = new FormData()
// for (const file of input.files) {
//   data.append('files',file,file.name)
// }

// fetch('/avatars', {
//   method: 'POST',
//   body: data
// })



// const myInput = document.getElementById('my-input');

// Later, perhaps in a form 'submit' handler or the input's 'change' handler:
// fetch('https://example.com/some_endpoint', {
//   method: 'POST',
//   body: myInput.files[0],
// });
