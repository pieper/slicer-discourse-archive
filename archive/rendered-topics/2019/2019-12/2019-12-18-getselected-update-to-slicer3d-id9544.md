# GetSelected() update to Slicer3D

**Topic ID**: 9544
**Date**: 2019-12-18
**URL**: https://discourse.slicer.org/t/getselected-update-to-slicer3d/9544

---

## Post #1 by @fraca (2019-12-18 08:34 UTC)

<p>Hi, i’mt trying to convert this code in Slicer 4.10.2, but i don’t know how to update the function GetSelected(). Can you help me?</p>
<blockquote>
<p>self.LabeledVolumeSelector = slicer.vtkSlicerNodeSelectorWidget()<br>
self.SelectedVolumeSelector = slicer.vtkSlicerNodeSelectorWidget()</p>
</blockquote>
<blockquote>
<p>labeledImage = self.LabeledVolumeSelector.GetSelected().GetImageData()<br>
selectedImage = self.SelectedVolumeSelector.GetSelected().GetImageData()</p>
</blockquote>

---

## Post #2 by @pieper (2020-01-02 17:12 UTC)

<p>Looks like this was answered here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="9548">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/f19dbf/48.png" class="avatar">
    <a href="https://discourse.slicer.org/t/arrayfromvolume-issue/9548">arrayFromVolume issue</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I’ m trying to obtain the array of this volume, but i obtain some errors. Can you help me? 

labeledImage = self.LabeledVolumeSelector.currentNode().GetImageData() 
selectedImage = self.SelectedVolumeSelector.currentNode().GetImageData() 

I tried to use slicer.util.arrayFromVolume but i obtain this error: TypeError: object of type 'vtkCommonDataModelPython.vtkImageData' has no len()  
This is the code written in 3DSlicer 3.6, it may be helpful: 

labeledImage = self.LabeledVolumeSelector.GetSel…
  </blockquote>
</aside>


---

## Post #3 by @fraca (2020-01-07 17:18 UTC)

<p>I solved my problem using <code>currentNode()</code></p>

---
