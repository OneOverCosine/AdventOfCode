const fs = require("fs");

function getInput(filename) {
    fs.readFile(filename, "utf-8", (err, data) => {
        if (err) throw err;

        let result = data.split("\n");

        console.log(typeof result);
        day01(result);
    });
}

function day01(masses) {
    // divide each mass by 3, round down, then subtract 2
    let totalFuelRequirements = 0;

    for (let i = 0; i < masses.length; i++) {
        let mass = parseInt(masses[i]);

        let fuelRequired = getFuelRequired(mass); //Math.floor((mass / 3)) - 2;

        totalFuelRequirements += fuelRequired;
    }
    console.log(`Result: ${totalFuelRequirements}`);
}

function getFuelRequired(mass) {
    let totalFuelRequired = 0;

    while (mass > 0) {
        let fuelRequired = Math.floor((mass / 3)) - 2;
        totalFuelRequired += fuelRequired > 0 ? fuelRequired : 0;
        mass = fuelRequired; // new mass
    }

    return totalFuelRequired;
}

getInput("01.txt");