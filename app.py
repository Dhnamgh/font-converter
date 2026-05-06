import streamlit as st
import unicodedata

# Cấu hình giao diện nhỏ gọn
st.set_page_config(page_title="Trình Đổi Font Tiếng Việt", layout="centered")

# Tiêu đề kích thước vừa phải
st.markdown("## 🔤 Trình Đổi Font Tiếng Việt")

def build_font_map(start_upper, start_lower):
    font_map = {}
    for i in range(26):
        font_map[chr(ord("A") + i)] = chr(start_upper + i)
        font_map[chr(ord("a") + i)] = chr(start_lower + i)
    return font_map

# Các bộ font ổn định nhất
FONT_STYLES = {
    "Chữ thường": {},
    "In đậm": build_font_map(0x1D400, 0x1D41A),
    "In nghiêng": build_font_map(0x1D434, 0x1D44E),
    "Gạch chân": {}, 
}

def convert_text(text, style):
    if not text:
        return ""
    font = FONT_STYLES.get(style, {})
    
    # Tách dấu NFD để giữ nguyên tiếng Việt
    text_normalized = unicodedata.normalize('NFD', text)
    result = []
    
    for c in text_normalized:
        # Xử lý In nghiêng/In đậm bằng cách lấy từ font map
        char = font.get(c, c) 
        
        # Xử lý Gạch chân: thêm ký tự tổ hợp \u0332 vào sau mỗi ký tự
        if style == "Gạch chân" and c.strip():
            char = c + "\u0332"
            
        result.append(char)
            
    return unicodedata.normalize('NFC', "".join(result))

# XỬ LÝ DÙNG THỬ NHANH (SỬA LỖI KHÔNG TÁC DỤNG)
example_text = "Thành phố Hồ Chí Minh"

# Nếu nhấn nút, cập nhật trực tiếp vào session_state
if st.button(f"✨ Dùng thử nhanh: {example_text}"):
    st.session_state["main_input"] = example_text

# Sử dụng tham số 'key' để Streamlit tự động liên kết với session_state[cite: 1]
input_text = st.text_area(
    "📌 Nhập nội dung", 
    height=120, 
    placeholder="Nhập nội dung tại đây...",
    key="main_input" 
)

style = st.radio("🎨 Chọn kiểu chữ", list(FONT_STYLES.keys()), horizontal=True)

if input_text.strip():
    output_text = convert_text(input_text, style)
    st.markdown("### ✅ Kết quả")
    st.code(output_text, language="text")
    
    # BỘ EMOJI PHONG PHÚ THEO CHỦ ĐỀ[cite: 1]
    st.write("---")
    st.write("💡 **Emoji theo chủ đề (Click để copy):**")
    
    tabs = st.tabs(["Giáo dục/Y tế", "Dữ liệu/Du lịch", "Fanpage"])
    
    with tabs[0]:
        st.code("🎓 📖 📝 🏫 🧪 🩺 🏥 💉 💊 🧬", language="text")
    with tabs[1]:
        st.code("📈 📊 📋 💻 🔍 ✈️ 🚗 🏨 🏖️ 🗺️", language="text")
    with tabs[2]:
        st.code("❤️ 🔥 ✅ 🚀 📍 📞 💎 ⚡ ✨ 📌 💯 📣", language="text")
else:
    st.info("Nhập nội dung hoặc nhấn 'Dùng thử nhanh' để xem kết quả.")
