'use strict';
// map
const map = L.map('map', {tap: false});
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60, 24], 7);


// global variables
//const apiUrl = 'http://127.0.0.1:5000/';

// icons:
const activeIcon = L.divIcon({className: 'active-icon'});
const passiveIcon = L.divIcon({className: 'passive-icon'});

//form for player name

document.querySelector('#player-form').addEventListener('submit', function (evt) {
  evt.preventDefault();
  const playerName = document.querySelector('#player-input').value;
  document.getElementById('replace-name').innerHTML = `<b>${playerName}</b>`;
  document.getElementById('current-airport').innerHTML = `Helsinki-Vantaa Airport`
  document.getElementById('current-city').innerHTML = `Helsinki`
  document.getElementById('current-country').innerHTML = `Finland`
  document.getElementById('current-temperature') .innerHTML = `Temperature: 2°C`
  document.getElementById('current-weather-condition').innerHTML = `Clouds`
  document.getElementById('current-wind-speed').innerHTML = `Wind: 5m/s`
  document.querySelector('#player-modal').classList.add('hide');
});

//function to fetch data from API
async function getData(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error('Invalid server input')
  const data = await response.json();
  return data
}

async function gameSetup() {
  try {
    const gameData = await getData('testdata/bigAirports.json');
    console.log(gameData);

    for(let airport of gameData.location) {
      const marker = L.marker([airport.latitude, airport.longitude]).addTo(map);
      if (airport.active) {
        marker.bindPopup(`Current location: <b>${airport.name}</b>, ${airport.country}`);
        marker.openPopup();
        marker.setIcon(activeIcon);
      }
      else {
        marker.setIcon(passiveIcon);
        const popupContent = document.createElement('div');
        popupContent.classList.add('pop-up')
        const content = document.createElement('p');
        content.innerHTML = `<b>${airport.name}</b>, ${airport.country}`;
        popupContent.append(content);
        const flyToBtn = document.createElement('button');
        flyToBtn.classList.add('button');
        flyToBtn.classList.add('travelBtn');
        flyToBtn.innerHTML = 'Travel';
        popupContent.classList.add('pop-up')
        popupContent.append(flyToBtn);
        marker.bindPopup(popupContent);
      }
    }
  } catch (error) {
    console.log(error);
  }
}


gameSetup()