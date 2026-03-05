def init_routes(app):

    @app.route("/")
    def home():
        return "Weather Tracker API"

    @app.route("/ingest", methods=["POST"])
    def ingest():
        return "POST ingest"

    
    @app.route("/observations", methods=["GET"])
    def list_observations():
        return "GET observations"

    
    @app.route("/observations/<id>", methods=["GET"])
    def get_observation(id):
        return f"GET observation {id}"

  
    @app.route("/observations/<id>", methods=["PUT"])
    def update_observation(id):
        return f"PUT observation {id}"

   
    @app.route("/observations/<id>", methods=["DELETE"])
    def delete_observation(id):
        return f"DELETE observation {id}"