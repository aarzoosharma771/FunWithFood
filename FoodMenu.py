import streamlit as st 
from streamlit_option_menu import option_menu
import random

def restrauntloc():
    st.markdown("<h2 style ='color:blue';>Location of Mars Resort-</h2>",unsafe_allow_html=True)
    st.markdown('<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3490.84443146881!2d77.63741867472132!3d28.96233836902896!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390c675c5b03cdbb%3A0xd1a4de7f7e67c3d3!2sMars%20Resorts!5e0!3m2!1sen!2sin!4v1744284643690!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>',unsafe_allow_html=True)
    st.header("Contact Us:",divider=True)
    st.markdown("You can reach us at:")
    st.markdown("**Email: marsresort@gmail.com")
    st.markdown("**Phone: 9876054321")
    st.markdown("**Address: MarsResorts,Meerut,India")
    st.image("mars3.jpeg",caption="Reach out to us!")


def restmenu():
    st.markdown("<h1 style='text-align: center';>Food Menu</h1",unsafe_allow_html=True)
    
    col1,col2, = st.columns(2)
    with col1:
     st.subheader("MAIN COURSE",divider=True)
     st.image("main.jpeg")
     st.text("Cheese Burger: 35")
     st.text("Cheesse Sandwich: 25") 
     st.text("Chicken Burger: 40") 
     st.text("Spicy Chicken: 50") 
     st.text("Hot Dog: 40") 
    with col2:
     st.subheader("APPETIZERS",divider=True)
     st.image("app.jpeg")
     st.text("Fruit Salad: 20")
     st.text("Cocktails: 12")
     st.text("Nuggets: 17")
     st.text("Sandwich: 20")
     st.text("French Fries: 30")
    col3,col4 = st.columns(2)
    with col3:
     st.subheader("SNACKS",divider=True)
     st.image("pakodA.jpeg")
     st.text("French Fries: 130")
     st.text("Mix Pakoda: 145")
     st.text("Paneer Pakoda: 190")
     st.text("Cheese Balls: 210")
     st.text("Paneer Fingers: 230")
    
    with col4:
        
     st.subheader("DOSA",divider=True)
     st.image("dosa.jpeg")
     st.text("Sada Dosa: 50")
     st.text("Masal Dosa: 70")
     st.text("Cheese Masala Dosa: 105")
     st.text("Paneer Masala Dosa: 110")
     st.text("Pizza Dosa: 220")
     st.text("Mashroom Chilli Dosa: 250")
    col5,col6 = st.columns(2)
    with col5:
     st.subheader("BEVERAGE",divider=True)
     st.image("cold.jpeg")
     st.text("Milk Shake: 34")
     st.text("Iced Tea: 22")
     st.text("Orange Juice: 24")
     st.text("Lemon Tea: 33")
     st.text("Iced Coffee: 23")
     
    with col6:
      st.subheader("ESPRESSO",divider=True)
      st.image("coffee.jpeg")
      st.text("Cappuccino: 50")
      st.text("Latte: 50") 
      st.text("Mocha: 30")
      st.text("French Press: 35") 
      st.text("Macchiato: 70")


def selectpaybill():
    st.header("Select Your Item",divider=True)
    
    menu_items={
        
        "Cheese Burger": 35,
        "Cheesse Sandwich": 25,
        "Chicken Burger": 30,
        "Spicy Chicken": 30,
        "Hot Dog": 40,
        "Fruit Salad": 20,
        "Cocktails": 12,
        "Nuggets": 17,
        "Sandwich": 20,
        "French Fries": 30,
        'French Fries': 130,
        'Mix Pakoda': 145,
        'Paneer Pakoda': 190,
        'Cheese Balls': 210,
        'Paneer Fingers': 230,
        'Sada Dosa': 50,
        'Masal Dosa': 70,
        'Cheese Masala Dosa': 105,
        'Paneer Masala Dosa': 110,
        'Pizza Dosa': 220,
        'Mashroom Chilli Dosa': 250,
        "Milk Shake": 34,
        "Iced Tea": 22,
        "Orange Juice": 24,
        "Lemon Tea": 33,
        "Iced Coffee": 23,
        "Cappuccino": 30,
        "Latte": 33,
        "Mocha": 25,
        "French Press": 28,
        "Macchiato": 32,
    }
      
    total = 0
    selected_items = st.multiselect("Select items",list(menu_items.keys()))
    quantities={}
    if selected_items:
      st.subheader("Select quantity for each item")
      for item in selected_items:
          qty = st.number_input(f"{item}(plates)",min_value =1,max_value=100,value=1,step=1)
          quantities[item]=qty
    st.markdown("<h2 style ='color:green';>Receipt-</h2>",unsafe_allow_html=True)
    for item in selected_items:
          price = menu_items[item]
          total+=price*quantities[item]
          st.write(f"{item}:{price} ({quantities[item]}Plate)")
    
    
    if st.subheader(f"Total Bill:{total}"):
         if total!=0 and total<=600:
           if st.button("Confirm Ordered"):
             st.success("Ordered Confirmed! Thankyou")
         elif total==0:
            if st.button("No Ordered"):
              st.success("No Order")
         elif total>600:
            if st.button("Confirm Ordered"):
             st.success("Confirm Order! Congratulation you've earned a reward because your total Amount is more than 600")
             st.success("Your discount is 50 Rupees")
             st.subheader(f"Total Bill:{total-50}")  


def quiz():
    st.header("Quiz",divider=True)
    questions = [{"text": "Que1. Which fruit has its seeds on the outside____.","answer": "C"},
    {"text":"Que2. Which spice is made from dried flower buds?","answer":"B"},
    {"text":"Que3. 'Rasgulla' is a famous sweet from which India state?","answer":"B"},
    {"text":"Que4. 'Pav Bhaji' is a popular street food from which Indian city?","answer":"D"},
    {"text":"Que5. Which spice is known as the 'Queen of Spices'?","answer":"C"}
   ]
    options=[["A. Kiwi","B. Raspberry","C. Strawberry","D. Blueberry"],
         ["A. Cinnamon","B. Clove","C. Cardamom","D. Nutmeg"],
         ["A. Gujrat","B. West Bengal","C. Rajasthan","D. Maharahtra"],
         ["A. Delhi","B. Chennai","C. Hyderabad","D. Mumbai"],
         ["A. Pepper","B. Clove","C. Cardamom","D. Cinnamon"]
        ]
    
    score=0
    for i,q in enumerate(questions):
        st.markdown(q["text"])
        user_answer = st.radio("choose an option:",options[i])
        if user_answer.startswith(q["answer"]):
         score+=1
    
    if st.button("Submit"):
        st.subheader(f"Your Total Score:- {score}/{len(questions)}")
        if score==4:
         st.subheader(f"Prize:- You won the 50 Rupees")
        elif score==5:
          st.subheader(f"Prize:- You won the 100 Rupees")


def game():
    st.markdown("<h1 style ='color:orange';>Play The Game-</h1>",unsafe_allow_html=True) 
    st.header("Guess the Number Game:",divider=True)
    if "number" not in st.session_state:
        st.session_state.number = random.randint(1,20)
        st.session_state.attempts = 0
    guess = st.number_input("Enter a number between 1 and 20:",min_value=1,max_value=20,step=1)
    if st.button("Guess"):
         st.session_state.attempts+=1
         
         if guess == st.session_state.number:
            reward =0
           
            if st.session_state.attempts==1:
             reward =50
           
            elif st.session_state.attempts == 2:
             reward =25
           
            st.success(f"Correct! You guessed it in {st.session_state.attempts} attempts.")
            if reward>0:
             st.info(f"You Won Rupees {reward}!")
            st.button("Play Again")
            del st.session_state["number"]
            del st.session_state["attempts"]
         
         elif guess<st.session_state.number:
          st.warning("Too low! Try Again.")
         
         else:
          st.warning("Too high! Try Again.")
   
        
def reserved_event():
  menu = { 
        "Cheese Burger": 35,
        "Cheesse Sandwich": 25,
        "Chicken Burger": 30,
        "Spicy Chicken": 30,
        "Hot Dog": 40,
        "Fruit Salad": 20,
        "Cocktails": 12,
        "Nuggets": 17,
        "Sandwich": 20,
        "French Fries": 30,
        'French Fries': 130,
        'Mix Pakoda': 145,
        'Paneer Pakoda': 190,
        'Cheese Balls': 210,
        'Paneer Fingers': 230,
        'Sada Dosa': 50,
        'Masal Dosa': 70,
        'Cheese Masala Dosa': 105,
        'Paneer Masala Dosa': 110,
        'Pizza Dosa': 220,
        'Mashroom Chilli Dosa': 250,
        "Milk Shake": 34,
        "Iced Tea": 22,
        "Orange Juice": 24,
        "Lemon Tea": 33,
        "Iced Coffee": 23,
        "Cappuccino": 30,
        "Latte": 33,
        "Mocha": 25,
        "French Press": 28,
        "Macchiato": 32,
    
   }    
  st.header("Reserved For Event-",divider=True)
  name = st.text_input("Enter your name: ")
  event = st.text_input("Enter your event (DD-MM-YYYY):")
  st.subheader("Select Food Items:-")
  selected_items=st.multiselect("Choose your Items:-",list(menu.keys()))
  quantities={}
  if selected_items:
      st.subheader("Select quantity for each item")
      for item in selected_items:
          qty = st.number_input(f"{item}(plates)",min_value =1,max_value=100,value=1,step=1)
          quantities[item]=qty
  if st.button("Generate Bill"):
      if name and event and selected_items:
          total = sum(menu[item]*quantities[item] for item in selected_items)
          st.success("Bill Generate")
          st.subheader("Final Bill",divider=True)
          st.write(f"Name:{name}")
          st.write(f"Reserved Event:{event}")
          st.subheader("Selected Items:")
          for item in selected_items:
              st.write(f"{item}:{menu[item]} ({quantities[item]}Plate)")
          st.subheader(f"Total Amount:{total}",)
          st.success("Your Event is Reserved!...")
      else:
           st.error("Please fill all fields and select at least one item")  

  
def feedback():
    st.markdown("<h1 style='text-align: center;'>Feedback</h1",unsafe_allow_html=True)
    
    st.subheader("We value your feedback ,Please leave your thought below:",divider=True)
    user_feedback=st.text_area("Your feedback",height=200)
    if st.button("Submit"):
        if user_feedback.strip():
            st.success("Thankyou for your feedback")


def about():
    st.header('Mars Resort',divider=True)
    st.image('newban.jpg')
    
    st.markdown("The Mars Resort in Meerut is a 5-star hotel offering a range of amenities including a garden, outdoor pool, restaurant, and a 24-hour front desk. It's known for its spacious and clean rooms, attentive staff, and convenient location on the main road, making it a popular choice for both business and leisure travelers. The resort also features a fitness center, a bar/lounge, and multiple food outlets. The Mars Group is promoted by Sanjay Narang and Rachna Narang.The contact number for Mars Resort in Meerut is +91-0121 407 5000.The Mars Resorts in Meerut is a luxury resort known for its lavish accommodations, premium amenities, fine dining, and beautiful decor, offering a serene and elegant escape with an outdoor pool and a focus on personalized guest service. ")
    st.image("mars2.jpeg")
    st.markdown("The Mars Resorts in Meerut offers a 5-star hotel experience with family rooms, private check-in and check-out, and free WiFi. Guests enjoy a fitness centre, outdoor swimming pool, terrace, and a lush garden.What are the check-in and check-out timings at Mars Resort? Check in starts at 2 PM in Mars Resort and check out timing is 11 AM. For early check-in or late check-out, you can contact the hotel directly. The front desk is available 24 hours a day for your help.Rooms feature air-conditioning, bathrobes, tea and coffee makers, pool or city views, and free toiletries. Additional amenities include a fitness room, 24-hour front desk, concierge service, and free on-site parking.")
    st.image("mars1.jpeg")
    st.markdown("[Visit Mars Resort Website](https://marsresorts.in/index.php)")
    st.markdown("[Visit Mars Resort Website about any Information](https://www.tripadvisor.in/Hotel_Review-g1162496-d25337234-Reviews-Mars_Resort-Meerut_Meerut_District_Uttar_Pradesh.html)")

with st.sidebar:
    st.header("Rastauraunt Management")
    selected = option_menu('Select From Here',['Restauraunt Location','Restauraunt Menu','SelectItem & PayBill','Quiz Prize','Play Game','Reserved Event','Feedback','About Restauraunt'])

if selected == 'Restauraunt Location':
    restrauntloc()

elif selected == 'Restauraunt Menu':
    restmenu()

elif selected == 'SelectItem & PayBill':
    selectpaybill()

elif selected == 'Quiz Prize':
    quiz()
    
elif selected == 'Play Game':
    game()
    
elif selected == 'Reserved Event':
    reserved_event()

elif selected == 'Feedback':
    feedback()

elif selected == 'About Restauraunt':
    about()
