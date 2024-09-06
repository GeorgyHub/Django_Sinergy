from django.urls import path, include
from News.views import HomeNews, NewsByCategory, ViewNews, AddNews, register, user_login, user_logout
# from News.views import index, get_category, view_news, add_news

urlpatterns = [
    # path('', index, name='Home'),
    path('', HomeNews.as_view(), name='Home'),
    # path('category/<int:category_id>', get_category, name='Category'),
    path('category/<int:category_id>', NewsByCategory.as_view(), name='Category'),
    #path('news/<int:news_id>', view_news, name='view_news'),
    path('news/<int:pk>', ViewNews.as_view(), name='view_news'),
    # path('news/add_new', add_news, name='add_news')
    path('news/add_new', AddNews.as_view(), name='add_news'),
    path('register/', register, name='Register'),
    path('login/', user_login, name='Login'),
    path('logout/', user_logout, name='Logout'),
]
