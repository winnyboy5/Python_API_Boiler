from mods.users import (UserResource)
from mods.auth import (SignupApi, LoginApi, ForgotPassword, ResetPassword)


def load_routes(route):
    
    route.add_resource(SignupApi, '/auth/signup')
    route.add_resource(LoginApi, '/auth/login')

    route.add_resource(ForgotPassword, '/auth/forgot')
    route.add_resource(ResetPassword, '/auth/reset')

    route.add_resource(UserResource, '/user/<int:user_id>')

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
