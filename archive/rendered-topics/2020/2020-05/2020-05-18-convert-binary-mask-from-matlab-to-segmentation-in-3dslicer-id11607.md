# Convert binary mask from MATLAB to segmentation in 3DSlicer

**Topic ID**: 11607
**Date**: 2020-05-18
**URL**: https://discourse.slicer.org/t/convert-binary-mask-from-matlab-to-segmentation-in-3dslicer/11607

---

## Post #1 by @go-lauren (2020-05-18 21:54 UTC)

<p>I have created binary masks for hrd/img scans in MATLAB, but I want to export them as segmentations in 3DSlicer.</p>
<p>I have tried saving the masks as a .nii file and adding data as labelmap, but nothing shows up.</p>

---

## Post #2 by @muratmaga (2020-05-18 23:23 UTC)

<p>Are you sure you successfuly export the masks from Matlab? Did you try to open them with some other software (ITK-SNap, fiji)?</p>
<p>Looking at the error log (Ctrl+0) will probably while loading has failed.</p>

---

## Post #3 by @go-lauren (2020-05-19 00:08 UTC)

<p>So I can load them as a volume (not labelmaps) into slicer and they will appear, but I want it to be a segmentation for the mri image.</p>
<p>It successfully loads as far as I know, but nothing appears. Currently, if I try importing as a segmentation, nothing shows up.</p>

---

## Post #4 by @lassoan (2020-05-19 03:53 UTC)

<p>You can directly load nrrd and nifti files as segmentations in recent Slicer Preview Releases. In the “Add data” dialog choose “Segmentation” as description.</p>
<p>In older Slicer versions, you had to do this in two steps: load volume as labelmap volumes, then convert to segmentation (by right-clicking on it in Data module).</p>

---

## Post #5 by @go-lauren (2020-05-20 18:23 UTC)

<p>I don’t really see Segmentation as an option in the Add data dialogue. I’m using 3D Slicer 4.10.2</p>

---

## Post #6 by @lassoan (2020-05-20 18:36 UTC)

<p>As I wrote above, you need to use a recent Slicer Preview Release.</p>

---

## Post #7 by @go-lauren (2020-05-20 22:06 UTC)

<p>So actually I think the problem was that the scale of the binary mask and the scale of the image doesn’t match, but I’m not sure why because I just made sure they correspond pixel to pixel.</p>

---

## Post #8 by @lassoan (2020-05-20 22:55 UTC)

<p>Is the origin, spacing, and axis directions are the same in the image and labelmap? Nifti header is not human-readable (it is one of the issues with this format), but you can use for example <a href="https://dartbrains.org/features/notebooks/3_Introduction_to_NeuroimagingData_in_Python.html">nibabel</a> to display file header content so that you can inspect it. If you don’t work with brain images then the best is to use a generic file format, such as nrrd (you can find nrrdread.m and nrrdwrite.m Matlab functions for reading/writing nrrd files <a href="https://github.com/PerkLab/SlicerMatlabBridge/tree/master/MatlabCommander/commandserver">here</a>) .</p>

---

## Post #9 by @go-lauren (2020-05-20 23:09 UTC)

<p>I’m not sure what those would be, because I simply loaded the hdr/img into MATLAB and then created a binary mask based on every slice of the 3 dim. image it produced. Is there a way to convert hdr/img to nrrd?</p>

---

## Post #10 by @muratmaga (2020-05-20 23:29 UTC)

<p>Are you trying to load both the binary mask you created and the original volume into the Slicer? If so, you can try to copy and paste the image spacing from the original AnalyzeImage volume to your binary mask using the <code>Volumes</code>. It would help if you can provide screenshots.</p>
<p>Otherwise all we can say something seems to be lost along your matlab conversion.</p>

---

## Post #11 by @lassoan (2020-05-21 00:05 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="10" data-topic="11607">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Otherwise all we can say something seems to be lost along your matlab conversion.</p>
</blockquote>
</aside>
<p>I agree that this is the most likely the root cause of the issue.</p>
<p><a class="mention" href="/u/go-lauren">@go-lauren</a>: When the image is read into Matlab, you need to store the image origin, position, and axis directions, too. It may be stored as a single 4x4 matrix or a 3x3 matrix and a vector (and in nift it might be also stored as a quaternion and a vector). When you write the processed image to file, you need to save this information to the image file. You can find how it is done for nrrd in usage examples in nrrdread.m and nrrdwrite.m.</p>

---

## Post #12 by @go-lauren (2020-05-21 01:07 UTC)

<p>Yes, pasting the spacing worked! What can I do to make sure that the mask and the image have the same spacing?</p>

---

## Post #13 by @go-lauren (2020-05-21 01:19 UTC)

<p>Never mind, I got it!! Thank you so much!</p>

---
