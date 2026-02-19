---
layout: default
title: "Answer Keys"
permalink: /teacher/answer-keys
---

<div class="page-wrapper">

<div class="section-header">
  <span class="section-number">Teacher Resource</span>
  <h1>Answer Keys</h1>
</div>

<p>Solutions for all section knowledge checks. Keep this page bookmarked — do not share the URL with students.</p>

<h2>Section 1 — The Physics You Need</h2>

<h3>Knowledge Check: Three Calculation Scenarios</h3>

<div class="callout callout-success">
  <span class="callout-title">Problem 1: Stress</span>
  <p><strong>Given:</strong> A bar with a cross-sectional area of 40 mm² has a 200 N force applied.</p>
  <p><strong>Find:</strong> Stress</p>
  <p><strong>Solution:</strong> σ = F / A = 200 N / 40 mm² = <strong>5.0 MPa</strong></p>
</div>

<div class="callout callout-success">
  <span class="callout-title">Problem 2: Strain</span>
  <p><strong>Given:</strong> A 100 mm bar stretches to 100.3 mm under load.</p>
  <p><strong>Find:</strong> Strain</p>
  <p><strong>Solution:</strong> ε = ΔL / L₀ = 0.3 mm / 100 mm = <strong>0.003</strong> (or 0.3%)</p>
</div>

<div class="callout callout-success">
  <span class="callout-title">Problem 3: Factor of Safety</span>
  <p><strong>Given:</strong> A part made from FDM PLA (yield strength = 40 MPa) experiences a maximum stress of 25 MPa.</p>
  <p><strong>Find:</strong> Factor of Safety. Will it survive?</p>
  <p><strong>Solution:</strong> FoS = Yield Strength / Applied Stress = 40 / 25 = <strong>1.6</strong></p>
  <p>FoS > 1.0, so the part is predicted to survive the load with a 60% margin before yield.</p>
</div>

<h2>Section 2 — What FEA Actually Does</h2>

<h3>Knowledge Check: Workflow Labeling</h3>

<div class="table-wrap">
<table>
  <thead>
    <tr><th>Step</th><th>Name</th><th>Answer</th></tr>
  </thead>
  <tbody>
    <tr><td>1</td><td>Geometry</td><td><strong>Human Decision</strong></td></tr>
    <tr><td>2</td><td>Material</td><td><strong>Human Decision</strong> — this is where errors hide</td></tr>
    <tr><td>3</td><td>Fixtures</td><td><strong>Human Decision</strong></td></tr>
    <tr><td>4</td><td>Loads</td><td><strong>Human Decision</strong></td></tr>
    <tr><td>5</td><td>Mesh</td><td><strong>Semi-automatic</strong> — computer generates, human can refine</td></tr>
    <tr><td>6</td><td>Solve</td><td><strong>Computer Calculation</strong></td></tr>
    <tr><td>7</td><td>Interpret</td><td><strong>Human Decision</strong></td></tr>
  </tbody>
</table>
</div>

<p><strong>Key takeaway students should articulate:</strong> 5 of the 7 steps involve human decisions. The computer only does Step 6. The quality of the output depends entirely on the quality of Steps 1–4.</p>

<h2>Section 3 — SolidWorks Simulation Setup</h2>

<h3>Knowledge Check: Annotated Screenshots</h3>

<p>Students submit screenshots showing four things. Verify:</p>

<div class="table-wrap">
<table>
  <thead>
    <tr><th>Screenshot</th><th>What to Look For</th><th>Common Mistakes</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>Material assignment</td>
      <td>Custom "FDM PLA — 100% Infill" with E = 3,300 MPa, UTS = 50 MPa, Yield = 40 MPa, ν = 0.35, ρ = 1,240 kg/m³</td>
      <td>Using built-in PLA instead of custom; leaving a field blank; wrong units (GPa vs MPa)</td>
    </tr>
    <tr>
      <td>Fixture placement</td>
      <td>Two faces or edges fixed at the support locations (bottom of bar, near each end)</td>
      <td>Fixing the entire bottom face; fixing only one support; fixing the top face</td>
    </tr>
    <tr>
      <td>Load application</td>
      <td>Single downward force (~50N) at the midpoint of the top face</td>
      <td>Load on wrong face; load pointing up; load value in wrong units</td>
    </tr>
    <tr>
      <td>Results summary</td>
      <td>Max Von Mises stress, max displacement, min FoS values visible</td>
      <td>Screenshot too small to read values; showing displacement plot instead of stress</td>
    </tr>
  </tbody>
</table>
</div>

<div class="callout callout-info">
  <span class="callout-title">Expected Results Range (50N load on 80×10×4mm bar)</span>
  <p>These will vary based on exact fixture placement, but reasonable values are:</p>
  <ul>
    <li><strong>Max Von Mises stress:</strong> 15–25 MPa</li>
    <li><strong>Max displacement:</strong> 0.05–0.15 mm</li>
    <li><strong>Min FoS:</strong> 1.5–2.5</li>
  </ul>
  <p>If a student gets stress > 50 MPa or FoS < 1.0 at 50N, their setup likely has an error.</p>
</div>

<h2>Section 4 — Reading Results</h2>

<h3>Knowledge Check: Interpret a Results Screenshot</h3>

<p><strong>Given values for the sample part:</strong> Max Von Mises = 35 MPa at fillet near fixed end. Yield strength = 40 MPa. Max displacement = 0.15 mm at free end. Min FoS = 1.14 at the fillet.</p>

<div class="callout callout-success">
  <span class="callout-title">Expected Student Answers</span>
  <ul>
    <li><strong>Max stress location:</strong> At the fillet near the fixed end</li>
    <li><strong>Max displacement:</strong> 0.15 mm at the free end (farthest from the fixtures)</li>
    <li><strong>Minimum FoS:</strong> 1.14 at the fillet near the fixed end</li>
    <li><strong>2-sentence summary (example acceptable answer):</strong> "The part will probably survive this load because the minimum Factor of Safety is 1.14, which is above 1.0. However, the margin is small — the fillet near the fixed end is close to yielding, and any increase in load or material weakness could cause failure at that location."</li>
  </ul>
</div>

<h2>Section 5 — Print the Specimen</h2>

<h3>Knowledge Check: Print Documentation</h3>

<p>Verify students provide:</p>
<ul>
  <li>Screenshot from Bambu Studio showing 100% infill, 0.20mm layer height, correct temperatures</li>
  <li>Photo of labeled specimens with correct naming convention (PLA-100-XY-02-[Initials]-[Number])</li>
  <li>Minimum 3 specimens</li>
</ul>

<h2>Section 6 — Break It</h2>

<h3>Knowledge Check: Data Sheet + Calculations</h3>

<div class="callout callout-info">
  <span class="callout-title">Expected Value Ranges for PLA</span>
  <p>These ranges assume 100% infill, 0.20mm layers, flat orientation, on a Bambu Lab P1S with PLA:</p>
  <ul>
    <li><strong>Failure force:</strong> 60–100 N (depends on specific filament and print quality)</li>
    <li><strong>Flexural stress at failure:</strong> 35–60 MPa</li>
    <li><strong>Flexural modulus:</strong> 2,500–3,800 MPa (CNC Kitchen reference: 3,300 MPa)</li>
  </ul>
  <p>Values outside these ranges aren't automatically wrong — but warrant investigation of test setup and print quality.</p>
</div>

<p><strong>Worked example to verify student math:</strong></p>
<p>If F = 85 N, L = 64 mm, b = 10 mm, d = 4 mm:</p>
<p>σ_f = (3 × 85 × 64) / (2 × 10 × 16) = 16,320 / 320 = <strong>51.0 MPa</strong></p>

<h2>Section 7 — Compare</h2>

<h3>Knowledge Check: Comparison Table + Reflection</h3>

<p><strong>Grading the reflection (3–5 sentences):</strong></p>
<div class="table-wrap">
<table>
  <thead>
    <tr><th>Criteria</th><th>Full Credit</th><th>Partial Credit</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>States percent error</td>
      <td>Correct calculation shown</td>
      <td>Calculation attempted but with arithmetic error</td>
    </tr>
    <tr>
      <td>Identifies causes</td>
      <td>Names 2+ specific, plausible sources of error</td>
      <td>Vague ("it was different") or names only 1 source</td>
    </tr>
    <tr>
      <td>Proposes improvements</td>
      <td>Suggests specific, actionable changes</td>
      <td>Suggests vague improvements ("be more careful")</td>
    </tr>
  </tbody>
</table>
</div>

<h2>Section 8 — The ABS Trap</h2>

<h3>Knowledge Check: Side-by-Side Comparison + Reflection</h3>

<p><strong>Expected outcome:</strong> The default (injection-molded) ABS profile produces significantly larger percent error (25–50%) compared to the PLA comparison (typically 10–20%).</p>

<p><strong>Key insight students should articulate in their reflection:</strong></p>
<div class="callout callout-success">
  <span class="callout-title">Acceptable Reflection Elements</span>
  <ul>
    <li>The default ABS profile is for injection-molded ABS, not 3D-printed ABS — they have different properties</li>
    <li>ABS is more affected by print conditions (layer adhesion, chamber temp) than PLA</li>
    <li>The simulation wasn't wrong — the material input was wrong</li>
    <li>Engineers must verify that material properties in the simulation match the actual manufacturing process</li>
    <li>The corrected FDM-ABS profile should produce smaller error, proving the input was the issue</li>
  </ul>
</div>

<div class="section-nav-bottom">
  <a href="{{ site.baseurl }}/teacher/pacing-guide">← Pacing Guide</a>
  <a href="{{ site.baseurl }}/teacher/rubric" class="next-link">Rubric →</a>
</div>

</div>
