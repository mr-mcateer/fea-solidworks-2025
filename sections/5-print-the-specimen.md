---
layout: default
title: "Section 5 — Print the Specimen"
permalink: /sections/5-print-the-specimen
---

<div class="page-wrapper">

  <div class="section-header">
    <span class="section-number">Section 5</span>
    <h1>Print the Specimen</h1>
    <div class="section-objective">
      <strong>Objective</strong>
      Students 3D print test bars with controlled, documented parameters for repeatable results.
    </div>
  </div>

  <div class="self-paced-note">
    <strong>Working on your own?</strong> You need printer access (Bambu Lab P1S) and PLA filament. Read the full parameter table before starting your print — changing settings mid-print invalidates the comparison with your simulation.
  </div>

  <h2>Why Print Settings Matter</h2>

  <p>
    In Section 3, you entered specific material properties into SolidWorks: Young's Modulus, yield strength, Poisson's ratio. Those numbers came from published data for PLA printed under specific conditions. Your simulation assumes those numbers are true. Every stress value, every displacement prediction, every Factor of Safety on your results plots depends on those material inputs being accurate.
  </p>

  <p>
    Here is the problem: if you print your specimen with different settings than the ones used to generate those published material properties, the real part will not behave the way the simulation expects. Print at 50% infill instead of 100%, and the part is weaker and more flexible than your simulation thinks. Change the layer height, and inter-layer adhesion changes. Print too fast, and layers do not bond as well. The physical specimen drifts away from the simulation model, and your comparison in Section 7 becomes meaningless.
  </p>

  <div class="callout callout-key">
    <span class="callout-title">Key Principle</span>
    <p>
      Consistency between your simulation inputs and your print settings is not optional. The FEA assumed a solid, homogeneous part with specific mechanical properties. Your print must match those assumptions as closely as possible, or the comparison breaks before you even start testing.
    </p>
  </div>

  <h2>Required Print Parameters</h2>

  <p>
    The table below lists every print setting you need to control in Bambu Studio for the P1S printer. The "Why" column is not filler. Read it. Every setting has a direct connection to how well your printed part matches the material model in your simulation.
  </p>

  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Parameter</th>
          <th>Setting</th>
          <th>Why</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Infill density</td>
          <td>100%</td>
          <td>FEA assumes a solid, homogeneous part. Any infill percentage below 100% creates internal geometry (honeycomb, gyroid, grid) that the simulation does not know about. The real part would be weaker and more flexible than what the simulation predicts.</td>
        </tr>
        <tr>
          <td>Infill pattern</td>
          <td>Rectilinear</td>
          <td>Most uniform material distribution at 100% fill. Other patterns can leave micro-gaps even at full density.</td>
        </tr>
        <tr>
          <td>Layer height</td>
          <td>0.20 mm</td>
          <td>Standard layer height, well-characterized in published mechanical property data. The material values you entered in Section 3 were measured from specimens printed at this height.</td>
        </tr>
        <tr>
          <td>Wall count</td>
          <td>4 minimum</td>
          <td>Ensures the outer edges of the specimen are fully solid. Thin walls can create weak boundaries that fail before the bulk material.</td>
        </tr>
        <tr>
          <td>Nozzle temperature</td>
          <td>210&ndash;215 &deg;C</td>
          <td>Standard PLA extrusion range on the P1S. Too low and layers do not fuse properly. Too high and the material degrades.</td>
        </tr>
        <tr>
          <td>Bed temperature</td>
          <td>60 &deg;C</td>
          <td>Standard PLA adhesion temperature. Keeps the first layers flat and bonded to the build plate.</td>
        </tr>
        <tr>
          <td>Print speed</td>
          <td>80% of default or slower</td>
          <td>Slower printing improves inter-layer adhesion. Better adhesion means the part behaves more like a continuous solid, which is closer to the isotropic material model your simulation uses.</td>
        </tr>
        <tr>
          <td>Cooling fan</td>
          <td>100% after first layer</td>
          <td>Standard for PLA. Full cooling prevents sagging and maintains dimensional accuracy of the specimen cross-section.</td>
        </tr>
        <tr>
          <td>Orientation</td>
          <td>Flat on bed (XY plane)</td>
          <td>The primary bending load during testing acts in-plane with the printed layers. This is the strongest orientation for a layered part and gives the closest match to isotropic material behavior.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-warn">
    <span class="callout-title">Do Not Improvise</span>
    <p>
      It is tempting to tweak settings because you read a forum post or watched a video about "better" print quality. For this project, do not change anything. These parameters were chosen because they match the conditions under which PLA material properties are published. "Better" print quality is irrelevant if it means your real part no longer matches your simulation inputs.
    </p>
  </div>

  <h2>Specimen Labeling Convention</h2>

  <p>
    Every specimen gets a label. No exceptions. Unlabeled specimens are useless because you cannot trace them back to their print conditions when you analyze data later. Use the following format:
  </p>

  <div class="callout callout-info">
    <span class="callout-title">Label Format</span>
    <pre><code>PLA-100-XY-02-[StudentInitials]-[SampleNumber]</code></pre>
    <p style="margin-top: 12px;">
      <strong>Example:</strong> <code>PLA-100-XY-02-JM-03</code>
    </p>
    <ul style="margin-top: 8px;">
      <li><code>PLA</code> &mdash; Material</li>
      <li><code>100</code> &mdash; Infill percentage (100%)</li>
      <li><code>XY</code> &mdash; Print orientation (flat on bed)</li>
      <li><code>02</code> &mdash; Layer height (0.2 mm)</li>
      <li><code>JM</code> &mdash; Student initials</li>
      <li><code>03</code> &mdash; Sample number (third specimen)</li>
    </ul>
    <p style="margin-top: 12px;">
      Write this on the specimen with a fine-tip marker, or print a label and tape it to a bag containing the specimen. Either way, it must be readable and permanent enough to survive until testing day.
    </p>
  </div>

  <h2>Print Quantity</h2>

  <p>
    Print a minimum of <strong>3 specimens</strong> per student or team.
  </p>

  <p>
    Why three? Because one specimen tells you almost nothing. If you test a single bar and it breaks at 42 MPa, you do not know if that result represents the material or if that particular bar had a hidden defect: a micro-void from under-extrusion, a weak layer bond from a momentary clog, a slight warp you did not notice. You have no way to tell.
  </p>

  <p>
    Three specimens give you a baseline for consistency. If all three break between 40 and 44 MPa, you can be reasonably confident that the material actually fails in that range. If one breaks at 42 MPa and another at 28 MPa, that spread tells you something went wrong with one of the prints, and you can investigate.
  </p>

  <div class="callout callout-success">
    <span class="callout-title">More Is Better</span>
    <p>
      Three is the minimum. If you have time and filament, print five. Professional material testing labs run dozens of specimens for statistical confidence. You are not running a lab certification, but more data points always make your analysis in Section 7 stronger. One outlier in a set of three is hard to deal with. One outlier in a set of five is easy to identify and discuss.
    </p>
  </div>

  <h2>Post-Print Conditioning</h2>

  <p>
    After your specimens come off the build plate, <strong>let them sit for at least 24 hours</strong> before testing.
  </p>

  <p>
    This is not busywork. During printing, the material is heated to over 200 &deg;C and then cooled rapidly. That thermal cycle creates internal stresses locked into the plastic, similar to how a hot glass dish can crack if you put it in cold water. These residual stresses are real forces inside the material even though nothing external is pushing on it.
  </p>

  <p>
    Over 24 hours at room temperature, those internal stresses relax. The polymer chains settle into a more stable arrangement. The result is a specimen whose mechanical behavior is more consistent and repeatable. Testing a part straight off the printer introduces an extra variable you cannot easily measure or account for.
  </p>

  <div class="callout callout-warn">
    <span class="callout-title">Do Not Rush This</span>
    <p>
      Plan your printing schedule so specimens have a full day to condition before testing. If you are printing on a Tuesday and testing on a Wednesday, print early in the day. If you print Tuesday evening and test Wednesday morning, you are cutting it too close.
    </p>
  </div>

  <h2>Document Everything</h2>

  <p>
    Before you slice, take a screenshot of your Bambu Studio settings showing all the parameters from the table above. Save it. This screenshot is your proof that you followed the controlled print conditions. If your results look strange in Section 7, the first question will be "did you actually print at 100% infill?" Your screenshot answers that question.
  </p>

  <p>
    After printing, photograph your labeled specimens next to a ruler or scale reference. This serves two purposes: it confirms the specimens exist and were labeled, and it gives you a visual record of print quality. If a specimen has visible defects (stringing, warping, layer separation), you want that documented before testing so you can explain any anomalies in your data later.
  </p>

  <div class="check-box">
    <div class="check-title">Knowledge Check</div>
    <p>Before moving on, confirm you have completed the following:</p>
    <ol>
      <li>Take a screenshot of your Bambu Studio print settings showing infill density, infill pattern, layer height, wall count, temperatures, speed, cooling, and orientation. Save the screenshot to your engineering notebook or project folder.</li>
      <li>Print a minimum of 3 specimens using the parameters in the table above.</li>
      <li>Label every specimen using the naming convention: <code>PLA-100-XY-02-[Initials]-[SampleNumber]</code></li>
      <li>Photograph your labeled specimens with a scale reference visible.</li>
      <li>Set specimens aside for 24-hour post-print conditioning before testing in Section 6.</li>
    </ol>
  </div>

  <div class="section-nav-bottom">
    <a href="{{ site.baseurl }}/sections/4-reading-results">&larr; Previous: Reading Results</a>
    <a href="{{ site.baseurl }}/sections/6-break-it" class="next-link">Next: Break It &rarr;</a>
  </div>

</div>
