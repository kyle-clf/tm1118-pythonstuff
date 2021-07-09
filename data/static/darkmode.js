var darkMode = document.getElementById('darkMode');

var darkLabel = "darkModeLabel";
var darkLang = "Dark";
var lightLang = "Light";

var imgID = "logo";
var darkImg = "./dark.png";
var lightImg = "./light.png";

document.addEventListener('DOMContentLoaded', function () {
  try {
    if (darkMode) {
      initTheme();

    }

  } catch (error) {

  }
  darkMode.addEventListener('change', function () {

    resetTheme();
  });
});




function initTheme() {
  var darkThemeSelected = localStorage.getItem('darkMode') !== null && localStorage.getItem('darkMode') === 'dark';
  darkMode.checked = darkThemeSelected;
  try {
    darkThemeSelected ? document.body.setAttribute('data-theme', 'dark') : document.body.removeAttribute('data-theme');
  } finally {

  }
  try {
    darkThemeSelected ? document.getElementById(imgID).src = darkImg : document.getElementById(imgID).src = lightImg;
  } finally {

  }
  try {

  } finally {
    darkThemeSelected ? document.getElementById(darkLabel).innerHTML = darkLang : document.getElementById(darkLabel).innerHTML = lightLang;
  }


}

function resetTheme() {
  if (darkMode.checked) {
    document.body.setAttribute('data-theme', 'dark');
    localStorage.setItem('darkMode', 'dark');
    try { document.getElementById(imgID).src = darkImg; } finally { }
    try { document.getElementById(darkLabel).innerHTML = darkLang; } finally { }
  } else {


    document.body.removeAttribute('data-theme');
    localStorage.removeItem('darkMode');
    try { document.getElementById(imgID).src = lightImg; } finally { }
    try { document.getElementById(darkLabel).innerHTML = lightLang; } finally { }
  }
}



function setDarkMode() {
  try {
    document.getElementById('darkMode').checked = !document.getElementById('darkMode').checked
    resetTheme();
  } finally { }

}