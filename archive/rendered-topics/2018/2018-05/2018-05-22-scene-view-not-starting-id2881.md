---
topic_id: 2881
title: "Scene View Not Starting"
date: 2018-05-22
url: https://discourse.slicer.org/t/2881
---

# Scene view not starting

**Topic ID**: 2881
**Date**: 2018-05-22
**URL**: https://discourse.slicer.org/t/scene-view-not-starting/2881

---

## Post #1 by @HLee (2018-05-22 15:52 UTC)

<p>Hello all,</p>
<p>I am quite new to Slicer but have used recent versions of Slicer (one year). Recently I noticed that when I started the program (several different versions… I am currently on 4.9.0 but it is the same for 4.6)<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c70afb7e6c55928109d4a8862636472f2bbdd7c.png" data-download-href="/uploads/short-url/6l8raqQX6Uc75RgEs14u34cutRy.png?dl=1" title="3D_Slicer_4_9_0-2018-05-20" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c70afb7e6c55928109d4a8862636472f2bbdd7c_2_690x438.png" alt="3D_Slicer_4_9_0-2018-05-20" data-base62-sha1="6l8raqQX6Uc75RgEs14u34cutRy" width="690" height="438" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c70afb7e6c55928109d4a8862636472f2bbdd7c_2_690x438.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/c/2c70afb7e6c55928109d4a8862636472f2bbdd7c_2_1035x657.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2c70afb7e6c55928109d4a8862636472f2bbdd7c.png 2x" data-dominant-color="F8F8F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D_Slicer_4_9_0-2018-05-20</span><span class="informations">1167×742 73.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div>, it does not start “3D scene view” and does not show any Dicom files from mine or sample data. I cannot find how to fix it. Has anyone have experienced this weird behavior?</p>
<p>Thank you!!<br>
Hyeri</p>

---

## Post #2 by @cpinter (2018-05-22 16:07 UTC)

<p>Hi Hyeri,</p>
<p>Your layout is set to “One-Up Quantitative”, so you would only see plots. Maybe you used it to show a DVH in full screen with SlicerRT… Anyway, You can change the layout using the layout selector button in the toolbar. It’s between the favourite module buttons and the place fiducial button, and in your screenshot it shows a bar chart.</p>
<p>Hope this helps,<br>
csaba</p>

---

## Post #3 by @HLee (2018-05-22 18:11 UTC)

<p>Great. It worked! Thank you!</p>
<p>Hyeri</p>

---
