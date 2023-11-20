from rest_framework import routers

from api.views import BookViewSet, LibUserViewSet, RentBookViewSet


router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'users', LibUserViewSet)
router.register(r'rentbooks', RentBookViewSet)
