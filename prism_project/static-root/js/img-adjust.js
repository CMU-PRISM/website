var img = document.getElementById("index-img");

function updateImg() {
    img.style.height = window.getComputedStyle(img).getPropertyValue('width');
}

// Run once, then again on resize
updateImg();
window.onresize = updateImg;
