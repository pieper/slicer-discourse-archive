---
topic_id: 11117
title: "Apply A Smooth Dense Deformation"
date: 2020-04-15
url: https://discourse.slicer.org/t/11117
---

# Apply a smooth dense deformation

**Topic ID**: 11117
**Date**: 2020-04-15
**URL**: https://discourse.slicer.org/t/apply-a-smooth-dense-deformation/11117

---

## Post #1 by @labixin (2020-04-15 01:33 UTC)

<p>Hi all,</p>
<p>I need to do the data augmentation used by the 3-D Unet work (<a href="https://arxiv.org/abs/1606.06650" rel="nofollow noopener">paper link</a>): “Besides rotation, scaling and gray value augmentation, we apply a smooth dense deformation field on both data and ground truth labels. For this, we sample random vectors from a normal distribution with standard deviation of 4 in a grid with a spacing of 32 voxels in each direction and then apply a B-spline interpolation.”</p>
<p>Can I achieve this with any Slicer module? Hope for some advice. Thanks a lot.</p>
<p>Crayon</p>

---

## Post #2 by @pieper (2020-04-15 13:44 UTC)

<p>HI -</p>
<p>Yes, you should be able to just create a grid transform for that.  This code might help get you started.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/0560b7fffc371cbbea1bfd79586a21de3be9fb0f/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L580-L622" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/0560b7fffc371cbbea1bfd79586a21de3be9fb0f/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L580-L622" target="_blank">Slicer/Slicer/blob/0560b7fffc371cbbea1bfd79586a21de3be9fb0f/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L580-L622</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="580" style="counter-reset: li-counter 579 ;">
<li>def gridTransformFromCorners(self,volumeNode,sourceCorners,targetCorners):</li>
<li>  """Create a grid transform that maps between the current and the desired corners.</li>
<li>  """</li>
<li>  # sanity check</li>
<li>  columns, rows, slices = volumeNode.GetImageData().GetDimensions()</li>
<li>  cornerShape = (slices, 2, 2, 3)</li>
<li>  if not (sourceCorners.shape == cornerShape and targetCorners.shape == cornerShape):</li>
<li>    raise Exception("Corner shapes do not match volume dimensions %s, %s, %s" %</li>
<li>                      (sourceCorners.shape, targetCorners.shape, cornerShape))</li>
<li>
</li>
<li>  # create the grid transform node</li>
<li>  gridTransform = slicer.vtkMRMLGridTransformNode()</li>
<li>  gridTransform.SetName(slicer.mrmlScene.GenerateUniqueName(volumeNode.GetName()+' acquisition transform'))</li>
<li>  slicer.mrmlScene.AddNode(gridTransform)</li>
<li>
</li>
<li>  # place grid transform in the same subject hierarchy folder as the volume node</li>
<li>  shNode = slicer.vtkMRMLSubjectHierarchyNode.GetSubjectHierarchyNode(slicer.mrmlScene)</li>
<li>  volumeParentItemId = shNode.GetItemParent(shNode.GetItemByDataNode(volumeNode))</li>
<li>  shNode.SetItemParent(shNode.GetItemByDataNode(gridTransform), volumeParentItemId)</li>
<li>
</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/0560b7fffc371cbbea1bfd79586a21de3be9fb0f/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L580-L622" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2020-04-16 15:39 UTC)

<p>You may also create a thin-plate spline transform using SlicerIGT extension’s Fiducial Registration Wizard module. You just need to specify two markups fiducial point lists and the module creates a transform that transform each point to a corresponding point in the other list and smoothly interpolates between them. This way, you can very easily create a smoothly changing dense displacement field by just specifying a few displacement vectors.</p>

---

## Post #4 by @labixin (2020-09-18 09:16 UTC)

<p>Thanks a lot. I have done the data augmentation with Fiducial Registration Wizard module following your advice. The deformed images are satisfactory. Now I am preparing the scientific paper. I am not sure how to describe this operation as data augmentation step. Hope for some suggestions. Your help is highly appreciated!</p>
<p>Sincerely,</p>
<p>Crayon</p>

---

## Post #5 by @lassoan (2020-09-18 14:43 UTC)

<p>If you use SlicerIGT modules then please cite this paper:<br>
<a href="https://www.ncbi.nlm.nih.gov/pubmed/27344106">Ungi T, Lasso A, Fichtinger G. Open-source platforms for navigated image-guided interventions. Med Image Anal. 2016 Oct;33:181-6. doi: 10.1016/j.media.2016.06.011.</a></p>
<p>If possible, please also cite 3D Slicer as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#how-to-cite">here</a>.</p>
<p>Internally, Fiducial registration wizard module uses VTK’s thin-plate spline transform implementation. Algorithm details are described in this paper: <a href="https://doi.org/10.1016/S0895-6111(02)00091-5">https://doi.org/10.1016/S0895-6111(02)00091-5</a></p>

---
