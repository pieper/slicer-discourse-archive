---
topic_id: 7251
title: "Loading Large Number Of Models"
date: 2019-06-19
url: https://discourse.slicer.org/t/7251
---

# Loading large number of models

**Topic ID**: 7251
**Date**: 2019-06-19
**URL**: https://discourse.slicer.org/t/loading-large-number-of-models/7251

---

## Post #1 by @ghnguyen (2019-06-19 21:13 UTC)

<p>Hi, I have more than 300 models that I want to load into Slicer at the same time, each is around 100-150 megabytes. Slicer was able to load all of them but when I tried to set one of the model visible along with a color legend bar using a custom module button, Slicer crashed and produced these error logs:</p>
<blockquote>
<p>[CRITICAL][Qt] 17.06.2019 15:12:42 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Slicer has caught an internal error.\n\nYou may be able to continue from this point, but results are undefined.\n\nSuggested action is to save your work and restart.\n\nIf you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="http://slicer.org" rel="noopener nofollow ugc">http://slicer.org</a>\n\n\nThe message detail is:\n\nException thrown in event: bad allocation”<br>
[ERROR][VTK] 17.06.2019 15:12:43 [vtkFloatArray (0000028A362E5320)] (d:\d\p\slicer-0-build\vtk\common\core\vtkGenericDataArray.txx:452) - Unable to allocate 961938 elements of size 4 bytes.<br>
[CRITICAL][Qt] 17.06.2019 15:12:43 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Slicer has caught an internal error.\n\nYou may be able to continue from this point, but results are undefined.\n\nSuggested action is to save your work and restart.\n\nIf you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="http://slicer.org" rel="noopener nofollow ugc">http://slicer.org</a>\n\n\nThe message detail is:\n\nException thrown in event: bad allocation”<br>
[ERROR][VTK] 17.06.2019 15:12:45 [vtkFloatArray (0000028AB87905A0)] (d:\d\p\slicer-0-build\vtk\common\core\vtkGenericDataArray.txx:452) - Unable to allocate 1487484 elements of size 4 bytes.<br>
[CRITICAL][Qt] 17.06.2019 15:12:45 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - “Slicer has caught an internal error.\n\nYou may be able to continue from this point, but results are undefined.\n\nSuggested action is to save your work and restart.\n\nIf you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="http://slicer.org" rel="noopener nofollow ugc">http://slicer.org</a>\n\n\nThe message detail is:\n\nException thrown in event: bad allocation”<br>
[WARNING][Qt] 17.06.2019 15:14:01 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - QWindowsWindow::setGeometry: Unable to set geometry 1602x1137+1920+23 on QWidgetWindow/‘qSlicerMainWindowWindow’. Resulting geometry:  1600x1137+1920+23 (frame: 8, 31, 8, 8, custom margin: 0, 0, 0, 0, minimum size: 1602x537, maximum size: 16777215x16777215).</p>
</blockquote>
<p>This does not happen if I only load around 150 or less models. Should I use another machine with larger memory or what is the error indicating here? Also, these models were originally Abaqus volumes that I have converted into vtu using the scripts available here with some modifications (<a href="https://github.com/Liujie-SYSU/odb2vtk" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Liujie-SYSU/odb2vtk: Python script converts Abaqus ODB files to VTK format for Paraview visualisation</a>). Thanks!</p>

---

## Post #2 by @pieper (2019-06-19 21:33 UTC)

<p>Hi - Anytime you see the “bad allocation” message it means you’ve run out of memory.  One option of course is to add more RAM to your computer or add virtual memory or maybe just use a bigger computer.</p>

---

## Post #3 by @lassoan (2019-06-19 21:39 UTC)

<p>You can reduce memory needs by 10-100x if you extract the visible outer surface of the mesh and visualize only that (instead of the unstructured grid volumetric mesh) and apply decimation.</p>

---

## Post #4 by @muratmaga (2019-06-20 20:11 UTC)

<p>Actually what is the proper why of doing this from CT scans? We will be segmenting a large number bones from mouse skulls, and for our purposes external surface is sufficient.</p>

---

## Post #5 by @lassoan (2019-06-20 22:06 UTC)

<p>Segmentation already produces surface mesh. <a class="mention" href="/u/ghnguyen">@ghnguyen</a> got his models imported from FEM software, which works with volumetric meshes.</p>

---
