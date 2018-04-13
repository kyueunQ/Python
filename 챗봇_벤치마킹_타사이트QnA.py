
# coding: utf-8

# # QnA 질문 분석
# 
# 참고 사이트 :
# - 웹 크롤링
# https://beomi.github.io/2017/01/20/HowToMakeWebCrawler/
# - 더클로젯 대여서비스 QnA
# http://www.theclozet.co.kr/faq/

# In[1]:


import requests


# In[3]:


response = requests.get("http://www.theclozet.co.kr/faq/")


# In[20]:


response.content


# In[21]:


content = str(response.content, "UTF-8")


# In[15]:


# BeautifulSoup : 태그로 구성된 요소를 python이 이해하는 상태로 변경
from bs4 import BeautifulSoup as bs


# In[23]:


result = bs(content, "html.parser")


# In[25]:


result.head


# In[26]:


result.find_all("div", {'class' : 'wpb_wrapper'})


# In[28]:


for qna in result.find_all("div", {'class' : 'wpb_wrapper'}):
        print(qna.text)


# ### [F12] - 코드가 궁금한 부분 선택(ctrl+shift+c) - 마우스 오른쪽 'copy' -' copy selector' 클릭 ↓
# #post-379 > div:nth-child(13) > div.col-sm-9.col-lg-4.col-sm-offset-3.nm_column > div > div.wpb_text_column.wpb_content_element > div > h6
# 
# div > h6

# In[35]:


ae = result.select(
    'div > h6'
)


# In[37]:


for con in ae:
    print(con.text)


# In[41]:


for con in ae:
    print(con.text.split(' '))

