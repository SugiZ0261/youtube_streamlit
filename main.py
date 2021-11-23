import  streamlit as st
import time

st.title('Streamlit入門 ~じゃんけん~') # タイトルの追加

st.write('プログレスバーの表示') 
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
	latest_iteration.text(f'Now Loading {i+1}%')
	bar.progress(i + 1)
	time.sleep(0.1)

'Done!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('じゃんけんしましょう！')
if button:
	right_column.write('じゃ〜んけ〜ん・・・')

expander1 = st.expander('グー！')
expander1.write('パー。あなたの負け。')
expander2 = st.expander('チョキ！')
expander2.write('グー。あなたの負け。')
expander3 = st.expander('パー！')
expander3.write('チョキ。あなたの負け。')
