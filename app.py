import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Trình Đổi Font Tiếng Việt", layout="centered")

st.markdown("## 🔤 Trình Đổi Font Tiếng Việt")

# Dùng thử nhanh - GIỮ NGUYÊN
example_text = "Ngày 06/5/2026 họp Chuyển đổi số tại Phòng Hội thảo"
if st.button(f"✨ Dùng thử nhanh: {example_text}"):
    st.session_state["main_input"] = example_text

# Danh sách Emoji - GIỮ NGUYÊN
EMOJI_GROUPS = {
    "Giáo dục & Y tế": ["🎓", "📖", "📝", "🏫", "📚", "🖊️", "🎒", "👨‍🏫", "👩‍🏫", "🩺", "🏥", "💉", "💊", "🧬", "🚑", "🧪", "🌡️", "🧠", "🩹"],
    "Dữ liệu & Du lịch": ["📈", "📉", "📊", "📋", "📂", "💻", "🔢", "🖥️", "🔍", "💡", "✈️", "🚗", "🏨", "🏖️", "🗺️", "⛰️", "🏟️", "🗼", "📸", "🌍", "🚢", "🚲"],
    "Hành chính": ["📑", "🏛️", "⚖️", "📨", "📞", "🏢", "✉️", "📜", "🗃️", "🔐", "📢", "🖋️", "🗂️", "📅", "💼", "🔑", "📁", "🗳️", "✒️", "🗞️"],
    "Fanpage": ["❤️", "🔥", "✅", "🚀", "📍", "📞", "💎", "⚡", "✨", "🌟", "🚩", "📌", "🎁", "🛒", "📩", "💯", "🆗", "📣", "💥", "🌈", "🎀", "🎊"]
}

# Hàm hiển thị HTML cho Word - GIỮ NGUYÊN[cite: 2]
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

# SỬA LỖI: Hàm chuyển đổi Unicode hỗ trợ đầy đủ Tiếng Việt cho Fanpage/Zalo
def full_unicode_transform(text, style):
    if not text or style == "Chữ thường": return text
    
    # Bảng mã Latin chuẩn[cite: 1]
    latin = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    bold = "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"
    italic = "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸ｘ𝘺𝘻0123456789"
    
    mapping = ""
    if style == "In đậm": mapping = bold
    elif style == "In nghiêng": mapping = italic
    elif style == "Gạch chân": return "".join([c + "\u0332" for c in text])
    else: return text

    table = str.maketrans(latin, mapping)
    
    # Xử lý ký tự có dấu bằng cách tách dấu và áp dụng kiểu cho chữ cái gốc
    import unicodedata
    normalized_text = unicodedata.normalize('NFD', text)
    transformed_text = ""
    for char in normalized_text:
        # Nếu là chữ cái Latin thì chuyển đổi, nếu là dấu thì giữ nguyên để nó "dính" vào chữ trước đó[cite: 1]
        transformed_text += char.translate(table)
    
    return unicodedata.normalize('NFC', transformed_text)

input_text = st.text_area("📌 Nhập nội dung", height=120, key="main_input")
style = st.radio("🎨 Chọn kiểu chữ", ["Chữ thường", "In đậm", "In nghiêng", "Gạch chân"], horizontal=True)

if input_text:
    output_html = transform_text(input_text, style)
    # Chuẩn bị sẵn văn bản Unicode để dán mọi nơi[cite: 1]
    copy_val = full_unicode_transform(input_text, style).replace("'", "\\'").replace("\n", "\\n")
    
    st.markdown("### ✅ Kết quả")
    
    custom_html = f"""
    <div id="wrapper" style="border: 1px solid #ddd; border-radius: 5px; padding: 10px; background-color: #f9f9f9;">
        <div id="content" style="font-size: inherit; font-family: sans-serif; color: #31333F; margin-bottom: 10px;">
            {output_html}
        </div>
        <button onclick="copyAll()" style="cursor:pointer; background-color:#4CAF50; color:white; border:none; padding:5px 12px; border-radius:4px; font-size: 14px;">
            📋 Nhấn để Copy (Dán được Fanpage/Zalo/Word)
        </button>
    </div>
    <script>
    function copyAll() {{
        const text = `{copy_val}`;
        navigator.clipboard.writeText(text).then(() => {{
            event.target.innerText = "✅ Đã copy xong!";
            setTimeout(() => {{ event.target.innerText = "📋 Nhấn để Copy (Dán được Fanpage/Zalo/Word)"; }}, 2000);
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
