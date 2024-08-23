import tkinter as tk
import ctypes


def minimize_terminal():
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    ctypes.windll.user32.ShowWindow(hwnd, 2)


def update_texts(*args):
    if language.get() == '简体中文':
        lbl_welcome.config(text='欢迎使用父母性别查询器')
        lbl_version.config(text='版本:v9.11451.4')
        lbl_author.config(text='作者:矿工Tob')
        lbl_open_source.config(text='由矿工Tob这个必养的开源')
        btn_father.config(text='查询父亲性别')
        btn_mother.config(text='查询母亲性别')
    elif language.get() == 'English':
        lbl_welcome.config(text='Welcome to the Parent Gender Finder')
        lbl_version.config(text='Version v9.11451.4')
        lbl_author.config(text='Author: Miner Tob')
        lbl_open_source.config(text='It is open source by Miner Tob')
        btn_father.config(text='Query Father\'s Gender')
        btn_mother.config(text='Query Mother\'s Gender')
    elif language.get() == 'Русский':
        lbl_welcome.config(text='Добро пожаловать в поиск пола родителей')
        lbl_version.config(text='Версия v9.11451.4')
        lbl_author.config(text='Автор: Минер Тоб')
        lbl_open_source.config(text='Открытый исходный код от Минер Тоб')
        btn_father.config(text='Запросить пол отца')
        btn_mother.config(text='Запросить пол матери')
    elif language.get() == '日本語':
        lbl_welcome.config(text='親の性別ファインダーへようこそ')
        lbl_version.config(text='バージョン v9.11451.4')
        lbl_author.config(text='著者：マイナー・トブ')
        lbl_open_source.config(text='マイナー・トブによるオープンソース')
        btn_father.config(text='父親の性別をクエリする')
        btn_mother.config(text='母親の性別をクエリする')
    elif language.get() == 'new gno hzit naij':
        lbl_welcome.config(text='iq nux ahc eib gnix um uf gnoy ihs niy nauh')
        lbl_version.config(text='neb nab:v9.11451.4')
        lbl_author.config(text='ehz ouz：矿工Tob')
        lbl_open_source.config(text='uoy 矿工Tob ehz eg BYD kai yuan')
        btn_father.config(text='uf niq nix eib ahc nux')
        btn_mother.config(text='um niq nix eib ahc nux')
    elif language.get() == 'Français':
        lbl_welcome.config(text='Bienvenue dans le Finder de Genre des Parents')
        lbl_version.config(text='Version:v9.11451.4')
        lbl_author.config(text='Auteur: Mineur Tob')
        lbl_open_source.config(text='C\'est un logiciel libre par Mineur Tob')
        btn_father.config(text='Consulter le genre du père')
        btn_mother.config(text='Consulter le genre de la mère')
    elif language.get() == 'العربية':
        lbl_welcome.config(text='مرحبًا بكم في باحث جنس الوالدين')
        lbl_version.config(text='الإصدار:v9.11451.4')
        lbl_author.config(text='المؤلف: مينر توب')
        lbl_open_source.config(text='إنه مفتوح المصدر بواسطة مينر توب')
        btn_father.config(text='استعلام عن جنس الأب')
        btn_mother.config(text='استعلام عن جنس الأم')
    elif language.get() == 'Español':
        lbl_welcome.config(text='Bienvenido al Buscador de Género de los Padres')
        lbl_version.config(text='Versión:v9.11451.4')
        lbl_author.config(text='Autor: Minero Tob')
        lbl_open_source.config(text='Es un software de código abierto por el minero Tob')
        btn_father.config(text='Consultar el género del padre')
        btn_mother.config(text='Consultar el género de la madre')
    elif language.get() == 'Português':
        lbl_welcome.config(text='Bem-vindo ao Encontrador de Gênero dos Pais')
        lbl_version.config(text='Versão:v9.11451.4')
        lbl_author.config(text='Autor: Miner Tob')
        lbl_open_source.config(text='É um software de código aberto feito por Miner Tob')
        btn_father.config(text='Consultar o gênero do pai')
        btn_mother.config(text='Consultar o gênero da mãe')


def display_result(message):
    lbl_result.config(text=message, fg="red")


def query_father():
    if language.get() == '简体中文':
        result = "查询完毕，您父亲的性别为: 男😅"
    elif language.get() == 'English':
        result = "After the query, your father's gender is: male 😅"
    elif language.get() == 'Русский':
        result = "После запроса пол вашего отца: мужской 😅"
    elif language.get() == '日本語':
        result = "クエリの結果、お父さんの性别は男性です 😅"
    elif language.get() == 'new gno hzit naij':
        result = "ib naw nux ahc,nin uf niq ed nix eib iew:Nam 😅"
    elif language.get() == 'Français':
        result = "Après la requête, le genre de votre père est : masculin 😅"
    elif language.get() == 'العربية':
        result = "بعد الاستعلام، جنس والدك هو: ذكر 😅"
    elif language.get() == 'Español':
        result = "Después de la consulta, el género de tu padre es: masculino 😅"
    elif language.get() == 'Português':
        result = "Após a consulta, o gênero do seu pai é: masculino 😅"
    display_result(result)


def query_mother():
    if language.get() == '简体中文':
        result = "查询完毕，您母亲的性别为: 女🤓"
    elif language.get() == 'English':
        result = "After the query, your mother's gender is: female 🤓"
    elif language.get() == 'Русский':
        result = "После запроса пол вашей матери: женский 🤓"
    elif language.get() == '日本語':
        result = "クエリの結果、お母さんの性别は女性です 🤓"
    elif language.get() == 'new gno hzit naij':
        result = "ib naw nux ahc,nin um niq ed nix eib iew:Namow 🤓"
    elif language.get() == 'Français':
        result = "Après la requête, le genre de votre mère est : féminin 🤓"
    elif language.get() == 'العربية':
        result = "بعد الاستعلام، جنس والدتك هو: أنثى 🤓"
    elif language.get() == 'Español':
        result = "Después de la consulta, el género de tu madre es: femenino 🤓"
    elif language.get() == 'Português':
        result = "Após a consulta, o gênero da sua mãe é: feminino 🤓"
    display_result(result)


# 创建主窗口
app = tk.Tk()
app.title("Parent Gender Finder")

# 隐藏终端窗口
if __name__ == "__main__":
    k = ctypes.windll.kernel32
    k.FreeConsole()

language = tk.StringVar(value='简体中文')  # 默认语言
app.geometry("800x700")  # 窗口大小
app.configure(bg="#e9ecef")  # 轻色背景

# 创建内容框架
frame = tk.Frame(app, bg="#e9ecef")  # 匹配主背景颜色
frame.pack(pady=20)

# 欢迎标签
lbl_welcome = tk.Label(frame, text='', font=("Arial", 24, "bold"), bg="#e9ecef", fg="#343a40")  # 深色文本
lbl_version = tk.Label(frame, text='', font=("Arial", 12), bg="#e9ecef", fg="#6c757d")  # 灰色文本
lbl_author = tk.Label(frame, text='', font=("Arial", 12), bg="#e9ecef", fg="#6c757d")
lbl_open_source = tk.Label(frame, text='', font=("Arial", 12), bg="#e9ecef", fg="#6c757d")

# 语言选择框
def on_language_select(event):
    update_texts()  # 调用更新语言文本

language_options = ['简体中文', 'English', 'Русский', '日本語', 'new gno hzit naij', 
                    'Français', 'العربية', 'Español', 'Português']

language_frame = tk.Frame(app, bg="#28a745", bd=2, relief="raised")
language_label = tk.Label(language_frame, text="选择语言", font=("Arial", 14), bg="#28a745", fg="white")
language_label.pack(pady=5)

dropdown = tk.OptionMenu(language_frame, language, *language_options, command=on_language_select)
dropdown.config(width=15, font=("Arial", 12), bg="#ffffff")
dropdown.pack()

language_frame.pack(pady=10)  # 调整框架的位置

# 按钮样式
button_style = {
    'font': ("Arial", 12),
    'bg': "#007BFF",
    'fg': "white",
    'activebackground': "#0056b3",
    'width': 20,
    'height': 2
}

btn_father = tk.Button(app, text='', command=query_father, **button_style)
btn_mother = tk.Button(app, text='', command=query_mother, **button_style)

# 显示标签
lbl_welcome.pack()
lbl_version.pack()
lbl_author.pack()
lbl_open_source.pack()
btn_father.pack(pady=10)
btn_mother.pack(pady=10)

# 添加查询结果标签
lbl_result = tk.Label(app, text="这里显示查询结果", font=("Arial", 18), fg="red", bg="#e9ecef")
lbl_result.pack(side=tk.BOTTOM, pady=20)  # 显示在窗口底部

update_texts()

# 最小化终端窗口
minimize_terminal()

app.mainloop()
