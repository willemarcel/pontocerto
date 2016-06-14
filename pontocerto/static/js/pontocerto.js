/* Project specific Javascript goes here. */
var data, geojson;

var map = L.map('map').setView([-12.9696, -38.4676], 13);
var transport = L.tileLayer('http://a.tile.thunderforest.com/transport/{z}/{x}/{y}.png', {
  attribution: 'Maps &copy; <a href="http://www.thunderforest.com">Thunderforest</a>, \
               Data &copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
});
var osm = L.tileLayer('http://a.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: 'Data &copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
});
transport.addTo(map);

var markerIcon = L.icon({
  iconUrl: 'static/js/images/marker-48.png',
  iconRetinaUrl: 'static/js/images/marker-48@2x.png',
  iconSize: [48, 48],
  iconAnchor: [24, 42],
  popupAnchor: [0, -30],
});

var grayIcon = L.icon({
  iconUrl: 'static/js/images/circle-gray-24@2x.png',
  iconRetinaUrl: 'static/js/images/gray-24@2x.png',
  iconSize: [33, 33],
  popupAnchor: [0, -12],
});

var redIcon = L.icon({
  iconUrl: 'static/js/images/circle-red-24@2x.png',
  iconRetinaUrl: 'static/js/images/circle-red-24@2x.png',
  iconSize: [33, 33],
  popupAnchor: [0, -12],
});

var yellowIcon = L.icon({
  iconUrl: 'static/js/images/circle-yellow-24@2x.png',
  iconRetinaUrl: 'static/js/images/circle-yellow-24@2x.png',
  iconSize: [33, 33],
  popupAnchor: [0, -12],
});

var greenIcon = L.icon({
  iconUrl: 'static/js/images/circle-green-24@2x.png',
  iconRetinaUrl: 'static/js/images/circle-green-24@2x.png',
  iconSize: [33, 33],
  popupAnchor: [0, -12],
});

var layerNaoAvaliado = L.layerGroup([]);
var layerCritica = L.layerGroup([]);
var layerAceitavel = L.layerGroup([]);
var layerFavoravel = L.layerGroup([]);

function resultado(avaliacao) {
    if (avaliacao == 'critica') {
        return '<span class="critica">Crítica</span>'
    }
    if (avaliacao == 'aceitavel') {
        return '<span class="aceitavel">Aceitável</span>'
    }
    if (avaliacao == 'favoravel') {
        return '<span class="favoravel">Favorável</span>'
    }
}

function popupSemAvaliacao(id) {
  return '<strong>Ponto ' + id + '</strong><p>Este ponto ainda não foi avaliado.</p>'
}

function popupContent(feature) {
  html = '<p><strong>Ponto ' + feature.id + '</strong></p>';
  html += '<p><strong>Avaliação Geral:</strong> ' + resultado(feature.properties.avaliacao.final) + '</p>';
  html += '<strong>Acesso:</strong> ' + resultado(feature.properties.avaliacao.acesso) + '<br>';
  html += '<strong>Abrigo:</strong> ' + resultado(feature.properties.avaliacao.abrigo) + '<br>';
  html += '<strong>Piso:</strong> ' + resultado(feature.properties.avaliacao.piso) + '<br>';
  html += '<strong>Rampa:</strong> ' + resultado(feature.properties.avaliacao.rampa) + '<br>';
  html += '<strong>Calçada:</strong> ' + resultado(feature.properties.avaliacao.calcada) + '<br>';
  html += '<strong>Plataforma:</strong> ' + resultado(feature.properties.avaliacao.plataforma) + '<br>';
  html += '<strong>Trânsito:</strong> ' + resultado(feature.properties.avaliacao.transito) + '<br>';
  html += '<strong>Equipamento:</strong> ' + resultado(feature.properties.avaliacao.equipamento) + '<br>';
  html += '<strong>Identificação:</strong> ' + resultado(feature.properties.avaliacao.identificacao) + '<br>';
  html += '<strong>Piso Tátil:</strong> ' + resultado(feature.properties.avaliacao.piso_tatil) + '<br>';
  html += '<strong>Logradouro:</strong> ' + resultado(feature.properties.avaliacao.logradouro) + '<br>';
  return html;
}

$.getJSON("core/pontos.geojson/?format=json", function (data) {
  var geojson = L.geoJson(data, {
    pointToLayer: function (feature, latlng) {
      return L.marker(latlng, {icon: grayIcon});
    },
  });

  var nao_avaliado = L.geoJson(data, {
    filter: function(feature, layer) {
        if (feature.properties.avaliacao == null) {
          return true;
        }
    },
    pointToLayer: function (feature, latlng) {
      return L.marker(latlng, {icon: grayIcon}).bindPopup(popupSemAvaliacao(feature.id));
    },
  });

  var critica = L.geoJson(data, {
    filter: function(feature, layer) {
        if (feature.properties.avaliacao != null && feature.properties.avaliacao.final == 'critica') {
          return true;
        }
    },
    pointToLayer: function (feature, latlng) {
      return L.marker(latlng, {icon: redIcon}).bindPopup(popupContent(feature));
    },
  });

  var aceitavel = L.geoJson(data, {
    filter: function(feature, layer) {
        if (feature.properties.avaliacao != null && feature.properties.avaliacao.final == 'aceitavel') {
          return true;
        }
    },
    pointToLayer: function (feature, latlng) {
      return L.marker(latlng, {icon: yellowIcon}).bindPopup(popupContent(feature));
    },
  });

  var favoravel = L.geoJson(data, {
    filter: function(feature, layer) {
        if (feature.properties.avaliacao != null && feature.properties.avaliacao.final == 'favoravel') {
          return true;
        }
    },
    pointToLayer: function (feature, latlng) {
      return L.marker(latlng, {icon: greenIcon}).bindPopup(popupContent(feature));
    },
  });
  nao_avaliado.addTo(layerNaoAvaliado);
  critica.addTo(layerCritica);
  aceitavel.addTo(layerAceitavel);
  favoravel.addTo(layerFavoravel);
});

layerNaoAvaliado.addTo(map);
layerCritica.addTo(map);
layerAceitavel.addTo(map);
layerFavoravel.addTo(map);

var baseMaps = {
  "OSM Transporte Público": transport,
  "OSM Padrão": osm,
};

var overlayMaps = {
  "Avaliação Favorável": layerFavoravel,
  "Avaliação Aceitável": layerAceitavel,
  "Avaliação Crítica": layerCritica,
  "Pontos ainda não avaliados": layerNaoAvaliado,
};

L.control.layers(baseMaps, overlayMaps, {collapsed: true}).addTo(map);
