import streamlit as st

# --- 1. 页面配置与注入【算法加强版】鬼畜样式 ---
st.set_page_config(page_title="2bTI 灵魂拷问 2.0", page_icon="☢️")

st.markdown("""
    <style>
    /* 动态背景：增加色彩深度 */
    .stApp {
        background: linear-gradient(125deg, #ff00ff, #7000ff, #00ffff, #ff0000, #ffff00);
        background-size: 800% 800%;
        animation: anim 12s ease infinite;
    }
    @keyframes anim {
        0%{background-position:0% 50%}
        50%{background-position:100% 50%}
        100%{background-position:0% 50%}
    }

    /* 文字阴影保护，确保在亮色背景下清晰 */
    h1, h2, h3, p, span, label {
        color: #ffffff !important;
        text-shadow: 
            2px 2px 0px #000, 
            -1px -1px 0px #000, 
            1px -1px 0px #000, 
            -1px 1px 0px #000,
            0px 0px 10px #ff00ff !important;
        font-family: 'Comic Sans MS', 'SimHei', sans-serif;
    }

    /* 容器样式 */
    .quiz-container {
        background: rgba(0, 0, 0, 0.75);
        padding: 25px;
        border-radius: 15px;
        border: 3px solid #00ff00;
        box-shadow: 0 0 20px rgba(0, 255, 0, 0.5);
        margin-bottom: 20px;
    }

    /* 按钮样式：黑绿高对比 */
    .stButton>button {
        background-color: #000 !important;
        color: #00ff00 !important;
        border: 2px solid #00ff00 !important;
        font-size: 20px !important;
        font-weight: bold !important;
        width: 100%;
        border-radius: 10px !important;
        padding: 12px !important;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background-color: #ff00ff !important;
        color: #fff !important;
        border: 2px solid #fff !important;
        transform: scale(1.03) rotate(-1deg);
    }

    /* 结果卡片 */
    .result-card {
        background: rgba(0, 0, 0, 0.9);
        border: 5px double #ff00ff;
        padding: 30px;
        border-radius: 10px;
        box-shadow: 0 0 30px #ff00ff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. 初始化核心逻辑：坐标轴系统 ---
# zx_axis: 正数偏正经(Z)，负数偏抽象(X)
# se_axis: 正数偏帅气(S)，负数偏恶心(E)
if 'page' not in st.session_state:
    st.session_state.page = 'intro'
if 'zx_axis' not in st.session_state:
    st.session_state.zx_axis = 0
if 'se_axis' not in st.session_state:
    st.session_state.se_axis = 0

# --- 3. 页面渲染 ---

# 【前导页】
if st.session_state.page == 'intro':
    st.markdown("<h1>☢️ 2bTI 灵魂拷问 <span style='color:#ffff00'>v2.0</span></h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="quiz-container">
        <h3>【算法纠偏系统已上线】</h3>
        <p style='font-size: 1.1rem;'>检测到 v1.0 版本存在严重的“伪君子”溢出风险，本版本引入了<b>坐标轴非线性判定逻辑</b>。</p>
        <p style='font-size: 1.1rem;'>简单来说：装杯很难，变态很容易。只要你露出一点马脚，系统会瞬间识别你的“畜生位”。</p>
        <p style='color: #ff00ff; font-weight: bold;'>⚠️ 正在进入北航 2b 行为实验室...</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🔥 [ 重新接受审判 ] 🔥"):
        st.session_state.zx_axis = 0
        st.session_state.se_axis = 0
        st.session_state.page = 'quiz'
        st.session_state.current_q = 0
        st.rerun()

# 【测试页】
elif st.session_state.page == 'quiz':
    # 权重配置: (zx正经/抽象权重, se帅气/恶心权重)
    # 正数向 Z/S 移动，负数向 X/E 移动
    questions = [
        {"q": "Q1：深夜想确认自己的硬件规格（物理），你会？", 
         "opts": [("拿卷尺精准测量并Excel建模对比", 2, 1), ("敲击键盘问AI这算不算乐器", -4, 1)]},
        
        {"q": "Q2：当你在公共场合放了一个生化武器级闷屁？", 
         "opts": [("保持眼神坚定，抬头挺胸帅气走开", 1, 3), ("悄悄兜一下闻闻确认肠道菌群", 0, -6)]},
        
        {"q": "Q3：如果你在街上看到一个绝世美女/帅哥，内心OS是？", 
         "opts": [("他在看我，一定被我的贵族气质吸引了", 1, 3), 
                  ("问他愿不愿意教我在水里吐泡泡", -5, 1), 
                  ("这腿够玩一年，洗澡会搓出很多泥吧", 1, -5), 
                  ("当众表演原地拉稀引起他的注意", -15, -15)]},
        
        {"q": "Q4：关于“Bra”和“Bro”的选择，你更倾向于？", 
         "opts": [("研究Bra的力学结构", 3, -2), ("戴在头上喊：看我新买的防雷头盔！", -6, 1)]},
        
        {"q": "Q5：发现自己今天没穿内裤出门时，你会？", 
         "opts": [("视为原始自由，步伐更加坚定自信", 1, 3), 
                  ("突然掀起衣角向好友展示那空荡荡的腰间", -6, 0), 
                  ("以此撰写朋友圈“局部通风健康指南”", 3, -4), 
                  ("在公共座椅疯狂磨蹭留下自己的信息", -10, -15)]},
        
        {"q": "Q6：如果你误入了一个满是异性的更衣室，你会？", 
         "opts": [("优雅转身：别看我，我只是路过的神", 3, 3), 
                  ("螃蟹步逃离：为了部落！", -5, 1), 
                  ("研究排水沟消防结构（其实在偷听）", 3, -7), 
                  ("表演杂技并问在场的人需不需要搓背", -15, -15)]}
    ]

    curr = questions[st.session_state.current_q]
    
    # 进度条
    st.progress(st.session_state.current_q / len(questions))
    
    st.markdown(f"<div class='quiz-container'><h2>{curr['q']}</h2></div>", unsafe_allow_html=True)
    
    # 按钮渲染
    for text, zx_w, se_w in curr["opts"]:
        if st.button(text):
            st.session_state.zx_axis += zx_w
            st.session_state.se_axis += se_w
            st.session_state.current_q += 1
            if st.session_state.current_q >= len(questions):
                st.session_state.page = 'result'
            st.rerun()

# 【结果页】
elif st.session_state.page == 'result':
    st.markdown("<h1>🧪 2bTI 深度鉴定报告</h1>", unsafe_allow_html=True)
    
    zx = st.session_state.zx_axis
    se = st.session_state.se_axis
    
    # 判定逻辑：象限判定法
    if zx >= 0 and se >= 0:
        res = "NB"
    elif zx < 0 and se >= 0:
        res = "SB"
    elif zx >= 0 and se < 0:
        res = "NM"
    else:
        res = "TM"
    
    data = {
        "NB": ("🧬 [2B-NB] 正经帅气型 (The Narcissist)", "如果帅是一种罪，我可能已经死刑起步了。", "你是装杯界的珠穆朗玛。即使在量硬件时也要Excel建模。你的生活是一场自带滤镜的真人秀，体面是你最后的倔强。算法显示：你装得非常成功。"),
        "SB": ("🤡 [2B-SB] 抽象帅气型 (The Stylized Buffoon)", "上帝给了我一副好皮囊，但我决定拿它来整活。", "社交圈的氧气泵。颜值上限极高，智商下限深不可测。只要不说话就是男神，一张嘴大家就想报警。你成功地把英俊和脑瘫结合得天衣无缝。"),
        "NM": ("🧐 [2B-NM] 正经恶心型 (The Academic Monster)", "我不是变态，我只是对世界有着极度严谨的生理好奇。", "学术型变态。你看起来像个教授，其实是个怪谈。喜欢用科学逻辑去解释猥琐行为，看人的眼神像在看生理解剖标本。你不仅恶心，还恶心得很有文化。"),
        "TM": ("☢️ [2B-TM] 抽象恶心型 (The Total Mutant)", "人类进化的时候，我可能在旁边忙着钻木取火。", "纯粹的“混沌恶”。你完全抛弃了碳基生物的体面。你的每一个点子都让舍友想连夜搬出宿舍，你的存在就是对人类文明的挑衅。建议物理隔离。")
    }
    
    title, quote, detail = data[res]
    st.markdown(f"""
    <div class="result-card">
        <h2 style='color: #00ff00; text-align: left;'>{title}</h2>
        <h3 style='color: #ffff00; font-style: italic; text-align: left;'>“{quote}”</h3>
        <hr style='border: 1px solid #444;'>
        <p style='font-size: 1.2rem; line-height: 1.6;'><b>深度本性分析：</b>{detail}</p>
        <p style='color: #00ffff; font-size: 0.9rem; margin-top: 20px;'>
            维度校验：秩序/混沌({zx}) | 魅力/异质({se})
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("不服？洗心革面重新开始"):
        # 清空状态并返回
        for key in ['zx_axis', 'se_axis', 'current_q']:
            st.session_state[key] = 0
        st.session_state.page = 'intro'
        st.rerun()