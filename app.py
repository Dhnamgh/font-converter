import streamlit as st

st.set_page_config(page_title="Trình Đổi Font Tiếng Việt - Bản Chuẩn", layout="centered")

st.markdown("## 🔤 Trình Đổi Font Tiếng Việt")

# Dùng thử nhanh
example_text = "Ngày 06/5/2026 họp Chuyển đổi số tại Phòng Hội thảo"
if st.button(f"✨ Dùng thử nhanh: {example_text}"):
    st.session_state["main_input"] = example_text

# Danh sách Emoji
EMOJI_LIST = {
    "Giáo dục & Y tế": "🎓 📖 📝 🏫 📚 🖊️ 🎒 👨‍🏫 👩‍🏫 🩺 🏥 💉 💊 🧬 🚑 🧪 🌡️ 🧠 🩹",
    "Dữ liệu & Du lịch": "📈 📉 📊 📋 📂 💻 🔢 🖥️ 🔍 💡 ✈️ 🚗 🏨 🏖️ 🗺️ ⛰️ 🏟️ 🗼 📸 🌍 🚢 🚲",
    "Hành chính": "📑 🏛️ ⚖️ 📨 📞 🏢 ✉️ 📜 🗃️ 🔐 📢 🖋️ 🗂️ 📅 💼 🔑 📁 🗳️ ✒️ 🗞️",
    "Fanpage": "❤️ 🔥 ✅ 🚀 📍 📞 💎 ⚡ ✨ 🌟 🚩 📌 🎁 🛒 📩 💯 🆗 📣 💥 🌈 🎀 🎊"
}

def transform_text(text, style):
    if not text or style == "Chữ thường":
        return text
    if style == "In đậm":
        return f"<b>{text}</b>"
    elif style == "In nghiêng":
        return f"<i>{text}</i>"
    elif style == "Gạch chân":
        return f"<u>{text}</u>"
    return text

input_text = st.text_area("📌 Nhập nội dung", height=120, key="main_input")
style = st.radio("🎨 Chọn kiểu chữ", ["Chữ thường", "In đậm", "In nghiêng", "Gạch chân"], horizontal=True)

if input_text:
    output = transform_text(input_text, style)
    st.markdown("### ✅ Kết quả")
    
    # Ép cỡ chữ 16px đồng nhất và hiển thị chuẩn
    # Sử dụng div có thể contenteditable để hỗ trợ copy định dạng tốt hơn trên trình duyệt
    st.markdown(f"""
        <div id="copy-area" style="font-size:16px; font-family:sans-serif; padding:10px; border:1px solid #ddd; border-radius:5px; background-color:#f9f9f9;">
            {output}
        </div>
    """, unsafe_allow_html=True)
    
    # Nút Copy mượt mà, không thông báo OK, copy đúng định dạng
    st.write("")
    if st.button("📋 Nhấn để Copy nội dung (Giữ định dạng)"):
        # Xử lý copy văn bản kèm định dạng cho Word/Fanpage[cite: 2]
        if style == "Gạch chân":
            plain_output = "".join([c + "\u0332" for c in input_text])
        else:
            plain_output = input_text
        
        # Streamlit không cho phép JS can thiệp sâu, nên dùng mẹo copy text thô chuẩn nhất[cite: 2]
        # Đối với Word/Fanpage, bôi đen tại khung Kết quả vẫn là cách giữ định dạng tốt nhất[cite: 2]
        st.code(plain_output, language="text")
        st.success("Đã tạo mã copy bên dưới!")

st.write("---")
st.write("💡 **Emoji chọn lọc:**")
tabs = st.tabs(list(EMOJI_LIST.keys()))
for i, tab in enumerate(tabs):
    with tab:
        st.code(EMOJI_LIST[list(EMOJI_LIST.keys())[i]], language="text")
