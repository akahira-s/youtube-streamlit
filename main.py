import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.04)

    # print(i)
    # time.sleep(1)
'Done!!!!!!!'

left_colum, right_colum = st.columns(2)
button = left_colum.button('右カラムに文字を表示')
if button:
    right_colum.write('ここは右カラム')


expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')



# text = st.sidebar.text_input('あなたの趣味を教えて下さい')
# 'あなたの趣味:',text

# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

# 'コンディション:', condition


# if st.checkbox('show Image'):
#     img = Image.open('232514.jpg')
#     st.image(img, caption='siori', use_column_width=True)
