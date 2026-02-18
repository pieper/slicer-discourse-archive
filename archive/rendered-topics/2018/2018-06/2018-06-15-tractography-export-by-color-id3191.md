# Tractography export by color 

**Topic ID**: 3191
**Date**: 2018-06-15
**URL**: https://discourse.slicer.org/t/tractography-export-by-color/3191

---

## Post #1 by @Nicholas.jacobson (2018-06-15 01:33 UTC)

<p>Hello,<br>
I’ve got a Tractography file in slicer with numerous colors. I’d like to export the curves with color or export the curves based on a color threshold. The idea with the latter is that I can export numerous files and bring them into another modeling program and assign the files to different layers based on color. Any ideas how to make this work?</p>

---

## Post #2 by @ihnorton (2018-06-15 01:52 UTC)

<p>Please try the <strong>Export tractography to PLY (mesh)</strong> module, available in the SlicerDMRI extension in nightly builds (since early April).</p>
<p>Note that we use PLY specifically because it supports color.</p>
<p>Most software with STL import also supports PLY, but if you specifically need OBJ (supports color) or STL (no color) you can <a href="https://github.com/SlicerDMRI/SlicerDMRI/wiki/How-to-export-atlas-or-tractography-for-visualization-in-Blender">convert in MeshLab</a>.</p>

---

## Post #3 by @Nicholas.jacobson (2018-06-15 15:37 UTC)

<p>Thank you. This is good to know but I’m need to keep these as curves and lines because we will be voxel printing. So to be more specific, is there a way to export curves and lines with color and/or segment these curves based on color?</p>

---

## Post #4 by @ihnorton (2018-06-15 16:44 UTC)

<p>What format are you looking for? I don’t know if STL support polylines, but at least VTK’s STL export does not seem to support that (the output is just a point cloud, I think; that’s why we apply a tube filter before export).</p>
<p>If you save as a PLY, then the colors will be stored per-vertex. If you save as VTK then the colors will be stored in an associated cell array.</p>
<p>Feel free to have a look at the code <a href="https://github.com/SlicerDMRI/SlicerDMRI/blob/master/Modules/Scripted/TractographyExportPLY/TractographyExportPLY.py">here</a>. It is Python so you can modify as-needed in a downloaded Slicer build without compiling yourself.</p>

---

## Post #5 by @ihnorton (2018-06-15 16:51 UTC)

<p>I should also mention that, as far as I understand, a number of people have used exactly this export process for 3D printing of tractography. The original export script is from <a class="mention" href="/u/pieper">@pieper</a>, and we made it into a module recently because this request comes up several times a month.</p>

---

## Post #6 by @Nicholas.jacobson (2018-06-15 17:10 UTC)

<p>And the process you mention and code is for the meshing ply?</p>
<p>It sounds like I might be able to export the vtk polylines and the color ply point cloud and color the lines by association.</p>
<p>Any format that exports with polylines in color works. We can work with a lot of different line based files. But the lines allow us to bitmap print or voxel print and keep file size low. Whereas the meshing is often way to big of a file.</p>

---

## Post #7 by @ihnorton (2018-06-15 19:15 UTC)

<p>The process I mentioned applies a tube filter to the streamlines, by default creating a 6-sided tube for each streamline, so memory usage goes up roughly 6x. # sides and radius are configurable. Each ring vertex is given the same color as the corresponding point had in Slicer’s viewer.</p>
<p>VTK does support polylines and is the most flexible option.</p>

---

## Post #8 by @Nicholas.jacobson (2018-06-15 19:33 UTC)

<p>Thanks I think I will export a vtk to rhino and then sort by direction. Then create seperate layers based on those directions.</p>

---

## Post #9 by @ljod (2018-06-15 19:40 UTC)

<p>A related option is to convert to voxels in Slicer using Tractography to Mask Image module. This upsamples along fibers to best fill in the intersected voxels, but it does not currently export colors. It could be helpful to take a look at the code.</p>
<p>It looks like we need to update the documentation for this module, as it seems to still be under the old name here:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/FiberBundleToLabelMap" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Modules/FiberBundleToLabelMap</a></p>

---
