from fasthtml.common import fast_app, Titled, serve, Link
from components import add_message, render_content, render_message_list


app, routes = fast_app(
    hdrs=(Link(rel="icon", type="assets/x-icon", href="/blog/assets/favicon.png"),)
)


@routes("/")
def homepage():
    return Titled('CodeChat 💬', render_content())

@routes('/submit-message', methods=["POST"])
def post(name: str, message: str):
    add_message(name, message)
    return render_message_list()

serve()