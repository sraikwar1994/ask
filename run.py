from ask_backend.app import create_app


if __name__ == "__main__":
    app = create_app()
    app.app_context().push()
    app.run(host="0.0.0.0")
