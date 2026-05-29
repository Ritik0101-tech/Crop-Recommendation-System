// =========================================
// LOAD INDIA STATES + DISTRICTS
// =========================================

async function loadIndiaData(){

    try{

        const response = await fetch(
            '/static/data/india_data.json'
        )

        const indiaData = await response.json()


        const stateSelect =
        document.getElementById("state")

        const districtSelect =
        document.getElementById("district")


        // =================================
        // DEFAULT OPTIONS
        // =================================

        stateSelect.innerHTML = `

        <option value="">

            Select State

        </option>
        `


        districtSelect.innerHTML = `

        <option value="">

            Select District

        </option>
        `


        // =================================
        // LOAD STATES
        // =================================

        Object.keys(indiaData).forEach(state=>{

            let option =
            document.createElement("option")

            option.value = state

            option.textContent = state

            stateSelect.appendChild(option)
        })


        // =================================
        // UPDATE DISTRICTS
        // =================================

        stateSelect.addEventListener(

            "change",

            function(){

                districtSelect.innerHTML = `

                <option value="">

                    Select District

                </option>
                `


                const selectedState =
                stateSelect.value


                if(selectedState){

                    indiaData[selectedState]
                    .forEach(district=>{

                        let option =
                        document.createElement("option")

                        option.value = district

                        option.textContent = district

                        districtSelect.appendChild(option)
                    })
                }
            }
        )

    }

    catch(error){

        console.log(
            "India Data Error:",
            error
        )
    }
}



// =========================================
// WEATHER
// =========================================

async function loadWeather(){

    if(!navigator.geolocation){

        document.getElementById(
            "weatherMiniText"
        ).innerHTML =
        "Location unavailable"

        return
    }


    navigator.geolocation.getCurrentPosition(

        async(position)=>{

            try{

                const lat =
                position.coords.latitude

                const lon =
                position.coords.longitude


                const response = await fetch(

                    `/weather?lat=${lat}&lon=${lon}`
                )

                const data =
                await response.json()


                // MINI WEATHER
                document.getElementById(
                    "weatherMiniText"
                ).innerHTML = `

                ${data.temperature}°C
                `


                // ICON
                let icon = "☀"


                if(data.condition
                    .toLowerCase()
                    .includes("cloud")){

                    icon = "☁"
                }

                else if(data.condition
                    .toLowerCase()
                    .includes("rain")){

                    icon = "🌧"
                }

                else if(data.condition
                    .toLowerCase()
                    .includes("storm")){

                    icon = "⛈"
                }


                document.getElementById(
                    "weatherIcon"
                ).innerHTML = icon

            }

            catch(error){

                console.log(error)
            }
        }
    )
}



// =========================================
// CHANGE LANGUAGE
// =========================================

function changeLanguage(){

    const lang =
    document.getElementById(
        "languageSelect"
    ).value


    // =====================================
    // HINDI
    // =====================================

    if(lang === "hi"){

        setText(
            "mainTitle",
            "स्मार्ट क्रॉप एआई"
        )

        setText(
            "dashboardTitle",
            "मिट्टी डेटा दर्ज करें"
        )

        setText(
            "predictBtn",
            "फसल खोजें"
        )

        setText(
            "clearBtn",
            "डेटा साफ करें"
        )

        setText(
            "backBtn",
            "वापस"
        )

        setPlaceholder(
            "n",
            "नाइट्रोजन"
        )

        setPlaceholder(
            "p",
            "फॉस्फोरस"
        )

        setPlaceholder(
            "k",
            "पोटैशियम"
        )

        setPlaceholder(
            "ph",
            "पीएच मान"
        )
    }


    // =====================================
    // ENGLISH
    // =====================================

    else{

        location.reload()
    }
}



// =========================================
// SET TEXT
// =========================================

function setText(id, text){

    const element =
    document.getElementById(id)

    if(element){

        element.innerText = text
    }
}



// =========================================
// SET PLACEHOLDER
// =========================================

function setPlaceholder(id, text){

    const element =
    document.getElementById(id)

    if(element){

        element.placeholder = text
    }
}



// =========================================
// VALIDATE INPUTS
// =========================================

function validateInputs(){

    const n =
    document.getElementById("n").value

    const p =
    document.getElementById("p").value

    const k =
    document.getElementById("k").value

    const ph =
    document.getElementById("ph").value

    const state =
    document.getElementById("state").value

    const district =
    document.getElementById("district").value


    // =====================================
    // EMPTY CHECK
    // =====================================

    if(!n || !p || !k || !ph){

        alert(
            "Please fill all input fields"
        )

        return false
    }


    if(!state){

        alert(
            "Please select state"
        )

        return false
    }


    if(!district){

        alert(
            "Please select district"
        )

        return false
    }


    // =====================================
    // RANGE CHECK
    // =====================================

    if(n < 0 || n > 140){

        alert(
            "Nitrogen value must be between 0-140"
        )

        return false
    }


    if(p < 0 || p > 145){

        alert(
            "Phosphorus value must be between 0-145"
        )

        return false
    }


    if(k < 0 || k > 205){

        alert(
            "Potassium value must be between 0-205"
        )

        return false
    }


    if(ph < 0 || ph > 14){

        alert(
            "pH value must be between 0-14"
        )

        return false
    }


    return true
}



// =========================================
// PREDICT CROP
// =========================================

async function predictCrop(){

    // =====================================
    // VALIDATE
    // =====================================

    if(!validateInputs()){

        return
    }


    try{

        // =================================
        // SHOW LOADING
        // =================================

        document.getElementById(
            "loading"
        ).classList.remove("hidden")


        // =================================
        // INPUTS
        // =================================

        const n =
        document.getElementById("n").value

        const p =
        document.getElementById("p").value

        const k =
        document.getElementById("k").value

        const ph =
        document.getElementById("ph").value

        const state =
        document.getElementById("state").value

        const district =
        document.getElementById("district").value

        const soil =
        document.getElementById("soil").value


        // =================================
        // LOCATION
        // =================================

        navigator.geolocation.getCurrentPosition(

            async(position)=>{

                try{

                    const lat =
                    position.coords.latitude

                    const lon =
                    position.coords.longitude


                    // =========================
                    // API
                    // =========================

                    const response = await fetch(

                        '/predict',

                        {

                            method:'POST',

                            headers:{

                                'Content-Type':
                                'application/json'
                            },

                            body:JSON.stringify({

                                n:n,

                                p:p,

                                k:k,

                                ph:ph,

                                state:state,

                                district:district,

                                soil:soil,

                                lat:lat,

                                lon:lon
                            })
                        }
                    )


                    const result =
                    await response.json()


                    // =========================
                    // HIDE LOADING
                    // =========================

                    document.getElementById(
                        "loading"
                    ).classList.add("hidden")


                    // =========================
                    // ERROR
                    // =========================

                    if(result.error){

                        alert(result.error)

                        return
                    }


                    // =========================
                    // SAVE RESULT
                    // =========================

                    localStorage.setItem(

                        "cropResult",

                        JSON.stringify(result)
                    )


                    // =========================
                    // REDIRECT
                    // =========================

                    window.location.href =
                    "/result"

                }

                catch(error){

                    console.log(error)

                    alert(
                        "Prediction failed"
                    )

                    document.getElementById(
                        "loading"
                    ).classList.add("hidden")
                }
            }
        )

    }

    catch(error){

        console.log(error)

        alert(
            "Something went wrong"
        )

        document.getElementById(
            "loading"
        ).classList.add("hidden")
    }
}



// =========================================
// CLEAR DATA
// =========================================

function clearData(){

    document.getElementById(
        "n"
    ).value = ""

    document.getElementById(
        "p"
    ).value = ""

    document.getElementById(
        "k"
    ).value = ""

    document.getElementById(
        "ph"
    ).value = ""


    document.getElementById(
        "state"
    ).selectedIndex = 0


    document.getElementById(
        "district"
    ).selectedIndex = 0


    document.getElementById(
        "soil"
    ).selectedIndex = 0
}



// =========================================
// START
// =========================================

window.onload = function(){

    loadIndiaData()

    loadWeather()
}