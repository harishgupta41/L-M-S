let getotp=document.querySelector("#getotp-btn");

// console.log(getotp)
getotp.addEventListener("click",()=>{
    let otpform=document.querySelector(".otp-verify");
    otpform.style.display="flex";
    let regform=document.querySelector(".reg-form");
    regform.style.display="none";
})
