
let display = document.getElementById("display");

// Display numbers and operators
function appendValue(value) {
    display.value += value;
}

// Clear the display
function clearDisplay() {
    display.value = "";
}

// Delete the last character
function deleteLast() {
    display.value = display.value.slice(0, -1);
}

// Perform calculation
function calculate() {
    try {
        if (display.value === "") {
            return;
        }

        let expression = display.value;

        // Allow only calculator characters
        if (!/^[0-9+\-*/%.()\s]+$/.test(expression)) {
            throw new Error("Invalid input");
        }

        let result = Function(
            '"use strict"; return (' + expression + ')'
        )();

        if (!Number.isFinite(result)) {
            throw new Error("Invalid calculation");
        }

        display.value = result;

    } catch (error) {
        display.value = "Error";
    }
}
