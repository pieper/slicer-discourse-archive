---
topic_id: 24852
title: "How To Export Segmentation As Gtlf Using Python Code"
date: 2022-08-21
url: https://discourse.slicer.org/t/24852
---

# How to export Segmentation as gtlf using python code

**Topic ID**: 24852
**Date**: 2022-08-21
**URL**: https://discourse.slicer.org/t/how-to-export-segmentation-as-gtlf-using-python-code/24852

---

## Post #1 by @Sirius_Chen (2022-08-21 15:20 UTC)

<p>Greetings!<br>
I need to export Segmentation as ONE gtlf file. I noticed I can use <a href="https://github.com/PerkLab/SlicerOpenAnatomy/" rel="noopener nofollow ugc">SlicerOpenAnatomy</a>, but using the python code——</p>
<pre><code class="lang-auto">exporter = vtk.vtkGLTFExporter()
exporter.SetRenderWindow(slicer.app.layoutManager().threeDWidget(0).threeDView().renderWindow())
exporter.SetFileName("c:/tmp/newfolder/mymodel.gltf")
exporter.Write()
</code></pre>
<p>——will export the entire scene and create a gltf file and several bin files.<br>
like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/280e807a53097579358f99ed3859e7055f19a794.png" alt="1661094927326" data-base62-sha1="5ImatlfdoElQhyWmDATyfNWNOxm" width="130" height="358"></p>
<p>Could anyone help me find the code that can export the Segmentation to ONE gtlf file?<br>
like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e863b1f1bc8a2d15425b7a6bf46a74c7b3d4f9fe.png" alt="image" data-base62-sha1="x9OmS39DlAAyvSdYyuKjasOuNY2" width="119" height="22"><br>
Thank you so much!</p>

---
