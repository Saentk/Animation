const triangleParticles = [];

function setupTriangleParticles() {
  triangleParticles.length = 0; // Clear the particles list
  createCanvas(window.innerWidth, window.innerHeight);
  const particlesLength = Math.floor(window.innerWidth / 30);

  for (let i = 0; i < particlesLength; i++) {
    triangleParticles.push(new TriangleParticle());
  }
}

function drawTriangleParticles() {
  background(0, 0, 64);
  triangleParticles.forEach((particle, idx) => {
    particle.update();
    particle.draw();
    particle.checkParticles(triangleParticles.slice(idx));
  });
}

class TriangleParticle {
  constructor() {
    this.side = Math.floor(Math.random() * 3);
    this.progress = Math.random();
    this.speed = Math.random() * (0.01 - 0.002) + 0.002;
    this.triangleRadius = 200;
    this.center = createVector(width / 2, height / 2);
    this.size = 10;
    this.pos = this.getTrianglePoint(this.side, this.progress);
  }

  update() {
    this.progress += this.speed;
    if (this.progress >= 1) {
      this.progress = 0;
      this.side = (this.side + 1) % 3;
    }
    this.pos = this.getTrianglePoint(this.side, this.progress);
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

  getTrianglePoint(side, progress) {
    const vertices = [
      createVector(this.center.x, this.center.y - this.triangleRadius),
      createVector(this.center.x + this.triangleRadius * sin(PI / 3), this.center.y + this.triangleRadius / 2),
      createVector(this.center.x - this.triangleRadius * sin(PI / 3), this.center.y + this.triangleRadius / 2),
    ];

    const start = vertices[side];
    const end = vertices[(side + 1) % 3];

    const x = lerp(start.x, end.x, progress);
    const y = lerp(start.y, end.y, progress);

    return createVector(x, y);
  }
}


//   getTrianglePoint(side, progress) {
//   const angle = 120 * side + progress * 120;
//   const radian = radians(angle);
//   const x = this.center.x + this.triangleRadius * cos(radian);
//   const y = this.center.y + this.triangleRadius * sin(radian);
//   return createVector(x, y);
// }


  // getTrianglePoint(side, progress) {
  //   const angle = 120 * floor(side / 2) + progress * 120;
  //   const radian = radians(angle);
  //   const xOffset = side % 2 === 0 ? 0 : this.triangleRadius * cos(radians(60));
  //   const x = this.center.x + xOffset + this.triangleRadius * cos(radian);
  //   const y = this.center.y + this.triangleRadius * sin(radian) * (side % 2 === 0 ? 1 : -1);
  //   return createVector(x, y);
  // }
