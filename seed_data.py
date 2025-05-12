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
    name="Texarkana",
    address="9978 Farm Market Rd 3129,Queen City",
    state="Texas",
    country="USA"
)
db.session.add(plant)

# --- Functional Locations ---
fl_data = [
    ("GPI-MILL01", "Graphics Packaging Mill 01", None, "A", "PLANT"),
    ("GPI-MILL01-UTL", "Utilities", "GPI-MILL01", "B", "AREA"),
    ("GPI-MILL01-UTL-CMP", "Compressed Air", "GPI-MILL01-UTL", "C", "SYSTEM"),
    ("GPI-MILL01-UTL-WTR", "Water Treatment", "GPI-MILL01-UTL", "C", "SYSTEM"),
    ("GPI-MILL01-STK", "Stock Preparation", "GPI-MILL01", "B", "AREA"),
    ("GPI-MILL01-STK-PLP", "Pulping", "GPI-MILL01-STK", "C", "SYSTEM"),
    ("GPI-MILL01-STK-RFN", "Refining", "GPI-MILL01-STK", "C", "SYSTEM"),
    ("GPI-MILL01-PM", "Paper Machine", "GPI-MILL01", "B", "AREA"),
    ("GPI-MILL01-PM-WET", "Wet End", "GPI-MILL01-PM", "C", "SYSTEM"),
    ("GPI-MILL01-PM-PRS", "Press Section", "GPI-MILL01-PM", "C", "SYSTEM"),
    ("GPI-MILL01-FIN", "Finishing", "GPI-MILL01", "B", "AREA"),
    ("GPI-MILL01-FIN-WND", "Winding", "GPI-MILL01-FIN", "C", "SYSTEM"),
    ("GPI-MILL01-FIN-PKG", "Packaging", "GPI-MILL01-FIN", "C", "SYSTEM")
]

functional_locations = []
for fl_id, desc, parent, indicator, category in fl_data:
    fl = FunctionalLocation(
        fl_id=fl_id,
        plant_id="GPI-MILL01",
        parent_fl_id=parent,
        structure_indicator=indicator,
        category=category,
        cost_center=f"CC-{fl_id.split('-')[-1]}",
        description=desc
    )
    functional_locations.append(fl)

db.session.add_all(functional_locations)



# --- Work Centers ---
work_center_descriptions = [
    "Utilities Mechanical", "Utilities Electrical", "Utilities Chemical",
    "Stock Prep Mechanical", "Stock Prep Electrical",
    "Paper Machine Mechanical", "Paper Machine Electrical",
    "Finishing Mechanical", "Finishing Electrical",
    "Boiler Operations", "Water Treatment", "Waste Management",
    "Maintenance General", "Instrumentation", "HVAC Maintenance",
    "Lubrication Services", "Energy Management", "Safety Compliance",
    "Workshop Services", "Automation Support"
]

work_centers = []
for i, desc in enumerate(work_center_descriptions):
    wc = WorkCenter(
        work_center_id=f"WC-{i+1:03}",
        description=desc,
        cost_center=f"CC-WC-{i+1:03}",
        rate_per_hour=85 + (i % 5) * 2,  # Rate variation
        capacity_hours_per_day=24 if "Mechanical" in desc or "Electrical" in desc else 16,
        responsible_person=f"{desc.split()[0]} Lead"
    )
    work_centers.append(wc)

db.session.add_all(work_centers)



# --- Equipment ---
from datetime import date, timedelta

equipment_data = [
    ("Air Compressor 1", "GPI-MILL01-UTL-CMP", "AC187632", "Atlas Copco", "GA132"),
    ("Air Compressor 2", "GPI-MILL01-UTL-CMP", "AC187633", "Atlas Copco", "GA132"),
    ("Air Dryer System", "GPI-MILL01-UTL-CMP", "AD45981", "SPX FLOW", "HRD-2400"),
    ("Distribution Manifold", "GPI-MILL01-UTL-CMP", "DM10043", "Custom", "N/A"),
    ("Primary Clarifier", "GPI-MILL01-UTL-WTR", "PC78932", "Veolia", "CL-2000"),
    ("Sand Filter", "GPI-MILL01-UTL-WTR", "SF45612", "Evoqua", "SF-300"),
    ("Reverse Osmosis Unit", "GPI-MILL01-UTL-WTR", "RO67891", "Pentair", "X-Flow"),
    ("Chemical Dosing System", "GPI-MILL01-UTL-WTR", "CD34567", "ProMinent", "Beta"),
    ("Pulper", "GPI-MILL01-STK-PLP", "PU78901", "Andritz", "FibreSolve"),
    ("Agitator", "GPI-MILL01-STK-PLP", "AG56789", "Milton Roy", "MixMaster"),
    ("HD Cleaner", "GPI-MILL01-STK-PLP", "HD34521", "Kadant", "SelectaFlot"),
    ("Pulp Transfer Pump", "GPI-MILL01-STK-PLP", "PP67892", "Sulzer", "APT"),
    ("Disk Refiner 1", "GPI-MILL01-STK-RFN", "DR98761", "Valmet", "OptiFiner"),
    ("Disk Refiner 2", "GPI-MILL01-STK-RFN", "DR98762", "Valmet", "OptiFiner"),
    ("Consistency Controller", "GPI-MILL01-STK-RFN", "CC45678", "Metso", "Smartrac"),
    ("Refiner Feed Pump", "GPI-MILL01-STK-RFN", "RF56789", "Sulzer", "MCE"),
    ("Headbox", "GPI-MILL01-PM-WET", "HB87654", "Valmet", "OptiFlo"),
    ("Forming Section", "GPI-MILL01-PM-WET", "FS76543", "Valmet", "OptiFormer"),
    ("Trim Squirt System", "GPI-MILL01-PM-WET", "TS45678", "Kadant", "AquaEdge"),
    ("Breast Roll", "GPI-MILL01-PM-WET", "BR87651", "Valmet", "BR-550"),
    ("First Press", "GPI-MILL01-PM-PRS", "FP76543", "Valmet", "OptiPress"),
    ("Second Press", "GPI-MILL01-PM-PRS", "SP76544", "Valmet", "OptiPress"),
    ("Press Felt", "GPI-MILL01-PM-PRS", "PF98761", "Albany", "Seam"),
    ("Uhle Box", "GPI-MILL01-PM-PRS", "UB87651", "Kadant", "VacuFoil"),
    ("Winder", "GPI-MILL01-FIN-WND", "WD87652", "Valmet", "OptiWin"),
    ("Slitter", "GPI-MILL01-FIN-WND", "SL76548", "Valmet", "OptiSlice"),
    ("Core Loader", "GPI-MILL01-FIN-WND", "CL56782", "Valmet", "AutoCore"),
    ("Roll Ejector", "GPI-MILL01-FIN-WND", "RE98723", "Valmet", "RollOut"),
    ("Wrapper", "GPI-MILL01-FIN-PKG", "WR78965", "BW Papersystems", "G-2000"),
    ("Labeler", "GPI-MILL01-FIN-PKG", "LB65489", "Markem-Imaje", "2200"),
    ("Strapping Machine", "GPI-MILL01-FIN-PKG", "SM98732", "Mosca", "RO-M"),
    ("Conveyor System", "GPI-MILL01-FIN-PKG", "CV87621", "Intralox", "Series 400"),
]

equipments = []
for i, (desc, fl_id, serial, manufacturer, model) in enumerate(equipment_data):
    eq = Equipment(
        equipment_id=f"EQ-{i+1:03}",  # original ID style
        fl_id=fl_id,
        equipment_description=desc,
        serial_number=serial,
        manufacturer=manufacturer,
        model=model,
        install_date=date(2020, 1, 1) + timedelta(days=i * 25),
        last_service_at=date(2024, 5, 1),
        criticality="A" if i % 4 == 0 else "B"
    )
    equipments.append(eq)

db.session.add_all(equipments)

# --- Users ---
user_names = [
    "Alice Smith", "Bob Johnson", "Clara Lee", "David Wilson", "Eva Davis",
    "Frank Garcia", "Grace Patel", "Henry Kim", "Ivy Nguyen", "Jack Martinez",
    "Karen Chen", "Leo Brown", "Maya Lopez", "Noah Clark", "Olivia Wright",
    "Paul Scott", "Quinn Walker", "Rita Young", "Sam Turner", "Tina Green"
]

users = []
roles = ["technician", "engineer", "general"]

for i in range(20):
    u = User(
        user_id=i + 1,
        name=user_names[i],
        role=roles[i % len(roles)]
    )
    users.append(u)

db.session.add_all(users)


material_names = [
    "Compressor Oil", "Filter Cartridge", "Gasket Set", "Bearing Grease", "Pump Seal Kit",
    "Pressure Gauge", "Hydraulic Fluid", "Lubricant Spray", "Electrical Tape", "Fuse Box",
    "Cooling Fan", "Motor Brushes", "Conveyor Belt", "Sensor Module", "Timing Belt",
    "Insulation Wrap", "Clamp Set", "Grease Gun", "Voltage Regulator", "Flow Meter"
]

materials = []
for i, name in enumerate(material_names):
    m = Material(
        material_id=i+1,
        name=name,
        lead_time=1 + (i % 5),
        cost=10.0 + i,
        unit_of_measure="Each",
        material_type="spares" if i % 2 == 0 else "non_value"
    )
    materials.append(m)
db.session.add_all(materials)


# --- Tools ---
tool_names = [
    "Torque Wrench", "Multimeter", "Digital Caliper", "Vibration Analyzer", "Laser Tachometer",
    "Hydraulic Jack", "Borescope", "Pressure Tester", "Infrared Thermometer", "Megger",
    "Allen Key Set", "Electric Drill", "Pipe Wrench", "Micrometer", "Screwdriver Set",
    "Oscilloscope", "Clamp Meter", "Fluke Tester", "Thermal Camera", "Label Printer"
]

tools = []
for i, name in enumerate(tool_names):
    t = Tool(
        tool_id=i+1,
        name=name,
        quantity=5 + (i % 3),
        serial_no=f"T-{i+1:03}",
        last_calibrated=date(2024, 1, 1) + timedelta(days=i)
    )
    tools.append(t)
db.session.add_all(tools)


# --- Task Lists and Operations ---
task_descriptions = [
    ("Air Compressor Preventive Maintenance", "CMPR"),
    ("Air Compressor Corrective Maintenance", "CMPR"),
    ("Pump Preventive Maintenance", "PUMP"),
    ("Pump Repair", "PUMP"),
    ("Refiner Preventive Maintenance", "REFN"),
    ("Paper Machine Wet End PM", "PMWET"),
    ("Press Section Preventive Maintenance", "PMPRS"),
    ("Winder Preventive Maintenance", "WIND"),
    ("Electrical Equipment Preventive Maintenance", "ELEC"),
    ("Chemical Feed System Check", "CHEM"),
    ("Sand Filter Maintenance", "WTR"),
    ("Reverse Osmosis Cleaning", "WTR"),
    ("Pulper Drive Inspection", "PLP"),
    ("Headbox Sensor Calibration", "PMWET"),
    ("Roll Ejector PM", "WIND"),
    ("Strapping Machine Maintenance", "PKG"),
    ("Trim Squirt System Flush", "PMWET"),
    ("Hydraulic Pressure Check", "PMPRS"),
    ("Felt Tensioning Procedure", "PMPRS"),
    ("Label Printer Cleaning", "PKG"),
]

task_lists = []
operations = []

for i in range(20):
    task_list_id = f"TL-{i+1:03}"
    description, category = task_descriptions[i]
    tl = TaskList(
        task_list_id=task_list_id,
        description=description,
        equipment_category=category,
        work_center_id=work_centers[i % len(work_centers)].work_center_id,
        operation_count=3,
        status="Active"
    )
    task_lists.append(tl)

    for j in range(3):
        op = TaskListOperation(
            task_list_id=task_list_id,
            operation_number=f"00{j+1}",
            description=f"Step {j+1} - {description.split()[0]}",
            duration_hours=1.0 + j,
            num_persons=1,
            qualification_required="MECH-L1" if j < 2 else "MECH-L2"
        )
        operations.append(op)

db.session.add_all(task_lists)
db.session.add_all(operations)


# --- Maintenance Plans ---
plan_descriptions = [
    "Air Compressor Quarterly PM",
    "Air Compressor Annual Service",
    "Pump Monthly Inspection",
    "Refiner Weekly Inspection",
    "Refiner Performance-Based Maintenance",
    "Paper Machine Wet End Daily Check",
    "Headbox Monthly Maintenance",
    "Press Section Weekly PM",
    "Winder Bi-Weekly Check",
    "Electrical Systems Monthly Audit",
    "Chemical Feed System Calibration",
    "Stock Prep Line Vibration Check",
    "Vacuum System Pressure Test",
    "Forming Fabric Inspection",
    "Sand Filter Backwash PM",
    "Labeler Sensor Alignment Check",
    "Wrapper Belt Tension Audit",
    "Core Loader Roller Check",
    "Reverse Osmosis Pre-filter Replacement",
    "Water Treatment System Flush"
]

plans = []
for i in range(20):
    p = MaintenancePlan(
        plan_id=i+1,
        description=plan_descriptions[i],
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
import random

# --- M2M Relationships ---
for i in range(20):
    plan_id = plans[i].plan_id

    # Assign 4 to 5 random materials
    material_ids = random.sample([m.material_id for m in materials], k=random.randint(4, 5))
    for mid in material_ids:
        db.session.add(MaintenancePlanMaterial(plan_id=plan_id, material_id=mid))

    # Assign 4 to 5 random tools
    tool_ids = random.sample([t.tool_id for t in tools], k=random.randint(4, 5))
    for tid in tool_ids:
        db.session.add(MaintenancePlanTool(plan_id=plan_id, tool_id=tid))

    # Assign exactly 1 user (same as before)
    db.session.add(MaintenancePlanUser(plan_id=plan_id, user_id=users[i].user_id))


# --- Work Orders ---

# Realistic unplanned work order descriptions
unplanned_descriptions = [
    "Pump seal failure detected",
    "Unexpected drop in air compressor pressure",
    "Refiner vibration exceeds threshold",
    "Oil leak in hydraulic system",
    "Paper break in press section",
    "Burnt electrical panel fuse",
    "Overheating in chemical dosing unit",
    "Reverse osmosis pump not priming",
    "Core loader jam during shift",
    "Winder stopped due to tension issues"
]

for i in range(10):
    db.session.add(WorkOrder(
        work_order_id=f"WO-{1000+i}",
        maintenance_plan_id=plans[i].plan_id,
        equipment_id=plans[i].equipment_id,
        type="planned",
        priority=["High", "Medium", "Low"][i % 3],
        description=f'Work Order for "{plans[i].description}"',
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
        equipment_id=equipments[i % 20].equipment_id,
        priority=["High", "Medium", "Low"][i % 3],
        description=unplanned_descriptions[i - 10],
        status="inprogress",
        estimated_cost=300 + i * 10,
        estimated_time_hours=3 + (i % 3),
        assigned_to=users[i % 20].user_id,
        material_availability="partial",
        steps_to_complete="Shutdown > Inspect > Fix > Restart"
    ))


# --- Notifications ---
notification_descriptions = [
    "Unusual noise detected in pump system",
    "Temperature spike in compressor unit",
    "Low pressure warning in filter assembly",
    "Hydraulic fluid level below threshold",
    "Motor vibration exceeds safe limits",
    "Control panel showing fault code 17",
    "Scheduled inspection due for press section",
    "Unexpected stop in forming section",
    "Routine lubrication overdue",
    "Sensor calibration required",
    "Oil discoloration found during routine check",
    "Seal wear noted on agitator shaft",
    "Air leak near manifold detected",
    "Water flow inconsistency in clarifier",
    "Pump running intermittently",
    "Strange odor near chemical dosing area",
    "Emergency stop triggered in finishing unit",
    "Bearing overheating observed",
    "Electrical short in panel box",
    "Manual override engaged in winding system"
]

for i in range(20):
    db.session.add(Notification(
        notification_id=f"NT-{i+1:03}",
        raised_by=users[i % 20].user_id,
        description=notification_descriptions[i]
    ))

# --- Finalize ---
db.session.commit()
print("✅ Seed data with 20 records in all tables loaded successfully.")
