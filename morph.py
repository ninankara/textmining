import jpype
import nltk
from konlpy.tag import Okt

from collections import Counter
from matplotlib import pylab
from matplotlib import font_manager, rc
from gensim.models import word2vec

pathJVM = "C:/Program Files/Java/jre1.8.0_181/bin/server/jvm.dll" #change into your jvm location
#pathJVM = "/Library/Java/JavaVirtualMachines/jdk-10.0.1.jdk/Contents/Home/lib/server/libjvm.dylib"
t = Okt(pathJVM)

newsraw = open("/joongang.txt","r", encoding="utf8") #change into your filelocation
newsdec = newsraw.read()

#POS Tagging / Morphology
newsmorph = t.morphs(newsdec)
newstag = t.pos(newsdec)
print (len(newstag))


ko = nltk.Text(newsmorph,name="joongang news")
print (len(set(ko.tokens)))

pylab.show = lambda: pylab.savefig('frequentwords.png')
# font_loc = '/Library/Fonts/AppleGothic.ttf'
# font_name = font_manager.FontProperties(fname=font_loc).get_name()
# rc('font',family=font_name)
#ko.plot(50)

#Word2Vec
newsw2v = word2vec.Word2Vec(newstag,sorted_vocab=1)
newsw2v.init_sims(replace=True)
newsw2v.save('joongang_w2v.model')

#frequent word
finance = newsw2v.most_similar(u'금융',topn=10)

for i in finance:
    print (i[0])
    print (i[1])

"""#create word dictionary
finance_w = [u'금융']
for item in finance:
    finance_w.append(item[0])

#create vector word
finance_vec = []
for word in finance_w:
    finance_vec.append(newsw2v[word])"""

