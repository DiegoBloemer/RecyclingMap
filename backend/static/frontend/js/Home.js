let map;

async function initMap() {
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  map = new Map(document.getElementById("map"), {
    center: { lat: -28.953497041630705, lng: -49.503713956383784 },
    zoom: 15,
    mapId: "MAP_DEMO_ID",
  });



// const forms = document.getElementById("localForm");

// forms.addEventListener("submit", (event) => {
//   event.preventDefault();
//   const formData = new FormData(forms);
//   const data = Object.fromEntries(formData.entries());
//   console.log(data);

//   const newLocationForMap = document.createElement("div");

//   // Adiciona a classe ao elemento
//   newLocationForMap.classList.add("newLocationForMap");

//   // Define o conteúdo do elemento
//   newLocationForMap.textContent = "Nova localização";

//   // Aplica estilos diretamente via JavaScript
//   newLocationForMap.style.backgroundColor = "#4286f5";
//   newLocationForMap.style.borderRadius = "8px";
//   newLocationForMap.style.color = "#ffffff";
//   newLocationForMap.style.fontSize = "14px";
//   newLocationForMap.style.padding = "10px 15px";
//   newLocationForMap.style.position = "relative";

//   new AdvancedMarkerElement({
//     map,
//     position: { lat: -28.953863171992705, lng: -49.50189008724842 },
//     content: newLocationForMap,
//   });
// });
}
initMap();
