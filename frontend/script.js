const API_BASE_URL =
    "http://127.0.0.1:8000";


// =====================================================
// Page Navigation
// =====================================================

const pages =
    document.querySelectorAll(".page");

const navButtons =
    document.querySelectorAll(".nav-button");


function showPage(pageId) {

    pages.forEach(function (page) {

        page.classList.remove(
            "active-page"
        );

    });


    const selectedPage =
        document.getElementById(pageId);


    if (selectedPage) {

        selectedPage.classList.add(
            "active-page"
        );

    }


    navButtons.forEach(function (button) {

        button.classList.remove("active");


        if (
            button.dataset.page === pageId
        ) {

            button.classList.add("active");

        }

    });


    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });


    if (
        pageId === "historyPage"
    ) {

        loadPredictionHistory();

    }

}


// Navigation buttons

navButtons.forEach(function (button) {

    button.addEventListener(
        "click",
        function () {

            showPage(
                button.dataset.page
            );

        }
    );

});


// =====================================================
// Form Elements
// =====================================================

const predictionForm =
    document.getElementById(
        "predictionForm"
    );


const predictButton =
    document.getElementById(
        "predictButton"
    );


// =====================================================
// Prediction Page Elements
// =====================================================

const probabilityCircle =
    document.getElementById(
        "probabilityCircle"
    );


const probabilityValue =
    document.getElementById(
        "probabilityValue"
    );


const scaleProbability =
    document.getElementById(
        "scaleProbability"
    );


const probabilityBar =
    document.getElementById(
        "probabilityBar"
    );


const predictionBadge =
    document.getElementById(
        "predictionBadge"
    );


const predictionResultText =
    document.getElementById(
        "predictionResultText"
    );


// =====================================================
// Buttons
// =====================================================

const newPredictionButton =
    document.getElementById(
        "newPredictionButton"
    );


const viewHistoryButton =
    document.getElementById(
        "viewHistoryButton"
    );


const refreshHistoryButton =
    document.getElementById(
        "refreshHistoryButton"
    );


// =====================================================
// History Elements
// =====================================================

const historyBody =
    document.getElementById(
        "historyBody"
    );


const historyStatus =
    document.getElementById(
        "historyStatus"
    );


// =====================================================
// Get Customer Data
// =====================================================

function getCustomerData() {

    return {

        gender:
            document.getElementById(
                "gender"
            ).value,


        SeniorCitizen:
            Number(
                document.getElementById(
                    "seniorCitizen"
                ).value
            ),


        Partner:
            document.getElementById(
                "partner"
            ).value,


        Dependents:
            document.getElementById(
                "dependents"
            ).value,


        tenure:
            Number(
                document.getElementById(
                    "tenure"
                ).value
            ),


        PhoneService:
            document.getElementById(
                "phoneService"
            ).value,


        MultipleLines:
            document.getElementById(
                "multipleLines"
            ).value,


        InternetService:
            document.getElementById(
                "internetService"
            ).value,


        OnlineSecurity:
            document.getElementById(
                "onlineSecurity"
            ).value,


        OnlineBackup:
            document.getElementById(
                "onlineBackup"
            ).value,


        DeviceProtection:
            document.getElementById(
                "deviceProtection"
            ).value,


        TechSupport:
            document.getElementById(
                "techSupport"
            ).value,


        StreamingTV:
            document.getElementById(
                "streamingTV"
            ).value,


        StreamingMovies:
            document.getElementById(
                "streamingMovies"
            ).value,


        Contract:
            document.getElementById(
                "contract"
            ).value,


        PaperlessBilling:
            document.getElementById(
                "paperlessBilling"
            ).value,


        PaymentMethod:
            document.getElementById(
                "paymentMethod"
            ).value,


        MonthlyCharges:
            Number(
                document.getElementById(
                    "monthlyCharges"
                ).value
            ),


        TotalCharges:
            Number(
                document.getElementById(
                    "totalCharges"
                ).value
            )

    };

}


// =====================================================
// Predict Churn
// =====================================================

predictionForm.addEventListener(
    "submit",
    async function (event) {

        event.preventDefault();


        predictButton.disabled =
            true;


        predictButton.innerHTML =
            "<span>Analyzing...</span>";


        const customerData =
            getCustomerData();


        try {

            const response =
                await fetch(
                    `${API_BASE_URL}/predict-churn`,
                    {

                        method: "POST",

                        headers: {

                            "Content-Type":
                                "application/json"

                        },

                        body:
                            JSON.stringify(
                                customerData
                            )

                    }
                );


            const data =
                await response.json();


            if (!response.ok) {

                throw new Error(
                    data.detail ||
                    data.message ||
                    "Prediction failed."
                );

            }


            displayPrediction(data);


            // Move to result page

            showPage(
                "resultPage"
            );


            // Refresh history

            loadPredictionHistory();

        }


        catch (error) {

            alert(
                "Unable to get prediction.\n\n" +
                error.message
            );


            console.error(
                "Prediction error:",
                error
            );

        }


        finally {

            predictButton.disabled =
                false;


            predictButton.innerHTML =
                "<span>Predict Churn</span>" +
                '<span class="button-arrow">→</span>';

        }

    }
);


// =====================================================
// Display Prediction
// =====================================================

function displayPrediction(data) {

    const probability =
        Number(
            data.churn_probability
        );


    const percentage =
        Math.max(
            0,
            Math.min(
                100,
                probability * 100
            )
        );


    const formatted =
        percentage.toFixed(2) + "%";


    // Probability text

    probabilityValue.textContent =
        formatted;


    scaleProbability.textContent =
        formatted;


    // Progress bar

    probabilityBar.style.width =
        `${percentage}%`;


    // Probability circle

    const degrees =
        percentage * 3.6;


    probabilityCircle.style.background =
        `
        conic-gradient(
            var(--cyan) 0deg,
            var(--accent) ${degrees}deg,
            #1b263a ${degrees}deg,
            #1b263a 360deg
        )
        `;


    // Prediction result

    if (
        data.churn_prediction === 1
    ) {

        predictionBadge.textContent =
            "HIGHER CHURN RISK";


        predictionBadge.className =
            "prediction-badge churn";


        predictionResultText.textContent =
            "Customer is likely to churn";

    }


    else {

        predictionBadge.textContent =
            "LOWER CHURN RISK";


        predictionBadge.className =
            "prediction-badge stay";


        predictionResultText.textContent =
            "Customer is unlikely to churn";

    }

}


// =====================================================
// New Prediction
// =====================================================

newPredictionButton.addEventListener(
    "click",
    function () {

        predictionForm.reset();


        showPage(
            "formPage"
        );

    }
);


// =====================================================
// View History
// =====================================================

viewHistoryButton.addEventListener(
    "click",
    function () {

        showPage(
            "historyPage"
        );

    }
);


// =====================================================
// Load Prediction History
// =====================================================

async function loadPredictionHistory() {

    historyStatus.textContent =
        "Loading prediction history...";


    try {

        const response =
            await fetch(
                `${API_BASE_URL}/predictions`
            );


        const predictions =
            await response.json();


        if (!response.ok) {

            throw new Error(
                "Unable to load prediction history."
            );

        }


        historyBody.innerHTML =
            "";


        if (
            !Array.isArray(
                predictions
            ) ||
            predictions.length === 0
        ) {

            historyStatus.textContent =
                "No predictions have been recorded yet.";


            historyBody.innerHTML = `

                <tr>

                    <td
                        colspan="11"
                        class="empty-history"
                    >
                        No prediction history available.
                    </td>

                </tr>

            `;

            return;

        }


        historyStatus.textContent =
            `${predictions.length} prediction(s) stored in MySQL`;


        predictions.forEach(
            function (prediction) {

                const row =
                    document.createElement(
                        "tr"
                    );


                const result =
                    prediction.churn_prediction === 1
                        ? "Likely to Churn"
                        : "Unlikely to Churn";


                const resultClass =
                    prediction.churn_prediction === 1
                        ? "prediction-churn"
                        : "prediction-stay";


                const probability =
                    (
                        Number(
                            prediction.churn_probability
                        ) * 100
                    ).toFixed(2);


                row.innerHTML = `

                    <td>
                        ${prediction.id}
                    </td>

                    <td>
                        ${prediction.gender}
                    </td>

                    <td>
                        ${prediction.tenure}
                    </td>

                    <td>
                        ${prediction.internet_service ?? "-"}
                    </td>

                    <td>
                        ${prediction.online_security ?? "-"}
                    </td>

                    <td>
                        ${prediction.tech_support ?? "-"}
                    </td>

                    <td>
                        ${prediction.contract}
                    </td>

                    <td>
                        ${prediction.payment_method ?? "-"}
                    </td>

                    <td>
                        ${Number(
                            prediction.monthly_charges
                        ).toFixed(2)}
                    </td>

                    <td class="${resultClass}">
                        ${result}
                    </td>

                    <td>
                        ${probability}%
                    </td>

                `;


                historyBody.appendChild(
                    row
                );

            }
        );

    }


    catch (error) {

        historyStatus.textContent =
            "Unable to load prediction history.";


        historyBody.innerHTML = `

            <tr>

                <td
                    colspan="11"
                    class="empty-history"
                >
                    Please make sure the FastAPI
                    server is running.
                </td>

            </tr>

        `;


        console.error(
            "History error:",
            error
        );

    }

}


// =====================================================
// Refresh History
// =====================================================

refreshHistoryButton.addEventListener(
    "click",
    function () {

        loadPredictionHistory();

    }
);