我写这个是为了好玩，但最终却让国外的人很尴尬（非常有趣的软件，虽然我作为开发者不知道这个软件的意义是什么）
I wrote this for fun, but ended up embarrassing people abroad (very interesting software, although I, the developer, have no idea what the point of this software is)
无论如何，享受这个软件带来的乐趣吧
Anyway, enjoy the fun of this software.




























如果你想打包一个完整的文件（exe格式）,请按照这这个文件格式打包：
If you want to package a complete file (exe format), please package it according to this file format:
youapp：
    login.py
    Subfolders：
        父母性别查询器最终版.exe
打包好后，在命令提示符中，输入以下命令：
After packaging, enter the following command in the command prompt:
pyinstaller --onefile --add-data "user_data.txt;." --add-data "父母性别查询器最终版.exe;." "登录父母性别查询器.py"
对了，在打包前，请先运行一次登录界面.py文件，随便填一个账号和密码，确保自动创建user_data.txt文件，以便打包后能对文件进行关联
By the way, before packaging, please run the login interface.py file once, fill in an account and password at random, and ensure that the user_data.txt file is automatically created so that the files can be associated after packaging.
