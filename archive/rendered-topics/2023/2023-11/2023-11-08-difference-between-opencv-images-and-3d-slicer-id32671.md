# Difference between opencv images and 3D slicer 

**Topic ID**: 32671
**Date**: 2023-11-08
**URL**: https://discourse.slicer.org/t/difference-between-opencv-images-and-3d-slicer/32671

---

## Post #1 by @Saman_Fouladi (2023-11-08 14:00 UTC)

<p>Hello. I trained my 2D unet with images which were loaded using opencv in png format. The predicted results are promising for organ segmentation. To work with 3D nrrd image (to show in 3D Slicer),  I convert a 3D image to 2D slides and then load them with SimpleITK.ReadImage (). After that I use from prediction model for organ segmentation . In this case the results are awful. Are loaded images using opencv very different in contrast with SimpleITK ? How can I deal with this problem?</p>

---

## Post #2 by @lassoan (2023-11-08 14:42 UTC)

<p>SimpleITK and OpenCV might use slightly different conventions (for example order of axes, or how you represent origin, spacing, and axis directions), but they can work on exactly the same images.</p>
<p>Note that OpenCV is developed by the computer vision community and you will find that their needs, assumptions, preferences, and conventions are quite different from the medical image computing community. It is easier to use libraries developed by the medical image computing community, such as ITK, VTK, MONAI, because they are designed to work well together and often used together.</p>
<aside class="quote no-group" data-username="Saman_Fouladi" data-post="1" data-topic="32671">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/saman_fouladi/48/68212_2.png" class="avatar"> Saman_Fouladi:</div>
<blockquote>
<p>To work with 3D nrrd image (to show in 3D Slicer), I convert a 3D image to 2D slides and then load them with SimpleITK.ReadImage ()</p>
</blockquote>
</aside>
<p>You do not need to split a 3D image to 2D slices to write to file. It is an unnecessary step that may slow down the processing and/or introduce errors. Instead, you can write the 3D image directly into a NRRD file using pynrrd; or if you are already using ITKPython or SimpleITK then you can convert your numpy array to an ITK image and use the ITK image writer.</p>

---

## Post #3 by @Saman_Fouladi (2023-11-08 17:52 UTC)

<p>Thank you very much for your valuable information. I trained my network with opencv images, because I had to work on 2D images. So should I train my network again with SimpleITK.ReadImage () for 2D images?</p>

---

## Post #4 by @lassoan (2023-11-09 02:55 UTC)

<p>What kind of images do you work with? Fluoroscopy, ultrasound, optical, …? Single image or a time sequence?</p>

---

## Post #5 by @Saman_Fouladi (2023-11-09 08:40 UTC)

<p>I am working on MRIs. I work on T2W images slide by slide.</p>

---

## Post #6 by @lassoan (2023-11-15 12:49 UTC)

<p>If you work with 3D medical images then it makes sense to use libraries that are developed fir this purpose, use ITKPython, SimpleITK, or Slicer readers/writers, work with 3D image objects and do the segmentation in 3D.</p>
<p>If you still want to do slice-by-slice segmentation in OpenCV (despite you can expect low-quality results from independently segmenting slices) then you can get the voxels of the input scalar volume and the output label volume as 3D numpy arrays, extract a slice, process it in OpenCV, and copy the processed voxels into a slice of the label volume array.</p>

---
