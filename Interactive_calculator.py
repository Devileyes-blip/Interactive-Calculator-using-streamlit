import sympy
from sympy import *
import streamlit as st

st.title("🧮 Interactive Calculator")
def cal():
    '''Will calculate '''
    if "history" not in st.session_state:
        st.session_state.history = {}

    inp = st.text_input("Enter the expression to calculate: ")
    if inp:
        try:
            exp = sympify(inp).evalf()    #evalf() = Evaluate a symbolic expression and return the result in decimal (floating-point) form.
            if not exp.is_number:
                st.error("Enter correct value which is Integers or numbers...")
            else:
                st.success(f"The answer is : {exp}")
                st.session_state.history[inp] = exp
        except Exception as e:
            st.error(f"Error: {e}")
        if st.toggle("Show History"):
            st.subheader("📜Calcultion History")
            for i, j in st.session_state.history.items():
                st.write(f"{i} = {j}")
               
cal()
