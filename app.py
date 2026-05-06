import streamlit as st
import unicodedata

st.set_page_config(page_title="Đổi Font Chữ Tiếng Việt", layout="centered")

st.title("🔤 Trình Đổi Font Facebook Tiếng Việt")

def build_font_map(start_upper, start_lower=None):
    font_map = {}
    for i in range(26):
        font_map[chr(ord("A") + i)] = chr(start_upper + i)
        if start_lower is not None:
            font_map[chr(ord("a") + i)] = chr(start_lower + i)
    return font_map

# Sử dụng các dải mã có độ tương thích cao hơn
FONT_STYLES = {
    "Chữ thường": {},
    "In đậm (Sans)": build_font_map(0x1D5EE, 0x1D608), # Kiểu Sans-serif đậm thường bền hơn
    "In đậm (Serif)": build_font_map(0x1D400, 0x1D41A),
    "In nghiêng": build_font_map(0x1D434, 0x1D44E),
    "Gạch chân": {}, # Placeholder
}

def convert_text_pro(text, style):
    font = FONT_STYLES.get(style, {})
    if not font:
        return text
    
    # Giữ nguyên dấu bằng cách tách NFD
    text_normalized = unicodedata.normalize('NFD', text)
    result = []
    
    for c in text_normalized:
        # Kiểm tra xem có phải chữ cái Latin không
        upper_c = c.upper()
        if upper_c in font or c in font:
            if c.isupper():
                result.append(font.get(c, c))
            else:
                # Nếu không có font chữ thường, lấy font chữ hoa (cho các bản in hoa)
                result.append(font.get(c, c))
        else:
            # Giữ nguyên dấu phụ và các ký tự đặc biệt
            result.append(c)
            
    return unicodedata.normalize('NFC', "".join(result))

input_text = st.text_area("📌 Nhập nội dung có dấu", height=120, placeholder="Ví dụ: Phòng họp Ban Giám hiệu")
style = st.radio("🎨 Chọn kiểu chữ", list(FONT_STYLES.keys()), horizontal=True)

if input_text.strip():
    output_text = convert_text_pro(input_text, style)
    st.markdown("### ✅ Kết quả (Đã giữ dấu)")
    st.code(output_text, language="text")
    
    # Cảnh báo về lỗi hiển thị trên thiết bị
    if "In nghiêng" in style:
        st.warning("⚠️ Nếu bạn thấy ô vuông, đó là do điện thoại/máy tính của bạn không hỗ trợ font nghiêng toán học. Hãy thử kiểu 'In đậm (Sans)' thường có độ tương thích cao nhất.")
