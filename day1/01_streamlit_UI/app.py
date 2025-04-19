import streamlit as st
import pandas as pd
import numpy as np
import time
# import altair as alt # Altairを使う場合はコメント解除

# ============================================
# ページ設定
# ============================================
st.set_page_config(
    page_title="Streamlit デモ",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# タイトルと説明
# ============================================
st.title("Streamlit 初心者向けデモ")
st.markdown("### コメントを解除しながらStreamlitの機能を学びましょう")
st.markdown("このデモコードでは、コメントアウトされた部分を順番に解除しながらUIの変化を確認できます。")
st.markdown("---") # セクション区切りを追加

# ============================================
# サイドバー
# ============================================
st.sidebar.header("デモのガイド")
st.sidebar.info("""
各セクション（▼で表示）をクリックして展開し、
コードのコメントを解除して、
Streamlitの様々な機能を確認しましょう。
""")

# ============================================
# 基本的なUI要素 (折りたたみ可能)
# ============================================
with st.expander("▼ 基本的なUI要素", expanded=True): # 初期表示で開く
    # テキスト入力 (インデント確認)
    st.subheader("テキスト入力")
    st.markdown("`st.text_input()` : ユーザーからのテキスト入力を受け付けます。")
    name = st.text_input("あなたの名前", "ゲスト")
    st.write(f"こんにちは、{name}さん！")

    st.subheader("ボタン")
    st.markdown("`st.button()` : クリックイベントをトリガーします。")
    if st.button("クリックしてください"):
        st.success("ボタンがクリックされました！")
        st.balloons() # クリック時のギミック例

    st.subheader("チェックボックス")
    st.markdown("`st.checkbox()` : オン/オフの状態を持ちます。")
    if st.checkbox("チェックを入れると追加コンテンツが表示されます"):
        st.info("🔓 これは隠れたコンテンツです！")

    st.subheader("スライダー")
    st.markdown("`st.slider()` : 数値範囲から値を選択します。")
    age = st.slider("年齢", 0, 100, 25)
    st.write(f"あなたの年齢: {age}")

    st.subheader("セレクトボックス")
    st.markdown("`st.selectbox()` : 選択肢から一つを選びます。")
    option = st.selectbox(
        "好きなプログラミング言語は?",
        ["Python", "JavaScript", "Java", "C++", "Go", "Rust"],
        index=0 # デフォルト選択
    )
    st.write(f"あなたは `{option}` を選びました")

# ============================================
# レイアウト (折りたたみ可能)
# ============================================
with st.expander("▼ レイアウト"):
    # カラム (インデント確認)
    st.subheader("カラムレイアウト")
    st.markdown("`st.columns()` で画面を縦に分割します。")
    col1, col2 = st.columns(2) # 2つのカラムを作成

    with col1:
        st.info("ここは左カラム")
        st.number_input("数値を入力", value=10, key='col1_num')

    with col2:
        st.warning("ここは右カラム")
        st.metric("メトリクス", "42", "2%")

    # タブ (インデント確認)
    st.subheader("タブ")
    st.markdown("`st.tabs()` でコンテンツをタブで切り替えられます。")
    tab_labels = ["第1タブ", "第2タブ", "グラフタブ"]
    tab1, tab2, tab3 = st.tabs(tab_labels)

    with tab1:
        st.write("これは第1タブの内容です")
        st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=200)

    with tab2:
        st.write("これは第2タブの内容です")
        st.date_input("日付を選択")

    with tab3:
        st.write("タブ内にグラフも表示できます。")
        tab_chart_data = pd.DataFrame(
            np.random.randn(10, 2),
            columns=['X', 'Y'])
        st.line_chart(tab_chart_data)

    # エクスパンダー内コンテンツ例 (インデント確認)
    st.subheader("エクスパンダー内のコンテンツ例")
    st.markdown("（注: Streamlitの仕様上、エクスパンダーの入れ子はできません。これはエクスパンダー内に表示するコンテンツの例です。）")
    st.warning("これはエクスパンダー内に配置できるコンテンツの例です。")
    st.code("print('Hello, Content inside Expander!')", language='python')

# ============================================
# データ表示 (折りたたみ可能)
# ============================================
with st.expander("▼ データの表示"):
    # サンプルデータフレームを作成 (インデント確認)
    st.markdown("Pandas DataFrame を使ってデータを準備します。")
    df = pd.DataFrame({
        '名前': ['田中', '鈴木', '佐藤', '高橋', '伊藤'],
        '年齢': [25, 30, 22, 28, 33],
        '都市': ['東京', '大阪', '福岡', '札幌', '名古屋'],
        '評価': np.random.rand(5) * 5 # ランダムな評価を追加
    })

    st.subheader("データフレーム")
    st.markdown("`st.dataframe()` : スクロールやソートが可能なテーブルを表示します。")
    st.dataframe(df, use_container_width=True, height=200) # 高さを指定

    st.subheader("テーブル")
    st.markdown("`st.table()` : 静的なテーブルを表示します。")
    st.table(df.head(3)) # 最初の3行だけ表示

    st.subheader("メトリクス")
    st.markdown("`st.metric()` : 主要な指標を強調して表示します。変化量も示せます。")
    col1, col2, col3 = st.columns(3)
    col1.metric("温度", "23°C", "1.5°C")
    col2.metric("湿度", "45%", "-5%")
    col3.metric("アクティブユーザー", "1,234", "+50")

    st.subheader("JSON表示")
    st.markdown("`st.json()` : 辞書やJSONデータを整形して表示します。")
    sample_dict = {
        "data": {
            "items": [
                {"id": 1, "name": "apple", "price": 100},
                {"id": 2, "name": "banana", "price": 150}
            ],
            "count": 2
        },
        "status": "success"
    }
    st.json(sample_dict, expanded=False) # デフォルトで折りたたむ

# ============================================
# グラフ表示 (折りたたみ可能)
# ============================================
with st.expander("▼ グラフの表示"):
    # --- インデント修正箇所 ---
    # サンプルデータ (インデントを修正)
    chart_data_line = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    chart_data_bar = pd.DataFrame({
        'カテゴリ': ['A', 'B', 'C', 'D'],
        '値': [10, 25, 15, 30]
    }).set_index('カテゴリ')
    chart_data_area = pd.DataFrame(
        np.random.rand(10, 3),
        columns=['X', 'Y', 'Z']
    )

    # 以下のブロック全体のインデントを確認・修正
    st.subheader("ラインチャート")
    st.markdown("`st.line_chart()` : 時系列データなどの折れ線グラフを表示します。")
    st.line_chart(chart_data_line)

    st.subheader("バーチャート") # エラーが出ていた行のインデントを修正
    st.markdown("`st.bar_chart()` : カテゴリ間の比較などに使う棒グラフを表示します。")
    st.bar_chart(chart_data_bar)

    st.subheader("エリアチャート")
    st.markdown("`st.area_chart()` : 折れ線グラフの下の領域を塗りつぶしたグラフです。")
    st.area_chart(chart_data_area)

    # Altairを使ったより高度なグラフ (オプション)
    st.subheader("Altair チャート (要 `pip install altair`)")
    st.markdown("`st.altair_chart()` でより複雑なグラフも描画できます。")
    try:
        import altair as alt # 関数内でimport
        scatter_data = pd.DataFrame(
            np.random.randn(100, 3),
            columns=['x', 'y', 'category']
        )
        scatter_data['category'] = pd.cut(scatter_data['category'], bins=3, labels=['G1', 'G2', 'G3'])

        chart = alt.Chart(scatter_data).mark_circle(size=60).encode(
            x='x',
            y='y',
            color='category',
            tooltip=['x', 'y', 'category']
        ).interactive() #インタラクティブ操作を有効化
        st.altair_chart(chart, use_container_width=True)
    except ImportError:
        st.warning("Altairライブラリが見つかりません。インタラクティブな散布図を表示するには、`pip install altair` を実行してください。")
    except Exception as e:
        st.error(f"Altairチャートの描画中にエラーが発生しました: {e}")
    # --- インデント修正箇所 ここまで ---

# ============================================
# インタラクティブ機能 (折りたたみ可能)
# ============================================
with st.expander("▼ インタラクティブ機能"):
    # プログレスバー (インデント確認)
    st.subheader("プログレスバー")
    st.markdown("`st.progress()` で処理の進捗状況を視覚的に示します。")
    if st.button("進捗をシミュレート"):
        st.info("プログレスバーが動作します。完了すると風船が出ます！")
        my_bar = st.progress(0) # プログレスバーを初期化
        for percent_complete in range(100):
            time.sleep(0.02) # 少しゆっくりに
            my_bar.progress(percent_complete + 1)
        st.balloons()
        st.success("シミュレーション完了！")

    # ファイルアップロード (インデント確認)
    st.subheader("ファイルアップロード")
    st.markdown("`st.file_uploader()` でユーザーがファイルをアップロードできるようにします。")
    uploaded_file = st.file_uploader(
        "CSV または TXT ファイルをアップロード",
        type=["csv", "txt"],
        accept_multiple_files=False # 単一ファイルのみ受け付ける
    )
    if uploaded_file is not None:
        st.success(f"ファイル '{uploaded_file.name}' がアップロードされました！")
        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
        st.write(file_details)

        if uploaded_file.type == "text/csv":
            try:
                df_uploaded = pd.read_csv(uploaded_file)
                st.write("CSVデータのプレビュー (最初の5行):")
                st.dataframe(df_uploaded.head())
            except Exception as e:
                st.error(f"CSVファイルの読み込み中にエラーが発生しました: {e}")
        elif uploaded_file.type == "text/plain":
            try:
                stringio = uploaded_file.getvalue().decode("utf-8")
                st.write("テキストファイルの内容 (最初の数行):")
                st.text_area("内容", stringio, height=150, key="txt_preview")
            except Exception as e:
                st.error(f"テキストファイルの処理中にエラーが発生しました: {e}")

    # カメラ入力 (インデント確認)
    st.subheader("カメラ入力")
    st.markdown("`st.camera_input()` でウェブカメラから画像を取得できます。(ローカル環境や権限許可が必要)")
    try:
        picture = st.camera_input("写真を撮る")
        if picture:
            st.image(picture)
            st.info("写真が撮影されました！")
    except Exception as e:
        st.warning(f"カメラ入力機能の利用中にエラーが発生しました: {e}\nウェブカメラへのアクセス許可や、環境によっては利用できない場合があります。")


# ============================================
# カスタマイズ (折りたたみ可能)
# ============================================
with st.expander("▼ スタイルのカスタマイズ"):
    # Markdown と HTML/CSS (インデント確認)
    st.subheader("Markdown と HTML/CSS")
    st.markdown("`st.markdown(..., unsafe_allow_html=True)` を使うと、HTMLタグやCSSを埋め込めます。")

    st.markdown("""
    <style>
    /* Streamlitのデフォルトスタイルを一部上書き */
    .stButton>button {
        background-color: #4CAF50; /* 緑色 */
        color: white;
        border-radius: 8px;
        border: none; /* 枠線を消す */
        padding: 10px 24px; /* パディング調整 */
        transition: background-color 0.3s ease; /* ホバー効果を滑らかに */
    }
    .stButton>button:hover {
        background-color: #45a049;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); /* ホバー時に影を追加 */
    }
    .big-font-expander {
        font-size: 22px !important; /* !importantで優先度を上げる */
        font-weight: bold;
        color: #ff4b4b; /* Streamlitの赤色系 */
        border-bottom: 2px solid #ff4b4b; /* 下線を追加 */
        display: inline-block; /* 下線の幅をテキストに合わせる */
        padding-bottom: 2px;
        margin-bottom: 10px; /* 下の要素とのマージン */
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font-expander">これはカスタムCSSでスタイリングされたテキストです！</p>', unsafe_allow_html=True)

    if st.button("スタイル適用テストボタン"):
        st.write("このボタンのスタイルがCSSで変更されています。")

    # テーマのカスタマイズ (インデント確認)
    st.subheader("テーマのカスタマイズ")
    st.markdown("Streamlitの設定メニュー（右上の☰）からテーマ（Light/Dark）を変更したり、カスタムテーマを作成できます。")
    st.markdown("`.streamlit/config.toml` ファイルを作成して、より詳細なテーマ設定も可能です。")
    st.code("""
# .streamlit/config.toml の例
[theme]
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"
""")

# ============================================
# デモの使用方法 (折りたたみ可能)
# ============================================
st.divider()
with st.expander("▼ このデモの使い方"):
    st.markdown("""
    1. コードエディタでコメントアウトされた部分を見つけます（#で始まる行）
    2. 確認したい機能のコメントを解除します（先頭の#を削除）
    3. 変更を保存して、ブラウザで結果を確認します
    4. 様々な組み合わせを試して、UIがどのように変化するか確認しましょう
    """)

    st.code("""
# 例：ボタンのコメントアウトを解除する

# --- 解除前 ---
# st.subheader("ボタン")
# # if st.button("クリックしてください"):
# #     st.success("ボタンがクリックされました！")
# #     st.balloons()

# --- 解除後 ---
st.subheader("ボタン")
if st.button("クリックしてください"):       # 行頭の '#' を削除
    st.success("ボタンがクリックされました！") # 行頭の '#' を削除
    st.balloons()                       # 行頭の '#' を削除

""", language='python')
    st.warning("コメントの解除やコードの変更は、Pythonのインデント（字下げ）を崩さないように注意してください。")