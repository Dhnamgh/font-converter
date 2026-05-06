import streamlit as st
import unicodedata

st.set_page_config(page_title="Đổi Font Chữ Pro", layout="centered")

st.title("🔤 Trình Đổi Font Chữ Tiếng Việt")

def build_font_map(start_upper, start_lower=None):
    font_map = {}
    for i in range(26):
        font_map[chr(ord("A") + i)] = chr(start_upper + i)
        if start_lower is not None:
            font_map[chr(ord("a") + i)] = chr(start_lower + i)
    return font_map

# Sử dụng bộ mã Serif cho in nghiêng để tăng khả năng tương thích
FONT_STYLES = {
    "Chữ thường": {},
    "In đậm": build_font_map(0x1D400, 0x1D41A),
    "In nghiêng": build_font_map(0x1D434, 0x1D44E), 
    "IN HOA ĐẬM": build_font_map(0x1D400),
    "IN HOA NGHIÊNG": build_font_map(0x1D434),
}

def remove_diacritics(text):
    """Loại bỏ hoàn toàn dấu tiếng Việt"""
    normalized = unicodedata.normalize('NFD', text)
    return "".join([c for c in normalized if not unicodedata.combining(c)])

def convert_text(text, style):
    font = FONT_STYLES[style]
    if not font:
        return text
    
    # CHIẾN THUẬT: Nếu là IN HOA, ta bỏ dấu để tránh dính chữ (giống các Fanpage lớn)
    if "IN HOA" in style:
        text = remove_diacritics(text).upper()
        result = "".join([font.get(c, c) for c in text])
        return result

    # Với in đậm/nghiêng thường: Dùng kỹ thuật tách dấu (NFD)
    text_normalized = unicodedata.normalize('NFD', text)
    result = []
    for c in text_normalized:
        if c.upper() in font or c.lower() in font:
            # Chỉ chuyển đổi phần thân chữ cái
            target = c.upper() if c.isupper() else c
            result.append(font.get(target, c))
        else:
            result.append(c)
            
    return unicodedata.normalize('NFC', "".join(result))

input_text = st.text_area("📌 Nhập nội dung", height=120)
style = st.radio("🎨 Chọn kiểu chữ", list(FONT_STYLES.keys()), horizontal=True)

if input_text.strip():
    output_text = convert_text(input_text, style)
    st.markdown("### ✅ Kết quả")
    st.code(output_text, language="text")
    
    if "IN HOA" in style:
        st.info("💡 Mẹo: Với kiểu IN HOA, hệ thống tự động bỏ dấu để hiển thị đẹp nhất trên mọi thiết bị.")
