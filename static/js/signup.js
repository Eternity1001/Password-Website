const form = document.querySelector("#myForm");

// The element is guaranteed to exist because of `defer`
form.addEventListener("input", (event) => {
  event.preventDefault(); // Stop native page refresh
  
  const data = new FormData(form);
  console.log(Object.fromEntries(data));
});