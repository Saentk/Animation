const hexagonParticles = [];

function setupHexagonParticles() {
  hexagonParticles.length = 0; // Clear the particles list
  createCanvas(window.innerWidth, window.innerHeight);
  const particlesLength = Math.floor(window.innerWidth / 30);

  for (let i = 0; i < particlesLength; i++) {
    hexagonParticles.push(new HexagonParticle());
  }
}
function drawHexagonParticles() {
  background(0, 0, 64);
  hexagonParticles.forEach((particle, idx) => {
    particle.update();
    particle.draw();
    particle.checkParticles(hexagonParticles.slice(idx));
  });
}

class HexagonParticle {
  constructor() {
    this.side = Math.floor(Math.random() * 6);
    this.progress = Math.random();
    this.speed = Math.random() * (0.01 - 0.002) + 0.002;
    this.hexagonRadius = 200;
    this.center = createVector(width / 2, height / 2);
    this.size = 10;
    this.pos = this.getHexagonPoint(this.side, this.progress);
  }

  update() {
    this.progress += this.speed;
    if (this.progress >= 1) {
      this.progress = 0;
      this.side = (this.side + 1) % 6;
    }
    this.pos = this.getHexagonPoint(this.side, this.progress);
  }

  draw() {
    noStroke();
    fill('rgba(255, 255, 255, 0.5)');
    circle(this.pos.x, this.pos.y, this.size);
  }

  checkParticles(particles) {
    particles.forEach(particle => {
      const d = dist(this.pos.x, this.pos.y, particle.pos.x, particle.pos.y);
      if (d < 120) {
        stroke('rgba(255, 255, 255, 0.1)');
        line(this.pos.x, this.pos.y, particle.pos.x, particle.pos.y);
      }
    });
  }

  getHexagonPoint(side, progress) {
  const angleBetweenVertices = TWO_PI / 6;
  const rotationOffset = HALF_PI;

  const vertices = [];
  for (let i = 0; i < 6; i++) {
    const angle = i * angleBetweenVertices + rotationOffset;
    const x = this.center.x + this.hexagonRadius * cos(angle);
    const y = this.center.y + this.hexagonRadius * sin(angle);
    vertices.push(createVector(x, y));
  }

  const start = vertices[side];
  const end = vertices[(side + 1) % 6];

  const x = lerp(start.x, end.x, progress);
  const y = lerp(start.y, end.y, progress);

  return createVector(x, y);
  }
}



