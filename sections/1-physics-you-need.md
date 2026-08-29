---
layout: default
title: "Section 1 — The Physics You Need"
permalink: /sections/1-physics-you-need
---

<div class="page-wrapper">

  <div class="section-header">
    <span class="section-number">Section 1</span>
    <h1>The Physics You Need</h1>
    <div class="section-objective">
      <strong>Objective</strong>
      Define stress, strain, and key material properties using correct units. By the end of this section, you will read a stress-strain curve, compare three 3D-printing filaments, and calculate whether a part will survive a given load.
    </div>
  </div>

  <div class="self-paced-note">
    <strong>Working on your own?</strong> No prerequisites — start here. You'll learn the six core terms (stress, strain, Young's Modulus, yield strength, UTS, Factor of Safety) that every other section builds on. Grab a calculator.
  </div>

  <!-- ============================================
       STRESS
       ============================================ -->
  <h2>Stress</h2>

  <p>
    Push on anything and it pushes back. That internal resistance, spread across the area it acts on, is <strong>stress</strong>. A small force on a large area produces low stress. The same force on a tiny area produces high stress. This is why a nail punctures skin but your palm does not.
  </p>

  <div class="formula">
    <span class="formula-label">Stress</span>
    &sigma; = F / A
    <span class="formula-note">F = force (N) &nbsp;|&nbsp; A = cross-sectional area (mm&sup2;) &nbsp;|&nbsp; &sigma; in MPa</span>
  </div>

  <div class="callout callout-key">
    <span class="callout-title">Key Concept</span>
    <p>1 MPa = 1 N/mm&sup2;. Megapascals and Newtons per square millimeter are the same unit. SolidWorks reports stress in MPa by default, so this is the unit you will use for every calculation in this course.</p>
  </div>

  <!-- ============================================
       STRAIN
       ============================================ -->
  <h2>Strain</h2>

  <p>
    When you apply stress to a material, it deforms. <strong>Strain</strong> measures that deformation as a ratio: how much the length changed divided by the original length. Because it is a ratio of two lengths, strain has no units.
  </p>

  <div class="formula">
    <span class="formula-label">Strain</span>
    &epsilon; = &Delta;L / L<sub>0</sub>
    <span class="formula-note">&Delta;L = change in length (mm) &nbsp;|&nbsp; L<sub>0</sub> = original length (mm) &nbsp;|&nbsp; &epsilon; is unitless</span>
  </div>

  <p>
    A strain of 0.01 means the material stretched 1% of its original length. A strain of 0.10 means it stretched 10%. Most engineering metals yield well below 1% strain. Polymers can reach 10% or more before they break.
  </p>

  <!-- ============================================
       YOUNG'S MODULUS
       ============================================ -->
  <h2>Young's Modulus (Stiffness)</h2>

  <p>
    Some materials are stiff (steel, glass). Others are flexible (rubber, silicone). <strong>Young's Modulus</strong> (E) puts a number on that property. It is the slope of the stress-strain curve in the straight-line region where the material behaves elastically&mdash;meaning it springs back when you let go.
  </p>

  <div class="formula">
    <span class="formula-label">Hooke's Law</span>
    &sigma; = E &middot; &epsilon;
    <span class="formula-note">E = Young's Modulus (MPa or GPa) &nbsp;|&nbsp; Valid only in the elastic region</span>
  </div>

  <div class="callout callout-info">
    <span class="callout-title">Scale Check</span>
    <p>Steel: E &asymp; 200,000 MPa (200 GPa). PLA filament: E &asymp; 3,300 MPa (3.3 GPa). PLA is about 60&times; less stiff than steel. That does not mean PLA is weak&mdash;it means PLA deflects 60&times; more under the same stress.</p>
  </div>

  <!-- ============================================
       YIELD STRENGTH
       ============================================ -->
  <h2>Yield Strength</h2>

  <p>
    Load a material gently and it bounces back (elastic behavior). Push past a certain stress level and the deformation becomes permanent. The stress at that transition is the <strong>yield strength</strong>. Below it, the part returns to its original shape. Above it, the part is permanently bent, stretched, or dented. For engineering purposes, exceeding yield strength means the part has failed&mdash;even if it has not broken in half.
  </p>

  <div class="callout callout-warn">
    <span class="callout-title">Watch Out</span>
    <p>Yield strength is not the same as breaking strength. A part can yield (permanently deform) long before it fractures. In FEA, you compare your predicted stress to yield strength to decide if a design is safe.</p>
  </div>

  <!-- ============================================
       ULTIMATE TENSILE STRENGTH
       ============================================ -->
  <h2>Ultimate Tensile Strength (UTS)</h2>

  <p>
    Keep loading past yield and the material enters <strong>plastic deformation</strong>&mdash;it is permanently changing shape. The highest stress the material reaches before it fails is the <strong>Ultimate Tensile Strength</strong> (UTS). After UTS, the material necks down (thins in one spot) and fractures. UTS tells you the absolute ceiling of what the material can withstand. You should never design to this limit. That is what Factor of Safety is for.
  </p>

  <!-- ============================================
       FACTOR OF SAFETY
       ============================================ -->
  <h2>Factor of Safety</h2>

  <p>
    Engineers do not design parts that <em>barely</em> survive. They build in a margin. <strong>Factor of Safety</strong> (FoS) is the ratio of how strong the material is to how much stress you are actually putting on it.
  </p>

  <div class="formula">
    <span class="formula-label">Factor of Safety</span>
    FoS = &sigma;<sub>yield</sub> / &sigma;<sub>applied</sub>
    <span class="formula-note">&sigma;<sub>yield</sub> = material yield strength &nbsp;|&nbsp; &sigma;<sub>applied</sub> = stress from your load</span>
  </div>

  <ul>
    <li><strong>FoS &gt; 1.0</strong> &mdash; The part is predicted to survive. Higher is safer.</li>
    <li><strong>FoS = 1.0</strong> &mdash; The part is at its exact limit. No margin. Not acceptable.</li>
    <li><strong>FoS &lt; 1.0</strong> &mdash; The applied stress exceeds yield strength. The part <em>will</em> permanently deform or break.</li>
  </ul>

  <div class="callout callout-key">
    <span class="callout-title">Rule of Thumb</span>
    <p>For student projects using 3D-printed polymers, a minimum FoS of 2.0 is a reasonable starting target. Safety-critical aerospace parts often require FoS of 1.5 with extensive testing. Consumer products might use 3.0 or higher. The right number depends on consequences of failure and how well you trust your material data.</p>
  </div>

  <!-- ============================================
       STRESS-STRAIN CURVE
       ============================================ -->
  <h2>The Stress-Strain Curve</h2>

  <p>
    Everything above fits onto one graph. The <strong>stress-strain curve</strong> is the single most important diagram in materials engineering. You plot stress (&sigma;) on the vertical axis and strain (&epsilon;) on the horizontal axis, then pull a sample until it breaks. The shape of that curve tells you everything about how the material behaves.
  </p>

  <div class="diagram-container">
    <svg viewBox="0 0 680 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;font-family:'IBM Plex Mono',monospace;">
      <!-- Background grid -->
      <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto">
          <polygon points="0 0, 10 3.5, 0 7" fill="#2D2D2D"/>
        </marker>
      </defs>

      <!-- Axes -->
      <line x1="70" y1="340" x2="650" y2="340" stroke="#2D2D2D" stroke-width="2" marker-end="url(#arrowhead)"/>
      <line x1="70" y1="340" x2="70" y2="20" stroke="#2D2D2D" stroke-width="2" marker-end="url(#arrowhead)"/>

      <!-- Axis labels -->
      <text x="360" y="380" text-anchor="middle" font-size="14" fill="#2D2D2D" font-weight="600">Strain (&epsilon;)</text>
      <text x="24" y="180" text-anchor="middle" font-size="14" fill="#2D2D2D" font-weight="600" transform="rotate(-90,24,180)">Stress (&sigma;)</text>

      <!-- Stress-strain curve -->
      <!-- Elastic region: straight line from origin to yield point -->
      <path d="M 70 340 L 200 120" stroke="#FF6B35" stroke-width="3" fill="none"/>
      <!-- Yield transition and plastic region: curve up to UTS -->
      <path d="M 200 120 Q 230 100, 280 90 Q 350 70, 420 60" stroke="#FF6B35" stroke-width="3" fill="none"/>
      <!-- Necking and fracture: curve down -->
      <path d="M 420 60 Q 480 65, 530 100 Q 560 130, 575 170" stroke="#FF6B35" stroke-width="3" fill="none"/>
      <!-- Fracture mark -->
      <line x1="572" y1="166" x2="582" y2="178" stroke="#EF4444" stroke-width="3"/>
      <line x1="582" y1="166" x2="572" y2="178" stroke="#EF4444" stroke-width="3"/>

      <!-- Region shading -->
      <!-- Elastic region background -->
      <rect x="70" y="30" width="130" height="310" fill="rgba(74,144,217,0.08)" rx="0"/>
      <!-- Plastic region background -->
      <rect x="200" y="30" width="380" height="310" fill="rgba(245,158,11,0.08)" rx="0"/>

      <!-- Yield point marker -->
      <circle cx="200" cy="120" r="5" fill="#4A90D9" stroke="#2D2D2D" stroke-width="1.5"/>
      <line x1="200" y1="120" x2="200" y2="340" stroke="#4A90D9" stroke-width="1" stroke-dasharray="6,4"/>

      <!-- UTS marker -->
      <circle cx="420" cy="60" r="5" fill="#FF6B35" stroke="#2D2D2D" stroke-width="1.5"/>
      <line x1="70" y1="60" x2="420" y2="60" stroke="#9CA3AF" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- Yield strength horizontal line -->
      <line x1="70" y1="120" x2="200" y2="120" stroke="#9CA3AF" stroke-width="1" stroke-dasharray="4,4"/>

      <!-- Labels -->
      <!-- Elastic region label -->
      <text x="135" y="300" text-anchor="middle" font-size="11" fill="#4A90D9" font-weight="700">ELASTIC</text>
      <text x="135" y="316" text-anchor="middle" font-size="10" fill="#4A90D9">REGION</text>

      <!-- Plastic region label -->
      <text x="380" y="300" text-anchor="middle" font-size="11" fill="#F59E0B" font-weight="700">PLASTIC</text>
      <text x="380" y="316" text-anchor="middle" font-size="10" fill="#F59E0B">REGION</text>

      <!-- Yield point label -->
      <text x="200" y="100" text-anchor="middle" font-size="11" fill="#4A90D9" font-weight="600">Yield Point</text>

      <!-- UTS label -->
      <text x="420" y="45" text-anchor="middle" font-size="11" fill="#FF6B35" font-weight="600">UTS</text>

      <!-- Fracture label -->
      <text x="577" y="200" text-anchor="middle" font-size="11" fill="#EF4444" font-weight="600">Fracture</text>

      <!-- Slope annotation (E) -->
      <text x="115" y="210" text-anchor="start" font-size="12" fill="#2D2D2D" font-weight="600">Slope = E</text>
      <text x="107" y="226" text-anchor="start" font-size="10" fill="#6B7280">(Young's Modulus)</text>

      <!-- Y-axis labels -->
      <text x="64" y="124" text-anchor="end" font-size="10" fill="#6B7280">&sigma;<tspan font-size="8" dy="2">y</tspan></text>
      <text x="64" y="64" text-anchor="end" font-size="10" fill="#6B7280">UTS</text>

      <!-- Necking annotation -->
      <text x="510" y="140" text-anchor="middle" font-size="10" fill="#6B7280" font-style="italic">Necking</text>
    </svg>
  </div>

  <h3>Reading the Curve, Region by Region</h3>

  <ol class="steps">
    <li>
      <strong>Elastic Region (straight line)</strong>
      Stress and strain increase together in a straight line. Remove the load and the material returns to its original shape. The slope of this line is Young's Modulus (E). A steeper line means a stiffer material.
    </li>
    <li>
      <strong>Yield Point (the bend in the curve)</strong>
      The curve stops being straight. Beyond this point, removing the load will not bring the material back to its original shape. The stress value here is the yield strength. This is the number FEA compares your applied stress against.
    </li>
    <li>
      <strong>Plastic Region (the curved portion)</strong>
      The material is permanently deforming. It may still be getting stronger (strain hardening), but the damage is done. The peak of this curve is Ultimate Tensile Strength (UTS).
    </li>
    <li>
      <strong>Fracture (the X)</strong>
      The material breaks. In ductile materials, the sample necks down (thins locally) before snapping. In brittle materials, fracture happens suddenly with little warning&mdash;sometimes right at the yield point.
    </li>
  </ol>

  <!-- ============================================
       DUCTILE VS BRITTLE
       ============================================ -->
  <h2>Ductile vs. Brittle Failure</h2>

  <p>
    How a material fails matters as much as when it fails. There are two fundamentally different failure modes.
  </p>

  <h3>Brittle Failure</h3>
  <p>
    The material snaps with little or no plastic deformation. There is almost no warning. The stress-strain curve goes straight up and then drops. PLA is a brittle polymer: load a PLA hook and it holds, holds, holds&mdash;then snaps clean. The break is sudden and the fracture surface is smooth.
  </p>

  <h3>Ductile Failure</h3>
  <p>
    The material stretches, bends, and visibly deforms before it breaks. You get warning. PETG is a ductile polymer: load a PETG hook and it bends, elongates, turns white at the stress point (crazing), and eventually tears. It may never fully snap in half.
  </p>

  <div class="callout callout-info">
    <span class="callout-title">CNC Kitchen Hook Tests</span>
    <p>Stefan from CNC Kitchen tested identical hook geometries printed in PLA, PETG, and ASA. PLA held the most weight (73 kg horizontal) but snapped instantly at failure. PETG held less (55 kg) but stretched visibly before failing. ASA snapped like PLA but absorbed more impact energy due to rubber particles in its microstructure. These results appear in the data table below.</p>
  </div>

  <!-- ============================================
       POLYMER CHEMISTRY TIE-IN
       ============================================ -->
  <h2>Why Different Filaments Behave Differently</h2>

  <p>
    You do not need to become a chemist. But you do need to understand <em>why</em> PLA snaps while PETG bends. The answer is in the molecular structure.
  </p>

  <img src="{{ site.baseurl }}/files/polymer-chain-structure.png" alt="Polymer chain molecular structure comparison: PLA crystalline vs PETG amorphous" style="max-width:500px; display:block; margin:20px auto;">
  <p class="img-caption">Crystalline chains (PLA) pack tight and snap. Amorphous chains (PETG) tangle and flex.</p>

  <h3>PLA &mdash; Stiff but Brittle</h3>
  <p>
    PLA (polylactic acid) has high <strong>crystallinity</strong>&mdash;its polymer chains pack tightly into ordered regions. Ordered packing means high stiffness (3,300 MPa bending modulus) but almost no ability to absorb energy before fracture. PLA also has a low <strong>glass transition temperature</strong> (~60&deg;C), which means it softens in a hot car or under sustained friction. High stiffness, low toughness, low heat resistance.
  </p>

  <h3>PETG &mdash; Flexible and Tough</h3>
  <p>
    PETG is PET (the stuff water bottles are made of) modified with <strong>glycol</strong>. The glycol modification disrupts crystallization, making PETG largely <strong>amorphous</strong>&mdash;its chains are tangled rather than ordered. Tangled chains slide past each other under load, which is why PETG stretches instead of snapping. Lower stiffness (1,900 MPa), but much higher elongation at break.
  </p>

  <h3>ABS/ASA &mdash; Impact Tough</h3>
  <p>
    ABS contains <strong>butadiene rubber</strong> particles dispersed throughout its structure. When a crack tries to propagate through ABS, it hits a rubber particle that absorbs the energy and blunts the crack tip. This is why ABS has high <strong>impact strength</strong> (18 kJ/m&sup2; notched Izod versus 5 kJ/m&sup2; for PLA). ASA replaces butadiene with acrylic rubber for UV resistance but works the same way. The trade-off: ABS is harder to print and warps more.
  </p>

  <h3>Why 3D-Printed Parts Are Different</h3>

  <img src="{{ site.baseurl }}/files/print-orientation-xy-z.png" alt="3D printing layer orientation: XY flat vs Z upright, showing strong and weak directions" style="max-width:550px; display:block; margin:20px auto;">
  <p class="img-caption">Print orientation determines where the weak layer bonds fall relative to your load.</p>

  <div class="callout callout-warn">
    <span class="callout-title">Anisotropy</span>
    <p>
      Injection-molded parts are roughly the same strength in every direction (<strong>isotropic</strong>). 3D-printed FDM parts are not. Each layer bonds to the layer below it through heat, and that bond is always weaker than the solid material within a single layer. The result is <strong>anisotropy</strong>&mdash;the part is strong along the print lines (X/Y) and weak between layers (Z).
    </p>
    <p>
      Think of it like wood: strong along the grain, easy to split across it. This is why print orientation matters enormously in FEA and in real life. A hook printed so that layers stack perpendicular to the load will fail at roughly half the force of the same hook printed with layers parallel to the load.
    </p>
  </div>

  <p>
    Look at the CNC Kitchen data table. The "Vertical hook failure" row shows what happens when layers are stacked perpendicular to the load direction. Every material loses strength, but some lose more than others. ABS drops to 29% of its horizontal capacity. PLA retains 55%. This is the anisotropy penalty, and it is different for every material.
  </p>

  <!-- ============================================
       CNC KITCHEN DATA TABLE
       ============================================ -->
  <h2>Material Comparison: CNC Kitchen Data</h2>

  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>Property</th>
          <th>PLA</th>
          <th>PETG</th>
          <th>ASA/ABS</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Bending modulus</strong></td>
          <td>3,300 MPa</td>
          <td>1,900 MPa</td>
          <td>2,300 MPa</td>
        </tr>
        <tr>
          <td><strong>Horizontal hook failure</strong></td>
          <td>73 kg</td>
          <td>55 kg</td>
          <td>57 kg</td>
        </tr>
        <tr>
          <td><strong>Vertical hook failure</strong></td>
          <td>40 kg (55%)</td>
          <td>25 kg (46%)</td>
          <td>17 kg (29%)</td>
        </tr>
        <tr>
          <td><strong>Impact strength (notched Izod)</strong></td>
          <td>5 kJ/m&sup2;</td>
          <td>8.6 kJ/m&sup2;</td>
          <td>18 kJ/m&sup2;</td>
        </tr>
        <tr>
          <td><strong>Thermal failure onset</strong></td>
          <td>60&deg;C</td>
          <td>80&deg;C</td>
          <td>110&deg;C</td>
        </tr>
        <tr>
          <td><strong>Failure behavior</strong></td>
          <td>Brittle snap</td>
          <td>Stretches, never fully snaps</td>
          <td>Brittle snap</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-success">
    <span class="callout-title">Reading the Table</span>
    <p>PLA wins on raw stiffness and horizontal load capacity. PETG wins on ductility&mdash;it bends rather than breaks. ABS/ASA wins on impact resistance and heat tolerance. No single material is best at everything. Choosing the right filament means knowing which property matters most for your application.</p>
  </div>

  <!-- ============================================
       KNOWLEDGE CHECK
       ============================================ -->
  <div class="check-box">
    <span class="check-title">Knowledge Check</span>
    <p>Calculate the following using the formulas from this section. Show your work with units.</p>
    <ol>
      <li>
        <strong>Stress calculation.</strong>
        A 3D-printed PLA bracket has a cross-sectional area of 80 mm&sup2; at its thinnest point. It must support a load of 200 N. What is the stress at that cross-section?
      </li>
      <li>
        <strong>Strain calculation.</strong>
        A PETG tensile specimen has an original gauge length of 50 mm. Under load, the gauge section stretches to 51.2 mm. What is the strain? Express it as both a decimal and a percentage.
      </li>
      <li>
        <strong>Factor of Safety.</strong>
        The PLA bracket from Problem 1 is made from filament with a yield strength of 50 MPa. Using the stress you calculated, what is the Factor of Safety? Would you trust this design for a load-bearing application? Why or why not?
      </li>
    </ol>
  </div>

  <!-- ============================================
       BOTTOM NAV
       ============================================ -->
  <div class="section-nav-bottom">
    <span></span>
    <a href="{{ site.baseurl }}/sections/2-what-fea-does" class="next-link">Next: What FEA Does &rarr;</a>
  </div>

</div>
