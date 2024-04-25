from fastapi import FastAPI, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, Response
from fastapi.middleware.cors import CORSMiddleware

from .contact_route import router as ContactRouter
import os

class WebServer():
    def __init__(self):
        print('initializing web server')
        self.app = FastAPI()
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
        pass
        # self.app.add_middleware(CacheControlMiddleware, cachecontrol_max_age=3600)  # Cache files for 1 hour (3600 seconds)

    def add_routes(self):
        self.app.include_router(ContactRouter)        

    def add_static(self):
        self.app.mount("/", StaticFiles(directory="public", html=True), name="static")
        pass
     