//git: https://github.com/sakthind-dev/simple_JS_Calculator/branches
const display = document.getElementById('display');

function appendValue(value) {
    display.value += value;
}

function clearDisplay() {
    display.value = '';
}

function deleteLast() {
    display.value = display.value.slice(0, -1);
}

function calculate() {
    try {
        display.value = eval(display.value) ?? '';
    } catch {
        display.value = 'Error';
    }
}

const button = document.getElementById("myButton");
const output = document.getElementById("output");

button.addEventListener("click", async () => {
  const response = await fetch("/run", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text: "button clicked" })
  });
  const data = await response.json();
  output.textContent = data.result;
});