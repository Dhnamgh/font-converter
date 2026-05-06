import streamlit as st
import unicodedata

# Cấu hình giao diện gọn gàng
st.set_page_config(page_title="Trình Đổi Font Tiếng Việt", layout="centered")

# Tiêu đề nhỏ gọn
st.markdown("## 🔤 Trình Đổi Font Tiếng Việt")

def build_font_map(start_upper, start_lower):
    font_map = {}
    for i in range(26):
        # Khớp chính xác từng chữ cái A-Z và a-z
        font_map[chr(ord("A") + i)] = chr(start_upper + i)
        font_map[chr(ord("a") + i)] = chr(start_lower + i)
    return font_map

# Sử dụng dải mã Serif ổn định nhất cho Facebook
FONT_STYLES = {
    "Chữ thường": {},
    "In đậm": build_font_map(0x1D400, 0x1D41A), 
    "In nghiêng": build_font_map(0x1D434, 0x1D44E),
    "Gạch chân": {}, 
}

def convert_text(text, style):
    font = FONT_STYLES.get(style, {})
    if not font and style != "Gạch chân":
        return text
    
    # Tách dấu để giữ nguyên tiếng Việt
    text_normalized = unicodedata.normalize('NFD', text)
    result = []
    
    for c in text_normalized:
        if c in font:
            result.append(font[c])
        elif style == "Gạch chân" and c.strip():
            # Kỹ thuật gạch chân chuẩn Unicode
            result.append(c + "\u0332")
        else:
            result.append(c)
            
    return unicodedata.normalize('NFC', "".join(result))

# Giao diện nhập liệu
input_text = st.text_area("📌 Nhập nội dung", height=120, placeholder="Ví dụ: Thành phố Hồ Chí Minh")

style = st.radio("🎨 Chọn kiểu chữ", list(FONT_STYLES.keys()), horizontal=True)

if input_text.strip():
    output_text = convert_text(input_text, style)
    st.markdown("### ✅ Kết quả")
    st.code(output_text, language="text")
    
    if style == "In nghiêng":
        st.caption("Lưu ý: Nếu vẫn thấy ô vuông ở kiểu nghiêng, hãy dùng kiểu 'In đậm' vì nó có độ tương thích cao nhất[cite: 1].")
