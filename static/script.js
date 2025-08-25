const scrollContainer = document.getElementById('scrollContainer');
const scrollLeftBtn = document.getElementById('scrollLeft');
const scrollRightBtn = document.getElementById('scrollRight');

scrollLeftBtn.addEventListener('click', () => {
  scrollContainer.scrollBy({ left: -260, behavior: 'smooth' });
});

scrollRightBtn.addEventListener('click', () => {
  scrollContainer.scrollBy({ left: 260, behavior: 'smooth' });
});
