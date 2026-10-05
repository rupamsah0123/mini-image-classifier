from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from PIL import Image
import io
import torch

from torchvision.models import resnet18, ResNet18_Weights


# --------------------------------------------------
# 1. Create FastAPI application
# --------------------------------------------------

app = FastAPI(title="Mini Image Classifier")


# --------------------------------------------------
# 2. Serve CSS and JavaScript files
# --------------------------------------------------

app.mount(
    "/css",
    StaticFiles(directory="css"),
    name="css"
)

app.mount(
    "/js",
    StaticFiles(directory="js"),
    name="js"
)


# --------------------------------------------------
# 3. Allow frontend requests
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# 4. Load pretrained ResNet-18 model
# --------------------------------------------------

weights = ResNet18_Weights.DEFAULT

model = resnet18(weights=weights)

model.eval()


# Image preprocessing
preprocess = weights.transforms()


# ImageNet class names
categories = weights.meta["categories"]


# --------------------------------------------------
# 5. Home page
# --------------------------------------------------

@app.get("/")
def home():
    return FileResponse("index.html")


# --------------------------------------------------
# 6. Health check
# --------------------------------------------------

@app.get("/health")
def health():
    return {
        "status": "ok"
    }


# --------------------------------------------------
# 7. Image prediction
# --------------------------------------------------

@app.post("/predict")
async def predict(file: UploadFile = File(...)):

    # Read uploaded image
    contents = await file.read()


    # Open image
    image = Image.open(
        io.BytesIO(contents)
    ).convert("RGB")


    # Preprocess image
    image_tensor = preprocess(image)


    # Add batch dimension
    image_tensor = image_tensor.unsqueeze(0)


    # Make prediction
    with torch.no_grad():

        output = model(image_tensor)


        # Convert model output to probabilities
        probabilities = torch.nn.functional.softmax(
            output[0],
            dim=0
        )


        # Get highest probability
        confidence, class_index = torch.max(
            probabilities,
            dim=0
        )


    # Get predicted class name
    label = categories[class_index.item()]


    # Convert confidence to percentage
    confidence_percentage = confidence.item() * 100


    # Return result
    return {
        "prediction": label,
        "confidence": round(
            confidence_percentage,
            2
        )
    }