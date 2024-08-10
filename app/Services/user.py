from app.Repository.user import user_profits_repository

def user_profits_service():
    return user_profits_repository()

if __name__=='__main__':
    user_profits_service()