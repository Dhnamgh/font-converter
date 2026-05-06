import streamlit as st

st.set_page_config(page_title="Trình Đổi Font Tiếng Việt - Bản Full", layout="centered")

# Phục hồi giao diện đầy đủ[cite: 2]
st.markdown("## 🔤 Trình Đổi Font Tiếng Việt")

# Phục hồi tính năng "Dùng thử nhanh"[cite: 2]
example_text = "Ngày 06/5/2026 họp Chuyển đổi số tại Phòng Hội thảo"
if st.button(f"✨ Dùng thử nhanh: {example_text}"):
    st.session_state["main_input"] = example_text

# Phục hồi danh sách Emoji đầy đủ[cite: 2]
EMOJI_LIST = {
    "Giáo dục & Y tế": "🎓 📖 📝 🏫 📚 🖊️ 🎒 👨‍🏫 👩‍🏫 🩺 🏥 💉 💊 🧬 🚑 🧪 🌡️ 🧠 🩹",
    "Dữ liệu & Du lịch": "📈 📉 📊 📋 📂 💻 🔢 🖥️ 🔍 💡 ✈️ 🚗 🏨 🏖️ 🗺️ ⛰️ 🏟️ 🗼 📸 🌍 🚢 🚲",
    "Hành chính": "📑 🏛️ ⚖️ 📨 📞 🏢 ✉️ 📜 🗃️ 🔐 📢 🖋️ 🗂️ 📅 💼 🔑 📁 🗳️ ✒️ 🗞️",
    "Fanpage": "❤️ 🔥 ✅ 🚀 📍 📞 💎 ⚡ ✨ 🌟 🚩 📌 🎁 🛒 📩 💯 🆗 📣 💥 🌈 🎀 🎊"
}

def transform_text(text, style):
    if not text or style == "Chữ thường":
        return text
    
    # Sử dụng HTML để đảm bảo chữ Đ và các chữ có dấu hiển thị chuẩn 100%[cite: 2]
    if style == "In đậm":
        return f"<b>{text}</b>"
    elif style == "In nghiêng":
        return f"<i>{text}</i>"
    elif style == "Gạch chân":
        return f"<u>{text}</u>"
    return text

# Nhập liệu
input_text = st.text_area("📌 Nhập nội dung", height=120, key="main_input")
style = st.radio("🎨 Chọn kiểu chữ", ["Chữ thường", "In đậm", "In nghiêng", "Gạch chân"], horizontal=True)

if input_text:
    output = transform_text(input_text, style)
    st.markdown("### ✅ Kết quả")
    
    # ĐÃ SỬA: Cỡ chữ kết quả 16px khớp với cỡ chữ nhập vào[cite: 2]
    st.markdown(f"""
        <div style='font-size:16px; padding:10px; border:1px solid #ddd; border-radius:5px; background-color: #f9f9f9;'>
            {output}
        </div>
    """, unsafe_allow_html=True)
    
    # Cung cấp dạng text thuần để copy nhanh nếu cần[cite: 2]
    st.info("Để giữ định dạng Đậm/Nghiêng sang Word/Fanpage, hãy bôi đen trực tiếp nội dung ở khung phía trên rồi Copy.")
    if style == "Gạch chân":
        plain_output = "".join([c + "\u0332" for c in input_text])
    else:
        plain_output = input_text 
    st.code(plain_output, language="text")

st.write("---")
# ĐÃ SỬA: Tên tiêu đề theo yêu cầu[cite: 2]
st.write("💡 **Emoji chọn lọc:**")
tabs = st.tabs(list(EMOJI_LIST.keys()))
for i, tab in enumerate(tabs):
    with tab:
        st.code(EMOJI_LIST[list(EMOJI_LIST.keys())[i]], language="text")
