import MySQLdb
import os
import os.path
import sys


def setPosts(id, title, date, updated, tags, content):
    base_path = os.path.split(os.path.realpath(sys.argv[0]))[0]
    base_path = base_path + "/source/_posts/"
    f = open(base_path + str(id) + '.md', 'w')
    f.write('---\n')
    f.write('title: "' + str(title) + '"\n')
    f.write('date: ' + str(date) + '\n')
    f.write('updated: ' + str(updated) + '\n')
    # f.write('comments: true' + '\n')
    f.write('tags: ["' + str(tags) + '"]\n')
    f.write('---\n')
    f.write('{% raw %}\n')
    f.write(str(content) + '\n')
    f.write('{% endraw %}\n')


def getPosts():
    try:
        conn = MySQLdb.connect(
                host='10.1.XX.XX',
                port=3306,
                user='root',
                passwd='gta@2015',
                db='lag',
        )
        cur = conn.cursor()
        cur.execute('SET NAMES UTF8')
        sql = "SELECT tasks.id,tasks.title,tasks.end_at,tasks.updated_at,group_concat(DISTINCT tags.topic SEPARATOR '\",\"') as tags,tasks.content FROM tasks LEFT JOIN task_tags ON task_tags.task_id = tasks.id LEFT JOIN tags ON task_tags.tag_id = tags.id WHERE tasks.deleted_at is NULL and tasks.price > 0 and tasks.user_id=9 GROUP BY tasks.id"
        cur.execute(sql)
        posts = cur.fetchall()
        # print(posts)
        for post in posts:
            setPosts(post[0], post[1], post[2], post[3], post[4], post[5])
            print post[0]
        cur.close()
        conn.close()
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])


getPosts()
