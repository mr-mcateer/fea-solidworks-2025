---
layout: default
title: "Section 3 — SolidWorks Simulation Setup"
permalink: /sections/3-solidworks-setup
---

<div class="page-wrapper">

  <div class="section-header">
    <span class="section-number">Section 3</span>
    <h1>SolidWorks Simulation Setup</h1>
    <div class="section-objective">
      <strong>Objective</strong>
      Set up and run a static stress study on a rectangular test bar in SolidWorks {{ site.solidworks_version }}. By the end of this section you will have a completed simulation with stress, displacement, and Factor of Safety results ready to interpret in Section 4.
    </div>
  </div>

  <div class="self-paced-note">
    <strong>Working on your own?</strong> You need SolidWorks open with the test-bar part file loaded. If you don't have SimulationXpress or Simulation Standard activated, ask your teacher. Follow each step exactly — screenshots in your engineering notebook as you go.
  </div>

  <!-- ============================================
       SIMULATIONXPRESS vs. SIMULATION STANDARD
       ============================================ -->

  <h2>SimulationXpress vs. Simulation Standard</h2>

  <p>
    SolidWorks {{ site.solidworks_version }} ships with two simulation tools. <strong>SimulationXpress</strong> is free with every SolidWorks license&mdash;it is already on your machine. <strong>Simulation Standard</strong> is a paid add-on with more capabilities. Both will work for this lesson. The table below shows what each one can do.
  </p>

  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Capability</th>
          <th>SimulationXpress</th>
          <th>Simulation Standard</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Part analysis</td>
          <td>Yes (single body only)</td>
          <td>Yes (parts + assemblies)</td>
        </tr>
        <tr>
          <td>Fixtures</td>
          <td>Fixed faces only</td>
          <td>Fixed, roller, pin, elastic support</td>
        </tr>
        <tr>
          <td>Loads</td>
          <td>Force, pressure</td>
          <td>Force, pressure, torque, gravity, bearing</td>
        </tr>
        <tr>
          <td>Mesh control</td>
          <td>Global size only</td>
          <td>Local refinement available</td>
        </tr>
        <tr>
          <td>Results</td>
          <td>Stress, displacement, FoS</td>
          <td>Full stress tensor, strain, custom plots</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-info">
    <span class="callout-title">Which one should I use?</span>
    <p>
      If your school has Simulation Standard, use it&mdash;the extra fixture types and mesh controls will come in handy later. If all you have is SimulationXpress, that is perfectly fine. Every step in this lesson includes instructions for both tools.
    </p>
  </div>

  <!-- ============================================
       STEP-BY-STEP WALKTHROUGH
       ============================================ -->

  <h2>Step-by-Step Walkthrough</h2>

  <p>
    Follow these seven steps in order. Each step builds on the one before it. If something goes wrong, check the troubleshooting reference before moving on.
  </p>

  <ol class="steps">

    <!-- STEP 1 -->
    <li>
      <strong>Open the test bar part file</strong>
      <p>
        Open <code>Test-Bar-80x10x4.SLDPRT</code> from the lesson repository&rsquo;s <code>files</code> folder. This is a simple rectangular bar: <strong>80 mm long &times; 10 mm wide &times; 4 mm thick</strong>. These proportions follow the ASTM D790 standard for three-point bend testing, which calls for a 16:1 span-to-depth ratio. Using a standard shape means our physical test results will be directly comparable to published data.
      </p>
      <p>
        Verify the part opens without errors. You should see a single solid body in the FeatureManager tree.
      </p>
    </li>

    <!-- STEP 2 -->
    <li>
      <strong>Create a new static study</strong>
      <p><strong>Simulation Standard path:</strong></p>
      <p>
        Go to the <strong>Simulation</strong> tab in the CommandManager. Click <strong>New Study</strong>. Select <strong>Static</strong> and name it <code>3pt-bend-PLA</code>. Click the green checkmark.
      </p>
      <p><strong>SimulationXpress path:</strong></p>
      <p>
        Go to <strong>Tools &gt; SimulationXpress</strong>. The wizard opens in the Task Pane on the right side. Click <strong>Next</strong> on the welcome screen to begin.
      </p>
      <p>
        In both cases, SolidWorks {{ site.solidworks_version }} creates a study tree at the bottom of the FeatureManager. You will see empty folders for Material, Fixtures, Loads, and Mesh.
      </p>
    </li>

    <!-- STEP 3 -->
    <li>
      <strong>Assign custom FDM PLA material</strong>
      <p>
        This is the most important step in the entire setup. SolidWorks includes a built-in PLA material, but those properties assume injection-molded plastic. FDM-printed PLA is weaker and more variable because of layer adhesion, infill patterns, and print temperature. We need to create a custom material that reflects how our actual printed parts behave.
      </p>

      <h4>How to create the custom material</h4>
      <p>
        In the study tree, right-click the part name (or the Material folder) and select <strong>Edit Material</strong>. In the Material dialog, click the <strong>Custom</strong> tab. Enter the name <code>FDM PLA &mdash; 100% Infill</code> and fill in these values:
      </p>

      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Property</th>
              <th>Value</th>
              <th>Notes</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Young's Modulus (E)</td>
              <td>3,300 MPa</td>
              <td>CNC Kitchen 3-point bend data; peer-reviewed range is 3,000&ndash;3,500 MPa</td>
            </tr>
            <tr>
              <td>Tensile Strength (UTS)</td>
              <td>50 MPa</td>
              <td>Conservative mid-range from published FDM PLA data at 100% infill</td>
            </tr>
            <tr>
              <td>Yield Strength</td>
              <td>40 MPa</td>
              <td>Approximate onset of plastic deformation for FDM PLA</td>
            </tr>
            <tr>
              <td>Poisson's Ratio</td>
              <td>0.35</td>
              <td>Standard value for PLA</td>
            </tr>
            <tr>
              <td>Density</td>
              <td>1,240 kg/m&sup3;</td>
              <td>PLA material specification</td>
            </tr>
          </tbody>
        </table>
      </div>

      <p>
        After entering the values, click <strong>Save</strong> to store the material in your custom library, then click <strong>Apply</strong> and <strong>Close</strong>. The part in the graphics area should update to show the assigned material.
      </p>

      <div class="callout callout-key">
        <span class="callout-title">Why these numbers matter</span>
        <p>
          These values are averages drawn from multiple published sources. Your actual filament, your printer, and your print settings will all cause variation. A spool of PLA from Brand A printed at 210 &deg;C will behave differently from Brand B printed at 200 &deg;C. Engineering accounts for this uncertainty through the <strong>Factor of Safety</strong>&mdash;you deliberately design parts to handle loads well beyond what you expect, so that real-world variation does not cause failure. We will examine FoS results in Section 4.
        </p>
      </div>
    </li>

    <!-- STEP 4 -->
    <li>
      <strong>Apply fixtures (supports)</strong>
      <p>
        A three-point bend test has two supports on the bottom of the bar and one load point on top at the midspan. We need to tell SolidWorks where the bar cannot move&mdash;those are the fixtures.
      </p>
      <p><strong>Simulation Standard:</strong> Right-click the <strong>Fixtures</strong> folder &gt; <strong>Fixed Geometry</strong>. Select the two narrow bottom edges (or small faces) where the physical supports would contact the bar. These represent the two outer support points in a three-point bend rig.</p>
      <p><strong>SimulationXpress:</strong> In the wizard, click <strong>Add a Fixture</strong>. Select the bottom faces at each support location and apply <strong>Fixed</strong>.</p>

      <div class="callout callout-warn">
        <span class="callout-title">Common mistake: over-constraining</span>
        <p>
          Do <em>not</em> fix the entire bottom face of the bar. Fixing too much surface area locks the part down so rigidly that it cannot bend the way it would in real life. The simulation will report artificially low stress and displacement. Only constrain the faces or edges that correspond to where the physical supports actually touch the specimen.
        </p>
      </div>
    </li>

    <!-- STEP 5 -->
    <li>
      <strong>Apply the load</strong>
      <p><strong>Simulation Standard:</strong> Right-click the <strong>External Loads</strong> folder &gt; <strong>Force</strong>. Select the top face of the bar at its midpoint. Set the force to <strong>50 N</strong> directed <strong>downward</strong> (negative Y, assuming Y is up in your coordinate system). Click the green checkmark.</p>
      <p><strong>SimulationXpress:</strong> In the wizard, click <strong>Add a Force</strong>. Select the top face at the midpoint. Enter <strong>50 N</strong> directed downward.</p>
      <p>
        Why 50 N? It is a convenient starting reference that produces measurable stress and displacement in our bar without exceeding the yield strength. Think of it as roughly the weight of a 5 kg mass pushing straight down. We will compare this predicted stress to actual test data later.
      </p>

      <div class="formula">
        <span class="formula-label">Quick check &mdash; weight to force</span>
        F = m &times; g = 5 kg &times; 9.81 m/s&sup2; &asymp; 49 N &asymp; 50 N
        <span class="formula-note">This is why 50 N is a practical lab-scale load.</span>
      </div>
    </li>

    <!-- STEP 6 -->
    <li>
      <strong>Mesh and solve</strong>
      <p>
        Right-click the <strong>Mesh</strong> folder and select <strong>Create Mesh</strong>. For your first run, accept the default mesh settings. Note the default element size that SolidWorks {{ site.solidworks_version }} assigns&mdash;write it down in your engineering notebook.
      </p>
      <p>
        Click <strong>Run This Study</strong> (green arrow in the toolbar, or right-click the study name &gt; Run). The solver will take a few seconds to a minute depending on your computer.
      </p>
      <p>
        When it finishes, three result plots appear automatically. Record these values in your notebook:
      </p>
      <ul>
        <li><strong>Maximum Von Mises stress</strong> (in MPa)</li>
        <li><strong>Maximum displacement</strong> (in mm)</li>
        <li><strong>Minimum Factor of Safety</strong></li>
      </ul>

      <div class="callout callout-success">
        <span class="callout-title">Sanity check</span>
        <p>
          For a 50 N load on this bar with PLA properties, expect a max stress somewhere in the range of 15&ndash;50 MPa, a displacement under 1 mm, and a Factor of Safety above 1.0. If your numbers are wildly outside this range, double-check your material values, fixture placement, and load direction before continuing.
        </p>
      </div>
    </li>

    <!-- STEP 7 -->
    <li>
      <strong>Optional: mesh refinement study</strong>
      <p>
        FEA results depend on mesh quality. A coarse mesh gives fast but less accurate answers. A finer mesh takes longer but captures stress concentrations more precisely. How do you know when the mesh is fine enough? You run a <strong>convergence check</strong>.
      </p>
      <p>
        Go back to the Mesh folder and edit the mesh settings. <strong>Halve the element size</strong> (for example, if the default was 2 mm, set it to 1 mm). Re-run the study. Compare the new max Von Mises stress to the previous result.
      </p>
      <p>
        If the stress value changed by less than about 5%, the mesh has <strong>converged</strong>&mdash;making it finer will not meaningfully change the answer. If the change is larger than 5%, halve the element size again and rerun. Record all values in a table like this:
      </p>

      <div class="table-wrap">
        <table>
          <thead>
            <tr>
              <th>Run</th>
              <th>Element Size (mm)</th>
              <th>Max Stress (MPa)</th>
              <th>% Change</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td>(default)</td>
              <td>&mdash;</td>
              <td>&mdash;</td>
            </tr>
            <tr>
              <td>2</td>
              <td>(default &divide; 2)</td>
              <td>&mdash;</td>
              <td>&mdash;</td>
            </tr>
            <tr>
              <td>3</td>
              <td>(if needed)</td>
              <td>&mdash;</td>
              <td>&mdash;</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout callout-info">
        <span class="callout-title">Why this matters</span>
        <p>
          In professional engineering, publishing simulation results without a convergence check is considered bad practice. If halving the mesh changes your answer by 20%, your original result was not trustworthy. This simple check builds a habit that separates careful engineering from guesswork.
        </p>
      </div>
    </li>

  </ol>

  <!-- ============================================
       KNOWLEDGE CHECK
       ============================================ -->

  <div class="check-box">
    <div class="check-title">Knowledge Check &mdash; Section 3</div>
    <p>Submit annotated screenshots showing each of the following. Use SolidWorks {{ site.solidworks_version }}&rsquo;s <strong>Snipping Tool</strong> or your OS screenshot tool. Annotate with arrows or labels so your instructor can clearly see what you are pointing to.</p>
    <ol>
      <li><strong>Material assignment</strong> &mdash; Screenshot of the Material dialog showing your custom "FDM PLA &mdash; 100% Infill" with all five property values visible.</li>
      <li><strong>Fixture placement</strong> &mdash; Screenshot of the model showing the fixture symbols on the correct faces or edges. The fixed areas should be highlighted in green.</li>
      <li><strong>Load application</strong> &mdash; Screenshot showing the 50 N force arrow on the top midpoint face, directed downward.</li>
      <li><strong>Results summary</strong> &mdash; Screenshot (or table) recording your max Von Mises stress (MPa), max displacement (mm), and minimum Factor of Safety from the solved study.</li>
    </ol>
    <p>If you completed the optional mesh refinement study (Step 7), include your convergence table with element sizes, stress values, and percent change between runs.</p>
  </div>

  <!-- ============================================
       BOTTOM NAV
       ============================================ -->

  <div class="section-nav-bottom">
    <a href="{{ site.baseurl }}/sections/2-what-fea-does">&larr; Section 2: What FEA Does</a>
    <a href="{{ site.baseurl }}/sections/4-reading-results" class="next-link">Section 4: Reading Results &rarr;</a>
  </div>

</div>
