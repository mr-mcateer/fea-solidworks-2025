#!/usr/bin/env python3
"""
Build a clean, minimal Apple-style PPTX presentation for
FEA Stress Analysis with SolidWorks 2025.

Resource deck for teacher Adam Kirsch
Crescent Valley High School, Corvallis OR — CTE Engineering

Run:  python3 build_presentation.py
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ── Colour palette ──────────────────────────────────────────────
WHITE       = RGBColor(0xFF, 0xFF, 0xFF)
CHARCOAL    = RGBColor(0x1D, 0x1D, 0x1F)
BLUE        = RGBColor(0x00, 0x71, 0xE3)
BODY_GRAY   = RGBColor(0x51, 0x51, 0x54)
LIGHT_GRAY  = RGBColor(0x86, 0x86, 0x8B)
RULE_GRAY   = RGBColor(0xD2, 0xD2, 0xD7)
TABLE_HEADER_BG = RGBColor(0xF5, 0xF5, 0xF7)
BLUE_LIGHT  = RGBColor(0xE8, 0xF0, 0xFE)

FONT = "Calibri"

# ── Slide dimensions (16:9 widescreen) ─────────────────────────
SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)

# ── Margins & grid ─────────────────────────────────────────────
LEFT_MARGIN   = Inches(0.9)
RIGHT_MARGIN  = Inches(0.9)
CONTENT_W     = SLIDE_W - LEFT_MARGIN - RIGHT_MARGIN
TOP_TITLE     = Inches(0.7)
TOP_BODY      = Inches(2.0)
BODY_H        = Inches(4.8)


# ═══════════════════════════════════════════════════════════════
# Helper functions
# ═══════════════════════════════════════════════════════════════

def set_slide_bg(slide, color=WHITE):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_textbox(slide, left, top, width, height):
    return slide.shapes.add_textbox(left, top, width, height)


def set_run(run, text, font_name=FONT, size=Pt(18), color=BODY_GRAY,
            bold=False, italic=False):
    run.text = text
    run.font.name = font_name
    run.font.size = size
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic


def add_para(tf, text, size=Pt(18), color=BODY_GRAY, bold=False,
             space_before=Pt(4), space_after=Pt(4), alignment=PP_ALIGN.LEFT,
             italic=False, level=0):
    """Append a paragraph to an existing text frame."""
    p = tf.add_paragraph()
    p.alignment = alignment
    p.space_before = space_before
    p.space_after = space_after
    p.level = level
    run = p.add_run()
    set_run(run, text, size=size, color=color, bold=bold, italic=italic)
    return p


def first_para(tf, text, size=Pt(18), color=BODY_GRAY, bold=False,
               alignment=PP_ALIGN.LEFT, space_before=Pt(0), space_after=Pt(4),
               italic=False):
    """Set the FIRST (existing) paragraph of a text frame."""
    p = tf.paragraphs[0]
    p.alignment = alignment
    p.space_before = space_before
    p.space_after = space_after
    run = p.add_run()
    set_run(run, text, size=size, color=color, bold=bold, italic=italic)
    return p


def slide_number_box(slide, num):
    """Small blue section number in top-right."""
    tb = add_textbox(slide, SLIDE_W - Inches(1.5), Inches(0.35),
                     Inches(1.0), Inches(0.4))
    first_para(tb.text_frame, f"{num:02d}",
               size=Pt(14), color=LIGHT_GRAY, alignment=PP_ALIGN.RIGHT)


def title_and_body(slide, slide_num, title_text, body_lines,
                   title_size=Pt(36), body_size=Pt(18), dash_prefix=True):
    """Standard content slide: big title + dash-prefixed body lines."""
    set_slide_bg(slide)
    slide_number_box(slide, slide_num)

    # Title
    tb = add_textbox(slide, LEFT_MARGIN, TOP_TITLE, CONTENT_W, Inches(1.0))
    tb.text_frame.word_wrap = True
    first_para(tb.text_frame, title_text,
               size=title_size, color=CHARCOAL, bold=True)

    # Thin rule
    add_rule(slide, LEFT_MARGIN, Inches(1.65), CONTENT_W)

    # Body
    tb2 = add_textbox(slide, LEFT_MARGIN, TOP_BODY, CONTENT_W, BODY_H)
    tb2.text_frame.word_wrap = True
    for i, line in enumerate(body_lines):
        prefix = "\u2013  " if dash_prefix else ""
        func = first_para if i == 0 else add_para
        func(tb2.text_frame, f"{prefix}{line}",
             size=body_size, color=BODY_GRAY,
             space_before=Pt(6), space_after=Pt(6))

    return tb, tb2


def add_rule(slide, left, top, width, color=RULE_GRAY, height=Pt(1)):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape


def add_blue_label(tf, label, text, is_first=False):
    """Add a line like '  01  Phase title — description' with blue number."""
    p = tf.add_paragraph() if not is_first else tf.paragraphs[0]
    p.space_before = Pt(10)
    p.space_after = Pt(4)

    r1 = p.add_run()
    set_run(r1, f"{label}    ", size=Pt(20), color=BLUE, bold=True)

    r2 = p.add_run()
    set_run(r2, text, size=Pt(18), color=BODY_GRAY)
    return p


def add_mixed_para(tf, parts, space_before=Pt(6), space_after=Pt(6),
                   is_first=False):
    """parts = list of (text, size, color, bold) tuples."""
    p = tf.add_paragraph() if not is_first else tf.paragraphs[0]
    p.space_before = space_before
    p.space_after = space_after
    for text, sz, clr, bld in parts:
        r = p.add_run()
        set_run(r, text, size=sz, color=clr, bold=bld)
    return p


# ═══════════════════════════════════════════════════════════════
# Build the deck
# ═══════════════════════════════════════════════════════════════

prs = Presentation()
prs.slide_width  = SLIDE_W
prs.slide_height = SLIDE_H
blank_layout = prs.slide_layouts[6]  # blank


# ── SLIDE 1 — Title ────────────────────────────────────────────
sl = prs.slides.add_slide(blank_layout)
set_slide_bg(sl)

# Main title
tb = add_textbox(sl, LEFT_MARGIN, Inches(1.8), CONTENT_W, Inches(1.5))
tb.text_frame.word_wrap = True
first_para(tb.text_frame, "Predict. Print. Break. Compare.",
           size=Pt(52), color=CHARCOAL, bold=True,
           alignment=PP_ALIGN.LEFT)

# Subtitle
tb2 = add_textbox(sl, LEFT_MARGIN, Inches(3.5), CONTENT_W, Inches(0.7))
first_para(tb2.text_frame, "FEA Stress Analysis with SolidWorks 2025",
           size=Pt(26), color=BLUE, bold=False,
           alignment=PP_ALIGN.LEFT)

# Bottom line
tb3 = add_textbox(sl, LEFT_MARGIN, Inches(6.2), CONTENT_W, Inches(0.5))
first_para(tb3.text_frame,
           "Crescent Valley High School  \u00b7  CTE Engineering",
           size=Pt(14), color=LIGHT_GRAY, alignment=PP_ALIGN.LEFT)


# ── SLIDE 2 — The Big Idea ─────────────────────────────────────
sl = prs.slides.add_slide(blank_layout)
set_slide_bg(sl)
slide_number_box(sl, 2)

tb = add_textbox(sl, LEFT_MARGIN, TOP_TITLE, CONTENT_W, Inches(1.0))
tb.text_frame.word_wrap = True
first_para(tb.text_frame, "The Big Idea",
           size=Pt(36), color=CHARCOAL, bold=True)

add_rule(sl, LEFT_MARGIN, Inches(1.65), CONTENT_W)

# Hero statement
tb2 = add_textbox(sl, LEFT_MARGIN, Inches(2.2), CONTENT_W, Inches(1.2))
tb2.text_frame.word_wrap = True
first_para(tb2.text_frame,
           "Students run an FEA simulation, 3D-print the part, "
           "physically break it, and compare prediction to reality.",
           size=Pt(24), color=CHARCOAL, bold=False)

# Sub-line
tb3 = add_textbox(sl, LEFT_MARGIN, Inches(3.8), CONTENT_W, Inches(0.6))
tb3.text_frame.word_wrap = True
first_para(tb3.text_frame,
           "One lesson.  Four phases.  Real engineering.",
           size=Pt(22), color=BLUE, bold=True)


# ── SLIDE 3 — Lesson Flow ──────────────────────────────────────
sl = prs.slides.add_slide(blank_layout)
set_slide_bg(sl)
slide_number_box(sl, 3)

tb = add_textbox(sl, LEFT_MARGIN, TOP_TITLE, CONTENT_W, Inches(1.0))
tb.text_frame.word_wrap = True
first_para(tb.text_frame, "Lesson Flow",
           size=Pt(36), color=CHARCOAL, bold=True)

add_rule(sl, LEFT_MARGIN, Inches(1.65), CONTENT_W)

tb2 = add_textbox(sl, LEFT_MARGIN, TOP_BODY, CONTENT_W, BODY_H)
tb2.text_frame.word_wrap = True

phases = [
    ("Phase 1: Learn", "Sections 1\u20132  \u2014  Physics vocab + FEA workflow"),
    ("Phase 2: Simulate", "Sections 3\u20134  \u2014  SolidWorks setup + read results"),
    ("Phase 3: Build & Test", "Sections 5\u20136  \u2014  Print specimens + 3-point bend"),
    ("Phase 4: Analyze", "Section 7  \u2014  Compare, percent error, reflection"),
    ("Advanced", "Section 8  \u2014  The ABS Trap (differentiation)"),
]
for i, (label, desc) in enumerate(phases):
    add_blue_label(tb2.text_frame, label, desc, is_first=(i == 0))


# ── SLIDE 4 — What Students Need to Know First ────────────────
sl = prs.slides.add_slide(blank_layout)
lines = [
    "Six terms: Stress, Strain, Young\u2019s Modulus, Yield Strength, UTS, Factor of Safety",
    "No physics prerequisite \u2014 all taught in Section 1",
    "The stress-strain curve is the single most important diagram",
]
title_and_body(sl, 4, "What Students Need to Know First", lines)


# ── SLIDE 5 — The Stress-Strain Curve ─────────────────────────
sl = prs.slides.add_slide(blank_layout)
set_slide_bg(sl)
slide_number_box(sl, 5)

tb = add_textbox(sl, LEFT_MARGIN, TOP_TITLE, CONTENT_W, Inches(1.0))
tb.text_frame.word_wrap = True
first_para(tb.text_frame, "The Stress-Strain Curve",
           size=Pt(36), color=CHARCOAL, bold=True)

add_rule(sl, LEFT_MARGIN, Inches(1.65), CONTENT_W)

# Four regions
tb2 = add_textbox(sl, LEFT_MARGIN, TOP_BODY, CONTENT_W, Inches(2.5))
tb2.text_frame.word_wrap = True

regions = [
    ("1  Elastic", "Proportional, fully recoverable deformation"),
    ("2  Yield", "Onset of permanent deformation"),
    ("3  Plastic", "Material deforms permanently, strain-hardens"),
    ("4  Fracture", "Ultimate failure"),
]
for i, (label, desc) in enumerate(regions):
    add_blue_label(tb2.text_frame, label, desc, is_first=(i == 0))

# Key insight
tb3 = add_textbox(sl, LEFT_MARGIN, Inches(4.7), CONTENT_W, Inches(0.8))
tb3.text_frame.word_wrap = True
p = tb3.text_frame.paragraphs[0]
p.space_before = Pt(8)
r1 = p.add_run()
set_run(r1, "Key insight:  ", size=Pt(18), color=BLUE, bold=True)
r2 = p.add_run()
set_run(r2, "slope = stiffness,  area under curve = toughness",
        size=Pt(18), color=BODY_GRAY)


# ── SLIDE 6 — Material Comparison ─────────────────────────────
sl = prs.slides.add_slide(blank_layout)
set_slide_bg(sl)
slide_number_box(sl, 6)

tb = add_textbox(sl, LEFT_MARGIN, TOP_TITLE, CONTENT_W, Inches(1.0))
tb.text_frame.word_wrap = True
first_para(tb.text_frame, "Material Comparison",
           size=Pt(36), color=CHARCOAL, bold=True)

add_rule(sl, LEFT_MARGIN, Inches(1.65), CONTENT_W)

tb2 = add_textbox(sl, LEFT_MARGIN, TOP_BODY, CONTENT_W, BODY_H)
tb2.text_frame.word_wrap = True

mats = [
    ("PLA", "Stiff, brittle, snaps clean  (3,300 MPa bending modulus)"),
    ("PETG", "Flexible, tough, stretches before failing  (1,900 MPa)"),
    ("ABS", "Impact resistant, but worst anisotropy in FDM  (2,300 MPa)"),
]
for i, (mat, desc) in enumerate(mats):
    add_blue_label(tb2.text_frame, mat, desc, is_first=(i == 0))

add_para(tb2.text_frame, "Source: CNC Kitchen data",
         size=Pt(13), color=LIGHT_GRAY, space_before=Pt(20), italic=True)


# ── SLIDE 7 — What FEA Actually Does ──────────────────────────
sl = prs.slides.add_slide(blank_layout)
set_slide_bg(sl)
slide_number_box(sl, 7)

tb = add_textbox(sl, LEFT_MARGIN, TOP_TITLE, CONTENT_W, Inches(1.0))
tb.text_frame.word_wrap = True
first_para(tb.text_frame, "What FEA Actually Does",
           size=Pt(36), color=CHARCOAL, bold=True)

add_rule(sl, LEFT_MARGIN, Inches(1.65), CONTENT_W)

# Concept bullets
tb2 = add_textbox(sl, LEFT_MARGIN, TOP_BODY, Inches(5.5), Inches(2.5))
tb2.text_frame.word_wrap = True

concepts = [
    "Computer breaks part into elements (mesh)",
    "Solves stress equations at every element",
    "Assembles full stress picture",
]
for i, c in enumerate(concepts):
    func = first_para if i == 0 else add_para
    func(tb2.text_frame, f"\u2013  {c}",
         size=Pt(18), color=BODY_GRAY,
         space_before=Pt(6), space_after=Pt(6))

# 7-step pipeline on the right side
tb3 = add_textbox(sl, Inches(7.0), TOP_BODY, Inches(5.5), Inches(4.0))
tb3.text_frame.word_wrap = True

steps = ["Geometry", "Material", "Fixtures", "Loads", "Mesh", "Solve",
         "Interpret"]
first_para(tb3.text_frame, "The 7-Step Pipeline",
           size=Pt(20), color=CHARCOAL, bold=True,
           space_after=Pt(12))

for i, step in enumerate(steps):
    clr = BLUE if i == 5 else BODY_GRAY  # highlight Solve
    bld = True if i == 5 else False
    add_para(tb3.text_frame, f"{i+1}.  {step}",
             size=Pt(17), color=clr, bold=bld,
             space_before=Pt(3), space_after=Pt(3))


# ── SLIDE 8 — GIGO ────────────────────────────────────────────
sl = prs.slides.add_slide(blank_layout)
set_slide_bg(sl)
slide_number_box(sl, 8)

tb = add_textbox(sl, LEFT_MARGIN, TOP_TITLE, CONTENT_W, Inches(1.0))
tb.text_frame.word_wrap = True
first_para(tb.text_frame, "GIGO: The Central Lesson",
           size=Pt(36), color=CHARCOAL, bold=True)

add_rule(sl, LEFT_MARGIN, Inches(1.65), CONTENT_W)

# Hero quote
tb2 = add_textbox(sl, LEFT_MARGIN, Inches(2.3), CONTENT_W, Inches(1.0))
tb2.text_frame.word_wrap = True
first_para(tb2.text_frame, "Garbage In, Garbage Out.",
           size=Pt(32), color=BLUE, bold=True)

# Body
tb3 = add_textbox(sl, LEFT_MARGIN, Inches(3.6), CONTENT_W, Inches(3.0))
tb3.text_frame.word_wrap = True
lines = [
    "6 of 7 steps are HUMAN decisions",
    "The computer only owns Step 6 (Solve)",
    "Wrong inputs = precise, beautiful, wrong answers",
]
for i, line in enumerate(lines):
    func = first_para if i == 0 else add_para
    func(tb3.text_frame, f"\u2013  {line}",
         size=Pt(20), color=BODY_GRAY,
         space_before=Pt(8), space_after=Pt(8))


# ── SLIDE 9 — SolidWorks Setup ────────────────────────────────
sl = prs.slides.add_slide(blank_layout)
lines = [
    "SimulationXpress (free) vs Simulation Standard (paid) \u2014 both work",
    "Custom FDM PLA material profile (E = 3300, Yield = 40, UTS = 50)",
    "Default library materials are wrong for 3D-printed parts",
    "Students must create their own material entry",
]
title_and_body(sl, 9, "SolidWorks Setup", lines, body_size=Pt(18))


# ── SLIDE 10 — Custom Material Profile ────────────────────────
sl = prs.slides.add_slide(blank_layout)
set_slide_bg(sl)
slide_number_box(sl, 10)

tb = add_textbox(sl, LEFT_MARGIN, TOP_TITLE, CONTENT_W, Inches(1.0))
tb.text_frame.word_wrap = True
first_para(tb.text_frame, "Custom Material Profile  \u2014  FDM PLA",
           size=Pt(36), color=CHARCOAL, bold=True)

add_rule(sl, LEFT_MARGIN, Inches(1.65), CONTENT_W)

# Build a table
rows, cols = 6, 2
tbl_shape = sl.shapes.add_table(rows, cols,
                                LEFT_MARGIN, Inches(2.2),
                                Inches(7.0), Inches(3.6))
tbl = tbl_shape.table

# Column widths
tbl.columns[0].width = Inches(3.5)
tbl.columns[1].width = Inches(3.5)

data = [
    ("Property", "Value"),
    ("Young\u2019s Modulus", "3,300 MPa"),
    ("Yield Strength", "40 MPa"),
    ("UTS", "50 MPa"),
    ("Poisson\u2019s Ratio", "0.35"),
    ("Density", "1,240 kg/m\u00b3"),
]

for r, (prop, val) in enumerate(data):
    for c, txt in enumerate([prop, val]):
        cell = tbl.cell(r, c)
        cell.text = ""
        p = cell.text_frame.paragraphs[0]
        p.alignment = PP_ALIGN.LEFT
        run = p.add_run()
        is_header = (r == 0)
        set_run(run, txt,
                size=Pt(16),
                color=CHARCOAL if is_header else BODY_GRAY,
                bold=is_header)

        # Cell fill
        cell_fill = cell.fill
        cell_fill.solid()
        if is_header:
            cell_fill.fore_color.rgb = TABLE_HEADER_BG
        else:
            cell_fill.fore_color.rgb = WHITE

        # Cell margins
        cell.margin_left = Inches(0.15)
        cell.margin_top = Inches(0.08)
        cell.margin_bottom = Inches(0.08)


# ── SLIDE 11 — Reading Results ─────────────────────────────────
sl = prs.slides.add_slide(blank_layout)
lines = [
    "Von Mises stress plot: red = high stress, blue = low",
    "Displacement plot: how far the part bends (watch for visual exaggeration)",
    "Factor of Safety: below 1.0 = predicted failure",
    "Always read the legend numbers, not just the colors",
]
title_and_body(sl, 11, "Reading Results", lines)


# ── SLIDE 12 — Print Parameters ───────────────────────────────
sl = prs.slides.add_slide(blank_layout)
set_slide_bg(sl)
slide_number_box(sl, 12)

tb = add_textbox(sl, LEFT_MARGIN, TOP_TITLE, CONTENT_W, Inches(1.0))
tb.text_frame.word_wrap = True
first_para(tb.text_frame, "Print Parameters",
           size=Pt(36), color=CHARCOAL, bold=True)

add_rule(sl, LEFT_MARGIN, Inches(1.65), CONTENT_W)

# Two-column layout
col1 = add_textbox(sl, LEFT_MARGIN, TOP_BODY, Inches(5.5), BODY_H)
col1.text_frame.word_wrap = True
first_para(col1.text_frame, "Printer",
           size=Pt(20), color=CHARCOAL, bold=True,
           space_after=Pt(8))
add_para(col1.text_frame, "Bambu Lab P1S",
         size=Pt(17), color=BODY_GRAY, space_after=Pt(20))

add_para(col1.text_frame, "Slicer Settings",
         size=Pt(20), color=CHARCOAL, bold=True, space_after=Pt(8))
slicer_lines = [
    "100% infill, rectilinear",
    "0.20 mm layer height, 4 walls",
    "210\u2013215 \u00b0C nozzle, 60 \u00b0C bed",
    "Orientation: flat on bed (XY)",
]
for line in slicer_lines:
    add_para(col1.text_frame, f"\u2013  {line}",
             size=Pt(16), color=BODY_GRAY,
             space_before=Pt(3), space_after=Pt(3))

col2 = add_textbox(sl, Inches(7.2), TOP_BODY, Inches(5.2), BODY_H)
col2.text_frame.word_wrap = True
first_para(col2.text_frame, "Quality Control",
           size=Pt(20), color=CHARCOAL, bold=True,
           space_after=Pt(8))
qc_lines = [
    "Print \u2265 3 specimens per condition",
    "Label every specimen",
    "24-hour conditioning before testing",
]
for line in qc_lines:
    add_para(col2.text_frame, f"\u2013  {line}",
             size=Pt(16), color=BODY_GRAY,
             space_before=Pt(3), space_after=Pt(3))


# ── SLIDE 13 — Three-Point Bend Test ──────────────────────────
sl = prs.slides.add_slide(blank_layout)
lines = [
    "Two supports, one load applied at center",
    "ASTM D790: 16:1 span-to-depth ratio (64 mm span, 4 mm depth)",
    "Three setup options: dead weight, shop press, CNC Kitchen style",
    "Safety glasses required for all students",
]
title_and_body(sl, 13, "Three-Point Bend Test", lines)


# ── SLIDE 14 — The Formulas ───────────────────────────────────
sl = prs.slides.add_slide(blank_layout)
set_slide_bg(sl)
slide_number_box(sl, 14)

tb = add_textbox(sl, LEFT_MARGIN, TOP_TITLE, CONTENT_W, Inches(1.0))
tb.text_frame.word_wrap = True
first_para(tb.text_frame, "The Formulas",
           size=Pt(36), color=CHARCOAL, bold=True)

add_rule(sl, LEFT_MARGIN, Inches(1.65), CONTENT_W)

tb2 = add_textbox(sl, LEFT_MARGIN, TOP_BODY, CONTENT_W, BODY_H)
tb2.text_frame.word_wrap = True

# Flexural stress
add_mixed_para(tb2.text_frame, [
    ("Flexural stress    ", Pt(18), CHARCOAL, True),
    ("\u03c3\u1da0 = (3 \u00b7 F \u00b7 L) / (2 \u00b7 b \u00b7 d\u00b2)", Pt(18), BLUE, True),
], is_first=True, space_after=Pt(16))

# Flexural modulus
add_mixed_para(tb2.text_frame, [
    ("Flexural modulus   ", Pt(18), CHARCOAL, True),
    ("E\u1da0 = (L\u00b3 \u00b7 m) / (4 \u00b7 b \u00b7 d\u00b3)", Pt(18), BLUE, True),
], space_after=Pt(24))

# Worked example
add_para(tb2.text_frame, "Worked Example",
         size=Pt(20), color=CHARCOAL, bold=True,
         space_before=Pt(16), space_after=Pt(8))

add_para(tb2.text_frame, "F = 85 N,  L = 64 mm,  b = 12.7 mm,  d = 4 mm",
         size=Pt(17), color=BODY_GRAY, space_after=Pt(4))

add_mixed_para(tb2.text_frame, [
    ("\u03c3\u1da0 = 51.0 MPa", Pt(20), BLUE, True),
    ("    within published PLA range", Pt(17), BODY_GRAY, False),
], space_before=Pt(8))


# ── SLIDE 15 — Compare: Predicted vs Actual ───────────────────
sl = prs.slides.add_slide(blank_layout)
set_slide_bg(sl)
slide_number_box(sl, 15)

tb = add_textbox(sl, LEFT_MARGIN, TOP_TITLE, CONTENT_W, Inches(1.0))
tb.text_frame.word_wrap = True
first_para(tb.text_frame, "Compare: Predicted vs Actual",
           size=Pt(36), color=CHARCOAL, bold=True)

add_rule(sl, LEFT_MARGIN, Inches(1.65), CONTENT_W)

tb2 = add_textbox(sl, LEFT_MARGIN, TOP_BODY, CONTENT_W, Inches(1.0))
tb2.text_frame.word_wrap = True
first_para(tb2.text_frame,
           "Percent Error  =  | (Predicted \u2013 Actual) / Actual | \u00d7 100%",
           size=Pt(20), color=BLUE, bold=True)

# Thresholds
tb3 = add_textbox(sl, LEFT_MARGIN, Inches(3.3), CONTENT_W, Inches(3.5))
tb3.text_frame.word_wrap = True

thresholds = [
    ("< 10%", "Strong correlation"),
    ("10 \u2013 20%", "Acceptable for FDM"),
    ("20 \u2013 35%", "Investigate sources of error"),
    ("> 35%", "Something fundamentally wrong"),
]
for i, (pct, desc) in enumerate(thresholds):
    func = first_para if i == 0 else add_para
    p = func(tb3.text_frame, "", size=Pt(18), color=BODY_GRAY,
             space_before=Pt(10), space_after=Pt(4))
    # clear auto-created run, add custom
    p.clear()
    r1 = p.add_run()
    set_run(r1, f"{pct}    ", size=Pt(20), color=BLUE, bold=True)
    r2 = p.add_run()
    set_run(r2, desc, size=Pt(18), color=BODY_GRAY)


# ── SLIDE 16 — Sources of Error ────────────────────────────────
sl = prs.slides.add_slide(blank_layout)
lines = [
    "Material property mismatch",
    "Print defects (voids, poor layer adhesion)",
    "Fixture alignment",
    "Measurement precision (caliper accuracy)",
    "Isotropic assumption on anisotropic parts",
    "Temperature and humidity",
]
title_and_body(sl, 16, "Sources of Error", lines)


# ── SLIDE 17 — The ABS Trap (Advanced) ────────────────────────
sl = prs.slides.add_slide(blank_layout)
set_slide_bg(sl)
slide_number_box(sl, 17)

tb = add_textbox(sl, LEFT_MARGIN, TOP_TITLE, CONTENT_W, Inches(1.0))
tb.text_frame.word_wrap = True
p = tb.text_frame.paragraphs[0]
p.alignment = PP_ALIGN.LEFT
r1 = p.add_run()
set_run(r1, "Advanced:  ", size=Pt(36), color=BLUE, bold=True)
r2 = p.add_run()
set_run(r2, "The ABS Trap", size=Pt(36), color=CHARCOAL, bold=True)

add_rule(sl, LEFT_MARGIN, Inches(1.65), CONTENT_W)

tb2 = add_textbox(sl, LEFT_MARGIN, TOP_BODY, CONTENT_W, BODY_H)
tb2.text_frame.word_wrap = True

abs_lines = [
    "Default SolidWorks ABS = injection-molded properties",
    "FDM ABS = weaker, highly anisotropic",
    "Expect 25\u201350% error with default profile",
    "Students create corrected FDM ABS profile and see error shrink",
]
for i, line in enumerate(abs_lines):
    func = first_para if i == 0 else add_para
    func(tb2.text_frame, f"\u2013  {line}",
         size=Pt(18), color=BODY_GRAY,
         space_before=Pt(8), space_after=Pt(8))

# Capstone callout
add_para(tb2.text_frame, "",
         size=Pt(10), color=BODY_GRAY, space_before=Pt(16))

p_cap = tb2.text_frame.add_paragraph()
p_cap.space_before = Pt(4)
r1 = p_cap.add_run()
set_run(r1, "Capstone lesson:  ", size=Pt(20), color=BLUE, bold=True)
r2 = p_cap.add_run()
set_run(r2, "Assumptions matter more than software.",
        size=Pt(20), color=CHARCOAL, bold=True)


# ── SLIDE 18 — Differentiation ────────────────────────────────
sl = prs.slides.add_slide(blank_layout)
set_slide_bg(sl)
slide_number_box(sl, 18)

tb = add_textbox(sl, LEFT_MARGIN, TOP_TITLE, CONTENT_W, Inches(1.0))
tb.text_frame.word_wrap = True
first_para(tb.text_frame, "Differentiation",
           size=Pt(36), color=CHARCOAL, bold=True)

add_rule(sl, LEFT_MARGIN, Inches(1.65), CONTENT_W)

tb2 = add_textbox(sl, LEFT_MARGIN, TOP_BODY, CONTENT_W, BODY_H)
tb2.text_frame.word_wrap = True

add_blue_label(tb2.text_frame,
               "CORE", "Sections 1\u20137  \u2014  all juniors",
               is_first=True)
add_blue_label(tb2.text_frame,
               "ADVANCED", "Full Sections 1\u20138 with ABS investigation")

add_para(tb2.text_frame, "",
         size=Pt(8), color=BODY_GRAY, space_before=Pt(16))
add_para(tb2.text_frame,
         "\u2013  Self-paced scaffolding on every section page",
         size=Pt(18), color=BODY_GRAY,
         space_before=Pt(8), space_after=Pt(6))
add_para(tb2.text_frame,
         "\u2013  Students who miss lecture can work independently",
         size=Pt(18), color=BODY_GRAY,
         space_before=Pt(4), space_after=Pt(6))


# ── SLIDE 19 — Resources Provided ─────────────────────────────
sl = prs.slides.add_slide(blank_layout)
set_slide_bg(sl)
slide_number_box(sl, 19)

tb = add_textbox(sl, LEFT_MARGIN, TOP_TITLE, CONTENT_W, Inches(1.0))
tb.text_frame.word_wrap = True
first_para(tb.text_frame, "Resources Provided",
           size=Pt(36), color=CHARCOAL, bold=True)

add_rule(sl, LEFT_MARGIN, Inches(1.65), CONTENT_W)

tb2 = add_textbox(sl, LEFT_MARGIN, TOP_BODY, CONTENT_W, BODY_H)
tb2.text_frame.word_wrap = True

resources = [
    ("Live Site", "mr-mcateer.github.io/fea-solidworks-2025"),
    ("Binders", ".docx (CORE + ADVANCED) \u2014 copy / paste / modify"),
    ("Reference", "Glossary, Formula Sheet, Troubleshooting Guide"),
    ("Teacher", "Pacing Guide, Answer Keys, Rubric, Procurement List"),
    ("Video", "CNC Kitchen as anchor resource"),
]
for i, (label, desc) in enumerate(resources):
    add_blue_label(tb2.text_frame, label, desc, is_first=(i == 0))


# ── SLIDE 20 — Assessment ─────────────────────────────────────
sl = prs.slides.add_slide(blank_layout)
lines = [
    "100-point rubric + 25 bonus (Section 8)",
    "Engineering notebook with screenshots, calculations, reflections",
    "Percent error analysis with identified error sources",
    "Written prediction BEFORE physical testing",
]
title_and_body(sl, 20, "Assessment", lines)


# ── SLIDE 21 — What You Need ──────────────────────────────────
sl = prs.slides.add_slide(blank_layout)
set_slide_bg(sl)
slide_number_box(sl, 21)

tb = add_textbox(sl, LEFT_MARGIN, TOP_TITLE, CONTENT_W, Inches(1.0))
tb.text_frame.word_wrap = True
first_para(tb.text_frame, "What You Need",
           size=Pt(36), color=CHARCOAL, bold=True)

add_rule(sl, LEFT_MARGIN, Inches(1.65), CONTENT_W)

# Two columns
col1 = add_textbox(sl, LEFT_MARGIN, TOP_BODY, Inches(5.8), BODY_H)
col1.text_frame.word_wrap = True

first_para(col1.text_frame, "Software",
           size=Pt(20), color=CHARCOAL, bold=True,
           space_after=Pt(6))
add_para(col1.text_frame,
         "\u2013  SolidWorks 2025 with SimulationXpress\n    or Simulation Standard",
         size=Pt(16), color=BODY_GRAY, space_after=Pt(16))

add_para(col1.text_frame, "Hardware",
         size=Pt(20), color=CHARCOAL, bold=True,
         space_after=Pt(6))
hw = [
    "Bambu Lab P1S (or any FDM with enclosure for ABS)",
    "Basic 3-point bend test rig",
    "Digital calipers",
    "Safety glasses",
]
for h in hw:
    add_para(col1.text_frame, f"\u2013  {h}",
             size=Pt(16), color=BODY_GRAY,
             space_before=Pt(3), space_after=Pt(3))

col2 = add_textbox(sl, Inches(7.2), TOP_BODY, Inches(5.2), BODY_H)
col2.text_frame.word_wrap = True

first_para(col2.text_frame, "Materials",
           size=Pt(20), color=CHARCOAL, bold=True,
           space_after=Pt(6))
add_para(col2.text_frame, "\u2013  PLA filament (required)",
         size=Pt(16), color=BODY_GRAY, space_after=Pt(4))
add_para(col2.text_frame, "\u2013  ABS filament (Section 8 only)",
         size=Pt(16), color=BODY_GRAY, space_after=Pt(16))

add_para(col2.text_frame, "Budget",
         size=Pt(20), color=CHARCOAL, bold=True,
         space_after=Pt(6))

p_budget = col2.text_frame.add_paragraph()
p_budget.space_before = Pt(4)
r1 = p_budget.add_run()
set_run(r1, "$20 \u2013 $58", size=Pt(28), color=BLUE, bold=True)
r2 = p_budget.add_run()
set_run(r2, "  per class", size=Pt(17), color=BODY_GRAY)


# ── SLIDE 22 — Next Steps ─────────────────────────────────────
sl = prs.slides.add_slide(blank_layout)
set_slide_bg(sl)
slide_number_box(sl, 22)

tb = add_textbox(sl, LEFT_MARGIN, TOP_TITLE, CONTENT_W, Inches(1.0))
tb.text_frame.word_wrap = True
first_para(tb.text_frame, "Next Steps",
           size=Pt(36), color=CHARCOAL, bold=True)

add_rule(sl, LEFT_MARGIN, Inches(1.65), CONTENT_W)

tb2 = add_textbox(sl, LEFT_MARGIN, TOP_BODY, CONTENT_W, BODY_H)
tb2.text_frame.word_wrap = True

steps = [
    "Review the live site: mr-mcateer.github.io/fea-solidworks-2025",
    "Pick CORE or ADVANCED path for your classes",
    "Modify the .docx binder to fit your schedule",
    "Questions \u2192 mr-mcateer.github.io/fea-solidworks-2025",
]

for i, step in enumerate(steps):
    p = first_para(tb2.text_frame, "", size=Pt(18), color=BODY_GRAY,
                   space_before=Pt(10), space_after=Pt(6)) if i == 0 \
        else add_para(tb2.text_frame, "", size=Pt(18), color=BODY_GRAY,
                      space_before=Pt(10), space_after=Pt(6))
    p.clear()
    r1 = p.add_run()
    set_run(r1, f"{i+1}   ", size=Pt(22), color=BLUE, bold=True)
    r2 = p.add_run()
    set_run(r2, step, size=Pt(18), color=BODY_GRAY)


# ═══════════════════════════════════════════════════════════════
# Save
# ═══════════════════════════════════════════════════════════════
out_path = "/Users/andymcateer/Desktop/Claude Projects/01_TEACHING/Department/Kirsch_Engineering/Lessons/FEA_SolidWorks_2025_Presentation.pptx"
prs.save(out_path)
print(f"Saved  {out_path}")
print(f"Slides: {len(prs.slides)}")
