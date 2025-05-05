from app import socketio
from flask import current_app
from flask_socketio import emit
from app.models import Packet

@socketio.on('connect')
def handle_connect():
    emit('protocol_update', get_protocol_stats())

def get_protocol_stats():
    stats = {
        'TCP': Packet.query.filter_by(protocol='TCP').count(),
        'UDP': Packet.query.filter_by(protocol='UDP').count(),
        'ICMP': Packet.query.filter_by(protocol='ICMP').count(),
        'Other': Packet.query.filter(Packet.protocol.notin_(['TCP', 'UDP', 'ICMP'])).count()
    }
    return stats

def broadcast_protocol_update():
    with current_app.app_context():
        socketio.emit('protocol_update', get_protocol_stats())