---
topic_id: 20442
title: "Image After Registration Doesnt Have The Same Dimension Of T"
date: 2021-11-01
url: https://discourse.slicer.org/t/20442
---

# Image after registration doesn't have the same dimension of the fixed image

**Topic ID**: 20442
**Date**: 2021-11-01
**URL**: https://discourse.slicer.org/t/image-after-registration-doesnt-have-the-same-dimension-of-the-fixed-image/20442

---

## Post #1 by @S_Arbabi (2021-11-01 20:14 UTC)

<p>Hi,</p>
<p>I’m going to register a moving image to a fixed image and save the registered in a file.<br>
I load the two images in two nodes, do the registration (Elastix), and then call the SetAndObserveTransformNodeID on moving image.<br>
then I save the node, but it’s just the same dimensions as the original moving image. sample code:</p>
<pre><code class="lang-auto">        moving_image_node.SetAndObserveTransformNodeID(transform_node.GetID())
        slicer.util.saveNode(moving_image_node, path)
</code></pre>
<p>and if I harden the transformation then the size of the saved node is something different than the original fixed and moving image. sample code:</p>
<pre><code class="lang-auto">        moving_image_node.SetAndObserveTransformNodeID(transform_node.GetID())        
        logic = slicer.vtkSlicerTransformLogic()
        logic.hardenTransform(moving_image_node)
        slicer.util.saveNode(moving_image_node, path)
</code></pre>
<p>I appreciate any points helping out.</p>

---

## Post #2 by @mikebind (2021-11-01 20:31 UTC)

<p>Without hardening the transform, saving the moving image just saves the original (untransformed) version because all information about the transformation is in the transform, not the moving image’s volume node. When you harden the transform, it will modify the moving image, but the new image’s dimensions are probably determined by the extrema of the transformed moving image.  The transform itself does not know anything about the dimensions or resolution of the fixed image.  If what you want is a resampled version of the transformed moving image into the space and resolution of the fixed image volume, then you want to set the “Output volume” output of the Elastix module to something other than None.  If you set the output volume to be the same volume node as the input moving volume, then the input moving volume will be overwritten with the registered and resampled version; if you select “Create new volume” then the input moving volume will not be modified and the registered and resampled version will be saved to a new image volume. Either way, this new volume will have the same geometry as the fixed volume, but with the registered contents from the moving volume.</p>

---

## Post #3 by @lassoan (2021-11-01 20:40 UTC)

<p>You can also resample a transformed volume to have the same geometry as any other volume by hardening the transform and then using “Resample Scalar/Vector/DWI volume” module.</p>

---
