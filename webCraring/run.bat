@echo 
cd source
pip install pyinstaller
pyinstaller --clean -D -F -n web_crawling_V0.1.exe main.py
pause