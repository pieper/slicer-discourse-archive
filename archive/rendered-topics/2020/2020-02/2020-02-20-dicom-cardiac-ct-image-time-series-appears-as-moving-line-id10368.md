# DICOM cardiac CT image time series appears as moving line

**Topic ID**: 10368
**Date**: 2020-02-20
**URL**: https://discourse.slicer.org/t/dicom-cardiac-ct-image-time-series-appears-as-moving-line/10368

---

## Post #1 by @ravi_nataraj (2020-02-20 16:27 UTC)

<p>Hi, everyone. I’m pretty new to 3D Slicer and Imaging in general. I’m trying to volume render a heart from a 2-chamber CT view, however, the format of the DICOM file is problematic. I have 20 instances (files) and every time I try to load it as a DICOM directory, it loads as very thin slices.</p>
<p>The image dimensions in the volume module are 256x256x1 and I have to resize it by changing the image spacing values. Another problem I have is whenever I cycle through each instance, it seems like I’m seeing a narrow “window” as the image below it is being translated as it moves. I’m not sure what to do because all the youtube videos I’ve watched show that cycling through each instance shows different perpendicular slices w/ a plane but this just seems like a long picture parallel to the plane and shows me sections of it as I cycle.</p>
<p>Also, when I try to volume render, I have to select scalar volume instead of multivolume when I load from the DICOM menu. Multivolume won’t let me even access the volume render menu but Scalar Volume (HLA/VLA FIESTA works, not ones from TriggerTime). Even so, with scalar volume, the render is like an extrusion through one plane. It doesn’t provide a 3D model of the heart, rather some distorted 3d lines passing through one plane (usually axial). My research professor may have mentioned that the CT images also have time instances associated with it, but I don’t know what to do that or how to even check.</p>
<p>I’ve tried reading some things online such as <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ#Image_is_stretched_or_compressed_along_one_axis" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/FAQ#Image_is_stretched_or_compressed_along_one_axis</a> where it tell me that the image is compressed along an axis but I’m not sure. Also, I’ve read <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2706116/" rel="nofollow noopener">https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2706116/</a> which says that modern CT uses thin slices but I’ve got no idea what to do.</p>
<p>Can anyone help me? Also, I apologize if the vocabulary I’ve used isn’t technical enough.</p>

---

## Post #2 by @lassoan (2020-02-20 17:38 UTC)

<aside class="quote no-group" data-username="ravi_nataraj" data-post="1" data-topic="10368">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ravi_nataraj/48/5748_2.png" class="avatar"> ravi_nataraj:</div>
<blockquote>
<p>Another problem I have is whenever I cycle through each instance, it seems like I’m seeing a narrow “window” as the image below it is being translated as it moves.</p>
</blockquote>
</aside>
<p>It looks like you have oblique slices, so probably you want to align the slice view to match the image acquisition axis direction. Click “Rotate to volume plane” button in the slice view controller.</p>
<aside class="quote no-group" data-username="ravi_nataraj" data-post="1" data-topic="10368">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ravi_nataraj/48/5748_2.png" class="avatar"> ravi_nataraj:</div>
<blockquote>
<p>The image dimensions in the volume module are 256x256x1 and I have to resize it by changing the image spacing values.</p>
</blockquote>
</aside>
<p>You cannot change the image dimensions. You can change the physical size by adjusting spacing, but if you load the image from a clinical CT then the spacing value should be already correct.</p>
<aside class="quote no-group" data-username="ravi_nataraj" data-post="1" data-topic="10368">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ravi_nataraj/48/5748_2.png" class="avatar"> ravi_nataraj:</div>
<blockquote>
<p>Also, when I try to volume render, I have to select scalar volume instead of multivolume when I load from the DICOM menu.</p>
</blockquote>
</aside>
<p>This is the expected behavior of MultiVolume module. You can check “Enable copying while sliding” in Multivolume explorer module to create a scalar volume of the currently selected time point.</p>
<p>You might find Sequences extension more intuitive to use. This extension adds more general 4D data support to Slicer, not just images, and has a few convenience features, such as a sequence browser toolbar.  To try it, install Sequences extension and in menu: Edit / Application settings / DICOM, set Preferred multi-volume import format → volume sequence.</p>

---

## Post #3 by @Chris_Rorden (2020-02-20 21:54 UTC)

<p>To provide insight into your problem, I would try converting your image to NIfTI with dcm2niix.</p>
<ol>
<li>Install <a href="https://github.com/rordenlab/dcm2niix/releases" rel="nofollow noopener">dcm2niix</a>.</li>
<li>Try converting your files without merging: <code>dcm2niix -m n c:\myDICOMs</code>
</li>
<li>Try converting your files with merging: <code>dcm2niix -m y c:\myDICOMs</code><br>
These should generate NifTI files (they end with the .nii extension) you can view with Slicer. It may also show that your slices were acquired with a gantry tilt or as separate packets. The command line output might also reveal other details that help troubleshoot your issue.</li>
</ol>

---

## Post #4 by @ravi_nataraj (2020-02-25 03:12 UTC)

<p>Sorry for the late reply.</p>
<p>I’ve rotated the slice view to the volume plane and it worked. The slices I have are indeed oblique like you said.</p>
<p>Also, I realized that all 3 views are the same oblique plane (they are parallel). The heart slices seem to change with time. Is there a way I can I reflect that in 3D slicer? When I move through iterations, it changes with units of mm. Can it be changed units of time such as seconds?</p>
<p>Additionally, my main goal is to take measurements of the heart. Specifically, I’m trying to find how the length of certain structures (ex. left ventricle, certain valves) expand and contract over the length of one cardiac cycle. Is there a way I track changing lengths of structures as a function of time? Can this be exported as a CSV file?</p>
<p>Again, thank you so much!</p>

---

## Post #5 by @lassoan (2020-02-25 04:40 UTC)

<aside class="quote no-group" data-username="ravi_nataraj" data-post="4" data-topic="10368">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ravi_nataraj/48/5748_2.png" class="avatar"> ravi_nataraj:</div>
<blockquote>
<p>The heart slices seem to change with time. Is there a way I can I reflect that in 3D slicer? When I move through iterations, it changes with units of mm. Can it be changed units of time such as seconds?</p>
</blockquote>
</aside>
<p>If you have a 2D+t image acquisition then Slicer should be able to recognize it as such and replay it using MultiVolumeExplorer or Sequence Browser module. Try to use latest Slicer Preview Release. If the data set is still loaded as a 3D volume then it would be great if you could share an anonymized version so that we can investigate.</p>
<aside class="quote no-group" data-username="ravi_nataraj" data-post="4" data-topic="10368">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ravi_nataraj/48/5748_2.png" class="avatar"> ravi_nataraj:</div>
<blockquote>
<p>Additionally, my main goal is to take measurements of the heart. Specifically, I’m trying to find how the length of certain structures (ex. left ventricle, certain valves) expand and contract over the length of one cardiac cycle. Is there a way I track changing lengths of structures as a function of time? Can this be exported as a CSV file?</p>
</blockquote>
</aside>
<p>If you install Sequences extension and load the data set as a “Volume Sequence” (by setting in menu: Edit / Application settings / DICOM / Preferred multi-volume format → volume sequence) then you can time-varying measurements (by adding a measurement at a single time point, then in Sequence Browser module adding a new sequence and setting the measurement as “proxy node”).  You can create a few-line python script to save the measurement results into a .csv file.</p>

---
