import streamlit as st
import unicodedata

st.set_page_config(
    page_title="Đổi Font Chữ cho website, Fanpage,... ",
    layout="centered"
)

st.title("🔤 Đổi Font Chữ Facebook (Hỗ trợ Tiếng Việt)")
st.write("Dán nội dung có dấu vào đây")

def build_font_map(start_upper, start_lower=None):
    font_map = {}
    for i in range(26):
        font_map[chr(ord("A") + i)] = chr(start_upper + i)
        if start_lower is not None:
            font_map[chr(ord("a") + i)] = chr(start_lower + i)
    return font_map

FONT_STYLES = {
    "Chữ thường": {},
    "In đậm": build_font_map(0x1D400, 0x1D41A),
    "In nghiêng": build_font_map(0x1D434, 0x1D44E),
    "IN HOA ĐẬM": build_font_map(0x1D400),
    "IN HOA NGHIÊNG": build_font_map(0x1D434),
}

def convert_text(text, style):
    font = FONT_STYLES[style]
    if not font:
        return text
      
    text_normalized = unicodedata.normalize('NFD', text)
    
    result = []
    for c in text_normalized:
        char_to_convert = c
        if "IN HOA" in style:
            char_to_convert = c.upper()
        
        # Chỉ chuyển đổi nếu là ký tự Latin (A-Z, a-z)
        # Các dấu phụ (combining marks) sẽ được giữ nguyên để dán đè lên chữ đã chuyển
        if char_to_convert in font:
            result.append(font[char_to_convert])
        else:
            result.append(c)
            
    # Gộp lại thành dạng chuẩn để hiển thị mượt mà trên trình duyệt
    return unicodedata.normalize('NFC', "".join(result))

input_text = st.text_area(
    "📌 Nhập nội dung (có dấu hay không đều được)",
    height=150,
    placeholder="Ví dụ: Xin chào, đây là tiếng Việt đậm nét!"
)

style = st.radio(
    "🎨 Chọn kiểu chữ",
    list(FONT_STYLES.keys()),
    horizontal=True
)

if input_text.strip():
    output_text = convert_text(input_text, style)
    st.markdown("### ✅ Kết quả (Đã tối ưu hiển thị)")
    st.code(output_text, language="text")
    st.caption("Mẹo: Một số trình duyệt có thể hiển thị dấu hơi lệch một chút, nhưng màu sắc sẽ đều hoàn toàn.")
else:
    st.info("Nhập nội dung để xem kết quả.")
