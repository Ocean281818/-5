import sqlite3

# 连接数据库
conn = sqlite3.connect("student.db")

# 创建学生信息表
def create_table():
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY,
                    name TEXT,
                    gender TEXT,
                    age INTEGER,
                    phone TEXT,
                    python_score INTEGER
                )''')
    conn.commit()

# 添加学生信息
def add_student():
    student_id = int(input("请输入学号: "))
    name = input("请输入姓名: ")
    gender = input("请输入性别: ")
    age = int(input("请输入年龄: "))
    phone = input("请输入电话: ")
    python_score = int(input("请输入Python课成绩: "))

    cur = conn.cursor()
    cur.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?)",
                (student_id, name, gender, age, phone, python_score))
    conn.commit()
    print("学生信息添加成功！")

# 删除学生信息
def del_student():
    student_id = int(input("请输入要删除的学号: "))
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id=?", (student_id,))
    conn.commit()
    print("学生信息删除成功！")

# 修改学生信息
def revise_student():
    student_id = int(input("请输入要修改的学号: "))
    cur = conn.cursor()
    cur.execute("SELECT * FROM students WHERE student_id=?", (student_id,))
    student = cur.fetchone()

    if student:
        print(f"学号: {student[0]}")
        print(f"姓名: {student[1]}")
        print(f"性别: {student[2]}")
        print(f"年龄: {student[3]}")
        print(f"电话: {student[4]}")
        print(f"Python课成绩: {student[5]}")

        field = input("请输入要修改的字段: ")
        if field in ('name', 'gender', 'age', 'phone', 'python_score'):
            new_value = input("请输入新值: ")
            cur.execute(f"UPDATE students SET {field}=? WHERE student_id=?", (new_value, student_id))
            conn.commit()
            print("学生信息修改成功！")
        else:
            print("无效的字段！")
    else:
        print("该学号的学生不存在！")

# 显示学生信息
def show_student():
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()

    if students:
        for student in students:
            print(f"学号: {student[0]}")
            print(f"姓名: {student[1]}")
            print(f"性别: {student[2]}")
            print(f"年龄: {student[3]}")
            print(f"电话: {student[4]}")
            print(f"Python课成绩: {student[5]}")
            print("--------------------")
    else:
        print("学生信息为空！")

# 显示菜单
def show_menu():
    print("===== 学生信息系统 =====")
    print("1. 增加学生信息")
    print("2. 删除学生信息")
    print("3. 修改学生信息")
    print("4. 显示学生信息")
    print("0. 退出系统")
    return int(input("请输入选项: "))

# 主函数
def main():
    create_table()
    while True:
        select = show_menu()
        if select == 1:
            add_student()
        elif select == 2:
            del_student()
        elif select == 3:
            revise_student()
        elif select == 4:
            show_student()
        elif select == 0:
            # 退出系统
            break
        else:
            print("输入有误！请重新操作！")
            continue

    # 关闭连接
    conn.close()

if __name__ == '__main__':
    main()
