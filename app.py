import streamlit as st
import unicodedata

st.set_page_config(page_title="Trình Đổi Font Tiếng Việt", layout="centered")

st.markdown("## 🔤 Trình Đổi Font Tiếng Việt")

def build_map(upper, lower, digit):
    mapping = {}
    for i in range(26):
        mapping[chr(ord("A") + i)] = chr(upper + i)
        mapping[chr(ord("a") + i)] = chr(lower + i)
    for i in range(10):
        mapping[chr(ord("0") + i)] = chr(digit + i)
    return mapping

# Tách riêng biệt dải mã để đảm bảo độ đậm nhạt đồng nhất giữa chữ và số
FONT_STYLES = {
    "Chữ thường": {},
    "In đậm": build_map(0x1D400, 0x1D41A, 0x1D7CE),
    "In nghiêng": build_map(0x1D608, 0x1D622, 0x1D614), # Dải mã Sans-serif Italic đồng bộ cả chữ và số
    "Gạch chân": {}, 
}

def convert_text(text, style):
    if not text: return ""
    font = FONT_STYLES.get(style, {})
    # Chuẩn hóa NFD để xử lý ký tự gốc và dấu riêng biệt
    text_normalized = unicodedata.normalize('NFD', text)
    result = []
    
    for c in text_normalized:
        char = font.get(c, c)
        if style == "Gạch chân" and c.strip():
            # Sử dụng ký tự kết hợp gạch chân tiêu chuẩn[cite: 1]
            char = c + "\u0332"
        result.append(char)
            
    return unicodedata.normalize('NFC', "".join(result))

# Chức năng dùng thử nhanh
example_text = "Thành phố Hồ Chí Minh"
if st.button(f"✨ Dùng thử nhanh: {example_text}"):
    st.session_state["main_input"] = example_text

input_text = st.text_area("📌 Nhập nội dung", height=120, key="main_input")
style = st.radio("🎨 Chọn kiểu chữ", list(FONT_STYLES.keys()), horizontal=True)

if input_text.strip():
    output_text = convert_text(input_text, style)
    st.markdown("### ✅ Kết quả")
    st.code(output_text, language="text")
    
    st.write("---")
    st.write("💡 **Emoji chọn lọc:**")
    
    t1, t2, t3, t4 = st.tabs(["Giáo dục & Y tế", "Dữ liệu & Du lịch", "Hành chính", "Fanpage"])
    with t1:
        st.code("🎓 📖 📝 🏫 📚 🖊️ 🎒 👨‍🏫 👩‍🏫 🩺 🏥 💉 💊 🧬 🚑 🧪 🌡️ 🧠 🩹", language="text")
    with t2:
        st.code("📈 📉 📊 📋 📂 💻 🔢 🖥️ 🔍 💡 ✈️ 🚗 🏨 🏖️ 🗺️ ⛰️ 🏟️ 🗼 📸 🌍", language="text")
    with t3:
        st.code("📑 🏛️ ⚖️ 📨 📞 🏢 ✉️ 📜 🗃️ 🔐 📢 🖋️ 🗂️ 📅 💼 🔑 📁 🗳️", language="text")
    with t4:
        st.code("❤️ 🔥 ✅ 🚀 📍 📞 💎 ⚡ ✨ 🌟 🚩 📌 🎁 🛒 📩 💯 🆗 📣 💥 🌈", language="text")
