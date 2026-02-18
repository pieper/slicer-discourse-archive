# Clipping a model via scripting

**Topic ID**: 43963
**Date**: 2025-08-04
**URL**: https://discourse.slicer.org/t/clipping-a-model-via-scripting/43963

---

## Post #1 by @chz31 (2025-08-04 22:19 UTC)

<p>Hi all,</p>
<p>I am trying to clipping a model via scripting:</p>
<pre><code class="lang-auto">if not clipModelsNode:
    clipModelsNode = slicer.mrmlScene.AddNewNodeByClass(
        'vtkMRMLClipModelsNode', 'ClipModels')

# Get model node to clip
modelNode = slicer.util.getNode('left_orbit_fx')

# Enable clipping on the model's display node
modelDisplayNode = modelNode.GetDisplayNode()
modelDisplayNode.SetClipping(True)

modelDisplayNode.SetSliceDisplayMode(
    modelDisplayNode.SliceDisplayIntersection)

clipModelsNode.SetRedSliceClipState(1)    # Positive side of red plane
clipModelsNode.SetYellowSliceClipState(0) # Off
clipModelsNode.SetGreenSliceClipState(0)  # Off
</code></pre>
<p>However, only after I manually selected the global clip model ‘ClipModels’ in the Models module UI for the model node, I could use the above script to turn on and off the clipping effect</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0281aa721037a3a8c369b4cfc04179ac24f732a.png" data-download-href="/uploads/short-url/tHreFaZIOtnYfTXqOuGRECKButQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0281aa721037a3a8c369b4cfc04179ac24f732a_2_690x235.png" alt="image" data-base62-sha1="tHreFaZIOtnYfTXqOuGRECKButQ" width="690" height="235" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d0281aa721037a3a8c369b4cfc04179ac24f732a_2_690x235.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0281aa721037a3a8c369b4cfc04179ac24f732a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0281aa721037a3a8c369b4cfc04179ac24f732a.png 2x" data-dominant-color="EAEAEA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">913×311 30.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I feel I probably missed a step to add the model node to the clipping node but I could not find how to do that. Can I have some advice on this issue?</p>
<p>Thanks!</p>

---
