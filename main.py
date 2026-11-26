from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. Define what data the frontend needs to send us
class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operation: str  # This will be "+", "-", "*", or "/"

# 2. Create the POST route to handle the math
@app.post("/calculate")
def calculate(request: CalculationRequest):
    
    # Check which operation the user wants
    if request.operation == "+":
        result = request.num1 + request.num2
    elif request.operation == "-":
        result = request.num1 - request.num2
    elif request.operation == "*":
        result = request.num1 * request.num2
    elif request.operation == "/":
        if request.num2 == 0:
            return {"error": "Cannot divide by zero!"}
        result = request.num1 / request.num2
    else:
        return {"error": "Invalid operation. Use +, -, *, or /"}

    # Send the answer back to the frontend
    return {
        "num1": request.num1,
        "num2": request.num2,
        "operation": request.operation,
        "result": result
    }