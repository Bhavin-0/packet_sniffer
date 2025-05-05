from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models import Packet
from app import db
from datetime import datetime, timedelta
import json

# Create blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Main landing page that redirects to login"""
    return redirect(url_for('auth.login'))

@main_bp.route('/dashboard')
@login_required
def dashboard():
    try:
        # Get packet statistics
        stats = get_packet_stats()
        
        # Convert stats to JSON-safe format for JavaScript
        stats_json = json.dumps({
            'protocols': stats['protocols'],
            'hourly_traffic': stats['hourly_traffic'],
            'top_sources': [
                {
                    'ip': source[0],
                    'count': source[1],
                    'size': source[2]
                } for source in stats['top_sources']
            ]
        })
        
        return render_template(
            'dashboard.html',
            stats=stats,
            stats_json=stats_json,
            current_time=datetime.utcnow()
        )
        
    except Exception as e:
        print(f"Dashboard error: {str(e)}")
        return render_template('error.html', error_message="Failed to load dashboard"), 500

def get_packet_stats():
    """Fetch and return all packet statistics"""
    return {
        'total_packets': Packet.query.count(),
        'protocols': get_protocol_distribution(),
        'hourly_traffic': get_hourly_traffic(),
        'top_sources': get_top_sources(),
        'alerts': get_alert_count(),
        'recent_alerts': get_recent_alerts()
    }

def get_protocol_distribution():
    """Return counts by protocol type"""
    return {
        'TCP': Packet.query.filter_by(protocol='TCP').count(),
        'UDP': Packet.query.filter_by(protocol='UDP').count(),
        'ICMP': Packet.query.filter_by(protocol='ICMP').count(),
        'Other': db.session.query(Packet).filter(
            ~Packet.protocol.in_(['TCP', 'UDP', 'ICMP'])
        ).count()
    }

def get_hourly_traffic():
    """Get traffic counts for the last 24 hours"""
    hours = []
    counts = []
    
    for i in range(24):
        hour = (datetime.utcnow() - timedelta(hours=i)).strftime('%H:00')
        count = Packet.query.filter(
            Packet.timestamp >= datetime.utcnow() - timedelta(hours=i+1),
            Packet.timestamp < datetime.utcnow() - timedelta(hours=i)
        ).count()
        hours.insert(0, hour)
        counts.insert(0, count)
        
    return {'hours': hours, 'counts': counts}

def get_top_sources(limit=5):
    """Get top talking IP addresses"""
    return db.session.query(
        Packet.source_ip,
        db.func.count(Packet.source_ip).label('count'),
        db.func.sum(Packet.length).label('total_size')
    ).group_by(Packet.source_ip
    ).order_by(db.desc('count')
    ).limit(limit).all()

def get_alert_count():
    """Get count of active alerts"""
    return 0  # Implement your alert logic

def get_recent_alerts(limit=5):
    """Get recent alert notifications"""
    return []  # Implement your alert system