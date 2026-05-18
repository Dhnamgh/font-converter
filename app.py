import streamlit as st
import streamlit.components.v1 as components
import unicodedata

st.set_page_config(page_title="Trình Đổi Font Tiếng Việt", layout="centered")

st.markdown("## 🔤 Trình Đổi Font Tiếng Việt")

# =====================
# Demo nhanh
# =====================
example_text = "Thành phố Hồ Chí Minh, ngày 06/5/2026"

if st.button("✨ Xem thử kết quả"):
    st.session_state["main_input"] = example_text

# =====================
# Emoji
# =====================
EMOJI_GROUPS = {
    "Giáo dục & Y tế": ["🎓", "📖", "📝", "🏫", "📚", "🖊️", "🎒", "👨‍🏫", "👩‍🏫", "🩺", "🏥", "💉", "💊", "🧬", "🚑", "🧪", "🌡️", "🧠", "🩹"],
    "Dữ liệu & Du lịch": ["📈", "📉", "📊", "📋", "📂", "💻", "🔢", "🖥️", "🔍", "💡", "✈️", "🚗", "🏨", "🏖️", "🗺️", "⛰️", "🏟️", "🗼", "📸", "🌍", "🚢", "🚲"],
    "Hành chính": ["📑", "🏛️", "⚖️", "📨", "📞", "🏢", "✉️", "📜", "🗃️", "🔐", "📢", "🖋️", "🗂️", "📅", "💼", "🔑", "📁", "🗳️", "✒️", "🗞️"],
    "Fanpage": ["❤️", "🔥", "✅", "🚀", "📍", "📞", "💎", "⚡", "✨", "🌟", "🚩", "📌", "🎁", "🛒", "📩", "💯", "🆗", "📣", "💥", "🌈", "🎀", "🎊"]
}

# =====================
# HTML hiển thị (đẹp, không lỗi)
# =====================
def transform_text(text, style):
    if not text or style == "Chữ thường":
        return text

    if style == "In đậm":
        return f"<b>{text}</b>"
    elif style == "In nghiêng":
        return f"<i>{text}</i>"
    elif style == "Gạch chân":
        return f"<u>{text}</u>"

    return text


# =====================
# Map bold ASCII
# =====================
BOLD_MAP = {
    **{chr(i): chr(0x1D400 + i - 65) for i in range(65, 91)},   # A-Z
    **{chr(i): chr(0x1D41A + i - 97) for i in range(97, 123)},  # a-z
    **{chr(i): chr(0x1D7CE + i - 48) for i in range(48, 58)}    # 0-9
}

# =====================
# FIX CHÍNH: không lệch dấu
# =====================
def full_unicode_transform(text, style):
    if not text or style == "Chữ thường":
        return text

    # ✅ Normalize Unicode (cực quan trọng)
    text = unicodedata.normalize("NFC", text)

    result = ""

    for ch in text:
        # ✅ Chỉ bold ASCII → không làm lệch dấu
        if ch in BOLD_MAP and style == "In đậm":
            result += BOLD_MAP[ch]
        else:
            result += ch

    return result


# =====================
# Input
# =====================
input_text = st.text_area("📌 Nhập nội dung", height=120, key="main_input")

style = st.radio(
    "🎨 Chọn kiểu chữ",
    ["Chữ thường", "In đậm", "In nghiêng", "Gạch chân"],
    horizontal=True
)

# =====================
# Output
# =====================
if input_text:
    output_html = transform_text(input_text, style)

    # Unicode để copy Facebook/Zalo
    output_text = full_unicode_transform(input_text, style)

    st.write("### ✅ Xem trước:")
    st.markdown(output_html, unsafe_allow_html=True)

    st.write("### 📋 Copy dùng Facebook/Zalo:")
    st.code(output_text)

# =====================
# Emoji
# =====================
st.write("---")
st.write("💡 **Emoji chọn nhanh:**")

tabs = st.tabs(list(EMOJI_GROUPS.keys()))

for i, tab in enumerate(tabs):
    group_name = list(EMOJI_GROUPS.keys())[i]
    with tab:
        cols = st.columns(10)
        for idx, emoji in enumerate(EMOJI_GROUPS[group_name]):
            with cols[idx % 10]:
                components.html(f"""
                <div style="font-size:26px;text-align:center;cursor:pointer">
                    {emoji}
                </div>
                """, height=40)

# =====================
# Footer
# =====================
st.write("---")
st.markdown("Copyright © 2026 Bản quyền thuộc về bạn.")
