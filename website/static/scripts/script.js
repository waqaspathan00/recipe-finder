function addIngredientInput(){
    const inputGroup = document.createElement("div");
    inputGroup.className = "input-group"
    const ingredientInput = document.createElement("input");
    ingredientInput.type = "text";
    ingredientInput.name = "ingredients[]";
    ingredientInput.placeholder = "Ingredient";
    ingredientInput.className = "form-control"; // set the CSS class
    inputGroup.appendChild(ingredientInput)

    const element = document.getElementById("ingredients-form");
    element.appendChild(inputGroup);
}

