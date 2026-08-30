const form = document.querySelector("#myForm");

function processFormLogic(data) {

  const password = data['password'];
  const confirm_password = data['confirm_password'];

  if (password == confirm_password){
    return true;
  }
  return false;


}

form.addEventListener("submit", (event) => {
  event.preventDefault(); // Pause native submit

  // Run function first
  const data = new FormData(form)
  const data_object = Object.fromEntries(data)

  if (processFormLogic(data_object)){
      form.submit();
  } else {
    const password_status = document.getElementById("password_status");
    password_status.style.color = 'red';
    password_status.textContent = "Password doesn't match";
  }
});