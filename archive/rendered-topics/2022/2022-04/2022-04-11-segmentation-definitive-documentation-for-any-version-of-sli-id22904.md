# Segmentation: Definitive documentation for any version of Slicer?

**Topic ID**: 22904
**Date**: 2022-04-11
**URL**: https://discourse.slicer.org/t/segmentation-definitive-documentation-for-any-version-of-slicer/22904

---

## Post #1 by @SlicerGroupie (2022-04-11 12:50 UTC)

<p>Is there a definitive set of documentation/tutorial <strong>on the topic of segmentation</strong> for any (reasonably) current version of slicer?</p>
<p>We ask because we’re trying to <em>manually</em> segment a medical image using Slicer. (My lab and I are new to Slicer, but not to medical images. We’re using Slicer v4.11.20210226 r29738 / 7a593c8, although we’ve tried earlier/later versions without success.)  It has been exceedingly frustrating (although we appreciate that Slicer must be a really great app), because not a single one of the tutorials/documents we have accessed via Slicer website has worked for us vis a vis segmentation.</p>
<p><strong>The key problem seems to be version control</strong>, more specifically, namely mismatch between the documentation vs the Slicer app itself. In other words, none of the videos/tutorials specify up-front which version of the Slicer they’re using, and so the steps in the tutorials/documentation don’t correspond to what we see in the app. On the other hand, we’ve been unable to find documentation for V. 4.11.x that actually works.</p>
<p>So – Is there a definitive set of tutorials/documentation <strong>for manual segmentation</strong> that actually works for Slicer v. 4.11 (or another reasonably current version), please?</p>
<p>Thank you in advance for any help you can provide!</p>

---

## Post #2 by @lassoan (2022-04-11 14:44 UTC)

<p>Thank you very much for your feedback.</p>
<p>In the past, documentation was loosely linked to the application: documentation on the <a href="https://www.slicer.org/wiki/Documentation/Nightly">wiki</a>, while the application on github. For latest Slicer versions, the documentation and the source code of the application are both stored in the same revision control system on github, so whenever the application is changed we can immediately update the documentation. It may happen that we forget to update the documentation and we only update screenshots after significant changes, but all these should be fixable quite easily.</p>
<p>The latest Slicer Stable Release is quite old now and it will be soon replaced by the current Slicer Preview Release. Therefore, I would recommend to <strong>use the latest Slicer Preview Release</strong>. The corresponding <strong><a href="https://slicer.readthedocs.io/en/latest/">documentation is available on readthedocs</a></strong>.</p>
<p>If you find that any text is not up-to-date, unclear, or incomplete, or there is any screenshot is misleading because it is too different from the current appearance then let us know. You can either report issues here or propose changes directly on github (click <code>Edit on GitHub</code> in the top-right corner in the documentation).</p>

---
