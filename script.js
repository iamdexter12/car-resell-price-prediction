const form = document.getElementById("myForm");
const resultDiv = document.querySelector(".result");
const main_result = document.getElementById("main_result");
form.addEventListener("submit", (e)=>{
    e.preventDefault();
    let formData = new FormData(form);
    fetch("http://127.0.0.1:5001/predict_car_price",{
        method:'post',
        body: formData
    }).then(res=>{
        return res.json();
    }).then(data=>{
        resultDiv.classList.remove('noDisplay');
        main_result.innerText = `ESTIMATED PRICE : ${data.estimated_price} Lakhs`
    })
})
