# Totalsegmentator to generate segmentation files, and the use these files to compute CT/PET suv value. but get the wrong answers

**Topic ID**: 27948
**Date**: 2023-02-21
**URL**: https://discourse.slicer.org/t/totalsegmentator-to-generate-segmentation-files-and-the-use-these-files-to-compute-ct-pet-suv-value-but-get-the-wrong-answers/27948

---

## Post #1 by @zhang_ming (2023-02-21 14:05 UTC)

<p>without or with the Totalsegmentator plugin , I draw roi manually or by AI, and then use the suv tools ,compute get blank or error value.  pic here<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d154a328c742c80708d23c3b4c5b001c052ef439.png" data-download-href="/uploads/short-url/tRP7Oj5jHLr21MdXgWiHbwdnX85.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d154a328c742c80708d23c3b4c5b001c052ef439_2_690x369.png" alt="image" data-base62-sha1="tRP7Oj5jHLr21MdXgWiHbwdnX85" width="690" height="369" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d154a328c742c80708d23c3b4c5b001c052ef439_2_690x369.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d154a328c742c80708d23c3b4c5b001c052ef439.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d154a328c742c80708d23c3b4c5b001c052ef439.png 2x" data-dominant-color="DBDEDD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">796×426 46.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>may anyone help me to solve the problems.<br>
The in hospital Doctor want to use this to analysis cancer patients, that will help patients a lot.<br>
thank you very much</p>

---

## Post #2 by @pieper (2023-02-21 14:36 UTC)

<p>I’d suggest practicing with public sample data, e.g. PET/CT from TCIA or IDC, and then see what’s different in the data you have.  If you find issues with the code that are specific to your data, then see if you can upload deidentified examples to illustrate the issues for reproduction and debugging.</p>
<p>Be sure to note that the Slicer tools are not officially supported and are intended for research only.</p>

---

## Post #3 by @zhang_ming (2023-02-21 14:42 UTC)

<p>ok, got it.<br>
thank you very much.<br>
our research is about pet suv value on colon. to become a reference to cancer situation. so  the pet tools are very import for us</p>

---

## Post #4 by @zhang_ming (2023-02-21 14:59 UTC)

<p>Sorry, correction, our patient are not patients with intestinal cancer. We will try it as soon as possible according to your suggestion!</p>

---
