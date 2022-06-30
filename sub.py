import subprocess

subprocess.run('cd',cwd=r'c:\visualstadio\KOSENPROCON\dictation-kit-4.5',shell=True)
subprocess.run(r'.\bin\windows\julius.exe -C main.jconf -C am-gmm.jconf -module -charconv utf-8 sjis',cwd=r'c:\visualstadio\KOSENPROCON\dictation-kit-4.5',shell=True)