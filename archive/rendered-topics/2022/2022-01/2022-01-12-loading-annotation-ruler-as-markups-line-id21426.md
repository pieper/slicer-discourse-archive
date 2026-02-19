---
topic_id: 21426
title: "Loading Annotation Ruler As Markups Line"
date: 2022-01-12
url: https://discourse.slicer.org/t/21426
---

# Loading Annotation Ruler as Markups Line

**Topic ID**: 21426
**Date**: 2022-01-12
**URL**: https://discourse.slicer.org/t/loading-annotation-ruler-as-markups-line/21426

---

## Post #1 by @jamesobutler (2022-01-12 20:49 UTC)

<p>If I have a bunch of annotation ruler node objects saved to disk as .acsv files, what is the correct way to load these into Slicer as Markups Line node objects? I would like to use the improved display node capabilities of the Markups Line node.</p>
<p>Using the Add Data dialog, I changed the description from “Annotation” to “Markups”, but then I just get an error on load.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a86e45a820e79da490225f769ac19518acdc23f5.png" data-download-href="/uploads/short-url/o20tg24TzuQymgZctuyl5UJYXul.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a86e45a820e79da490225f769ac19518acdc23f5.png" alt="image" data-base62-sha1="o20tg24TzuQymgZctuyl5UJYXul" width="517" height="310" data-dominant-color="FBFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">737×443 9.09 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6485d3ba511ae6f00e001a2b2e1a97287a434a15.png" alt="image" data-base62-sha1="elgt9smXc1P9G9c7xoZmunzIRbD" width="502" height="243"></p>
<pre><code class="lang-auto">[ERROR][VTK] 12.01.2022 15:48:44 [vtkSlicerMarkupsLogic (000002B87EDA8550)] (D:\D\P\Slicer-0\Modules\Loadable\Markups\Logic\vtkSlicerMarkupsLogic.cxx:875) - vtkSlicerMarkupsLogic::LoadMarkups failed: unrecognized file extension in C:/Users/JamesButler/Downloads/C_1.acsv
</code></pre>

---

## Post #2 by @jamesobutler (2022-01-13 17:23 UTC)

<p>Through python code I’ll load the Annotation Ruler, get the positions of the 2 points, remove the Annotation Ruler, add a Markups Line, add 2 points with the same positions as the old object.</p>
<pre><code class="lang-python">ruler_path = r"C:\Users\JamesButler\Downloads\C_1.acsv"
old_ruler_node = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLAnnotationRulerNode')
storage_node = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLAnnotationRulerStorageNode')
storage_node.SetFileName(ruler_path)
success = storage_node.ReadData(old_ruler_node)
pos1 = [0, 0, 0]
pos2 = [0, 0, 0]
old_ruler_node.GetPosition1(pos1)
old_ruler_node.GetPosition2(pos2)
slicer.mrmlScene.RemoveNode(old_ruler_node)
ruler_node = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsLineNode')
ruler_node.AddControlPoint(vtk.vtkVector3d(pos1))
ruler_node.AddControlPoint(vtk.vtkVector3d(pos2))
</code></pre>

---
