# from fastapi import FastAPI, Form
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import HTMLResponse
# from fastapi.middleware.cors import CORSMiddleware

# from typing import Annotated

import uvicorn
import os
from src.email import SiteEmail
from src.webserver import WebServer

from dotenv import load_dotenv
load_dotenv()

# email = SiteEmail(debug=True)
# email.send('test', 'test@example.com', 'testing')

server = WebServer()
app = server.get_app()


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=os.environ.get('WEB_PORT', 8000))

# app = FastAPI()

# print(f"USE_CORS: {os.environ.get('USE_CORS')}")
# if os.environ.get('USE_CORS').lower() == 'true':
#     print('using CORS')
#     origins = [
#         f"{os.environ.get('WEB_SERVER')}:{os.environ.get('WEB_PORT', 8000)}/",
#     ]

#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=origins,
#         allow_credentials=True,
#         allow_methods=["*"],
#         allow_headers=["*"]
#     )

# @app.post("/contact", response_class=HTMLResponse)
# def handle_contact_request(name: Annotated[str, Form()], email: Annotated[str, Form()], message: Annotated[str, Form()]):
#     try:
#             email = SiteEmail()
#             email.send(name, email, message)
#             # send_email(name, email, message)
#             return """
# <div class="response thanks">
#     <h2>Thank you.</h2>
#     <p>Your message has been sent and I'll reply as soon as possible.</p>
# </div>
# """
#     except:
#          return """
# <div class="response error">
#     <h2>Something went wrong</h2>
#     <p>Your post was received but could not be sent along properly.</p>
#     <p>Please try again in a while.</p>
# </div>
# """
# app.mount("/", StaticFiles(directory=".", html=True), name="static")


