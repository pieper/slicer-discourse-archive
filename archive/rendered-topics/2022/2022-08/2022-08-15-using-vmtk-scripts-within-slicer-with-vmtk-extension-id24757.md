# Using vmtk scripts within Slicer with vmtk-extension

**Topic ID**: 24757
**Date**: 2022-08-15
**URL**: https://discourse.slicer.org/t/using-vmtk-scripts-within-slicer-with-vmtk-extension/24757

---

## Post #1 by @Doodads (2022-08-15 05:09 UTC)

<p>Hi, I have a vessel modelling workflow written in python which makes use of vmtk to convert a surface file (.vtk) to a mesh file (.vtu). I would like to migrate the workflow to use the Slicer environment as well as replace some of the scripts (e.g. vmtkcenterlines, vmtkcenterlinesnetwork) with those used in the slicer vmtk-extension.</p>
<p>The workflow makes use of the following vmtk scripts: <em>vmtksurfacereader, vmtksurfacekiteremoval, vmtksurfacesmoothing,  vmtkvmtkcenterlines, vmtkcenterlinesnetwork, vmtksurfaceclipper, vmtkbranchclipper, vmtksurfaceconnectivity, vmtkflowextensions, vmtkdistancetocenterlines, vmtksurfaceremeshing, vmtkmeshgenerator, vmtksurfacewriter, vmtkmeshwriter</em>. Apart from the above vmtk rendering scripts like <em>vmtksurfaceviewer</em>, etc… were used as well. Visualization can be handled by Slicer so I did not include those to the list.</p>
<p>May I confirm that all the vmtk scripts are contained within slicer when I install the extension, or is access limited to those used for the functions present within the extension? (e.g. Can I use vmtkmeshgenerator from within the slicer python interactor?)</p>
<p>Additionally, how to access vmtk from slicer? I can’t import vmtk within the slicer python interactor. I get the following error when I input <code>import vmtk</code></p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
ModuleNotFoundError: No module named 'vmtk'
</code></pre>

---

## Post #2 by @pieper (2022-08-15 15:05 UTC)

<p>I believe the packaging is different in the extension.  Have a look in the scripted modules to see how they access the vmtk filters and you should be able to do the same.</p>

---

## Post #3 by @nmg-earthling (2024-02-09 19:35 UTC)

<p>Doodads, did you have any success.  I’m struggling with the same problem.</p>

---
