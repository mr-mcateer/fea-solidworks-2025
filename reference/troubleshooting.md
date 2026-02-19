---
layout: default
title: "Troubleshooting"
permalink: /reference/troubleshooting
---

<div class="page-wrapper">

<div class="section-header">
  <span class="section-number">Reference</span>
  <h1>Troubleshooting</h1>
</div>

<p>Common SolidWorks Simulation errors and how to fix them. If your study won't run or your results look wrong, start here.</p>

<h2>Study Won't Run</h2>

<h3>"No material assigned" or "Incomplete material definition"</h3>
<div class="callout callout-info">
  <span class="callout-title">Fix</span>
  <p>Right-click the part in the Simulation tree → <strong>Apply/Edit Material</strong>. Make sure all five properties are filled in (Young's Modulus, Tensile Strength, Yield Strength, Poisson's Ratio, Density). A blank field will block the solver.</p>
</div>

<h3>"No fixtures defined" or "Insufficient constraints"</h3>
<div class="callout callout-info">
  <span class="callout-title">Fix</span>
  <p>The solver needs to know how the part is held in space. Apply at least one fixture. For the test bar: fix the two bottom support faces. If you get "rigid body motion" errors, the part can still move freely in at least one direction — add a fixture to prevent that motion.</p>
</div>

<h3>"No loads applied"</h3>
<div class="callout callout-info">
  <span class="callout-title">Fix</span>
  <p>Apply at least one load (force or pressure) to a face or edge. Without a load, there's nothing to analyze.</p>
</div>

<h3>"Mesh failed" or "Unable to mesh the part"</h3>
<div class="callout callout-info">
  <span class="callout-title">Fix</span>
  <p>The mesh generator couldn't divide your geometry into elements. Common causes:</p>
  <ul>
    <li><strong>Very thin features:</strong> Elements can't fit inside extremely thin walls. Increase the feature or decrease global element size.</li>
    <li><strong>Small geometry errors:</strong> Tiny gaps or overlapping faces. Run <em>Evaluate → Check</em> in SolidWorks to find geometry issues.</li>
    <li><strong>Element size too large for the part:</strong> Try reducing the global element size by 50%.</li>
  </ul>
</div>

<h3>"Solver failed" or study takes forever</h3>
<div class="callout callout-info">
  <span class="callout-title">Fix</span>
  <p>Usually means the mesh is too fine (too many elements) for your computer's memory. Try:</p>
  <ul>
    <li>Increase element size (coarser mesh, fewer elements)</li>
    <li>Close other programs to free memory</li>
    <li>For SimulationXpress: keep element count under 50,000 for reliable solving on classroom computers</li>
  </ul>
</div>

<h2>Results Look Wrong</h2>

<h3>Stress is extremely high at one point (singularity)</h3>
<div class="callout callout-warn">
  <span class="callout-title">Diagnosis</span>
  <p>If the maximum stress is at a sharp interior corner and the value keeps increasing every time you refine the mesh — that's a <strong>singularity</strong>, not a real stress. The math says stress is infinite at a perfectly sharp corner. Reality doesn't have perfectly sharp corners.</p>
  <p><strong>Fix:</strong> Add a fillet to the sharp corner in your SolidWorks part, then re-run. If the high stress goes away or converges to a stable value, it was a singularity.</p>
</div>

<h3>Stress is zero everywhere</h3>
<div class="callout callout-warn">
  <span class="callout-title">Diagnosis</span>
  <p>Check that your load is actually applied. Verify:</p>
  <ul>
    <li>The load magnitude isn't accidentally set to 0</li>
    <li>The load is applied to the correct face (not an adjacent face)</li>
    <li>The load direction is correct (a downward force should point in -Y if your part is oriented with Y up)</li>
  </ul>
</div>

<h3>Displacement seems impossibly large or small</h3>
<div class="callout callout-warn">
  <span class="callout-title">Diagnosis</span>
  <p>Check your units. SolidWorks Simulation uses the unit system from your material properties. If you entered Young's Modulus in GPa but the field expected MPa, your stiffness is off by 1,000x.</p>
  <p>Also check: did you enter force in N when the field expected a different unit? Verify the units shown next to each input field.</p>
</div>

<h3>The part deforms in a weird direction</h3>
<div class="callout callout-warn">
  <span class="callout-title">Diagnosis</span>
  <p>Check your fixture and load directions:</p>
  <ul>
    <li>Is the force pointing the right way? Click on the load arrow — it should point toward the part, not away from it.</li>
    <li>Are fixtures on the correct faces? Fixing the wrong face changes the entire stress pattern.</li>
    <li>Is the part oriented correctly? The test bar should be flat (XY plane) with force applied downward.</li>
  </ul>
</div>

<h3>FoS is less than 1.0 everywhere</h3>
<div class="callout callout-warn">
  <span class="callout-title">Diagnosis</span>
  <p>Your applied load exceeds the material's yield strength everywhere on the part. Either:</p>
  <ul>
    <li>Your load is too high (check units — did you enter 500N instead of 50N?)</li>
    <li>Your yield strength value is too low (check the custom material profile)</li>
    <li>The part is genuinely too weak for the applied load (which is a valid result — this is what the part would do in real life)</li>
  </ul>
</div>

<h2>SimulationXpress-Specific Issues</h2>

<h3>Can't find SimulationXpress</h3>
<div class="callout callout-info">
  <span class="callout-title">Fix</span>
  <p>In SolidWorks {{ site.solidworks_version }}: <strong>Tools → Evaluate → SimulationXpress</strong>. It's available in every SolidWorks license. If you don't see it, your installation may be missing the add-in — check <strong>Tools → Add-Ins</strong>.</p>
</div>

<h3>SimulationXpress won't let me pick edges for fixtures</h3>
<div class="callout callout-info">
  <span class="callout-title">Fix</span>
  <p>SimulationXpress only supports face-based fixtures (not edges or vertices). Select the <em>face</em> where the support contacts the bar, not the edge. You may need to split the bottom face at the support locations using the <strong>Split Line</strong> feature first.</p>
</div>

<h3>SimulationXpress only shows basic results</h3>
<div class="callout callout-info">
  <span class="callout-title">Expected behavior</span>
  <p>SimulationXpress shows Von Mises stress, displacement, and Factor of Safety — which is everything you need for this lesson. For full stress tensors, strain plots, and custom result plots, you need Simulation Standard (paid add-on).</p>
</div>

<h2>Print / Physical Test Issues</h2>

<h3>Specimens break during removal from build plate</h3>
<div class="callout callout-info">
  <span class="callout-title">Fix</span>
  <p>Let the build plate cool completely before removing. PLA specimens at 100% infill stick firmly. Use the flexible build plate — bend it slightly to release. Never pry with sharp tools at the specimen edges.</p>
</div>

<h3>Test results vary wildly between specimens</h3>
<div class="callout callout-info">
  <span class="callout-title">Diagnosis</span>
  <p>Check for:</p>
  <ul>
    <li><strong>Print defects:</strong> Hold specimens up to light — look for voids, gaps between layers, or under-extrusion</li>
    <li><strong>Inconsistent dimensions:</strong> Measure each specimen with calipers. Width and thickness should be within ±0.1mm</li>
    <li><strong>Support alignment:</strong> Are the supports at exactly the same span for each test?</li>
    <li><strong>Loading rate:</strong> Adding weight slowly vs. quickly changes results. Be consistent.</li>
  </ul>
</div>

<h3>Calculated flexural modulus doesn't match published values</h3>
<div class="callout callout-info">
  <span class="callout-title">Diagnosis</span>
  <p>Common causes of low flexural modulus:</p>
  <ul>
    <li>Poor layer adhesion (print too fast, nozzle too cool)</li>
    <li>Internal voids from under-extrusion</li>
    <li>Measurement error in deflection (calipers not zeroed, reading wrong point)</li>
    <li>Support span not measured accurately</li>
  </ul>
  <p>A flexural modulus within 15% of the CNC Kitchen reference value (3,300 MPa) is reasonable for classroom conditions.</p>
</div>

<div class="section-nav-bottom">
  <a href="{{ site.baseurl }}/reference/formula-sheet">← Formula Sheet</a>
  <a href="{{ site.baseurl }}/" class="next-link">Back to Home →</a>
</div>

</div>
