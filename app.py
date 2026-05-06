import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Trình Đổi Font Tiếng Việt", layout="centered")

st.markdown("## 🔤 Trình Đổi Font Tiếng Việt")

# Dùng thử nhanh
example_text = "Ngày 06/5/2026 họp Chuyển đổi số tại Phòng Hội thảo"
if st.button(f"✨ Dùng thử nhanh: {example_text}"):
    st.session_state["main_input"] = example_text

# Danh sách Emoji
EMOJI_LIST = {
    "Giáo dục & Y tế": "🎓 📖 📝 🏫 📚 🖊️ 🎒 👨‍🏫 👩‍🏫 🩺 🏥 💉 💊 🧬 🚑 🧪 🌡️ 🧠 🩹",
    "Dữ liệu & Du lịch": "📈 📉 📊 📋 📂 💻 🔢 🖥️ 🔍 💡 ✈️ 🚗 🏨 🏖️ 🗺️ ⛰️ 🏟️ 🗼 📸 🌍 🚢 🚲",
    "Hành chính": "📑 🏛️ ⚖️ 📨 📞 🏢 ✉️ 📜 🗃️ 🔐 📢 🖋️ 🗂️ 📅 💼 🔑 📁 🗳️ ✒️ 🗞️",
    "Fanpage": "❤️ 🔥 ✅ 🚀 📍 📞 💎 ⚡ ✨ 🌟 🚩 📌 🎁 🛒 📩 💯 🆗 📣 💥 🌈 🎀 🎊"
}

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

input_text = st.text_area("📌 Nhập nội dung", height=120, key="main_input")
style = st.radio("🎨 Chọn kiểu chữ", ["Chữ thường", "In đậm", "In nghiêng", "Gạch chân"], horizontal=True)

if input_text:
    output = transform_text(input_text, style)
    st.markdown("### ✅ Kết quả")
    
    # SỬA CỠ CHỮ: Dùng !important để đảm bảo cỡ chữ không bị to hơn khung nhập liệu[cite: 1]
    st.markdown(f"""
        <div id="target-copy" style="font-size: 14px !important; font-family: sans-serif !important; padding: 10px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9; color: #31333F;">
            {output}
        </div>
    """, unsafe_allow_html=True)
    
    # SỬA NÚT COPY: JavaScript tự động bôi đen và copy định dạng (không hiện thông báo OK)[cite: 1]
    st.write("")
    copy_js = f"""
    <button onclick="copyFunction()" style="cursor:pointer; background-color:#4CAF50; color:white; border:none; padding:10px 20px; border-radius:5px; font-size:14px;">
        📋 Nhấn để Copy nội dung (Giữ định dạng)
    </button>

    <script>
    function copyFunction() {{
        var doc = parent.document;
        var element = doc.getElementById('target-copy');
        var range = doc.createRange();
        range.selectNode(element);
        window.getSelection().removeAllRanges();
        window.getSelection().addRange(range);
        doc.execCommand('copy');
        window.getSelection().removeAllRanges();
    }}
    </script>
    """
    components.html(copy_js, height=50)

st.write("---")
st.write("💡 **Emoji chọn lọc:**")
tabs = st.tabs(list(EMOJI_LIST.keys()))
for i, tab in enumerate(tabs):
    with tab:
        st.code(EMOJI_LIST[list(EMOJI_LIST.keys())[i]], language="text")
