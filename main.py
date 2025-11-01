import streamlit as st
brut=st.number_input("Brüt Maaş:")
ucret=st.checkbox("ücret geliri")
ucret=True
v158=158000*0.15
v330=(330000-158000)*0.20
v1200=(1200000-330000)*0.27
v4300=(4300000-1200000)*0.35
v1200b=(800000-330000)*0.27
v4300b=(4300000-800000)*0.35

if ucret:
    if brut<158000:
        vergi=brut*0.15
    elif brut<330000:
        vergi=v158+((brut-158000)*0.20)
    elif brut<1200000:
        vergi=v158+v330+((brut-330000)*0.27)
    elif brut<4300000:
        vergi=v158+v330+v1200+((brut-1200000)*0.35)
    else:
        vergi=v158+v330+v1200+v4300+((brut-4300000)*0.40)

else:
    if brut<158000:
        vergi=brut*0.15
    elif brut<330000:
        vergi=v158+((brut-158000)*0.20)
    elif brut<800000:
        vergi=v158+v330+((brut-330000)*0.27)
    elif brut<4300000:
        vergi=v158+v330+v1200b+((brut-800000)*0.35)
    else:
        vergi=v158+v330+v1200b+v4300b+((brut-4300000)*0.40)


st.write("Brüt:",brut,"Vergi:",vergi,"Net:",brut-vergi,"Ort Ay Net:",(brut-vergi)/12)