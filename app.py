import streamlit as st

# --- 1. 页面配置与注入【还原版】鬼畜样式 ---
st.set_page_config(page_title="2bTI 灵魂拷问 2.0", page_icon="☢️")

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(125deg, #ff00ff, #7000ff, #00ffff, #ff0000, #ffff00);
        background-size: 800% 800%;
        animation: anim 12s ease infinite;
    }
    @keyframes anim { 0%{background-position:0% 50%} 50%{background-position:100% 50%} 100%{background-position:0% 50%} }

    h1, h2, h3, p, span, label {
        color: #ffffff !important;
        text-shadow: 2px 2px 0px #000, -1px -1px 0px #000, 1px -1px 0px #000, -1px 1px 0px #000, 0px 0px 8px #ff00ff !important;
        font-family: 'Comic Sans MS', 'SimHei', sans-serif;
    }

    .quiz-container {
        background: rgba(0, 0, 0, 0.7);
        padding: 30px;
        border-radius: 20px;
        border: 4px solid #00ff00;
        box-shadow: 0 0 20px #00ff00;
        margin-bottom: 20px;
    }

    .stButton>button {
        background-color: #000 !important;
        color: #00ff00 !important;
        border: 3px solid #00ff00 !important;
        font-size: 22px !important;
        font-weight: bold !important;
        width: 100%;
        border-radius: 10px !important;
        padding: 15px !important;
        transition: 0.2s;
        text-shadow: none !important;
    }
    .stButton>button:hover {
        background-color: #ff00ff !important;
        color: #fff !important;
        border: 3px solid #fff !important;
        transform: scale(1.02) rotate(-1deg);
        box-shadow: 0 0 30px #ff00ff;
    }

    .result-card {
        background: rgba(0, 0, 0, 0.9);
        border: 6px double #ff00ff;
        padding: 30px;
        border-radius: 5px;
        color: #fff;
        line-height: 1.6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 初始化逻辑（平衡权重版） ---
if 'page' not in st.session_state:
    st.session_state.page = 'intro'
if 'zx_axis' not in st.session_state:
    st.session_state.zx_axis = 0 # 正经-抽象轴
if 'se_axis' not in st.session_state:
    st.session_state.se_axis = 0 # 帅气-恶心轴

# --- 3. 页面渲染逻辑 ---

# 【前导页】
if st.session_state.page == 'intro':
    st.markdown("<h1 style='font-size: 3.5rem;'>别装了！测测你到底是个什么<br>NB / SB / NM / TM？</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="quiz-container">
        <h3>【前导语】</h3>
        <p style='font-size: 1.2rem;'>朋友，你是否经常在深夜对着镜子产生一些违法但合理的想法？<br>
        你是否在面对“Bro”和“Bra”时有过一丝灵魂的震颤？<br><br>
        别再用心理词汇洗白自己了，快来认领你的<b>“畜生位”</b>。<br>
        这里没有心理医生，只有最真实的灵魂拷问。</p>
        <p style='color: #ffff00; font-weight: bold;'>⚠️ 警告：本测评包含大量抽象思维及对老油条的不尊重。</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🔥 [ 我倒要看看我有多变态 ] 🔥"):
        st.session_state.zx_axis, st.session_state.se_axis = 0, 0
        st.session_state.page = 'quiz'
        st.session_state.current_q = 0
        st.rerun()

# 【测试页】
elif st.session_state.page == 'quiz':
    # 算法修正：(文本, zx变动, se变动)
    questions = [
        {"q": "Q1：深夜独自在卧室想确认自己的硬件规格（物理），你会？", 
         "opts": [("拿卷尺精准测量并Excel建模对比", 3, 1), ("敲击键盘问AI这算不算乐器", -2, 1)]},
        {"q": "Q2：当你在公共场合不小心产生了一个“生化武器”级闷屁时？", 
         "opts": [("保持眼神坚定，抬头挺胸帅气走开", 1, 3), ("悄悄兜一下闻闻确认肠道菌群是否健康", 0, -2)]},
        {"q": "Q3：如果你在街上看到一个绝世美女/帅哥，内心OS是？", 
         "opts": [("他在看我，一定被我的贵族气质吸引了", 2, 2), 
                  ("问他愿不愿意教我在水里吐泡泡", -3, 1), 
                  ("这腿够玩一年，洗澡会搓出很多泥吧", 1, -2), 
                  ("当众表演原地拉稀引起他的注意", -4, -4)]},
        {"q": "Q4：关于“Bra”和“Bro”的选择，你更倾向于？", 
         "opts": [("研究Bra的力学结构（理工男的严谨）", 3, -1), ("把Bra戴在头上大喊：看我新买的防雷头盔！", -3, 2)]},
        {"q": "Q5：发现自己今天没穿内裤出门时，你会？", 
         "opts": [("视为原始自由，步伐更加坚定自信", 2, 3), 
                  ("突然掀起衣角向好友展示那空荡荡的腰间", -3, 0), 
                  ("以此撰写朋友圈“通风健康指南”", 3, -2), 
                  ("在公共座椅疯狂磨蹭留下属于自己的信息", -4, -5)]},
        {"q": "Q6：如果你误入了一个满是异性的更衣室，你会？", 
         "opts": [("优雅转身：别看我，我只是路过的神", 3, 3), 
                  ("螃蟹步逃离现场并大喊：为了部落！", -2, 1), 
                  ("研究排水沟消防结构（其实耳朵竖得比兔高）", 2, -3), 
                  ("表演杂技并问在场的人需不需要搓背", -4, -4)]}
    ]

    curr = questions[st.session_state.current_q]
    st.progress((st.session_state.current_q) / len(questions))
    st.markdown(f"<div class='quiz-container'><h2>{curr['q']}</h2></div>", unsafe_allow_html=True)
    
    for text, zx_val, se_val in curr["opts"]:
        if st.button(text):
            st.session_state.zx_axis += zx_val
            st.session_state.se_axis += se_val
            st.session_state.current_q += 1
            if st.session_state.current_q >= len(questions):
                st.session_state.page = 'result'
            st.rerun()

# 【结果页】
elif st.session_state.page == 'result':
    st.markdown("<h1>🧪 2bTI 鉴定报告</h1>", unsafe_allow_html=True)
    zx, se = st.session_state.zx_axis, st.session_state.se_axis
    
    if zx >= 0 and se >= 0: res = "NB"
    elif zx < 0 and se >= 0: res = "SB"
    elif zx >= 0 and se < 0: res = "NM"
    else: res = "TM"
    
    data = {
        "NB": ("🧬 [2B-NB] 正经帅气型 (Narcissistic Boss)", "如果帅是一种罪，我可能已经死刑起步了。", "你是典型的“精致利己主义装杯犯”。即便在量JJ这种荒诞时刻也要讲究精准度。你的生活是一场真人秀，而你永远是自带滤镜的一号。"),
        "SB": ("🤡 [2B-SB] 抽象帅气型 (Stylized Buffoon)", "上帝给了我一副好皮囊，但我决定拿它来整活。", "你是社交圈的氧气泵。颜值上限极高，智商下限深不可测。只要不说话就是男神，一张嘴大家就想报警。"),
        "NM": ("🧐 [2B-NM] 正经恶心型 (Normal Monster)", "我不是变态，我只是对世界有着极度严谨的生理好奇。", "学术型变态。你看起来像个教授，其实是个怪谈。喜欢用科学逻辑去解释猥琐行为，看人的眼神像在看生理解剖标本。"),
        "TM": ("☢️ [2B-TM] 抽象恶心型 (Total Mutant)", "人类进化的时候，我可能在旁边忙着钻木取火。", "纯粹的“混沌恶”。你完全抛弃了碳基生物的体面，你的每一个点子都让舍友想连夜搬出宿舍。")
    }
    
    title, quote, detail = data[res]
    st.markdown(f"""
    <div class="result-card">
        <h2 style='color: #00ff00; text-align: left;'>{title}</h2>
        <h3 style='color: #ffff00; font-style: italic; text-align: left;'>“{quote}”</h3>
        <hr style='border: 1px solid #555;'>
        <p style='font-size: 1.3rem; line-height: 1.8;'><b>人格侧写：</b>{detail}</p>
        <p style='color: #00ffff;'><b>[ 算法分析 ]：</b>正经指数 {zx} | 帅气指数 {se}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("不服？洗心革面重新测"):
        st.session_state.zx_axis, st.session_state.se_axis = 0, 0
        st.session_state.page = 'intro'
        st.rerun()