let mathData;
let number=204;

function setup() {
  createCanvas(600, 600);
  let url_and_number = 'http://localhost:8000/scripts/factor.py?number='.concat(204)
  loadJSON(url_and_number, gotData, 'json');
}

function gotData(data) {
  mathData = data;
}

function draw() {
  background(0);

  fill(255)
  text("What are the prime factors of my number?", 100,100)
  if (mathData) {
    print(mathData.factors)
  }

}
