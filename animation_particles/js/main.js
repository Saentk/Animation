const animations = {
  particles: {
    setup: setupParticles,
    draw: drawParticles,
  },
  circularParticles: {
    setup: setupCircularParticles,
    draw: drawCircularParticles,
  },
  hexagonParticles: {
    setup: setupHexagonParticles,
    draw: drawHexagonParticles,
  },
  triangleParticles: {
    setup: setupTriangleParticles,
    draw: drawTriangleParticles,
  },
};

let currentAnimation = 'particles';
const toggleButton = document.getElementById('toggleButton');

function setup() {
  clear();
  animations[currentAnimation].setup();
}

function draw() {
  animations[currentAnimation].draw();
}

toggleButton.addEventListener('click', () => {
  const animationKeys = Object.keys(animations);
  const currentIndex = animationKeys.indexOf(currentAnimation);
  const nextIndex = (currentIndex + 1) % animationKeys.length;
  currentAnimation = animationKeys[nextIndex];
  setup();
});
