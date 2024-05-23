updateHeader = document.getElementById('update_header');
header = document.getElementsByTagName('header')[0];
updateHeader.addEventListener('click', () => {
  header.textContent = 'New Header!!!';
});
