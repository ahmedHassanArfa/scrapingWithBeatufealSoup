from pymongo import MongoClient

class storeTargetItemsToDB():

    def storeTargetItemsToDB(self, itemsList, order, db, webSite):

        for item in list(itemsList):
            if not item.get_text().strip():
                continue
            if item.name == "script":
                continue
            print(item.get_text())
            print('\n')
            # save in db
            result = db.text.update_one(
                {"webSite": webSite, "order": order},
                {
                    "$set": {
                        "target.text": item.get_text()
                    }
                }
            )
            order = order + 1

        return