---
topic_id: 47323
title: "Is there a Python API to get MLC/Jaw position sequences from a VMAT plan?"
date: 2026-06-12
url: https://discourse.slicer.org/t/47323
last_bumped: 2026-06-16T23:16:47.989Z
---

# Is there a Python API to get MLC/Jaw position sequences from a VMAT plan?

**Topic ID**: 47323
**Date**: 2026-06-12
**URL**: https://discourse.slicer.org/t/is-there-a-python-api-to-get-mlc-jaw-position-sequences-from-a-vmat-plan/47323

---

## Post #1 by @Aki (2026-06-12 00:56 UTC)

<p>Hi, there</p>
<p>I would like to get MLC/Jaw position sequences and dose/MU data at each control point from data imported into 3DSlicer. Is there any API to access such data. I would like to make a python script or extension to make a beam projection image at each control point without a patient body. I have already installed SlicerRT.</p>
<p>I uses 3DSlicer version 5.10 on linux and Windows11 pro.</p>
<p>I appreciate your help.</p>
<p>Aki</p>

---

## Post #2 by @cpinter (2026-06-16 13:42 UTC)

<h2><a name="p-134376-accessing-rt-plan-control-point-data-in-slicerrt-1" class="anchor" href="#p-134376-accessing-rt-plan-control-point-data-in-slicerrt-1" aria-label="Heading link"></a>Accessing RT Plan Control Point Data in SlicerRT</h2>
<h3><a name="p-134376-how-the-data-is-structured-after-import-2" class="anchor" href="#p-134376-how-the-data-is-structured-after-import-2" aria-label="Heading link"></a>How the Data Is Structured After Import</h3>
<p>When you import an RT Plan DICOM, SlicerRT creates:</p>
<ul>
<li><strong>Static beams</strong> (2 control points): one <code>vtkMRMLRTBeamNode</code> per beam, with jaw/MLC data from CP0.</li>
<li><strong>Dynamic beams</strong> (IMRT/VMAT, many CPs): a <strong>Sequence</strong> setup — one <code>vtkMRMLRTBeamNode</code> + one MLC <code>vtkMRMLTableNode</code> per control point, driven by a <code>vtkMRMLSequenceBrowserNode</code> named <code>{BeamName}_SequenceBrowser</code>.</li>
</ul>
<h3><a name="p-134376-h-1-access-jaw-positions-and-beam-angles-per-control-point-3" class="anchor" href="#p-134376-h-1-access-jaw-positions-and-beam-angles-per-control-point-3" aria-label="Heading link"></a>1. Access Jaw Positions and Beam Angles Per Control Point</h3>
<p>For <strong>dynamic beams</strong>, iterate the sequence to read each CP’s beam node:</p>
<pre><code class="lang-auto">import slicer

# Find the plan node
planNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLRTPlanNode')

# Iterate beams in the plan
beams = vtk.vtkCollection()
planNode.GetBeams(beams)

for i in range(beams.GetNumberOfItems()):
    proxyBeamNode = beams.GetItemAsObject(i)
    beamName = proxyBeamNode.GetName()

    # Find the sequence browser for this beam
    browserNode = slicer.mrmlScene.GetFirstNodeByName(beamName + '_SequenceBrowser')
    if not browserNode:
        # Static beam — read directly from the beam node
        print(f"  X1Jaw={proxyBeamNode.GetX1Jaw()}, X2Jaw={proxyBeamNode.GetX2Jaw()}")
        print(f"  Y1Jaw={proxyBeamNode.GetY1Jaw()}, Y2Jaw={proxyBeamNode.GetY2Jaw()}")
        continue

    # Dynamic beam — iterate control points via the sequence
    beamSeqNode = browserNode.GetMasterSequenceNode()
    nCPs = beamSeqNode.GetNumberOfDataNodes()
    print(f"Beam '{beamName}' has {nCPs} control points")

    for cp in range(nCPs):
        browserNode.SetSelectedItemNumber(cp)
        # After setting the index, the proxy node reflects this CP's data
        print(f"  CP{cp}: Gantry={proxyBeamNode.GetGantryAngle():.1f}, "
              f"Collimator={proxyBeamNode.GetCollimatorAngle():.1f}, "
              f"Couch={proxyBeamNode.GetCouchAngle():.1f}")
        print(f"    Jaws X=[{proxyBeamNode.GetX1Jaw():.1f}, {proxyBeamNode.GetX2Jaw():.1f}] "
              f"Y=[{proxyBeamNode.GetY1Jaw():.1f}, {proxyBeamNode.GetY2Jaw():.1f}] mm")

</code></pre>
<h3><a name="p-134376-h-2-access-mlc-leaf-positions-per-control-point-4" class="anchor" href="#p-134376-h-2-access-mlc-leaf-positions-per-control-point-4" aria-label="Heading link"></a>2. Access MLC Leaf Positions Per Control Point</h3>
<p>The MLC data is stored in a <code>vtkMRMLTableNode</code> with 3 columns:</p>
<ul>
<li>Column 0: leaf-pair boundary positions</li>
<li>Column 1: leaf side-1 positions (Bank A)</li>
<li>Column 2: leaf side-2 positions (Bank B)</li>
</ul>
<pre><code class="lang-auto">    for cp in range(nCPs):
        browserNode.SetSelectedItemNumber(cp)

        mlcTable = proxyBeamNode.GetMultiLeafCollimatorTableNode()
        if mlcTable:
            table = mlcTable.GetTable()
            nLeafPairs = table.GetNumberOfRows()
            boundaries = [table.GetValue(row, 0).ToDouble() for row in range(nLeafPairs)]
            bankA = [table.GetValue(row, 1).ToDouble() for row in range(nLeafPairs)]
            bankB = [table.GetValue(row, 2).ToDouble() for row in range(nLeafPairs)]
            print(f"  CP{cp} MLC: {nLeafPairs} leaf pairs")
            print(f"    Bank A: {bankA[:5]}...")
            print(f"    Bank B: {bankB[:5]}...")

</code></pre>
<h3><a name="p-134376-h-3-cumulativemetersetweight-dose-per-mu-5" class="anchor" href="#p-134376-h-3-cumulativemetersetweight-dose-per-mu-5" aria-label="Heading link"></a>3. CumulativeMetersetWeight / Dose per MU</h3>
<p><strong>This is not stored in MRML nodes.</strong> SlicerRT discards it during import. Read it directly from the DICOM file using <strong>pydicom</strong>:</p>
<pre><code class="lang-auto">import pydicom

rtplan_path = r"C:\path\to\RTPLAN.dcm"
ds = pydicom.dcmread(rtplan_path)

for beam in ds.BeamSequence:
    beam_name = beam.BeamName
    final_mu = beam.FinalCumulativeMetersetWeight  # or use FractionGroupSequence for actual MU
    print(f"\nBeam: {beam_name}")
    for cp_idx, cp in enumerate(beam.ControlPointSequence):
        mu_weight = cp.CumulativeMetersetWeight
        print(f"  CP{cp_idx}: CumulativeMetersetWeight={mu_weight}")

        # Jaw positions (only present at CP0 or when they change)
        if hasattr(cp, 'BeamLimitingDevicePositionSequence'):
            for bld in cp.BeamLimitingDevicePositionSequence:
                print(f"    {bld.RTBeamLimitingDeviceType}: {list(bld.LeafJawPositions)}")

</code></pre>
<p>The actual MU at each CP = <code>(CumulativeMetersetWeight / FinalCumulativeMetersetWeight) * BeamMeterset</code>, where <code>BeamMeterset</code> is in the <code>FractionGroupSequence &gt; ReferencedBeamSequence</code>.</p>
<h3><a name="p-134376-h-4-beam-projection-image-without-a-patient-body-6" class="anchor" href="#p-134376-h-4-beam-projection-image-without-a-patient-body-6" aria-label="Heading link"></a>4. Beam Projection Image Without a Patient Body</h3>
<p>This is not a DRR (which requires CT). You want an <strong>aperture projection image</strong> — a 2D image showing the MLC/jaw opening as seen from the source. Use matplotlib or numpy:</p>
<pre><code class="lang-auto">import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

def render_beam_aperture(x1jaw, x2jaw, y1jaw, y2jaw,
                          boundaries, bankA, bankB,
                          image_size_mm=400, resolution=512,
                          title="", output_path=None):
    """Render MLC/jaw aperture at a single control point."""
    px_per_mm = resolution / image_size_mm
    half = image_size_mm / 2.0

    # White background = open, black = blocked
    img = np.zeros((resolution, resolution), dtype=np.float32)

    def mm_to_px(x, y):
        col = int((x + half) * px_per_mm)
        row = int((half - y) * px_per_mm)  # y flipped
        return col, row

    # Jaw aperture rectangle (in BLD coordinate system)
    for row_idx in range(len(boundaries) - 1):
        leaf_y1 = boundaries[row_idx]
        leaf_y2 = boundaries[row_idx + 1]
        # Skip if leaf pair outside jaw Y
        if leaf_y2 &lt; y1jaw or leaf_y1 &gt; y2jaw:
            continue
        leaf_x1 = max(bankA[row_idx], x1jaw)
        leaf_x2 = min(bankB[row_idx], x2jaw)
        if leaf_x2 &lt;= leaf_x1:
            continue
        # Fill open area
        c1, r2 = mm_to_px(leaf_x1, leaf_y1)
        c2, r1 = mm_to_px(leaf_x2, leaf_y2)
        c1 = max(0, min(c1, resolution-1))
        c2 = max(0, min(c2, resolution-1))
        r1 = max(0, min(r1, resolution-1))
        r2 = max(0, min(r2, resolution-1))
        img[r1:r2, c1:c2] = 1.0

    fig, ax = plt.subplots(figsize=(6, 6))
    extent = [-half, half, -half, half]
    ax.imshow(img, cmap='gray', origin='lower', extent=extent, vmin=0, vmax=1)
    ax.set_xlabel('X (mm, BLD coords)')
    ax.set_ylabel('Y (mm, BLD coords)')
    ax.set_title(title)
    if output_path:
        plt.savefig(output_path, dpi=150, bbox_inches='tight')
    else:
        plt.show()
    plt.close()

# --- Full loop: one projection image per control point per beam ---
import os

output_dir = r"C:\output\apertures"
os.makedirs(output_dir, exist_ok=True)

for i in range(beams.GetNumberOfItems()):
    proxyBeamNode = beams.GetItemAsObject(i)
    beamName = proxyBeamNode.GetName()
    browserNode = slicer.mrmlScene.GetFirstNodeByName(beamName + '_SequenceBrowser')
    if not browserNode:
        continue

    beamSeqNode = browserNode.GetMasterSequenceNode()
    nCPs = beamSeqNode.GetNumberOfDataNodes()

    for cp in range(nCPs):
        browserNode.SetSelectedItemNumber(cp)

        mlcTable = proxyBeamNode.GetMultiLeafCollimatorTableNode()
        if not mlcTable:
            continue
        table = mlcTable.GetTable()
        n = table.GetNumberOfRows()
        boundaries = [table.GetValue(r, 0).ToDouble() for r in range(n)]
        bankA     = [table.GetValue(r, 1).ToDouble() for r in range(n)]
        bankB     = [table.GetValue(r, 2).ToDouble() for r in range(n)]

        gantry = proxyBeamNode.GetGantryAngle()
        title = f"{beamName} | CP{cp} | Gantry={gantry:.1f}\u00b0"
        out_path = os.path.join(output_dir, f"{beamName}_CP{cp:03d}.png")

        render_beam_aperture(
            x1jaw=proxyBeamNode.GetX1Jaw(),
            x2jaw=proxyBeamNode.GetX2Jaw(),
            y1jaw=proxyBeamNode.GetY1Jaw(),
            y2jaw=proxyBeamNode.GetY2Jaw(),
            boundaries=boundaries,
            bankA=bankA,
            bankB=bankB,
            title=title,
            output_path=out_path
        )
        print(f"Saved: {out_path}")

</code></pre>
<h3><a name="p-134376-key-points-summary-7" class="anchor" href="#p-134376-key-points-summary-7" aria-label="Heading link"></a>Key Points Summary</h3>
<div class="md-table">
<table>
<thead>
<tr>
<th>Data</th>
<th>Source</th>
<th>Python Access</th>
</tr>
</thead>
<tbody>
<tr>
<td>Jaw X/Y positions</td>
<td><code>vtkMRMLRTBeamNode</code></td>
<td><code>GetX1Jaw()</code>, <code>GetX2Jaw()</code>, <code>GetY1Jaw()</code>, <code>GetY2Jaw()</code></td>
</tr>
<tr>
<td>MLC leaf positions</td>
<td><code>vtkMRMLTableNode</code> linked to beam</td>
<td><code>GetMultiLeafCollimatorTableNode()</code> → <code>GetTable()</code></td>
</tr>
<tr>
<td>Gantry/Couch/Collimator angles</td>
<td><code>vtkMRMLRTBeamNode</code></td>
<td><code>GetGantryAngle()</code>, <code>GetCouchAngle()</code>, <code>GetCollimatorAngle()</code></td>
</tr>
<tr>
<td>CumulativeMetersetWeight</td>
<td>DICOM only — not in MRML</td>
<td>pydicom: <code>cp.CumulativeMetersetWeight</code></td>
</tr>
<tr>
<td>Iterate control points</td>
<td><code>vtkMRMLSequenceBrowserNode</code></td>
<td><code>SetSelectedItemNumber(cp_idx)</code></td>
</tr>
<tr>
<td>DRR image (needs CT)</td>
<td><code>DrrImageComputation</code> module</td>
<td><code>slicer.modules.drrimagecomputation.logic().ComputePlastimatchDRR(...)</code></td>
</tr>
</tbody>
</table>
</div><p>For the aperture image the matplotlib approach above works without any CT data. For a true radiograph-style projection image you’d use <code>DrrImageComputation</code> with a CT volume — see the test at <a>DrrImageComputationTest.py</a>.</p>

---

## Post #3 by @Aki (2026-06-16 23:16 UTC)

<p>Dear Csaba Pinter,</p>
<p>Thank you so much for kindly sending codes.</p>
<p>It is very helpful. I will learn from the codes.</p>
<p>Thanks a lot.</p>
<p>Aki</p>

---
