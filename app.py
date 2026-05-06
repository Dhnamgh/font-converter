import streamlit as st
import unicodedata

st.set_page_config(page_title="Trình Đổi Font Tiếng Việt", layout="centered")

st.markdown("## 🔤 Trình Đổi Font Tiếng Việt")

def build_full_map(upper_start, lower_start, digit_start):
    mapping = {}
    # Ánh xạ chữ cái A-Z và a-z
    for i in range(26):
        mapping[chr(ord("A") + i)] = chr(upper_start + i)
        mapping[chr(ord("a") + i)] = chr(lower_start + i)
    # Ánh xạ chữ số 0-9 để không bị lệch màu
    for i in range(10):
        mapping[chr(ord("0") + i)] = chr(digit_start + i)
    return mapping

# Sử dụng dải mã toán học Serif Bold và Italic đầy đủ nhất
FONT_STYLES = {
    "Chữ thường": {},
    "In đậm": build_full_map(0x1D400, 0x1D41A, 0x1D7CE),
    "In nghiêng": build_full_map(0x1D434, 0x1D44E, 0x1D7CE), # Dùng chung dải số đậm để dễ nhìn
    "Gạch chân": {}, 
}

def convert_text(text, style):
    if not text: return ""
    font = FONT_STYLES.get(style, {})
    text_normalized = unicodedata.normalize('NFD', text)
    result = []
    
    for c in text_normalized:
        # Chuyển đổi font nếu có trong map, nếu không giữ nguyên (dấu tiếng Việt)[cite: 1]
        char = font.get(c, c)
        if style == "Gạch chân" and c.strip():
            # Kỹ thuật gạch chân liền mạch[cite: 1]
            char = c + "\u0332"
        result.append(char)
            
    return unicodedata.normalize('NFC', "".join(result))

# Xử lý dùng thử nhanh
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
    st.write("💡 **Kho Emoji khổng lồ (Gấp đôi số lượng):**")
    
    t1, t2, t3, t4 = st.tabs(["Giáo dục & Y tế", "Dữ liệu & Du lịch", "Hành chính", "Fanpage"])
    with t1:
        st.code("🎓 📖 📝 🏫 📚 🖊️ 🎒 🧐 👨‍🏫 👩‍🏫 🩺 🏥 💉 💊 🧬 🚑 🧪 🌡️ 🧠 🩹", language="text")
    with t2:
        st.code("📈 📉 📊 📋 📂 💻 🔢 🖥️ 🔍 💡 ✈️ 🚗 🏨 🏖️ 🗺️ ⛰️ 🏟️ 🗼 📸 🌍", language="text")
    with t3:
        st.code("📑 🏛️ ⚖️ 📨 📞 🏢 📆 ✉️ ✒️ 🗳️ 📜 🗃️ 🔏 🔐 📢 🗞️ 🖋️ 🗂️ 📅 💼", language="text")
    with t4:
        st.code("❤️ 🔥 ✅ 🚀 📍 📞 💎 ⚡ ✨ 🌟 🚩 📌 🎁 🛒 📩 💯 🆗 📣 💥 🌈", language="text")
else:
    st.info("Nhập nội dung hoặc nhấn 'Dùng thử nhanh' để xem kết quả.")
