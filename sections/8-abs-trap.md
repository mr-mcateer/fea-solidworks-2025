---
layout: default
title: "Section 8 — The ABS Trap"
permalink: /sections/8-abs-trap
---

<div class="page-wrapper">

  <div class="section-header">
    <span class="section-number">Section 8</span>
    <h1>The ABS Trap</h1>
    <div class="section-objective">
      <strong>Objective</strong>
      Discover that incorrect material assumptions produce large simulation errors. Create a corrected custom material profile and demonstrate that better inputs produce better predictions.
    </div>
  </div>

  <div class="self-paced-note">
    <strong>Working on your own?</strong> This is the advanced extension. Complete Sections 1–7 first. You'll re-run your simulation with ABS material properties and discover what happens when inputs don't match reality. Requires SolidWorks access.
  </div>

  <!-- ============================================
       SETUP
       ============================================ -->
  <h2>Setup: Running the Default ABS Simulation</h2>

  <p>
    You have already seen how SolidWorks performs against physical reality with PLA. Now you are going to repeat the experiment with ABS &mdash; and walk straight into a trap that catches professional engineers every day.
  </p>

  <ol class="steps">
    <li>
      <strong>Open the same test bar part</strong> in SolidWorks that you used for your PLA simulations. Same geometry, same mesh settings.
    </li>
    <li>
      <strong>Assign SolidWorks' built-in ABS material.</strong> Go to the material library, expand Plastics, and select <strong>ABS</strong>. Do not create a custom profile. Use the default library material exactly as SolidWorks provides it.
    </li>
    <li>
      <strong>Apply identical fixtures and loads.</strong> Same boundary conditions as your PLA study &mdash; same fixed faces, same force magnitudes, same directions. The only variable you are changing is the material.
    </li>
    <li>
      <strong>Run the simulation.</strong> When the solver finishes, record three values from the results:
      <ul>
        <li>Predicted maximum Von Mises stress (MPa)</li>
        <li>Predicted maximum displacement (mm)</li>
        <li>Predicted minimum Factor of Safety</li>
      </ul>
      Write these down. You will need them for comparison.
    </li>
  </ol>

  <!-- ============================================
       THE TRAP
       ============================================ -->
  <h2>The Trap</h2>

  <div class="callout callout-danger">
    <span class="callout-title">What You Just Did</span>
    <p>
      SolidWorks' built-in ABS profile is based on <strong>injection-molded ABS</strong>. That material is isotropic, fully dense, and manufactured by forcing molten plastic into a steel mold under high pressure. The library values reflect that process: Young's Modulus around 2,000&ndash;2,300&nbsp;MPa, Ultimate Tensile Strength around 40&ndash;50&nbsp;MPa, uniform properties in every direction.
    </p>
    <p>
      You are not using injection-molded ABS. You are using <strong>FDM-printed ABS</strong>. Your part is built layer by layer. Each layer bonds to the one below it through heat &mdash; and that bond depends on chamber temperature, nozzle temperature, cooling rate, layer height, and print speed. At 100% infill, the part looks solid, but the interlayer adhesion is significantly weaker than the bulk material, especially in the Z-axis.
    </p>
    <p>
      You just told the simulation your part was made by one manufacturing process when it was actually made by a completely different one. The simulation believed you.
    </p>
  </div>

  <!-- ============================================
       PHYSICAL TEST
       ============================================ -->
  <h2>Physical Test</h2>

  <p>
    Print ABS test specimens using the same controlled parameters you established for your PLA tests: 100% infill, flat orientation on the build plate, consistent layer height and nozzle temperature. If you do not have an enclosed printer, note that &mdash; it matters, and it will show up in your results.
  </p>

  <p>
    Break the specimens the same way you broke the PLA ones. Same fixture, same loading direction, same measurement method. Record the actual failure load, actual displacement at failure, and actual failure location. Photograph the fracture surface.
  </p>

  <!-- ============================================
       EXPECTED RESULT
       ============================================ -->
  <h2>What You Will Find</h2>

  <div class="callout callout-warn">
    <span class="callout-title">Expected Result</span>
    <p>
      The error between your simulation prediction and your physical test will be <strong>significantly larger for ABS than it was for PLA</strong>. Expect 25&ndash;50% error depending on your print conditions &mdash; possibly more if you printed without an enclosure. The part will likely fail at a lower load than the simulation predicted, and the fracture may occur at a different location than the stress plot indicated, particularly if interlayer adhesion is the weakest link rather than the bulk material.
    </p>
    <p>
      With PLA, the default library values were already closer to FDM-printed reality because PLA is less sensitive to print conditions. ABS is not forgiving. The gap between injection-molded properties and FDM-printed properties is wider, and the simulation error reflects that gap directly.
    </p>
  </div>

  <!-- ============================================
       THE REVEAL
       ============================================ -->
  <h2>The Reveal</h2>

  <div class="callout callout-key">
    <span class="callout-title">This Is the Point of the Entire Lesson</span>
    <p>
      The simulation was not wrong. The math was correct. The solver did exactly what solvers do. The mesh was fine. The boundary conditions were fine.
    </p>
    <p>
      <strong>The material assumptions were wrong.</strong>
    </p>
    <p>
      You told SolidWorks your part was made of injection-molded ABS. It was not. You gave it FDM-printed ABS. Those are <em>different materials</em> with different mechanical properties, different failure modes, and different directional behavior. The simulation gave you a precise answer to the wrong question.
    </p>
    <p>
      This is the most important thing you will learn in this course: <strong>a simulation is only as good as the assumptions you feed it.</strong> Garbage in, garbage out &mdash; but with a professional-looking stress plot attached.
    </p>
  </div>

  <!-- ============================================
       CNC KITCHEN CONNECTION
       ============================================ -->
  <h2>CNC Kitchen Data: The Anisotropy Evidence</h2>

  <p>
    Stefan from CNC Kitchen tested identical hook geometries printed horizontally and vertically in multiple materials. The vertical orientation forces the load path across layer boundaries &mdash; the weakest link in any FDM part. Here is the result that matters for this section:
  </p>

  <div class="callout callout-info">
    <span class="callout-title">The Anisotropy Gap</span>
    <p>
      ASA (chemically similar to ABS) vertical hooks retained only <strong>29% of horizontal strength</strong> &mdash; the most dramatic anisotropy gap of the three materials tested. PLA retained 55%. PETG retained 46%. ABS/ASA is the most sensitive to print conditions and orientation of the three common filaments.
    </p>
    <p>
      This is why the default material profile failed you worse with ABS than with PLA. The gap between isotropic library data and anisotropic FDM reality is widest for ABS. The simulation cannot account for what you do not tell it.
    </p>
  </div>

  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Material</th>
          <th>Horizontal Hook Failure</th>
          <th>Vertical Hook Failure</th>
          <th>Retention (%)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>PLA</strong></td>
          <td>73 kg</td>
          <td>40 kg</td>
          <td>55%</td>
        </tr>
        <tr>
          <td><strong>PETG</strong></td>
          <td>55 kg</td>
          <td>25 kg</td>
          <td>46%</td>
        </tr>
        <tr>
          <td><strong>ASA/ABS</strong></td>
          <td>57 kg</td>
          <td>17 kg</td>
          <td><strong>29%</strong></td>
        </tr>
      </tbody>
    </table>
  </div>

  <p>
    Look at that bottom row. ABS/ASA loses 71% of its load-carrying capacity when the layers are perpendicular to the force. The default SolidWorks profile does not know this. It assumes the same strength in every direction because injection-molded ABS <em>is</em> the same in every direction. Your FDM part is not.
  </p>

  <!-- ============================================
       THE FIX
       ============================================ -->
  <h2>The Fix: Creating a Corrected Material Profile</h2>

  <p>
    Now that you understand the problem, you can solve it. You are going to create a custom material profile in SolidWorks that represents what FDM-printed ABS actually is, not what injection-molded ABS is.
  </p>

  <ol class="steps">
    <li>
      <strong>Open the material editor.</strong> Right-click the material in the FeatureManager tree and select "Edit Material."
    </li>
    <li>
      <strong>Create a custom material.</strong> Right-click "Custom Materials" in the material tree, select "New Category," and name it something clear like <em>FDM Filaments</em>. Then right-click that category and select "New Material."
    </li>
    <li>
      <strong>Name the material precisely.</strong> Call it <strong>FDM ABS &mdash; 100% Infill, No Enclosure</strong>. The name should tell any engineer exactly what this profile represents and under what conditions it is valid. If you printed in an enclosure, change the name accordingly.
    </li>
    <li>
      <strong>Enter corrected property values.</strong> Use the suggested values in the table below. These are representative of FDM-printed ABS at 100% infill, 240&deg;C nozzle temperature, 0.2&nbsp;mm layer height, printed flat without an enclosed chamber. Your actual values may differ &mdash; that is the point.
    </li>
    <li>
      <strong>Save the material and assign it to your part.</strong> Replace the default ABS with your new custom profile.
    </li>
    <li>
      <strong>Rerun the simulation.</strong> Same fixtures, same loads, same mesh. Only the material properties have changed.
    </li>
    <li>
      <strong>Record the new predictions</strong> and compare them to your physical test results. The error should shrink.
    </li>
  </ol>

  <h3>Suggested Corrected FDM ABS Properties</h3>

  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Property</th>
          <th>SolidWorks Default (Injection-Molded)</th>
          <th>Corrected FDM Value (No Enclosure)</th>
          <th>Notes</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Young's Modulus (E)</strong></td>
          <td>2,000&ndash;2,300 MPa</td>
          <td>~1,600&ndash;1,800 MPa</td>
          <td>Reduced stiffness due to layer interfaces and micro-voids</td>
        </tr>
        <tr>
          <td><strong>Yield Strength</strong></td>
          <td>~40 MPa</td>
          <td>~25&ndash;30 MPa</td>
          <td>Interlayer bonds yield before bulk material</td>
        </tr>
        <tr>
          <td><strong>Ultimate Tensile Strength</strong></td>
          <td>~40&ndash;50 MPa</td>
          <td>~28&ndash;33 MPa</td>
          <td>Lower due to layer adhesion limits</td>
        </tr>
        <tr>
          <td><strong>Poisson's Ratio</strong></td>
          <td>0.394</td>
          <td>0.38</td>
          <td>Slight reduction; minor effect on results</td>
        </tr>
        <tr>
          <td><strong>Density</strong></td>
          <td>1,020&ndash;1,040 kg/m&sup3;</td>
          <td>~980&ndash;1,010 kg/m&sup3;</td>
          <td>Micro-voids reduce effective density even at 100% infill</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-info">
    <span class="callout-title">These Are Starting Points</span>
    <p>
      The corrected values above are drawn from published FDM-ABS tensile test data and represent typical results, not universal constants. Your specific filament brand, nozzle temperature, layer height, cooling conditions, and enclosure will all shift these numbers. The point is not to get the exact right values on the first try. The point is to get <em>closer</em> than the injection-molded defaults &mdash; and to understand that those defaults were never correct for your manufacturing process.
    </p>
  </div>

  <!-- ============================================
       THE LESSON
       ============================================ -->
  <h2>The Lesson</h2>

  <div class="callout callout-success">
    <span class="callout-title">What You Just Learned</span>
    <p>
      FEA is a tool. It does exactly what you tell it. It does not guess, it does not assume, and it does not warn you when your inputs are wrong. It runs the math on whatever material properties you provide and returns a result with six decimal places of false confidence.
    </p>
    <p>
      The engineering skill is not pressing the "Run" button. <strong>The engineering skill is knowing what to tell the tool.</strong> Which material model to use. Which properties to enter. Which simplifications are acceptable and which ones will wreck your prediction.
    </p>
    <p>
      Every professional engineer who runs FEA has to make material assumption decisions exactly like the one you just experienced. Aerospace engineers choose between handbook values for aluminum alloys and test data from their specific heat treatment lot. Automotive engineers decide whether to model a weld zone with base metal properties or degraded HAZ properties. Biomedical engineers select tissue models from published literature knowing that real human tissue varies from patient to patient.
    </p>
    <p>
      You just experienced that decision and its consequences firsthand. You saw what happens when the assumptions are wrong, you measured how far off the prediction landed, and you fixed it by building a material model that matches reality. That is the core of simulation engineering, and you did it as a junior in high school.
    </p>
  </div>

  <!-- ============================================
       KNOWLEDGE CHECK
       ============================================ -->
  <div class="check-box">
    <div class="check-title">Knowledge Check</div>

    <h3>Side-by-Side Comparison</h3>

    <p>
      Fill in the table below with your recorded values. If you did not complete the physical test, use the expected ranges discussed in this section to estimate.
    </p>

    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Measurement</th>
            <th>ABS &mdash; Default Profile</th>
            <th>ABS &mdash; Corrected FDM Profile</th>
            <th>Physical Test (Actual)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Max Von Mises Stress (MPa)</strong></td>
            <td></td>
            <td></td>
            <td></td>
          </tr>
          <tr>
            <td><strong>Max Displacement (mm)</strong></td>
            <td></td>
            <td></td>
            <td></td>
          </tr>
          <tr>
            <td><strong>Min Factor of Safety</strong></td>
            <td></td>
            <td></td>
            <td></td>
          </tr>
          <tr>
            <td><strong>Failure Load (N)</strong></td>
            <td></td>
            <td></td>
            <td></td>
          </tr>
          <tr>
            <td><strong>Failure Location</strong></td>
            <td></td>
            <td></td>
            <td></td>
          </tr>
          <tr>
            <td><strong>% Error vs. Physical Test</strong></td>
            <td></td>
            <td></td>
            <td>Baseline</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h3>Written Reflection</h3>

    <p>Answer the following in complete sentences. Use specific numbers from your data.</p>

    <ol>
      <li>
        Why did the default ABS profile produce a larger error than the default PLA profile? What is physically different about ABS that makes the gap between injection-molded properties and FDM-printed properties wider?
      </li>
      <li>
        What does this teach you about trusting simulation results? Under what conditions should you trust an FEA prediction, and under what conditions should you be skeptical?
      </li>
      <li>
        If you were designing a load-bearing part for a real application and planned to FDM-print it in ABS, what steps would you take before trusting the simulation results?
      </li>
    </ol>
  </div>

  <!-- ============================================
       BOTTOM NAVIGATION
       ============================================ -->
  <div class="section-nav-bottom">
    <a href="{{ site.baseurl }}/sections/7-compare" class="prev-link">&larr; Section 7: Compare</a>
    <a href="{{ site.baseurl }}/" class="next-link">Back to Home</a>
  </div>

</div>
