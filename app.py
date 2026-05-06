import streamlit as st

st.set_page_config(page_title="Trình Đổi Font Tiếng Việt", layout="centered")

st.markdown("## 🔤 Trình Đổi Font Tiếng Việt")

# Chức năng dùng thử nhanh
example_text = "Ngày 06/5/2026 họp Chuyển đổi số tại Phòng Hội thảo"
if st.button(f"✨ Dùng thử nhanh: {example_text}"):
    st.session_state["main_input"] = example_text

# Từ điển ánh xạ Unicode để copy không bị mất định dạng[cite: 1]
def get_unicode_map(style):
    maps = {
        "In đậm": (0x1D400, 0x1D41A, 0x1D7CE),
        "In nghiêng": (0x1D434, 0x1D44E, 0x1D7CE)
    }
    if style not in maps: return {}
    u_base, l_base, d_base = maps[style]
    mapping = {chr(ord("A") + i): chr(u_base + i) for i in range(26)}
    mapping.update({chr(ord("a") + i): chr(l_base + i) for i in range(26)})
    mapping.update({chr(ord("0") + i): chr(d_base + i) for i in range(10)})
    return mapping

def convert_to_copyable(text, style):
    if style == "Chữ thường": return text
    if style == "Gạch chân": return "".join([c + "\u0332" for c in text])
    
    mapping = get_unicode_map(style)
    # Giữ nguyên chữ có dấu để tránh lỗi font nhạt màu[cite: 1]
    return "".join([mapping.get(c, c) for c in text])

input_text = st.text_area("📌 Nhập nội dung", height=120, key="main_input")
style = st.radio("🎨 Chọn kiểu chữ", ["Chữ thường", "In đậm", "In nghiêng", "Gạch chân"], horizontal=True)

if input_text:
    copyable_text = convert_to_copyable(input_text, style)
    st.markdown("### ✅ Kết quả")
    
    # CSS ép cỡ chữ kết quả bằng với cỡ chữ nhập liệu[cite: 1]
    st.markdown(f"""
        <div style="font-size: 16px; font-family: sans-serif; padding: 10px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
            {copyable_text}
        </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.info("Nhấn vào khung dưới để copy sang Word/Fanpage:")
    st.code(copyable_text, language="text")

st.write("---")
st.write("💡 **Emoji chọn lọc:**")
EMOJI_LIST = {
    "Giáo dục & Y tế": "🎓 📖 📝 🏫 📚 🖊️ 🎒 👨‍🏫 👩‍🏫 🩺 🏥 💉 💊 🧬 🚑 🧪 🌡️ 🧠 🩹",
    "Dữ liệu & Du lịch": "📈 📉 📊 📋 📂 💻 🔢 🖥️ 🔍 💡 ✈️ 🚗 🏨 🏖️ 🗺️ ⛰️ 🏟️ 🗼 📸 🌍 🚢 🚲",
    "Hành chính": "📑 🏛️ ⚖️ 📨 📞 🏢 ✉️ 📜 🗃️ 🔐 📢 🖋️ 🗂️ 📅 💼 🔑 📁 🗳️ ✒️ 🗞️",
    "Fanpage": "❤️ 🔥 ✅ 🚀 📍 📞 💎 ⚡ ✨ 🌟 🚩 📌 🎁 🛒 📩 💯 🆗 📣 💥 🌈 🎀 🎊"
}
tabs = st.tabs(list(EMOJI_LIST.keys()))
for i, tab in enumerate(tabs):
    with tab:
        st.code(EMOJI_LIST[list(EMOJI_LIST.keys())[i]], language="text")
