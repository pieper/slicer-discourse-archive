# Unable to load freesurfer surface in Slicer 4.10 stable and also in 4.11 nightly

**Topic ID**: 4528
**Date**: 2018-10-25
**URL**: https://discourse.slicer.org/t/unable-to-load-freesurfer-surface-in-slicer-4-10-stable-and-also-in-4-11-nightly/4528

---

## Post #1 by @devakumar (2018-10-25 12:34 UTC)

<p>Dear Slicer team</p>
<p>Unable to load freesurfer surface in Slicer 4.10 stable and also in 4.11 nightly.</p>
<p>Also, is it possible to load the gii files in 3D Slicer.</p>
<p>Regards<br>
Devakumar</p>

---

## Post #2 by @stephan (2018-10-25 13:10 UTC)

<p>Just my five cents on this, because I am using scalar overlays quite a bit (and I import them in the freesurfer [.w] format):<br>
It still works for me in 4.10.0<br>
There has always been an issue with multiple models in the scene, where after loading the scalar overlay file it is always attached to the first model in the hierarchy (i.e. the one which shows up topmost in the list of models in the model module). So do you maybe have multiple models in your scene and the overlay is simply attached to a different one than the one you’d like it to?</p>
<p>EDIT: After posting my reply, I re-read your original post again and realized you were not talking about the freesurfer <em>overlays</em> but some freesurfer <em>surface</em>. In this case, please disregard my reply. I have no experience with freesurfer <em>surface</em> files.</p>

---

## Post #3 by @pieper (2018-10-25 14:43 UTC)

<p><a class="mention" href="/u/devakumar">@devakumar</a> if you can link to specific datafiles that aren’t loading that could help people debug.</p>
<p>Also were these files working with previous versions of Slicer?</p>

---

## Post #4 by @lassoan (2018-10-25 15:20 UTC)

<p>Thanks for reporting this. I was able to reproduce the issue and fixed it. FreeSurfer surface reading should work well in nightly builds that you download tomorrow or later.</p>

---

## Post #5 by @devakumar (2018-10-27 07:20 UTC)

<p>Dear Andras, Thank you. I will try it today and let you know.</p>
<p>Dear Steve, Yes, I was able to load these files in the previous versions of Slicer.</p>
<p>Regards</p>
<p>Devakumar</p>

---

## Post #6 by @devakumar (2018-10-27 14:10 UTC)

<p>Hi Stephen</p>
<p>Yes, I had problem in loading the lh.pial and rh.pial surface files.</p>
<p>Is it possible to load surface files in gii format to 3D Slicer?</p>
<p>Regards<br>
Devakumar</p>

---

## Post #7 by @devakumar (2018-10-27 16:07 UTC)

<p>I managed to convert the gii to freesurfer surface format using mris_convert.</p>
<p>Devakumar</p>

---

## Post #8 by @devakumar (2018-10-27 18:02 UTC)

<p>The new nightly build is able to load freesurfer surface files. Thank you Andras.</p>
<p>Regards<br>
Devakumar</p>

---

## Post #9 by @lassoan (2018-10-27 21:01 UTC)

<p>Great! Thanks for testing.</p>

---
