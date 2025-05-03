"""Import all routers and add them to routers_list."""
from aiogram import Router

from .example_admin import example_admin_router
from .example_echo import example_echo_router
from .example_simple_menu import example_menu_router
from .example_user import example_user_router

routers_list = [
    example_admin_router,
    example_menu_router,
    example_user_router,
    example_echo_router,  # echo_router must be last
]

master_router = Router()

master_router.include_routers(*routers_list)

__all__ = [
    "master_router",
]
