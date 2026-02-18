# Crop Volume reports error when input is a color volume

**Topic ID**: 16857
**Date**: 2021-03-30
**URL**: https://discourse.slicer.org/t/crop-volume-reports-error-when-input-is-a-color-volume/16857

---

## Post #1 by @giovform (2021-03-30 20:05 UTC)

<p>Steps to reproduce:</p>
<ol>
<li>Load any 2D image using “Add Data”;</li>
<li>Go to “Crop Volume” module;</li>
<li>On “Input ROI” select “Create new AnnotationROI”;</li>
<li>Change the ROI to any subregion of the image on the red slice view;</li>
<li>On “Output volume”, select “Create new Volume” item that exists below “Rename current Volume” item (this step is important to reproduce the error);</li>
<li>Click “Apply”;</li>
<li>Nothing will happen and the created volume will have zero dimensions;</li>
</ol>
<p>If you skip step 5, the error does not happen and the image is cropped successfully.</p>
<p>Using the latest stable release version 4.11.20210226.</p>
<p>The log file accuses the following error:</p>
<pre><code>[ERROR][VTK] 30.03.2021 17:15:12 [vtkSlicerCropVolumeLogic (0000022AEADACDB0)] (D:\D\S\Slicer-1\Modules\Loadable\CropVolume\Logic\vtkSlicerCropVolumeLogic.cxx:141) - CropVolume: output volume (vtkMRMLScalarVolumeNode) is not compatible with input volume (vtkMRMLVectorVolumeNode)</code></pre>

---

## Post #2 by @chir.set (2021-03-31 06:38 UTC)

<aside class="quote no-group" data-username="giovform" data-post="1" data-topic="16857">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giovform/48/4687_2.png" class="avatar"> giovform:</div>
<blockquote>
<p>Nothing will happen and the created volume will have zero dimensions;</p>
</blockquote>
</aside>
<p>With 4.13.0-2021-03-20 r29789 / 233d7ac, the cropped volume does have the ROI dimensions but is not auto-displayed in the slice views. You can show it using the views’ control widgets. The VTK error you mention does not appear though.</p>

---

## Post #3 by @lassoan (2021-04-03 02:22 UTC)

<p>The error message tells that you wanted to store the result of a cropped vector volume (most likely a color image) in a scalar volume. This is not possible.</p>
<p>Currently, the output volume selector only allows pre-creating scalar volumes. I’ll update the output volume selector to allow pre-creating vector volumes and display a more intuitive error message in the module GUI.</p>
<p>For now, if you crop a vector volume then you need to pre-create an output volume elsewhere (e.g., clone the input volume in Data module) or leave the default “Create new volume” setting to let the module create the appropriate output volume type automatically.</p>

---
