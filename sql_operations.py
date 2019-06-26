import sqlite3
"""Операции для работы с базой данных"""
def m_sql(date):
    """Данная функция выводит информацию о фильме за введённую дату"""
    con = sqlite3.connect('D:/Flask_diplom/archives.db')
    cur = con.cursor()
    cur.execute('select "M_NAME" from "movies" where "DATE"=?;',[date])
    res = cur.fetchall()
    cur.close()
    con.close()
    return res[0][0]

def w_sql(date):
    """Данная функция выводит информацию о температуре в Минске(погода) за введённую дату"""
    con = sqlite3.connect('D:/Flask_diplom/archives.db')
    cur = con.cursor()
    cur.execute('select "TEMP" from "weather" where "DATE"=?;',[date])
    res = cur.fetchall()
    cur.close()
    con.close()
    return res[0][0]

def c_sql(date):
    """Данная функция выводит информацию о курсе доллара и евро за введённую дату"""
    con = sqlite3.connect('D:/Flask_diplom/archives.db')
    cur = con.cursor()
    cur.execute('select "USD","EUR" from "courses" where "DATE"=?;',[date])
    res = cur.fetchall()
    cur.close()
    con.close()
    return res[0]





