---
layout: default
title: "Section 6 — Break It: Physical Testing"
permalink: /sections/6-break-it
---

<div class="page-wrapper">

  <div class="section-header">
    <span class="section-number">Section 6</span>
    <h1>Break It: Physical Testing</h1>
    <div class="section-objective">
      <strong>Objective</strong>
      Students physically load their printed specimens, record failure data, and calculate flexural stress.
    </div>
  </div>

  <div class="self-paced-note">
    <strong>Working on your own?</strong> You need your printed specimen from Section 5, a test rig (your teacher will tell you which setup), safety glasses, and a way to measure force and deflection. Have your engineering notebook ready — you'll record data in real time.
  </div>

  <h2>Testing Method: Three-Point Bend</h2>

  <p>
    The three-point bend test is the most classroom-accessible mechanical test you can run. The setup is simple: your specimen sits on two supports spaced apart at a known distance. You apply a downward load at the center, exactly halfway between the supports. You increase the load until the specimen breaks.
  </p>

  <p>
    That is it. Two supports, one load point, one formula. The math is straightforward because the geometry of the loading is symmetric. The maximum stress occurs at the bottom surface of the specimen, directly under the loading point. This is where failure begins, and this is what the formula calculates.
  </p>

  <img src="{{ site.baseurl }}/files/three-point-bend-setup.png" alt="Three-point bend test diagram showing specimen on two supports with center force, dimensions labeled" style="max-width:400px; display:block; margin:20px auto;">
  <p class="img-caption">Three-point bend test: specimen on two supports, force applied at center.</p>

  <img src="{{ site.baseurl }}/files/specimen-dimensions.svg" alt="Test specimen dimensions: 80mm length, 10mm width, 4mm depth, 64mm support span" style="max-width:600px; display:block; margin:20px auto;">
  <p class="img-caption">ASTM D790 proportions: 16:1 span-to-depth ratio.</p>

  <div class="callout callout-key">
    <span class="callout-title">Why Three-Point Bend?</span>
    <p>
      Tensile testing (pulling a specimen apart) requires a dedicated testing machine with grips. Compression testing requires careful alignment to prevent buckling. Three-point bending only requires two supports and a way to push down in the middle. You can build a working test rig from hardware-store materials in under an hour. The standard that governs this test for plastics is ASTM D790.
    </p>
  </div>

  <h2>Test Setup Options</h2>

  <p>
    Your teacher will tell you which setup your classroom is using. All three options work. They differ in how you apply and measure the load.
  </p>

  <h3>Option A &mdash; Dead Weight Loading</h3>

  <p>
    Place your specimen on two support pins (steel rod, wooden dowel, or angle iron) separated by the test span. Hang a bucket or container from the midpoint of the specimen using a wire or hook. Add known masses one at a time. After each addition, measure the deflection at the center of the specimen using digital calipers or a dial indicator. Record every load step. Keep adding mass until the specimen breaks. This method is slow and methodical, which makes it excellent for collecting a full force-deflection curve.
  </p>

  <h3>Option B &mdash; Shop-Built Jig with Press</h3>

  <p>
    Mount two support pins on a base plate. Place a bathroom scale or load cell underneath the base. Use a small arbor press or a C-clamp rig to push down on the specimen at the midpoint. Apply load slowly. Watch the scale reading climb until the specimen fractures. Record the maximum force displayed at the moment of failure. This method is faster than dead weights and gives you a clear peak force, but you may not get a full deflection curve unless you pause to measure at each step.
  </p>

  <h3>Option C &mdash; CNC Kitchen Style</h3>

  <p>
    This follows the same principle Stefan Hermann uses. Place a solid rectangular bar on two supports at the correct span. Apply increasing known weights at the center point, one at a time. After each weight, measure how much the bar has deflected downward. Plot force versus deflection. The slope of the straight-line portion of that graph gives you the bending modulus directly. Continue loading to failure if you want the ultimate flexural stress as well.
  </p>

  <div class="callout callout-warn">
    <span class="callout-title">Safety</span>
    <p>
      When the specimen breaks, pieces can fly. Wear safety glasses for every test. Keep your face and fingers away from the loading point. If you are using dead weights, the bucket will drop when the specimen fractures &mdash; make sure nothing fragile is underneath it. If you are using a press, release the load slowly after failure.
    </p>
  </div>

  <h2>Span and Support Geometry</h2>

  <p>
    These dimensions matter. If you change them, the formula results change. Use the same span for every specimen so your data is comparable across the class.
  </p>

  <div class="callout callout-info">
    <span class="callout-title">Standard Dimensions (ASTM D790)</span>
    <p>
      <strong>Support span (L):</strong> 64 mm. This gives a 16:1 span-to-depth ratio for a 4 mm thick specimen, which is what ASTM D790 recommends for flexural testing of plastics.
    </p>
    <p>
      <strong>Support pin diameter:</strong> Approximately 5&ndash;6 mm. Use steel rod or dowel pins. Both supports should be the same diameter.
    </p>
    <p>
      <strong>Loading nose radius:</strong> Approximately 5&ndash;6 mm. The part that pushes down on the specimen should have a rounded surface, not a sharp edge. A sharp edge creates a stress concentration that does not match the formula's assumptions.
    </p>
  </div>

  <h2>Data Collection</h2>

  <p>
    Copy this table into your engineering notebook or use a printed version from your teacher. Fill it in during the test. Do not rely on memory after the fact. Record every load step as it happens.
  </p>

  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Load Step</th>
          <th>Applied Mass (g)</th>
          <th>Force F (N) = mass &times; 0.00981</th>
          <th>Measured Deflection &delta; (mm)</th>
          <th>Notes</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td>2</td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td>3</td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td>4</td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td>5</td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td>6</td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td>7</td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td>8</td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
        </tr>
        <tr>
          <td>Failure</td>
          <td></td>
          <td></td>
          <td></td>
          <td>Describe how it broke</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-info">
    <span class="callout-title">Recording Failure</span>
    <p>
      On the failure row, write down everything you observe. Did the specimen snap cleanly? Did it bend and go white before breaking (stress whitening)? Did layers delaminate? Did it break under the loading nose or off to one side? Take a photo of the broken specimen with a ruler in the frame for scale. This information matters in Section 7 when you compare physical results to your simulation.
    </p>
  </div>

  <h2>Calculations</h2>

  <p>
    Once your specimen has broken, you have the numbers you need. There are two key formulas for three-point bending. Both come directly from beam theory.
  </p>

  <h3>Flexural Stress at Failure</h3>

  <p>
    This tells you the maximum stress on the outer surface of the specimen at the moment it broke.
  </p>

  <div class="formula">
    <span class="formula-label">&sigma;<sub>f</sub></span> = (3 &times; F &times; L) / (2 &times; b &times; d&sup2;)
    <span class="formula-note">
      Where: F = failure force (N), L = support span (mm), b = specimen width (mm), d = specimen depth/thickness (mm). Result is in MPa.
    </span>
  </div>

  <p>
    This is the number you will compare against the yield strength you entered into SolidWorks. If your material properties were accurate, the simulation's predicted stress at failure load should be close to this measured value.
  </p>

  <h3>Flexural Modulus (from the Elastic Region)</h3>

  <p>
    This tells you how stiff your printed material actually is. You need the force-deflection data from your table to calculate it. Plot Force (y-axis) versus Deflection (x-axis). Find the straight-line portion of the curve &mdash; this is the elastic region where the specimen was bending but had not yet started to permanently deform. Measure the slope of that straight line. That slope is <em>m</em>, in units of N/mm.
  </p>

  <div class="formula">
    <span class="formula-label">E<sub>f</sub></span> = (L&sup3; &times; m) / (4 &times; b &times; d&sup3;)
    <span class="formula-note">
      Where: m = slope of the force-deflection curve in the linear region (N/mm), L = support span (mm), b = specimen width (mm), d = specimen depth/thickness (mm). Result is in MPa.
    </span>
  </div>

  <div class="callout callout-key">
    <span class="callout-title">Benchmark Value</span>
    <p>
      CNC Kitchen reports a bending modulus of approximately 3,300 MPa for PLA. Compare your calculated E<sub>f</sub> to that value, and also compare it to the Young's Modulus you entered in SolidWorks. If all three numbers are in the same ballpark, your simulation inputs were reasonable. If they are far apart, you know something is off &mdash; print settings, material quality, or the property values you used.
    </p>
  </div>

  <h3>Worked Example</h3>

  <p>
    Suppose your specimen failed at a load of 85 N. The support span is 64 mm, the specimen width is 10 mm, and the specimen thickness is 4 mm.
  </p>

  <ol class="steps">
    <li>
      <strong>Identify your values.</strong>
      F = 85 N, L = 64 mm, b = 10 mm, d = 4 mm.
    </li>
    <li>
      <strong>Plug into the flexural stress formula.</strong>
      &sigma;<sub>f</sub> = (3 &times; 85 &times; 64) / (2 &times; 10 &times; 4&sup2;)
    </li>
    <li>
      <strong>Solve the numerator.</strong>
      3 &times; 85 &times; 64 = 16,320
    </li>
    <li>
      <strong>Solve the denominator.</strong>
      2 &times; 10 &times; 16 = 320
    </li>
    <li>
      <strong>Divide.</strong>
      16,320 &divide; 320 = 51.0 MPa
    </li>
    <li>
      <strong>Interpret the result.</strong>
      The flexural stress at failure was 51.0 MPa. Published flexural strength values for PLA typically range from 48 to 80 MPa depending on print orientation, infill, and filament brand. This result is within that range.
    </li>
  </ol>

  <p>
    Now suppose that from your force-deflection plot, the slope of the linear region was m = 32 N/mm.
  </p>

  <ol class="steps">
    <li>
      <strong>Identify your values.</strong>
      m = 32 N/mm, L = 64 mm, b = 10 mm, d = 4 mm.
    </li>
    <li>
      <strong>Plug into the flexural modulus formula.</strong>
      E<sub>f</sub> = (64&sup3; &times; 32) / (4 &times; 10 &times; 4&sup3;)
    </li>
    <li>
      <strong>Solve the numerator.</strong>
      262,144 &times; 32 = 8,388,608
    </li>
    <li>
      <strong>Solve the denominator.</strong>
      4 &times; 10 &times; 64 = 2,560
    </li>
    <li>
      <strong>Divide.</strong>
      8,388,608 &divide; 2,560 = 3,277 MPa
    </li>
    <li>
      <strong>Interpret the result.</strong>
      The measured flexural modulus is 3,277 MPa. CNC Kitchen's reported value is approximately 3,300 MPa. These are very close, which means the material stiffness you measured lines up with published data.
    </li>
  </ol>

  <div class="callout callout-success">
    <span class="callout-title">What Good Data Looks Like</span>
    <p>
      If your flexural stress at failure falls between 45 and 80 MPa for PLA, and your flexural modulus falls between 2,800 and 3,800 MPa, your test was executed well. Numbers outside those ranges are not necessarily wrong &mdash; but they should prompt you to check your test setup, your measurements, and your specimen quality before moving on.
    </p>
  </div>

  <div class="callout callout-danger">
    <span class="callout-title">Common Mistakes</span>
    <p>
      <strong>Unit errors.</strong> The formulas expect force in Newtons, lengths in millimeters, and mass conversion using g = 9.81 m/s&sup2; (multiply grams by 0.00981 to get Newtons). Mixing up grams and kilograms is the most common source of answers that are off by a factor of 1,000.
    </p>
    <p>
      <strong>Measuring the wrong dimension.</strong> The specimen width (b) is the horizontal dimension as it sits on the supports. The depth (d) is the vertical dimension &mdash; the direction the load pushes through. Swapping b and d will give you the wrong answer because d is squared in the stress formula and cubed in the modulus formula.
    </p>
    <p>
      <strong>Specimen not centered.</strong> If the loading nose is not hitting the exact midpoint between the supports, the stress distribution is asymmetric and the formula does not apply cleanly. Take a moment to center the specimen before loading.
    </p>
  </div>

  <div class="check-box">
    <div class="check-title">Knowledge Check</div>
    <p>
      To complete this section, you must have:
    </p>
    <ol>
      <li>A completed data table with all load steps, forces, and deflections filled in.</li>
      <li>A calculated flexural stress at failure (&sigma;<sub>f</sub>) with all work shown.</li>
      <li>A calculated flexural modulus (E<sub>f</sub>) with the slope of your force-deflection curve identified, if your test method provided deflection data.</li>
      <li>A photo of your broken specimen showing the failure location, with a ruler or scale reference in the image.</li>
    </ol>
    <p>
      Record all of this in your engineering notebook. You will need these numbers in Section 7 when you compare your physical test results to the SolidWorks simulation predictions.
    </p>
  </div>

  <div class="section-nav-bottom">
    <a href="{{ site.baseurl }}/sections/5-print-the-specimen">&larr; Previous: Print the Specimen</a>
    <a href="{{ site.baseurl }}/sections/7-compare" class="next-link">Next: Compare &rarr;</a>
  </div>

</div>
