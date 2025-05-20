let zeichenkette = ["123", "1234", "12345", "1234566", "1234567"];
let i = 0;
let maxLen = 0;


while (i < zeichenkette.length) {
    if (zeichenkette[i].length > maxLen) {
        maxLen = zeichenkette[i].length;
    }
    i++;
}

i = 0;
const laengste = [];

while (i < zeichenkette.length) {
    if (zeichenkette[i].length === maxLen) {
        laengste.push(zeichenkette[i]);
    }
    i++;
}

console.log(`Die längste Zeichenkette: ${JSON.stringify(laengste)}`);