# Advice on editing STL files of bones 

**Topic ID**: 34721
**Date**: 2024-03-05
**URL**: https://discourse.slicer.org/t/advice-on-editing-stl-files-of-bones/34721

---

## Post #1 by @daniel_reale (2024-03-05 20:24 UTC)

<p>Well,</p>
<p>So I’m doing my final year project, and as part of it I’ve been printing various versions of the same femur. I had one with the internal cavities, I’ve had one that’s solid throughout, I’ve had big ones and small ones etc etc. The latest version was one that had been sliced in half length ways, this was good as It cut down on supports and it helped improve the print quality of both faces.</p>
<p>All of this was done just using 3D slicer and the STL’s it exported, however right now (Unless I’m just not thinking smart enough lol) I think I’ve reached a roadblock. So the final variation I’m hoping to make is either 1. The two halves, where one half has two holes and the other has two matching pegs so they can clip together… or 2. Two halves with holes that I can print separate dowls for.</p>
<p>This seems simple enough, however:</p>
<ol>
<li>The STL’s that 3D slicer exports are too complex and far too curvy for Fusion 360 to convert into 3d models. Decimating the models before exporting does not help this issue, I also want to avoid decimating as much as possible to avoid loss of surface info.</li>
<li>I’ve tried converting the STL’s in DWG’s to use in autocad, but again all of the faces make it far too complex to work with. I was mainly considering using Autocad so I could be numerically certain that everything was the right size and was placed correctly.</li>
</ol>
<p>Does anyone have any suggestions on how I could go about this? I’m sure someone has tried to accomplish something similar on here.</p>

---

## Post #2 by @pieper (2024-03-05 21:29 UTC)

<p>I would think you could use the scissors tool to make slots - e.g. use a rectangle shape and set symmetric slice cut of several centimeters.  Then just add that segment to one half of the bone and subtract it from the other side.</p>

---

## Post #3 by @lassoan (2024-03-07 03:17 UTC)

<p>Engineering CAD software generally cannot do anything with detailed meshes coming from image segmentation. That is why we added mesh editing tools in Slicer - Dynamic modeler module, Combine models module (in Sandbox extension), Surface toolbox module, etc.</p>
<p>For the pegs: If you find that the segmentation is not detailed enough and toh do not want to increase its resolution, then you can create cylinders using Create models module (SlicerIGT extension), position cylinders (using the new positioning handles in latest Slicer Preview Release), and use Combine models to add the cylinder to one half and remove it from the other half.</p>

---
