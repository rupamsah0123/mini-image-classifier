// Get elements from the HTML page
const imageInput = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const predictButton = document.getElementById("predictButton");

const predictionText = document.getElementById("prediction");
const confidenceText = document.getElementById("confidence");


// --------------------------------------------------
// 1. Show image preview when user selects an image
// --------------------------------------------------

imageInput.addEventListener("change", function () {

    const file = imageInput.files[0];

    if (file) {

        const imageURL = URL.createObjectURL(file);

        preview.src = imageURL;

        preview.style.display = "block";

        predictionText.textContent = "";
        confidenceText.textContent = "";
    }
});


// --------------------------------------------------
// 2. Send image to FastAPI when Predict is clicked
// --------------------------------------------------

predictButton.addEventListener("click", async function () {

    const file = imageInput.files[0];

    // Check whether user selected an image
    if (!file) {

        alert("Please select an image first.");

        return;
    }


    // Disable button while prediction is running
    predictButton.disabled = true;

    predictButton.textContent = "Predicting...";


    // Create FormData
    const formData = new FormData();

    formData.append("file", file);


    try {

        // Send image to FastAPI
        const response = await fetch("/predict", {

            method: "POST",

            body: formData
        });


        // Convert response to JSON
        const result = await response.json();


        // Display prediction
        predictionText.textContent =
            "Prediction: " + result.prediction;


        // Display confidence
        confidenceText.textContent =
            "Confidence: " + result.confidence + "%";

    }

    catch (error) {

        console.error(error);

        predictionText.textContent =
            "Error: Could not connect to the server.";

        confidenceText.textContent = "";

    }


    // Enable button again
    predictButton.disabled = false;

    predictButton.textContent = "Predict Image";

});