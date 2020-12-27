from mods.users import (UserListResource, UserResource)
from mods.auth import (SignupApi, LoginApi)


def load_routes(route):
    route.add_resource(UserListResource, '/users')
    route.add_resource(UserResource, '/user/<int:user_id>')

    route.add_resource(SignupApi, '/api/auth/signup')
    route.add_resource(LoginApi, '/api/auth/login')

    # route.add_resource(ForgotPassword, '/api/auth/forgot')
    # route.add_resource(ResetPassword, '/api/auth/reset')
    return route

# @app.route("/")
# def hello_world():
#     return jsonify(hello="world")


# @app.route("/media/<path:filename>")
# def mediafiles(filename):
#     return send_from_directory(app.config["MEDIA_FOLDER"], filename)


# @app.route("/upload", methods=["GET", "POST"])
# def upload_file():
#     if request.method == "POST":
#         file = request.files["file"]
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(app.config["MEDIA_FOLDER"], filename))
#     return f"""{''}
#     <!doctype html>
#     <title>upload new File</title>
#     <form action="" method=post enctype=multipart/form-data>
#     <p><input type=file name=file><input type=submit value=Upload>
#     </form>
#     """
