import asyncio
import os
import sys

# 将项目根目录加入 path，以便导入 utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from utils.voice import generate_voice_for_scripts

# 语音配置
VOICE = "zh-CN-XiaoxiaoNeural"
OUTPUT_DIR = "media/sunzi/lesson03/voice"

# 第三课解说词
scripts = {
    # 封面
    "01_cover": "大家好！欢迎回到《我是小小谋略家》。今天是孙子兵法第三课。我要问你一个问题：你觉得，打仗最厉害的人是谁？是打赢了一百次的人吗？",
    
    # 真正的赢家
    "02_best_winner": "孙武爷爷说：“百战百胜，非善之善者也。”意思是，打一百次赢一百次，虽然很厉害，但还不是最棒的。那什么才是最棒的呢？“不战而屈人之兵！”不用打架，就能让对手认输，这才是真正的绝世高手！",
    
    # 解决问题的四个等级
    "03_four_levels": "解决问题有四个等级。第一等叫“伐谋”，用脑子想办法化解冲突；第二等叫“伐交”，用嘴巴沟通，或者找朋友帮忙；第三等叫“伐兵”，真的动手打起来，这就容易受伤了；最差的一等叫“攻城”，硬碰硬，大家都头破血流，这是笨蛋才干的事！",
    
    # 胜利的数学题
    "04_know_yourself": "那怎么才能做到“不战而胜”呢？孙武爷爷教了我们一句最有名的咒语：“知彼知己，百战不殆。”意思是：既了解对手，又了解自己，那你遇到什么困难都不会有危险。如果你只了解自己，不了解对手，那一半赢一半输；如果你谁都不了解，那就输定啦！",
    
    # 结尾互动
    "05_ending": "最后，小武给你出一个思考题：如果同学给你起难听的外号，你会怎么做？A：骂回去，和他打一架！B：生闷气，回家哭鼻子。C：想办法让他自己觉得没意思，主动停止。想一想，哪个才是“不战而胜”的智慧呢？在评论区告诉小武吧！我们下节课见！"
}

if __name__ == "__main__":
    asyncio.run(generate_voice_for_scripts(scripts, OUTPUT_DIR, VOICE))

