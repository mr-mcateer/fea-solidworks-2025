#!/usr/bin/env python3
"""
Build a Teacher Resource Binder (.docx) for the FEA SolidWorks 2025 lesson.
Prepared for Adam Kirsch, Crescent Valley High School, Corvallis, Oregon.
Clean formatting: Calibri 11pt body, dark bold headings, light gray table headers.
"""

from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from datetime import date
import os

# ============================================================
# CONFIGURATION
# ============================================================
OUTPUT_PATH = "/Users/andymcateer/Desktop/Claude Projects/01_TEACHING/Kirsch_Engineering/Lessons/FEA_SolidWorks_2025_Teacher_Binder.docx"

# Colors
CHARCOAL = RGBColor(0x2D, 0x2D, 0x2D)
DARK_GRAY = RGBColor(0x4A, 0x4A, 0x4A)
MED_GRAY = RGBColor(0x6B, 0x72, 0x80)
LIGHT_GRAY_HEX = "E8E8E8"
ALT_ROW_HEX = "F5F5F5"
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

doc = Document()

# ============================================================
# STYLES SETUP
# ============================================================
style = doc.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(11)
font.color.rgb = CHARCOAL
style.paragraph_format.space_after = Pt(6)
style.paragraph_format.line_spacing = 1.15

# Page margins
for section in doc.sections:
    section.top_margin = Cm(2.54)
    section.bottom_margin = Cm(2.54)
    section.left_margin = Cm(2.54)
    section.right_margin = Cm(2.54)

# Heading 1: dark, bold, page break before
h1 = doc.styles['Heading 1']
h1.font.name = 'Calibri'
h1.font.size = Pt(20)
h1.font.color.rgb = CHARCOAL
h1.font.bold = True
h1.paragraph_format.space_before = Pt(0)
h1.paragraph_format.space_after = Pt(12)
h1.paragraph_format.page_break_before = True

# Heading 2: dark, bold
h2 = doc.styles['Heading 2']
h2.font.name = 'Calibri'
h2.font.size = Pt(14)
h2.font.color.rgb = CHARCOAL
h2.font.bold = True
h2.paragraph_format.space_before = Pt(14)
h2.paragraph_format.space_after = Pt(6)

# Heading 3: dark gray
h3 = doc.styles['Heading 3']
h3.font.name = 'Calibri'
h3.font.size = Pt(12)
h3.font.color.rgb = DARK_GRAY
h3.font.bold = True
h3.paragraph_format.space_before = Pt(10)
h3.paragraph_format.space_after = Pt(4)


# ============================================================
# HELPERS
# ============================================================

def add_para(text, bold=False, italic=False, size=None, color=None,
             alignment=None, space_after=None, space_before=None):
    """Add a simple paragraph."""
    p = doc.add_paragraph()
    run = p.add_run(text)
    if bold:
        run.bold = True
    if italic:
        run.italic = True
    if size:
        run.font.size = Pt(size)
    if color:
        run.font.color.rgb = color
    if alignment is not None:
        p.alignment = alignment
    if space_after is not None:
        p.paragraph_format.space_after = Pt(space_after)
    if space_before is not None:
        p.paragraph_format.space_before = Pt(space_before)
    return p


def set_cell_shading(cell, hex_color):
    """Set background shading on a table cell."""
    shading = OxmlElement('w:shd')
    shading.set(qn('w:fill'), hex_color)
    shading.set(qn('w:val'), 'clear')
    cell._tc.get_or_add_tcPr().append(shading)


def add_table(headers, rows, col_widths=None):
    """Add a clean table with light gray header row."""
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Header row
    for i, header in enumerate(headers):
        cell = table.cell(0, i)
        p = cell.paragraphs[0]
        run = p.add_run(header)
        run.bold = True
        run.font.size = Pt(10)
        run.font.name = 'Calibri'
        run.font.color.rgb = CHARCOAL
        set_cell_shading(cell, LIGHT_GRAY_HEX)

    # Data rows
    for r, row_data in enumerate(rows):
        for c, cell_text in enumerate(row_data):
            cell = table.cell(r + 1, c)
            p = cell.paragraphs[0]
            run = p.add_run(str(cell_text))
            run.font.size = Pt(10)
            run.font.name = 'Calibri'
            run.font.color.rgb = CHARCOAL
            if r % 2 == 1:
                set_cell_shading(cell, ALT_ROW_HEX)

    if col_widths:
        for i, width in enumerate(col_widths):
            for row in table.rows:
                row.cells[i].width = Inches(width)

    # Small spacer after table
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return table


def add_bullets(items, bold_prefix=False):
    """Add a bulleted list."""
    for item in items:
        p = doc.add_paragraph(style='List Bullet')
        if bold_prefix and ': ' in item:
            prefix, rest = item.split(': ', 1)
            run = p.add_run(prefix + ': ')
            run.bold = True
            run.font.size = Pt(11)
            p.add_run(rest).font.size = Pt(11)
        else:
            run = p.add_run(item)
            run.font.size = Pt(11)


def add_page_break():
    doc.add_page_break()


# ============================================================
# PAGE 1 — COVER
# ============================================================
for _ in range(6):
    doc.add_paragraph()

add_para("FEA SolidWorks 2025", bold=True, size=36, color=CHARCOAL,
         alignment=WD_ALIGN_PARAGRAPH.CENTER, space_after=8)
add_para("Teacher Resource Binder", bold=True, size=20, color=DARK_GRAY,
         alignment=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)

add_para("\u2500" * 40, size=10, color=MED_GRAY,
         alignment=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)

add_para("Crescent Valley High School \u00b7 CTE Engineering",
         size=13, color=DARK_GRAY, alignment=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_para("Prepared for Adam Kirsch",
         size=13, color=DARK_GRAY, alignment=WD_ALIGN_PARAGRAPH.CENTER, space_after=6)
add_para(date.today().strftime("%B %d, %Y"),
         size=12, color=MED_GRAY, alignment=WD_ALIGN_PARAGRAPH.CENTER)


# ============================================================
# PAGE 2 — ABOUT THIS RESOURCE
# ============================================================
doc.add_heading("About This Resource", level=1)

doc.add_paragraph(
    "This lesson teaches students to predict how a 3D-printed part will behave "
    "under load using SolidWorks Simulation, then verify that prediction by printing "
    "the part and physically breaking it. The cycle is: predict, print, break, compare. "
    "Students build a custom FDM PLA material profile, run a static stress study, "
    "3D-print test specimens, perform a three-point bend test, and calculate percent "
    "error between simulation and reality."
)

doc.add_heading("Target Audience", level=2)
doc.add_paragraph(
    "High school juniors with CSWA-level SolidWorks experience. No physics background "
    "required. All necessary physics vocabulary is taught in Section 1."
)

doc.add_heading("Schedule", level=2)
doc.add_paragraph("Block schedule, 80-minute periods. Core lesson (Sections 1\u20137): 5\u20137 blocks. "
                   "Advanced investigation (Section 8): 1\u20132 additional blocks.")

doc.add_heading("Equipment", level=2)
add_bullets([
    "SolidWorks 2025 (SimulationXpress or Simulation Standard)",
    "Bambu Lab P1S 3D printer",
    "PLA filament (Sections 1\u20137)",
    "ABS filament (Section 8 only)",
    "Digital calipers, safety glasses, test rig materials",
])

doc.add_heading("Live Website", level=2)
doc.add_paragraph("https://mr-mcateer.github.io/fea-solidworks-2025/")
doc.add_paragraph(
    "The website is self-paced. Every section includes a \u201cWorking on your own?\u201d note "
    "that scaffolds prerequisites for independent learners. Advanced students who miss "
    "your lecture can navigate the full lesson without additional instruction."
)


# ============================================================
# PAGE 3 — LESSON FLOW
# ============================================================
doc.add_heading("Lesson Flow", level=1)

add_table(
    ["Phase", "Sections", "What Students Do", "Approx Time"],
    [
        ["Learn", "1\u20132", "Physics vocabulary, FEA workflow", "1\u20132 blocks"],
        ["Simulate", "3\u20134", "Setup and run simulation, read results", "1\u20132 blocks"],
        ["Build & Test", "5\u20136", "Print specimens, three-point bend test", "2\u20133 blocks"],
        ["Analyze", "7", "Compare, percent error, reflection", "1 block"],
        ["Advanced", "8", "ABS Trap investigation", "1\u20132 blocks"],
    ],
    col_widths=[1.2, 0.9, 3.0, 1.2]
)


# ============================================================
# PAGES 4-5 — QUICK REFERENCE: KEY CONTENT PER SECTION
# ============================================================
doc.add_heading("Quick Reference: Key Content Per Section", level=1)

sections_summary = [
    ("Section 1 \u2014 The Physics You Need",
     "Students learn six core terms: stress, strain, Young\u2019s Modulus, yield strength, UTS, "
     "and Factor of Safety. They read a stress-strain curve and compare PLA, PETG, and ABS "
     "using CNC Kitchen data.",
     "Three calculations with correct units and work shown."),

    ("Section 2 \u2014 What FEA Actually Does",
     "Introduces the seven-step FEA workflow and the Garbage In, Garbage Out principle. "
     "Students identify which steps are human decisions vs. computer calculations.",
     "Labeled workflow list and GIGO explanation."),

    ("Section 3 \u2014 SolidWorks Simulation Setup",
     "Step-by-step walkthrough: create a static study, assign a custom FDM PLA material "
     "profile (E=3300, Yield=40, UTS=50, \u03bd=0.35, \u03c1=1240), apply fixtures and a 50 N load, "
     "mesh, and solve.",
     "Annotated screenshots of material, fixtures, load, and recorded results."),

    ("Section 4 \u2014 Reading Results",
     "Students interpret Von Mises stress, displacement, and Factor of Safety plots. "
     "Covers singularities vs. real stress concentrations. Students record predictions "
     "before printing.",
     "Written interpretation of a classmate\u2019s simulation results."),

    ("Section 5 \u2014 Print the Specimen",
     "Controlled print parameters: 100% infill, rectilinear, 0.20 mm layers, 4 walls, "
     "210\u2013215\u00b0C, 60\u00b0C bed, flat XY orientation. Specimen labeling convention introduced.",
     "Bambu Studio screenshot and labeled specimen photos."),

    ("Section 6 \u2014 Break It: Physical Testing",
     "Three-point bend test per ASTM D790 (80\u00d710\u00d74 mm bar, 64 mm span). Students apply "
     "incremental loads, record deflection, and calculate flexural stress at failure.",
     "Completed data sheet and flexural stress calculation with work shown."),

    ("Section 7 \u2014 Compare: Predicted vs. Actual",
     "Students calculate percent error between FEA prediction and physical test, then "
     "write a reflection identifying sources of discrepancy.",
     "Comparison table, percent error, and 3\u20135 sentence reflection."),

    ("Section 8 \u2014 The ABS Trap (Advanced)",
     "Students run FEA with SolidWorks\u2019 default (injection-molded) ABS profile, test "
     "physically, and discover the large error. They create a corrected FDM ABS profile "
     "and rerun to see the error shrink.",
     "Side-by-side comparison and reflection on material assumptions."),
]

for title, summary, deliverable in sections_summary:
    doc.add_heading(title, level=2)
    doc.add_paragraph(summary)
    p = doc.add_paragraph()
    run = p.add_run("Deliverable: ")
    run.bold = True
    run.font.size = Pt(11)
    p.add_run(deliverable).font.size = Pt(11)


# ============================================================
# PAGE 6 — CUSTOM FDM PLA MATERIAL PROFILE
# ============================================================
doc.add_heading("Custom FDM PLA Material Profile", level=1)

doc.add_paragraph(
    "SolidWorks\u2019 built-in PLA assumes injection-molded properties. FDM-printed PLA at "
    "100% infill has different values due to layer bonding, voids, and raster orientation. "
    "Students must create a custom material with these values:"
)

add_table(
    ["Property", "Value", "Units"],
    [
        ["Young\u2019s Modulus (E)", "3,300", "MPa"],
        ["Yield Strength", "40", "MPa"],
        ["Ultimate Tensile Strength", "50", "MPa"],
        ["Poisson\u2019s Ratio (\u03bd)", "0.35", "\u2014"],
        ["Density (\u03c1)", "1,240", "kg/m\u00b3"],
    ],
    col_widths=[2.5, 1.5, 1.5]
)

doc.add_heading("Setup Steps (SolidWorks 2025)", level=2)
doc.add_paragraph("1. Simulation tab \u2192 New Study \u2192 Static \u2192 name it \u201c3pt-bend-PLA\u201d")
doc.add_paragraph("2. In the Simulation tree, right-click the part \u2192 Apply/Edit Material \u2192 Custom tab")
doc.add_paragraph("3. Enter each of the five property values above")
doc.add_paragraph("4. Save the custom material (name it \u201cFDM PLA \u2014 100% Infill\u201d)")
doc.add_paragraph("5. Apply \u2192 Close")


# ============================================================
# PAGE 7 — SOLIDWORKS 2025 SETUP NOTES
# ============================================================
doc.add_heading("SolidWorks 2025 Setup Notes", level=1)

doc.add_heading("SimulationXpress vs. Simulation Standard", level=2)

add_table(
    ["Capability", "SimulationXpress (Free)", "Simulation Standard (Paid)"],
    [
        ["Access", "Tools \u2192 SimulationXpress", "Simulation tab in CommandManager"],
        ["Part analysis", "Single body only", "Parts + assemblies"],
        ["Fixtures", "Fixed faces only", "Fixed, roller, pin, elastic support"],
        ["Loads", "Force, pressure", "Force, pressure, torque, gravity, bearing"],
        ["Mesh control", "Global size only", "Local refinement available"],
        ["Results", "Stress, displacement, FoS", "Full tensor, strain, custom plots"],
    ],
    col_widths=[1.8, 2.1, 2.4]
)

doc.add_paragraph(
    "Note: In SolidWorks 2025, SimulationXpress is under Tools \u2192 SimulationXpress "
    "(formerly under Tools \u2192 Evaluate). Simulation Standard uses the Simulation tab "
    "in CommandManager. Both work for this lesson."
)

doc.add_heading("Fixture Setup", level=2)
doc.add_paragraph(
    "Fix the two support edges or faces only. Do NOT fix the entire bottom face. "
    "Fixing too many surfaces over-constrains the part and makes it artificially stiff, "
    "producing unrealistic results."
)

doc.add_heading("Load Setup", level=2)
doc.add_paragraph(
    "Apply 50 N downward on the top face at the midpoint. This is the reference load "
    "students will replicate physically in Section 6."
)


# ============================================================
# PAGE 8 — PRINT PARAMETERS
# ============================================================
doc.add_heading("Print Parameters", level=1)

doc.add_paragraph("Required settings for Bambu Lab P1S, PLA filament:")

add_table(
    ["Parameter", "Setting", "Why"],
    [
        ["Infill density", "100%", "FEA assumes a solid, homogeneous part"],
        ["Infill pattern", "Rectilinear", "Most uniform material distribution at 100%"],
        ["Layer height", "0.20 mm", "Standard, well-characterized in published data"],
        ["Wall count", "4 minimum", "Ensures specimen edges are solid"],
        ["Nozzle temp", "210\u2013215\u00b0C", "Standard PLA range on P1S"],
        ["Bed temp", "60\u00b0C", "PLA adhesion standard"],
        ["Print speed", "80% of default or slower", "Better inter-layer adhesion"],
        ["Cooling fan", "100% after first layer", "Standard for PLA"],
        ["Orientation", "Flat on bed (XY plane)", "Bending load in-plane with layers"],
    ],
    col_widths=[1.5, 2.0, 2.8]
)

doc.add_heading("Specimen Labeling Convention", level=2)
doc.add_paragraph("Format: PLA-100-XY-02-[Initials]-[Number]")
doc.add_paragraph("Example: PLA-100-XY-02-JM-03 = PLA material, 100% infill, XY orientation, "
                   "0.2 mm layers, student JM, sample 3.")
doc.add_paragraph("Minimum 3 specimens per student or team. Let specimens sit 24 hours before testing.")


# ============================================================
# PAGE 9 — THREE-POINT BEND TEST SETUP
# ============================================================
doc.add_heading("Three-Point Bend Test Setup", level=1)

doc.add_heading("ASTM D790 Specimen Dimensions", level=2)
add_table(
    ["Dimension", "Value"],
    [
        ["Length", "80 mm"],
        ["Width (b)", "10 mm"],
        ["Depth (d)", "4 mm"],
        ["Support span (L)", "64 mm"],
        ["Span-to-depth ratio", "16:1"],
    ],
    col_widths=[2.5, 2.5]
)

doc.add_heading("Key Formulas", level=2)

doc.add_paragraph("Flexural stress at failure:")
p = doc.add_paragraph()
run = p.add_run("\u03c3f = (3 \u00b7 F \u00b7 L) / (2 \u00b7 b \u00b7 d\u00b2)")
run.bold = True
run.font.size = Pt(12)
p.paragraph_format.space_after = Pt(2)
doc.add_paragraph("F = failure force (N), L = support span (mm), b = width (mm), d = depth (mm). Result in MPa.")

doc.add_paragraph("Flexural modulus:")
p = doc.add_paragraph()
run = p.add_run("Ef = (L\u00b3 \u00b7 m) / (4 \u00b7 b \u00b7 d\u00b3)")
run.bold = True
run.font.size = Pt(12)
p.paragraph_format.space_after = Pt(2)
doc.add_paragraph("m = slope of force-deflection curve in linear region (N/mm). Result in MPa.")

doc.add_heading("Data Collection Template", level=2)
add_table(
    ["Load Step", "Applied Mass (g)", "Force F (N)", "Deflection \u03b4 (mm)", "Notes"],
    [
        ["1", "", "", "", ""],
        ["2", "", "", "", ""],
        ["3", "", "", "", ""],
        ["4", "", "", "", ""],
        ["5", "", "", "", ""],
        ["Failure", "", "", "", "Describe failure mode"],
    ],
    col_widths=[0.9, 1.3, 1.1, 1.3, 1.7]
)

doc.add_paragraph("Safety: PLA fragments can fly when specimens snap. Require safety glasses during testing.",
                   style='List Bullet')


# ============================================================
# PAGE 10 — INTERPRETING RESULTS
# ============================================================
doc.add_heading("Interpreting Results", level=1)

doc.add_heading("Percent Error Formula", level=2)
p = doc.add_paragraph()
run = p.add_run("% Error = |(Predicted \u2212 Actual) / Actual| \u00d7 100%")
run.bold = True
run.font.size = Pt(12)

doc.add_heading("Error Interpretation Ranges", level=2)
add_table(
    ["Error Range", "Interpretation"],
    [
        ["< 10%", "Strong correlation. Material assumptions and test setup well-matched."],
        ["10\u201320%", "Acceptable. Typical for FDM parts due to manufacturing variability."],
        ["20\u201335%", "Investigate. Likely material mismatch, print defects, or fixture issues."],
        ["> 35%", "Something is fundamentally off. Re-check all assumptions."],
    ],
    col_widths=[1.3, 5.0]
)

doc.add_heading("Common Sources of Error", level=2)
add_bullets([
    "Material property values: May not match your specific filament brand or batch.",
    "Print defects: Under-extrusion, voids, poor layer adhesion weaken the real part.",
    "Fixture alignment: Supports not level or centered changes load distribution.",
    "Measurement precision: Caliper resolution, scale accuracy, identifying exact failure moment.",
    "Isotropic assumption: FEA assumes homogeneous, isotropic material; FDM prints are neither.",
    "Environmental factors: Temperature and humidity during printing and testing.",
], bold_prefix=True)


# ============================================================
# PAGE 11 — DIFFERENTIATION
# ============================================================
doc.add_heading("Differentiation", level=1)

doc.add_heading("CORE Path (All Students)", level=2)
doc.add_paragraph("Sections 1\u20137. Every student completes the full predict-print-break-compare cycle "
                   "with PLA. 100-point rubric.")

doc.add_heading("ADVANCED Path (Motivated Students)", level=2)
doc.add_paragraph("Sections 1\u20138. Adds the ABS Trap investigation, which reveals what happens when "
                   "material assumptions are wrong. 25 bonus points.")

doc.add_heading("The ABS Trap (Section 8)", level=2)
doc.add_paragraph(
    "Section 8 is where the deepest learning happens. Students run FEA with SolidWorks\u2019 "
    "default injection-molded ABS profile, physically test FDM-printed ABS, and discover "
    "the large error. They then create a corrected FDM ABS profile and rerun. The lesson: "
    "the simulation was not wrong\u2014the material assumptions were wrong."
)

doc.add_heading("Self-Paced Scaffolding", level=2)
doc.add_paragraph(
    "Every section on the website includes a \u201cWorking on your own?\u201d note that lists "
    "prerequisites and provides enough context for independent learners to proceed "
    "without teacher instruction. Students who are absent or ahead can self-navigate."
)


# ============================================================
# PAGE 12 — ASSESSMENT OVERVIEW
# ============================================================
doc.add_heading("Assessment Overview", level=1)

doc.add_paragraph("100-point core rubric + 25 bonus points for Section 8.")

add_table(
    ["Category", "Points", "What\u2019s Assessed"],
    [
        ["Engineering Notebook", "30", "Calculations, screenshots, data recording throughout"],
        ["Simulation Screenshots", "15", "Material profile, fixtures, load, results"],
        ["Physical Test Data", "15", "Completed data sheet, flexural stress calculation"],
        ["Comparison Analysis", "25", "Percent error calculation, comparison table"],
        ["Reflection", "15", "Source-of-error analysis, improvement plan"],
        ["CORE TOTAL", "100", ""],
        ["Bonus: Section 8 (ABS Trap)", "+25", "Side-by-side comparison + written reflection"],
    ],
    col_widths=[2.2, 0.8, 3.3]
)


# ============================================================
# PAGE 13 — PROCUREMENT
# ============================================================
doc.add_heading("Procurement", level=1)

doc.add_paragraph("Materials needed and estimated costs for a class of ~30 students:")

add_table(
    ["Item", "Estimated Cost", "Notes"],
    [
        ["PLA filament", "~$20/kg", "One spool covers a full class (~3 classes total)"],
        ["ABS filament (Section 8 only)", "~$22/kg", "Optional, advanced section only"],
        ["Test rig materials", "$10\u201330", "Hardware store: steel rod, angle iron, bucket"],
        ["Safety glasses", "School supply", "Required during bend testing"],
        ["Digital calipers", "$15\u201325", "Or school supply if available"],
    ],
    col_widths=[2.2, 1.3, 2.8]
)

p = doc.add_paragraph()
run = p.add_run("Total estimated cost: $20\u201358 per class.")
run.bold = True
run.font.size = Pt(11)
doc.add_paragraph(
    "If your shop already has a 3D printer, calipers, and safety glasses, the only "
    "consumable cost is filament."
)


# ============================================================
# PAGE 14 — STANDARDS ALIGNMENT
# ============================================================
doc.add_heading("Standards Alignment", level=1)

doc.add_heading("NGSS Performance Expectations", level=2)
add_bullets([
    "HS-ETS1-1: Analyze a major global challenge \u2014 define criteria and constraints.",
    "HS-ETS1-2: Design a solution using mathematical models and simulations.",
    "HS-ETS1-3: Evaluate a solution using prioritized criteria, trade-offs, and refinement.",
    "HS-PS2-6: Mathematical expressions of Newton\u2019s second law (force/stress relationships).",
])

doc.add_heading("NGSS Science & Engineering Practices", level=2)
add_bullets([
    "Developing and using models (FEA simulation)",
    "Planning and carrying out investigations (physical testing)",
    "Analyzing and interpreting data (predicted vs. actual comparison)",
    "Using mathematics and computational thinking (stress calculations, percent error)",
])

doc.add_heading("CTE Pathways", level=2)
add_bullets([
    "Mechanical engineering",
    "Materials science",
    "CSWA-FEA certification pathway",
])


# ============================================================
# PAGE 15 — ALL RESOURCES AT A GLANCE
# ============================================================
doc.add_heading("All Resources at a Glance", level=1)

add_bullets([
    "Website: https://mr-mcateer.github.io/fea-solidworks-2025/",
    "GitHub repo: https://github.com/mr-mcateer/fea-solidworks-2025",
    ".docx binders: CORE (Sections 1\u20137) and ADVANCED (Sections 1\u20138)",
    "CNC Kitchen reference video: Stefan Hermann PLA/PETG/ABS comparison \u2014 anchor resource throughout the lesson",
])

doc.add_paragraph(
    "The website is the primary student-facing resource. The .docx binders are offline "
    "backups and can be printed. This teacher binder consolidates all instructor-facing "
    "reference material in one document."
)


# ============================================================
# SAVE
# ============================================================
doc.save(OUTPUT_PATH)
file_size = os.path.getsize(OUTPUT_PATH)
print(f"Saved: {OUTPUT_PATH}")
print(f"Size: {file_size / 1024:.1f} KB")
