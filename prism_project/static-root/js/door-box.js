function doorBox() {
    // If innerText starts with OPEN, green
    if (door.innerText[0] == "O") {
        box.style.backgroundColor = "#cfc";
    }
    // If innerText starts with CLOSED, red
    else if (door.innerText[0] == "C") {
        box.style.backgroundColor = "#fcc"
    }
    // Default to yellow
    else {
        box.style.backgroundColor = "#ffc"
    }
}

var box = document.getElementById("door-status-indicator");
var door = document.getElementById("door-status");

// Run every so often
doorBox()