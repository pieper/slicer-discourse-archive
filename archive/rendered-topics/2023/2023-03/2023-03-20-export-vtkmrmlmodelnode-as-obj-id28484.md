# Export "vtkMRMLModelNode" as .OBJ

**Topic ID**: 28484
**Date**: 2023-03-20
**URL**: https://discourse.slicer.org/t/export-vtkmrmlmodelnode-as-obj/28484

---

## Post #1 by @Contente (2023-03-20 19:36 UTC)

<p>I have a segmentation that was converted into models in order to use the Surface Toolkit with them and access decimation and other optimization methods.</p>
<p>However, I want to export the models that have been processed to a .obj file, but the “slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsClosedSurfaceRepresentationToFiles()” only works for segments. Is there a way to do it without converting the models to a segmentation?</p>
<p>If not, how can I convert my models to a segmentation in python?</p>

---

## Post #2 by @Contente (2023-03-20 21:13 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07609ea8e08145784e69e50db32e38721419f622.png" data-download-href="/uploads/short-url/13glEgdPvYTQOL6EVpxAnwoBWSe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07609ea8e08145784e69e50db32e38721419f622.png" alt="image" data-base62-sha1="13glEgdPvYTQOL6EVpxAnwoBWSe" width="690" height="223" data-dominant-color="E1EAF0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">700×227 13.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93cae822c9947bf8728f5e0faef7e72c4f086f08.png" alt="image" data-base62-sha1="l5qUF8RykHOTjEv1y3Tc0hWLRtC" width="461" height="249"></p>
<p>In order to simplify, I want to be able to do the following steps with Python scripts.</p>
<p>When I use “slicer.modules.segmentations.logic().ImportModelToSegmentationNode()” method, my Slicer3D stops for 30 minutes and crashes.</p>
<p>And the “slicer.util.saveNode(model, outputFileName)” gives this error:<br>
Saving failed with all writers found for file “C:\Users\virtu\Desktop\python-slicer\obj_"muscle".obj” of type “ModelFile”</p>

---

## Post #3 by @lassoan (2023-03-21 01:32 UTC)

<p>You can save models into OBJ files using <code>slicer.util.exportNode</code> function. For example:</p>
<pre><code class="lang-python">modelNode = slicer.util.getNode('Model')
objFilePath = '/path/to/file.obj'
slicer.util.exportNode(modelNode, objFilePath)
</code></pre>

---

## Post #4 by @Contente (2023-03-22 13:36 UTC)

<p>Such a simple solution…</p>
<p>Anyway, thanks a lot! It solved my problem.</p>

---
