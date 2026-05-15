import asyncio
import edge_tts
import os

VOICE = "zh-CN-XiaoxiaoNeural"
OUT_DIR = r"C:\Users\赵梓维\Desktop\produc1\audio"

# 合并3段为1段长配音，覆盖约1分钟的体检录屏
text = (
    "当一个大学生说我又月光了，小招不会说教，而是用三分钟快速体检帮你找到钱去哪了。"
    "注意看，每次只问一个问题。第一步问月自由支配金额，第二步问储蓄习惯，第三步问理财经验，第四步问存钱目标。"
    "用户回复后才进入下一问，像朋友聊天一样自然，完全没有填表的压迫感。"
    "四步完成后，小招直接在对话流中输出结构化体检报告。"
    "给出零到一百的健康分，同龄人排名，告诉你亮点在哪，隐藏黑洞是什么，以及马上可以做的行动建议。"
    "整个过程不需要任何表格、按钮或者表单，全在自然对话中完成。"
)

async def main():
    path = os.path.join(OUT_DIR, "checkup.mp3")
    tts = edge_tts.Communicate(text, VOICE, rate="-5%")  # 稍慢，填满1分钟
    await tts.save(path)
    print(f"checkup.mp3 done -> {path}")

asyncio.run(main())
