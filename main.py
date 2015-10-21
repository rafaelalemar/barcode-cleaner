from flask import Flask, render_template

# Estas credencias voce encontrara no https://code.google.com/apis/console
# usuario rafael@moontools.com.br
# Segundo as instrucoees deste link: http://stackoverflow.com/questions/9499286/using-google-oauth2-with-flask
GOOGLE_LOGIN_CLIENT_ID = "753563466893-rq70ohv414o0tcg4bsu9ri2eujngm2uv.apps.googleusercontent.com"
GOOGLE_LOGIN_CLIENT_SECRET = "S438_M7RRJYdo2URzTUvio_n"

OAUTH_CREDENTIALS={
        'google': {
            'id': GOOGLE_LOGIN_CLIENT_ID,
            'secret': GOOGLE_LOGIN_CLIENT_SECRET
        }
}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run()
