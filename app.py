import streamlit as st
import unicodedata

# Cấu hình trang
st.set_page_config(page_title="Trình Đổi Font Tiếng Việt", layout="centered")

# Tiêu đề nhỏ hơn (dùng h2 thay vì title)
st.markdown("## 🔤 Trình Đổi Font Tiếng Việt")

def build_font_map(start_upper, start_lower):
    font_map = {}
    for i in range(26):
        font_map[chr(ord("A") + i)] = chr(start_upper + i)
        font_map[chr(ord("a") + i)] = chr(start_lower + i)
    return font_map

# Sử dụng các dải mã Unicode ổn định hơn để tránh lỗi ô vuông
FONT_STYLES = {
    "Chữ thường": {},
    "In đậm": build_font_map(0x1D5DB, 0x1D5F5), # Bold Sans-serif
    "In nghiêng": build_font_map(0x1D622, 0x1D63C), # Italic Sans-serif
    "Gạch chân": {}, 
}

def convert_text(text, style):
    font = FONT_STYLES.get(style, {})
    if not font:
        if style == "Gạch chân":
            # Kỹ thuật gạch chân bằng ký tự kết hợp
            return "".join([c + "\u0332" for c in text])
        return text
    
    # Tách dấu để giữ tiếng Việt
    text_normalized = unicodedata.normalize('NFD', text)
    result = []
    
    for c in text_normalized:
        # Chuyển đổi chính xác cả hoa và thường để tránh lỗi "pHÒNG"
        if c in font:
            result.append(font[c])
        elif c.upper() in font and c.isupper():
            result.append(font[c.upper()])
        elif c.lower() in font and c.islower():
            result.append(font[c.lower()])
        else:
            result.append(c)
            
    return unicodedata.normalize('NFC', "".join(result))

# Giao diện nhập liệu
input_text = st.text_area("📌 Nhập nội dung", height=120, placeholder="Ví dụ: Phòng họp Ban Giám hiệu")

style = st.radio("🎨 Chọn kiểu chữ", list(FONT_STYLES.keys()), horizontal=True)

if input_text.strip():
    output_text = convert_text(input_text, style)
    st.markdown("### ✅ Kết quả")
    # Hiển thị trong code block để dễ copy
    st.code(output_text, language="text")
    
    if style == "In nghiêng":
        st.caption("Lưu ý: Nếu vẫn thấy ô vuông, hãy thử kiểu 'In đậm' vì nó có độ tương thích cao nhất trên mọi điện thoại.")
