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

// Adiciona evento de tecla Enter no campo de senha
document.addEventListener("DOMContentLoaded", function() {
    const passwordInput = document.getElementById("password");
    if (passwordInput) {
        passwordInput.addEventListener("keypress", function(event) {
            if (event.key === "Enter") {
                login(); // Chama a função de login
            }
        });
    }
});

function verificarLogin() {
    const estaLogado = localStorage.getItem("loggedIn") === "true";
    const loginBtn = document.getElementById("login-btn");
    const cadastroContainer = document.getElementById("cadastro-container");
    const logoutBtn = document.getElementById("logout-btn");

    if (estaLogado) {
        if (loginBtn) loginBtn.style.display = "none";
        if (cadastroContainer) cadastroContainer.style.display = "block";
        if (logoutBtn) logoutBtn.style.display = "block";
    }
}

function logout() {
    localStorage.removeItem("loggedIn");
    window.location.href = "home.html";
}

document.addEventListener("DOMContentLoaded", verificarLogin);
