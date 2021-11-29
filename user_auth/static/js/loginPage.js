document.addEventListener("DOMContentLoaded", function (event) {
// Your code to run since DOM is loaded and ready
VanillaTilt.init(document.querySelectorAll(".card"), {
max: 25,
speed: 400,
glare: false,
"max-glare": 0.8
});
VanillaTilt.init(document.querySelectorAll(".card"));
});
