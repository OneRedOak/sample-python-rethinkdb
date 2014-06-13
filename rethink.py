import rethinkdb as r


class Rethink():
    def __init__(self):
        self.client = r.connect(host = 'localhost', port = 28015).repl()
        r.db_drop('test').run()
        r.db_create('test').run()

    def populate(self):
        r.db('test').table_create('table').run()        
        things = [
            {"name": "Vishnu"},
            {"name": "Lakshmi"},
            {"name": "Ganesha"},
            {"name": "Krishna"},
            {"name": "Murugan"}
        ]
        r.table('table').insert(things).run()

    def count(self):
        print("Table Count: " + r.table('table').get_all('name').run().count())
        return r.table('table').get_all('name').run().count()

if __name__ == "__main__":
    rethink = Rethink()
    rethink.populate()
    print(mongo.count())
