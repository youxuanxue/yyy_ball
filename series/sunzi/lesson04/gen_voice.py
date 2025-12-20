import asyncio
import os
import sys

# 将项目根目录加入 path，以便导入 utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from utils.voice import generate_voice_for_scripts

# 语音配置
VOICE = "zh-CN-XiaoxiaoNeural"
OUTPUT_DIR = "media/sunzi/lesson04/voice"

# 第四课解说词
scripts = {
    # 封面
    "01_cover": "大家好！欢迎回到《我是小小谋略家》。今天是第四课。大家都想当赢家，但你知道怎么做才能“永远不输”吗？孙武爷爷有一个超级秘密！",
    
    # 先为不可胜
    "02_invincible": "孙武爷爷说：“善战者，先为不可胜”。意思是，打仗前，先把自己练得棒棒的，像穿了钢铁侠的盔甲一样，谁也打不倒你。只要我不输，我就已经立于不败之地啦！",
    
    # 在己 vs 在敌
    "03_control": "记住这句话：“不可胜在己，可胜在敌。” 意思是：我不被你打败，这事儿归我管；但我能不能打赢你，那得看你犯不犯错。就像考试，我能保证自己复习好，但不能保证考卷出得简不简单。",
    
    # 赢家 vs 输家
    "04_winner_mindset": "聪明的将军，都是先在家里算好了肯定能赢，才出门去打仗；而笨蛋将军，是什么都没准备好，冲上去跟人家打，心里祈祷“老天保佑让我赢吧”。你是哪一种呢？",
    
    # 结尾互动
    "05_ending": "所以，真正的胜利，是在打仗之前就决定的！最后小武考考你：明天要考试了，哪种做法是“先为不可胜”？A：找个学霸，考试时偷看他的答案。B：每天认真复习，把错题都弄懂。C：祈祷老师生病，明天不用考试。快在评论区告诉小武吧！我们下节课见！"
}

if __name__ == "__main__":
    asyncio.run(generate_voice_for_scripts(scripts, OUTPUT_DIR, VOICE))

