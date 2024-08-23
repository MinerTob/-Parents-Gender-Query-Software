import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os
import subprocess

# 用户数据类
class UserData:
    def __init__(self):
        self.users = {}
        self.remember_me = False
        self.load()  # 加载用户数据

    def load(self):
        # 尝试读取用户数据
        try:
            if os.path.exists('user_data.txt'):
                with open('user_data.txt', 'r') as file:
                    for line in file.readlines():
                        username, password = line.strip().split(',')
                        self.users[username] = password
        except Exception as e:
            print(f"加载用户数据时出错: {str(e)}")

    def save(self):
        # 将用户数据写入文本文件
        with open('user_data.txt', 'w') as file:
            for username, password in self.users.items():
                file.write(f"{username},{password}\n")

    def register(self, username, password):
        if username in self.users:
            return False  # 用户名已存在
        self.users[username] = password
        self.save()  # 保存用户数据
        return True

    def login(self, username, password):
        return username in self.users and self.users[username] == password

# 启动父母性别查询器
def start_gender_finder():
    target_filename = "父母性别查询器最终版.exe"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 在当前目录及其子目录中寻找文件
    for root, dirs, files in os.walk(current_dir):
        if target_filename in files:
            file_path = os.path.join(root, target_filename)
            print(f"找到文件: {file_path}")  # 调试输出
            break
    else:
        messagebox.showerror("错误", "父母性别查询器未找到，请确保文件在启动器同一目录或子目录下。")
        print(f"未找到目标文件: {target_filename}")  # 调试输出
        return

    # 启动进程（隐藏窗口）
    try:
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

        subprocess.Popen(
            [file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            startupinfo=startupinfo
        )
        print("启动性别查询器成功！")  # 调试输出
    except Exception as e:
        messagebox.showerror("错误", f"无法启动文件: {str(e)}")

# 登录窗口
def open_login_window():
    def handle_login():
        username = entry_username.get()
        password = entry_password.get()
        
        print(f"尝试登录: 用户名={username}, 密码={password}")  # 调试输出
        
        if user_data.login(username, password):
            print("登录成功!")  # 调试输出
            user_data.remember_me = remember_var.get()
            user_data.save()  # 确保用户数据保存
            login_window.destroy()  # 关闭登录窗口
            start_gender_finder()  # 启动性别查询器
        else:
            lbl_error.config(text="无效的用户名或密码")

    def open_register_window():
        login_window.withdraw()  # 隐藏登录窗口
        open_register_window_instance()  # 打开注册窗口

    def on_username_selected(event):
        selected_username = entry_username.get()
        if selected_username in user_data.users:
            entry_password.delete(0, tk.END)
            entry_password.insert(0, user_data.users[selected_username])  # 填充密码

    # 创建登录窗口
    login_window = tk.Tk()
    login_window.title("登录")
    login_window.geometry("800x700")
    login_window.configure(bg="#f0f8ff")

    tk.Label(login_window, text="用户名", bg="#f0f8ff", font=("Arial", 18)).pack(pady=20)

    username_list = list(user_data.users.keys())
    entry_username = ttk.Combobox(login_window, values=username_list, font=("Arial", 16), width=30)
    entry_username.pack(pady=10, padx=50)

    entry_username.bind("<<ComboboxSelected>>", on_username_selected)

    tk.Label(login_window, text="密码", bg="#f0f8ff", font=("Arial", 18)).pack(pady=20)
    entry_password = tk.Entry(login_window, show='*', font=("Arial", 16), width=30)
    entry_password.pack(pady=10, padx=50)

    remember_var = tk.BooleanVar(value=user_data.remember_me)
    remember_cb = tk.Checkbutton(
        login_window, 
        text="记住密码", 
        variable=remember_var, 
        font=("Arial", 16), 
        bg="#f0f8ff"
    )
    remember_cb.pack(pady=20)

    lbl_error = tk.Label(login_window, text="", fg="red", bg="#f0f8ff", font=("Arial", 14))
    lbl_error.pack(pady=10)

    button_width = 20
    btn_login = tk.Button(login_window, text="登录", command=handle_login, font=("Arial", 16), bg="#007BFF", fg="white", width=button_width)
    btn_login.pack(pady=20)

    btn_register = tk.Button(login_window, text="没有帐户？立即注册", command=open_register_window, font=("Arial", 16), bg="#28a745", fg="white", width=button_width)
    btn_register.pack(pady=10)

    login_window.protocol("WM_DELETE_WINDOW", lambda: login_window.destroy())
    login_window.mainloop()

# 注册窗口
def open_register_window_instance():
    def handle_register():
        username = entry_username.get()
        password = entry_password.get()
        
        if username.strip() == "":
            lbl_message.config(text="用户名为空！")
            return
        if password.strip() == "":
            lbl_message.config(text="密码为空！")
            return
        
        if user_data.register(username, password):
            lbl_message.config(text="注册成功！可以登录了。")
            entry_username.set(username)  # 填充用户名
            entry_password.delete(0, tk.END)  # 清空密码框
            entry_password.insert(0, password)  # 填充当前注册的密码
        else:
            lbl_message.config(text="用户名已存在！")

    register_window = tk.Toplevel()
    register_window.title("注册")
    register_window.geometry("800x700")
    register_window.configure(bg="#f0f8ff")

    tk.Label(register_window, text="用户名", bg="#f0f8ff", font=("Arial", 18)).pack(pady=20)
    entry_username = tk.Entry(register_window, font=("Arial", 16), width=30)
    entry_username.pack(pady=10, padx=50)

    tk.Label(register_window, text="密码", bg="#f0f8ff", font=("Arial", 18)).pack(pady=20)
    entry_password = tk.Entry(register_window, show='*', font=("Arial", 16), width=30)
    entry_password.pack(pady=10, padx=50)

    lbl_message = tk.Label(register_window, text="", bg="#f0f8ff", fg="green", font=("Arial", 14))
    lbl_message.pack(pady=10)

    button_width = 20
    btn_register = tk.Button(register_window, text="注册", command=handle_register, font=("Arial", 16), bg="#28a745", fg="white", width=button_width)
    btn_register.pack(pady=20)

    btn_back = tk.Button(register_window, text="已有帐户？去登录", command=lambda: [register_window.destroy(), open_login_window()], font=("Arial", 16), bg="#007BFF", fg="white", width=button_width)
    btn_back.pack(pady=10)

# 初始化用户数据
user_data = UserData()

# 打开登录窗口
open_login_window()
