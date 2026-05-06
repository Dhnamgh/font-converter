import streamlit as st
import unicodedata

# Cấu hình giao diện gọn gàng
st.set_page_config(page_title="Trình Đổi Font Tiếng Việt", layout="centered")

# Tiêu đề nhỏ gọn
st.markdown("## 🔤 Trình Đổi Font Tiếng Việt")

def build_font_map(start_upper, start_lower):
    font_map = {}
    for i in range(26):
        # Khớp chính xác mã cho từng ký tự A-Z và a-z
        font_map[chr(ord("A") + i)] = chr(start_upper + i)
        font_map[chr(ord("a") + i)] = chr(start_lower + i)
    return font_map

# Các bộ font ổn định nhất cho Facebook và di động
FONT_STYLES = {
    "Chữ thường": {},
    "In đậm": build_font_map(0x1D400, 0x1D41A),
    "In nghiêng": build_font_map(0x1D434, 0x1D44E),
    "Gạch chân": {}, 
}

def convert_text(text, style):
    font = FONT_STYLES.get(style, {})
    # Tách dấu NFD để xử lý phần thân chữ cái
    text_normalized = unicodedata.normalize('NFD', text)
    result = []
    
    for c in text_normalized:
        char = font.get(c, c) # Lấy font mới, nếu không có (như dấu) thì giữ nguyên
        if style == "Gạch chân" and c.strip():
            # Thêm ký tự kết hợp gạch chân[cite: 1]
            char = c + "\u0332"
        result.append(char)
            
    return unicodedata.normalize('NFC', "".join(result))

# CHỨC NĂNG DÙNG THỬ NHANH
example_text = "Thành phố Hồ Chí Minh"
if "input_val" not in st.session_state:
    st.session_state.input_val = ""

# Nhấn vào nút này để điền nhanh dữ liệu mẫu
if st.button(f"✨ Dùng thử nhanh: {example_text}"):
    st.session_state.input_val = example_text

input_text = st.text_area(
    "📌 Nhập nội dung", 
    value=st.session_state.input_val, 
    height=100, 
    key="main_input"
)

style = st.radio("🎨 Chọn kiểu chữ", list(FONT_STYLES.keys()), horizontal=True)

if input_text.strip():
    output_text = convert_text(input_text, style)
    st.markdown("### ✅ Kết quả")
    st.code(output_text, language="text")
    
    # DANH SÁCH EMOJI THEO CHỦ ĐỀ[cite: 1]
    st.write("---")
    st.write("💡 **Emoji theo chủ đề (Click để copy):**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.caption("🏫 Giáo dục & Y tế")
        st.code("🎓 📖 📝 🏫 🧪 🩺 🏥 💉 💊 🧬", language="text")
        st.caption("📊 Phân tích & Dữ liệu")
        st.code("📈 📉 📊 📋 📂 💻 🔢 🖥️ 🔍 💡", language="text")
        
    with col2:
        st.caption("✈️ Du lịch & Địa điểm")
        st.code("✈️ 🚗 🏨 🏖️ 🗺️ ⛰️ 🏟️ 🗼 📸 🌍", language="text")
        st.caption("🔥 Phổ biến Fanpage")
        st.code("❤️ 🔥 ✅ 🚀 📍 📞 💎 ⚡ ✨ 📌", language="text")
else:
    st.info("Nhập nội dung hoặc nhấn 'Dùng thử nhanh' để xem kết quả.")
