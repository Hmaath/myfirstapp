import streamlit as st

# MBTI별 추천 미적분 단원 및 책/공부법
mbti_recommendations = {
    "INTJ": {
        "단원": "함수의 극한과 연속",
        "설명": "논리적 사고를 바탕으로 수학적 구조를 분석하는 데 적합해요.",
        "책": "개념원리 미적분 – 개념 정리에 집중하세요."
    },
    "INFP": {
        "단원": "미분의 활용",
        "설명": "창의적인 문제 상황에서 수학적 의미를 찾는 데 강점을 보여요.",
        "책": "쎈 미적분 – 다양한 응용 문제로 감성 자극!"
    },
    "ENTP": {
        "단원": "여러 가지 함수의 극한",
        "설명": "새로운 방식으로 접근하며 문제 해결을 즐깁니다.",
        "책": "수학의 정석 – 기초 개념을 실험처럼 탐구!"
    },
    "ISFJ": {
        "단원": "접선의 방정식",
        "설명": "정확하고 섬세하게 단계를 따라가는 데 적합해요.",
        "책": "마플 – 안정적인 개념 반복 중심 학습"
    },
    # 나머지 MBTI도 추가 가능 (예시는 4개만)
}

def main():
    st.title("📘 MBTI 기반 미적분 추천기")
    st.markdown("당신의 **MBTI**에 맞는 고3 **미적분 단원**과 책을 추천해드려요 💡")

    mbti_list = list(mbti_recommendations.keys())
    selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", mbti_list)

    if selected_mbti:
        rec = mbti_recommendations[selected_mbti]
        st.subheader("🔍 추천 결과")
        st.write(f"**추천 단원**: {rec['단원']}")
        st.write(f"**설명**: {rec['설명']}")
        st.write(f"**추천 교재 또는 공부법**: {rec['책']}")
        st.success("당신의 성향에 딱 맞는 공부 방식이에요! 😊")

    st.markdown("---")
    st.caption("Made with ❤️ by ChatGPT + Streamlit")

if __name__ == "__main__":
    main()
