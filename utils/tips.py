import random


# =========================================
# GENERAL FARMING TIPS
# =========================================

general_tips = [

    {
        "title":
        "Use Organic Compost",

        "description":
        "Organic compost improves soil fertility and increases water retention."
    },

    {
        "title":
        "Crop Rotation",

        "description":
        "Rotate crops regularly to maintain soil nutrients and reduce pests."
    },

    {
        "title":
        "Proper Irrigation",

        "description":
        "Avoid over-irrigation and use drip irrigation for better water management."
    },

    {
        "title":
        "Use Quality Seeds",

        "description":
        "Certified seeds improve crop yield and disease resistance."
    },

    {
        "title":
        "Soil Testing",

        "description":
        "Test soil every season before applying fertilizers."
    }
]



# =========================================
# CROP TIPS
# =========================================

crop_tips = {

    "rice": [

        "Maintain standing water during growth.",

        "Apply nitrogen fertilizer properly.",

        "Avoid water shortage during flowering."
    ],

    "wheat": [

        "Use well-drained soil.",

        "Apply irrigation during root initiation.",

        "Use balanced fertilizers."
    ],

    "maize": [

        "Ensure proper spacing.",

        "Use organic manure.",

        "Protect crop from insects."
    ],

    "cotton": [

        "Avoid over irrigation.",

        "Use potassium-rich fertilizers.",

        "Monitor bollworm regularly."
    ]
}



# =========================================
# GET GENERAL TIPS
# =========================================

def get_general_tips(count=3):

    return random.sample(

        general_tips,

        min(count, len(general_tips))
    )



# =========================================
# GET CROP TIPS
# =========================================

def get_crop_tips(crop_name):

    crop_name = crop_name.lower()


    if crop_name in crop_tips:

        return crop_tips[crop_name]


    return [

        "Use proper irrigation.",

        "Monitor soil nutrients regularly.",

        "Apply fertilizers carefully."
    ]