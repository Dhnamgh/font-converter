import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Trình Đổi Font Tiếng Việt", layout="centered")

st.markdown("## 🔤 Trình Đổi Font Tiếng Việt")

# Dùng thử nhanh
example_text = "Ngày 06/5/2026 họp Chuyển đổi số tại Phòng Hội thảo"
if st.button(f"✨ Dùng thử nhanh: {example_text}"):
    st.session_state["main_input"] = example_text

# Danh sách Emoji - GIỮ NGUYÊN[cite: 2]
EMOJI_GROUPS = {
    "Giáo dục & Y tế": ["🎓", "📖", "📝", "🏫", "📚", "🖊️", "🎒", "👨‍🏫", "👩‍🏫", "🩺", "🏥", "💉", "💊", "🧬", "🚑", "🧪", "🌡️", "🧠", "🩹"],
    "Dữ liệu & Du lịch": ["📈", "📉", "📊", "📋", "📂", "💻", "🔢", "🖥️", "🔍", "💡", "✈️", "🚗", "🏨", "🏖️", "🗺️", "⛰️", "🏟️", "🗼", "📸", "🌍", "🚢", "🚲"],
    "Hành chính": ["📑", "🏛️", "⚖️", "📨", "📞", "🏢", "✉️", "📜", "🗃️", "🔐", "📢", "🖋️", "🗂️", "📅", "💼", "🔑", "📁", "🗳️", "✒️", "🗞️"],
    "Fanpage": ["❤️", "🔥", "✅", "🚀", "📍", "📞", "💎", "⚡", "✨", "🌟", "🚩", "📌", "🎁", "🛒", "📩", "💯", "🆗", "📣", "💥", "🌈", "🎀", "🎊"]
}

# Hàm chuyển đổi HTML - GIỮ NGUYÊN[cite: 2]
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

# BỔ SUNG: Hàm bổ trợ riêng để dán được vào Fanpage/Zalo
def to_unicode(text, style):
    if style == "Chữ thường": return text
    bold_map = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗")
    italic_map = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸ｘ𝘺𝘻0123456789")
    if style == "In đậm": return text.translate(bold_map)
    if style == "In nghiêng": return text.translate(italic_map)
    if style == "Gạch chân": return "".join([c + "\u0332" for c in text])
    return text

input_text = st.text_area("📌 Nhập nội dung", height=120, key="main_input")
style = st.radio("🎨 Chọn kiểu chữ", ["Chữ thường", "In đậm", "In nghiêng", "Gạch chân"], horizontal=True)

if input_text:
    output_html = transform_text(input_text, style)
    unicode_output = to_unicode(input_text, style)
    
    st.markdown("### ✅ Kết quả")
    
    # Khung hiển thị và Copy định dạng cho Word - GIỮ NGUYÊN[cite: 2]
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
    
    # BỔ SUNG: Khung dành riêng cho Fanpage/Zalo[cite: 1]
    st.info("👇 Dùng khung này để dán vào Fanpage/Zalo (vẫn giữ được Đậm/Nghiêng):")
    st.code(unicode_output, language="text")

st.write("---")
st.write("💡 **Emoji chọn lọc (nhấn/chọn vào để Copy):**")

# Hệ thống Emoji - GIỮ NGUYÊN[cite: 2]
tabs = st.tabs(list(EMOJI_GROUPS.keys()))
for i, tab in enumerate(tabs):
    group_name = list(EMOJI_GROUPS.keys())[i]
    with tab:
        cols = st.columns(10)
        for idx, emoji in enumerate(EMOJI_GROUPS[group_name]):
            with cols[idx % 10]:
                st.components.v1.html(f"""
                    <button onclick="copyEmoji('{emoji}')" style="font-size:20px; border:none; background:none; cursor:pointer; width:100%; height:100%;">
                        {emoji}
                    </button>
                    <script>
                    function copyEmoji(emo) {{
                        navigator.clipboard.writeText(emo);
                    }}
                    </script>
                """, height=40)
