def soil_advice(ph):

    if ph < 5.5:

        return {

            "nature": "Acidic Soil",

            "problem": "Low nutrient absorption",

            "solution": "Add lime and compost",

            "quantity": "200 kg/hectare"
        }

    elif ph > 7.5:

        return {

            "nature": "Alkaline Soil",

            "problem": "High salt concentration",

            "solution": "Add gypsum",

            "quantity": "150 kg/hectare"
        }

    return {

        "nature": "Healthy Soil",

        "problem": "No major issue",

        "solution": "Maintain compost",

        "quantity": "Normal maintenance"
    }