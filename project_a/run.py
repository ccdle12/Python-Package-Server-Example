"""Entry Point for project_a app, serves a Flask API."""

from app import app

app.config.from_object('config.DevelopmentConfig')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
