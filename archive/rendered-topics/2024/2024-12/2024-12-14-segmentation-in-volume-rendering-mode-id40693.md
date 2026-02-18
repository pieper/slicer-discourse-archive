# Segmentation in volume rendering mode

**Topic ID**: 40693
**Date**: 2024-12-14
**URL**: https://discourse.slicer.org/t/segmentation-in-volume-rendering-mode/40693

---

## Post #1 by @alex_He (2024-12-14 09:08 UTC)

<p>Hi I am trying to do segmentation in 3d view in volume rendering mode but failed, any advise?</p>

---

## Post #2 by @muratmaga (2024-12-15 02:26 UTC)

<p>You cannot visualize segmentations with volume rendering. Segmentations are shown as 3D closed surface representation (models). Hit the the Show 3D button to visualize your segments. Or see the user documentation <a href="https://slicer.readthedocs.io">https://slicer.readthedocs.io</a> (and scroll down to segmentation link).</p>

---

## Post #3 by @alex_He (2024-12-15 09:25 UTC)

<p>Thanks for your advise, but I need to cutoff some parts in the volume rendering 3d view to see more insight of the volume, could you please advise me how to do it?</p>

---

## Post #4 by @muratmaga (2024-12-15 13:49 UTC)

<p>You can use the crop option in the volume rendering to cut your volume.</p>

---

## Post #5 by @alex_He (2024-12-16 05:08 UTC)

<p>Thanks for your advise, I will try it out.</p>

---

## Post #6 by @alex_He (2024-12-16 13:07 UTC)

<p>Hi after some trying , i notice that the crop options can only allow me to crop the volume with the rectangular crop box, but I need to crop the volume using a free enclosed surface , not the rectangular box. Or i need to trim the crop box to some other shape like wedge shape, please advise further.</p>

---

## Post #7 by @cpinter (2024-12-16 13:17 UTC)

<p>I think in the current Slicer version the best option you have is to use the Mask volume effect in Segment Editor. Create a segment (I suggest starting with using Scissors in 3D) that contains the part you want to keep, then go to the Mask volume tool, enter the background value (e.g. -3000 for CT), then click Apply. Now volume render the masked volume.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dd8fb0e04ceb668352d90474f22f63e36682baa.png" data-download-href="/uploads/short-url/4g2IZfz87x63H0VqKV2KViwRzEm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dd8fb0e04ceb668352d90474f22f63e36682baa.png" alt="image" data-base62-sha1="4g2IZfz87x63H0VqKV2KViwRzEm" width="538" height="499"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">538×499 21.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @alex_He (2024-12-16 13:23 UTC)

<p>Thanks, but I do not fully understand what you said, could you please explain a little more detail?</p>

---

## Post #9 by @cpinter (2024-12-16 13:25 UTC)

<p>I see you only saw the email. Please go to the forum page, I added a screenshot after submitting the comment.</p>

---

## Post #10 by @alex_He (2024-12-16 13:48 UTC)

<p>Ok , I got you, will try tomorrow. Thanks</p>

---
