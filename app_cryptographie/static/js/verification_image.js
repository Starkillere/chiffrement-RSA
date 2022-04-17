var fileName = document.getElementById('images');
var bout = document.getElementById('Cacher');
var bout2 = document.getElementById('popop')
function verifier() {
    if (fileName.value.length === 0) {
        alert("Vous devez mettre une image !");
        bout.type = 'button';
        bout2.style.display = 'none';
    }
    else {
        bout.type =  'submit';
        bout2.style.display = 'block';
    }
}
