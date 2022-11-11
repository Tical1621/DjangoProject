import psycopg2
from config import Config


def insert_group(group_id, group_name, members_count):
    print(f"db {group_id},{group_name},{members_count}")
    sql = """INSERT INTO public.groups VALUES (%s,%s,%s);"""
    conn = None
    try:
        params = Config['DATABASES'] # вот тут видимо не образуется коннект,разобраться с этим в 1 очередь
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        print(f"sql {sql}")
        cur.execute(sql, (group_id, group_name, members_count,))
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
