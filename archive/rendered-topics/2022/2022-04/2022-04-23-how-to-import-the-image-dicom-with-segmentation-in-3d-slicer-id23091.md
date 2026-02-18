# How to import the image dicom with segmentation in 3d slicer

**Topic ID**: 23091
**Date**: 2022-04-23
**URL**: https://discourse.slicer.org/t/how-to-import-the-image-dicom-with-segmentation-in-3d-slicer/23091

---

## Post #1 by @akmal871026 (2022-04-23 01:03 UTC)

<p>Dear Sir,</p>
<p>I have 100 slice image dicom. I did the lesion segmentation using MATLAB.</p>
<p>Then, how to import my images with my segmentation in 3D Slicer?</p>

---

## Post #2 by @lassoan (2022-04-23 05:39 UTC)

<p>I would recommend to save the segmentation from Matlab into a nrrd file. Use the <code>.seg.nrrd</code> file extension to get the file loaded as a segmentation by default. You can use <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m">nrrdwrite</a> to create a segmentation file from a Matlab array. Make sure to use the same image geometry (<code>ijkToLpsTransform</code>) as the input nrrd file that you segmented.</p>
<p>What was the reason for implementing your lesion segmentation method in Matlab? Python has very significant advantages, such as many more available packages, easier to distribute to end users (no licensing hassles), and being able to run your scripts directly in Slicer (no need to use <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge">Slicer MatlabBridge</a> or manually save+process+load data).</p>

---

## Post #3 by @akmal871026 (2022-04-23 06:19 UTC)

<p>I used the method gradient different weight.</p>
<p>There is no in 3D slicer.</p>

---

## Post #4 by @lassoan (2022-04-23 12:58 UTC)

<aside class="quote no-group" data-username="akmal871026" data-post="3" data-topic="23091">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akmal871026/48/11642_2.png" class="avatar"> akmal871026:</div>
<blockquote>
<p>gradient different weight</p>
</blockquote>
</aside>
<p>What is the exact name of the function that you used? Does it calculate the image gradient magnitude? That (and hundreds of similar functions) are available in VTK, ITK, scipy, and in many other pip-installable Python packages.</p>
<p>Are you using this example: <a href="https://www.mathworks.com/help/images/ref/gradientweight.html?msclkid=806a04f0c2cd11ec87b78491f191d2e3" class="inline-onebox">Calculate weights for image pixels based on image gradient - MATLAB gradientweight</a> ? Image segmentation using Fast marching is available in Slicer, for example in the <code>Fast marching</code> effect in Segment Editor (provided by <code>SegmentEditorExtraEffects</code> extension). You can use <code>Grow from seeds</code> effect for automatic segmentation, too (you generate scribbles based on a user click); or Local threshold effect (that uses <code>Grow from seeds</code> or <code>Watershed</code> or simple grayscale connectivity to segment an object by a single click).</p>

---

## Post #5 by @akmal871026 (2022-04-23 15:05 UTC)

<p>yup. I used the function graydiffweight <a href="https://www.mathworks.com/help/images/ref/graydiffweight.html" class="inline-onebox" rel="noopener nofollow ugc">Calculate weights for image pixels based on grayscale intensity difference - MATLAB graydiffweight</a>.</p>
<p>actually, I have modified this function to get one equation that is used in graydiffweight algorithm. Then, I will get the high accuracy volume segmentation for SPECT images.</p>
<p>I have tried to use many methods in 3D Slicer, but it’s not accurate to compare to what I was done.</p>
<p>Back to the issue is, when I have done segmentation SPECT images using Matlab, then I want to import to 3D Slicer to analyze the radiomics parameter using radiomics extension in 3D Slicer.</p>

---

## Post #6 by @lassoan (2022-04-23 15:53 UTC)

<p>It seems that <code>graydiffweight</code> can compute the difference of array values and a constant value. You can reproduce what the function does with 1-2 <code>numpy</code> function calls.</p>
<aside class="quote no-group" data-username="akmal871026" data-post="5" data-topic="23091">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akmal871026/48/11642_2.png" class="avatar"> akmal871026:</div>
<blockquote>
<p>I have tried to use many methods in 3D Slicer, but it’s not accurate to compare to what I was done.</p>
</blockquote>
</aside>
<p>Probably you have tried some high-level modules in Slicer, which expose some commonly needed features, but they may not be exactly what you need. You have access to all functions of all Python packages in Slicer, so if you need any custom computation then it should be about as easy to implement that as in Matlab.</p>
<p>The enormous advantage of Python is that if you implement something then you can make it easily available to all Python users (via PyPI) and to clinical users (for example, as a Slicer extension).</p>
<aside class="quote no-group" data-username="akmal871026" data-post="5" data-topic="23091">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/akmal871026/48/11642_2.png" class="avatar"> akmal871026:</div>
<blockquote>
<p>hen I have done segmentation SPECT images using Matlab, then I want to import to 3D Slicer to analyze the radiomics parameter using radiomics extension in 3D Slicer.</p>
</blockquote>
</aside>
<p>See my answer above - you can use <code>nrrdread.m</code> and <code>nrrdwrite.m</code> to read/write image data (SPECT image, segmentation, etc.) while preserving essential image metadata.</p>

---

## Post #7 by @akmal871026 (2022-04-23 16:20 UTC)

<p>Thank you sir. My problem solve.</p>
<p>But I still don’t know how to apply MatlabBridge ??</p>
<p>Can give me some video?</p>

---

## Post #8 by @lassoan (2022-04-24 04:22 UTC)

<p>Documentation and examples of the MatlabBridge are available here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge" class="inline-onebox">Documentation/Nightly/Extensions/MatlabBridge - Slicer Wiki</a> It should be sufficient for you to get started with it.</p>

---
