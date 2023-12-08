function checkCredentials() {
  // Test credentials
  const testUsername = 'admin';
  const testPassword = '123';

  // Get user input
  const usernameInput = document.getElementById('username').value;
  const passwordInput = document.getElementById('password').value;

  // Check if the entered credentials match the test credentials
  if (usernameInput === testUsername && passwordInput === testPassword) {
    document.getElementById("loginStatus").textContent = '';
    document.getElementById('username').value = '';
    document.getElementById('password').value = '';
    window.location.href = 'https://webkia-1-s1046819.deta.app/contact/list';
  } else {
    document.getElementById("loginStatus").textContent =
            "Usuario o contraseña incorrectos. Por favor, intenta de nuevo.";
  }
}