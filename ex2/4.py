contacts = {}

def add_contact(name, phone, email, company):
    contacts[name] = {'Phone': phone, 'Email': email, 'Company': company}

def del_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"{name}已经被删除。")
    else:
        print(f"{name}不在通讯录中。")

def get_contact_info(name):
    if name in contacts:
        info = contacts[name]
        print(f"姓名：{name}\n电话：{info['Phone']}\n邮箱：{info['Email']}\n工作单位：{info['Company']}")
    else:
        print(f"{name}不在通讯录中。")

def list_all_contacts():
    if not contacts:
        print("通讯录为空。")
    else:
        for name in contacts:
            get_contact_info(name)

if __name__=="__main__":
    add_contact('张三', '123456789', 'zhangsan@example.com', 'ABC公司')
    add_contact('李四', '987654321', 'lisi@example.com', 'XYZ公司')

    get_contact_info('张三')
    del_contact('李四')

    list_all_contacts()