# Problem with showing the organs in the Digitally Reconstructed Radiographs(DRR)

**Topic ID**: 5687
**Date**: 2019-02-08
**URL**: https://discourse.slicer.org/t/problem-with-showing-the-organs-in-the-digitally-reconstructed-radiographs-drr/5687

---

## Post #1 by @aseman (2019-02-08 08:18 UTC)

<p>Hi 3D Slicer experts and all<br>
I want to get the distance between the organs (such as the heart) and the radiation fields(like the Figure A) ; and I need the DRR (Digitally Reconstructed Radiographs) to this. I imported the DRR from treatment planning system(TPS) to Slicer, but I can’t see the organs with this image.(Figure B) and have this problem both in 3D Sicer 4.8.1(windows) and 4.10.1 (Linux). can you help me on how to view the radiation field and organs in DRR( in beams eye view)?<br>
Thanks A lot<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b87c1a3c169ec7aa9e9f17ddb52428e3856b6a15.jpeg" alt="Fig%20A" data-base62-sha1="qk1K3HuJbUU94s4RUXjfNB8oU1n" width="160" height="283"></p>

---

## Post #2 by @cpinter (2019-02-08 14:46 UTC)

<p>Do you have to measure the distance in the beam’s eye view or the smallest distance would be useful too?<br>
If you show the DRRs in the 3D view (just hit the eye button in Data module), does it appear in the right place?</p>

---

## Post #3 by @aseman (2019-02-09 05:16 UTC)

<p>Hi<br>
I want to measure the different distances in the beam’s eye view, such as the maximum distance that the heart is located in the field ; or, the distance between the lung and the edge of the field in the middle of the field.<br>
also, Display the DRR in three dimensions view as shown below<br>
Thanks a lot<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a2d393e0bb73996d8821bedbdf707fd585c7bfb.png" data-download-href="/uploads/short-url/aAcdSOapG6Dk97P5kXBOOXyPf8D.png?dl=1" title="picture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a2d393e0bb73996d8821bedbdf707fd585c7bfb.png" alt="picture" data-base62-sha1="aAcdSOapG6Dk97P5kXBOOXyPf8D" width="575" height="500" data-dominant-color="9A9ACD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">picture</span><span class="informations">656×570 20.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @aseman (2019-02-26 11:45 UTC)

<p>Hi 3D slicer experts<br>
Unfortunately I didn’t receive any feedback for my question !  I want to calculate the lung distance at the center of beam’s eye view (CLD)  and  also for the heart , the maximum heart distance (MHD)  from the posterior edge of radiation field like the below DRR… Is it possible to calculate these parameters with Slicer or not?<br>
Thanks a lot<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b9fa27fe5a26b28859012e0584fe865120d70c5.png" alt="picture%2CMHD" data-base62-sha1="mcI1tzYMTnkP5z18UkYN8f3wpHD" width="359" height="340"></p>

---

## Post #5 by @aseman (2020-03-19 05:39 UTC)

<p>Hi 3D Slicer Experts and all<br>
If I import the CT image and RT Structure into the slicer, is it possible to display organs in beam’s eye view with slicer 4.10 (or 4.11) or not?<br>
Thanks a lot</p>

---

## Post #6 by @cpinter (2020-03-19 08:59 UTC)

<p>The beam’s eye view function is in the Room’s Eye View module, with an unfinished implementation, see <a href="https://github.com/SlicerRt/SlicerRT/blob/master/RoomsEyeView/qSlicerRoomsEyeViewModuleWidget.cxx#L759">here</a>. There is a good chance that it would be very easy to make it work. I’ll take a look at it today.</p>

---

## Post #7 by @cpinter (2020-03-19 12:07 UTC)

<p><a class="mention" href="/u/aseman">@aseman</a> I fixed a bunch of problems in SlicerRT, and patched up the beam’s eye view function so that it does what it should. There are probably still bugs in the Room’s Eye View module, but it is still experimental, so it’s expected. Anyhow, at least beam’s eye view now works.</p>
<p>Please download tomorrow’s preview release and let us know.</p>

---
