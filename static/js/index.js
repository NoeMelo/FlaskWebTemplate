const clearBtn = document.querySelector("#clearBtn");

clearBtn.addEventListener('click',()=>{
    const textAreaInput = document.querySelector("#textAreaInput");
    textAreaInput.value = "";
});