from flask import Blueprint, jsonify
from app.models import WorkOrder

bp = Blueprint("work_order_api", __name__, url_prefix="/api")

@bp.route("/get_work_orders", methods=["GET"])
def get_work_orders():
    return jsonify([
        {
            "work_order_id": w.work_order_id,
            "type": w.type,
            "maintenance_plan": w.maintenance_plan.description if w.maintenance_plan else None,
            "equipment": w.equipment.equipment_description if w.equipment else None,
            "priority": w.priority,
            "description": w.description,
            "status": w.status,
            "estimated_cost": float(w.estimated_cost) if w.estimated_cost else None,
            "estimated_time_hours": float(w.estimated_time_hours) if w.estimated_time_hours else None,
            "assigned_to": w.assigned_user.name if w.assigned_user else None,
            "material_availability": w.material_availability,
            "steps_to_complete": w.steps_to_complete
        }
        for w in WorkOrder.query.all()
    ])
