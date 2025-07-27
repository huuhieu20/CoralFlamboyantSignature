import streamlit as st

st.title("🔐 Đăng ký tài khoản")

username = st.text_input("1️⃣ Tài khoản")
password = st.text_input("2️⃣ Mật khẩu", type="password")
confirm_password = st.text_input("3️⃣ Nhập lại mật khẩu", type="password")
full_name = st.text_input("4️⃣ Tên người dùng")
email = st.text_input("5️⃣ Email")

progress = 0
fields = [username, password, confirm_password, full_name, email]

for field in fields:
    if field:
        progress += 20

st.progress(progress)

if st.button("Đăng ký"):
    if not all(fields):
        st.warning("❗ Vui lòng điền đầy đủ tất cả các trường.")
    elif password != confirm_password:
        st.error("❌ Mật khẩu không khớp.")
    else:
        st.success("✅ Đăng ký thành công!")
        st.balloons()
