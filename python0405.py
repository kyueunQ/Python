
# coding: utf-8

# ## Python 기초

# ### end="    "

# In[9]:


print("string", end="  ")
print("python")


# ### print(string, int, string) 

# In[16]:


name = "kyueun"
age = 25
phone = "010-xxxx-xxxx"


# In[17]:


print("내 이름은 " + name + "입니다.", end=" ")
print("나는", age, "살입니다.")
print("내 연락처는 " + phone + "입니다!")


# ### 마치 java 'scanner' 처럼

# In[1]:


input("나이를 입력하세요 " )


# In[5]:


num = input("나이를 입력하세요")


# In[6]:


type(num)


# In[7]:


int(num) + 1


# ### String format

# In[10]:


print("안녕하세요 %s" % "kyu")


# In[11]:


print("안녕하세요 {name}".format(name="kyu"))


# ### len(string)

# In[12]:


key = "python"


# In[13]:


len(key)


# ### 예제 1

# In[2]:


name = input("이름을 입력하세요 ")


# In[3]:


age = input("나이를 입력하세요 ")


# In[4]:


phone = input("핸드폰 번호를 입력하세요 ")


# In[6]:


print("내 이름은 " + name + "입니다.", end=" ")
print("내이름은 ",len(name), "글자입니다.")
print("나는.", age, "살입니다.")
print("내 연락처는 " + phone + "입니다!")


# ### index

# In[7]:


string = "Kyueun"


# In[12]:


"Kyueun"[0:3]  #0~2까지 출력


# In[13]:


"Kyueun"[:]   #전체 출력


# In[10]:


string[3]


# In[15]:


string[-1]   #마지막 순서의 알파벳


# In[18]:


"Kyueun"[0:5:3]


# ### 예제 2

# In[26]:


likes = ''


# In[27]:


likes += "book"


# In[29]:


likes += ", cake"


# In[32]:


likes


# ## 데이터 구조

# ### List

# In[33]:


likes = []


# In[36]:


likes.append("cake")


# In[37]:


likes.append("cookie")


# In[38]:


likes.append("game")


# In[41]:


likes[-1]


# In[40]:


likes[0]


# In[42]:


del likes[-1]


# In[43]:


likes


# In[44]:


likes.reverse()


# In[45]:


likes


# ### 예제 3

# In[56]:


var = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# In[47]:


var[0]


# In[48]:


var[-1]


# In[50]:


var[0:3]


# In[66]:


var[0:2] + var[-2:]


# In[65]:


var[1::2]


# In[54]:


var.reverse()


# In[55]:


var


# ## List의 Method

# ### .sort()

# In[71]:


var = [7, 4, 9, 2, 5, 2]
var.sort()
var


# ### var.pop(0)과 del var[0] 비교

# In[77]:


var.pop(0)


# In[78]:


del var[2]   #어떤 숫자가 사라졌는지 알 수 없음


# In[80]:


var.insert(-1, 5)
var


# In[81]:


var.count(5)  #list안에 5가 몇 번이 들어있나


# In[88]:


2 in var

