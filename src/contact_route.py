from typing import Annotated
from fastapi import APIRouter, Form
from fastapi.responses import HTMLResponse

from src.email import SiteEmail

router = APIRouter()

@router.post("/contact", response_class=HTMLResponse)
def handle_contact_request(name: Annotated[str, Form()], email: Annotated[str, Form()], message: Annotated[str, Form()]):
    print('trying email')
    siteemail = SiteEmail()
    # siteemail.debug = True
    if siteemail.send(name, email, message):
        return """
        <div class="response thanks">
            <h2>Thank you.</h2>
            <p>Your message has been sent and I'll reply as soon as possible.</p>
        </div>
        """
    else:
        return """
        <div class="response error">
            <h2>Something went wrong</h2>
            <p>Your post was received but could not be sent along properly.</p>
            <p>Please try again in a while.</p>
        </div>
        """