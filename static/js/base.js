// Toggle grid padding
function myFunction() {
  var x = document.getElementById("myGrid");
  if (x.className === "w3-row") {
    x.className = "w3-row-padding";
  } else { 
    x.className = x.className.replace("w3-row-padding", "w3-row");
  }
}

// Open and close sidebar
function w3_open() {
  document.getElementById("mySidebar").style.width = "100%";
  document.getElementById("mySidebar").style.display = "block";
}

function w3_close() {
  document.getElementById("mySidebar").style.display = "none";
}

// Auto-including the user id with the post
var name = "{{ request.user.id }}";
  document.getElementById("change").value = name;

// Close alert message
function closeMessage() {
  document.getElementById('message').style.display = "none";
}
