PROTIEN_PERCENT = 0.3;
CARB_PERCENT = 0.5;
FAT_PERCENT = 0.2;

required_data = {
    calories:{
        total:user_personal_data.calories, 
        proteins:user_personal_data.calories*PROTIEN_PERCENT, 
        carbohydrates:user_personal_data.calories*CARB_PERCENT, 
        fats:user_personal_data.calories*FAT_PERCENT } ,
    minerals:{Magnesium:,
        Calcium:,
        Potassium:,
        Sodium:,
        Phosphorus:,
        Chloride:,
        Sulphur:,
        Chromium:,
        Copper:,
        Fluoride:,
        Iodine:,
        Iron:,
        Manganese:,
        Molybdenum:,
        Selenium:,
        Zinc:,
        } ,
    vitamins: {Vitamin_C:,
        Cobalamin_VB12:,
        Thiamine_VB1:,
        Riboflavin_VB2:,
        Niacin_VB3:,
        Pantothenic_Acid_VB5:,
        Pyridoxine_VB6:,
        Biotin_VB7:,
        Folate_VB9:,
        Vitamin_D:,
        Vitamin_K:,
        Vitamin_E:,
        Vitamin_A:

        },
    water: 8
  }