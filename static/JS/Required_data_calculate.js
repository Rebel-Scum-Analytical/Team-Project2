
function calculateAge(dob){
    var from = dob.split("/");
    var birthdateTimeStamp = new Date(from[2], from[1] - 1, from[0]);
    var cur = new Date();
    var diff = cur - birthdateTimeStamp;
    // This is the difference in milliseconds
    user_age = Math.floor(diff/31557600000);
    if(user_age <= 13)
    {
        age_key = "13";

    }else if((user_age>= 14) && (user_age<= 18))
    {
        age_key = "18";

    }else if((user_age>= 19) && (user_age<= 30))
    {
        age_key = "30";
    }else if((user_age>= 31) && (user_age<= 50))
    {
        age_key = "50";
    }
    else if((user_age>= 51) && (user_age<= 70))
    {
        age_key = "70";
    }else {
        age_key = "100";
    }
    return age_key


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

function dri_macro_nutrient(data){
    return data_macro_rda[data.gender][data.nutrient][data.age_key]
}

function dri_micro_nutrient_minerals(data){

    values = [] 
    values.push(data_mineral_rda[data.gender][data.nutrient][data.age_key])
    return values
}

function dri_micro_nutrient_vitamins(data){

    values = []   
    values.push(data_vitamin_rda[data.gender][data.nutrient][data.age_key])
    return values
}


  


