---
topic_id: 23512
title: "Setup Jupyter Desktop Server"
date: 2022-05-20
url: https://discourse.slicer.org/t/23512
---

# Setup Jupyter Desktop Server

**Topic ID**: 23512
**Date**: 2022-05-20
**URL**: https://discourse.slicer.org/t/setup-jupyter-desktop-server/23512

---

## Post #1 by @Tiago_Guiomar (2022-05-20 18:21 UTC)

<p>I’m trying to show the GUI in my jupyter notebook but I need to setup the Jupyter Desktop Server, any idea on how to do it?</p>

---

## Post #2 by @lassoan (2022-05-21 03:27 UTC)

<p>Please describe which <a href="https://github.com/Slicer/SlicerJupyter">installation option</a> did you choose, what exactly did, did you expect to happen, and what happened instead.</p>

---

## Post #3 by @Tiago_Guiomar (2022-05-24 18:30 UTC)

<p>I’m running option 2, everytime I run the following code  3D Slicer opens a new tab and won’t run its GUI in jupyter</p>
<pre><code class="lang-auto">app = slicernb.AppWindow(contents="full", windowScale=1)

slicer.util.selectModule("SegmentEditor")
segmentEditorWidget = slicer.modules.segmenteditor.widgetRepresentation().self().editor
segmentEditorNode = segmentEditorWidget.mrmlSegmentEditorNode()
segmentationNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(volumeNode)


display(app)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1edb7a3053a7229af34d5b7ff1368bae45692bcf.jpeg" data-download-href="/uploads/short-url/4oYye7jVGmmWz2lpmX9AUlVqDBt.jpeg?dl=1" title="Capturar" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1edb7a3053a7229af34d5b7ff1368bae45692bcf_2_517x167.jpeg" alt="Capturar" data-base62-sha1="4oYye7jVGmmWz2lpmX9AUlVqDBt" width="517" height="167" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1edb7a3053a7229af34d5b7ff1368bae45692bcf_2_517x167.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1edb7a3053a7229af34d5b7ff1368bae45692bcf.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1edb7a3053a7229af34d5b7ff1368bae45692bcf.jpeg 2x" data-dominant-color="E7E7E7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capturar</span><span class="informations">707×229 13.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
