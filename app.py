import streamlit as st

st.set_page_config(page_title="Trình Đổi Font Tiếng Việt Chuẩn", layout="centered")

st.markdown("## 🔤 Trình Đổi Font Tiếng Việt (Tối Ưu)")

# Hàm tạo bản đồ ký tự chuẩn, tránh dải mã gây lỗi số
def get_font_map(style):
    upper_base = {"In đậm": 0x1D400, "In nghiêng": 0x1D434}
    lower_base = {"In đậm": 0x1D41A, "In nghiêng": 0x1D44E}
    digit_base = {"In đậm": 0x1D7CE, "In nghiêng": 0x1D7CE} # Giữ số đứng cho dễ đọc
    
    mapping = {}
    if style in upper_base:
        for i in range(26):
            mapping[chr(ord("A") + i)] = chr(upper_base[style] + i)
            mapping[chr(ord("a") + i)] = chr(lower_base[style] + i)
        for i in range(10):
            mapping[chr(ord("0") + i)] = chr(digit_base[style] + i)
    return mapping

def convert_text(text, style):
    if style == "Chữ thường" or not text:
        return text
    
    # Xử lý riêng cho Gạch chân để liền mạch nhất có thể
    if style == "Gạch chân":
        return "".join([c + "\u0332" if c != " " else " \u0332" for c in text])

    font_map = get_font_map(style)
    result = ""
    for char in text:
        # Chỉ chuyển đổi ký tự Latin không dấu để tránh lệch màu "nhạt - đậm"
        if char in font_map:
            result += font_map[char]
        else:
            # Giữ nguyên ký tự tiếng Việt có dấu để bảo toàn độ hiển thị chuẩn
            result += char
    return result

# Giao diện
input_text = st.text_area("📌 Nhập nội dung", placeholder="Ví dụ: Công văn số 33 ngày 09/03/2026...", height=120)
style = st.radio("🎨 Chọn kiểu chữ", ["Chữ thường", "In đậm", "In nghiêng", "Gạch chân"], horizontal=True)

if input_text:
    output = convert_text(input_text, style)
    st.markdown("### ✅ Kết quả")
    # Sử dụng st.code để người dùng dễ dàng copy không lỗi định dạng[cite: 1]
    st.code(output, language="text")

st.write("---")
st.write("💡 **Bộ Emoji chuyên dụng:**")
t1, t2 = st.tabs(["Hành chính & Y tế", "Fanpage & Nổi bật"])
with t1:
    st.code("📑 🏛️ ⚖️ 🏥 🩺 💊 📋 📂 ✉️ 📜 📅 💼 🔑 📁", language="text")
with t2:
    st.code("❤️ 🔥 ✅ 🚀 📍 📞 💎 ⚡ ✨ 🌟 🚩 📌 🎁 📩 💯", language="text")
