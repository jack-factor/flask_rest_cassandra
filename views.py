from models import User


class ViewUser():

    def getList():
        users = User.getList()
        result = []
        for item in users:
            result.append({'_id': item.id,
                           'email': item.email,
                           'name': item.name,
                           'lastname': item.lastname,
                           'phone': item.phone})
        return result

    def getByID(pk):
        user = User.getByID(pk)
        result = {'email': user.email,
                  'name': user.name,
                  'lastname': user.lastname,
                  'phone': user.phone}
        return result

    def save(args):
        return User.save(args)

    def update(args):
        return User.update(args)

    def deleteByID(args):
        return User.delete(args)
