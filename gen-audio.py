import asyncio
import edge_tts
import os

VOICE = "zh-CN-XiaoxiaoNeural"  # 自然女声，更稳定
OUT_DIR = r"C:\Users\赵梓维\Desktop\produc1\audio"
os.makedirs(OUT_DIR, exist_ok=True)

lines = [
    "大家好，我是小招同学。一款专为在校大学生设计的AI理财陪伴搭子。",
    "当一个大学生说我又月光了，小招不会说教。而是用3分钟快速体检，帮你找到钱去哪了。",
    "注意看，每次只问一个问题。用户回复后才进入下一问。像朋友聊天一样自然。",
    "四步完成后，直接在对话流中输出结构化体检报告。健康分、同龄人排名、亮点、隐藏黑洞、行动建议。整个过程不需要任何表格或表单。",
    "当用户产生冲动消费时，小招会用行为经济学做出温柔的拦截。打车30元，换算成3顿食堂饭、2杯奶茶。",
    "更重要的是，省下的钱自动转入毕业旅行基金。每一次拦截都是正向反馈，把枯燥的省钱变成一个打怪升级的游戏。",
    "当室友晒收益，用户FOMO上头时，小招启动FOMO粉碎机。不罗列复杂研报，而是用伙食费还够吗做极端回撤模拟。",
    "跌20%少半个月饭钱，跌50%只能吃泡面。最后给出低门槛替代方案，附上风险免责声明。银行级合规不是口号。",
    "每周日的赛博把脉周报，用恩格尔系数、拦截次数、储蓄进度，让用户对自己的财务状态一目了然。",
    "坚持了5天没喝奶茶，跑赢全国70%大学生。用同龄人排名制造良性激励，让财务自律变成可以晒的社交货币。",
    "小招同学，用AI把行为经济学翻译成校园日常，用搭子的温度替代工具的冰冷。",
    "从认知唤醒到行为养成，从消费觉察到定投转化。这是招商银行面向大学生群体的金融启蒙入口，也是未来三十年零售客群的第一触点。",
    "扫码体验。谢谢各位评委老师。招商银行数字金融训练营，AI产品赛道，赵梓维。",
]

async def gen(i, text):
    path = os.path.join(OUT_DIR, f"{i:02d}.mp3")
    tts = edge_tts.Communicate(text, VOICE)
    await tts.save(path)
    print(f"  {i:02d}.mp3 done")
    await asyncio.sleep(2)  # avoid rate limit

async def main():
    print(f"Generating {len(lines)} audio clips...")
    for i, t in enumerate(lines, 1):
        await gen(i, t)
    print(f"\nAll done! Files: {OUT_DIR}")

asyncio.run(main())
