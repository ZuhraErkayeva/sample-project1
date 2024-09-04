from datetime import datetime
def main_func():
    print("1. Vazifa qo'shish")
    print("2. Vazifa o'chirish")
    print("3. Vazifalarni ko'rish")
    print("4. Vazifalarni tugash vaqti bo'yicha ko'rish")
    print("5. Vazifalarni qidirish")
    print("6. Muddati o'tgan vazifalarni ko'rish")
    print("7. Vazifani tugallash")
    print("8. Dasturdan chiqish")
def add_task(td):
    title = input("Vazifani kiriting: ")
    desc = input("Izohni kiriting: ")
    due_date = input("Tugash muddatini kiriting kun-oy-yil (01-01-2024): ")
    status = "Jarayonda"
    td[title] = [desc, datetime.strptime(due_date, "%d-%m-%Y").date(), status]
    print("Vazifa muvofaqqiyatli qo'shildi!")

def remove_task(td):
        title = input("O'chirilishi kerak bo'lgan vazifani kiriting: ")
        if title in td:
            del td[title]
            print("Vazifa muvoffaqiyatli o'chirildi")
        else:
            print("Bunday vazifa mavjud emas")
def view_tasks(td):

        if len(td) > 0:
            for title, detail in td.items():
                print(f"Vazifa nomi: {title}")
                print(f"Vazifa tavsifi: {detail[0]}")
                print(f"Vazifa tugash vaqti: {detail[1]}")
                print(f"Vazifa status: {detail[2]}\n")
        else:
            print("Hali vazifalar yo'q")
def sort_by_due_date(td):
    sorted_data = sorted(td.items(), key=lambda x: x[1][1])
    for i in sorted_data:
        print(f"Vazifa nomi: {i[0]}")
        print(f"Vazifa tavsifi: {i[1][0]}")
        print(f"Vazifa tugash vaqti: {i[1][1]}")
        print(f"Vazifa status: {i[1][2]}\n")
def search_task(td):
        search = input("Qidirmoqchi bo'lgan vazifangizni kiriting: ")
        print("\n")
        result = []
        for title, detail in td.items():
            if detail[0].find(search) >= 0 or title.find(search) >= 0:
                result.append((title, detail))
        if len(result) > 0:
            for i in result:
                print(f"Vazifa nomi: {i[0]}")
                print(f"Vazifa tavsifi: {i[1][0]}")
                print(f"Vazifa tugash vaqti: {i[1][1]}")
                print(f"Vazifa status: {i[1][2]}\n")
        else:
            print("Topilmadi")

def display_overdue_tasks(td):
    today = datetime.today().date()
    overdue_tasks = {title: detail for title, detail in td.items() if detail[1] < today}
    if overdue_tasks:
        for title, detail in overdue_tasks.items():
            print(f"Overdue Task Title: {title}")
            print(f"Description: {detail[0]}")
            print(f"Due Date: {detail[1]}")
            print(f"Status: Overdue\n")
            td[title][2] = "Overdue"
    else:
        print("No overdue tasks")

def mark_task_as_completed(td):
    title = input("Bajarilgan vazifani kiriting:  ")
    if title in td:
        td[title][2] = "Completed"
        print("Vazifa bajarildi deb belgilandi")
    else:
        print("Task not found")
def close_project():
    print("Dasturdan muvoffaqiyatli chiqildi")

def close_application():
    print("Ilovadan chiqildi!")