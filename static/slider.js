// Source: W3 schools https://www.w3schools.com/howto/howto_js_rangeslider.asp

// Slider definition stuff
var slider = document.getElementById("myRange");
var output = document.getElementById("currentVal");

// declare the busy-colour variable from our css so we can modify it with busyness
var busyColour = document.querySelector(':root');

output.innerHTML = slider.value; // Display the default slider value


// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  output.innerHTML = this.value;

  /*
  // END GOAL OF THIS: update the database
  // Import the staff login details (so we know what hospital they're working for)
  user_file = fopen('../data/dummy_staff_user.json', 0);
  user_str = fread(user_file, flength(file));
  user = JSON.parse(user_str);

  // import in the hospital database
  hospital_file = fopen('../data/hospitals.json', 0);
  hosp_str = fread(user_file, flength(file));
  hosp_array = JSON.parse(hosp_file);

  // Iterate and match
  for (i = 0; i < hosp_array.length; i++) {
    if (hosp_array[i].name.localCompare(user.hospital) == 0) {
        console.log("Names match");
    }
  }
*/
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

  var data = this.value;
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/staff_home', true);
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
          console.log("sucess")
          alert('Data sent successfully');
      } else {
        console.log("FAIL")
      }
  };
  xhr.send(data);
}



