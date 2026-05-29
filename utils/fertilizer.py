def fertilizer_advice(n, p, k):

    if n < 40:

        return {

            "fertilizer": "Urea",

            "quantity": "45 kg/hectare",

            "advice": "Apply after irrigation"
        }

    elif p < 40:

        return {

            "fertilizer": "DAP",

            "quantity": "30 kg/hectare",

            "advice": "Mix before sowing"
        }

    elif k < 40:

        return {

            "fertilizer": "MOP",

            "quantity": "25 kg/hectare",

            "advice": "Apply in early stage"
        }

    return {

        "fertilizer": "Balanced",

        "quantity": "No extra fertilizer needed",

        "advice": "Soil nutrients are balanced"
    }