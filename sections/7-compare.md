---
layout: default
title: "Section 7 — Compare: Predicted vs. Actual"
permalink: /sections/7-compare
---

<div class="page-wrapper">

  <div class="section-header">
    <span class="section-number">Section 7</span>
    <h1>Compare: Predicted vs. Actual</h1>
    <div class="section-objective">
      <strong>Objective</strong>
      Students calculate percent error between their FEA prediction and physical test results, then explain sources of discrepancy.
    </div>
  </div>

  <div class="self-paced-note">
    <strong>Working on your own?</strong> You need your FEA prediction from Section 4 and your physical test data from Section 6. This section is calculation and writing — grab a calculator and your engineering notebook.
  </div>

  <h2>Why Compare?</h2>

  <p>
    Running a simulation is only half the job. Breaking the part is the other half. The real engineering happens right now, when you put the two sets of numbers side by side and ask: how close was my prediction? A simulation that cannot be validated against physical evidence is just a colorful guess. This section gives you the tools to turn your data into a honest comparison.
  </p>

  <h2>The Comparison Table</h2>

  <p>
    Copy the table below into your engineering notebook and fill in every cell. You already have your FEA results from Section 5 and your physical test data from Section 6. This is where they meet.
  </p>

  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Metric</th>
          <th>FEA Predicted</th>
          <th>Physical Test Result</th>
          <th>% Error</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Max stress at failure load</td>
          <td>___ MPa</td>
          <td>___ MPa (calculated from test data)</td>
          <td></td>
        </tr>
        <tr>
          <td>Deflection at reference load</td>
          <td>___ mm</td>
          <td>___ mm (measured)</td>
          <td></td>
        </tr>
        <tr>
          <td>Failure location</td>
          <td>Describe where FEA showed max stress</td>
          <td>Describe where the part actually broke + attach photo</td>
          <td>Match? Y / N</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p>
    For the stress row, use the failure load you recorded during your physical test and the stress value your simulation reported at that same load. For the deflection row, pick a reference load that you applied during both the simulation and the physical test so the comparison is apples-to-apples. For the failure location row, there is no number to calculate. Instead, describe the location in words and decide whether the simulation predicted the right spot.
  </p>

  <h2>Percent Error Formula</h2>

  <div class="formula">
    <span class="formula-label">Percent Error</span>
    <p>
      |&thinsp;(Predicted &minus; Actual) &divide; Actual&thinsp;| &times; 100%
    </p>
    <span class="formula-note">
      The absolute value bars mean the result is always positive. It does not matter whether you over-predicted or under-predicted &mdash; the formula gives you the magnitude of the miss.
    </span>
  </div>

  <p>
    Work through the calculation by hand for each row. Show your work in your notebook. Plug in the FEA value for "Predicted" and the physical test value for "Actual." If your FEA predicted 42 MPa and your test yielded 38 MPa, the percent error is |(42 &minus; 38) / 38| &times; 100% = 10.5%.
  </p>

  <h2>Interpreting Your Error</h2>

  <p>
    The percent error number by itself does not tell you whether your simulation was good or bad. Context matters. For 3D-printed FDM parts tested in a classroom, the ranges below give you a reasonable starting point for interpretation.
  </p>

  <div class="callout callout-success">
    <span class="callout-title">Less than 10% &mdash; Strong Correlation</span>
    <p>
      Your simulation and your physical test are in close agreement. The material properties you used in SolidWorks were a good match for your actual filament, your fixtures modeled reality well, and your measurements were solid. This is an excellent result for a classroom test with FDM parts. Document it and be confident in your simulation setup.
    </p>
  </div>

  <div class="callout callout-info">
    <span class="callout-title">10% to 20% &mdash; Acceptable</span>
    <p>
      This range is typical for FDM parts. 3D printing introduces variability that does not exist in machined metal or injection-molded plastic. Layer adhesion, infill density, nozzle temperature, and print speed all affect the mechanical behavior of your part in ways that are hard to capture perfectly in a simulation. A result in this range means your model is useful and your assumptions were reasonable.
    </p>
  </div>

  <div class="callout callout-warn">
    <span class="callout-title">20% to 35% &mdash; Investigate</span>
    <p>
      Something is off, and you need to figure out what. The most common causes at this level are: material property values that do not match your specific filament brand or batch, print defects like under-extrusion or poor layer adhesion, fixture misalignment during testing, or measurement errors with your instruments. Go back through your test setup and your simulation inputs and look for the mismatch.
    </p>
  </div>

  <div class="callout callout-danger">
    <span class="callout-title">Greater than 35% &mdash; Something Is Fundamentally Off</span>
    <p>
      An error this large usually means one of your core assumptions is wrong. Did you use material properties for ABS but print in PLA? Did the part slip in the fixture during testing? Was the load applied to a different face than what you modeled? Do not try to explain away a 35%+ error with minor factors. Go back to basics and check your simulation setup against your physical test setup, step by step.
    </p>
  </div>

  <h2>Sources of Error</h2>

  <p>
    Every comparison between a simulation and a physical test has error. The goal is not zero error &mdash; that is unrealistic. The goal is to understand <em>where</em> the error comes from so you can reduce it next time. Review the list below and identify which sources apply to your specific results.
  </p>

  <div class="callout callout-key">
    <span class="callout-title">Common Sources of Error</span>
    <ul>
      <li>
        <strong>Material property mismatch.</strong> The Young's Modulus, yield strength, and other values you entered in SolidWorks came from a datasheet or a textbook. Your specific filament brand and batch may have different properties. Different spool colors from the same manufacturer can behave differently.
      </li>
      <li>
        <strong>Print defects.</strong> Under-extrusion, voids between layers, poor layer adhesion, and stringing all weaken the part compared to the ideal solid that the simulation assumes. If you see gaps or rough spots on your broken part, this is likely a contributor.
      </li>
      <li>
        <strong>Fixture alignment.</strong> If your supports were not perfectly level, or the part was not centered on the supports, the load distribution in reality did not match what you modeled. Even a small offset changes where the stress concentrates.
      </li>
      <li>
        <strong>Measurement precision.</strong> Caliper resolution, scale accuracy, and the difficulty of identifying the exact moment of failure all introduce uncertainty. If your caliper reads to 0.1 mm but your deflection was only 2 mm, that is already 5% uncertainty from the instrument alone.
      </li>
      <li>
        <strong>Homogeneous and isotropic assumption.</strong> FEA assumes your material is perfectly uniform in every direction. FDM prints are neither. They have layers, so they are stronger along the layer than across it. They have infill patterns, so they are not solid throughout. This is a fundamental limitation of using standard FEA on printed parts.
      </li>
      <li>
        <strong>Temperature and humidity.</strong> The conditions during printing affect layer bonding and dimensional accuracy. The conditions during testing affect material stiffness. PLA in particular gets softer in warm environments. If your classroom was unusually warm or humid on test day, that matters.
      </li>
    </ul>
  </div>

  <p>
    In your notebook, circle or highlight the sources that you believe contributed most to your specific percent error. You do not need to pick just one. Most real-world discrepancies come from a combination of factors.
  </p>

  <div class="check-box">
    <div class="check-title">Knowledge Check</div>
    <p>
      <strong>Part 1:</strong> Complete the comparison table above with your FEA predictions and physical test results. Calculate the percent error for each row. Show your work.
    </p>
    <p>
      <strong>Part 2:</strong> Write a short response (3&ndash;5 sentences) in your engineering notebook that answers all three of these questions:
    </p>
    <ol>
      <li>What was your percent error for max stress and for deflection?</li>
      <li>What do you think caused the difference between your predicted and actual values?</li>
      <li>What would you change in your simulation setup or test procedure to get a closer match next time?</li>
    </ol>
  </div>

  <div class="section-nav-bottom">
    <a href="{{ site.baseurl }}/sections/6-break-it">&larr; Previous: Break It</a>
    <a href="{{ site.baseurl }}/sections/8-abs-trap" class="next-link">Next: The ABS Trap &rarr;</a>
  </div>

</div>
