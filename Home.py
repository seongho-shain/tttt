import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
key_dict = json.loads(st.secrets["textkey"])
# Firebase 프로젝트의 서비스 계정 키 파일 경로
cred = credentials.Certificate(key_dict)

# Firebase 앱 초기화
if not firebase_admin._apps:
    # Firebase 앱이 초기화되지 않았으면 초기화
    firebase_admin.initialize_app(cred)
    print("Firebase 앱이 초기화되었습니다.")
else:
    # Firebase 앱이 이미 초기화되었으면 기존 앱 사용
    print("Firebase 앱이 이미 초기화되었습니다.")

# Firestore 클라이언트 생성
db = firestore.client()

st.title("회원 가입")

# 이름 입력 필드
name = st.text_input("이름")

# 비밀번호 입력 필드
password = st.text_input("비밀번호", type="password")

# 회원 가입 버튼
if st.button("회원 가입"):
    # 입력 값 유효성 검사 (필요에 따라 추가)
    if not name or not password:
        st.error("이름과 비밀번호를 모두 입력해주세요.")
    else:
        # Firestore에 데이터 저장
        try:
            db.collection('users').document(name).set({
                'name': name,
                'password': password
            })
            st.success("회원 가입 성공!")
        except Exception as e:
            st.error(f"회원 가입 실패: {e}")
