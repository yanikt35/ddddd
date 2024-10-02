import streamlit as st

def taco_bar_calculator(num_people, meat_type, selected_vegetables):
    # Ingredients needed per person (grams) and prices per unit
    meat_per_person = {
        "ground beef": (184.0, 3.5),  # Ground beef (grams, price per pound)
        "shrimp": (184.0, 6.0),       # Shrimp
        "hamburger": (142.0, 4.0),    # Hamburger meat
        "chicken": (156.0, 3.0),      # Chicken
        "pork": (198.0, 5.0)          # Pork (Carnitas)
    }

    # Check meat type
    if meat_type not in meat_per_person:
        return "Invalid meat type. Please choose from: ground beef, shrimp, hamburger, chicken, pork"

    # Calculate total amounts and prices
    meat_weight, meat_price_per_lb = meat_per_person[meat_type]
    total_meat_mass = meat_weight * num_people
    total_meat_price = (total_meat_mass / 453.592) * meat_price_per_lb  # Convert grams to pounds

    # Define other ingredients and their prices
    ingredients = {
        "cheddar cheese": (35.4 * num_people, 2.5),  # (grams, price per pound)
        "monterey cheese": (21.3 * num_people, 3.0),
        "sour cream": (56.7 * num_people, 1.5),
        "guacamole": (51.0 * num_people, 4.0),
        "taco sauce": (65.2 * num_people, 2.0),
        "pico de gallo": (45.4 * num_people, 3.0),
        "taco shells": (2 * num_people, 0.5),
        "tortillas": (num_people, 0.3),
        "rice": (70.9 * num_people, 1.0)
    }

    # Define vegetable prices
    vegetable_prices = {
        "lettuce": (36.9 * num_people, 1.0),  # (grams, price per pound)
        "onions": (25.5 * num_people, 0.8),
        "beans": (31.2 * num_people, 1.2),
        "refried beans": (62.4 * num_people, 1.5),
        "tomatoes": (51.0 * num_people, 1.0),
        "olives": (22.7 * num_people, 2.0),
        "bell pepper": (56.7 * num_people, 1.5)
    }

    # Calculate total prices for other ingredients
    total_prices = {}
    for ingredient, (weight, price_per_lb) in ingredients.items():
        total_price = (weight / 453.592) * price_per_lb  # Convert grams to pounds
        total_prices[ingredient] = total_price

    # Calculate total prices for vegetables
    total_vegetable_prices = {}
    for vegetable in selected_vegetables:
        if vegetable in vegetable_prices:
            weight, price_per_lb = vegetable_prices[vegetable]
            total_price = (weight / 453.592) * price_per_lb  # Convert grams to pounds
            total_vegetable_prices[vegetable] = total_price

    # Total price calculation
    total_price = total_meat_price + sum(total_prices.values()) + sum(total_vegetable_prices.values())
    
    # Price per taco calculation assuming each person eats two tacos
    price_per_taco = total_price / (num_people * 2)

    return {
        'total_meat_mass': total_meat_mass,
        'total_meat_price': total_meat_price,
        'total_prices': total_prices,
        'total_vegetable_prices': total_vegetable_prices,
        'total_price': total_price,
        'price_per_taco': price_per_taco
    }

# Streamlit app layout
st.title("Taco Bar Calculator")

# Input number of people
num_people = st.number_input("Enter the number of people:", min_value=1)

# Select meat type
meat_type = st.selectbox("Choose your meat type:", options=list(meat_per_person.keys()))

# Select vegetables
vegetable_options = list(vegetable_prices.keys())
selected_vegetables = st.multiselect("Select your vegetables:", options=vegetable_options)

# Calculate button
if st.button("Calculate"):
    results = taco_bar_calculator(num_people, meat_type, selected_vegetables)

    # Display results
    st.subheader("Results")
    st.write(f"Total meat mass: {results['total_meat_mass']:.1f} g")
    st.write(f"Total meat price: ${results['total_meat_price']:.2f}")

    for ingredient in results['total_prices']:
        st.write(f"{ingredient.capitalize()}: Total price: ${results['total_prices'][ingredient]:.2f}")

    for vegetable in selected_vegetables:
        if vegetable in results['total_vegetable_prices']:
            st.write(f"{vegetable.capitalize()}: Total price: ${results['total_vegetable_prices'][vegetable]:.2f}")

    st.write(f"Total cost for the Taco Bar: ${results['total_price']:.2f}")
    st.write(f"Price per taco: ${results['price_per_taco']:.2f}")
