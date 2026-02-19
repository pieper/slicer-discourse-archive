---
topic_id: 12481
title: "Overlay Color Onto Vtkmrmlscalarvolumenode Image"
date: 2020-07-10
url: https://discourse.slicer.org/t/12481
---

# Overlay color onto vtkMRMLScalarVolumeNode image

**Topic ID**: 12481
**Date**: 2020-07-10
**URL**: https://discourse.slicer.org/t/overlay-color-onto-vtkmrmlscalarvolumenode-image/12481

---

## Post #1 by @rohan_n (2020-07-10 17:29 UTC)

<p>For a Slicer module I am developing, the user selects which image they want to use as an input by selecting its vtkMRMLScalarVolumeNode from a dropdown menu.</p>
<p>Then, the user presses a button to colorize the tumor on that image. Pressing this button calls a function that takes the 3D numpy array from the vtkMRMLScalarVolumeNode, creates a 4D numpy array where the 4th dimension contains RGB color values, converts the 4D numpy array to: np.dtype([(‘R’, ‘u1’), (‘G’, ‘u1’), (‘B’, ‘u1’)]), and saves the final 3D RGB image as a NIFTI file.</p>
<p>Then the user can drag the NIFTI file into Slicer and see something like the image below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86b095a584dccda1f28ab18699c731419e294c69.png" data-download-href="/uploads/short-url/jdwjkcQoM23d93mQM2TILMtB7AJ.png?dl=1" title="sercolor" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86b095a584dccda1f28ab18699c731419e294c69_2_690x423.png" alt="sercolor" data-base62-sha1="jdwjkcQoM23d93mQM2TILMtB7AJ" width="690" height="423" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86b095a584dccda1f28ab18699c731419e294c69_2_690x423.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86b095a584dccda1f28ab18699c731419e294c69.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86b095a584dccda1f28ab18699c731419e294c69.png 2x" data-dominant-color="494344"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sercolor</span><span class="informations">867×532 89.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Instead of creating a .nii file that contains both the background image from the input vtkMRMLScalarVolumeNode and a blue/green/purple region on top of the tumor, I would prefer to continue displaying the input image in its original vtkMRMLScalarVolumeNode and display the blue/green/purple region as a separate object that is overlayed on top of the input image. In addition, I would like this blue/green/purple region to remain visible even after the user selects a different vtkMRMLScalarVolumeNode from the dropdown menu.</p>
<p>Is it possible to make this change that I want, and if so, could you please include some example lines of code that would help me figure out how to incorporate this change into my Python scripted module?</p>
<p>Thanks,<br>
Rohan Nadkarni</p>

---

## Post #2 by @lassoan (2020-07-10 17:34 UTC)

<p>You can display the grayscale image as background volume and the color image as foreground volume using <code>slicer.util.setSliceViewerLayers()</code>.</p>

---

## Post #3 by @rohan_n (2020-07-10 19:15 UTC)

<p>Andras,</p>
<p>Thanks for the suggestion. However, I’m having trouble adding the color image to a vtkMRMLScalarVolumeNode.</p>
<p>By default, this numpy image (img_np_rgb) has dimensions of 512x152x168x3. I think the vtkMRMLScalarVolumeNode expects a 3D input, so trying to add this 4D image to the node results in an error.</p>
<p>In order to make it possible to save the 3D color image as a NIFTI, I had to do this:</p>
<p>rgb_dtype = np.dtype([(‘R’,‘u1’),(‘G’,‘u1’),(‘B’,‘u1’)])<br>
rgb_typed = img_np_rgb.view(rgb_dtype).reshape(shape_3d)</p>
<p>where shape_3d is the shape of the original image without color added.</p>
<p>When I try to add rgb_typed to the vtkMRMLScalarVolumeNode, I also get an error.</p>
<p>What is the correct way to reformat img_np_rgb so that it can be added to a vtkMRMLScalarVolumeNode?</p>
<p>Thanks,<br>
Rohan</p>

---

## Post #4 by @lassoan (2020-07-10 20:12 UTC)

<p>You can create a “vtkMRMLVectorVolumeNode” and set its voxels from a numpy array using <a href="https://github.com/Slicer/Slicer/blob/b13a49465eec642a3bd9c2d5c50b2afb57088259/Base/Python/slicer/util.py#L1091-L1125"><code>slicer.util.updateVolumeFromArray()</code></a> convenience function.</p>

---

## Post #5 by @rohan_n (2020-07-10 21:55 UTC)

<p>After incorporating your suggestions from both comments, I’ve resolved this issue.<br>
Thanks for your help Andras!</p>

---
