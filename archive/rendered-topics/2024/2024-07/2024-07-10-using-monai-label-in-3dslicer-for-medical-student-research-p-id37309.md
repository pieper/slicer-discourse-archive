---
topic_id: 37309
title: "Using Monai Label In 3Dslicer For Medical Student Research P"
date: 2024-07-10
url: https://discourse.slicer.org/t/37309
---

# Using Monai Label in 3DSlicer for Medical Student Research Project

**Topic ID**: 37309
**Date**: 2024-07-10
**URL**: https://discourse.slicer.org/t/using-monai-label-in-3dslicer-for-medical-student-research-project/37309

---

## Post #1 by @Saim_ali (2024-07-10 15:05 UTC)

<p>Hello,</p>
<p>I am a medical student with no computer science background looking for some help with using Monai Label with 3D slicer. My main issue is with connecting to the Monai Server.</p>
<p>I was able to follow a tutorial online and use anaconda terminal to download the monai pip package, connect to the server and then was able to run the model on the test data and segment out the spleen CT. But was wondering if there is a more permanent way to download Monai Label Radiology instead of having to do it every time from the terminal. I am a bit confused in the workflow to generate labeled scans without having to go through the download process and server activation every time. Any insight would be very helpful, I have gotten confused trying to understand the technical aspects of this program.</p>
<p>For background, I am a medical student working on a research project to calculate surface areas of organs from CT scans, this would ideally be automated by a model such as Monai Label Radiology. Thank you in advance.</p>

---

## Post #2 by @pieper (2024-07-10 18:19 UTC)

<p>MONAI Label is a very powerful environment but may not be strictly needed for your project, or at least not be the ideal place to start.  DId you look at TotalSegmentator and Auto3DSeg?  I believe they will give you spleen segmentations pretty easily and you could focus on calculating surface areas (which might also be mostly automatic, but you may need to review/fix the results to match your protocols).</p>

---

## Post #3 by @Saim_ali (2024-07-10 18:37 UTC)

<p>Hi Steve, Thank you for your quick response. I had not look at either but just downloaded the Auto3DSeg module to try it out and yes it is much easier to use and seems like it will work for my purposes. Thank you! I went into a hole on MonaiLabel and it seems to be out of my technical ability range.</p>
<p>Another question for you if you have the time… My project would require surface area of the Liver + spleen which seems doable with the preset models. However I am also looking for the surface area of the abdominal cavity, not an organ that would be pretrained with the models in Auto3Dseg. How feasible would it be for me to feed contoured images into the model to give an output of the abdominal cavity?</p>

---

## Post #4 by @pieper (2024-07-10 18:48 UTC)

<p>It’s great that you can leverage these tools for your research - be sure to let us know how it goes.</p>
<p>Regarding liver/spleen surface areas, you should be able to get that from SegmentStatistics.  You’ll want to look at each scan to confirm the organ isn’t clipped by the scan field of view or not otherwise poorly segmented (these models aren’t so robust for people with big pathologies or post-op conditions).  Then maybe you just merge all the organs in the abdominal cavity into one segment and get the area or volume of that.  While you could retrain a model it’s probably better to see if you can meet your research goals using existing models.</p>

---

## Post #5 by @Saim_ali (2024-07-12 18:38 UTC)

<p>Hi Steve,</p>
<p>Thank you for all of your help, I will be sure to keep you posted on my research. I was able to use SegmentStatistics and it is very helpful to my goal.</p>
<p>Regarding abdominal cavity, the surface area that I am looking for on top of the organ surface area is the parietal peritoneum. Which is different than the addition of all abdominal organ surface areas. It is the outside border of the abdomen. A way that we could estimate this would be to just outline the 3D model of the abdominal organs and see what that surface area is. I am not sure if this is possible, but will look around the program. Please let me know if you have any ideas or contacts I could reach out to! And thanks for keeping everything open-source, this has been a great tool and learning experience.</p>

---

## Post #6 by @lassoan (2024-07-12 19:13 UTC)

<p>You can get a “bag” (convex or concave hull, like a “shrinkwrap”) around all your segmented abdominal organ segments by using <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">SurfaceWrapSolidify extension</a>. Since the shape is quite simple, you may also be able to very quickly segment the peritoneum by painting it on 5-10 slices and use <code>Fill between slices</code> effect.</p>
<p>This is probably not a very hard segmentation task, so if you create a few dozen segmentations with manual/semiautomatic tools then there is a chance that you can train a segmentation network (MONAI Auto3DSeg or nn-UNet) with them. If it does not work with a few dozen training images then it will work if you provide a few hundred.</p>

---

## Post #7 by @Saim_ali (2024-07-12 20:39 UTC)

<p>Hi Andras,</p>
<p>Thanks for replying, I have been learning a lot from your previous threads so it is nice to hear from you.</p>
<p>I have used SurfaceWrapSolidify and it does a pretty good job, I am attaching the results. The front edge of the abdominal wall is very well estimated, the back less so, not as many inclusion points in the back so I am going to workshop that to be more accurate. I am trying to stay away from training my own segmentation network because I am not great with the coding aspect. But any guidance on that end would be great. Also any tips on getting a more accurate wrap would be great too. Once again, thanks a lot. This is a great tool.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b2e280681a6636d511a4dfa7274467273c1b8a1.jpeg" data-download-href="/uploads/short-url/hzHCl53nxCpjXqVTmHjT5QI7whX.jpeg?dl=1" title="AbdominalSATest" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b2e280681a6636d511a4dfa7274467273c1b8a1_2_690x435.jpeg" alt="AbdominalSATest" data-base62-sha1="hzHCl53nxCpjXqVTmHjT5QI7whX" width="690" height="435" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b2e280681a6636d511a4dfa7274467273c1b8a1_2_690x435.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b2e280681a6636d511a4dfa7274467273c1b8a1_2_1035x652.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b2e280681a6636d511a4dfa7274467273c1b8a1_2_1380x870.jpeg 2x" data-dominant-color="C3C1BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">AbdominalSATest</span><span class="informations">1920×1211 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @Saim_ali (2024-07-15 16:49 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> I know I’ve taken up some of your time, just bumping this in case you have any ideas.</p>

---

## Post #9 by @Saim_ali (2024-07-16 16:30 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> is there a way to set exclusion criteria to wrap solidify? I.e. remove structures from the created wrap such as pancreas, kidney, vertebrae?</p>

---

## Post #10 by @lassoan (2024-07-16 16:58 UTC)

<p>I’m not sure what improvements are you looking for. If you want to allow some concavities (follow the shape of the segment more closely) then you can enable <code>Carve holes</code> and adjust the slider next to it.</p>

---

## Post #11 by @liam26 (2026-01-16 03:28 UTC)

<p>Can you walk me through your process for this? Thanks!</p>

---
