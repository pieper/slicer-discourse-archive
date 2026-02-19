---
topic_id: 44602
title: "Exporting Centreline"
date: 2025-09-26
url: https://discourse.slicer.org/t/44602
---

# Exporting centreline 

**Topic ID**: 44602
**Date**: 2025-09-26
**URL**: https://discourse.slicer.org/t/exporting-centreline/44602

---

## Post #1 by @Caitlin_Goldfinch (2025-09-26 19:10 UTC)

<p>I have created a centreline from a blood vessel segment. I want to export the centreline as an STL or OBJ file, so that I can import it into Fusion and use it as a path to extrude along. (Needing to 3d print this specific blood vessel. I know previous advice stated to use the markups for the models extension. However, that 3d model is not the correct diameter, nor is it hollow. Furthermore, upon import to Fusion, I can’t edit the vessel (even after converting to a mesh) to make it hollow. Is there any advice to achieve my goal of exporting the centreline? (mrk.json, .json and .fcsv can’t be read in Fusion)</p>

---

## Post #2 by @lassoan (2025-09-26 19:19 UTC)

<p>If Autodesk Fusion 360 supports import of a curve from any open file format, then you can ask any chatbot to write that file format.</p>
<p>For example, my prompt to ChatGPT:</p>
<blockquote>
<p>Write python script that I can run in 3D Slicer that exports control points of a markups curve into a CSV format that Autodesk Fusion 360 can read as a curve.</p>
</blockquote>
<p>This is the code it generated:</p>
<pre data-code-wrap="python"><code class="lang-python">import csv
import slicer

# --- User settings ---
outputFile = r"C:/Temp/curve_points.csv"  # Change path as needed
markupsNodeName = "OC"  # Name of your Markups Curve node in Slicer
# ---------------------

# Get the markups node
markupsNode = slicer.util.getNode(markupsNodeName)
nPoints = markupsNode.GetNumberOfControlPoints()

# Open CSV file for writing
with open(outputFile, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    # Write header for Fusion 360 (X,Y,Z)
    writer.writerow(["X", "Y", "Z"])
    
    # Write each control point
    for i in range(nPoints):
        ras = [0.0, 0.0, 0.0]
        markupsNode.GetNthControlPointPosition(i, ras)
        # Export in millimeters (Fusion 360 expects mm)
        writer.writerow(ras)

print(f"✅ Exported {nPoints} control points from '{markupsNodeName}' to {outputFile}")
</code></pre>
<p>I’ve tried it and it works flawlessly. If you want the points in LPS coordinate system (probably you do) or you want to get the dense curve points, not just the control points, then you can ask the chatbot to update the code accordingly (I’ve tested and it generates correct code). You can also ask the chatbot to create a simple GUI or run this operation on many files.</p>

---
