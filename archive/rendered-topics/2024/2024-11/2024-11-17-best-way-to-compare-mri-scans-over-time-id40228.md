---
topic_id: 40228
title: "Best Way To Compare Mri Scans Over Time"
date: 2024-11-17
url: https://discourse.slicer.org/t/40228
---

# Best Way to Compare MRI Scans Over Time?

**Topic ID**: 40228
**Date**: 2024-11-17
**URL**: https://discourse.slicer.org/t/best-way-to-compare-mri-scans-over-time/40228

---

## Post #1 by @noobslicer (2024-11-17 02:10 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 5.6.2</p>
<p>Hi everyone,</p>
<p>I have about 10 MRI scans of a family member, taken from the early 2000s to now, covering the brain and the spine. I want to compare these scans over the years, ideally by creating a video or GIF that fades between similar images or viewing them side by side, but I’m not sure how to start.</p>
<p>The reports include phrases like:</p>
<ul>
<li>Multiplanar MR images of the brain before and after injecting gadolinium.</li>
<li>Axial and sagittal MR images of the spine, with contrast, in T1/T2-weighted sequences.</li>
<li>FLAIR images and gradient echo techniques for certain views.</li>
</ul>
<p>Someone told me that unless these scans use 3D sequences (which I don’t think they do), it’s hard to compare because the slices aren’t in the exact same planes. Still, I want to try since doctors here don’t spend much time reviewing older scans, and a proper comparison could really help.</p>
<p>ChatGPT mentioned ANTs, but it seems more complicated than Slicer. Do you know of any software, tools, or AI that could align and compare these images easily or even create the kind of video I’m hoping for? Or could you please guide me on how to achieve this using Slicer?</p>
<p>Thanks in advance for any help!</p>

---

## Post #2 by @pieper (2024-11-17 18:44 UTC)

<p>What you describe should be possible.  Of course the scans may look very different from study to study so you may not be able to see the same structures in the same way at each time point.</p>
<p>You could start with this information: <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html" class="inline-onebox">Registration — 3D Slicer documentation</a></p>
<p>Basically you load each study and then register point to point to put all the scans in the same space.</p>
<p>From there you can make a sequence (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/sequences.html" class="inline-onebox">Sequences — 3D Slicer documentation</a>) for all the time points and to make an animation you can use the ScreenCapture module (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/screencapture.html" class="inline-onebox">Screen Capture — 3D Slicer documentation</a>).</p>

---

## Post #3 by @noobslicer (2024-11-17 19:13 UTC)

<p>Thank you. I’ve opened two studies to experiment, but it looks like I’ll need to go through a lot of documentation and maybe some YouTube videos, as there are just so many options, buttons, views, and menus to figure out!</p>
<p>Does Slicer automatically find images with the same MR setting and view to compare them?</p>

---

## Post #4 by @pieper (2024-11-17 19:30 UTC)

<aside class="quote no-group" data-username="noobslicer" data-post="3" data-topic="40228">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/ea5d25/48.png" class="avatar"> noobslicer:</div>
<blockquote>
<p>there are just so many options, buttons, views, and menus to figure out!</p>
</blockquote>
</aside>
<p>True, it’s complicated, in part because there are many kinds of imaging and many different things people might want to do.  Hopefully you can find your way through it.  If you run into specific issues be sure to post, ideally with screenshots so we can give you specific suggestions.</p>
<aside class="quote no-group" data-username="noobslicer" data-post="3" data-topic="40228">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/ea5d25/48.png" class="avatar"> noobslicer:</div>
<blockquote>
<p>Does Slicer automatically find images with the same MR setting and view to compare them?</p>
</blockquote>
</aside>
<p>No, that’s something you need to do manually.  MR scans are not uniform, so there may not even be the same scan types from study to study, or they may have different names (series descriptions) for the same type of scan depending on how they were acquired.</p>

---

## Post #5 by @noobslicer (2024-11-19 21:49 UTC)

<p>I watched the first three YouTube tutorials by Jan Witowski, and while they are the best I found, I didn’t continue because they seem to focus on segmentation, which might not be relevant to this project if I’m correct.</p>
<p>Instead, since I only have one week to create the comparison, I opened all 10 MRI scans in Weasis, exported them as PNG files, and organized them into folders. I further categorized the folders based on the scanned regions, such as Brain, TSp, LSp, etc., to make things less confusing. It would have been great if 3D Slicer had some sort of AI or similarity check to assist with this part.</p>
<p>I noticed that Weasis provides two parameters for each slice: Thickness and Location. How accurate are these values? Could 3D Slicer use them to generate a 3D model of the body from all 10 scans and align slices from different scans to this model for comparing slices that are close to one another?</p>
<p>If that’s not feasible, what approach would you recommend for visually comparing the brain and spine across these 10 MRI scans spanning several years? There are over 2,300 slices/images in total. From what I understand about 3D Slicer so far, it doesn’t seem to simplify this specific application I’m trying to achieve, meaning I’d have to handle all the tedious work manually. Am I correct?</p>

---

## Post #6 by @pieper (2024-11-19 22:16 UTC)

<p>Based on what you have described I would suggest the following:</p>
<ul>
<li>drag and drop the folders containing the dicom files for each of the 10 scans (called Studies) so that they are indexed in Slicer’s <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html">dicom database</a></li>
<li>this will sort the files by date and collect related images into what are called “series” which typically correspond to what loads in Slicer as a Volume (taking into account the image geometry like spacing and slice location)</li>
<li>you can load whole studies or individual series to view.  If the particular MR series corresponds to a volume it will load as one.  If a series is not a volume it may be something else more complex and probably you want to ignore those.</li>
<li>In slicer’s <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/data.html">data module</a> the studies and series will be arranged in a hierarchy that you <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#selecting-displayed-data">can selectively view</a></li>
<li>You can use the Registration methods I linked to earlier to align the data to the same space.</li>
<li>You can compare any two time points by putting one in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">foreground and one in the background and adjusting the opacity</a></li>
<li>If you identify a sequence you want to view as a video, you can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/sequences.html#sequences">create a sequence</a> which you can record to a video with the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/screencapture.html#screen-capture">Screen Capture</a> module.</li>
</ul>

---

## Post #7 by @noobslicer (2024-11-22 15:46 UTC)

<p>Thank you.<br>
I’m not sure how one of these two slices could be registered to the other when they seem to be on slightly different planes. How can the registered image still be accurate?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd59b309345af63005381ccc804fcea8dd80be48.png" data-download-href="/uploads/short-url/tiC3O99WhqYVFW9pferetLUZm88.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd59b309345af63005381ccc804fcea8dd80be48_2_438x500.png" alt="1" data-base62-sha1="tiC3O99WhqYVFW9pferetLUZm88" width="438" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd59b309345af63005381ccc804fcea8dd80be48_2_438x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd59b309345af63005381ccc804fcea8dd80be48.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd59b309345af63005381ccc804fcea8dd80be48.png 2x" data-dominant-color="4A4A4A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">477×544 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78d6befbfa08e48edf50762f866a12e498647f84.png" data-download-href="/uploads/short-url/heZo2lgwNvMsh9bOeOi7nS7LJXe.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78d6befbfa08e48edf50762f866a12e498647f84_2_442x500.png" alt="2" data-base62-sha1="heZo2lgwNvMsh9bOeOi7nS7LJXe" width="442" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78d6befbfa08e48edf50762f866a12e498647f84_2_442x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78d6befbfa08e48edf50762f866a12e498647f84.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78d6befbfa08e48edf50762f866a12e498647f84.png 2x" data-dominant-color="343434"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">512×578 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Also, for spinal MR images, how is registration handled given the presence of surrounding structures like internal organs? Is there a method to focus solely on the spinal column for registration, ignoring the rest of the image?</p>

---

## Post #8 by @pieper (2024-11-22 16:08 UTC)

<p>The brain images should register well, as long as there is a full volume of data.  If they are thickly sliced, then seeing one scan rotated into the sampling grid of the other will probably be fuzzy, but at least the structures will line up.  You should go ahead and try. <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html" class="inline-onebox">Registration — 3D Slicer documentation</a></p>
<p>For your question about the spine, yes, you can provide a mask that indicates which part of the image should be registered.  Parts outside the mask will be ignored.</p>

---
