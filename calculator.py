import streamlit as st
st.write("Commodity Calculator")
with st.form("commodity"):
    risk=st.number_input("Risk",value=100)
    option_type=st.selectbox('Type of Commodity', ('--Select--','Gold Petal','Silver Micro'))
    entry=st.number_input("Entry Price",value=1)
    stopLoss=st.number_input("Stop Loss",value=0)
    
    #calculation
    slDiff=entry-stopLoss
    quantity=risk/slDiff
    Target1_1=entry+slDiff
    Target1_2=entry+slDiff*2
    Target1_3=entry+slDiff*3

    #submit
    submit=st.form_submit_button("submit")
    if submit:
        st.error(option_type,icon='🥇')
        st.warning("SL Rupee per Share {0: .2f}".format(slDiff))
        st.info("Quantity {0: .2f}".format(quantity))
        st.write("Target")
        st.success("Target 1:1 >> {0: .2f}".format(Target1_1))
        st.success("Target 1:2 >> {0: .2f}".format(Target1_2))
        st.success("Target 1:3 >> {0: .2f}".format(Target1_3))




    
