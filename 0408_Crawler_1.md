
# 파이썬 웹 크롤러


```python
# 실수로 str = 'pyhon' 값을 할당했을 때, str()기능이 실행X
# 아래와 같이 입력하여 초기화할 수 있음
import builtins
```

## pip install requests  (설치)
: 파이썬 코드내에서 주소를 입력 받았을 때, 마크업을 하기 위함


```python
import requests
```


```python
# requests.get()를 실행했을 때 [200] : Ok를 의미함
# 아래 결과가 하나의 String 파일이기 때문에, indexing에 어려움
# html 구문 해석기를 통해 의미있는 단위를 찾아야 함

# .get : http를 가져올 때 GET method를 사용한다는 의미
response = requests.get("https://www.naver.com")
```


```python
# html 구문을 해석하는 작업을 통해 
response.text
```

## pip i.tinstall beautifulsoup4 (설치)
    : HTML 구문 해석
    : 위의 복잡한 코드를 '객체'로 받아서 가공할 수 있게함


```python
from bs4 import BeautifulSoup as bs
```


```python
# BeautifulSoup이란 객체에 response.text를 call함
# parser : 구문 해석기
# 지금 보내는 text string이 html이라서, 'html.parser'로 분석해달라 요청
result = bs(response.text, 'html.parser')
```


```python
result
```





```python
result.title
```




    <title>NAVER</title>




```python
result.title.text
```


```python
result.head
```
