def taco_bar_calculator(num_people, meat_type, selected_vegetables):
    # ส่วนผสมที่ต้องการต่อคน (กรัม) และราคาต่อหน่วย
    meat_per_person = {
        "ground beef": (184.0, 3.5),  # เนื้อบด (กรัม, ราคาเป็นปอนด์)
        "shrimp": (184.0, 6.0),       # กุ้ง
        "hamburger": (142.0, 4.0),    # เนื้อแฮมเบอร์เกอร์
        "chicken": (156.0, 3.0),      # ไก่
        "pork": (198.0, 5.0)          # หมู (Carnitas)
    }

    # ตรวจสอบประเภทเนื้อ
    if meat_type not in meat_per_person:
        return "ประเภทเนื้อไม่ถูกต้อง กรุณาเลือกจาก: ground beef, shrimp, hamburger, chicken, pork"

    # คำนวณปริมาณรวมและราคา
    meat_weight, meat_price_per_lb = meat_per_person[meat_type]
    total_meat_mass = meat_weight * num_people
    total_meat_price = (total_meat_mass / 453.592) * meat_price_per_lb  # แปลงกรัมเป็นปอนด์

    # กำหนดส่วนผสมอื่น ๆ และราคาของพวกเขา
    ingredients = {
        "cheddar cheese": (35.4 * num_people, 2.5),  # (กรัม, ราคาเป็นปอนด์)
        "monterey cheese": (21.3 * num_people, 3.0),
        "sour cream": (56.7 * num_people, 1.5),
        "guacamole": (51.0 * num_people, 4.0),
        "taco sauce": (65.2 * num_people, 2.0),
        "pico de gallo": (45.4 * num_people, 3.0),
        "taco shells": (2 * num_people, 0.5),
        "tortillas": (num_people, 0.3),
        "rice": (70.9 * num_people, 1.0)
    }

    # กำหนดราคาผัก
    vegetable_prices = {
        "lettuce": (36.9 * num_people, 1.0),  # (กรัม, ราคาเป็นปอนด์)
        "onions": (25.5 * num_people, 0.8),
        "beans": (31.2 * num_people, 1.2),
        "refried beans": (62.4 * num_people, 1.5),
        "tomatoes": (51.0 * num_people, 1.0),
        "olives": (22.7 * num_people, 2.0),
        "bell pepper": (56.7 * num_people, 1.5)
    }

    # คำนวณราคาสำหรับส่วนผสมอื่น ๆ
    total_prices = {}
    for ingredient, (weight, price_per_lb) in ingredients.items():
        total_price = (weight / 453.592) * price_per_lb  # แปลงกรัมเป็นปอนด์
        total_prices[ingredient] = total_price

    # คำนวณราคาสำหรับผัก
    total_vegetable_prices = {}
    for vegetable in selected_vegetables:
        if vegetable in vegetable_prices:
            weight, price_per_lb = vegetable_prices[vegetable]
            total_price = (weight / 453.592) * price_per_lb  # แปลงกรัมเป็นปอนด์
            total_vegetable_prices[vegetable] = total_price

    # คำนวณราคารวมทั้งหมด
    total_price = total_meat_price + sum(total_prices.values()) + sum(total_vegetable_prices.values())
    
    # คำนวณราคาต่อทาโก้ โดยสมมติว่าทุกคนจะกินทาโก้ประมาณสองชิ้น
    price_per_taco = total_price / (num_people * 2)

    # แสดงผลลัพธ์
    print("\nยินดีต้อนรับสู่ Taco Bar Calculator!")
    print(f"จำนวนคน: {num_people}\n")
    
    print("🌮 ส่วนผสมหลัก")
    print(f"เลือกประเภทเนื้อ:\n{meat_type.capitalize()}\nมวลเนื้อ: {total_meat_mass:.1f} g")
    print(f"ราคารวมเนื้อ: ${total_meat_price:.2f}")

    for ingredient, (weight, _) in ingredients.items():
        print(f"{ingredient.capitalize()}: {weight:.1f} g, ราคารวม: ${total_prices[ingredient]:.2f}")

    # แสดงราคาผัก
    print("\nราคาผัก:")
    for vegetable in selected_vegetables:
        if vegetable in vegetable_prices:
            weight, price_per_lb = vegetable_prices[vegetable]
            total_price = (weight / 453.592) * price_per_lb  # แปลงกรัมเป็นปอนด์
            print(f"{vegetable.capitalize()}: {weight:.1f} g, ราคารวม: ${total_price:.2f}")

    # แสดงราคารวมและราคาต่อทาโก้
    print(f"\nราคารวมสำหรับ Taco Bar: ${total_price:.2f}")
    print(f"ราคาต่อทาโก้: ${price_per_taco:.2f}")

# ตัวอย่างการใช้งาน
num_people = int(input("ยินดีต้อนรับสู่ Taco Bar Calculator!\nกรุณากรอกจำนวนคน: "))  # จำนวนคน
meat_type = input("\nเลือกประเภทเนื้อของคุณ (ground beef, shrimp, hamburger, chicken, pork): ").lower()

# ขอให้ผู้ใช้เลือกผัก
print("\nเลือกผักของคุณ (แยกด้วยเครื่องหมายจุลภาค): lettuce, onions, beans, refried beans, tomatoes, olives, bell pepper")
vegetable_input = input("กรุณากรอกตัวเลือกของคุณ: ").lower()
selected_vegetables = [veg.strip() for veg in vegetable_input.split(",")]

# เรียกใช้ฟังก์ชันคำนวณ
taco_bar_calculator(num_people, meat_type, selected_vegetables)