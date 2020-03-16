user_personal_data = 
{
    height: 65,
    weight: 205,
    gender: "male",
    date_of_birth:"10/1/1980",
    physical_activity_level:"Lightly_active",
    calories:0
}

function calculateAge(dob){
    var from = dob.split("/");
    var birthdateTimeStamp = new Date(from[2], from[1] - 1, from[0]);
    var cur = new Date();
    var diff = cur - birthdateTimeStamp;
    // This is the difference in milliseconds
    return Math.floor(diff/31557600000);
}
function calculateMultiplier(PAL){
switch (PAL) {
    case 'Sedentary': return 1.2;
    case 'Lightly_active':return 1.375;
    case 'moderately_active':return 1.55;
    case 'very_active':return 1.725;
    case 'extra_active':return 1.9;
    default: return 1.2;      
  }
}

function calculateBMRCalories(user_personal_data){
    if(user_personal_data.gender === "Male")
    {
        bmr = (66 + 
            6.3*user_personal_data.weight +
            12.9*user_personal_data.height -
            6.8*calculateAge(user_personal_data.date_of_birth));
    
    
    }else(user_personal_data.gender === "Female")
    {
        bmr = (655 + 
            4.3*user_personal_data.weight +
            4.7*user_personal_data.height -
            4.7*calculateAge(user_personal_data.date_of_birth));
    
    }
    user_personal_data.calories = bmr*calculateMultiplier(user_personal_data.physical_activity_level)
    
}

calculateBMRCalories(user_personal_data);
console.log(user_personal_data);

  


