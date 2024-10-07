# DA36-miniproject1
## indiecinema🍿
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
### class
###### ㄴ 각 class는 service, repo, entity file을 가집니다.

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