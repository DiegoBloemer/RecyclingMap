async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  let map = new Map(document.getElementById("map"), {
    center: { lat: -28.953497041630705, lng: -49.503713956383784 },
    zoom: 15,
    mapId: "MAP_DEMO_ID",
  });

  let marcadores = [];

  // Função para limpar e atualizar os marcadores no mapa
  function atualizarMapa(pontos) {
    // Remove marcadores antigos
    marcadores.forEach((marcador) => marcador.setMap(null));
    marcadores = [];

    // Adiciona novos marcadores
    pontos.forEach((ponto) => {
      const marcador = new google.maps.Marker({
        position: { lat: parseFloat(ponto.latitude), lng: parseFloat(ponto.longitude) },
        map: map,
        title: ponto.nome,
      });

      let imagensHtml = "";
      if (ponto.imagens.length > 0) {
        ponto.imagens.forEach((url) => {
          imagensHtml += `<img src="${url}" alt="Imagem de ${ponto.nome}" style="width: 100px; height: auto; margin: 5px;">`;
        });
      } else {
        imagensHtml = "<p>Sem imagens disponíveis.</p>";
      }

      const infoWindow = new google.maps.InfoWindow({
        content: `
          <h3>${ponto.nome}</h3>
          <p>${ponto.endereco}</p>
          <p>Tipo de Resíduo: ${ponto.tipo_residuo}</p>
          <div style="display: flex; flex-wrap: wrap;">${imagensHtml}</div>
        `,
      });

      marcador.addListener("click", () => {
        infoWindow.open(map, marcador);
      });

      marcadores.push(marcador);
    });
  }

  // Inicializar o mapa com todos os pontos
  fetch("/pontos/")
    .then((response) => response.json())
    .then((data) => atualizarMapa(data))
    .catch((error) => console.error("Erro ao carregar os pontos:", error));

  // Capturar o evento de busca e atualizar os marcadores
  document.querySelector(".search-bar .input").addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
      const termoBusca = event.target.value;

      // Faz a requisição para a API de busca
      fetch(`/buscar_pontos/?search=${encodeURIComponent(termoBusca)}`)
        .then((response) => response.json())
        .then((data) => atualizarMapa(data))
        .catch((error) => console.error("Erro ao buscar pontos:", error));
    }
  });
}

initMap();
