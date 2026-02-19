---
topic_id: 10372
title: "Surface Generation From Label Map Volume"
date: 2020-02-20
url: https://discourse.slicer.org/t/10372
---

# Surface generation from label map volume

**Topic ID**: 10372
**Date**: 2020-02-20
**URL**: https://discourse.slicer.org/t/surface-generation-from-label-map-volume/10372

---

## Post #1 by @Aep93 (2020-02-20 23:33 UTC)

<p>Hello all,<br>
I am trying a code  for generating surface from a label map volume. When I enter the following command:</p>
<pre><code class="lang-auto">reconstructSurface.SetInputConnection(threshold.GetOutputPort())
reconstructSurface.SetProjectionPlaneMode(vtk.VTK_BEST_FITTING_PLANE)
</code></pre>
<p>I will get the following error:</p>
<pre><code class="lang-auto">File "&lt;console&gt;", line 1*
    reconstructSurface.SetInputConnection(threshold.GetOutputPort()) 
    reconstructSurface.SetProjectionPlaneMode(vtk.VTK_BEST_FITTING_PLANE)*
SyntaxError: invalid syntax*
</code></pre>
<p>Can anyone help me about it?<br>
Thanks</p>

---

## Post #2 by @lassoan (2020-02-21 00:16 UTC)

<p>Point cloud reconstruction filters are not suitable for creating surfaces from labelmaps. Instead, you can use marching cubes or flying edges filter, followed by surface smoothing. In Slicer, you can do all the steps with just two lines of code - see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_segmentation_from_a_labelmap_volume_and_display_in_3D">here</a>.</p>

---

## Post #3 by @Aep93 (2020-02-21 15:25 UTC)

<p>Thank you very much for your comment. I used the code you mentioned but what I get is something like a volume. Actually, I want to segment a tissue with very small thickness (eardrum) and convert my model to a surface so that I can use it as shell element if FEM packages. Do you have any suggestion for that?<br>
Thanks and regards.</p>

---

## Post #4 by @lassoan (2020-02-21 15:57 UTC)

<p>OK, if you want to reconstruct an open surface from points then surface reconstruction filters can make sense. You may use markups fiducials to define surface points instead of derive them from labelmaps.</p>
<p>You got the error message above because of a typo (you typed a “*” character at the end of the line that caused the syntax error).</p>

---

## Post #5 by @Aep93 (2020-02-21 16:32 UTC)

<p>Thank you very much for your response.</p>

---
