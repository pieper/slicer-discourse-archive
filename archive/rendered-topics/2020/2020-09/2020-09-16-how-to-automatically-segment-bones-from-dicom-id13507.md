---
topic_id: 13507
title: "How To Automatically Segment Bones From Dicom"
date: 2020-09-16
url: https://discourse.slicer.org/t/13507
---

# how to automatically segment bones from dicom

**Topic ID**: 13507
**Date**: 2020-09-16
**URL**: https://discourse.slicer.org/t/how-to-automatically-segment-bones-from-dicom/13507

---

## Post #1 by @Matt_Dean (2020-09-16 18:52 UTC)

<p>Hi, I have dicom files with multiple (separate) bones scanned at once. I want to automatically segment each bone and create a watertight surface mesh (ply format) for each bone. All the tutorials I am finding require manual segmentation but given the number of scans I need this to be as automated as possible, I’m guessing through the Python modules. Since the bones are already separated I think this should easy compared to segmenting out connected bones, where more human intervention is required. Also, I have an .hx script that can be run in Amira and works beautifully, but can no longer afford Amira. Can someone point me in the right direction to automatically segment out bones in Slicer? Thanks, much appreciated.</p>

---

## Post #2 by @lassoan (2020-09-17 01:34 UTC)

<p>All the tools are available in Slicer to fully automate this with minimal, very high-level Python scripting. The <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">Slicer script repository</a> probably contains examples for all the steps, but if you don’t find anything then let us know. To learn about basics of writing Python processing scripts or modules for Python, see this <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">tutorial</a>. Note that you can also use <a href="https://github.com/Slicer/SlicerJupyter">Slicer as a Jupyter notebook kernel</a>, if you prefer to work with notebooks.</p>
<p>Before you write the script, I would recommend to determine a good workflow using the Slicer GUI. Approximately these steps should work for you:</p>
<ul>
<li>Import and load DICOM image using DICOM module</li>
<li>Threshold</li>
<li>Split islands to segments (to add separate label to each bone)</li>
<li>Export to models (only STL and OBJ can be exported directly to files)</li>
<li>Save models as PLY</li>
</ul>
<p>If you want to solidify bones and/or make them easier to 3D print by converting to shell, then you can use WrapSolidify effect (provided by <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">SurfaceWrapSolidify extension</a>).</p>

---

## Post #3 by @Matt_Dean (2020-09-17 16:07 UTC)

<p>Hi Andras, thank you very much. Oftentimes just learning the names of the functions/extensions is a huge step forward for me. This is very helpful.</p>

---
