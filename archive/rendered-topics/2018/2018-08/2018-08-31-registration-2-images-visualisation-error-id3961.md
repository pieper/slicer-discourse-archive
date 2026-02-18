# Registration 2 images visualisation error?

**Topic ID**: 3961
**Date**: 2018-08-31
**URL**: https://discourse.slicer.org/t/registration-2-images-visualisation-error/3961

---

## Post #1 by @Laura (2018-08-31 18:33 UTC)

<p>Good evening,</p>
<p>On the Elastix General Registration Module (on MacOS), I am doing a generic rigid preset.<br>
However, when I superimpose the 2 images (the one “fixed” and the one “resampled, after the registration”, I have this result visually :<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5dadf573cfb4bbf162a8bc75884a5c7e1b89ea5.png" alt="11" data-base62-sha1="z4VUyKVFwzRd1c3ip1KvwyDuVsV" width="274" height="260"></p>
<p>Can you tell me why have I this visualisation ?<br>
Is it wrong or right ?<br>
I have checked on Data module and these two images have the same dimensions and spacing.</p>
<p>Maybe do I have to find a way to do a ICP registration instead ?<br>
I don’t know what to do…</p>
<p>Thanks a lot in advance<br>
Have a good weekend<br>
Laura</p>

---

## Post #2 by @lassoan (2018-08-31 18:44 UTC)

<p>Fixed image should be aligned well with the computed output image, so the result that you show does not look right.</p>
<p>Do you try to register 2D (single-slice 3D) images?<br>
Are they binary (black-and-white only) images?</p>

---

## Post #3 by @Laura (2018-08-31 18:48 UTC)

<p>The images (fixed and moving) are both nifti files that I have saved before after doing segmentations so they are in 3D. Do you think that this is the problem ?<br>
The moving one is binary and the fixed one has been created from volume clip with model so I don’t really know if it is binary volume…how can I check that ?</p>

---

## Post #4 by @lassoan (2018-08-31 18:55 UTC)

<p>These are binary volumes. Intensity-based registration methods cannot be effectively applied to binary images.</p>
<p>One option is to apply distance transform to them and then use intensity-based registration. This approach is implemented in Segment Registration extension. I would recommend to import your images into segmentation node (convert to labelmap node in Volumes module, if you forgot to click “labelmap” option when loaded the binary volumes) and use Segment Registration module to register them.</p>

---

## Post #5 by @Laura (2018-08-31 19:13 UTC)

<p>I am so sorry but I think that I have misunderstood something…</p>
<p>I have done this :</p>
<ul>
<li>
<p>Load file1(fixed) and file2 (moving)</p>
</li>
<li>
<p>On Volumes, create label map of these 2 files</p>
</li>
<li>
<p>on Segment registration,<br>
Fixed image = file1<br>
Moving image = file2<br>
Perform registration</p>
</li>
<li>
<p>Then, I have a new file called “file1_Resampled_1x1x1mm”</p>
</li>
<li>
<p>On General Registration Elastix,<br>
fixed volume = file1_Resampled_1x1x1mm<br>
moving volume = file2<br>
Preset = generic rigid<br>
Output volume : Create new volume<br>
Apply</p>
</li>
<li>
<p>The result of the superimpose is :<br>
Foreground = new volume created<br>
Background = file1_Resampled_1x1x1mm<br>
Result =<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/61c6e6b3c7945dc6f75634f9ea3aae62b3a677f0.png" alt="22" data-base62-sha1="dWYsqgY82FavGWGjeRBxCCn86mk" width="278" height="269"></p>
</li>
</ul>
<p>I can’t understand…<br>
Thanks a lot for your help !<br>
Laura</p>

---

## Post #6 by @cpinter (2018-08-31 19:34 UTC)

<p>In Segment Registration you cannot select labelmaps as inputs, only segmentations, and you’re not mentioning that you imported file1 and 2 to segmentation nodes. Are you sure you’re using the module called “Segment Registration”?</p>

---

## Post #7 by @Laura (2018-08-31 19:41 UTC)

<p>OH ! I have forgotten to convert label map to segment nodes !!!</p>

---

## Post #8 by @Laura (2018-08-31 20:02 UTC)

<p>Unfortunately…<br>
I am so sorry but I think that I have again misunderstood something…</p>
<p>I have done this :</p>
<ul>
<li>
<p>Load file1(fixed) and file2 (moving)</p>
</li>
<li>
<p>On Volumes, create label map of these 2 files (file1_label and file2_label)</p>
</li>
<li>
<p>on Segmentations :<br>
Segmentation : segmentation<br>
Export label map : file1_label<br>
Segmentation : segmentation_1<br>
Export label map : file2_label</p>
</li>
<li>
<p>on Segment registration,<br>
Fixed image = file1<br>
Fixed segmentation = segmentation<br>
Fixed segment : file1_label</p>
</li>
</ul>
<p>Moving image = file2<br>
Moving segmentation = segmentation_1<br>
Moving segment : file2_label<br>
Perform registration</p>
<ul>
<li>
<p>Then, I have a new file called “file2 cropped”</p>
</li>
<li>
<p>On General Registration Elastix,<br>
fixed volume = file1<br>
moving volume = file2 cropped<br>
Preset = generic rigid<br>
Output volume : Create new volume<br>
Apply</p>
</li>
<li>
<p>The result of the superimpose is :<br>
Foreground = new volume created<br>
Background = file1<br>
Result = <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75c5c0546999885b7af1103ea8ff4ad7d5ce8e5f.png" alt="03" data-base62-sha1="gNRxJZCdU2QpNxnSfQGE2w6Nb3x" width="221" height="257"></p>
</li>
</ul>
<p>I can’t understand…<br>
Thanks a lot for your help !<br>
Laura</p>

---

## Post #9 by @cpinter (2018-08-31 20:17 UTC)

<p>What is the “On General Registration Elastix” part? If you use Segment Registration then what it does is registration.</p>
<p>Are there any errors after the Segment Registration step in the log? See About / Report an error</p>

---

## Post #10 by @Laura (2018-08-31 20:20 UTC)

<p>Oh so I don’t need to go on Elastix general registration !!!<br>
Just stop after my “file2 cropped” and superimpose this one with my file1 !!!<br>
So many thanks ! and so sorry for not having understood before !!!</p>

---
