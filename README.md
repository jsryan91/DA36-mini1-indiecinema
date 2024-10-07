# DA36-miniproject1

# 🍿IndieCinema🍿
***
IndieCinema는 독립영화관 영화 현장 예매 키오스크 콘솔 프로그램입니다.
<br>

시네필들을 위한 상영 · 영화 이벤트 정보를 제공합니다

<br>


## 🎥 인디시네마에서는 이런 걸 할 수 있어요!
***
### 1. 영화 예매

- 당일 매칭된 영화와 상영 시간 스케쥴을 확인 후 상영 시간을 번호로 선택
- 선택한 영화에 따른 이벤트 정보 확인
- 좌석을 (n,m) 형태로 입력하여 좌석 선택 
- 결제 진행 여부 최종 확인 후 예매 내역 출력

### 2. 예매 내역 조회

- 예매 후 부여받은 예매 번호 입력시 예매 내역 출력

### 3. 전체 이벤트 조회

- 상영관에서 진행 중인 모든 이벤트 확인

### 4. 관리자 모드

- 올바른 관리자 코드 입력시 관리자 모드 전환
- 총 매출과 이윤 확인 
- 누적 관객수 확인

<br>

## 🎥 인디시네마의 시연영상 함께 보실까요?
###### 해당 팀원의 youtube 채널로 이동합니다. 영상 내용은 동일합니다.

[![indiecinema의 시연영상](https://img.youtube.com/vi/b5c93B7LmgE/0.jpg)](https://youtu.be/b5c93B7LmgE?si=qccVx5oWY42ytTdv)

[김정아의 채널에서 보기](https://youtu.be/OA49HNgpa_E?si=nUdQBPnGgQJdxZme)
<br>
[심정석의 채널에서 보기](https://www.youtube.com/watch?v=C9HAoDm_--M)
<br>
[조한희의 채널에서 보기](https://youtu.be/b5c93B7LmgE?si=PV0pb73ppMglAS-9)
<br>
[허채연의 채널에서 보기](https://youtu.be/e6QbKj5W4f8?si=5ByYNl8veqf3mCNh)


<br>

## ⚙️ 인디시네마는 이런 기술을 사용했어요!
***

- Python
- Excel file
- Text file
- Figma
- Github

<br>


## 🏠 인디시네마의 클래스 구조
*** 

* main_menu.py 
  * user가 kiosk에서 입력하는 값을 받음
  * 입력하는 값에 따른 return 값을 출력해주는 일을 담당

---
* Entity
  * 실제 자료의 구조 (객체)
  

* Service
  * 사용자가 입력한 값에 대한 return 값을 요청하는 역할


* Repo (repositoriy)
  * 정보의 저장소
---
## class
###### ㄴ 각 class는 entity, repo, service file을 가집니다.

1) **movie**
- movie.txt 파일에 현재 영화관에서 상영중인 영화 목록 관리

2) **theater**
- theater.xlsx 파일에 날짜별 worksheet 생성 이후에 상영정보 (영화제목/시간/좌석) 저장

  - python에서 excel 접근  
  - ```pip install openpyxl```
  - ```import openpyxl```  

3) **rev (reservation)**
- reservation.txt 파일에 예매 정보를 저장합니다
  - 형식 : 예매번호(rev_id),영화제목,상영시간, 좌석(행), 좌석(열)


4) **event**
- event.txt 파일에 영화별 event 내용 저장
  - 형식 : (영화 내용, 진행하는 이벤트 내용, 이벤트 진행 기간 )


5) **admin**
- 관리자
  1) 매출 확인
  2) 총 관객 수 확인

<br>

## 💭 인디시네마 팀원들의 소감 들어볼까요?
***
### 🟤허채연 (team lead)

<br>

### 🟣김정아 

<br>

### 🟡심정석

<br>

### 🟢조한희
- 객체지향 개념을 학습한 후, 클래스 다이어그램을 그려 구조도를 작성하면서 객체지향 프로그램의 전체 흐름을 이해할 수 있었습니다.
- Github 협업 도구를 사용하여 하나의 파일에서 공동작업하는 방법을 배우는 소중한 기회였습니다. 또 작은 부분도 하나하나 서로 소통하며 이해시키는 과정에서 소통의 중요성을 깨달았습니다.
- 독립영화를 좋아한다는 개인적인 이유로 프로젝트 주제를 제안했는데, 프로젝트를 성공적으로 마무리할 수 있어 매우 뿌듯했습니다. 특히, 프로젝트의 출발점이었던 영화 별 이벤트 조회 기능을 후반부에 추가하면서 클래스를 통한 기능 구현 로직을 더 깊이 이해할 수 있었습니다.

