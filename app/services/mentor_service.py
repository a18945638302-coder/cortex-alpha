import os

MENTOR_PROMPTS = {
    "buffett": "你在用情绪做决策。巴菲特的核心问题只有一个：你当初买入的长期逻辑，今天是否发生了实质变化？如果没有，这次操作更像是痛苦的逃离，而非理性判断。建议今晚重读买入笔记。",
    "livermore": "止损纪律是交易员的生命线。你在亏损时才动手，说明入场时没有设置预定止损位。铁律只有一条：在买入的同时就决定止损点，而不是等疼了再跑。",
    "quant": "数据分析：此次操作期望值为负。你在情绪峰值操作，历史数据显示此类状态下胜率仅33%。建议设置机械止损线，彻底排除情绪变量。"
}

async def get_ai_feedback(content: str, style: str) -> str:
    # 暂时返回模拟数据，后续接入真实 AI
    return MENTOR_PROMPTS.get(style, MENTOR_PROMPTS["buffett"])