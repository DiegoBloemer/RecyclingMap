// Abre/Fecha o modal
function toggleModal() {
    const modal = document.getElementById("userModal");
    if (modal.style.display === "flex") {
      modal.style.display = "none";
    } else {
      modal.style.display = "flex";
    }
  }
  
  // Fecha o modal ao clicar fora dele
  window.onclick = function (event) {
    const modal = document.getElementById("userModal");
    if (event.target === modal) {
      modal.style.display = "none";
    }
  };