# 플리

1. startproject playList
   1. python -m pip install django~=4.2
   2. django-admin startproject playList
   3. File > Settings... > Language & Framework > Django > [v] Enable Django Support
   4. Run > Edit Configurations... > + Django Server > Name: runserver
   5. VCS > Enable Version Control Integration... > git > ok
2. startapp 플리
   1. python manage.py startapp 플리
   2. '플리', in INSTALLED_APPS in settings.py
3. 플리/
   1. models
      1. User
         1. id, pw, created_at, updated_at
      2. PlayList
         1. id, title, image, created_at, updated_at, author
      3. python manage.py makemigrations 플리
      4. python manage.py migrate
   2. views
      1. show_index
      2. show_login
      3. show_signup
      4. show_url
      5. show_mypage
      6. show_create
      7. show_delete
   3. templates/플리/
      1. index.html
      2. login.html
      3. signup.html
      4. url.html
      5. playlist_list.html
      6. playlist_create.html
      7. playlist_confirm_delete.html
   4. urls
      1. 플리:show_index
      2. 플리:EmailLoginView.as_view()
      3. 플리:SingUpView.as_view()
      4. 플리:show_url
      5. 플리:playListview.as_view()
      6. 플리:PlayListCreateView.as_view()
      7. 플리:PlayListDeleteView.as_view()
   5. static/
      1. css/
         1. index.css > index html 스타일 시트
         2. login.css > login, signup html 스타일 시트 
         3. style.css > 전역 스타일 시트
         4. create.css > playList create html 스타일 시트
         5. delete.css > playList delete html 스타일 시트
         6. mypage.css > playList list view html 스타일 시트
         7. url.css > url html 스타일 시트
      2. img/
         1. solar_play-bold-duotone.svg > 로고 이미지
         2. sound-bar.svg > 사운드바 이미지
         3. delete.svg > playList 삭제 이미지
         4. edit.svg > playList 수정 이미지
4. templates/
   1. base.html
      1. settings.py > TEMPLATES
         1. 'DIRS': [BASE_DIR / 'templates']
