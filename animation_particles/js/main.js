// main.js
let currentAnimation = 'particles';
const toggleButton = document.getElementById('toggleButton');

function setup() {
  clear();
  if (currentAnimation === 'circularParticles') {
    setupCircularParticles();
  } else if (currentAnimation === 'hexagonParticles') {
    setupHexagonParticles();
  } else if (currentAnimation === 'triangleParticles') {
    setupTriangleParticles();
  } else {
    setupParticles();
  }
}

function draw() {
  if (currentAnimation === 'circularParticles') {
    drawCircularParticles();
  } else if (currentAnimation === 'hexagonParticles') {
    drawHexagonParticles();
  } else if (currentAnimation === 'triangleParticles') {
    drawTriangleParticles();
  } else {
    drawParticles();
  }
}

toggleButton.addEventListener('click', () => {
  if (currentAnimation === 'particles') {
    currentAnimation = 'circularParticles';
  } else if (currentAnimation === 'circularParticles') {
    currentAnimation = 'hexagonParticles';
  } else if (currentAnimation === 'hexagonParticles') {
    currentAnimation = 'triangleParticles';
  } else {
    currentAnimation = 'particles';
  }
  setup();
});
