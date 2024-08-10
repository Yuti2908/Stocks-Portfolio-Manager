from app.Repository.user import user_profits_repository, add_cash_repository

def user_profits_service():
    return user_profits_repository()

if __name__=='__main__':
    user_profits_service()


def add_cash_service(added_cash):
    return add_cash_repository(added_cash)