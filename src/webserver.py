from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from .route_contact import router as ContactRouter
from .route_home import router as HomeRouter
import os

class WebServer():
    def __init__(self):
        print('initializing web server')
        self.app = FastAPI(COOKIE_SAMESITE="strict")
        self.config_cors()
        self.add_middleware()
        self.add_routes()
        self.add_static()

    def get_app(self):
        return self.app

    def config_cors(self):
        if os.environ.get('USE_CORS').lower() == 'true':
            origins = [
                f"{os.environ.get('WEB_SERVER')}:{os.environ.get('WEB_PORT', 8000)}/",
            ]

            self.app.add_middleware(
                CORSMiddleware,
                allow_origins=origins,
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"]
            )        

    def add_middleware(self):
        # self.app.add_middleware(CacheControlMiddleware, cachecontrol_max_age=3600)  # Cache files for 1 hour (3600 seconds)
        pass

    def add_routes(self):
        self.app.include_router(HomeRouter)
        self.app.include_router(ContactRouter)        

    def add_static(self):
        self.app.mount("/", StaticFiles(directory="public", html=True), name="static")
        pass
     