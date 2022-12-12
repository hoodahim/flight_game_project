'use strict';

// // // // // // // // // // // //
// Map:                          //
// // // // // // // // // // // //

const map = L.map('map', {tap: false});
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60, 24], 7);


// // // // // // // // // // // //
// Global variables:             //
// // // // // // // // // // // //

const apiUrl = 'http://127.0.0.1:5000/';
let playerName;
const activeIcon = L.divIcon({className: 'active-icon'});
const passiveIcon = L.divIcon({className: 'passive-icon'});
let score = 0;
let travelled_distance = 0;
let co2_consumed = 0;
let co2_budget = 2000;
let london = Boolean(true);
let caparica = Boolean(true);
let prague = Boolean(true);
let ibiza = Boolean(true);
let reykjavik = Boolean(true);
let budapest = Boolean(true);
let rainy = Boolean(true);
let windy = Boolean(true);
let cloudy = Boolean(true);
let sunny = Boolean(true);
let snows = Boolean(true);
let endOfGame = Boolean(false);


// // // // // // // // // // // //
// EventListener for username:   //
// // // // // // // // // // // //
// Displays chosen name and hides modal
// Calls function rule, which displays the rules to output field
// Calls async function gameSetup

document.querySelector('#player-form').addEventListener('submit', function (evt) {
  evt.preventDefault();
  playerName = document.querySelector('#player-input').value;
  document.getElementById('replace-name').innerHTML = `<b>${playerName}</b>`;
  document.querySelector('#player-modal').classList.add('hide');
  rule();
  gameSetup(`${apiUrl}new_game?loc=EFHK`);
});


// // // // // // // // // // // //
// Setting up the game:          //
// // // // // // // // // // // //
// Called by eventListener, parameter: url
// Communication with python, provides current location
// Response is provided in a form of json data by python
// Calls function updateWeather, which displays the current weather of the current location
// Calls function updateLocation, which the current location
// Calls function addDestination, which appends the markers to the map

async function gameSetup(url) {
  try {
    const response = await fetch(url);
    const data = await response.json();
    updateWeather(data[0]);
    updateLocation(data[0]);
    await addDestination(data);
      } catch (error) {
    console.log('Error1');
  }
  }


// // // // // // // // // // // // // // //
// Function for chosen new locations:     //
// // // // // // // // // // // // // // //
// Called by async function addDestination, parameter: url of new location and the data fetched previous round
// Allows players to travel while game is not over
// Empties previous outputs
// Communicates and fetches data based on new location with python
// Calls function updateState, which updates CO2 budget, emission and distance
// Calls function updateLocation, which the current location
// Calls function addDestination, which appends the markers to the map
// Calls function updateWeather, which displays the current weather of the current location
// Calls function goalChecker, which matches data with goals

async function flyTo(url, previous_data) {
  if (!endOfGame) {
    document.querySelector('.status-box').innerHTML = '';
    document.querySelector('.weather-box').innerHTML = '';
    document.querySelector('.text-box').innerHTML = '';
    document.querySelector('.order-box').innerHTML = '';
    updateState(previous_data);
    updateLocation(previous_data);
    try {
      const response = await fetch(url);
      const data = await response.json();
      await addDestination(data);
      updateWeather(data[0]);
      goalChecker(data[0]);
    } catch (error) {
      console.log('Error 2');
    }
  }
}


// // // // // // // // // // // // // // // // // // // //
// Function to print the rules to output field:          //
// // // // // // // // // // // // // // // // // // // //
// Called by eventListener (from modal)
// Displays rules to output

function rule() {
  document.querySelector('.status-box').innerHTML = `Welcome, ${playerName}! Let's select your first destination!`;
  document.querySelector('.text-box').innerHTML = `You have had this bucket list for a while now and it's time to put things finally into motion!<br>
    - You wish to visit 5 + 1 secret locations and reach 5 weather targets in Europe.<br>
    - Each secret location has an assigned weather goal, they are paired the same way as they are listed.<br>
    - I ask you kindly to take into consideration sustainability. I will be your conscience and not allow you to travel further if CO2 emission reaches 2 tonnes.<br>
    The scoring system works the following way: 3000 points are needed to win.<br>
    - Guessed secret location with its assigned weather target: +1000 points<br>
    - Reached weather target, but not at the secret location: +500 points<br>
    - Guessed secret location without weather target: +300 points<br>
    - Guessed "Easter Egg" location: +1000 points<br>`
}


// // // // // // // // // // // // // // // // // // // // // // // //
// Function to add the map markers based to current location:        //
// // // // // // // // // // // // // // // // // // // // // // // //
// Called by functions gameSetup and flyTo, parameter: data of new, current location
// Appends the markers to the map and displays popups
// Calls function flyTo when Travel button is clicked

async function addDestination(data) {
  for (let airport of data) {
    const marker = L.marker([airport.latitude, airport.longitude]).addTo(map);
      if (airport.active) {
        marker.bindPopup(`Current location: <b>${airport.name}</b><br>${airport.location}, ${airport.country}`);
        marker.openPopup();
        marker.setIcon(activeIcon);
      } else {
        marker.setIcon(passiveIcon);
        const popupContent = document.createElement('div');
        popupContent.classList.add('pop-up');
        const content = document.createElement('p');
        content.innerHTML = `<b>${airport.name}</b><br>${airport.location}, ${airport.country}`;
        popupContent.append(content);
        const flyToBtn = document.createElement('button');
        flyToBtn.classList.add('button');
        flyToBtn.classList.add('travelBtn');
        flyToBtn.innerHTML = 'Travel';
        popupContent.classList.add('pop-up')
        popupContent.append(flyToBtn);
        marker.bindPopup(popupContent);
        flyToBtn.addEventListener('click', function () {
          flyTo(`${apiUrl}fly_to?new_loc=${airport.ident}`, airport);
        })
      }
  }
}


// // // // // // // // // // // // // // //
// Function to update weather row:        //
// // // // // // // // // // // // // // //
// Called by functions gameSetup and flyTo, parameter: data of current location
// Updates displayed current weather

function updateWeather(data) {
    document.getElementById('current-weather-condition').innerHTML = data.weather.main;
    document.getElementById('current-temperature').innerHTML = `Temperature: ${data.weather.temp}°C`;
    document.getElementById('current-wind-speed').innerHTML = `Wind: ${data.weather.wind}m/s`;
}


// // // // // // // // // // // // // //
// Function to update location row:    //
// // // // // // // // // // // // // //
// Called by functions gameSetup and flyTo, parameter: data of current location
// Updates displayed current location

function updateLocation(data) {
    document.getElementById('current-airport').innerHTML = data.name;
    document.getElementById('current-city').innerHTML = data.location;
    document.getElementById('current-country').innerHTML = data.country;
}


// // // // // // // // // // // // // // // // // // // // // // // // // //
// Function to update and display CO2 emission and distance rows:          //
// // // // // // // // // // // // // // // // // // // // // // // // // //
// Called by async function flyTo, parameter: previous data, which contains CO2, distance generated during travel
// Updates displayed CO2 values and distance

function updateState(data) {
  co2_consumed += data.co2_consumption;
  co2_budget -= data.co2_consumption;
  travelled_distance += data.distance;
  document.getElementById('current-co2-consumed').innerHTML = `CO2 generated: ${co2_consumed}kg`;
  document.getElementById('current-co2-available').innerHTML = `Available CO2: ${co2_budget}kg`;
  document.getElementById('current-odometer').innerHTML = `Travelled distance: ${travelled_distance}km`;
}


// // // // // // // // // // // // // // // // // // // // // // // //
// Function to check if any of the goals are reached:                //
// // // // // // // // // // // // // // // // // // // // // // // //
// Call by async function flyTo, parameter: data of new, current location
// Compares it to both location and weather goals and displays output if new goal reached
// Turns weather boolean to false, so score cannot be given again for the same goal and hides the box
// Calls function ....Printer, if location is reached to display fun fact to output field
// Calls function goal...., which hides the weather box and changes boolean to avoid score given more than one for same weather
// Calls function updateScore, which adds addition score to existing and displays it

function goalChecker(data) {
  // Budapest
  if (data.ident === 'LHBP' && budapest) {
    document.querySelector('.status-box').innerHTML = `You guessed the Easter Egg location: +1000points.`;
    updateScore(1000);
    budapestPrinter();
  }
  // London & Rain
  if (london || rainy) {
    if (london && rainy && (data.weather.main === 'Rain' || data.weather.main === 'Drizzle') && (data.ident === 'EGKK' || data.ident === 'EGSS' || data.ident === 'EGGW' || data.ident === 'EGLL')) {
      document.querySelector('.status-box').innerHTML = `You guessed the first secret location and it rains: +1000points.`;
      updateScore(1000);
      londonPrinter();
      goalRainy();
    }
    else if (london && (data.ident === 'EGKK' || data.ident === 'EGSS' || data.ident === 'EGGW' || data.ident === 'EGLL')) {
      document.querySelector('.status-box').innerHTML = `You guessed the first secret location: +300points.`;
      updateScore(300);
      londonPrinter();
    }
    else if (rainy && (data.weather.main === 'Rain' || data.weather.main === 'Drizzle')) {
      document.querySelector('.weather-box').innerHTML = `It's raining: +500points.`;
      updateScore(500);
      goalRainy();
    }
  }
  //Caparica & wind
  if (caparica || windy) {
    if (caparica && windy && data.weather.wind >= 10 && data.ident === 'LPPT') {
      document.querySelector('.status-box').innerHTML = `You guessed the second secret location and it's windy: +1000points.`;
      updateScore(1000);
      caparicaPrinter();
      goalWindy();
    }
    else if (caparica && data.ident === 'LPPT') {
      document.querySelector('.status-box').innerHTML = `You guessed the second secret location: +300points.`;
      updateScore(300);
      caparicaPrinter();
    }
    else if (windy && data.weather.wind >= 10) {
      document.querySelector('.weather-box').innerHTML = `It's windy: +500points.`;
      updateScore(500);
      goalWindy();
    }
  }
  // Prague & clouds
  if (prague || cloudy) {
    if (prague && cloudy && data.weather.main === 'Clouds' && data.ident === 'LKPR') {
      document.querySelector('.status-box').innerHTML = `You guessed the third secret location and it's cloudy: +1000points.`;
      updateScore(1000);
      praguePrinter();
      goalCloudy();
    }
    else if (prague && data.ident === 'LKPR') {
      document.querySelector('.status-box').innerHTML = `You guessed the third secret location: +300points.`;
      updateScore(300);
      praguePrinter();
    }
    else if (cloudy && data.weather.main === 'Clouds') {
      document.querySelector('.weather-box').innerHTML = `It's cloudy: +500points.`;
      updateScore(500);
      goalCloudy();
    }
  }
  // Ibiza & sunny
  if (ibiza || sunny) {
    if (ibiza && sunny && data.weather.temp >= 15 && data.ident === 'LEIB') {
      document.querySelector('.status-box').innerHTML = `You guessed the fourth secret location and it's sunny: +1000points.`;
      updateScore(1000);
      ibizaPrinter();
      goalSunny();
    }
    else if (ibiza && data.ident === 'LEIB') {
      document.querySelector('.status-box').innerHTML = `You guessed the fourth secret location: +300points.`;
      updateScore(300);
      ibizaPrinter();
    }
    else if (sunny && data.weather.temp >= 15) {
      document.querySelector('.weather-box').innerHTML = `It's sunny: +500points.`;
      updateScore(500);
      goalSunny();
    }
  }
  // Reykjavik & snow
  if (reykjavik || snows) {
    if (reykjavik && snows && data.weather.main === 'Snow' && data.ident === 'BIKF') {
      document.querySelector('.status-box').innerHTML = `You guessed the fifth secret location and it snows: +1000points.`;
      updateScore(1000);
      reykjavikPrinter();
      goalSnows();
    }
    else if (reykjavik && data.ident === 'BIKF') {
      document.querySelector('.status-box').innerHTML = `You guessed the fifth secret location: +300points.`;
      updateScore(300);
      reykjavikPrinter();
    }
    else if (snows && data.weather.main === 'Snow') {
      document.querySelector('.weather-box').innerHTML = `It snows: +500points.`;
      updateScore(500);
      goalSnows();
    }
  }
  progressChecker()
}


// // // // // // // // // // // //
// Function to update score:     //
// // // // // // // // // // // //
// Called by function goalChecker, parameter: addition score
// Adds additional score to existing score and displays new score

function updateScore(addition) {
  score += addition;
  document.querySelector('#current-score').innerHTML = `${score} points`;
}


// // // // // // // // // // // //
// Function to check progress:   //
// // // // // // // // // // // //
// Called by function goalChecker at the end
// Checks if score is 3000 or more ---> Boolean changes to true, game ends, player cannot travel further ---> Win
// Checks if CO2 budget is 0 or less ---> Boolean changes to true, game ends, player cannot travel further ---> Loose

function progressChecker() {
  document.querySelector('.order-box').innerHTML = `Please select your next location.`;
  if (score >= 3000) {
     document.querySelector('.outcome-box').innerHTML = `<b>You won ${playerName}!!! :) Your final score is: ${score} points.</b>`;
     document.querySelector('.order-box').innerHTML = "";
     endOfGame = Boolean(true);
  }
  else if (co2_budget <= 0) {
    document.querySelector('.outcome-box').innerHTML = `<b>You lost ${playerName} :( Exceeded CO2 budget.</b>`;
    document.querySelector('.order-box').innerHTML = "";
    endOfGame = Boolean(true);
  }
}


// // // // // // // // // // // //
// Functions for fun facts:      //
// // // // // // // // // // // //
// Each function is called by function goalChecker when the right place is visited:
// - boolean turns false to avoid getting the score twice for revisiting the same place
// - hides the riddle box and changes the text to the actual location
// - displays the fun fact in the output field

function londonPrinter() {
  london = Boolean(false);
  const london_riddle = document.querySelector('.riddle1');
  london_riddle.classList.add('done');
  london_riddle.innerHTML = 'London, United Kingdom';
  document.querySelector('.text-box').innerHTML = `Fun fact:<br><b>“The guards of the tower of London are called “Meat Eaters”. This is due to their historical role as the most important royal guards, as they were promised a proper meal, containing meat, even if the rest of the nation had a food crisis.”</b>`;
}

function caparicaPrinter() {
  caparica = Boolean(false);
  const caparica_riddle = document.querySelector('.riddle2');
  caparica_riddle.classList.add('done');
  caparica_riddle.innerHTML = 'Caparica, Portugal';
  document.querySelector('.text-box').innerHTML = `Fun fact:<br><b>“Costa da Caparica is a popular surfing spot as there are constant, but not massive waves. This beautiful, 26-kilometre long beach area also hosts many festivals, so don't be surprised to see people gathered here, especially on the weekends.”</b>`;
}

function praguePrinter() {
  prague = Boolean(false);
  const prague_riddle = document.querySelector('.riddle3');
  prague_riddle.classList.add('done');
  prague_riddle.innerHTML = 'Prague, Czech Republic';
  document.querySelector('.text-box').innerHTML = `Fun fact:<br><b>“The Charles Bridge has some mathematical significance. Former Czech king Charles IV laid the first stone of the bridge at precisely 5.31 am on July 9, 1357. The king was so into astrology and numerology that he chose this date because of its written form: 1-3-5-7-9-7-5-3-1 (year, day, month, time).”</b>`;
}

function ibizaPrinter() {
  ibiza = Boolean(false);
  const ibiza_riddle = document.querySelector('.riddle4');
  ibiza_riddle.classList.add('done');
  ibiza_riddle.innerHTML = 'Ibiza, Spain';
  document.querySelector('.text-box').innerHTML = `Fun fact:<br><b>“The correct pronunciation of the island’s name is ‘Evissa’. The settlers who founded Ibiza originally named it Ibozzim, and dedicated the island to Bes – the God of music and dance.”</b>`;
}

function reykjavikPrinter() {
  reykjavik = Boolean(false);
  const reykjavik_riddle = document.querySelector('.riddle5');
  reykjavik_riddle.classList.add('done');
  reykjavik_riddle.innerHTML = 'Reykjavik, Iceland';
  document.querySelector('.text-box').innerHTML = `Fun fact:<br><b>“Any Icelandic horse that leaves the country is forever forbidden to return; such are the strict protocols that regulate breeding in Iceland. The Icelandic horse is among the world’s purest bred breeds, having been isolated for over 1000 years.”</b>`;
}

function budapestPrinter() {
  budapest = Boolean(false);
  const budapest_riddle = document.querySelector('.riddle6');
  budapest_riddle.classList.add('done');
  budapest_riddle.innerHTML = 'Budapest, Hungary';
  document.querySelector('.text-box').innerHTML = `Fun fact:<br><b>“If you ever visit it, pay attention to the buildings. They are old, a lot of their facade is deteriorating and a lot of them have bullet marks from WWII and the Hungarian Revolution of 1956. When it gets dark, if you take a walk at the bank of the Danube, it’s beautifully lit up.”</b>`;
}


// // // // // // // // // // // //
// Functions for weather goals:      //
// // // // // // // // // // // //
// Each function is called by function goalChecker when the weather condition is met:
// - boolean turns false to avoid getting the score twice for the same weather condition
// - hides the weather box

function goalRainy() {
  document.querySelector('.goal-rainy').classList.add('done');
  rainy = Boolean(false);
}

function goalWindy() {
  document.querySelector('.goal-windy').classList.add('done');
  windy = Boolean(false);
}

function goalCloudy() {
  document.querySelector('.goal-cloudy').classList.add('done');
  cloudy = Boolean(false);
}

function goalSunny() {
  document.querySelector('.goal-sunny').classList.add('done');
  sunny = Boolean(false);
}

function goalSnows() {
  document.querySelector('.goal-snows').classList.add('done');
  snows = Boolean(false);
}