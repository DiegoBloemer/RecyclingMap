let map;

async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  map = new Map(document.getElementById("map"), {
    center: { lat: -28.953497041630705, lng: -49.503713956383784 },
    zoom: 15,
    mapId: "MAP_DEMO_ID",
  });



  fetch("/pontos/")
  .then((response) => response.json())
  .then((data) => {
      data.forEach((ponto) => {
          const marker = new google.maps.Marker({
              position: { lat: parseFloat(ponto.latitude), lng: parseFloat(ponto.longitude) },
              map: map,
              title: ponto.nome,
          });

          // Opcional: Adicionar uma janela de informações
          const infoWindow = new google.maps.InfoWindow({
              content: `
                  <h3>${ponto.nome}</h3>
                  <p>${ponto.endereco}</p>
                  <p>Tipo de Resíduo: ${ponto.tipo_residuo}</p>
              `,
          });

          marker.addListener("click", () => {
              infoWindow.open(map, marker);
          });
      });
  })
  .catch((error) => console.error("Erro ao carregar os pontos:", error));
}
initMap();
