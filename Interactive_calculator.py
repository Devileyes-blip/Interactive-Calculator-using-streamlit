import sympy
from sympy import *
import streamlit as st 
st.title("🧮 Interactive Calculator")
def cal():
    '''Will calculate '''
    if "history" not in st.session_state:
        st.session_state.history = {}

    inp = st.text_input("Enter the expression to calculate: ")
    a = symbols('x')
    if inp:
        option = st.radio("Select an operation:",["Simplify", "Solve", "Expand", "Solve for variable"])
        
        if option == "Solve":
            exp = sympify(inp).evalf()
        elif option == "Simplify":
            exp = factor(inp)
        elif option == "Expand":
            exp = expand(inp)
        else:
            # Will soon add solve for variable
            pass

        st.success(f"The answer is : {exp}")
        st.session_state.history[inp] = exp
        
        if st.toggle("Show History"):
            st.subheader("📜Calcultion History")
            for i, j in st.session_state.history.items():
                st.write(f"{i} = {j}")
               
cal()
