import streamlit as st
import pickle
import pandas as pd
import numpy as np
from catboost import CatBoostRegressor



pipe = pickle.load(open('catboost_model.pkl','rb'))
st.title('Clay Predictor')


Coarse = st.number_input('Coarse')
cacl2ph = st.number_input('cacl2ph')
h2oph = st.number_input('h2oph')
EC = st.number_input('EC')
OC = st.number_input('OC')
CaCO3 = st.number_input('CaCO3')
P = st.number_input('P')
N = st.number_input('N')
K = st.number_input('K')
Soil_Stones=st.number_input('Soil_Stones')


# 'pH(CaCl2)':[pH(CaCl2)],'pH(H2O)':[pH(H2O)],
if st.button('Predict'):
      input=pd.DataFrame({'Coarse':[Coarse],'cacl2ph':[cacl2ph],'h2oph':[h2oph],'EC':[EC],'OC':[OC],'CaCO3':[CaCO3],'P':[P],'N':[N],'K':[K],'Soil_Stones':[Soil_Stones]})
      result = pipe.predict(input)
      st.success('THE CLAY FOR GIVEN DATA WILL BE {}'.format(result))
# st.header(result)
