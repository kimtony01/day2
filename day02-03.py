# random 모듈을 이용 1~45 중 중복 없는 번호 6개를 뽑고 
# 자료 구조 list(X), set(중복안됨), 버튼을 누르면 5세트 한번에 생성
# datetime 으로 생성 시간도 함께 보여준다

import streamlit as st
import random
from datetime import datetime

st.title('🎱로또 번호 자동 생성기')
st.caption('버튼을 누르면 1~45 사이의 중복 없는 번호 6개짜리 세트를 5개 만들어줍니다.')

st.markdown('---')

def lotto_one_set() -> list:
    """1~45 에서 중복 없이 번호 6개 뽑아 정렬된 리스트로 반환"""
    number = set()
    while len(number) < 6:
        number.add(random.randint(1, 45))
    return sorted(number)

def ball_color(n: int) -> str:
    """번호대별 로또공 색깔 이모지 반환"""
    if n <= 10:
        return '🟡'  # 노랑
    elif n <= 20:
        return '🔵'  # 파랑
    elif n <= 30:
        return '🔴'  # 빨강
    elif n <= 40:
        return '⚫'  # 검정
    else:
        return '🟢'  # 초록

submitted = st.button('✅ 5세트 번호 생성하기', key='lotto_button')

if submitted:
    now_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    st.write(f'생성 시각: **{now_str}**')

    for set_index in range(1, 6):
        lotto_num = lotto_one_set()
        balls = '  '.join([f'{ball_color(n)}**{n}**' for n in lotto_num])
        st.write(f'{set_index}세트 : {balls}')