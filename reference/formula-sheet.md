---
layout: default
title: "Formula Sheet"
permalink: /reference/formula-sheet
---

<div class="page-wrapper">

<div class="section-header">
  <span class="section-number">Reference</span>
  <h1>Formula Sheet</h1>
</div>

<p>All equations from this lesson on one page. Print this and keep it at your workstation.</p>

<h2>Stress, Strain, and Material Properties</h2>

<div class="formula">
  <span class="formula-label">Stress</span>
  σ = F / A
  <span class="formula-note">σ = stress (MPa) &nbsp;|&nbsp; F = force (N) &nbsp;|&nbsp; A = cross-sectional area (mm²)</span>
</div>

<div class="formula">
  <span class="formula-label">Strain</span>
  ε = ΔL / L₀
  <span class="formula-note">ε = strain (unitless) &nbsp;|&nbsp; ΔL = change in length (mm) &nbsp;|&nbsp; L₀ = original length (mm)</span>
</div>

<div class="formula">
  <span class="formula-label">Hooke's Law (Elastic Region Only)</span>
  σ = E × ε
  <span class="formula-note">E = Young's Modulus (MPa) &nbsp;|&nbsp; Slope of stress-strain curve in elastic region</span>
</div>

<div class="formula">
  <span class="formula-label">Factor of Safety</span>
  FoS = Yield Strength / Applied Stress
  <span class="formula-note">FoS &lt; 1.0 = failure predicted &nbsp;|&nbsp; FoS &gt; 2.0 = comfortable margin</span>
</div>

<h2>Three-Point Bend Test (Section 6)</h2>

<div class="formula">
  <span class="formula-label">Flexural Stress at Failure</span>
  σ_f = (3 × F × L) / (2 × b × d²)
  <span class="formula-note">F = failure force (N) &nbsp;|&nbsp; L = support span (mm) &nbsp;|&nbsp; b = width (mm) &nbsp;|&nbsp; d = depth/thickness (mm) &nbsp;|&nbsp; Result in MPa</span>
</div>

<div class="formula">
  <span class="formula-label">Flexural Modulus (from Elastic Region)</span>
  E_f = (L³ × m) / (4 × b × d³)
  <span class="formula-note">m = slope of force-deflection curve in linear region (N/mm) &nbsp;|&nbsp; Result in MPa</span>
</div>

<h2>Comparison (Section 7)</h2>

<div class="formula">
  <span class="formula-label">Percent Error</span>
  % Error = |(Predicted − Actual) / Actual| × 100%
  <span class="formula-note">Use absolute value — error is always positive</span>
</div>

<h2>Unit Conversions</h2>

<div class="table-wrap">
<table>
  <thead>
    <tr>
      <th>Quantity</th>
      <th>Unit</th>
      <th>Equivalents</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Stress / Modulus</td>
      <td>MPa</td>
      <td>1 MPa = 1 N/mm² = 1,000,000 Pa</td>
    </tr>
    <tr>
      <td>Stress / Modulus</td>
      <td>GPa</td>
      <td>1 GPa = 1,000 MPa</td>
    </tr>
    <tr>
      <td>Force</td>
      <td>N (Newton)</td>
      <td>1 kg mass × 9.81 m/s² = 9.81 N</td>
    </tr>
    <tr>
      <td>Force (from grams)</td>
      <td>N</td>
      <td>mass (g) × 0.00981 = force (N)</td>
    </tr>
    <tr>
      <td>Length</td>
      <td>mm</td>
      <td>1 mm = 0.001 m = 0.03937 in</td>
    </tr>
    <tr>
      <td>Area</td>
      <td>mm²</td>
      <td>For rectangular cross-section: A = width × thickness</td>
    </tr>
  </tbody>
</table>
</div>

<h2>Specimen Geometry (ASTM D790 Proportions)</h2>

<div class="table-wrap">
<table>
  <thead>
    <tr>
      <th>Dimension</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Length</td><td>80 mm</td></tr>
    <tr><td>Width (b)</td><td>10 mm</td></tr>
    <tr><td>Thickness (d)</td><td>4 mm</td></tr>
    <tr><td>Support span (L)</td><td>64 mm</td></tr>
    <tr><td>Span-to-depth ratio</td><td>16:1</td></tr>
    <tr><td>Cross-sectional area (A)</td><td>40 mm²</td></tr>
  </tbody>
</table>
</div>

<h2>FDM PLA Material Properties (Custom Profile)</h2>

<div class="table-wrap">
<table>
  <thead>
    <tr>
      <th>Property</th>
      <th>Value</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Young's Modulus (E)</td><td>3,300 MPa</td></tr>
    <tr><td>Tensile Strength (UTS)</td><td>50 MPa</td></tr>
    <tr><td>Yield Strength</td><td>40 MPa</td></tr>
    <tr><td>Poisson's Ratio</td><td>0.35</td></tr>
    <tr><td>Density</td><td>1,240 kg/m³</td></tr>
  </tbody>
</table>
</div>

<h2>Worked Example: Flexural Stress</h2>

<div class="callout callout-info">
  <span class="callout-title">Example Calculation</span>
  <p><strong>Given:</strong> A PLA test bar (b = 10 mm, d = 4 mm) on supports with L = 64 mm span. It failed at a load of F = 85 N.</p>
  <p><strong>Find:</strong> Flexural stress at failure.</p>
  <p><strong>Solution:</strong></p>
  <p>σ_f = (3 × F × L) / (2 × b × d²)</p>
  <p>σ_f = (3 × 85 × 64) / (2 × 10 × 4²)</p>
  <p>σ_f = 16,320 / 320</p>
  <p>σ_f = <strong>51.0 MPa</strong></p>
  <p>This is close to the published UTS of 50 MPa for FDM PLA — the result makes sense.</p>
</div>

<div class="section-nav-bottom">
  <a href="{{ site.baseurl }}/reference/glossary">← Glossary</a>
  <a href="{{ site.baseurl }}/reference/troubleshooting" class="next-link">Troubleshooting →</a>
</div>

</div>
