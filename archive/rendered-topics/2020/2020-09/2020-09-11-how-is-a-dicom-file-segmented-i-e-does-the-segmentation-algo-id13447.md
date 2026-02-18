# How is a DICOM file segmented? i.e. Does the segmentation algorithm consider one voxel thickness layer at a time?

**Topic ID**: 13447
**Date**: 2020-09-11
**URL**: https://discourse.slicer.org/t/how-is-a-dicom-file-segmented-i-e-does-the-segmentation-algorithm-consider-one-voxel-thickness-layer-at-a-time/13447

---

## Post #1 by @Joshua_Mathew_Jacob (2020-09-11 18:34 UTC)

<p>I know this is a very vague question but I’ve kind of understood how image segmentation works in 2D. When it comes to DICOM files, I know that a slice is basically a 3D image made of voxels, where voxel thickness depends on slice thickness, FOV, matrix size etc. This means a slice could be an 3D array whose 3rd dimension depends on voxel thickness.<br>
Eg. if I have a 512x512 matrix size, slice thickness 1.25, voxel thickness 0.25, then that slice would be consist of 512x512x5 voxels??</p>
<p>So, how does the segmentation happen here? Is each layer of one voxel thickness segmented at a time using the 2D principles? From my understanding, voxels are also just assigned an intensity value like pixels. So if we look at a single voxel thick layer it will look like a 2D image. Please correct me if I’m wrong.</p>
<p>Thanking you in advance for your patience to read this.</p>

---

## Post #2 by @lassoan (2020-09-11 18:57 UTC)

<p>For segmentations, you almost always want to see an infinitely thin cross-section of the volume. Thick slices (combining voxels along the slice plane normal with min/max/mean operation) are only used for very specific tasks, such as making small lesions easier to notice or make 3D shapes more recognizable without having a true 3D view.</p>
<p>Using traditional, fully manual 2D segmentation tools you would normally delineate a structure on each slice of a volume along a chosen axis. This is of course very time-consuming and the quality is generally quite poor, because users may draw contours inconsistently between neighbor slices where the structure’s boundaries were not clearly visible. You can improve results by iterating through all the slices in the other two axes as well and correcting any inconsistencies. If you repeat this review/touch-up of cross sections along all 3 axes several times then segmentation will have good quality, but it takes so much time that is very rarely done, as it is rarely necessary and most often it is not possible to have “perfect” segmentation anyway.</p>
<p>With 3D segmentation methods, you provide inputs seeds, intensity ranges, constraints, etc. and the algorithms compute consistent, smooth regions in 3D, taking into account all the inputs and the entire 3D volume at once.</p>
<p>You can find an overview of image segmentation in 3D Slicer <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">here</a> and description of built-in segmentation tools <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html">here</a>.</p>

---

## Post #3 by @Joshua_Mathew_Jacob (2020-09-11 19:12 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for your reply. I think you have cleared my doubt. However is there a written algorithm (like a psuedo-code) that explains the various 3D segmentation methods?<br>
For eg: I think global thresholding in 3D would be sort of like the following :<br>
g(x,y,z)={a, if f(x,y,z)&gt;T ;  0 if f(x,y,z)&lt;T}  where a is some intensity value and T is threshold.<br>
Another doubt I have now is that how are pixel/voxel cordinates given? Are the cordinate values based on geometric centre?</p>

---

## Post #4 by @lassoan (2020-09-11 19:19 UTC)

<p>Probably you can find overview and categorization of image segmentation methods in medical image computing textbooks. You may find <a href="https://itk.org/ItkSoftwareGuide.pdf">ITK Software Guide</a> (book 2, chapter 4) useful.</p>

---

## Post #5 by @Joshua_Mathew_Jacob (2020-09-11 19:52 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a>. I have another query, I have seen that there are certain segmentations done in which region growing is combined with thresholding (specifically adaptive/variable thresholding) .<br>
Why is such a process done? Would not region growing work fine on its own?</p>

---

## Post #6 by @lassoan (2020-09-11 19:58 UTC)

<p>Region growing’s main issue that you can easily end up with huge segmentation errors due to leaks. You almost always need to constrain it/combine with other methods to prevent this.</p>

---
