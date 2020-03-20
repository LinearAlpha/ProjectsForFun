@echo 
cd source
pyinstaller --onefile -n web_crawling_V0.3.exe main.py --uac-admin^
                                                       --exclude-module openpyxl^
                                                       --exclude-module os^
pause