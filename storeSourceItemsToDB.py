from pymongo import MongoClient

class storeSourceItemsToDB():

    def storeSourceItemsToDB(self, itemsList, order, db, webSite):

        for item in list(itemsList):
            if not item.get_text().strip():
                continue
            if item.name == "script":
                continue
            print(item.get_text())
            print('\n')
            # save in db
            result = db.text.insert_one(
                {
                    "source": {
                        "text": item.get_text()

                    },
                    "target": {
                        "text": ""

                    },
                    "order": order,
                    "webSite": webSite

                }
            )
            order = order + 1

        return