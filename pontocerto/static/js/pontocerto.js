/* Project specific Javascript goes here. */
var data, geojson;
var map = L.map('map').setView([-12.9696, -38.4676], 13);
var mapTiles = L.tileLayer('http://a.tile.thunderforest.com/transport/{z}/{x}/{y}.png', {
  attribution: 'Maps &copy; <a href="http://www.thunderforest.com">Thunderforest</a>, \
               Data &copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
});
mapTiles.addTo(map);

var markerIcon = L.icon({
  iconUrl: 'static/js/images/marker-48.png',
  iconRetinaUrl: 'static/js/images/marker-48@2x.png',
  iconSize: [48, 48],
  iconAnchor: [24, 42],
  popupAnchor: [0, -30],
});

var grayIcon = L.icon({
  iconUrl: 'static/js/images/gray-24.png',
  iconRetinaUrl: 'static/js/images/gray-24@2x.png',
  iconSize: [15, 15],
  popupAnchor: [0, -8],
});

var redIcon = L.icon({
  iconUrl: 'static/js/images/red-24.png',
  iconRetinaUrl: 'static/js/images/red-24@2x.png',
  iconSize: [15, 15],
  popupAnchor: [0, -8],
});

var yellowIcon = L.icon({
  iconUrl: 'static/js/images/yellow-24.png',
  iconRetinaUrl: 'static/js/images/yellow-24@2x.png',
  iconSize: [15, 15],
  popupAnchor: [0, -8],
});

var greenIcon = L.icon({
  iconUrl: 'static/js/images/green-24.png',
  iconRetinaUrl: 'static/js/images/green-24@2x.png',
  iconSize: [15, 15],
  popupAnchor: [0, -8],
});

function popupContent(id) {
  return '<strong>Ponto ' + id + '</strong>'
}

$.getJSON("core/pontos.geojson/?format=json", function (data) {
  var geojson = L.geoJson(data, {
    pointToLayer: function (feature, latlng) {
      return L.marker(latlng, {icon: grayIcon}).bindPopup(popupContent(feature.id));
    },
  });
  
  var nao_avaliado = L.geoJson(data, {
    filter: function(feature, layer) {
        if (feature.properties.avaliacao == null) {
          return true;
        }
    },
    pointToLayer: function (feature, latlng) {
      return L.marker(latlng, {icon: grayIcon}).bindPopup(popupContent(feature.id));
    },
  });
  
  var critica = L.geoJson(data, {
    filter: function(feature, layer) {
        if (feature.properties.avaliacao != null && feature.properties.avaliacao.final == 'critica') {
          return true;
        }
    },
    pointToLayer: function (feature, latlng) {
      return L.marker(latlng, {icon: redIcon}).bindPopup(popupContent(feature.id));
    },
  });
  
  var aceitavel = L.geoJson(data, {
    filter: function(feature, layer) {
        if (feature.properties.avaliacao != null && feature.properties.avaliacao.final == 'aceitavel') {
          return true;
        }
    },
    pointToLayer: function (feature, latlng) {
      return L.marker(latlng, {icon: yellowIcon}).bindPopup(popupContent(feature.id));
    },
  });
  
  var favoravel = L.geoJson(data, {
    filter: function(feature, layer) {
        if (feature.properties.avaliacao != null && feature.properties.avaliacao.final == 'favoravel') {
          return true;
        }
    },
    pointToLayer: function (feature, latlng) {
      return L.marker(latlng, {icon: greenIcon}).bindPopup(popupContent(feature.id));
    },
  });
  nao_avaliado.addTo(map);
  critica.addTo(map);
  aceitavel.addTo(map);
  favoravel.addTo(map);
});
