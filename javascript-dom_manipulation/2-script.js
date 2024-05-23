const redHeader = document.getElementById('red_header')
redHeader.addEventListener('click', () => {
  const header = document.querySelector('header');
  header.classList.add('red');
});
