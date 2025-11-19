const button_1 = document.querySelector("#button_1");
const heading_1 = document.querySelector("#heading_1");

let count = 1;

button_1.onclick = () =>{
    if (count < 10){
        button_1.textContent = "Try Again!";
        heading_1.textContent = `${count} clicks so far`;
        count += 1;
    }else{
        button_1.style.backgroundColor = "red";
        button_1.textContent = "Too Many Clicks";
        heading_1.textContent = `${count} clicks`;
    }

};