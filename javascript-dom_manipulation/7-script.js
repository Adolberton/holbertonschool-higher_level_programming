list_movies = document.getElementById('list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
  if (!response.ok) {
    throw new Error('La requête a échoué');
  }
  return response.json();
  })
  .then(data => {
  data.results.forEach(movie => {
    newMovie = document.createElement('li');
    newMovie.textContent = movie.title;
    list_movies.appendChild(newMovie);
  });
  })
  .catch(error => console.error('Error:', error));
