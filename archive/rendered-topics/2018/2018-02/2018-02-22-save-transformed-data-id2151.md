---
topic_id: 2151
title: "Save Transformed Data"
date: 2018-02-22
url: https://discourse.slicer.org/t/2151
---

# Save transformed data

**Topic ID**: 2151
**Date**: 2018-02-22
**URL**: https://discourse.slicer.org/t/save-transformed-data/2151

---

## Post #1 by @Nathan (2018-02-22 17:31 UTC)

<p>Operating system: windows<br>
Slicer version: 4.8.1</p>
<p>Hello,</p>
<p>I have ~50 sets of images that I have registered to a brain template. Would it be possible to save them after regridding to a common matrix? I would like to open the transformed images in Matlab.</p>
<p>-Nathan</p>

---

## Post #2 by @lassoan (2018-02-22 20:01 UTC)

<p>You should be able to do it with a short Python script: load data, <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python">run CLI modules</a> to register and resample, and <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_save_an_image.2Fvolume_using_python_.3F">save resampled images</a>.</p>

---

## Post #3 by @Nathan (2018-02-22 20:50 UTC)

<p>Is there no way to do it without jumping in and learning Python scripting?</p>
<p>It’s not something I have done before.</p>
<p>Seems like there should be a way to save reformatted data.</p>

---

## Post #4 by @lassoan (2018-02-22 21:23 UTC)

<p>You can of course save iamges using the GUI. However, if you do batch processing of 50 data sets then you can save time by writing a few lines of Python.</p>
<p>Learning Python scripting and libraries is well worth the effort anyway, as Python ecosystem nowadays provides everything as Matlab and much more, for free, without relying on any proprietary, closed-source components.</p>

---

## Post #5 by @Nathan (2018-02-22 22:25 UTC)

<p>I have tried “hardening” the transformation and saving it. The saved images are in their native coordinate spaces and orientations. Is there a way to save them all regridded to the same 3D matrix?</p>
<p>Sorry if this is an obvious question, but I can’t seem to find how to do this in the documentation.</p>
<p>The data is all registered and ready to go.</p>
<p>I have been meaning to learn Python, but don’t have time today to jump in.</p>
<p>Thanks,<br>
Nathan</p>

---

## Post #6 by @fedorov (2018-02-24 02:48 UTC)

<p><a class="mention" href="/u/nathan">@Nathan</a> sorry for the confusion. “Hardening” does not reformat the images, it only modifies the direction cosines matrix in the output. You should instead use Resample image module, setting your atlas image as reference, and the transformation nodes as “Transform files”.</p>
<p>You can also write a bash script to do this operation, since the resample module is a command-line tool. On mac it is in <code>/Applications/Slicer.app/Contents/lib/Slicer-4.9/cli-modules/ResampleScalarVolume</code>, if you run it with <code>--help</code> it will print all flags.</p>
<p>Let us know if this does not answer your question!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e4ac7472b439c255db51989b3578e2073f976f2.jpeg" data-download-href="/uploads/short-url/kiM0NoDvsGktLXNsS9sEDpp2Bdo.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e4ac7472b439c255db51989b3578e2073f976f2_2_508x500.jpg" alt="image" data-base62-sha1="kiM0NoDvsGktLXNsS9sEDpp2Bdo" width="508" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e4ac7472b439c255db51989b3578e2073f976f2_2_508x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e4ac7472b439c255db51989b3578e2073f976f2.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e4ac7472b439c255db51989b3578e2073f976f2.jpeg 2x" data-dominant-color="F1F1F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">577×567 92.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @Nathan (2018-02-26 13:54 UTC)

<p>Awesome - thank you. I don’t know how I missed that module.</p>
<p>The images have multiple transformations applied to them (rigid registrations from time2 to time1 and from time1 to time0, and then affine + nonrigid registration between time0 and brain template via ANTS). Is there a way to deal with that, or should I harden the transformations before resampling? It seems that hardening sometimes results in cropping of the data.</p>
<p>-Nathan</p>

---

## Post #8 by @lassoan (2018-02-26 14:36 UTC)

<p>To have optimal image quality, harden all the transforms in one step. If you have non-linear transforms among the transforms then resampling will be performed automatically, but the extent of the hardened volume will be the same as the original volume, so any parts outside the original extent will be cropped. For most resample modules you can specify an output geometry (by selecting a reference volume), you just have to set that output geometry to avoid any undesired cropping.</p>

---

## Post #9 by @Nathan (2018-02-26 15:48 UTC)

<p>Thanks again for the help.</p>
<p>I am getting substantial cropping when I harden the transformations. Is there a way around this?</p>
<p>Not sure if it matters, but I am hardening the transformation in the “Data” module.</p>
<p>Affine Transformation<br>
+Nonrigid Transformation<br>
++Transformation (time1 to time0)<br>
+++Transformation (time2 to time1)<br>
++++Image data</p>
<p>One or more of the transformations moves the data outside its original coordinate space.</p>

---

## Post #10 by @lassoan (2018-02-26 17:01 UTC)

<p>As I wrote before, if you harden in Data module, then the original volume’s geometry is used as output geometry. If the volume has moved, you can either use Crop volume module to define a region of interest where you want your volume to be cropped&amp;resampled into, or use one of the resampling modules that accept a reference volume (and create a reference volume that is large enough and positioned so that no undesired cropping occurs).</p>

---

## Post #11 by @Nathan (2018-02-26 20:40 UTC)

<p>When I “crop” the data to a bigger ROI, the registration/transformation is no longer valid.</p>
<p>It’s frustrating…I am looking at the data on my screen all nicely lined up and interpolated in Slicer. I just want to export it. I guess you can’t always get what you want.</p>
<p>Guess I will figure out how to regrid nonrigid registrations in Matlab.</p>

---

## Post #12 by @fedorov (2018-02-26 20:40 UTC)

<p>You could also try hardening the transforms (harden at one level above the volume), and then use the resulting single transform as input to the resample module. Have you tried that?</p>

---

## Post #13 by @Nathan (2018-02-26 21:47 UTC)

<p>I think I’ll run into the same problem since the data I am interested in examining was acquired in a limited volume:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e90585c265a642eeedcce6d6d4b5f42e5d69930a.jpeg" data-download-href="/uploads/short-url/xfp57aG21DzAaNriiM6f61uB0uK.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e90585c265a642eeedcce6d6d4b5f42e5d69930a_2_690x288.jpg" alt="image" data-base62-sha1="xfp57aG21DzAaNriiM6f61uB0uK" width="690" height="288" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e90585c265a642eeedcce6d6d4b5f42e5d69930a_2_690x288.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e90585c265a642eeedcce6d6d4b5f42e5d69930a_2_1035x432.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e90585c265a642eeedcce6d6d4b5f42e5d69930a_2_1380x576.jpg 2x" data-dominant-color="737372"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3440×1440 1.12 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I think it will always be cropped.</p>
<p>If you’re curious, we created a lesion in the thalamus in each patient as a treatment for tremor. You cannot see the thalamic nuclei in the MRI, so I did nonrigid registration to an atlas that has the nuclei segmented.</p>
<p>I was curious to visualize all the lesions superimposed on the atlas, and to calculate the probability for a lesion on the atlas for all patients. This would be trivial in Matlab if I could export the data on the same grid.</p>

---

## Post #14 by @lassoan (2018-02-26 22:47 UTC)

<aside class="quote no-group" data-username="Nathan" data-post="11" data-topic="2151">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/c5a1d2/48.png" class="avatar"> Nathan:</div>
<blockquote>
<p>I am looking at the data on my screen all nicely lined up and interpolated in Slicer. I just want to export it.</p>
</blockquote>
</aside>
<p>Have you considered do the processing in Python, using numpy, VTK, ITK, etc?</p>
<p>By the way, resampling volumes at an arbitrary ROI is very, very easy:</p>
<ul>
<li>if you have a reference volume that defines the geometry, then specify that in a resample module</li>
<li>if you don’t have a preferred reference volume then use Crop volume module (then you define geometry using a freehand editable region of interest widget).</li>
</ul>

---

## Post #15 by @Nathan (2018-02-26 23:11 UTC)

<p>The problem is that there are four transformations of the data (2 rigid, nonrigid, than another rigid) before I get to the reference volume that I want to resample to. When I harden the transformation before resampling, the data is cropped.</p>
<p>If I crop the data to a larger ROI before hardening it, the transformations are no longer correct because that procedure puts the data into a new coordinate space.</p>
<p>Does that make sense?</p>

---

## Post #16 by @fedorov (2018-02-26 23:15 UTC)

<aside class="quote no-group" data-username="Nathan" data-post="15" data-topic="2151">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/c5a1d2/48.png" class="avatar"> Nathan:</div>
<blockquote>
<p>When I harden the transformation before resampling, the data is cropped.</p>
</blockquote>
</aside>
<p>It is not clear to me why that would be. If you register your data to the atlas, and you see the transformed data lining up with the atlas image before resampling, it should show the same way after you harden the transforms and apply the Resample volume module. It is either a bug, or there is some mis-communication.</p>
<p>Since I know you are local to BWH, I can meet with you in person tomorrow to troubleshoot this, if you like. I was hoping we could figure this out in the forum, just to see if we could help you as we would any other Slicer user, but it is probably more expedient to just meet and investigate this on the spot.</p>

---

## Post #17 by @Nathan (2018-02-26 23:22 UTC)

<p>That would be great and will probably save us both a lot of time. My schedule is open tomorrow.</p>

---

## Post #18 by @Nathan (2018-02-27 12:22 UTC)

<p>Andras,</p>
<p>Thank you for your help on this. I am sure that I am missing something obvious.</p>
<p>Andrey is going to come to my office today. Hopefully we’ll figure it out.</p>
<p>-Nathan</p>

---

## Post #19 by @fedorov (2018-02-27 23:22 UTC)

<p>To follow up on this issue, I met with Nathan today, and the suggestion I made earlier was easy to implement and it worked.</p>
<p>We hardened the transform hierarchy at the level immediately above the volume node, and then used Resample Volume module to apply the resulting hardened transform to the moving volume, while specifying the atlas as reference.</p>

---

## Post #20 by @lassoan (2018-03-05 15:07 UTC)

<p>FYI, I’ve <a href="https://issues.slicer.org/view.php?id=4433">implemented automatic update of image extent</a> when non-linear transform is hardened on a volume, so clipping will no more occur.</p>
<p>Resampling with a reference volume is still be needed when the goal is to have various volumes with the same geometry. To achieve this, one volume can be transformed using hardening the transform; then this volume can be used as reference volume for resampling all the other volumes.</p>

---

## Post #21 by @fedorov (2018-03-05 15:22 UTC)

<p>Andras, thank you!</p>
<aside class="quote no-group" data-username="lassoan" data-post="20" data-topic="2151">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Resampling with a reference volume is still be needed when the goal is to have various volumes with the same geometry. To achieve this, one volume can be transformed using hardening the transform; then this volume can be used as reference volume for resampling all the other volumes.</p>
</blockquote>
</aside>
<p>I don’t understand what you meant above. What are the steps to resample a give volume into a specific geometry using the “harden transform” feature?</p>

---

## Post #22 by @lassoan (2018-03-05 15:38 UTC)

<blockquote>
<p>What are the steps to resample a give volume into a specific geometry using the “harden transform” feature?</p>
</blockquote>
<p>This is not done by “harden transform” but you can use one of the resampling modules for this. The same way as before.</p>
<p>The new feature is that if you don’t have a reference volume, then you can create it by simply hardening the transform on a volume. Before this feature was available, you had to use Crop volume module to create a reference volume (or harden large translation/rotation components of the transform and use the resulting volume as reference volume).</p>

---

## Post #23 by @fedorov (2018-03-05 15:50 UTC)

<p>This makes sense now, thank you for the clarification Andras!</p>

---

## Post #24 by @Noemi_Garau (2022-07-06 21:42 UTC)

<p>Is there a similar approach to save the transformation file (.tfm)?</p>

---

## Post #25 by @lassoan (2022-07-07 00:41 UTC)

<p>Yes, sure you can harden a transform on another transform. While multiple linear transforms are collapsed into one linear transform; if you harden non-linear transforms then you’ll have composite transforms that are all listed in the transform file.</p>
<p>If you want then you can get a single combined displacement field of all the transforms as a grid transform. For this, there is no need to harden the transform but simply use Transforms module’s Convert section. You can convert the grid transform to a bspline transform using ScatteredTransform extension for a more efficient representation (10-100x smaller file size, with some potential loss of minor details for highly irregular displacement fields).</p>

---
