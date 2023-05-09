const form = document.getElementById('upload-form');
const status = document.getElementById('status');

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const response = await fetch('/check-virus', { method: 'POST', body: formData });
  const result = await response.json();
  status.innerText = result.message;
});