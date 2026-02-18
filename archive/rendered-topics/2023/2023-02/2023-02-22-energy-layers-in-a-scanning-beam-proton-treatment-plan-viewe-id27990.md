# Energy layers in a scanning beam proton treatment plan viewed in SlicerRT

**Topic ID**: 27990
**Date**: 2023-02-22
**URL**: https://discourse.slicer.org/t/energy-layers-in-a-scanning-beam-proton-treatment-plan-viewed-in-slicerrt/27990

---

## Post #1 by @alema (2023-02-22 22:30 UTC)

<p>Hello,</p>
<p>Is information about “energy layers” available in SlicerRT? In SlicerRT (version 1.0.0 running as an extension to 3D Slicer 5.2.1 on Linux), I see only one table (corresponding to one energy layer) with x and y positions and the weights of the scanning beam. The original RT plan created using Varian Eclipse uses at least 20 energy layers, each containing x and y positions and weights.</p>
<p>I’m new to SlicerRT, so it may be my fault that I don’t know how to display the tables. I aim to extract information about the scanning beam and use it in the Monte Carlo simulation code Topas.</p>
<p>Thank you,<br>
Alexandr</p>

---

## Post #2 by @alema (2023-02-24 18:45 UTC)

<p>In the end, I extracted the ScanSpot_PositionMap_MetersetWeights tables via Pydicom. For a given field, SlicerRT shows only one of the tables. IMHO, the feature to view all of them (one table for one energy layer) is not implemented in SlicerRT.</p>
<p>Alexandr</p>

---

## Post #3 by @Mik (2023-02-25 15:34 UTC)

<p>Dear Alexandr,</p>
<p>Scan spot position map is a dynamic sequence for a RTBeam in a RTPlan.</p>
<p>If you have a dynamic beam with multiple control points in your plan, and the plan with the beam was loaded successfully, you can use <code>Sequences</code> module.</p>
<ol>
<li>
<p>After successful loading, select module <code>Sequences</code> in <code>Sequences</code> subsection;<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7f9689b58bdbf602001121724a5f6ac159f1ccb.png" data-download-href="/uploads/short-url/x68En84CiN6hxfxUiPM29MhZVDd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7f9689b58bdbf602001121724a5f6ac159f1ccb_2_326x500.png" alt="image" data-base62-sha1="x68En84CiN6hxfxUiPM29MhZVDd" width="326" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7f9689b58bdbf602001121724a5f6ac159f1ccb_2_326x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7f9689b58bdbf602001121724a5f6ac159f1ccb_2_489x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7f9689b58bdbf602001121724a5f6ac159f1ccb.png 2x" data-dominant-color="F1F1F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">489×750 44.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
</li>
<li>
<p>Select required sequence browser for a particular beam;</p>
</li>
<li>
<p>Change <code>Control point</code> index for desired value;</p>
</li>
<li>
<p>In subject hierarchy click on ScanSpot_PositionMap table to get different values for each control point.</p>
</li>
</ol>
<p>Lack of good documentation is a real issue indeed.</p>

---

## Post #4 by @Mik (2023-02-25 17:57 UTC)

<p>If you need a <code>Nominal Beam Energy</code> parameter for each control point, or the first value if energy is fixed, that information is unavailable from GUI.</p>

---

## Post #5 by @alema (2023-02-27 17:23 UTC)

<p>Dear Mikhail,</p>
<p>Thank you for the information. I’ve checked that SlicerRT and the code below provide the same values. That is what I need.</p>
<pre><code class="lang-auto">import pydicom
import pandas as pd

dRN = pydicom.dcmread("RN.Plan1.dcm")

iIbs = 2    # Sequence browser index in SlicerRT - 1
iIcps = 48  # Control point in SlicerRT

np = dRN.IonBeamSequence[iIbs].IonControlPointSequence[iIcps].NumberOfScanSpotPositions
xv = dRN.IonBeamSequence[iIbs].IonControlPointSequence[iIcps].ScanSpotPositionMap[0::2]
yv = dRN.IonBeamSequence[iIbs].IonControlPointSequence[iIcps].ScanSpotPositionMap[1::2]
wt = dRN.IonBeamSequence[iIbs].IonControlPointSequence[iIcps].ScanSpotMetersetWeights
ScanSpotTable = pd.DataFrame({'x': xv, 'y': yv, 'weight': wt})

print('Energy = {} MeV'.format(dRN.IonBeamSequence[iIbs].IonControlPointSequence[iIcps].NominalBeamEnergy))
print(ScanSpotTable)
</code></pre>
<p>Output:</p>
<pre><code class="lang-auto">Energy = 63.259 MeV
      x     y    weight
0 -14.0 -21.0  0.058259
1 -28.0 -14.0  0.068364
2 -21.0 -14.0  0.038700
3 -14.0 -14.0  0.155363
4  -7.0  -7.0  0.075061
5 -14.0  -7.0  0.039275
6 -21.0  -7.0  0.097907
7 -14.0   0.0  0.110739
</code></pre>

---
