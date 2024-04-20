from src.ui.client.views.Router import Router
from src.ui.client.views.data_view import DataView
from src.ui.client.views.index_view import IndexView
from src.ui.client.views.register_view import  RegisterView
from src.ui.client.views.login_view import  LoginView

router = Router()

router.routes = {
  "/": IndexView(),
  "/register": RegisterView(),
  "/login": LoginView(),
  "/data": DataView(),
}