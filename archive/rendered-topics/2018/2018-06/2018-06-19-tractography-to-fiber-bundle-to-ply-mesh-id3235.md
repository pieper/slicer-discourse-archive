# Tractography to Fiber Bundle to PLY mesh

**Topic ID**: 3235
**Date**: 2018-06-19
**URL**: https://discourse.slicer.org/t/tractography-to-fiber-bundle-to-ply-mesh/3235

---

## Post #1 by @Nicholas.jacobson (2018-06-19 22:53 UTC)

<p>Hello,<br>
Can anyone run me through the process for converting a tractography to a fiber bundle. Trying to explort the vtk file of curves for our tractography model into a PLY mesh. However, it appears I need to convert this into a fiber bundle prior to converting to a mesh.</p>
<p>When I run the Tractography to PLY mesh I get an error that says 'None type object has no attribute ‘SetName’</p>

---

## Post #2 by @ljod (2018-06-20 01:46 UTC)

<p>It looks like this data may have been loaded as a model. Please load it into slicer (when you add data to Slicer or drag and drop it into slicer) as a FiberBundle.</p>

---

## Post #3 by @lassoan (2018-06-20 02:01 UTC)

<p><a class="mention" href="/u/ljod">@ljod</a> FYI, you can define composite file extensions to give Slicer hint how to load a certain file type by default. For example, segmentations are saved as .nrrd files, but we use .seg.nrrd extension so that when we drag-and-drop a segmentation file to Slicer, it is offered to be loaded as “Segmentation” by default (instead of as a simple “Volume”). You could use a file extension such as .fb.ply to make the file loaded as FiberBundle by default (instead of “Model”).</p>

---

## Post #4 by @ljod (2018-06-20 02:12 UTC)

<p>That is great thank you. I didn’t know about this feature.</p>

---
