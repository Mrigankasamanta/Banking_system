let dark = document.querySelector(".dark")
let light = document.querySelector(".light")
let body = document.querySelector("body")
let msg = document.querySelector(".msg")

dark.addEventListener("click",() => {
    body.classList.add("night");
    body.classList.remove("day");
    dark.classList.add("hide");
    light.classList.remove("hide");
    msg.style.color = "aquamarine"
});

light.addEventListener("click",() => {
    body.classList.add("day");
    body.classList.remove("night");
    dark.classList.remove("hide");
    light.classList.add("hide");
    msg.style.color = "#072de9"
})