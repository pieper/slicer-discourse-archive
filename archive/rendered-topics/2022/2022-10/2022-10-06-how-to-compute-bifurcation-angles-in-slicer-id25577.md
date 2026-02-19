---
topic_id: 25577
title: "How To Compute Bifurcation Angles In Slicer"
date: 2022-10-06
url: https://discourse.slicer.org/t/25577
---

# How to compute bifurcation angles in Slicer?

**Topic ID**: 25577
**Date**: 2022-10-06
**URL**: https://discourse.slicer.org/t/how-to-compute-bifurcation-angles-in-slicer/25577

---

## Post #1 by @tim (2022-10-06 14:31 UTC)

<p>Hi,</p>
<p>my goal is to compute centerlines, diameters and bifurcation angles of a vascular tree using Slicer and its Python interactor.</p>
<p>I managed to compute both centerlines and diameters using the vmtk scripted modules.<br>
However, I am not sure how to extract the bifurcation angles. Here’s what I’ve tried so far:</p>
<p>Following the vmtk <a href="http://www.vmtk.org/tutorials/GeometricAnalysis.html" rel="noopener nofollow ugc">tutorial</a> I set up the following workflow:</p>
<ol>
<li>Compute centerlines using ExtractCenterline scripted module → Output: centerline</li>
<li>Split up centerline into separate branches using branch extractor script → Output: branchCenterlines</li>
<li>Compute bifurcation reference systems using branchCenterlines → Output: reference systems</li>
<li>Compute bifurcation vectors using branchCenterlines and reference systems</li>
</ol>
<p>For steps 2-4, I use the code found in the “Execute()” method of the respective vmtk script (e.g. from <a href="https://github.com/vmtk/vmtk/blob/master/vmtkScripts/vmtkbifurcationreferencesystems.py" rel="noopener nofollow ugc">here</a>)</p>
<p>My code runs without any errors but I cannot really make sense of the output (-&gt; centerlineBifurcationVectors.GetOutput()) so I am wondering if what I am doing is correct.</p>
<p>My questions are:</p>
<ol>
<li>Is my workflow / approach for computing the bifurcation angles correct?</li>
<li>If yes, how can I use the output of the bifurcation vectors computation to find the bifurcation angles?</li>
</ol>
<p>Thanks a lot in advance!</p>

---

## Post #2 by @Bob_Cieri (2024-02-20 23:02 UTC)

<p>Hi Tim,</p>
<p>Did you ever get this to work? I’m interested in doing something similar and have been playing around with VMTK.</p>
<p>Bob</p>

---
