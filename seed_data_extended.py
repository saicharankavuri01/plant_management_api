from app import create_app, db
from app.models import *
from datetime import date

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
functional_locations = [
    FunctionalLocation(fl_id="GPI-MILL01", fl_name="Main Plant", plant_id="GPI-MILL01", parent_fl_id=None, structure_indicator="A", category="PLANT", cost_center="CC10000", description="Main Site"),
    FunctionalLocation(fl_id="GPI-MILL01-UTL", fl_name="Utilities", plant_id="GPI-MILL01", parent_fl_id="GPI-MILL01", structure_indicator="B", category="AREA", cost_center="CC10100", description="Utility Area"),
    FunctionalLocation(fl_id="GPI-MILL01-UTL-CMP", fl_name="Compressed Air", plant_id="GPI-MILL01", parent_fl_id="GPI-MILL01-UTL", structure_indicator="C", category="SYSTEM", cost_center="CC10101", description="Compressor Room"),
    FunctionalLocation(fl_id="GPI-MILL01-PM-WET", fl_name="Wet End", plant_id="GPI-MILL01", parent_fl_id="GPI-MILL01", structure_indicator="C", category="SYSTEM", cost_center="CC10300", description="Paper Machine Wet End"),
]
db.session.add_all(functional_locations)

# --- Work Centers ---
work_centers = [
    WorkCenter(work_center_id="UTL-MECH-01", description="Utilities Mechanical", cost_center="CC10100", rate_per_hour=85, capacity_hours_per_day=24, responsible_person="John Smith"),
    WorkCenter(work_center_id="PM-MECH-01", description="Paper Machine Mechanical", cost_center="CC10300", rate_per_hour=90, capacity_hours_per_day=24, responsible_person="David Wilson")
]
db.session.add_all(work_centers)

# --- Equipment ---
equipments = [
    Equipment(equipment_id="UTL-CMP-001", fl_id="GPI-MILL01-UTL-CMP", equipment_description="Air Compressor 1", serial_number="AC187632", manufacturer="Atlas Copco", model="GA132", install_date=date(2019,5,12), last_service_at=date(2024,5,1), criticality="A"),
    Equipment(equipment_id="PM-WET-001", fl_id="GPI-MILL01-PM-WET", equipment_description="Headbox", serial_number="HB87654", manufacturer="Valmet", model="OptiFlo", install_date=date(2021,2,10), last_service_at=date(2024,4,15), criticality="A")
]
db.session.add_all(equipments)

# --- Task Lists ---
task_lists = [
    TaskList(task_list_id="TL-COMP-PM01", description="Air Compressor PM", equipment_category="CMPR", work_center_id="UTL-MECH-01", operation_count=5, status="Active"),
    TaskList(task_list_id="TL-PMWET-PM01", description="Headbox Monthly PM", equipment_category="PMWET", work_center_id="PM-MECH-01", operation_count=3, status="Active")
]
db.session.add_all(task_lists)

# --- Task List Operations ---
operations = [
    TaskListOperation(task_list_id="TL-COMP-PM01", operation_number="0010", description="Visual Inspection", duration_hours=0.5, num_persons=1, qualification_required="MECH-L1"),
    TaskListOperation(task_list_id="TL-COMP-PM01", operation_number="0020", description="Oil Level Check", duration_hours=1.0, num_persons=1, qualification_required="MECH-L1"),
    TaskListOperation(task_list_id="TL-COMP-PM01", operation_number="0030", description="Replace Filter", duration_hours=0.75, num_persons=1, qualification_required="MECH-L2"),
    TaskListOperation(task_list_id="TL-PMWET-PM01", operation_number="0010", description="Inspect Headbox", duration_hours=1.0, num_persons=1, qualification_required="MECH-L3"),
    TaskListOperation(task_list_id="TL-PMWET-PM01", operation_number="0020", description="Clean Slice Lip", duration_hours=1.5, num_persons=1, qualification_required="MECH-L2"),
    TaskListOperation(task_list_id="TL-PMWET-PM01", operation_number="0030", description="Fabric Tension Check", duration_hours=0.5, num_persons=1, qualification_required="MECH-L2"),
]
db.session.add_all(operations)

# --- Materials ---
materials = [
    Material(material_id=1, name="Compressor Oil", lead_time=5, cost=55.50, unit_of_measure="L", material_type="spares"),
    Material(material_id=2, name="Filter Cartridge", lead_time=3, cost=20.00, unit_of_measure="Each", material_type="spares"),
    Material(material_id=3, name="Cleaning Cloth", lead_time=2, cost=5.00, unit_of_measure="Each", material_type="non_value")
]
db.session.add_all(materials)

# --- Tools ---
tools = [
    Tool(tool_id=1, name="Torque Wrench", quantity=4, serial_no="TW-001", last_calibrated=date(2024,1,1)),
    Tool(tool_id=2, name="Multimeter", quantity=2, serial_no="MM-101", last_calibrated=date(2024,2,1))
]
db.session.add_all(tools)

# --- Users ---
users = [
    User(user_id=1, name="Alice Smith", role="technician"),
    User(user_id=2, name="Bob Lee", role="engineer"),
    User(user_id=3, name="Clara Doe", role="technician")
]
db.session.add_all(users)

# --- Maintenance Plans ---
plans = [
    MaintenancePlan(plan_id=1, description="Air Compressor Quarterly PM", equipment_id="UTL-CMP-001", fl_id="GPI-MILL01-UTL-CMP", frequency_type="Calendar", frequency_value=3, frequency_unit="Months", offset=0, strategy="Time-Based", work_center_id="UTL-MECH-01", task_list_id="TL-COMP-PM01", is_active=True, last_executed_at=date(2024, 3, 1), next_due_date=date(2024, 6, 1)),
    MaintenancePlan(plan_id=2, description="Headbox Monthly PM", equipment_id="PM-WET-001", fl_id="GPI-MILL01-PM-WET", frequency_type="Calendar", frequency_value=1, frequency_unit="Months", offset=0, strategy="Time-Based", work_center_id="PM-MECH-01", task_list_id="TL-PMWET-PM01", is_active=True, last_executed_at=date(2024, 4, 1), next_due_date=date(2024, 5, 1))
]
db.session.add_all(plans)
db.session.commit()

# --- M2M: Plan <-> Material ---
plan_material_links = [
    MaintenancePlanMaterial(plan_id=1, material_id=1),
    MaintenancePlanMaterial(plan_id=1, material_id=2),
    MaintenancePlanMaterial(plan_id=2, material_id=3)
]
db.session.add_all(plan_material_links)

# --- M2M: Plan <-> Tool ---
plan_tool_links = [
    MaintenancePlanTool(plan_id=1, tool_id=1),
    MaintenancePlanTool(plan_id=2, tool_id=2)
]
db.session.add_all(plan_tool_links)

# --- M2M: Plan <-> User ---
plan_user_links = [
    MaintenancePlanUser(plan_id=1, user_id=1),
    MaintenancePlanUser(plan_id=1, user_id=2),
    MaintenancePlanUser(plan_id=2, user_id=3)
]
db.session.add_all(plan_user_links)

# --- Work Orders ---
work_orders = [
    WorkOrder(
        work_order_id="WO-1001",
        maintenance_plan_id=1,
        type="planned",
        priority="High",
        description="Quarterly PM for Air Compressor 1",
        status="planning",
        estimated_cost=350.00,
        estimated_time_hours=4.0,
        assigned_to=1,
        material_availability="available"
    ),
    WorkOrder(
        work_order_id="WO-1002",
        maintenance_plan_id=2,
        type="planned",
        priority="Medium",
        description="Monthly PM for Headbox",
        status="released",
        estimated_cost=280.00,
        estimated_time_hours=3.5,
        assigned_to=3,
        material_availability="partial"
    ),
    WorkOrder(
        work_order_id="WO-1003",
        type="unplanned",
        priority="Critical",
        description="Emergency repair of leaking pipe.",
        status="inprogress",
        estimated_cost=500.00,
        estimated_time_hours=5,
        assigned_to=2,
        material_availability="not-available",
        steps_to_complete="1. Shut valve\n2. Replace damaged section\n3. Pressure test"
    )

]
db.session.add_all(work_orders)

# --- Notifications ---
notifications = [
    Notification(
        notification_id="NT-001",
        raised_by=1,
        description="Observed vibration in compressor unit."
    ),
    Notification(
        notification_id="NT-002",
        raised_by=2,
        description="Electrical panel needs inspection."
    )
]
db.session.add_all(notifications)

# --- Finalize DB ---
db.session.commit()
print("✅ Seed data including work orders and notifications loaded successfully.")
