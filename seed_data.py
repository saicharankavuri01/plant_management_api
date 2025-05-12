# seed_data_full.py

from app import create_app, db
from app.models import *
from datetime import date, timedelta

app = create_app()
app.app_context().push()

db.drop_all()
db.create_all()

# --- Maintenance Plant ---
plant = MaintenancePlant(
    plant_id="GPI-MILL01",
    name="Graphics Packaging Mill 01",
    address="123 Mill Rd, GA",
    state="Georgia",
    country="USA"
)
db.session.add(plant)

# --- Functional Locations ---
functional_locations = []
for i in range(20):
    fl = FunctionalLocation(
        fl_id=f"FL-{i+1:03}",
        fl_name=f"Location {i+1}",
        plant_id="GPI-MILL01",
        parent_fl_id="FL-001" if i != 0 else None,
        structure_indicator=chr(65 + (i % 3)),
        category="SYSTEM" if i % 3 == 0 else "AREA",
        cost_center=f"CC10{i:02}",
        description=f"Functional Location {i+1} Description"
    )
    functional_locations.append(fl)
db.session.add_all(functional_locations)

# --- Work Centers ---
work_centers = []
for i in range(20):
    wc = WorkCenter(
        work_center_id=f"WC-{i+1:03}",
        description=f"Work Center {i+1}",
        cost_center=f"CC-WC-{i+1:03}",
        rate_per_hour=75 + i,
        capacity_hours_per_day=8 + (i % 3),
        responsible_person=f"Person {i+1}"
    )
    work_centers.append(wc)
db.session.add_all(work_centers)

# --- Equipment ---
equipments = []
for i in range(20):
    eq = Equipment(
        equipment_id=f"EQ-{i+1:03}",
        fl_id=functional_locations[i % len(functional_locations)].fl_id,
        equipment_description=f"Equipment {i+1}",
        serial_number=f"SN-{1000+i}",
        manufacturer=f"Make {i+1}",
        model=f"Model {i+1}",
        install_date=date(2020, 1, 1) + timedelta(days=i*30),
        last_service_at=date(2024, 5, 1),
        criticality="A" if i % 3 == 0 else "B"
    )
    equipments.append(eq)
db.session.add_all(equipments)

# --- Users ---
users = []
for i in range(20):
    u = User(
        user_id=i+1,
        name=f"User {i+1}",
        role=["technician", "engineer", "general"][i % 3]
    )
    users.append(u)
db.session.add_all(users)

# --- Materials ---
materials = []
for i in range(20):
    m = Material(
        material_id=i+1,
        name=f"Material {i+1}",
        lead_time=1 + (i % 5),
        cost=10.0 + i,
        unit_of_measure="Each",
        material_type="spares" if i % 2 == 0 else "non_value"
    )
    materials.append(m)
db.session.add_all(materials)

# --- Tools ---
tools = []
for i in range(20):
    t = Tool(
        tool_id=i+1,
        name=f"Tool {i+1}",
        quantity=5 + (i % 3),
        serial_no=f"T-{i+1:03}",
        last_calibrated=date(2024, 1, 1) + timedelta(days=i)
    )
    tools.append(t)
db.session.add_all(tools)

# --- Task Lists and Operations ---
task_lists = []
operations = []
for i in range(20):
    task_list_id = f"TL-{i+1:03}"
    tl = TaskList(
        task_list_id=task_list_id,
        description=f"Task List {i+1}",
        equipment_category="CAT-A",
        work_center_id=work_centers[i % 20].work_center_id,
        operation_count=3,
        status="Active"
    )
    task_lists.append(tl)
    for j in range(3):
        op = TaskListOperation(
            task_list_id=task_list_id,
            operation_number=f"00{j+1}",
            description=f"Step {j+1} for TL-{i+1}",
            duration_hours=1.0 + j,
            num_persons=1,
            qualification_required="MECH-L1"
        )
        operations.append(op)
db.session.add_all(task_lists)
db.session.add_all(operations)

# --- Maintenance Plans ---
plans = []
for i in range(20):
    p = MaintenancePlan(
        plan_id=i+1,
        description=f"Plan {i+1}",
        equipment_id=equipments[i].equipment_id,
        fl_id=equipments[i].fl_id,
        frequency_type="Calendar",
        frequency_value=3,
        frequency_unit="Months",
        offset=0,
        strategy="Time-Based",
        work_center_id=work_centers[i % 20].work_center_id,
        task_list_id=task_lists[i].task_list_id,
        is_active=True,
        last_executed_at=date(2024, 5, 1),
        next_due_date=date(2024, 8, 1)
    )
    plans.append(p)
db.session.add_all(plans)
db.session.commit()

# --- M2M Relationships ---
for i in range(20):
    db.session.add(MaintenancePlanMaterial(plan_id=plans[i].plan_id, material_id=materials[i].material_id))
    db.session.add(MaintenancePlanTool(plan_id=plans[i].plan_id, tool_id=tools[i].tool_id))
    db.session.add(MaintenancePlanUser(plan_id=plans[i].plan_id, user_id=users[i].user_id))

# --- Work Orders ---
for i in range(10):
    db.session.add(WorkOrder(
        work_order_id=f"WO-{1000+i}",
        maintenance_plan_id=plans[i].plan_id,
        equipment_id=plans[i].equipment_id,  # ✅ Add equipment_id from the plan
        type="planned",
        priority="High" if i % 2 == 0 else "Medium",
        description=f"Work Order {i+1}",
        status="released",
        estimated_cost=100 + i * 10,
        estimated_time_hours=2 + (i % 4),
        assigned_to=users[i].user_id,
        material_availability="available"
    ))

for i in range(10, 20):
    db.session.add(WorkOrder(
        work_order_id=f"WO-{1000+i}",
        type="unplanned",
        equipment_id=equipments[i % 20].equipment_id,  # ✅ Add equipment_id manually for unplanned
        priority="Critical",
        description=f"Emergency WO {i+1}",
        status="inprogress",
        estimated_cost=300 + i * 10,
        estimated_time_hours=3 + (i % 3),
        assigned_to=users[i % 20].user_id,
        material_availability="partial",
        steps_to_complete="Shutdown > Inspect > Fix > Restart"
    ))

# --- Notifications ---
for i in range(20):
    db.session.add(Notification(
        notification_id=f"NT-{i+1:03}",
        raised_by=users[i % 20].user_id,
        description=f"Notification {i+1} for equipment issue."
    ))

# --- Finalize ---
db.session.commit()
print("✅ Seed data with 20 records in all tables loaded successfully.")
