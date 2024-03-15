# 영화

## 부트스트랩 

### 부트스트랩 모달 태그
- 모달의 영역은 `flex`안에서는 적용이 안됨 
- 따라서 모달 영역을 맨 밑에 두고 한다

### 이미지나 내용물의 위치(부트스트랩) 
- `text-center`: 가운데
- `text-end`: 오른쪽
- `text-start`: 왼쪽

### card 사용할 때 주의점
- `row` 영역안에 `col`들이 잘 들어가 있는가?
- 같은 높이 영역을 지정해주고 싶을 때: `card`부분에 `h-100`추가 ex: `<div class="card h-100">`

### width에 따라 다른 태그나 내용이 보여야할 때
- `d-none`, `d-block`을 사용

### header 이미지 가운데 정렬
- `header`태그에 `d-flex`적용 후 `justify-content-center`적용

  
## 스타일

### width를 고정하는 방법
- `style`영역에 `media`쿼리를 작성한다
```
@media screen and (min-width: 1400px) {
      .main-img {
        width: 1380px;
      }
    }
```
- `min-width`: 이상일 때 내용이 실행 됨