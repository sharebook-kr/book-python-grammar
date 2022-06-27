import pickle

def show_main_menu():
    print("*" * 40)
    print(" 1. 일기쓰기")
    print(" 2. 일기조회")
    print(" 3. 종료")
    print("*" * 40)
    main_menu = input("메뉴선택: ")
    return main_menu

def write_diary(diary):
    date = input("날짜입력 (예: 2020-09-10): ")
    content = input("내용: ")
    diary[date] = content

def dump_diary(diary):
    with open("diary.db", "wb") as f:
        pickle.dump(diary, f)

def load_diary():
    try:
        with open("diary.db", "rb") as f:
            diary = pickle.load(f)
            return diary
    except FileNotFoundError:
        return {}

def show_diary(diary):
    for date, content in diary.items():
        print("-" * 40)
        print(date, content)

def main():
    diary = load_diary()
    #print(diary)

    while True:
        main_menu = show_main_menu()

        if main_menu == '1':
            write_diary(diary)
        elif main_menu == '2':
            show_diary(diary)
        elif main_menu == '3':
            dump_diary(diary)
            print("감사일기를 종료합니다.")
            break

main()