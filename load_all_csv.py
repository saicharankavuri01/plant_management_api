import pandas as pd
from datetime import datetime
from app import create_app, db
from app.models import FunctionalLocation, FLEquipmentCombination, MaintenanceNotification, MaintenanceWorkOrder

app = create_app()
app.app_context().push()

# Load Functional Locations
df_fl = pd.read_csv("data/functional_location.csv")
for _, row in df_fl.iterrows():
    location = FunctionalLocation(
        fl_id=row['fl_id'],
        fl_name=row['fl_name'],
        plant_id=row['plant_id'],
        parent_fl_id=row['parent_fl_id'] if pd.notnull(row['parent_fl_id']) else None,
        description=row['description']
    )
    db.session.add(location)
db.session.commit()
print("✅ Functional locations loaded.")

# Load FL-Equipment Combinations
df_combo = pd.read_csv("data/fl-equipment_combination.csv")
for _, row in df_combo.iterrows():
    combo = FLEquipmentCombination(
        combination_id=row['combination_id'],
        fl_id=row['fl_id'],
        equipment_id=row['equipment_id'],
        install_date=datetime.strptime(row['install_date'], "%m/%d/%Y").date(),
        removal_date=datetime.strptime(row['removal_date'], "%m/%d/%Y").date() if pd.notnull(row['removal_date']) else None,
        is_active=row['is_active']
    )
    db.session.add(combo)
db.session.commit()
print("✅ FL-Equipment combinations loaded.")

# Load Maintenance Notifications
df_note = pd.read_csv("data/maintenance_notification.csv")
for _, row in df_note.iterrows():
    note = MaintenanceNotification(
        notification_id=row['notification_id'],
        notification_type=row['notification_type'],
        fl_id=row['fl_id'],
        equipment_id=row['equipment_id'],
        planned_unplanned=row['planned_unplanned'],
        priority=row['priority'],
        status=row['status'],
        description=row['description'],
        notification_date=datetime.strptime(row['notification_date'], "%m/%d/%Y").date()
    )
    db.session.add(note)
db.session.commit()
print("✅ Maintenance notifications loaded.")

# Load Maintenance Work Orders
df_work = pd.read_csv("data/maintenance_work_order.csv")
for _, row in df_work.iterrows():
    work = MaintenanceWorkOrder(
        work_order_id=row['work_order_id'],
        notification_id=row['notification_id'],
        description=row['description'],
        start_date=datetime.strptime(row['start_date'], "%m/%d/%Y").date(),
        end_date=datetime.strptime(row['end_date'], "%m/%d/%Y").date(),
        status=row['status'],
        planning_plant_id=row['planning_plant_id']
    )
    db.session.add(work)
db.session.commit()
print("✅ Maintenance work orders loaded.")
