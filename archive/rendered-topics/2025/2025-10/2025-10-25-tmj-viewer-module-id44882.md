# Tmj viewer module

**Topic ID**: 44882
**Date**: 2025-10-25
**URL**: https://discourse.slicer.org/t/tmj-viewer-module/44882

---

## Post #1 by @mohammed_alshakhas (2025-10-25 14:58 UTC)

<p>im working on modeule for view tmj images especially mri .  code vibing , zero coding skills or knowledge</p>
<p>now im at point of doing dual sagittal view and im trying to have independet slice intersection .</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/17b8cd64ab42acc9fbe2954b86dc398eafef81fa.jpeg" data-download-href="/uploads/short-url/3nQUYtHBWX2EJEvofGnsXAikWdI.jpeg?dl=1" title="Screenshot 2025-10-24 at 14.57.13" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17b8cd64ab42acc9fbe2954b86dc398eafef81fa_2_690x279.jpeg" alt="Screenshot 2025-10-24 at 14.57.13" data-base62-sha1="3nQUYtHBWX2EJEvofGnsXAikWdI" width="690" height="279" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17b8cd64ab42acc9fbe2954b86dc398eafef81fa_2_690x279.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17b8cd64ab42acc9fbe2954b86dc398eafef81fa_2_1035x418.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/17b8cd64ab42acc9fbe2954b86dc398eafef81fa_2_1380x558.jpeg 2x" data-dominant-color="272424"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-10-24 at 14.57.13</span><span class="informations">1920×779 91.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>the idea to have full control over each series independently . i did  many iteration with AI to work  the code for it but its not going very well . im just wonder if this is actually possible in slicer.</p>
<p>if anyone can help me this part , or tell me how to guide the ai technically  to acieve this .</p>

---

## Post #2 by @pieper (2025-10-25 15:14 UTC)

<p>It’s not clear to me exactly what you are trying to accomplish, but it sounds like the CompareVolumes module might already have the features you need.</p>

---

## Post #3 by @mohammed_alshakhas (2025-10-25 15:39 UTC)

<p>im try to view each series into different orientation side by side . im also trying to have each view to be independent , i can move them without  affecting others.</p>
<p>for example i do rotation and transform view without the second series being affected . bare in mind these are series from same volume.</p>
<p>in compare view i cant have indpendent control for each view . they seem to be synced which is not what i need</p>

---
