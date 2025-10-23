class Car {
  constructor(brand, model, year) {
    this.brand = brand;
    this.model = model;
    this.year = year;
  }

  getInfo() {
    return `${this.year} ${this.brand} ${this.model}`;
  }

  displayDetails() {
    console.log('Car Details:');
    console.log(`Brand: ${this.brand}`);
    console.log(`Model: ${this.model}`);
    console.log(`Year: ${this.year}`);
    console.log('--------------------');
  }

  toString() {
    return this.getInfo();
  }
}

// Create objects and call the method
const car1 = new Car('Toyota', 'Camry', 2022);
const car2 = new Car('Honda', 'Civic', 2023);
const car3 = new Car('Tesla', 'Model 3', 2024);

car1.displayDetails();
car2.displayDetails();
car3.displayDetails();

console.log('String representation:');
console.log(car1.toString());
