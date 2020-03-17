// This Object contains the nested objects.
//First level of keys are "Female" and "Male"
//Second level is Macronutrient names
//Third level keys are
//"13" - means the particular RDA for ages 9-13 years
//"18" - means the particular RDA for ages 14-18 years
//"30" - means the particular RDA for ages 19-30 years
//"50" - means the particular RDA for ages 31-50 years
//"70" - means the particular RDA for ages 51-70 years
//"100" - means the particular RDA for ages >70 years
//unit - means the unit for this particular macronutrient RDA
const data_macro_rda = {
  Female: {
    Water: {
      "13": "2.1",
      "30": "2.7",
      "50": "2.7",
      "70": "2.7",
      unit: "(L/d)",
      "18": "2.3",
      "100": "2.7"
    },
    Carbohydrate: {
      "13": "130",
      "30": "130",
      "50": "130",
      "70": "130",
      unit: "(g/d)",
      "18": "130",
      "100": "130"
    },
    Fiber: {
      "13": "26",
      "30": "25",
      "50": "25",
      "70": "21",
      unit: "(g/d)",
      "18": "26",
      "100": "21"
    },
    Linoleic_Acid: {
      "13": "10",
      "30": "12",
      "50": "12",
      "70": "11",
      unit: "(g/d)",
      "18": "11",
      "100": "11"
    },
    Alpha_Linolenic_Acid: {
      "13": "1",
      "30": "1.1",
      "50": "1.1",
      "70": "1.1",
      unit: "(g/d)",
      "18": "1.1",
      "100": "1.1"
    },
    Protein: {
      "13": "34",
      "30": "46",
      "50": "46",
      "70": "46",
      unit: "(g/d)",
      "18": "46",
      "100": "46"
    }
  },
  "Male": {
    Water: {
      "13": "2.4",
      "50": "3.7",
      "70": "3.7",
      "100": "3.7",
      unit: "(L/d)",
      "18": "3.3",
      "30": "3.7"
    },
    Carbohydrate: {
      "13": "130",
      "50": "130",
      "70": "130",
      "100": "130",
      unit: "(g/d)",
      "18": "130",
      "30": "130"
    },
    Fiber: {
      "13": "31",
      "50": "38",
      "70": "30",
      "100": "30",
      unit: "(g/d)",
      "18": "38",
      "30": "38"
    },
    Linoleic_Acid: {
      "13": "12",
      "50": "17",
      "70": "14",
      "100": "14",
      unit: "(g/d)",
      "18": "16",
      "30": "17"
    },
    Alpha_Linolenic_Acid: {
      "13": "1.2",
      "50": "1.6",
      "70": "1.6",
      "100": "1.6",
      unit: "(g/d)",
      "18": "1.6",
      "30": "1.6"
    },
    Protein: {
      "13": "34",
      "50": "56",
      "70": "56",
      "100": "56",
      unit: "(g/d)",
      "18": "52",
      "30": "56"
    }
  }
};
