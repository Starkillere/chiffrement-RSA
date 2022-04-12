const input = document.getElementById("password");
const checkbox = document.getElementById("box")
function afficherPassword() { 
    if (input.type === "password") { 
        input.type = "text"; 
    } 
    else { 
        input.type = "password"; 
    } 
}
checkbox.onclick = afficherPassword()