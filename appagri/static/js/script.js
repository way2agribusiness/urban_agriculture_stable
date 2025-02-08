var toggleBtn = document.getElementById('toggleBtn');
var content = document.getElementById('content');

toggleBtn.addEventListener('click', function () {
  if (content.style.display === 'none') {
    content.style.display = 'grid';
  } else {
    content.style.display = 'none';
  }
});
//  nav button toggle end

/////gallery/////
const subImgs = document.querySelectorAll('.sub_img img');
const mainImg = document.querySelector('.main_img');

subImgs.forEach((subImg) => {
  subImg.addEventListener('click', function () {
    mainImg.setAttribute('src', this.getAttribute('src'));
  });
});
///////////blog toggel////////////
function myFunction() {
  var x = document.getElementById('myDIV');
  if (x.style.display === 'none') {
    x.style.display = 'block';
  } else {
    x.style.display = 'none';
  }
}
/////////end bllog toggle///////
/////////sidebar toggle///////
function mySidebar() {
  var x = document.getElementById('side_bar');
  if (x.style.display === 'none') {
    x.style.display = 'block';
  } else {
    x.style.display = 'none';
  }
}
////////end sidebar/////////
/////////////brands//////////
const control = document.getElementById('direction-toggle');
const marquees = document.querySelectorAll('.marquee');
const wrappero = document.querySelector('.wrapper');

if (control) {
  control.addEventListener('click', () => {
    control.classList.toggle('toggle--vertical');
    wrappero.classList.toggle('wrapper--vertical');
    [...marquees].forEach((marquee) =>
      marquee.classList.toggle('marquee--vertical')
    );
  });
}
//////////brands end///////////
/////////////dark mode///////////
const modeToggle = document.querySelector('#mode-toggle');
const body = document.querySelector('body');

modeToggle.addEventListener('click', () => {
  body.classList.toggle('dark-mode');
  div.classList.toggle('dpcard');
});

/////////////END///////////////

///////////////weather////////////////
const wrapper = document.querySelector('.wrapper'),
  inputPart = document.querySelector('.input-part'),
  infoTxt = inputPart.querySelector('.info-txt'),
  inputField = inputPart.querySelector('input'),
  locationBtn = inputPart.querySelector('button'),
  weatherPart = wrapper.querySelector('.weather-part'),
  wIcon = weatherPart.querySelector('img'),
  arrowBack = wrapper.querySelector('header i');

let api;

inputField.addEventListener('keyup', (e) => {
  if (e.key == 'Enter' && inputField.value != '') {
    requestApi(inputField.value);
  }
});

locationBtn.addEventListener('click', () => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(onSuccess, onError);
  } else {
    alert('Your browser not support geolocation api');
  }
});

function requestApi(city) {
  api = `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=06362abbf757402ffae9686038facb28`;
  fetchData();
}

function onSuccess(position) {
  const { latitude, longitude } = position.coords;
  api = `https://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&units=metric&appid=06362abbf757402ffae9686038facb28`;
  fetchData();
}

function onError(error) {
  infoTxt.innerText = error.message;
  infoTxt.classList.add('error');
}

function fetchData() {
  infoTxt.innerText = 'Getting weather details...';
  infoTxt.classList.add('pending');
  fetch(api)
    .then((res) => res.json())
    .then((result) => weatherDetails(result))
    .catch(() => {
      infoTxt.innerText = 'Something went wrong';
      infoTxt.classList.replace('pending', 'error');
    });
}

function weatherDetails(info) {
  if (info.cod == '404') {
    infoTxt.classList.replace('pending', 'error');
    infoTxt.innerText = `${inputField.value} isn't a valid city name`;
  } else {
    const city = info.name;
    const country = info.sys.country;
    const { description, id } = info.weather[0];
    const { temp, feels_like, humidity } = info.main;

    if (id == 800) {
      wIcon.src = 'icons/clear.svg';
    } else if (id >= 200 && id <= 232) {
      wIcon.src = 'icons/storm.svg';
    } else if (id >= 600 && id <= 622) {
      wIcon.src = 'icons/snow.svg';
    } else if (id >= 701 && id <= 781) {
      wIcon.src = 'icons/haze.svg';
    } else if (id >= 801 && id <= 804) {
      wIcon.src = 'icons/cloud.svg';
    } else if ((id >= 500 && id <= 531) || (id >= 300 && id <= 321)) {
      wIcon.src = 'icons/rain.svg';
    }

    weatherPart.querySelector('.temp .numb').innerText = Math.floor(temp);
    weatherPart.querySelector('.weather').innerText = description;
    weatherPart.querySelector(
      '.location span'
    ).innerText = `${city}, ${country}`;
    weatherPart.querySelector('.temp .numb-2').innerText =
      Math.floor(feels_like);
    weatherPart.querySelector('.humidity span').innerText = `${humidity}%`;
    infoTxt.classList.remove('pending', 'error');
    infoTxt.innerText = '';
    inputField.value = '';
    wrapper.classList.add('active');
  }
  console.log(weatherPart);
}

arrowBack.addEventListener('click', () => {
  wrapper.classList.remove('active');
});
///////////////end weather//////////////////
/////////back button/////////////
function goBack() {
  window.history.back();
}
/////end//////////
///////close button///////
$(".closebtn").on("click", function(e) {
  $(".wrapper").hide()
})  