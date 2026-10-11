import streamlit as st

st.set_page_config(page_title="Antlers Sync (デモ版)", page_icon="⚽", layout="centered")

st.title("🔴⚪ Antlers Sync (ベータ版)")
st.caption("鹿島アントラーズ サポーター専用カレンダー＆観戦アシスタント")

# 会員区分選択
st.sidebar.header("⚙️ ユーザー設定")
member_cat = st.sidebar.selectbox("あなたの会員区分", ["SOCIO", "ファンクラブ", "一般"])

st.sidebar.success(f"現在の設定: {member_cat}会員")

# チケット案内カード
st.subheader("🗓 次の試合＆チケット情報")

with st.container():
    st.markdown("### ⚽ VS ガンバ大阪")
    st.write("📅 **日時**: 2026年10月9日 (金) 19:00 キックオフ")
    st.write("📍 **会場**: 県立カシマサッカースタジアム")
    
    ticket_url = "[suspicious link removed]"
    if member_cat == "SOCIO":
        [不審なリンクを削除しました]("🎟 **SOCIO最優先発売中！**")
    elif member_cat == "ファンクラブ":
        st.warning("🎟 **ファンクラブ先行発売中**")
    else:
        st.success("🎟 **一般発売準備中**")

    st.markdown(f"👉 **[{member_cat}専用チケット購入ページへ直行]({ticket_url})**")

st.divider()

# AI観戦日記
st.subheader("📝 AI観戦日記 & SNS投稿作成")

score = st.text_input("試合スコア・結果メモ", "鹿島 2 - 1 G大阪 (勝利!)")
impression = st.text_area("試合の感想", "優磨の勝ち越しヘッドで熱狂のカシマ！最高のアドバンテージを握った！")

if st.button("✨ AIでSNS投稿文を自動生成"):
    st.success("生成された投稿文:")
    post_text = f"【観戦日記】{score}\n{impression}\n\n#antlers #鹿島アントラーズ #AntlersSync"
    st.code(post_text)
    
    intent_url = f"[suspicious link removed]{post_text}"
    st.markdown(f"🐤 **[X (旧Twitter) でシェアする]({intent_url})**")
