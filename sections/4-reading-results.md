---
layout: default
title: "Section 4 — Reading Results"
permalink: /sections/4-reading-results
---

<div class="page-wrapper">

  <div class="section-header">
    <span class="section-number">Section 4</span>
    <h1>Reading Results</h1>
    <div class="section-objective">
      <strong>Objective</strong>
      Interpret Von Mises stress, displacement, and Factor of Safety plots and explain what they mean in plain language.
    </div>
  </div>

  <div class="self-paced-note">
    <strong>Working on your own?</strong> You should have a completed simulation from Section 3 with results visible. This section teaches you to read the color plots. Keep SolidWorks open — you'll reference your own results as you read.
  </div>

  <h2>Von Mises Stress Plot</h2>

  <p>
    After the solver finishes, the first plot SolidWorks shows you is usually the <strong>Von Mises stress plot</strong>. This is the most important result to understand.
  </p>

  <p>
    Von Mises stress is a single combined-stress number calculated at every point in your part. It accounts for tension, compression, and shear all acting at the same time and rolls them into one value measured in megapascals (MPa). The reason we use it is simple: real-world loads rarely produce pure tension or pure compression alone. Von Mises gives us one number we can compare directly to the material's yield strength.
  </p>

  <div class="formula">
    <span class="formula-label">Failure Criterion</span>
    If &sigma;<sub>VM</sub> &ge; &sigma;<sub>yield</sub> at any point, that location is predicted to permanently deform or fail.
  </div>

  <img src="{{ site.baseurl }}/files/von-mises-stress-plot.svg" alt="Von Mises stress plot showing red at center (high stress) and blue at supports (low stress)" style="max-width:650px; display:block; margin:20px auto;">
  <p class="img-caption">Von Mises stress on a test bar under three-point bending. Red = high stress at center. Blue = low stress near supports.</p>

  <p>
    The plot uses a color spectrum. <strong>Red regions</strong> carry the highest stress. <strong>Blue regions</strong> carry the lowest. Everything in between falls on a gradient. But the colors alone tell you nothing &mdash; you must read the legend on the side of the plot to know what values the colors represent.
  </p>

  <div class="callout callout-warn">
    <span class="callout-title">Warning</span>
    <p>
      Always read the legend. The same shade of red could mean 10&nbsp;MPa on one plot and 500&nbsp;MPa on another. SolidWorks auto-scales the color range to fit your specific results, so two different parts will have completely different scales. Never compare colors across plots &mdash; compare numbers.
    </p>
  </div>

  <p>
    When you look at the plot, ask yourself three questions:
  </p>

  <ol>
    <li>Where is the red region? That is the most stressed location on the part.</li>
    <li>What is the maximum Von Mises stress value? Read the number at the top of the legend or use the probe tool to click the red spot directly.</li>
    <li>Is that maximum stress below the material's yield strength? If yes, the part is predicted to survive the load. If no, it is predicted to fail at that location.</li>
  </ol>

  <h2>Displacement Plot</h2>

  <p>
    The <strong>displacement plot</strong> shows how far each point on the part moves under the applied load, measured in millimeters. This tells you how much the part bends, stretches, or compresses. The color scale works the same way as the stress plot: red means the most movement, blue means the least (usually zero at a fixture).
  </p>

  <img src="{{ site.baseurl }}/files/displacement-plot.svg" alt="Displacement plot showing exaggerated deformation with max displacement at center" style="max-width:650px; display:block; margin:20px auto;">
  <p class="img-caption">Displacement plot with visual exaggeration. The curve looks dramatic, but actual deflection is only 0.08 mm.</p>

  <p>
    Displacement matters because even if a part does not break, it might flex too much to function properly. A shelf bracket that bends 5&nbsp;mm under load is not broken, but it is probably not acceptable either.
  </p>

  <div class="callout callout-danger">
    <span class="callout-title">Critical</span>
    <p>
      SolidWorks exaggerates deformation visually. The deformed shape on your screen might look like the part bent 10&nbsp;mm when the actual displacement value is 0.02&nbsp;mm. The software scales up the deformation so you can see the shape of the deflection, but it does not represent the real magnitude. <strong>Read the numbers in the legend, not the picture.</strong> If you need to see the true-scale deformation, right-click the plot and change the deformation scale to 1:1.
    </p>
  </div>

  <h2>Factor of Safety Plot</h2>

  <img src="{{ site.baseurl }}/files/factor-of-safety-plot.svg" alt="Factor of Safety plot showing orange/red at center (lower FoS) and blue at supports (higher FoS)" style="max-width:650px; display:block; margin:20px auto;">
  <p class="img-caption">Factor of Safety: blue = safe, red = at risk. The minimum FoS is where the part fails first.</p>

  <p>
    The <strong>Factor of Safety (FoS) plot</strong> shows the ratio of yield strength to Von Mises stress at every point on the part. You already know the formula from Section 1:
  </p>

  <div class="formula">
    <span class="formula-label">Factor of Safety</span>
    FoS = &sigma;<sub>yield</sub> &divide; &sigma;<sub>VM</sub>
  </div>

  <p>
    The color coding on this plot is the reverse of what you might expect:
  </p>

  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Color</th>
          <th>FoS Range</th>
          <th>Meaning</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Red</strong></td>
          <td>Below 1.0</td>
          <td>Failure predicted &mdash; stress exceeds yield strength at this location.</td>
        </tr>
        <tr>
          <td><strong>Yellow / Green</strong></td>
          <td>1.0 &ndash; 2.0</td>
          <td>Survives, but with a thin margin. Any unexpected extra load could cause failure.</td>
        </tr>
        <tr>
          <td><strong>Blue</strong></td>
          <td>Above 2.0</td>
          <td>Comfortable margin &mdash; the part is well within its capacity at this location.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <p>
    The single most useful number on this plot is the <strong>minimum FoS</strong> and <strong>where it occurs</strong>. That location is the weakest point on the part &mdash; the place that will fail first if the load increases. Use the probe tool or read the bottom of the legend to find the minimum value.
  </p>

  <div class="callout callout-info">
    <span class="callout-title">Note</span>
    <p>
      A minimum FoS of exactly 1.0 means the part is right at the edge &mdash; any small increase in load, any material defect, or any manufacturing variation could push it into failure. In professional engineering, most designs target a minimum FoS of 1.5 to 3.0 depending on the application and consequences of failure.
    </p>
  </div>

  <h2>Singularities and Artifacts</h2>

  <p>
    Sometimes you will see an extremely high stress value concentrated at a sharp interior corner in your model. The stress might be two or three times higher than anywhere else on the part, and the red spot is just a single tiny point. Before you panic, check whether this is a <strong>singularity</strong>.
  </p>

  <p>
    A singularity is a math artifact, not a real physical phenomenon. It happens because sharp 90-degree interior corners create a theoretical infinite stress concentration. When FEA tries to calculate stress at that exact corner, the answer keeps climbing as you make the mesh finer. There is no correct answer &mdash; the math just diverges to infinity.
  </p>

  <p>
    Here is how to tell the difference between a singularity and a real stress concentration:
  </p>

  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th></th>
          <th>Real Stress Concentration</th>
          <th>Singularity (Artifact)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Mesh refinement</strong></td>
          <td>Stress converges to a stable value as mesh gets finer.</td>
          <td>Stress keeps growing with no limit as mesh gets finer.</td>
        </tr>
        <tr>
          <td><strong>Affected area</strong></td>
          <td>Stress is elevated over a visible region around the feature.</td>
          <td>The extreme value is confined to one or two elements at the exact corner.</td>
        </tr>
        <tr>
          <td><strong>Geometry</strong></td>
          <td>Occurs at fillets, holes, notches &mdash; features with actual geometry.</td>
          <td>Occurs at perfectly sharp interior corners with zero fillet radius.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-info">
    <span class="callout-title">The Fix</span>
    <p>
      Add a fillet to the sharp corner. Even a small radius (0.5&nbsp;mm) eliminates the singularity and lets FEA calculate a real, finite stress value. This is good design practice anyway &mdash; sharp interior corners are stress concentrators in real parts too, and fillets make parts stronger.
    </p>
  </div>

  <h2>The Prediction</h2>

  <p>
    You now have everything you need to make a prediction about your part. Before you send it to the 3D printer, you need to write down what you expect to happen when you test it physically. This is your hypothesis. The physical test in Section 6 is the experiment.
  </p>

  <div class="callout callout-key">
    <span class="callout-title">Your Prediction &mdash; Write This Down</span>
    <p>
      Before printing your specimen, record the following from your simulation results at your chosen test load:
    </p>
    <ol>
      <li><strong>Predicted maximum Von Mises stress</strong> &mdash; the peak value from your stress plot, in MPa.</li>
      <li><strong>Predicted maximum displacement</strong> &mdash; the peak value from your displacement plot, in mm.</li>
      <li><strong>Predicted Factor of Safety</strong> &mdash; the minimum FoS value from your FoS plot.</li>
      <li><strong>Predicted failure location</strong> &mdash; describe where on the part you expect failure to occur (for example, "the fillet on the underside near the left support").</li>
    </ol>
    <p>
      This is your hypothesis. Write it clearly, with units and specific locations. In Section 6, you will load the real part and compare your prediction to what actually happens. The quality of your engineering analysis depends on making this prediction <em>before</em> you see the real results &mdash; not after.
    </p>
  </div>

  <!-- ============================================
       KNOWLEDGE CHECK
       ============================================ -->
  <div class="check-box">
    <div class="check-title">Knowledge Check</div>

    <p>
      A classmate runs a simulation on a different bracket design and gets the following results at a 50&nbsp;N load:
    </p>

    <ul>
      <li>Maximum Von Mises stress: <strong>35&nbsp;MPa</strong>, located at the fillet near the fixed end</li>
      <li>Material yield strength (PLA): <strong>40&nbsp;MPa</strong></li>
      <li>Maximum displacement: <strong>0.15&nbsp;mm</strong>, at the tip where the load is applied</li>
      <li>Minimum Factor of Safety: <strong>1.14</strong>, at the fillet near the fixed end</li>
    </ul>

    <p>Using these results, answer the following:</p>

    <ol>
      <li>Where on the part is the stress highest?</li>
      <li>Where on the part is the displacement greatest, and how far does that point move?</li>
      <li>What is the minimum Factor of Safety, and where does it occur?</li>
      <li>Write two sentences summarizing whether this part survives the 50&nbsp;N load. Include specific numbers in your answer.</li>
    </ol>
  </div>

  <!-- ============================================
       BOTTOM NAVIGATION
       ============================================ -->
  <div class="section-nav-bottom">
    <a href="{{ site.baseurl }}/sections/3-solidworks-setup" class="prev-link">&larr; Section 3: SolidWorks Setup</a>
    <a href="{{ site.baseurl }}/sections/5-print-the-specimen" class="next-link">Section 5: Print the Specimen &rarr;</a>
  </div>

</div>
