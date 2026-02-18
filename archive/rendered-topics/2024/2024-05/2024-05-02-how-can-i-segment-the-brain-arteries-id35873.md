# How can I segment the brain arteries?

**Topic ID**: 35873
**Date**: 2024-05-02
**URL**: https://discourse.slicer.org/t/how-can-i-segment-the-brain-arteries/35873

---

## Post #1 by @vieimar (2024-05-02 14:59 UTC)

<p>The goal of my project is to segment the brain arteries. I tried the tutorial “Extraction of STL from DICOM images to generate geometry of cerebral arteries” but it didn’t work : Exception thrown in SimpleITK LaplacianImageFilter_Execute: D:\D\S\S-0-build\SimpleITK\Code\Common\include\sitkMemberFunctionFactory.hxx:158:<br>
sitk::ERROR: Pixel type: 16-bit unsigned integer is not supported in 3D by class slicer_itk::simple::LaplacianImageFilter. I think it’s bacause this filter can’t apply on 16 bits images.<br>
What can I do instead ?<br>
Also, where can I find the module “Vesselness Filtering” ? I can’t find it in modules or extension manager…I am new in using 3DSlicer ! Thank you for your help</p>

---

## Post #2 by @mikebind (2024-05-02 16:56 UTC)

<aside class="quote no-group" data-username="vieimar" data-post="1" data-topic="35873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/ee7513/48.png" class="avatar"> vieimar:</div>
<blockquote>
<p>Also, where can I find the module “Vesselness Filtering” ? I can’t find it in modules or extension manager…I am new in using 3DSlicer ! Thank you for your help</p>
</blockquote>
</aside>
<p>Vesselness Filtering is module of the SlicerVMTK extension.  If you install the SlicerVMTK extension, the Vesselness Filtering module will be among those added.</p>

---

## Post #3 by @vieimar (2024-05-03 15:09 UTC)

<p>Thank you for your response. Do you know of a method to create a hollow shell around the segmentation so that I can 3D print it later? Also, are there any automated segmentation methods available for arteries? Thanks again.</p>

---

## Post #4 by @mikebind (2024-05-03 15:55 UTC)

<p>You can create a hollow shell using the Hollow effect in Segment Editor. You may need to increase the resolution of your segmentation (see documentation <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough" rel="noopener nofollow ugc">here</a> or forum threads about increasing segmentation resolution) to achieve a desirable quality.</p>
<aside class="quote no-group" data-username="vieimar" data-post="3" data-topic="35873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/ee7513/48.png" class="avatar"> vieimar:</div>
<blockquote>
<p>are there any automated segmentation methods available for arteries?</p>
</blockquote>
</aside>
<p>I don’t know about this; I suspect people have tried though, so I would search the forum here to see what you can find.</p>
<aside class="quote no-group" data-username="vieimar" data-post="1" data-topic="35873">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/ee7513/48.png" class="avatar"> vieimar:</div>
<blockquote>
<p>Exception thrown in SimpleITK LaplacianImageFilter_Execute: D:\D\S\S-0-build\SimpleITK\Code\Common\include\sitkMemberFunctionFactory.hxx:158:<br>
sitk::ERROR: Pixel type: 16-bit unsigned integer is not supported in 3D by class slicer_itk::simple::LaplacianImageFilter. I think it’s bacause this filter can’t apply on 16 bits images.<br>
What can I do instead ?</p>
</blockquote>
</aside>
<p>You could try using Cast Scalar Volume module to change the data type, perhaps to float or double (I’m not sure what the LaplacianImageFilter wants, but I’m guessing it’s the ability to have non-integer values).</p>

---

## Post #5 by @vieimar (2024-05-06 15:44 UTC)

<p>Thank you for your help! I am new with 3DSlicer.<br>
The segmentation of my image is of good quality and is not very complex. So, as suggested, I applied the Hollow module to my segmentation. However, I noticed that the larger arteries were hollow while the smaller ones were solid. I tried changing several parameters such as the shell thickness. Furthermore, I don’t understand why the segmentation is no longer displayed once the shell is created. I also wanted to display the diameter of the arteries of my shell using “Markups” and “Line,” but I am unable to display the value. Therefore, I used “Segment Statistics,” which displayed a table with volume values, but it did not show the diameters. How can I ensure that the shell has properly enveloped my segmentation? Thank you again.</p>

---

## Post #6 by @mikebind (2024-05-06 16:42 UTC)

<p>The “Hollow” tool replaces the existing segment with the hollowed version of the segment.  If you would like to have both, then you can make a copy by creating a new segment and making it a copy of the original non-hollowed segment using “Logical Operators” → Copy.  Then, you can hollow one of the copies and leave the other one alone. If you have selected use current segment as inside surface on the hollow tool, then there should be no overlap between the hollowed segment and the original, so anywhere the original segment was present should be a hole in the hollowed version.  If you have selected to use the current segment as the medial surface or outside surface, then wherever the original is too thin (less than the shell thickness or less than double the shell thickness respectively) the lumen would be filled by the hollowed version.  You should also pay attention to the segment editor “Masking” settings, which could be responsible if you are not seeing the expected results.  When you run the hollow effect, you probably want the editable area to be “Everywhere”, the editable intensity range unchecked, and the modify other segments setting to be “Allow overlap”.</p>
<p>What is going wrong with the diameter measurement display?  There was a recent version of Slicer which had a bug where the length measurement was not displayed, but that has been fixed.  What version of Slicer are you using?</p>

---
