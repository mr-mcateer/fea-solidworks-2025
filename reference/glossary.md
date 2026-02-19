---
layout: default
title: "Glossary"
permalink: /reference/glossary
---

<div class="page-wrapper">

<div class="section-header">
  <span class="section-number">Reference</span>
  <h1>Glossary</h1>
</div>

<p>Every key term from the lesson, defined once, in one place. Ctrl+F is your friend.</p>

<h2>A</h2>

<dl>
<dt><strong>Anisotropy</strong></dt>
<dd>A material property that varies depending on the direction you measure it. FDM 3D-printed parts are anisotropic — strong along the print layers, weak between them. The opposite is <em>isotropic</em> (same in all directions).</dd>

<dt><strong>ASTM D790</strong></dt>
<dd>The American Society for Testing and Materials standard for flexural (bending) properties of plastics. It defines specimen dimensions, support span, loading rate, and calculation methods. This lesson follows its proportions (16:1 span-to-depth ratio).</dd>
</dl>

<h2>B</h2>

<dl>
<dt><strong>Bending Modulus (Flexural Modulus)</strong></dt>
<dd>A measure of how stiff a material is when bent. Calculated from the linear portion of a three-point bend test's force-deflection curve. Units: MPa. CNC Kitchen measured PLA at 3,300 MPa.</dd>

<dt><strong>Brittle Failure</strong></dt>
<dd>Failure mode where the material snaps suddenly with little or no visible deformation beforehand. PLA and ABS exhibit brittle failure. Compare with <em>ductile failure</em>.</dd>
</dl>

<h2>C</h2>

<dl>
<dt><strong>Convergence (Mesh)</strong></dt>
<dd>When refining the mesh (making elements smaller) no longer significantly changes the stress results. If halving element size changes max stress by less than ~5%, the mesh has converged. This means your result is mesh-independent.</dd>

<dt><strong>Crystallinity</strong></dt>
<dd>The degree to which polymer chains are organized in a regular, ordered structure. PLA has high crystallinity, which makes it stiff but brittle.</dd>
</dl>

<h2>D</h2>

<dl>
<dt><strong>Deflection (Displacement)</strong></dt>
<dd>How far a point on the part moves from its original position under load. Measured in mm. SolidWorks displays this as a color plot — but exaggerates the visual deformation. Always read the numerical values.</dd>

<dt><strong>Density</strong></dt>
<dd>Mass per unit volume. For PLA: 1,240 kg/m³. Used by FEA to calculate the part's mass and, if gravity is applied, body forces.</dd>

<dt><strong>Ductile Failure</strong></dt>
<dd>Failure mode where the material stretches and deforms visibly before breaking. PETG is ductile — it yields and elongates. Compare with <em>brittle failure</em>.</dd>
</dl>

<h2>E</h2>

<dl>
<dt><strong>Elastic Region</strong></dt>
<dd>The portion of the stress-strain curve where the material returns to its original shape when the load is removed. Like a rubber band snapping back. Ends at the <em>yield point</em>.</dd>

<dt><strong>Element</strong></dt>
<dd>One small piece of the mesh. FEA divides your part into thousands of elements, solves stress equations for each one, then assembles the full picture. Smaller elements = more accuracy = more computation time.</dd>
</dl>

<h2>F</h2>

<dl>
<dt><strong>Factor of Safety (FoS)</strong></dt>
<dd>Yield Strength ÷ Applied Stress. Tells you how much margin exists before failure. FoS &lt; 1.0 = failure predicted. FoS &gt; 2.0 = comfortable margin. Engineers choose target FoS based on consequences of failure.</dd>

<dt><strong>FDM (Fused Deposition Modeling)</strong></dt>
<dd>3D printing method that builds parts by extruding melted plastic layer by layer. Creates anisotropic parts because layers are bonded by heat, not molecular continuity.</dd>

<dt><strong>FEA (Finite Element Analysis)</strong></dt>
<dd>A computational method that predicts how a part responds to forces, heat, or vibration. The computer divides the geometry into small elements, applies physics equations to each one, and assembles the results. Only as good as the inputs you give it.</dd>

<dt><strong>Fixture</strong></dt>
<dd>A boundary condition that tells the simulation how the part is held or supported in the real world. Common types: fixed (no movement), roller (slides in one direction), pin. Getting fixtures wrong changes the entire stress distribution.</dd>

<dt><strong>Flexural Stress</strong></dt>
<dd>The stress on the outer surface of a specimen during bending. Calculated as σ = (3FL)/(2bd²). The outer fibers experience the highest stress in bending.</dd>
</dl>

<h2>G</h2>

<dl>
<dt><strong>Garbage In, Garbage Out (GIGO)</strong></dt>
<dd>The fundamental principle of all simulation. If your inputs (material properties, fixtures, loads) are wrong, the computer will produce a mathematically precise — but physically meaningless — answer.</dd>

<dt><strong>Glass Transition Temperature (Tg)</strong></dt>
<dd>The temperature at which a polymer transitions from rigid to rubbery. PLA: ~60°C. PETG: ~80°C. ABS: ~105°C. Below Tg, the material is stiff. Above it, it softens dramatically.</dd>
</dl>

<h2>H</h2>

<dl>
<dt><strong>Hooke's Law</strong></dt>
<dd>σ = Eε. Stress equals Young's Modulus times strain. Only valid in the elastic region (before yield). The foundation of linear FEA.</dd>

<dt><strong>Homogeneous</strong></dt>
<dd>Having the same properties at every point. FEA assumes your material is homogeneous. FDM parts are not — they have layer boundaries, potential voids, and varying bond strength throughout.</dd>
</dl>

<h2>I</h2>

<dl>
<dt><strong>Infill</strong></dt>
<dd>The internal structure of a 3D-printed part. 100% infill = solid. Any percentage below 100% creates internal geometry (honeycomb, grid, etc.) that the FEA simulation does not model. For this lesson, 100% infill is required.</dd>

<dt><strong>Isotropic</strong></dt>
<dd>Having the same properties in all directions. Injection-molded plastics are approximately isotropic. FDM prints are not. See <em>anisotropy</em>.</dd>
</dl>

<h2>L</h2>

<dl>
<dt><strong>Load</strong></dt>
<dd>Any force, pressure, or moment applied to a part in the simulation. Must match the real-world loading condition as closely as possible. Common mistake: applying load to the wrong face or in the wrong direction.</dd>
</dl>

<h2>M</h2>

<dl>
<dt><strong>Mesh</strong></dt>
<dd>The network of elements that the FEA solver creates from your part geometry. Think of it as a 3D grid overlaid on your part. Finer mesh = more elements = more accurate results = longer solve time.</dd>

<dt><strong>MPa (Megapascal)</strong></dt>
<dd>Unit of stress and material stiffness. 1 MPa = 1 N/mm² = 1,000,000 Pa. Most FDM plastic properties are in the range of tens to thousands of MPa.</dd>
</dl>

<h2>P</h2>

<dl>
<dt><strong>Percent Error</strong></dt>
<dd>|(Predicted − Actual) / Actual| × 100%. Measures how far off your simulation prediction was from the physical test result.</dd>

<dt><strong>Plastic Region</strong></dt>
<dd>The portion of the stress-strain curve after yield where the material deforms permanently. The material will not return to its original shape even if the load is removed.</dd>

<dt><strong>Poisson's Ratio (ν)</strong></dt>
<dd>When you stretch a material lengthwise, it gets thinner sideways. Poisson's ratio is the ratio of sideways shrinkage to lengthwise stretch. PLA: 0.35. Ranges from 0 (cork) to ~0.5 (rubber).</dd>
</dl>

<h2>S</h2>

<dl>
<dt><strong>Singularity (Stress)</strong></dt>
<dd>A location in the FEA model where stress increases without limit as the mesh is refined. Occurs at sharp interior corners. Not physically real — it is a mathematical artifact. Fix by adding a fillet to the geometry.</dd>

<dt><strong>Static Study</strong></dt>
<dd>An FEA analysis type that assumes loads are applied slowly and remain constant. No vibration, no impact, no time-varying forces. The type used in this lesson.</dd>

<dt><strong>Strain (ε)</strong></dt>
<dd>Change in length divided by original length. A unitless ratio that describes how much a material deforms. Strain of 0.01 = the material stretched by 1% of its original length.</dd>

<dt><strong>Stress (σ)</strong></dt>
<dd>Force divided by area. The internal resistance of a material to an external force. Units: MPa (N/mm²). Think of it as pressure distributed inside the material.</dd>

<dt><strong>Stress-Strain Curve</strong></dt>
<dd>A graph plotting stress (y-axis) vs. strain (x-axis) as a material is pulled until it breaks. Reveals elastic region, yield point, plastic region, ultimate strength, and fracture. The most important single graph in materials science.</dd>
</dl>

<h2>T</h2>

<dl>
<dt><strong>Three-Point Bend Test</strong></dt>
<dd>A mechanical test where a specimen rests on two supports and a load is applied at the center. Measures flexural stress and flexural modulus. The most classroom-accessible mechanical test for plastics.</dd>
</dl>

<h2>U</h2>

<dl>
<dt><strong>Ultimate Tensile Strength (UTS)</strong></dt>
<dd>The maximum stress a material can withstand before failure. The highest point on the stress-strain curve. For FDM PLA at 100% infill: approximately 50 MPa.</dd>
</dl>

<h2>V</h2>

<dl>
<dt><strong>Von Mises Stress</strong></dt>
<dd>A single combined-stress value at each point that accounts for tension, compression, and shear acting simultaneously. Used to predict yielding. If Von Mises stress exceeds yield strength at any location, that location is predicted to fail. The default stress plot in SolidWorks Simulation.</dd>
</dl>

<h2>Y</h2>

<dl>
<dt><strong>Yield Strength (Yield Point)</strong></dt>
<dd>The stress level where permanent deformation begins. Below yield, the material springs back (elastic). Above yield, the material is permanently changed (plastic). For FDM PLA: approximately 40 MPa.</dd>

<dt><strong>Young's Modulus (E)</strong></dt>
<dd>A measure of material stiffness. The slope of the stress-strain curve in the elastic region. Higher E = stiffer material. For FDM PLA: approximately 3,300 MPa. Units: MPa or GPa. Also called <em>elastic modulus</em> or <em>modulus of elasticity</em>.</dd>
</dl>

<div class="section-nav-bottom">
  <a href="{{ site.baseurl }}/">← Back to Home</a>
  <a href="{{ site.baseurl }}/reference/formula-sheet" class="next-link">Formula Sheet →</a>
</div>

</div>
