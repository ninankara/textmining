import requests
import codecs
from bs4 import BeautifulSoup

#URL with keyword 금융 
result = requests.get("http://search.joins.com/JoongangNews?Keyword=%EA%B8%88%EC%9C%B5&SortType=Accuracy&SearchCategoryType=JoongangNews&PeriodType=All&ScopeType=All&ImageType=All&JplusType=All&BlogType=All&ImageSearchType=Image&TotalCount=0&StartCount=0&IsChosung=False&IssueCategoryType=All&IsDuplicate=True&Page=1&PageSize=10&IsNeedTotalCount=True")
print (result.status_code)
newsCtxURL = []

#HTML parsing
newscontent = result.content
scrap = BeautifulSoup(newscontent,'html.parser')

#get Page Navigation
pageCount = scrap.find_all(class_="link_page")

for i in range(len(pageCount)):
    pageNav = pageCount[i].string.strip()
    print (pageNav)
    urlNav = requests.get("http://search.joins.com/JoongangNews?page="+str(pageNav)+"&Keyword=%EA%B8%88%EC%9C%B5&SortType=New&SearchCategoryType=JoongangNews")
    print (urlNav.status_code)
    
    getPage = BeautifulSoup(urlNav.content,'html.parser')

    #List available News URL
    checkduplicate = "NULL"
   

    newsSection = getPage.find("div",{'class':'section_news'})
    if newsSection==None: 
        print("null")
    urlList=newsSection.find_all('li')
   
    for link in range(len(urlList)):
        print(len(urlList))
        urlcontent= urlList[link].find('a')['href']
    

        if urlcontent != checkduplicate:
            newsCtxURL.append(urlcontent)
            checkduplicate = urlcontent
        #print ("this is url: ",urlcontent['href'])


#Open each news content URL and retrieve the news content article
with codecs.open("joongang.txt","wb",encoding="utf-8") as documentNews: #you may change the file loc. default: python installation folder
    for ctx in newsCtxURL:
        try:
            #documentNews.write(ctx+'\n')
            getArticle = requests.get(ctx)
            articles = BeautifulSoup(getArticle.content,'html.parser')
            articles_head = articles.find("h1",{'class','headline mg'})
            articles_body = articles.find("div",{'id':'article_body'})

            #get News Title
            newsTitle = articles_head.string.strip()

            #get News Content
            newsBody = articles_body.text.strip()

            #Write to TXT file
            documentNews.write(newsTitle+'\n')
            documentNews.write(newsBody+'\n')
        except AttributeError:
            pass


print ("====Web Scrapping Done====")