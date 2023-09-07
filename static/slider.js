// Source: W3 schools https://www.w3schools.com/howto/howto_js_rangeslider.asp

var slider = document.getElementById("myRange");
var output = document.getElementById("currentVal");
var busyColour = document.querySelector(':root');
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  output.innerHTML = this.value;

  // change the colour
  if (this.value >= 9) {
    busyColour.style.setProperty('--busy-colour', '#FF0D0D');
  } else if (this.value >= 7) {
    busyColour.style.setProperty('--busy-colour', '#FF4E11');
  } else if (this.value >= 6) {
    busyColour.style.setProperty('--busy-colour', '#FF8E15');
  } else if (this.value >= 5) {
    busyColour.style.setProperty('--busy-colour', '#FAB733');
  } else if (this.value >= 3) {
    busyColour.style.setProperty('--busy-colour', '#ACB334');
  } else {
    busyColour.style.setProperty('--busy-colour', '#69B34C');
  }
}



