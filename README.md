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
   1. views
      1. show_index
   2. templates/플리/
      1. index.html
   3. urls
      1. 플리:show_index
   4. static/
      1. css/
         1. index.css > index html 스타일 시트
         2. style.css > 전역 스타일 시트
      2. img/
         1. solar_play-bold-duotone.svg > 로고 이미지
         2. sound-bar.svg > 사운드바 이미지
4. templates/
   1. base.html
      1. settings.py > TEMPLATES
         1. 'DIRS': [BASE_DIR / 'templates']