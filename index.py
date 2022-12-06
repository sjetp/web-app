import streamlit as st
st.write("First Web App")
with st.form("my_form"):
   st.write("Inside the form")
   slider_val1 = st.number_input("Insert a Number")
   slider_val2 = st.number_input("Insert a Number")
   checkbox_val = st.checkbox("Form checkbox")
   slider_val=slider_val1 + slider_val2
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")