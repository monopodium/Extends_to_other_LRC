## 
```
python3 -m venv C:\Users\mashu\Nutstore\1\paper_2023\sim_code\py3_env

C:\Users\mashu\Nutstore\1\paper_2023\sim_code\py3_env\Scripts\Activate.ps1
```

Links:
https://docs.python.org/zh-cn/3/library/venv.html#:~:text=%E9%80%9A%E8%BF%87%E6%89%A7%E8%A1%8C%20venv%20%E6%8C%87%E4%BB%A4%E6%9D%A5%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA%20%E8%99%9A%E6%8B%9F%E7%8E%AF%E5%A2%83%3A%20python3%20-m%20venv%20%2Fpath%2Fto%2Fnew%2Fvirtual%2Fenvironment,%E8%BF%90%E8%A1%8C%E6%AD%A4%E5%91%BD%E4%BB%A4%E5%B0%86%E5%88%9B%E5%BB%BA%E7%9B%AE%E6%A0%87%E7%9B%AE%E5%BD%95%EF%BC%88%E7%88%B6%E7%9B%AE%E5%BD%95%E8%8B%A5%E4%B8%8D%E5%AD%98%E5%9C%A8%E4%B9%9F%E5%B0%86%E5%88%9B%E5%BB%BA%EF%BC%89%EF%BC%8C%E5%B9%B6%E6%94%BE%E7%BD%AE%E4%B8%80%E4%B8%AA%20pyvenv.cfg%20%E6%96%87%E4%BB%B6%E5%9C%A8%E5%85%B6%E4%B8%AD%EF%BC%8C%E6%96%87%E4%BB%B6%E4%B8%AD%E6%9C%89%E4%B8%80%E4%B8%AA%20home%20%E9%94%AE%EF%BC%8C%E5%AE%83%E7%9A%84%E5%80%BC%E6%8C%87%E5%90%91%E8%BF%90%E8%A1%8C%E6%AD%A4%E5%91%BD%E4%BB%A4%E7%9A%84%20Python%20%E5%AE%89%E8%A3%85%EF%BC%88%E7%9B%AE%E6%A0%87%E7%9B%AE%E5%BD%95%E7%9A%84%E5%B8%B8%E7%94%A8%E5%90%8D%E7%A7%B0%E6%98%AF.venv%20%EF%BC%89%E3%80%82

## 坑坑：
报错：
```
Traceback (most recent call last):
  File "c:\Users\mashu\Nutstore\1\paper_2023\sim_code\pic_sim\draw.py", line 5, in <module>
    from our_placement import our_placement
  File "c:\Users\mashu\Nutstore\1\paper_2023\sim_code\pic_sim\our_placement.py", line 3, in <module>
    from tkinter import Label, _flatten
ModuleNotFoundError: No module named 'tkinter'
```
### 解决方案
```
https://www.w3cschool.cn/article/10855071.html#:~:text=%E7%9B%B4%E6%8E%A5%E9%80%89%E6%8B%A9%20uninstall%20%E5%8D%B3%E5%8F%AF%E8%BF%9B%E8%A1%8C%20python%20%E7%9A%84%E5%8D%B8%E8%BD%BD%E4%BA%86%E3%80%82%20%E7%AC%AC%E4%BA%8C%E7%A7%8D%E6%96%B9%E5%BC%8F%EF%BC%8C%E5%9C%A8%E8%AE%BE%E7%BD%AE%3E%E5%BA%94%E7%94%A8%3E%E5%BA%94%E7%94%A8%E5%92%8C%E5%8A%9F%E8%83%BD%E4%B8%AD%EF%BC%8C%E6%89%BE%E5%88%B0,python%20%E7%9B%B8%E5%85%B3%E9%80%89%E9%A1%B9%EF%BC%8C%E4%B9%9F%E5%8F%AF%E4%BB%A5%E8%BF%9B%E8%A1%8C%E5%8D%B8%E8%BD%BD%EF%BC%88%E5%8C%85%E6%8B%AC%20python%20%E7%8E%AF%E5%A2%83%E5%92%8C%20python%20%E5%90%AF%E5%8A%A8%E5%99%A8%EF%BC%89%E3%80%82
```

报错：
```
source C:\Users\mashu\Nutstore\1\paper_2023\sim_code\py3_env\Scripts\activate
source : 无法将“source”项识别为 cmdlet、函数、脚本文件或可运行程序的名称。请检查名称的拼写，如果包括路
径，请确保路径正确，然后再试一次。
所在位置 行:1 字符: 1
+ source C:\Users\mashu\Nutstore\1\paper_2023\sim_code\py3_env\Scripts\ ...
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (source:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
```
### 解决方案
```
Win 键 + Q ，在搜索框内输入 Powershell 。
点击以管理员身份运行。
输入代码 set-executionpolicy remotesigned 按回车键执行命令。
输入 A，按回车键执行


其中在默认的CMD 中可以使用 activate.bat 来激活环境变量，在PowerShell 或者是Windows10 中 新发布Terminal 中需要使用 Activate.ps1 文件来激活 ，默认情况下直接激活则会出现

想了解 计算机上的现用执行策略，打开 PowerShell 然后输入 get-executionpolicy

默认情况下返回的是 Restricted

以管理员身份打开PowerShell 输入 set-executionpolicy remotesigned

就可以正常在 PowerShell 中运行 ps1 文件了
```


```
git push的时候总是让你输入密码，把公钥添加到账户里也不行。
https://blog.csdn.net/Nick_Zhang_CSDN/article/details/99308541
```