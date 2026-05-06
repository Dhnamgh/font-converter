import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Trình Đổi Font Tiếng Việt", layout="centered")

st.markdown("## 🔤 Trình Đổi Font Tiếng Việt")

# Dùng thử nhanh
example_text = "Ngày 06/5/2026 họp Chuyển đổi số tại Phòng Hội thảo"
if st.button(f"✨ Dùng thử nhanh: {example_text}"):
    st.session_state["main_input"] = example_text

# Danh sách Emoji được tách rời để tạo nút bấm riêng
EMOJI_GROUPS = {
    "Giáo dục & Y tế": ["🎓", "📖", "📝", "🏫", "📚", "🖊️", "🎒", "👨‍🏫", "👩‍🏫", "🩺", "🏥", "💉", "💊", "🧬", "🚑", "🧪", "🌡️", "🧠", "🩹"],
    "Dữ liệu & Du lịch": ["📈", "📉", "📊", "📋", "📂", "💻", "🔢", "🖥️", "🔍", "💡", "✈️", "🚗", "🏨", "🏖️", "🗺️", "⛰️", "🏟️", "🗼", "📸", "🌍", "🚢", "🚲"],
    "Hành chính": ["📑", "🏛️", "⚖️", "📨", "📞", "🏢", "✉️", "📜", "🗃️", "🔐", "📢", "🖋️", "🗂️", "📅", "💼", "🔑", "📁", "🗳️", "✒️", "🗞️"],
    "Fanpage": ["❤️", "🔥", "✅", "🚀", "📍", "📞", "💎", "⚡", "✨", "🌟", "🚩", "📌", "🎁", "🛒", "📩", "💯", "🆗", "📣", "💥", "🌈", "🎀", "🎊"]
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
    output_html = transform_text(input_text, style)
    st.markdown("### ✅ Kết quả")
    
    # Cỡ chữ inherit tự động khớp với khung nhập liệu
    custom_html = f"""
    <div id="wrapper" style="border: 1px solid #ddd; border-radius: 5px; padding: 10px; background-color: #f9f9f9;">
        <div id="content" style="font-size: inherit; font-family: sans-serif; color: #31333F; margin-bottom: 10px;">
            {output_html}
        </div>
        <button onclick="copyRichText()" style="cursor:pointer; background-color:#4CAF50; color:white; border:none; padding:5px 12px; border-radius:4px; font-size: 14px;">
            📋 Copy định dạng
        </button>
    </div>
    <script>
    function copyRichText() {{
        var range = document.createRange();
        var node = document.getElementById("content");
        range.selectNode(node);
        window.getSelection().removeAllRanges();
        window.getSelection().addRange(range);
        document.execCommand("copy");
        window.getSelection().removeAllRanges();
        event.target.innerText = "✅ Đã copy!";
        setTimeout(() => {{ event.target.innerText = "📋 Copy định dạng"; }}, 2000);
    }}
    </script>
    """
    components.html(custom_html, height=100)

st.write("---")
st.write("💡 **Emoji chọn lọc:**")

# SỬA: Thay đổi cách copy Emoji để giữ màu và không copy cả hàng
tabs = st.tabs(list(EMOJI_GROUPS.keys()))
for i, tab in enumerate(tabs):
    group_name = list(EMOJI_GROUPS.keys())[i]
    with tab:
        cols = st.columns(10) # Chia thành các ô nhỏ để nhấn copy từng cái
        for idx, emoji in enumerate(EMOJI_GROUPS[group_name]):
            with cols[idx % 10]:
                if st.button(emoji, key=f"emo_{group_name}_{idx}"):
                    # Dùng mẹo ẩn khung copy để giữ màu cho Emoji
                    components.html(f"""
                        <script>
                        const el = document.createElement('textarea');
                        el.value = '{emoji}';
                        document.body.appendChild(el);
                        el.select();
                        document.execCommand('copy');
                        document.body.removeChild(el);
                        </script>
                    """, height=0)
                    st.toast(f"Đã copy {emoji}")
