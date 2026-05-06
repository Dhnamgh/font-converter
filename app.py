import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Trình Đổi Font Tiếng Việt - Bản Chuẩn", layout="centered")

st.markdown("## 🔤 Trình Đổi Font Tiếng Việt")

# Phục hồi tính năng "Dùng thử nhanh"
example_text = "Ngày 06/5/2026 họp Chuyển đổi số tại Phòng Hội thảo"
if st.button(f"✨ Dùng thử nhanh: {example_text}"):
    st.session_state["main_input"] = example_text

# Danh sách Emoji đầy đủ
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
    
    # 1. SỬA CỠ CHỮ: Ép cỡ chữ 16px (bằng với khung nhập liệu)[cite: 2]
    # Thêm ID 'copy-area' để JavaScript có thể tìm thấy và sao chép
    result_html = f"""
        <div id="copy-area" style="font-size:16px; font-family:sans-serif; padding:10px; border:1px solid #ddd; border-radius:5px; background-color:#f9f9f9; min-height:50px;">
            {output}
        </div>
    """
    st.markdown(result_html, unsafe_allow_html=True)
    
    # 2. SỬA NÚT COPY: Dùng JavaScript để copy kèm định dạng (Rich Text)
    st.write("")
    copy_button_html = """
    <button onclick="copyRichText()" style="cursor:pointer; background-color:#4CAF50; color:white; border:none; padding:8px 16px; border-radius:4px; font-weight:bold;">
        📋 Nhấn để Copy nội dung (Giữ định dạng)
    </button>

    <script>
    function copyRichText() {
        var range = document.createRange();
        var referenceNode = parent.document.getElementById("copy-area");
        range.selectNode(referenceNode);
        window.getSelection().removeAllRanges();
        window.getSelection().addRange(range);
        parent.document.execCommand("copy");
        window.getSelection().removeAllRanges();
        alert("Đã copy nội dung có định dạng!");
    }
    </script>
    """
    components.html(copy_button_html, height=50)

st.write("---")
st.write("💡 **Emoji chọn lọc:**")
tabs = st.tabs(list(EMOJI_LIST.keys()))
for i, tab in enumerate(tabs):
    with tab:
        st.code(EMOJI_LIST[list(EMOJI_LIST.keys())[i]], language="text")
