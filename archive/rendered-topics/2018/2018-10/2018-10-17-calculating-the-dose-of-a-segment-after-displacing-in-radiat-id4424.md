# Calculating the dose of a segment after displacing in radiation fields

**Topic ID**: 4424
**Date**: 2018-10-17
**URL**: https://discourse.slicer.org/t/calculating-the-dose-of-a-segment-after-displacing-in-radiation-fields/4424

---

## Post #1 by @aseman (2018-10-17 04:38 UTC)

<p>Operating system: windows 10<br>
Slicer version:4.8.1<br>
Hi 3D slicer experts and all users<br>
I have dose volume and a specific segment(heart) that has been displaced in radiation fields; and following figure shows 2 states for heart in the radiation fields.Using DVHs I could calculate the maximum, minimum and mean dose for each state; but<br>
1- I want to know how much is the dose at any point in the heart , without using Iso doses ? is it possible?<br>
2-I want to know how much has  been the dose at different points changed with displacing the heart in radiation fields? In the other words , if we consider a desired point in the first state, how much is its dose after displacing?<br>
Thanks a lot<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fdfa7ad17d0fb5886488c57447fb677c418fcd35.png" alt="Picture" data-base62-sha1="AeNrVsDLgOyY3k78nDMdh7q0juB" width="408" height="242"></p>

---

## Post #2 by @cpinter (2018-10-17 14:52 UTC)

<ol>
<li>Select the dose volume as the foreground layer in the slice views. Then when you move the mouse over the voxels, the CT and dose values will be shown in the data probe in the bottom left.</li>
<li>Are you interested about corresponding points in the heart? Then you can register the two CTs using deformable registration. I suggest using the SlicerElastix extension or the BRAINS general registration module (it’s harder to initialize but <a href="https://www.slicer.org/wiki/Documentation/Nightly/Registration/RegistrationLibrary">here</a> is a library of examples). Once you have the transform going from one CT to another you can apply the same transform to the dose volume (in Data module double click on the rightmost cell and choose the transform or you can do it in the Transforms module or the Transforms tab in the Data module). Then you will be able to overlay the two dose volumes corresponding to the same anatomical positions.</li>
</ol>
<p>I suggest using the latest nightly version because I fixed a bug not too long ago about DVH calculation on transformed dose volumes. Or you can wait a day and use 4.10, which will be released tonight.</p>

---

## Post #3 by @aseman (2018-10-18 07:11 UTC)

<p>Hi<br>
Thank you very much for your guidelines; but I still have another question. I want to get a volume of heart that take a certain dose; in the other words , I want to know which areas of heart is getting the 20 Gy dose for each state separately , and identify those areas.<br>
Thanks a lot</p>

---

## Post #4 by @cpinter (2018-10-18 12:22 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DoseVolumeHistogram" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DoseVolumeHistogram</a></p>

---

## Post #5 by @aseman (2018-10-18 19:10 UTC)

<p>Hi<br>
Thank you very much for your guideline. I could quantitatively calculate how much volume of the heart received 2 Gy dose(for example %5 of total heart volume), using Dose Volume Histogram module; but unfortunately, I can’t observe this volume in 2D or 3D viewers. can you guide me?<br>
Thanks a lot</p>

---

## Post #6 by @aseman (2018-10-22 04:33 UTC)

<p>Hi<br>
Unfortunately, I didn’t receive any feedback. Is it possible to see V20 , which is quantitatively calculated by the Dose Volume Histogram module , in 2D or 3D viewer ? (V20: the volume which is received 20 Gy dose).  can you guide me?<br>
Thanks a lot</p>

---

## Post #7 by @cpinter (2018-10-22 13:43 UTC)

<p>It’s in the wiki page I sent you earlier:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DoseVolumeHistogram#Panels_and_their_use" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DoseVolumeHistogram#Panels_and_their_use</a><br>
You can calculate V20 within the DVH module, not in the viewers.</p>

---

## Post #8 by @lassoan (2018-10-22 14:18 UTC)

<aside class="quote no-group" data-username="aseman" data-post="6" data-topic="4424">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/c0e974/48.png" class="avatar"> aseman:</div>
<blockquote>
<p>Is it possible to see V20 , which is quantitatively calculated by the Dose Volume Histogram module , in 2D or 3D viewer ?</p>
</blockquote>
</aside>
<p>You can show regions above a certain dose threshold by using Segment Editor:</p>
<ul>
<li>Click <em>Threshold</em>  effect</li>
<li>Choose a segment of interest in <em>Masking</em> section / <em>Editable area</em></li>
<li>Add a new segment</li>
<li>Select the dose volume as master volume</li>
<li>Select desired dose range in the double-slider (e.g., move the left slider to 20, leave right slider at maximum)</li>
<li>Click <em>Apply</em></li>
<li>Click <em>Show 3D</em> to see the highlighted region in 3D views</li>
</ul>

---
