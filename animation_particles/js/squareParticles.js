const squareParticles = [];

function setupSquareParticles() {
  squareParticles.length = 0;
  createCanvas(window.innerWidth, window.innerHeight);
  const particlesLength = Math.floor(window.innerWidth / 30);

  for (let i = 0; i < particlesLength; i++) {
    squareParticles.push(new SquareParticle());
  }
}

function drawSquareParticles() {
  background(0, 0, 64);
  squareParticles.forEach((particle, idx) => {
    particle.update();
    particle.draw();
    particle.checkParticles(squareParticles.slice(idx));
  });
}

class SquareParticle {
  constructor() {
    this.side = Math.floor(random(4));
    this.progress = random();
    this.speed = random(0.005, 0.01);
    this.squareSize = 300;
    this.center = createVector(width / 2, height / 2);
    this.size = 10;
    this.pos = this.getSquarePoint(this.side, this.progress);
  }

  update() {
    this.progress += this.speed;
    if (this.progress >= 1) {
      this.progress = 0;
      this.side = (this.side + 1) % 4;
    }
    this.pos = this.getSquarePoint(this.side, this.progress);
  }

  draw() {
    noStroke();
    fill('rgba(255, 255, 255, 0.5)');
    rect(this.pos.x - this.size / 2, this.pos.y - this.size / 2, this.size, this.size);
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

  getSquarePoint(side, progress) {
    const halfSize = this.squareSize / 2;
    const topLeft = createVector(this.center.x - halfSize, this.center.y - halfSize);
    const topRight = createVector(this.center.x + halfSize, this.center.y - halfSize);
    const bottomLeft = createVector(this.center.x - halfSize, this.center.y + halfSize);
    const bottomRight = createVector(this.center.x + halfSize, this.center.y + halfSize);

    const points = [topLeft, topRight, bottomRight, bottomLeft];
    const start = points[side];
    const end = points[(side + 1) % 4];

    const x = lerp(start.x, end.x, progress);
    const y = lerp(start.y, end.y, progress);

    return createVector(x, y);
  }
}
