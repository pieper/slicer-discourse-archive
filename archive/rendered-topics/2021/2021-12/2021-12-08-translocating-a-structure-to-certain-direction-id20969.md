---
topic_id: 20969
title: "Translocating A Structure To Certain Direction"
date: 2021-12-08
url: https://discourse.slicer.org/t/20969
---

# Translocating a structure to certain direction

**Topic ID**: 20969
**Date**: 2021-12-08
**URL**: https://discourse.slicer.org/t/translocating-a-structure-to-certain-direction/20969

---

## Post #1 by @sima (2021-12-08 17:52 UTC)

<p>Hi every body<br>
i want to a structure translocates to certain direction that i define. how can i do that?<br>
thanks a lot</p>

---

## Post #2 by @mikebind (2021-12-08 18:10 UTC)

<p>A more specific description of the problem you are trying to solve would allow more help.  In general, you can move things (for example image volumes, models, segmentations, markups, etc.) around in space in Slicer by using Transforms (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html" class="inline-onebox">Transforms — 3D Slicer documentation</a>). Create a transform node and apply it to the object you want to move, and then you can use the sliders in the Transforms module to interactively apply translations and/or rotations. If you are trying to align objects or images, then you are better off using a registration method (there are several available in Slicer).</p>

---

## Post #3 by @sima (2021-12-09 19:18 UTC)

<p>thanks a lot</p>
<p>In fact, I have had problem with this module and I do not know how to make exact translocation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8eea3cde902e4e686bac6fcd4abfcd746c268035.jpeg" data-download-href="/uploads/short-url/kohEtNComS4X9I8UkEXnEc3FCMl.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8eea3cde902e4e686bac6fcd4abfcd746c268035_2_690x366.jpeg" alt="1" data-base62-sha1="kohEtNComS4X9I8UkEXnEc3FCMl" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8eea3cde902e4e686bac6fcd4abfcd746c268035_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8eea3cde902e4e686bac6fcd4abfcd746c268035_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8eea3cde902e4e686bac6fcd4abfcd746c268035.jpeg 2x" data-dominant-color="ABAAAA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1363×723 196 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In this picture I want to move the red model  exactly on the skin and in the direction of the beam radiation. (Actually, moving in the direction of the center line of the beam radiation)<br>
when I use ’ linear transform ’ the model is not in the right place and goes out of range of the beam radiation.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2f1f52ab783cb168402851d0bc742e4402ca5b8.jpeg" data-download-href="/uploads/short-url/rOz1jxtBZ0WW3kQ5kErD45hbrba.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2f1f52ab783cb168402851d0bc742e4402ca5b8_2_690x349.jpeg" alt="2" data-base62-sha1="rOz1jxtBZ0WW3kQ5kErD45hbrba" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2f1f52ab783cb168402851d0bc742e4402ca5b8_2_690x349.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c2f1f52ab783cb168402851d0bc742e4402ca5b8_2_1035x523.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2f1f52ab783cb168402851d0bc742e4402ca5b8.jpeg 2x" data-dominant-color="A8A8A7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1359×689 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So, the transmission direction is incorrect and when I do the transitions in the PA and LR directions together, the result is not accurate… <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>
<p>Could you please help me ?</p>

---

## Post #4 by @mikebind (2021-12-10 18:29 UTC)

<p>Here is a function you could use to translate an object in a specified direction a specified distance.</p>
<pre><code class="lang-auto">def translateAlongVector(nodeToMove, directionVectorRAS, translationDistance):
  """ Moves nodeToMove by translationDistance the direction of directionVectorRAS.
  If nodeToMove already has a transform applied to it, this function updates that
  transform to translate the nodeToMove from it's current transformed location. If
  nodeToMove does not have an existing parent transform, then one is created for it.
  """
  # Create parent transform node if one does not exist
  transformNodeID = nodeToMove.GetTransformNodeID()
  if transformNodeID is None:
    # Need to create a new transform node
    transformNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLinearTransformNode', 'translationTransform')
    nodeToMove.SetAndObserveTransformNodeID(transformNode.GetID())
  else:
    # Get existing transform node
    transformNode =  slicer.mrmlScene.GetNodeByID(transformNodeID)
  # Determine translation vector
  import numpy as np
  unitDirectionVectorRAS = directionVectorRAS/np.linalg.norm(directionVectorRAS) # normalize
  translationVector = unitDirectionVectorRAS * translationDistance
  # Add translation to the 4x4 transformation matrix
  vtkTransformationMatrix = transformNode.GetMatrixTransformToParent()
  transformationMatrix = slicer.util.arrayFromVTKMatrix(vtkTransformationMatrix)
  transformationMatrix[:3,3] = transformationMatrix[:3,3] + translationVector
  transformNode.SetAndObserveMatrixTransformToParent( slicer.util.vtkMatrixFromArray(transformationMatrix) )
</code></pre>
<p>Example usage:</p>
<pre><code class="lang-auto">modelName = "myRedModel" # replace with the name of the object you want to move
modelNode = slicer.util.getNode(modelName)
beamDirection = [10, 20, 0] # a RAS (right, anterior, superior) vector describing the direction of the beam 
distanceToSkin = 30 # distance to move the model in mm
# apply the translation
translateAlongVector( modelNode, beamDirection, distanceToSkin)
</code></pre>

---
