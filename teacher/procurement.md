---
layout: default
title: "Procurement"
permalink: /teacher/procurement
---

<div class="page-wrapper">

<div class="section-header">
  <span class="section-number">Teacher Resource</span>
  <h1>Procurement &amp; Materials List</h1>
</div>

<p>Everything you need to run this lesson, with estimated costs. Most items are already in a typical CTE shop. The only consumable cost is filament.</p>

<h2>Equipment (Already in Lab)</h2>

<div class="table-wrap">
<table>
  <thead>
    <tr><th>Item</th><th>Qty Needed</th><th>Notes</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>Bambu Lab P1S 3D Printer</td>
      <td>1+ (more = faster queue)</td>
      <td>Enclosed, warm classroom. Already owned per project spec.</td>
    </tr>
    <tr>
      <td>SolidWorks {{ site.solidworks_version }} workstations</td>
      <td>1 per student or pair</td>
      <td>SimulationXpress (free) or Simulation Standard (if licensed)</td>
    </tr>
    <tr>
      <td>Digital calipers</td>
      <td>1 per team</td>
      <td>For measuring specimen dimensions and deflection. 0.01mm resolution.</td>
    </tr>
    <tr>
      <td>Safety glasses</td>
      <td>1 per student</td>
      <td>Required during physical testing. PLA fragments can fly on failure.</td>
    </tr>
  </tbody>
</table>
</div>

<h2>Consumables</h2>

<div class="table-wrap">
<table>
  <thead>
    <tr><th>Item</th><th>Qty Needed</th><th>Est. Cost</th><th>Notes</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>PLA filament (1.75mm)</td>
      <td>~200g per class of 30</td>
      <td>$5–8</td>
      <td>Each test bar (80×10×4mm, 100% infill) uses ~3.5g. At 3 bars per student × 30 students = ~315g. One standard 1kg spool handles 3 classes. Use a consistent brand/color for comparable results.</td>
    </tr>
    <tr>
      <td>ABS filament (1.75mm) — Section 8 only</td>
      <td>~200g per class of 30</td>
      <td>$6–10</td>
      <td>Same calculation as PLA. Only needed if running the advanced investigation. P1S enclosure helps with warping.</td>
    </tr>
  </tbody>
</table>
</div>

<h2>Testing Apparatus</h2>

<p>Choose one option based on what you have available. Option A is cheapest and works well for this lesson.</p>

<h3>Option A — Dead Weight Loading (Recommended)</h3>

<div class="table-wrap">
<table>
  <thead>
    <tr><th>Item</th><th>Qty</th><th>Est. Cost</th><th>Source</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>Steel rod or dowel, 5–6mm diameter, ~150mm long</td>
      <td>2 per test station</td>
      <td>$2–5 total</td>
      <td>Hardware store / shop stock</td>
    </tr>
    <tr>
      <td>Support base (V-block, angle iron, or wood blocks with grooves)</td>
      <td>1 set per station</td>
      <td>$0–10</td>
      <td>Shop-built from scrap. Two blocks spaced 64mm apart with grooves for the support rods.</td>
    </tr>
    <tr>
      <td>Small bucket or bag + hook/wire</td>
      <td>1 per station</td>
      <td>$3–5</td>
      <td>For hanging from specimen midpoint. A small paint can with a wire bail works.</td>
    </tr>
    <tr>
      <td>Calibrated masses (assorted)</td>
      <td>Set of 50g–1kg</td>
      <td>$0–15</td>
      <td>Borrow from physics dept. Or use bags of hardware (bolts, nuts) weighed on a scale.</td>
    </tr>
    <tr>
      <td>Kitchen/postal scale (0.1g or 1g resolution)</td>
      <td>1 per station</td>
      <td>$10–15</td>
      <td>For weighing masses if not using calibrated set</td>
    </tr>
  </tbody>
</table>
</div>

<p><strong>Option A total per station: $15–50</strong> (most from shop stock)</p>

<h3>Option B — Press + Scale</h3>

<div class="table-wrap">
<table>
  <thead>
    <tr><th>Item</th><th>Qty</th><th>Est. Cost</th><th>Source</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>Small arbor press (0.5–1 ton)</td>
      <td>1</td>
      <td>$40–80</td>
      <td>Already in many shops. Harbor Freight / Amazon.</td>
    </tr>
    <tr>
      <td>Bathroom scale or load cell (50kg range)</td>
      <td>1</td>
      <td>$10–25</td>
      <td>Under the specimen supports to read applied force</td>
    </tr>
    <tr>
      <td>Support fixture (same as Option A)</td>
      <td>1 set</td>
      <td>$5–10</td>
      <td>Shop-built</td>
    </tr>
  </tbody>
</table>
</div>

<p><strong>Option B total: $55–115</strong></p>

<h3>Option C — Digital Load Cell Setup</h3>

<div class="table-wrap">
<table>
  <thead>
    <tr><th>Item</th><th>Qty</th><th>Est. Cost</th><th>Source</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>Digital force gauge (100N range)</td>
      <td>1</td>
      <td>$50–150</td>
      <td>Amazon / scientific supply. Gives precise digital readout of applied force.</td>
    </tr>
    <tr>
      <td>Support fixture</td>
      <td>1 set</td>
      <td>$5–10</td>
      <td>Shop-built</td>
    </tr>
  </tbody>
</table>
</div>

<p><strong>Option C total: $55–160</strong></p>

<h2>Printable Materials (Included in Repository)</h2>

<div class="table-wrap">
<table>
  <thead>
    <tr><th>File</th><th>Format</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td>test-bar.SLDPRT</td><td>SolidWorks</td><td>80×10×4mm rectangular test bar</td></tr>
    <tr><td>test-bar.STL</td><td>STL</td><td>Same bar, for students without SolidWorks access to print</td></tr>
    <tr><td>data-sheet.pdf</td><td>PDF</td><td>Printable data collection sheet for Section 6</td></tr>
    <tr><td>comparison-template.pdf</td><td>PDF</td><td>Printable comparison table for Section 7</td></tr>
    <tr><td>material-properties-table.pdf</td><td>PDF</td><td>Published FDM material properties with source citations</td></tr>
  </tbody>
</table>
</div>

<h2>Budget Summary</h2>

<div class="table-wrap">
<table>
  <thead>
    <tr><th>Category</th><th>Low Estimate</th><th>High Estimate</th><th>Notes</th></tr>
  </thead>
  <tbody>
    <tr><td>Filament (PLA only)</td><td>$5</td><td>$8</td><td>Per class of 30</td></tr>
    <tr><td>Filament (PLA + ABS)</td><td>$11</td><td>$18</td><td>If running Section 8</td></tr>
    <tr><td>Testing apparatus (Option A)</td><td>$15</td><td>$50</td><td>One-time, reusable</td></tr>
    <tr><td><strong>Total per class (core lesson)</strong></td><td><strong>$20</strong></td><td><strong>$58</strong></td><td></td></tr>
    <tr><td><strong>Total per class (with Section 8)</strong></td><td><strong>$26</strong></td><td><strong>$68</strong></td><td></td></tr>
  </tbody>
</table>
</div>

<div class="callout callout-success">
  <span class="callout-title">Bottom Line</span>
  <p>If your shop already has a 3D printer, calipers, safety glasses, and basic hardware — the only cost is filament. One spool of PLA ($20–25) covers approximately 3 classes of 30 students through the full core lesson.</p>
</div>

<h2>Standards Alignment (for Administrative Justification)</h2>

<h3>NGSS</h3>
<ul>
  <li><strong>HS-ETS1-1:</strong> Analyze a major global problem — define criteria and constraints</li>
  <li><strong>HS-ETS1-2:</strong> Design a solution using mathematical models and simulations</li>
  <li><strong>HS-ETS1-3:</strong> Evaluate a solution using prioritized criteria, trade-offs, and refinement</li>
  <li><strong>HS-PS2-6:</strong> Mathematical expressions of Newton's second law (force/stress relationships)</li>
</ul>

<h3>NGSS Science &amp; Engineering Practices Addressed</h3>
<ul>
  <li>Developing and using models (FEA simulation)</li>
  <li>Planning and carrying out investigations (physical testing)</li>
  <li>Analyzing and interpreting data (predicted vs. actual comparison)</li>
  <li>Using mathematics and computational thinking (stress calculations, percent error)</li>
  <li>Constructing explanations and designing solutions (error analysis, material selection)</li>
</ul>

<h3>CTE / Career Connections</h3>
<ul>
  <li>Mechanical Engineer</li>
  <li>Materials Scientist</li>
  <li>Quality Assurance Engineer</li>
  <li>Aerospace Structures Analyst</li>
  <li>Biomedical Device Engineer</li>
  <li>Manufacturing Engineer</li>
  <li>CSWA-FEA certification pathway (SolidWorks Associates — FEA specialization)</li>
</ul>

<div class="section-nav-bottom">
  <a href="{{ site.baseurl }}/teacher/rubric">← Rubric</a>
  <a href="{{ site.baseurl }}/" class="next-link">Back to Home →</a>
</div>

</div>
