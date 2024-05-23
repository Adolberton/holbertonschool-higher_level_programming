fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => {
    if (!response.ok) {
      throw new Error('La requête a échoué');
    }
    return response.json();
  })
  .then(data => {
    const hello = data.hello;
    document.getElementById('hello').textContent = hello;
  })
  .catch(error => console.error('Error:', error));
