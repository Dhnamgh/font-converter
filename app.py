import streamlit as st

st.set_page_config(page_title="Trình Đổi Font Tiếng Việt - Bản Full", layout="centered")

# Phục hồi giao diện đầy đủ
st.markdown("## 🔤 Trình Đổi Font Tiếng Việt")

# Phục hồi tính năng "Dùng thử nhanh"
example_text = "Ngày 06/5/2026 họp Chuyển đổi số tại Phòng Hội thảo"
if st.button(f"✨ Dùng thử nhanh: {example_text}"):
    st.session_state["main_input"] = example_text

# Phục hồi danh sách Emoji đầy đủ từ các bản trước
EMOJI_LIST = {
    "Giáo dục & Y tế": "🎓 📖 📝 🏫 📚 🖊️ 🎒 👨‍🏫 👩‍🏫 🩺 🏥 💉 💊 🧬 🚑 🧪 🌡️ 🧠 🩹",
    "Dữ liệu & Du lịch": "📈 📉 📊 📋 📂 💻 🔢 🖥️ 🔍 💡 ✈️ 🚗 🏨 🏖️ 🗺️ ⛰️ 🏟️ 🗼 📸 🌍 🚢 🚲",
    "Hành chính": "📑 🏛️ ⚖️ 📨 📞 🏢 ✉️ 📜 🗃️ 🔐 📢 🖋️ 🗂️ 📅 💼 🔑 📁 🗳️ ✒️ 🗞️",
    "Fanpage": "❤️ 🔥 ✅ 🚀 📍 📞 💎 ⚡ ✨ 🌟 🚩 📌 🎁 🛒 📩 💯 🆗 📣 💥 🌈 🎀 🎊"
}

def transform_text(text, style):
    if not text or style == "Chữ thường":
        return text
    
    # Sử dụng HTML để ép hiển thị Bold/Italic/Underline đồng nhất cho tiếng Việt
    # Cách này giúp chữ Đ và các chữ có dấu không bao giờ bị nhạt hay lỗi ô vuông
    if style == "In đậm":
        return f"<b>{text}</b>"
    elif style == "In nghiêng":
        return f"<i>{text}</i>"
    elif style == "Gạch chân":
        return f"<u>{text}</u>"
    return text

# Nhập liệu
input_text = st.text_area("📌 Nhập nội dung", height=120, key="main_input")
style = st.radio("🎨 Chọn kiểu chữ", ["Chữ thường", "In đậm", "In nghiêng", "Gạch chân"], horizontal=True)

if input_text:
    output = transform_text(input_text, style)
    st.markdown("### ✅ Kết quả")
    
    # Hiển thị trực quan để xem độ đậm/nghiêng/gạch chân liền mạch
    st.markdown(f"<div style='font-size:1.2rem; padding:10px; border:1px solid #ddd; border-radius:5px;'>{output}</div>", unsafe_allow_html=True)
    
    # Cung cấp dạng text thuần (Unicode Combined) để copy đi nơi khác
    st.info("Dưới đây là mã để bạn copy vào Facebook/Word:")
    if style == "Gạch chân":
        plain_output = "".join([c + "\u0332" for c in input_text])
    else:
        # Nếu không phải gạch chân, bản này ưu tiên hiển thị chuẩn tiếng Việt 100%
        plain_output = input_text 
    st.code(plain_output, language="text")

st.write("---")
st.write("💡 **Emoji chọn lọc đầy đủ:**")
tabs = st.tabs(list(EMOJI_LIST.keys()))
for i, tab in enumerate(tabs):
    with tab:
        st.code(EMOJI_LIST[list(EMOJI_LIST.keys())[i]], language="text")
