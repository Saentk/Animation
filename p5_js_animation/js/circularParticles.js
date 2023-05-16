const circularParticles = [];

function setupCircularParticles() {
  circularParticles.length = 0; // Clear the particles list
  createCanvas(window.innerWidth, window.innerHeight);
  const particlesLength = Math.floor(window.innerWidth / 20);

  for (let i = 0; i < particlesLength; i++) {
    circularParticles.push(new CircularParticle());
  }
}

function drawCircularParticles() {
  background(0, 0, 64);
  circularParticles.forEach((particle, idx) => {
    particle.update();
    particle.draw();
    particle.checkParticles(circularParticles.slice(idx));
  });
}

class CircularParticle {
  constructor() {
    this.angle = random(TWO_PI);
    this.radius = random(270, 300);
    this.speed = random(0.01, 0.05);
    this.center = createVector(width / 2, height / 2);
    this.pos = createVector(this.center.x + this.radius * cos(this.angle), this.center.y + this.radius * sin(this.angle));
    this.size = 10;
  }

  update() {
    this.angle += this.speed;
    this.pos.x = this.center.x + this.radius * cos(this.angle);
    this.pos.y = this.center.y + this.radius * sin(this.angle);
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
}
