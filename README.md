<br>

# Django로 만드는 맛집 프로젝트[2팀]  

<br>

## **개발환경**
+ PyCham Community 
+ GitHub

<br>

## **사용 기술**
  ### **백엔드**   
  + Python(3.9)
  + Django
  + DJango ORM
     
 ### **데이터베이스**
  + Mysql

 ### **프론트엔드**
  + Javascript
  + HTML, CSS

<br>

  ## **주요 키워드**
  + REST API
  + Git 관리
  + HTTPS 통신(ngrok)  

<br>

  ## **구현 기능**
  + **user app**
    + 회원가입/회원탈퇴 로직
    + 로그인/로그아웃 로직 + 소셜네트워크 로그인
    + 회원수정/암호변경/ID찾기
    + 이메일인증
     
  + **hplace app**
    + 게시글 작성/수정/삭제    
    + 각 상점 위치 GPS 지도
    + 실시간 날씨 api
    + 실시간 누적방문자 api
   
  + **hplace app**
    + 코멘트 작성/삭제
  
  <br><br>
  
  ## **시스템 구조**
  ![인프라 설계](https://user-images.githubusercontent.com/97924823/151301762-8bbf0b4f-9826-457f-ba81-9c7ee27e4809.png)
  
  
  ## **ERD 구조**
![KakaoTalk_20220127_145038159](https://user-images.githubusercontent.com/96184680/151300028-0553fcc6-ff9d-4946-935d-37a727c17c6d.png)
  
  <br><br>
  
  ### **프로젝트 진행 과정 중 핵심 문제점과 해결방법**
   > #### 문제1. 소셜네트워크(구글, 네이버)를 활용해 로그인을 할 수 있는 기능 + DB연동 
   > #### 해결방법 : Django 라이브러리 'allauth'를 활용하여 superuser를 생성하고 admin페이지에 각 소셜네트워크(구글, 네이버) 개발자 사이트에서 Client ID와 Secret Code 값을 적용

  
  
   





