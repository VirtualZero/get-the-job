function getRandomNums() {
    var randNum1 = Math.floor(Math.random() * 10);
    var randNum2 = Math.floor(Math.random() * 10);
    document.getElementById('random-number1').innerHTML = randNum1;
    document.getElementById('input-rand-num1').value = randNum1;
    document.getElementById('random-number2').innerHTML = randNum2;
    document.getElementById('input-rand-num2').value = randNum2;
}

window.onload = function () {
    document.getElementById('landing-preloader').style.display = 'none';
    document.getElementById('content-section').style.display = 'block';
}