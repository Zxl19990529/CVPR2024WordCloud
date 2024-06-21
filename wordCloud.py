import os
import shutil
import matplotlib.pyplot as plt
from wordcloud import WordCloud  # 词云库
from wordcloud import STOPWORDS




if __name__ == '__main__':
    f=open('allPapers.txt','r')
    lines = f.readlines()
    titles = []
    index = 0
    step=4
    for i in range(len(lines)//step):
        titles.append(lines[i*step].strip())
    print(titles)
    all_words = ','.join(titles)

    stopwords = set(STOPWORDS)  # 用一个集合set存储英文停用词
    stopwords.add("Image")       # 可在原有停用词基础上自定义增加所需的词语
    stopwords.add('Learning')
    stopwords.add('via')
    # 带入到WordCloud实例中的stopwords参数即可。
    # wc = WordCloud(width=600, height=400, background_color='white',
    #            max_font_size=45,stopwords=stopwords, max_words=4000)
    # 2.创建WordCloud实例,设置词云图宽高(最终以矩形显示)、背景颜色(默认黑色)和最大显示字数
    wc = WordCloud(width=1920, height=1080, background_color="white", max_words=200,stopwords=stopwords)
    # 3.根据读取的英文文本，先分词再生成词云图
    wc.generate(all_words)
    # 4.使用matplotlib绘图
    plt.imshow(wc)
    plt.axis("off") # 取消坐标系
    plt.show()      # 在IDE中显示图片
    # 5.将生成的词云图保存在本地
    wc.to_file('wordcloud.png')
