
function mostrarSenha() {
    var inputPass = document.getElementById('password'); 
    var btnShowPass = document.getElementById('btn-senha');

    if (inputPass.type === 'password') {
        inputPass.type = 'text';
        btnShowPass.classList.replace('bi-eye-slash', 'bi-eye');
    } else {
        inputPass.type = 'password';
        btnShowPass.classList.replace('bi-eye', 'bi-eye-slash');
    }
}

function login() {
    const user = document.getElementById("username").value;
    const pass = document.getElementById("password").value;

    if (user === "admin" && pass === "admin") {
        localStorage.setItem("loggedIn", "true");
        window.location.href = "home.html";
    } else {
        document.getElementById("error-msg").style.display = "block";
    }
}
