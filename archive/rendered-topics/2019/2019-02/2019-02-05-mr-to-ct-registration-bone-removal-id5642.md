# MR to CT registration, bone removal

**Topic ID**: 5642
**Date**: 2019-02-05
**URL**: https://discourse.slicer.org/t/mr-to-ct-registration-bone-removal/5642

---

## Post #1 by @opetne (2019-02-05 14:57 UTC)

<p>I have 2 series of a dog what had a brain tumor: a dual energy, vascular CT and MR. First of all, I’d like to register the 2 series to each other. I tried several methods: fiducial registration and Elastix but without any results. From the MR series, I’d like to reconstruct the tumor for displaying it’s size. As next, I’d like to reconstruct the vasculature and extract the skull from the model. So far I was not able to make a usable model. Is there someone who could help me with the steps, where I could made the mistakes?<br>
The series can be found here:<br>
<a href="https://justanatomy.ddns.net:5001/sharing/5OjBzbkKw" class="onebox" target="_blank" rel="nofollow noopener">https://justanatomy.ddns.net:5001/sharing/5OjBzbkKw</a></p>
<p>Thanks in advance</p>

---

## Post #2 by @muratmaga (2019-02-05 17:16 UTC)

<p>Can you define what you mean “without any results”? Did they not complete or not given you sufficient precision to align then. Did you try brains registration module?</p>

---

## Post #3 by @opetne (2019-02-05 20:13 UTC)

<p>Dear Murat,</p>
<p>Without result means that if I the CT was the fixed volume at the elastix there was a blurry image and the bony markers were absolutely not in an overlaping position. If I tried the fiducial registration, nothing happened.</p>

---

## Post #5 by @muratmaga (2019-02-06 04:50 UTC)

<p>Also fiducial registration definitely works. Make sure you specify the same number of fiducials from each scan in the exact same order. I have a tutorial for it for a very different context, but it may help you to identify what went wrong for you.<br>
<a href="https://blogs.uw.edu/maga/2018/12/using-landmarks-to-manually-superimpose-two-volumes/" class="onebox" target="_blank" rel="noopener">https://blogs.uw.edu/maga/2018/12/using-landmarks-to-manually-superimpose-two-volumes/</a></p>
<p>I had a quick try and ended up with this result with rigid registration with General Registraiton (Brains) module with centering the volumes prior to registration. Your CT and MR are very different in content, if you need better alignment you do need to crop more carefully and pay attention to the warnings to DICOM browser is giving. I don’t have any experience with angiograms, so I can’t tell what exactly was wrong.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97ee06681119a94e3b3ba67b0f23299539ec9e00.png" data-download-href="/uploads/short-url/lG23ZbaE2chE5dkCNnHPoyP65ji.png?dl=1" title="dog_coregistration"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97ee06681119a94e3b3ba67b0f23299539ec9e00_2_309x500.png" alt="dog_coregistration" data-base62-sha1="lG23ZbaE2chE5dkCNnHPoyP65ji" width="309" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97ee06681119a94e3b3ba67b0f23299539ec9e00_2_309x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97ee06681119a94e3b3ba67b0f23299539ec9e00_2_463x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/7/97ee06681119a94e3b3ba67b0f23299539ec9e00_2_618x1000.png 2x" data-dominant-color="4D0907"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">dog_coregistration</span><span class="informations">690×1116 87.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @opetne (2019-02-06 12:13 UTC)

<p>Dear Murat,</p>
<p>I workde with the fiducial registration on horse joints and it worked well. But this time no movement of the two fiducial set was seen. They remained in the same (original position).</p>
<p>Ors</p>

---

## Post #7 by @muratmaga (2019-02-06 19:20 UTC)

<p>That really shouldn’t be the case. Your two volumes have very different physical locations. You should get a large translation with fiducial registration. I suggest checking your steps.<br>
Remember fiducials don’t get moved to the new location automatically you need to apply the resultant transform to them (as well as the volume).</p>

---
