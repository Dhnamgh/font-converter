import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Trình Đổi Font Tiếng Việt", layout="centered")

st.markdown("## 🔤 Trình Đổi Font Tiếng Việt")

# Dùng thử nhanh - GIỮ NGUYÊN
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

# Hàm chuyển đổi hiển thị HTML (dùng cho bôi đen copy sang Word) - GIỮ NGUYÊN[cite: 2]
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

# Logic Unicode để dán vào Fanpage/Zalo vẫn giữ định dạng
def to_unicode_style(text, style):
    if not text or style == "Chữ thường": return text
    # Maps chuẩn để Facebook/Zalo không thể đưa về chữ thường[cite: 1]
    maps = {
        "In đậm": ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", 
                   "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"),
        "In nghiêng": ("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", 
                      "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸ｘ𝘺𝘻")
    }
    if style == "Gạch chân":
        return "".join([c + "\u0332" for c in text])
    if style in maps:
        c_from, c_to = maps[style]
        table = str.maketrans(c_from, c_to)
        return text.translate(table)
    return text

input_text = st.text_area("📌 Nhập nội dung", height=120, key="main_input")
style = st.radio("🎨 Chọn kiểu chữ", ["Chữ thường", "In đậm", "In nghiêng", "Gạch chân"], horizontal=True)

if input_text:
    output_html = transform_text(input_text, style)
    # Tạo sẵn chuỗi Unicode để nút bấm copy dùng[cite: 1]
    unicode_str = to_unicode_style(input_text, style).replace("'", "\\'").replace("\n", "\\n")
    
    st.markdown("### ✅ Kết quả")
    
    # Khung hiển thị - Sửa nút bấm để copy dạng Unicode giúp dán được mọi nơi
    custom_html = f"""
    <div id="wrapper" style="border: 1px solid #ddd; border-radius: 5px; padding: 10px; background-color: #f9f9f9;">
        <div id="content" style="font-size: inherit; font-family: sans-serif; color: #31333F; margin-bottom: 10px;">
            {output_html}
        </div>
        <button onclick="copyToClipboard()" style="cursor:pointer; background-color:#4CAF50; color:white; border:none; padding:5px 12px; border-radius:4px; font-size: 14px;">
            📋 Copy (Dán được Fanpage/Zalo/Word)
        </button>
    </div>
    <script>
    function copyToClipboard() {{
        const text = `{unicode_str}`;
        navigator.clipboard.writeText(text).then(() => {{
            event.target.innerText = "✅ Đã copy!";
            setTimeout(() => {{ event.target.innerText = "📋 Copy (Dán được Fanpage/Zalo/Word)"; }}, 2000);
        }});
    }}
    </script>
    """
    components.html(custom_html, height=100)

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
                    <button onclick="navigator.clipboard.writeText('{emoji}')" style="font-size:20px; border:none; background:none; cursor:pointer; width:100%; height:100%;">
                        {emoji}
                    </button>
                """, height=40)
