import streamlit as st

st.set_page_config(page_title="Đổi Font Chữ Facebook", layout="centered")

st.title("🔤 Đổi Font Chữ Đăng Facebook")
st.write("Dán nội dung và chọn kiểu chữ. Copy kết quả để đăng Facebook.")

def build_font_map(start_upper, start_lower):
    font_map = {}
    for i in range(26):
        font_map[chr(ord("A") + i)] = chr(start_upper + i)
        if start_lower:
            font_map[chr(ord("a") + i)] = chr(start_lower + i)
    return font_map

FONT_STYLES = {
    "Chữ thường": {},
    "In đậm": build_font_map(0x1D400, 0x1D41A),
    "In nghiêng": build_font_map(0x1D434, 0x1D44E),
    "IN HOA ĐẬM": build_font_map(0x1D400, None),
    "IN HOA NGHIÊNG": build_font_map(0x1D434, None),
}

def convert_text(text, style):
    font = FONT_STYLES[style]
    result = ""
    for c in text:
        if "IN HOA" in style:
            c = c.upper()
        result += font.get(c, c)
    return result

input_text = st.text_area(
    "📌 Nhập nội dung",
    height=150,
    placeholder="Ví dụ: Xin chào Facebook"
)

style = st.radio(
    "🎨 Chọn kiểu chữ",
    list(FONT_STYLES.keys()),
    horizontal=True
)

if input_text.strip():
    output = convert_text(input_text, style)
    st.markdown("### ✅ Kết quả (copy để đăng)")
    st.code(output, language="text")
else:
    st.info("Nhập nội dung để xem kết quả")
``
