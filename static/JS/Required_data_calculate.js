
function calculateAge(dob){
    var from = dob.split("/");
    var birthdateTimeStamp = new Date(from[2], from[1] - 1, from[0]);
    var cur = new Date();
    var diff = cur - birthdateTimeStamp;
    // This is the difference in milliseconds
    return Math.floor(diff/31557600000);
}
function calcPhysicalMultiplier(PAL){
switch (PAL) {
    case 'Sedentary': return 1.2;
    case 'Lightly_active':return 1.375;
    case 'moderately_active':return 1.55;
    case 'very_active':return 1.725;
    case 'extra_active':return 1.9;
    default: return 1.2;      
  }
}

function calculateCalories(user_personal_data){
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
    return(bmr*calcPhysicalMultiplier(user_personal_data.physical_activity_level))
    
}


  


