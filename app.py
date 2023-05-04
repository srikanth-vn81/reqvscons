
# data analysis and wrangling
import numpy as np
import pandas as pd
import streamlit as st
from datetime import date

#from st_aggrid import AgGrid
#from st_aggrid.grid_options_builder import GridOptionsBuilder
#from st_aggrid.shared import JsCode

#from functionforDownloadButtons import download_button

# File Uploader

#from PIL import Image
#with st.sidebar.container():
	#image = Image.open("C:\\Users\\srikanthve\\Desktop\\Capture.JPG")
	#st.image(image)


uploaded_file = st.file_uploader(
        "",
        key="1",
        
    )
if uploaded_file is not None:
	#file_container = st.expander("Check your uploaded .csv")
	df = pd.read_csv(uploaded_file)
	uploaded_file.seek(0)
	#file_container.write(shows)
	
	
else:
	st.info(
            f"""
                👆 Upload a .csv file)
                """

        )

	st.stop()


#if st.button("RUN"):
limit = 0
df=df[(df['Gross_RM_WriteOff_value']>limit)]
df=df.loc[(df.SBU == "FF")]

grouper = df.groupby(['ItemCode','Itemgroup','Prodgroup','BuyerDivision','Description','Colur_Size','Plant'])
df =grouper[['Production_Savings_Requirement_vs_ConsumptionValue','Quantity']].sum().reset_index()
df=df[(df['Production_Savings_Requirement_vs_ConsumptionValue']>limit)]

df_final = df=df[(df['Production_Savings_Requirement_vs_ConsumptionValue']>100)]

df_final.sort_values("Production_Savings_Requirement_vs_ConsumptionValue", axis=0, ascending=False, inplace=True)


df_final['systemdate']=date.today()
df_final['systemdate']= pd.to_datetime(df_final["systemdate"])
df_final['weekno'] = df_final['systemdate'].dt.week
st.write(df_final)

#from st_aggrid import GridUpdateMode, DataReturnMode

#gb = GridOptionsBuilder.from_dataframe(df_final)
# enables pivoting on all columns, however i'd need to change ag grid to allow export of pivoted/grouped data, however it select/filters groups
#gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)
#gb.configure_selection(selection_mode="multiple", use_checkbox=True)
#gb.configure_side_bar()  # side_bar is clearly a typo :) should by sidebar
#gridOptions = gb.build()

#response = AgGrid(
    #df_final,
    #gridOptions=gridOptions,
    #enable_enterprise_modules=True,
    #update_mode=GridUpdateMode.MODEL_CHANGED,
    #data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
    #fit_columns_on_grid_load=False,
	
#)
#if st.button('Download'):
	#df_final.to_csv(r'C:\Users\srikanthve\Downloads\dineshshare.csv')
	#st.success("Downloaded Successfully")
#else:
	#st.write("")

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(df_final)

st.download_button(
    label="Download",
    data=csv,
    file_name='dineshshare.csv',
    mime='text/csv',
)

# In[ ]:




