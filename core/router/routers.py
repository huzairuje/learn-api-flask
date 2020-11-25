import core.controllers.base as base_controller


class Router:
    @staticmethod
    def run(app):
        @app.route('/', methods=['GET'])
        def home():
            return base_controller.home()

        @app.route('/internal-server-error', methods=['GET'])
        def internal_server_error():
            return base_controller.internal_server_error()
