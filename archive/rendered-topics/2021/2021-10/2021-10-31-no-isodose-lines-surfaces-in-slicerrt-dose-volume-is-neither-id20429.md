# No isodose lines/surfaces in SlicerRT - dose volume is neither "GY" nor "RELATIVE"

**Topic ID**: 20429
**Date**: 2021-10-31
**URL**: https://discourse.slicer.org/t/no-isodose-lines-surfaces-in-slicerrt-dose-volume-is-neither-gy-nor-relative/20429

---

## Post #1 by @Harsforn (2021-10-31 13:39 UTC)

<p>Hi all,</p>
<p>I’m trying to generate a RT treatment plan and visualise isodose surfaces through the SlicerRT extension. I’ve added 5 beams and selected the Mock Python dose engine but after calculating, the output dose volume doesn’t appear to be working correctly - when trying to visualise isodoses through the corresponding module, I get the error: dose volume is neither “GY” nor “RELATIVE”. I’ve included screencaps of both the error and the External Beam Planning configuration.</p>
<p>Thanks for your time.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28834a4956a65308f06a3a769d3a7237cf3326de.png" data-download-href="/uploads/short-url/5MonYBHhQfa5JLHUtajEVOOCink.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28834a4956a65308f06a3a769d3a7237cf3326de_2_690x345.png" alt="image" data-base62-sha1="5MonYBHhQfa5JLHUtajEVOOCink" width="690" height="345" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28834a4956a65308f06a3a769d3a7237cf3326de_2_690x345.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28834a4956a65308f06a3a769d3a7237cf3326de_2_1035x517.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/28834a4956a65308f06a3a769d3a7237cf3326de_2_1380x690.png 2x" data-dominant-color="969A9A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2151×1077 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4dd821cbb89cdda4b27fc9a3c2707c71ac216ce.png" data-download-href="/uploads/short-url/wEDrqYrclahSZyZz5cu67QdOy3c.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4dd821cbb89cdda4b27fc9a3c2707c71ac216ce_2_468x500.png" alt="image" data-base62-sha1="wEDrqYrclahSZyZz5cu67QdOy3c" width="468" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4dd821cbb89cdda4b27fc9a3c2707c71ac216ce_2_468x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4dd821cbb89cdda4b27fc9a3c2707c71ac216ce_2_702x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4dd821cbb89cdda4b27fc9a3c2707c71ac216ce_2_936x1000.png 2x" data-dominant-color="FBFBFB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">972×1037 28.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Mik (2021-11-02 06:58 UTC)

<aside class="quote no-group" data-username="Harsforn" data-post="1" data-topic="20429">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/85e7bf/48.png" class="avatar"> Harsforn:</div>
<blockquote>
<p>I get the error: dose volume is neither “GY” nor “RELATIVE”</p>
</blockquote>
</aside>
<p>Dear <a class="mention" href="/u/harsforn">@Harsforn</a><br>
It’s not an error, just a warning message that calculated dose volume doesn’t have a dose units attribute. You can calculate isodose surface in any case, but the units on the color bar will be “MU” (monitor units). Could you confirm that calculated dose volume has expected dose distribution? That it’s not filled with zero values?</p>
<p>P.S.<br>
I don’t know how Mock Python dose engine calculates dose distribution (Is it working or not).</p>

---

## Post #3 by @cpinter (2021-11-02 09:40 UTC)

<p>Mock Python is just an example plugin to show developers how to write a dose engine in Python. It simply fills the beam volumes with a constant value (maybe with some noise applied). It should not be used for anything that intends to approximate real scenarios, only for testing.</p>

---

## Post #4 by @Harsforn (2021-11-02 09:44 UTC)

<p>Ahh I see; thank you. Is there another standalone photon dose engine/plugin available? I see that the orthovoltage engine uses dosxyzynrc but was hoping to avoid relying on that if possible.</p>

---

## Post #5 by @cpinter (2021-11-02 09:50 UTC)

<p>Unfortunately our repeated past attempts to secure funding for adding a photon dose engine (among other things) were unsuccessful, so there are no good options to calculate MV photon dose in SlicerRT.</p>

---

## Post #6 by @cpinter (2021-11-02 10:33 UTC)

<p>To answer your question about standalone photon engine, I have been looking at matRad (who at the time were not interested in working together on Slicer integration) but I haven’t checked the project for years. Back then the engine was not fully validated but was said to be pretty accurate.</p>
<p>If you find the matRad engine useful, and then have some affinity and motivation, we’d be happy to help in integrating it into Slicer. It should be fairly simple using SlicerMatlabBridge, but none of my colleagues had time to check in depth matRad and vice versa. Let me know if this sounds interesting to you!</p>

---

## Post #7 by @Harsforn (2021-11-02 10:45 UTC)

<p>I’ve actually been using matRad together with Slicer! I performed segmentation etc. through slicer (very user friendly) and then exported to matRad for dose calculations but I’ve found matRad to be very prescriptive with the kinds of files/formats it accepts - for example, if a scalar volume is not isotropic the DICOM import fails with an error about the slices being misaligned (which I corrected with Slicer’s Crop Volume but then ran into negative indexing issues with MATLAB/matRad).</p>
<p>I’ve been going back and forth between Slicer and matRad which is why I was asking about SlicerRT’s dose engine in this post - an attempt to cut matRad out of my workflow due to numerous compatibility issues I ran into.</p>
<p>While I am very interested in its integration with Slicer, my project is all but finished tomorrow so I wouldn’t be much help I’m afraid. I am a big fan of Slicer in the short time I’ve used it though and will continue to follow its development. Thank you all for your great work!</p>

---

## Post #8 by @zhuyingying1234 (2022-03-26 06:32 UTC)

<p>hi experts and all<br>
I also encountered the same problem after I imported the DICOM image and conducted the beams and dose calculation. After reading the above solution, I understand is that this slicer RT can only be used for reading plans and some post-processing, but not for making real plans, right?<br>
thank your answer</p>

---

## Post #9 by @Mik (2022-03-26 08:15 UTC)

<p>Correct. You can’t create a real plan and calculate dose distribution.</p>

---

## Post #10 by @zhuyingying1234 (2022-03-26 08:23 UTC)

<p>thank you sir<br>
I would also like to ask why some people studying 3D-Slicer RT restored the complete iso-dose line and DVH diagram？</p>

---

## Post #11 by @Mik (2022-03-26 08:37 UTC)

<p>My guess, that a user calculated dose distribution in third party program or package and now the user wants to calculate a new DVH histogram with already available CT and Segmentation data.</p>
<p>It’s a long and hard way to create a new TPS for scratch.</p>

---

## Post #12 by @zhuyingying1234 (2022-03-26 09:10 UTC)

<p>so is plan design feasible in Slicer RT? Have you tried it? I tried it and found it was not very good. There were only the adjustment of the shooting field Angle and the lead door, which felt a little similar to the forward intensity adjustment, and the DVH was also not ideal…</p>

---

## Post #13 by @Mik (2022-03-26 12:14 UTC)

<aside class="quote no-group" data-username="zhuyingying1234" data-post="12" data-topic="20429">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zhuyingying1234/48/67107_2.png" class="avatar"> zhuyingying1234:</div>
<blockquote>
<p>so is plan design feasible in Slicer RT?</p>
</blockquote>
</aside>
<p>It’s unfinished. Many things are absent and it can be used only as a template for future use or development.</p>
<blockquote>
<p>and the DVH was also not ideal…</p>
</blockquote>
<p>Do you have any suggestions how to do it more usable, robust and user friendly?</p>

---

## Post #14 by @zhuyingying1234 (2022-03-26 13:07 UTC)

<p>Thank you very much for your answer. As a novice, I hope I can make progress together with  slicer RT.thank you very much.</p>

---
