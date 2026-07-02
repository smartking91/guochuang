import datetime as dt

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


st.set_page_config(
    page_title="舆擎｜企业舆情AI风控SaaS",
    page_icon="YQ",
    layout="wide",
    initial_sidebar_state="expanded",
)

NOW = dt.datetime(2026, 7, 2, 15, 30)

COLORS = {
    "bg": "#06111f",
    "panel": "#0c1b2e",
    "panel2": "#10243d",
    "text": "#f8fafc",
    "muted": "#b7c7dc",
    "cyan": "#22d3ee",
    "blue": "#60a5fa",
    "green": "#22c55e",
    "yellow": "#facc15",
    "orange": "#f97316",
    "red": "#ef4444",
    "violet": "#a78bfa",
}


st.markdown(
    f"""
    <style>
    .stApp {{
        background:
            radial-gradient(circle at 12% 0%, rgba(34, 211, 238, .14), transparent 28%),
            radial-gradient(circle at 86% 2%, rgba(250, 204, 21, .11), transparent 30%),
            linear-gradient(180deg, {COLORS["bg"]} 0%, #081426 100%);
        color: {COLORS["text"]};
    }}
    header, footer, #MainMenu, .stDeployButton {{ visibility: hidden; }}
    .stApp, .stApp p, .stApp li, .stApp span, .stApp label,
    .stApp div[data-testid="stMarkdownContainer"] {{
        color: {COLORS["text"]} !important;
    }}
    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #050d19 0%, #0a1830 100%);
        border-right: 1px solid rgba(96, 165, 250, .35);
    }}
    section[data-testid="stSidebar"] * {{ color: {COLORS["text"]} !important; }}
    section[data-testid="stSidebar"] div[role="radiogroup"] label {{
        background: rgba(15, 23, 42, .45);
        border-radius: 8px;
        padding: 7px 9px;
        margin-bottom: 5px;
    }}
    h1, h2, h3 {{
        color: {COLORS["text"]} !important;
        letter-spacing: 0;
    }}
    div[data-testid="stMetric"] {{
        background: linear-gradient(145deg, rgba(16, 36, 61, .98), rgba(8, 20, 38, .94));
        border: 1px solid rgba(96, 165, 250, .34);
        border-radius: 8px;
        padding: 16px 18px 13px;
        box-shadow: 0 12px 28px rgba(0, 0, 0, .24), inset 0 0 20px rgba(34, 211, 238, .07);
    }}
    div[data-testid="stMetricLabel"], div[data-testid="stMetricDelta"] {{
        color: #c7d2fe !important;
        font-weight: 760 !important;
    }}
    div[data-testid="stMetricValue"],
    div[data-testid="stMetricValue"] div,
    div[data-testid="stMetricValue"] span {{
        color: #facc15 !important;
        -webkit-text-fill-color: #facc15 !important;
        font-weight: 900 !important;
        text-shadow: 0 0 15px rgba(250, 204, 21, .36);
    }}
    .topbar {{
        padding: 18px 20px;
        border-radius: 8px;
        background: linear-gradient(115deg, rgba(16, 36, 61, .96), rgba(7, 17, 31, .82));
        border: 1px solid rgba(96, 165, 250, .28);
        margin-bottom: 16px;
    }}
    .brand {{
        color: #facc15;
        font-size: 30px;
        font-weight: 900;
        margin-bottom: 5px;
    }}
    .subtle {{
        color: #cbd5e1 !important;
        font-size: 14px;
        line-height: 1.65;
    }}
    .panel {{
        background: linear-gradient(145deg, rgba(16, 36, 61, .94), rgba(10, 24, 48, .9));
        border: 1px solid rgba(148, 163, 184, .20);
        border-radius: 8px;
        padding: 17px;
        min-height: 116px;
        box-shadow: 0 12px 28px rgba(0, 0, 0, .2);
    }}
    .panel-title {{
        color: #67e8f9;
        font-size: 16px;
        font-weight: 850;
        margin-bottom: 8px;
    }}
    .panel-body {{
        color: #d7e5f7;
        font-size: 14px;
        line-height: 1.65;
    }}
    .chip {{
        display: inline-block;
        border: 1px solid rgba(34, 211, 238, .46);
        color: #e0f2fe !important;
        background: rgba(15, 23, 42, .52);
        padding: 6px 10px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 800;
        margin: 8px 7px 0 0;
    }}
    .risk-l2, .risk-l3, .risk-l4 {{
        display: inline-block;
        min-width: 62px;
        text-align: center;
        border-radius: 999px;
        padding: 5px 12px;
        color: white;
        font-weight: 850;
    }}
    .risk-l2 {{ background: #22c55e; }}
    .risk-l3 {{ background: #f97316; }}
    .risk-l4 {{ background: #ef4444; box-shadow: 0 0 15px rgba(239, 68, 68, .45); }}
    .event {{
        border-left: 3px solid #22d3ee;
        background: rgba(15, 23, 42, .9);
        padding: 11px 14px;
        margin-bottom: 10px;
        border-radius: 6px;
        line-height: 1.58;
    }}
    .event strong {{ color: #facc15; }}
    div[data-testid="stDataFrame"] {{
        background: rgba(15, 23, 42, .96) !important;
        border: 1px solid rgba(148, 163, 184, .22);
        border-radius: 8px;
    }}
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div {{
        background-color: rgba(15, 23, 42, .96) !important;
        border-color: rgba(34, 211, 238, .35) !important;
        color: {COLORS["text"]} !important;
    }}
    div[data-baseweb="select"] span,
    div[data-baseweb="input"] input {{
        color: {COLORS["text"]} !important;
        -webkit-text-fill-color: {COLORS["text"]} !important;
    }}
    button[kind="primary"] {{
        background: linear-gradient(90deg, #0ea5e9 0%, #facc15 100%) !important;
        border: 0 !important;
        color: #06121f !important;
        font-weight: 850 !important;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


def apply_theme(fig, height=390):
    fig.update_layout(
        template="plotly_dark",
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#f8fafc", size=13),
        margin=dict(l=20, r=20, t=52, b=36),
        legend=dict(font=dict(color="#f8fafc"), bgcolor="rgba(0,0,0,0)"),
    )
    fig.update_xaxes(gridcolor="rgba(148, 163, 184, .14)", zerolinecolor="rgba(148, 163, 184, .18)")
    fig.update_yaxes(gridcolor="rgba(148, 163, 184, .14)", zerolinecolor="rgba(148, 163, 184, .18)")
    return fig


def panel(title, body):
    st.markdown(
        f'<div class="panel"><div class="panel-title">{title}</div><div class="panel-body">{body}</div></div>',
        unsafe_allow_html=True,
    )


def badge(level):
    cls = {"L2": "risk-l2", "L3": "risk-l3", "L4": "risk-l4"}[level]
    label = {"L2": "L2 关注", "L3": "L3 预警", "L4": "L4 警报"}[level]
    return f'<span class="{cls}">{label}</span>'


def event_line(time_label, title, body):
    st.markdown(
        f'<div class="event"><strong>{time_label}｜{title}</strong><br>{body}</div>',
        unsafe_allow_html=True,
    )


ACCOUNTS = {
    "星澜智造｜融资尽调版": {
        "industry": "高端装备制造",
        "plan": "企业专业版",
        "scene": "融资/授信/招投标",
        "risk": 47,
        "level": "L4",
        "engine": "C-RATE",
        "summary": "二级供应商新增涉诉信息，融资尽调窗口期内关联方风险快速升高。",
    },
    "禾木清饮｜品牌声誉版": {
        "industry": "消费品牌",
        "plan": "成长企业版",
        "scene": "品牌声誉/危机公关",
        "risk": 56,
        "level": "L3",
        "engine": "Anom-Graph",
        "summary": "新品配料安全争议在短视频平台集中扩散，疑似非自然传播。",
    },
    "云阶科技｜竞对洞察版": {
        "industry": "工程服务",
        "plan": "企业专业版",
        "scene": "竞品动态/投标决策",
        "risk": 59,
        "level": "L3",
        "engine": "F-MOSAIC",
        "summary": "竞品价格带下探，并伴随区域子公司工商变更与招标信号。",
    },
}


alerts = pd.DataFrame(
    [
        ["15:18", "星澜智造", "关联方涉诉传导", "C-RATE", "L4", 47, "融资尽调窗口期，供应链关联风险触发红色警报"],
        ["15:02", "禾木清饮", "异常传播聚类", "Anom-Graph", "L3", 56, "短视频评论区出现批量相似质疑语句"],
        ["14:47", "云阶科技", "竞品降价偷袭", "F-MOSAIC", "L3", 59, "竞品报价指数7日内下降18%"],
        ["14:36", "星澜智造", "政策压力上升", "C-RATE", "L2", 73, "行业监管关键词热度升高"],
        ["14:21", "禾木清饮", "高赞评论转负", "Anom-Graph", "L2", 76, "头部评论情绪出现轻度负偏"],
    ],
    columns=["时间", "企业", "风险事件", "引擎", "等级", "评分", "摘要"],
)

dates = pd.date_range(end=NOW, periods=14, freq="D")
trend_df = pd.DataFrame(
    {
        "日期": list(dates) * 3,
        "风险热度": np.r_[
            np.linspace(34, 81, 14) + np.sin(np.arange(14)) * 4,
            np.linspace(28, 61, 14) + np.cos(np.arange(14)) * 3,
            np.linspace(39, 69, 14) + np.sin(np.arange(14) / 2) * 5,
        ],
        "场景": ["融资投标"] * 14 + ["品牌声誉"] * 14 + ["竞品动态"] * 14,
    }
)

source_df = pd.DataFrame(
    [
        ["公开新闻", 1286, 92, "已接入"],
        ["短视频评论", 48277, 76, "已接入"],
        ["工商司法", 832, 95, "已接入"],
        ["招投标公告", 417, 88, "已接入"],
        ["竞品价格", 6294, 81, "监测中"],
        ["企业授权数据", 15620, 90, "试点中"],
    ],
    columns=["数据源", "今日采集量", "可信度", "状态"],
)


st.sidebar.title("舆擎 SaaS")
st.sidebar.caption("企业舆情AI分级预警平台")
st.sidebar.markdown("---")
account_name = st.sidebar.selectbox("当前企业工作台", list(ACCOUNTS.keys()))
account = ACCOUNTS[account_name]
st.sidebar.markdown(
    f"""
    <div class="panel">
      <div class="panel-title">{account_name}</div>
      <div class="panel-body">
        行业：{account["industry"]}<br>
        套餐：{account["plan"]}<br>
        场景：{account["scene"]}
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "功能导航",
    [
        "经营风险总览",
        "实时监测中心",
        "三大AI引擎",
        "分级预警中心",
        "处置方案报告",
        "客户与商业验证",
    ],
)
st.sidebar.markdown("---")
st.sidebar.info("企业级SaaS工作台：覆盖监测、研判、预警、处置和复盘全流程，支撑企业经营风险的日常管理。")


st.markdown(
    f"""
    <div class="topbar">
      <div class="brand">舆擎｜企业舆情AI分级预警SaaS平台</div>
      <div class="subtle">
        当前租户：{account_name}　｜　更新时间：{NOW.strftime("%Y-%m-%d %H:%M")}　｜　
        核心引擎：{account["engine"]}　｜　当前风险：{account["summary"]}
      </div>
      <span class="chip">金融场景化NLP</span>
      <span class="chip">关系图谱穿透</span>
      <span class="chip">三级动态预警</span>
      <span class="chip">10分钟处置方案</span>
    </div>
    """,
    unsafe_allow_html=True,
)


if page == "经营风险总览":
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("今日监测声量", "72,726", "+18.4%")
    c2.metric("有效风险信号", "1,426", "+9.7%")
    c3.metric("当前综合评分", str(account["risk"]), "低分优先处置")
    c4.metric("高优先级预警", "3", "L4 1条")

    left, right = st.columns([1.1, .9])
    with left:
        fig = px.area(
            trend_df,
            x="日期",
            y="风险热度",
            color="场景",
            title="近14日经营风险热度",
            color_discrete_sequence=[COLORS["red"], COLORS["orange"], COLORS["blue"]],
        )
        st.plotly_chart(apply_theme(fig, 410), use_container_width=True)
    with right:
        donut_df = pd.DataFrame(
            {"风险类型": ["关联方风险", "声誉传播", "竞品动态", "政策环境"], "占比": [36, 29, 23, 12]}
        )
        fig = px.pie(
            donut_df,
            names="风险类型",
            values="占比",
            hole=.58,
            title="风险构成",
            color_discrete_sequence=[COLORS["red"], COLORS["orange"], COLORS["blue"], COLORS["green"]],
        )
        fig.update_traces(textinfo="label+percent", textposition="outside")
        st.plotly_chart(apply_theme(fig, 410), use_container_width=True)

    st.markdown("### 租户运行状态")
    a, b, c = st.columns(3)
    with a:
        panel("产品交付状态", "企业工作台、风险监测、AI引擎、预警中心和处置报告均已打通，适合展示真实SaaS交付形态。")
    with b:
        panel("核心价值", "从信息监测升级为经营决策支持，让企业在融资、声誉和竞对场景中提前处理风险。")
    with c:
        panel("国创亮点", "平台把PPT中的三大引擎、三级预警、闭环处置变成可操作后台，增强项目落地可信度。")


elif page == "实时监测中心":
    st.title("实时监测中心")
    st.markdown("多源数据接入状态、风险声量和可信度展示，帮助企业持续掌握经营风险变化。")

    st.dataframe(source_df, use_container_width=True, hide_index=True)

    left, right = st.columns([.95, 1.05])
    with left:
        fig = px.bar(
            source_df,
            x="数据源",
            y="今日采集量",
            color="可信度",
            text="今日采集量",
            title="今日多源数据采集",
            color_continuous_scale=["#0f172a", COLORS["cyan"], COLORS["yellow"]],
        )
        fig.update_layout(coloraxis_showscale=False)
        st.plotly_chart(apply_theme(fig, 400), use_container_width=True)
    with right:
        keyword_df = pd.DataFrame(
            [
                ["供应商涉诉", 96, "融资投标"],
                ["配料质疑", 88, "品牌声誉"],
                ["低价套餐", 83, "竞品动态"],
                ["招标短名单", 79, "竞品动态"],
                ["现金流压力", 74, "融资投标"],
                ["集中差评", 71, "品牌声誉"],
            ],
            columns=["关键词", "热度", "场景"],
        )
        fig = px.bar(
            keyword_df,
            x="热度",
            y="关键词",
            color="场景",
            orientation="h",
            title="高频风险关键词",
            color_discrete_sequence=[COLORS["red"], COLORS["orange"], COLORS["blue"]],
        )
        st.plotly_chart(apply_theme(fig, 400), use_container_width=True)

    st.markdown("### 最新信号流")
    event_line("15:18", "供应商涉诉信号入库", "公开司法信息显示二级供应商新增被执行记录，系统已映射至融资尽调风险链。")
    event_line("15:02", "异常传播聚类", "短视频评论区出现批量相似质疑表达，Anom-Graph识别为传播异常。")
    event_line("14:47", "竞品价格带下探", "核心竞品价格指数连续7天下降，F-MOSAIC触发竞品动态预警。")


elif page == "三大AI引擎":
    st.title("三大AI引擎")
    engine_df = pd.DataFrame(
        [
            ["C-RATE", "经营风险预警", "关联方风险40% / 偿债能力25% / 供应链稳定20% / 行业政策15%", "融资尽调、授信审查"],
            ["Anom-Graph", "品牌声誉监测", "传播异常35% / 信源可信25% / 情绪突变20% / 关联账号20%", "声誉危机、公关澄清"],
            ["F-MOSAIC", "竞对动态洞察", "价格变动30% / 工商变更25% / 招投标25% / 舆情情绪20%", "投标决策、市场竞争"],
        ],
        columns=["引擎", "业务模块", "权重配置", "应用场景"],
    )
    st.dataframe(engine_df, use_container_width=True, hide_index=True)

    selected_engine = st.selectbox("选择引擎查看分析", engine_df["引擎"].tolist(), index=engine_df["引擎"].tolist().index(account["engine"]))
    dimensions = {
        "C-RATE": {"关联方风险": 42, "偿债能力": 58, "供应链稳定": 46, "行业政策": 71},
        "Anom-Graph": {"传播异常": 48, "信源可信": 63, "情绪突变": 51, "关联账号": 57},
        "F-MOSAIC": {"价格变动": 44, "工商变更": 61, "招投标": 55, "舆情情绪": 67},
    }[selected_engine]

    left, right = st.columns([.9, 1.1])
    with left:
        radar_df = pd.DataFrame({"维度": list(dimensions.keys()), "得分": list(dimensions.values())})
        fig = px.line_polar(
            radar_df,
            r="得分",
            theta="维度",
            line_close=True,
            range_r=[0, 100],
            title=f"{selected_engine}维度评分",
        )
        fig.update_traces(fill="toself", fillcolor="rgba(34, 211, 238, .25)", line_color=COLORS["cyan"])
        st.plotly_chart(apply_theme(fig, 430), use_container_width=True)
    with right:
        if selected_engine == "C-RATE":
            fig = go.Figure()
            edge_x = [0, 1, None, 1, 2, None, 1, 1.7, None, 2, 2.8]
            edge_y = [1, 1.55, None, 1.55, 1, None, 1.55, 2.25, None, 1, .35]
            node_x = [0, 1, 2, 1.7, 2.8]
            node_y = [1, 1.55, 1, 2.25, .35]
            names = ["本企业", "一级供应商", "涉诉主体", "投资方", "核心客户"]
            fig.add_trace(go.Scatter(x=edge_x, y=edge_y, mode="lines", line=dict(color="rgba(148,163,184,.55)", width=2), hoverinfo="skip"))
            fig.add_trace(go.Scatter(x=node_x, y=node_y, mode="markers+text", text=names, textposition="bottom center", marker=dict(size=[30, 24, 30, 22, 22], color=[COLORS["cyan"], COLORS["blue"], COLORS["red"], COLORS["green"], COLORS["yellow"]], line=dict(color="#fff", width=1))))
            fig.update_layout(title="关联风险图谱", xaxis=dict(visible=False), yaxis=dict(visible=False), showlegend=False)
        elif selected_engine == "Anom-Graph":
            hours = pd.date_range(end=NOW, periods=10, freq="20min")
            spread = pd.DataFrame({"时间": hours, "自然讨论": [8, 9, 10, 13, 15, 18, 20, 23, 25, 28], "异常传播": [2, 3, 4, 8, 17, 31, 48, 68, 89, 96]})
            fig = px.line(spread, x="时间", y=["自然讨论", "异常传播"], markers=True, title="异常传播曲线", color_discrete_sequence=[COLORS["green"], COLORS["red"]])
        else:
            days = pd.date_range(end=NOW, periods=9, freq="D")
            price = pd.DataFrame({"日期": days, "我方报价指数": [100, 100, 99, 101, 100, 100, 99, 100, 100], "竞品报价指数": [100, 99, 96, 94, 90, 86, 84, 83, 82]})
            fig = px.line(price, x="日期", y=["我方报价指数", "竞品报价指数"], markers=True, title="竞品价格异动", color_discrete_sequence=[COLORS["cyan"], COLORS["orange"]])
        st.plotly_chart(apply_theme(fig, 430), use_container_width=True)

    a, b, c = st.columns(3)
    with a:
        panel("准确率提升", "金融场景语料微调后，情感分类准确率从通用NLP的78.0%提升至92.3%。")
    with b:
        panel("信号识别提升", "有效风险信号识别率从40.0%提升至85.0%，减少无效信息淹没。")
    with c:
        panel("可解释输出", "每次预警保留权重、触发信号、风险路径和处置建议，便于企业复核。")


elif page == "分级预警中心":
    st.title("分级预警中心")
    st.markdown("SaaS后台的核心工作台：风险事件按优先级进入队列，运营负责人可以直接查看证据、判级和下一步动作。")

    display_alerts = alerts.copy()
    display_alerts["等级"] = display_alerts["等级"].apply(badge)
    st.markdown(display_alerts.to_html(escape=False, index=False), unsafe_allow_html=True)

    st.markdown("### 分级规则")
    cols = st.columns(3)
    with cols[0]:
        panel("L2 关注", "评分60-80或偏离超过1.5σ。系统推送风险信息、关联走势与政策匹配参考。")
    with cols[1]:
        panel("L3 预警", "评分低于60且单维低于45。系统生成归因分析报告、话术模板与分阶段处置路径。")
    with cols[2]:
        panel("L4 警报", "评分低于60且负面舆情超过40%。10分钟内直达企业核心负责人并启动跟进。")


elif page == "处置方案报告":
    st.title("处置方案报告")
    st.markdown("面向真实客户交付的报告页：给结论、给证据、给责任人、给时间窗口。")

    if st.button("生成当前企业处置报告", type="primary", use_container_width=True):
        st.session_state["report_ready"] = True
    ready = st.session_state.get("report_ready", False)

    if ready:
        st.markdown(
            f"""
            <div class="panel">
              <div class="panel-title">{account_name}｜{badge(account["level"])}｜{account["engine"]}处置报告</div>
              <div class="panel-body">{account["summary"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        report_rows = pd.DataFrame(
            [
                ["0-10分钟", "确认触发证据与责任人", "项目负责人 / 法务 / 客服主管", "完成"],
                ["10-30分钟", "形成统一对外口径与内部说明", "业务负责人 / 市场负责人", "进行中"],
                ["30-120分钟", "提交补充材料或平台申诉", "核心管理层 / 外部合作方", "待启动"],
                ["当日闭环", "沉淀风险标签并更新阈值", "运营负责人 / 算法负责人", "待启动"],
            ],
            columns=["处置窗口", "动作", "责任角色", "状态"],
        )
        st.dataframe(report_rows, use_container_width=True, hide_index=True)

        st.markdown("### 建议话术")
        st.code(
            "我们已完成该风险事件的初步核查，并同步启动内部复核与外部沟通流程。\n"
            "当前证据显示，风险集中在可解释、可隔离的局部环节，企业经营主体基本面未发生重大变化。\n"
            "后续我们将在30分钟内补充证明材料，并持续同步处置进展。",
            language="text",
        )
    else:
        st.info("点击按钮生成当前租户的处置报告。")


elif page == "客户与商业验证":
    st.title("客户与商业验证")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("合作企业", "5家")
    c2.metric("标杆试点", "20家")
    c3.metric("短视频矩阵", "10万+粉")
    c4.metric("续签目标", "90%")

    pricing = pd.DataFrame(
        [
            ["基础版", "1.5万元/年", "单企业基础监测、L2风险提示、月度报告"],
            ["专业版", "3-5万元/年", "三大引擎、L3/L4预警、处置方案、多人协作"],
            ["API与定制报告", "0.5-5万元/份", "金融机构、园区、服务商定制接入"],
        ],
        columns=["产品包", "价格", "权益"],
    )
    st.dataframe(pricing, use_container_width=True, hide_index=True)

    left, right = st.columns(2)
    with left:
        funnel = pd.DataFrame({"阶段": ["短视频/园区触达", "免费试用", "试点验证", "付费签约", "续签复购"], "企业数": [420, 86, 20, 5, 4]})
        fig = px.funnel(funnel, x="企业数", y="阶段", title="获客与转化漏斗", color_discrete_sequence=[COLORS["cyan"]])
        st.plotly_chart(apply_theme(fig, 400), use_container_width=True)
    with right:
        competitor = pd.DataFrame(
            [
                ["企查查", "商业查询", "仅出报告，无处置方案", "10万+"],
                ["慧科讯业", "全媒体监测", "仅给数据，不做风险预判", "3-10万+"],
                ["舆擎", "中小企业经营风险AI预警", "预警+归因+处置闭环", "1.5万元起"],
            ],
            columns=["产品", "定位", "差异", "年成本"],
        )
        st.dataframe(competitor, use_container_width=True, hide_index=True)
