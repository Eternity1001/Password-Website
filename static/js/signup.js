const form = document.querySelector("#myForm");


function incorrect_password(){
  const password_status = document.getElementById("password_status");
   password_status.style.color = 'red';
   password_status.textContent = "Password doesn't match";
}

async function processFormLogic(data) {

  const password = data['password'];
  const confirm_password = data['confirm_password'];

  if (password !== confirm_password){
    incorrect_password();
    return false;
    
  } 
  try {
        const formData = {
          email: data['email'],
          username: data['username'],
          password: data['password'],
          confirm_password: data['confirm_password']
        }
        console.log("called")
        const response = await fetch("/verify-account", {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify(formData)
        });

        if (!response.ok){
          return false
        }

        const results = await response.json();
        if (results['error'] === "Password"){
            incorrect_password();
        }
        

      }
      catch (error) {
        console.error("Verification error:", error);
         return false;

      }

}

form.addEventListener("submit", async (event) => {
  event.preventDefault(); 

  const data = new FormData(form);
  const data_object = Object.fromEntries(data);


  const isValid = await processFormLogic(data_object);

  if (isValid) {
    console.log("called here")
    // form.submit();
  }
});