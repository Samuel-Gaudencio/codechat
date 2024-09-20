import os
from datetime import datetime
import pytz
from supabase import create_client
from dotenv import load_dotenv
from fasthtml.common import *

load_dotenv()

TIMESTAMP_FMT = "%Y-%m-%d %H:%M:%S %p UTC-3"

supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))



def render_form():
    form = Form(
        Fieldset(
            Input(
                type="text",
                name="name",
                placeholder="Nome",
                required=True,
                maxlength=20
            ),
            Input(
                type="text",
                name="message",
                placeholder="Mensagem",
                required=True,
                maxlength=100
            ),
            Button("Enviar", type="submit"),
            role="group"
        ),
        method= "post",
        hx_post='/submit-message',
        hx_target='#message-list',
        hx_swap='outerHTML',
        hx_on__after_request="this.reset()"
    )

    return form

def render_message(entry):
    return (
        Article(
            Header(f"Nome: {entry['name']}"),
            P(f"Mensagem: {entry['message']}"),
            Footer(Small(Em(f"Postado: {entry['timestamp']}")))
        ),
    )

def get_time():
    tz = pytz.timezone("America/Sao_Paulo")
    return datetime.now(tz)

def add_message(name, message):
    timestamp = get_time().strftime(TIMESTAMP_FMT)
    supabase.table("CodeChat").insert(
        {"name": name, "message": message, "timestamp": timestamp}
    ).execute()


def get_messages():
    response = (
        supabase.table("CodeChat").select("*").order("id", desc=True).execute()
    )
    return response.data

def render_message_list():
    messages = get_messages()
    return Div(
        *[render_message(entry) for entry in messages],
        id="message-list"
    )

def render_content():
    return Div(
        P("Conversa Aberta sobre Tecnologia!"),
        render_form(),
        Div(
            "Feito por by ",
            A("Samuel", href="https://www.linkedin.com/in/samuel-siqueirapy/", target="_black")
        ),
        Hr(),
        render_message_list(),
        
    )