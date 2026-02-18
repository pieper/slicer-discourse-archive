# IGSTK repository can't find for older version of slicer 4.8.1

**Topic ID**: 3808
**Date**: 2018-08-16
**URL**: https://discourse.slicer.org/t/igstk-repository-cant-find-for-older-version-of-slicer-4-8-1/3808

---

## Post #1 by @kamrul079 (2018-08-16 22:20 UTC)

<p>I am trying to use webcams or NDI tracking device with my already built module in slicer. I need to build IGSTK. But I could n’t find the repository for IGSTK. I need that version of IGSTK that will compatible with slicer 4.8.1 version. I need the repository of IGSTK to build that for tracking.</p>

---

## Post #2 by @Andinet_Enquobahrie (2018-08-16 23:33 UTC)

<p>Several of IGSTK’s functionalities are available in SlicerIGT and PLUS modules.  IGSTK has not been updated for years. I strongly recommend migrating your application to use SlicerIGT and PLUS modules instead</p>
<p>Checkout some tutorial material including tracking device interfacing</p>
<p><a href="http://www.slicerigt.org/wp/user-tutorial/" class="onebox" target="_blank" rel="nofollow noopener">http://www.slicerigt.org/wp/user-tutorial/</a></p>

---

## Post #3 by @kamrul079 (2018-08-17 15:23 UTC)

<p><a class="mention" href="/u/andinet_enquobahrie">@Andinet_Enquobahrie</a> thank you for your suggestion. Unfortunately, I can not be able to add the “SlicerIGT” extension with my slicer 4.8.1 that I had built from the source.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41d12a2f6b649d1ac7d27d90bcc1b162ec8fd261.png" data-download-href="/uploads/short-url/9ofatTijOPO05lj7VbRe5XWH2tH.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41d12a2f6b649d1ac7d27d90bcc1b162ec8fd261_2_627x500.png" alt="Capture" data-base62-sha1="9ofatTijOPO05lj7VbRe5XWH2tH" width="627" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41d12a2f6b649d1ac7d27d90bcc1b162ec8fd261_2_627x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41d12a2f6b649d1ac7d27d90bcc1b162ec8fd261.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41d12a2f6b649d1ac7d27d90bcc1b162ec8fd261.png 2x" data-dominant-color="FCFCFC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">928×740 22.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2018-08-17 17:14 UTC)

<p>If you build Slicer then you need to build all the extensions that you need. Once you have built Slicer, building extensions is very simple.</p>

---

## Post #7 by @kamrul079 (2018-08-17 18:50 UTC)

<p>I had built SlicerIGT module in slicer 4.8.1. As shown in the tutorial that under IGT category, a new “Sequences” category would exist but in my case, there is no “sequences”.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98895aa61a4690d775fa2f5835cc9a1967e05489.png" data-download-href="/uploads/short-url/lLoR1MSegEEZoo0nRQb86FlJhJn.png?dl=1" title="slicerigtt" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98895aa61a4690d775fa2f5835cc9a1967e05489_2_690x428.png" alt="slicerigtt" data-base62-sha1="lLoR1MSegEEZoo0nRQb86FlJhJn" width="690" height="428" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98895aa61a4690d775fa2f5835cc9a1967e05489_2_690x428.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98895aa61a4690d775fa2f5835cc9a1967e05489_2_1035x642.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/98895aa61a4690d775fa2f5835cc9a1967e05489_2_1380x856.png 2x" data-dominant-color="7B7C84"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicerigtt</span><span class="informations">1931×1200 283 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @jamesobutler (2018-08-17 23:02 UTC)

<p>Refer to the Slide right before the one you posted above.  It says to install the following extensions “SlicerIGT” and “Sequences”.  You probably haven’t built the <a href="https://github.com/SlicerRt/Sequences" rel="noopener nofollow ugc">Sequences</a> extension and that is why it is not showing in the module browser.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efa2e6246d70624f9c3642739fb4ce9f16bf58bc.jpeg" data-download-href="/uploads/short-url/ybV7Kc9LCJElQOxYGjdnLwBz3WI.jpeg?dl=1" title="SlicerIGT_tutorial_screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efa2e6246d70624f9c3642739fb4ce9f16bf58bc_2_642x500.jpeg" alt="SlicerIGT_tutorial_screenshot" data-base62-sha1="ybV7Kc9LCJElQOxYGjdnLwBz3WI" width="642" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efa2e6246d70624f9c3642739fb4ce9f16bf58bc_2_642x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/efa2e6246d70624f9c3642739fb4ce9f16bf58bc_2_963x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/efa2e6246d70624f9c3642739fb4ce9f16bf58bc.jpeg 2x" data-dominant-color="DFDFE5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerIGT_tutorial_screenshot</span><span class="informations">1086×845 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @kamrul079 (2018-08-19 00:38 UTC)

<p>Which version of “Sequence” I should build for slicer 4.8.1? What do you think?</p>

---

## Post #10 by @lassoan (2018-08-19 06:37 UTC)

<p>See repository url and tag/branch/hash for all extensions for Slicer 4.8: <a href="https://github.com/Slicer/ExtensionsIndex/tree/4.8">https://github.com/Slicer/ExtensionsIndex/tree/4.8</a></p>
<p>If an extension fails to build, report it at the extension’s bugtracker. If you don’t get response then you can post the problem on this forum (in a new topic for each problem).</p>

---
