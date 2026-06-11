import starlette as st

st.title("COUNTER APP")

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("increament(+1)"):
    st.session_state.count+=1

st.metric(
    label = "current count",
    value = st.session_state.count
)       
