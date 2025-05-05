from app import create_app, socketio
import json
app = create_app()

if __name__ == '__main__':
    socketio.run(app, debug=True)