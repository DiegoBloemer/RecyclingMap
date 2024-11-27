// Função para abrir o modal de Usuário
function UserModal() {
  const userModal = document.getElementById("userModal");
  userModal.style.display = "flex"; // Exibe o modal
  // Quando clicar fora, fecha o modal
  window.onclick = function (event) {
    if (event.target === userModal) {
      userModal.style.display = "none";
    }
  };
}

// Função para abrir o modal de Local
function LocalAddModal() {
  const localAddModal = document.getElementById("LocalAddModal");
  localAddModal.style.display = "flex "; // Exibe o modal
  // Quando clicar fora, fecha o modal
  window.onclick = function (event) {
    if (event.target === localAddModal) {
      localAddModal.style.display = "none";
      clearLocalForm(); // Limpa os dados do formulário
    }
  };
}


function clearLocalForm() {
  const form = document.getElementById("localForm");
  form.reset(); // Limpa os campos do formulário
}