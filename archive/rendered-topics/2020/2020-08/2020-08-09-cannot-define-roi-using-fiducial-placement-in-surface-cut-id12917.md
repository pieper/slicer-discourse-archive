# Cannot define ROI using fiducial placement in Surface Cut

**Topic ID**: 12917
**Date**: 2020-08-09
**URL**: https://discourse.slicer.org/t/cannot-define-roi-using-fiducial-placement-in-surface-cut/12917

---

## Post #1 by @Erwin (2020-08-09 14:47 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2<br>
Expected behavior: Use surface cut to define an irregular ROI by fiducial placement</p>
<p>Actual behavior:<br>
I was trying to use fiducial placement to define a ROI via Surface Cut. However, I could only place single dots or regular cubes because both the place button and the delete button appeared in grey and not clickable. Has anyone ever experienced this before?</p>
<p>Many thanks,<br>
Erwin</p>

---

## Post #2 by @lassoan (2020-08-09 14:48 UTC)

<p>Maybe we broke backward compatibility when we added new features to Surface cut. Could you try if the latest Slicer Preview Release works well?</p>

---

## Post #3 by @jamesobutler (2020-08-09 15:21 UTC)

<p>I installed SegmentEditorExtraEffects extension today with Slicer 4.10.2 which contains the Surface Cut effect and everything seems to work. <a class="mention" href="/u/erwin">@Erwin</a> Did you also install the required MarkupsToModel extension when prompted during the install process of SegmentEditorExtraEffects through the ExtensionsManager?</p>

---

## Post #4 by @jamesobutler (2020-08-09 16:29 UTC)

<p>I can make it appear to be single dots when I have the option “Smooth Model” turned off and place points in say the Red slice viewer and then a couple in the Yellow slice viewer, but I can still apply and delete points as expected.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7daafcf1913cf31b693941d9bc9dd64254e77131.png" data-download-href="/uploads/short-url/hVI1uoLJwI7zEuRK7284W52jvu9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7daafcf1913cf31b693941d9bc9dd64254e77131_2_690x370.png" alt="image" data-base62-sha1="hVI1uoLJwI7zEuRK7284W52jvu9" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7daafcf1913cf31b693941d9bc9dd64254e77131_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7daafcf1913cf31b693941d9bc9dd64254e77131_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7daafcf1913cf31b693941d9bc9dd64254e77131_2_1380x740.png 2x" data-dominant-color="8E8E94"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 300 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @Erwin (2020-08-10 09:17 UTC)

<p>Hi James, thanks for getting back to me!<br>
I’ve installed all the required extensions and tried turning off smooth model, it still didn’t work. I can see the two buttons next to “Fiducial Placement” in your screenshot appeared clickable while mine strangely remained grey no matter how I try.</p>

---

## Post #6 by @Erwin (2020-08-10 09:27 UTC)

<p>Thanks Andras, it works!</p>

---

## Post #7 by @jamesobutler (2020-08-10 11:23 UTC)

<p>Hmm I still don’t believe we broke backwards compatibility as I was showing using Surface cut in Slicer 4.10.2 with success.</p>

---

## Post #8 by @Georgescu_George (2020-08-16 08:49 UTC)

<p>this is exactly my problem, did you manage to fix it somehow?</p>

---

## Post #9 by @jamesobutler (2020-08-16 13:34 UTC)

<p><a class="mention" href="/u/georgescu_george">@Georgescu_George</a> What extensions do you have installed? Did you restart Slicer as part of the install of some extensions? If you go to Help-&gt;Report a Bug after replicating the issue are there any errors reported at the bottom of the log?</p>

---

## Post #10 by @Georgescu_George (2020-08-16 14:17 UTC)

<p>I’ve switched to the Slicer Preview Release and now everything is fine.<br>
Thank you very much for coming back so fast with a response.</p>

---

## Post #11 by @jamesobutler (2020-08-16 14:58 UTC)

<p><a class="mention" href="/u/georgescu_george">@Georgescu_George</a> Could you still provide response to the questions I asked above? I’m curious to see what users might be facing when using Slicer 4.10.2.</p>

---

## Post #12 by @Georgescu_George (2020-08-17 05:43 UTC)

<p>My extensions are DCMQI, Markupstomodel, PETDICOMExtension, quantitative reporting, segmenteditorextraeffects and slicerdevelopmentToolbox. I did restart Slicer after installing the extensions.<br>
This is what I get at the bottom of the log:<br>
[CRITICAL][Stream] 17.08.2020 08:36:53 [] (unknown:0) - AttributeError: ‘module’ object has no attribute ‘markupstomodel’</p>

---

## Post #13 by @jamesobutler (2020-08-18 00:43 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Would this indicate some issue with installing and registering markupsToModels?</p>

---

## Post #14 by @lassoan (2020-08-18 01:38 UTC)

<p>Yes, it seems that MarkupsToModel module is not found for some reason.</p>

---
