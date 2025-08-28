# Hacked down version of DALL-E Template
import reflex as rx


def index():
    return rx.center(
        rx.vstack(
            rx.heading("Reflex PoC", font_size="1.5em"),
            rx.form(
                rx.vstack(
                    rx.input(
                        id="prompt_text",
                        placeholder="Enter a prompt..",
                        size="3",
                    ),
                    rx.button(
                        "Generate Image",
                        type="submit",
                        size="3",
                    ),
                    align="stretch",
                    spacing="2",
                ),
                width="100%",
            ),
            rx.divider(),
            width="25em",
            bg="white",
            padding="2em",
            align="center",
        ),
        width="100%",
        height="100vh",
        background="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%),radial-gradient(circle at 82% 25%,rgba(33,150,243,.18),hsla(0,0%,100%,0) 35%),radial-gradient(circle at 25% 61%,rgba(250, 128, 114, .28),hsla(0,0%,100%,0) 55%)",
    )


# Add state and page to the app.
app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="medium",
        accent_color="mint",
    ),
)
app.add_page(index, title="Reflex PoC")
