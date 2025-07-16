import streamlit as st
import pandas as pd
import altair as alt

# CSV 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

st.title("🌍 국가별 MBTI 상위 3 유형 시각화")
st.markdown("국가를 선택하면, 해당 국가에서 비율이 가장 높은 **MBTI 3가지 유형**을 보여드려요!")

# 국가 선택
country_list = df["Country"].unique().tolist()
selected_country = st.selectbox("국가를 선택하세요", country_list)

# 선택된 국가의 데이터 추출
if selected_country:
    row = df[df["Country"] == selected_country].iloc[0]
    mbti_scores = row.drop("Country").sort_values(ascending=False).head(3)

    chart_data = pd.DataFrame({
        "MBTI": mbti_scores.index,
        "비율": mbti_scores.values
    })

    st.subheader(f"📊 {selected_country}의 상위 3개 MBTI 유형")

    # Altair로 시각화
    chart = alt.Chart(chart_data).mark_bar().encode(
        x=alt.X("MBTI", sort="-y"),
        y="비율",
        color=alt.Color("MBTI", legend=None),
        tooltip=["MBTI", "비율"]
    ).properties(
        width=500,
        height=300
    )

    st.altair_chart(chart, use_container_width=True)

    st.markdown("---")
    st.caption("데이터 출처: uploaded MBTI 국가 분포 CSV")

