let display = document.getElementById("display");
let historyList = document.getElementById("historyList");

function append(val){
    display.value += val;
}

function clearDisplay(){
    display.value = "";
}

function backspace(){
    display.value = display.value.slice(0,-1);
}

function calculate(){
    let expression = display.value;

    fetch("/calculate", {
        method:"POST",
        headers:{ "Content-Type":"application/json" },
        body: JSON.stringify({expression})
    })
    .then(res=>res.json())
    .then(data=>{
        addHistory(expression, data.result);
        display.value = data.result;
    })
    .catch(()=> display.value="Error");
}

function addHistory(exp,res){
    let li = document.createElement("li");
    li.textContent = exp + " = " + res;
    historyList.prepend(li);
}