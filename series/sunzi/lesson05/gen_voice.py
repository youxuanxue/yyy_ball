import asyncio
import os
import sys

# 将项目根目录加入 path，以便导入 utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from utils.voice import generate_voice_for_scripts

# 语音配置
VOICE = "zh-CN-XiaoxiaoNeural"
OUTPUT_DIR = "media/sunzi/lesson05/voice"

# 第五课解说词
scripts = {
    # 封面
    "01_cover": "大家好！欢迎回到《我是小小谋略家》。今天是第五课。如果说第四课讲的是怎么练成“金刚不坏之身”，那今天这一课，就是教你怎么变成“战场上的魔术师”！",
    
    # 橘子与橙汁
    "02_orange": "孙武爷爷说，“形”和“势”是不一样的。“形”就像上帝给你一个橘子，它就在那儿，不会变。而“势”，就是你动脑筋，把它榨成一杯美味的橙汁。只有把原本静止的东西用好、动起来，才能发挥出巨大的威力！",
    
    # 叠被子
    "03_quilts": "怎么指挥千军万马呢？孙武爷爷教了一招：“治众如治寡”。意思是，管很多人，要像管一个人一样简单。秘密就是——像叠被子一样！虽然叠被子不能打仗，但如果大家都能把被子叠得一模一样，那行动起来就能整整齐齐，像一个人一样听指挥啦！",
    
    # 战场魔术师
    "04_magic": "打仗就像变魔术。一方面，我们要光明正大地排兵布阵，这叫“正”；另一方面，我们要像变魔术一样，突然出奇招，给对手一个措手不及，这叫“奇”。只有“奇正相生”，才能变幻无穷，把对手绕晕！",
    
    # 结尾互动
    "05_ending": "所以，不仅要身体强壮，还要脑子灵活，学会造势，才能成为真正的常胜将军！最后小武考考你：如果你是班长，想让全班同学都听指挥，应该怎么做？A：每个人想干嘛就干嘛，开心就好。B：制定统一的规则，大家都按规则做。C：只管自己的好朋友，别人不管。快在评论区告诉小武吧！我们下节课见！"
}

if __name__ == "__main__":
    asyncio.run(generate_voice_for_scripts(scripts, OUTPUT_DIR, VOICE))

