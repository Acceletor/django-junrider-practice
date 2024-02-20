console.log("junrider");

const subscriptionForm = document.querySelector('.subscription-form')

function foodSetValidation(event){
    const checkedFoodset = document.querySelectorAll('input[name="food_set"]:checked');
    if(checkedFoodset.length === 0){
        event.preventDefault();
        alert('Choose at least one menu');
    }
}

if (!!subscriptionForm){
    subscriptionForm.addEventListener('submit', foodSetValidation)
}


