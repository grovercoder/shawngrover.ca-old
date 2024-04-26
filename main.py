import uvicorn
import os
from src.email import SiteEmail
from src.webserver import WebServer

from dotenv import load_dotenv
load_dotenv()

# for troubleshooting the email tool
# email = SiteEmail(debug=True)
# email.send('test', 'test@example.com', 'testing')

# set up the web server
server = WebServer()
app = server.get_app()

if __name__ == "__main__":
    port = int(os.environ.get('WEB_PORT', 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
