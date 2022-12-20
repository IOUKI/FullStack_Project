from mysql import connector
from werkzeug.security import generate_password_hash, check_password_hash
from random import randint
import datetime

def db_conn():
    conn = connector.connect(
        host='mysql_db',
        user='my_user',
        password='123456',
        database='test_db',
        port='3306'
    )
    return conn

def do_SQL_stuff(sql):
    conn = db_conn()
    Cursor = conn.cursor()
    Cursor.execute(sql)
    conn.commit()
    conn.close()

def do_select_stuff(sql):
    conn = db_conn()
    Cursor = conn.cursor()
    Cursor.execute(sql)
    result = Cursor.fetchall()
    conn.close()
    return result

class user_query:

    def create_user(account, password):
        symbol = '!@#$%^&*()_+'
        salt = ''
        for i in range(5):
            index = randint(0, (len(symbol) - 1))
            salt += symbol[index]

        hash_key = generate_password_hash((password+salt))
        sql = f'insert into user_key(account, hash_key, hash_salt) \
                values("{account}", "{hash_key}", "{salt}");'
        do_SQL_stuff(sql)
        return True

    def user_list():
        sql = 'select * from user_key;'
        result = do_select_stuff(sql)
        print(result)

    def login(account, password):
        sql = f'select id, hash_key, hash_salt from user_key where account = "{account}";'
        result = do_select_stuff(sql)
        if result == []:
            return False

        user_id = result[0][0]
        hash_key = result[0][1]
        hash_salt = result[0][2]
        check_user = check_password_hash(hash_key, (password+hash_salt))
        if check_user == True:
            now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            random_num = randint(0, 100)
            session_id = now_time + str(0) + str(random_num)
            sql = f'update user_key \
                    set s_id = "{session_id}" \
                    where id = {user_id};'
            do_SQL_stuff(sql)
            return session_id
        else:
            return False

    def getUserId(s_id):
        sql = f'select id from user_key where s_id = "{s_id}";'
        result = do_select_stuff(sql)
        if result == []:
            return False
        else:
            return result[0][0]

class todo_query:

    def add(s_id, title, content):
        user_id = user_query.getUserId(s_id)
        if user_id != False:
            sql = f'insert into todo(user_id, title, content) \
                    values({user_id}, "{title}", "{content}")'
            do_SQL_stuff(sql)
            return True
        else:
            return False

    def update(todo_id, title, content):
        sql = f'update todo \
                set title = "{title}", \
                content = "{content}" \
                where id = {todo_id};'
        do_SQL_stuff(sql)
    
    def select(s_id):
        sql = f'select todo.id, todo.title, todo.content \
                from todo, user_key \
                where user_key.id = todo.user_id \
                and s_id = "{s_id}";'
        result = do_select_stuff(sql)
        list = []
        for x in result:
            list.append({
                'todo_id': x[0],
                'title': x[1],
                'content': x[2]
            })
        return list

    def delete(s_id, todo_id):
        user_id = user_query.getUserId(s_id)
        if user_id != False:
            sql = f'delete from todo where id = {todo_id};'
            do_SQL_stuff(sql)
            return True 
        else:
            return False

