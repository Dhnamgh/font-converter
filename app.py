import streamlit as st
import unicodedata

# Cấu hình giao diện
st.set_page_config(page_title="Trình Đổi Font Tiếng Việt", layout="centered")

# Tiêu đề thu nhỏ
st.markdown("## 🔤 Trình Đổi Font Tiếng Việt")

def build_font_map(start_upper, start_lower):
    font_map = {}
    for i in range(26):
        font_map[chr(ord("A") + i)] = chr(start_upper + i)
        font_map[chr(ord("a") + i)] = chr(start_lower + i)
    return font_map

# Sử dụng các dải mã có độ tương thích cao nhất cho Facebook
FONT_STYLES = {
    "Chữ thường": {},
    "In đậm": build_font_map(0x1D400, 0x1D41A),
    "In nghiêng": build_font_map(0x1D622, 0x1D63C), # Chuyển sang Sans-serif Italic để giảm lỗi ô vuông
    "Gạch chân": {}, 
}

def convert_text(text, style):
    font = FONT_STYLES.get(style, {})
    
    # Tách dấu tiếng Việt (NFD) để xử lý phần thân chữ cái
    text_normalized = unicodedata.normalize('NFD', text)
    result = []
    
    for c in text_normalized:
        if c in font:
            # Thay thế chữ cái bằng font tương ứng[cite: 1]
            char = font[c]
            if style == "Gạch chân":
                char += "\u0332"
            result.append(char)
        elif style == "Gạch chân" and c.strip():
            # Thêm gạch chân cho cả ký tự có dấu[cite: 1]
            result.append(c + "\u0332")
        else:
            result.append(c)
            
    # Hợp nhất lại (NFC) để hiển thị chuẩn xác[cite: 1]
    return unicodedata.normalize('NFC', "".join(result))

# Nhập liệu
input_text = st.text_area("📌 Nhập nội dung", height=100, placeholder="Ví dụ: Thành phố Hồ Chí Minh")

style = st.radio("🎨 Chọn kiểu chữ", list(FONT_STYLES.keys()), horizontal=True)

if input_text.strip():
    output_text = convert_text(input_text, style)
    st.markdown("### ✅ Kết quả")
    st.code(output_text, language="text")
    
    # Khu vực Emoji thường dùng cho Fanpage[cite: 1]
    st.write("✨ **Emoji thường dùng (Click để copy):**")
    emojis = "❤️ 🔥 ✅ 🚀 📍 📞 💎 ⚡ ✨ 🌟 🚩 📌 🎁 🛒 📩 💯 🆗 📣"
    st.code(emojis, language="text")
else:
    st.info("Nhập nội dung để xem kết quả.")
