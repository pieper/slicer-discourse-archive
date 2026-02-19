---
topic_id: 22524
title: "3D Gel Dosimetry Slicelets Calibration Issue"
date: 2022-03-15
url: https://discourse.slicer.org/t/22524
---

# 3D gel dosimetry - Slicelets: Calibration issue

**Topic ID**: 22524
**Date**: 2022-03-15
**URL**: https://discourse.slicer.org/t/3d-gel-dosimetry-slicelets-calibration-issue/22524

---

## Post #1 by @Kawtar_Lakrad (2022-03-15 17:26 UTC)

<p>Operating system: windows 11<br>
Slicer version: 4:13<br>
I am having issue with the calibration; it is like if it is not applying the equation I am working with.<br>
Do you have any idea about this issue?<br>
Thank you.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/178ffb98fd832e9702445587b72eac44652eee15.png" data-download-href="/uploads/short-url/3mrsJTLT2M65Clnnwir2Qjk3O29.png?dl=1" title="Calibration issue" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/178ffb98fd832e9702445587b72eac44652eee15.png" alt="Calibration issue" data-base62-sha1="3mrsJTLT2M65Clnnwir2Qjk3O29" width="689" height="160" data-dominant-color="272727"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Calibration issue</span><span class="informations">1346×313 11.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-03-17 01:26 UTC)

<p>Please describe what you did, what you expected to happen, and what happened instead.</p>

---

## Post #3 by @Kawtar_Lakrad (2022-03-21 18:10 UTC)

<p>I applied a calibration function, and it is supposed to calibrate using it, but I noticed that even if I hit apply calibration, it doesn’t really use the function.<br>
Thank you for your help.</p>

---

## Post #4 by @lassoan (2022-03-22 02:24 UTC)

<p>We would need much more details - what data did you use, how exactly you calibrated, how did you check if the calibration was applied. If you find that it is too much work to describe each click then you can record your screen and share that video (upload to dropbox/onedrive/google drive and post the link here).</p>

---

## Post #5 by @Kawtar_Lakrad (2022-03-31 16:42 UTC)

<p>I use DICOM files for both planned and measured data. the planned data is dose (Gy) and the measured data is density change (HU). HU change is linear to the dose change so what I do is using segments → segment statics → then use those values to apply calibration. It used to work perfectly but now it is like if it is not taking the values I enter in consideration.</p>
<p>Thank you.</p>

---

## Post #6 by @lassoan (2022-04-03 14:49 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> can you have a look at this?</p>

---

## Post #7 by @cpinter (2022-04-04 11:26 UTC)

<p>If someone touches the Gel Dosimetry extension code then it will require much more than a few little fixes because it has not been maintained for years. I’m surprised it still works… probably there are Python errors in the interactor at every step (but the users don’t see that). I don’t have the capacity to volunteer that kind of time on this extension that is not related in any sense to my current projects.</p>
<p><a class="mention" href="/u/kawtar_lakrad">@Kawtar_Lakrad</a> Would it be possible to</p>
<ol>
<li>Do what you intend to do and then see what is in the Python interactor and paste the errors here?</li>
<li>In the meantime use a Slicer version where the extension worked well? Also if you can identify the last version that worked well for you it would be helpful for fixing this problem.</li>
</ol>

---
