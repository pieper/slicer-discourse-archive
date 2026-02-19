---
topic_id: 42471
title: "Unexpected Behaviour Remeshing In Surface Toolbox"
date: 2025-04-07
url: https://discourse.slicer.org/t/42471
---

# Unexpected behaviour remeshing in Surface Toolbox

**Topic ID**: 42471
**Date**: 2025-04-07
**URL**: https://discourse.slicer.org/t/unexpected-behaviour-remeshing-in-surface-toolbox/42471

---

## Post #1 by @evaherbst (2025-04-07 16:06 UTC)

<p>Hi all,</p>
<p>I was playing around with remeshing models, and I realized that if I do uniform remesh, with the same settings, and apply it twice, it shrinks on each run.</p>
<p>Here I applied it around 5-6 times to show the shrinkage:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee9341ea5aa9f90f8466e81fd57bff9f46c2c76c.png" data-download-href="/uploads/short-url/y2x8pvlQaCj36CJllfAmF7adv9G.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee9341ea5aa9f90f8466e81fd57bff9f46c2c76c_2_414x500.png" alt="image" data-base62-sha1="y2x8pvlQaCj36CJllfAmF7adv9G" width="414" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/ee9341ea5aa9f90f8466e81fd57bff9f46c2c76c_2_414x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee9341ea5aa9f90f8466e81fd57bff9f46c2c76c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee9341ea5aa9f90f8466e81fd57bff9f46c2c76c.png 2x" data-dominant-color="A0A8A5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">483×583 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I know you usually would not remesh twice with the same settings, but this was just to illustrate the issue, it also happens with other settings.<br>
I was wondering if this means there is some issue with the remeshing.</p>
<p>Thank you,<br>
Eva</p>

---

## Post #2 by @muratmaga (2025-04-07 19:32 UTC)

<p>If you are feeding the remeshed model iteratively as the input, I can see this happening. I suspect the operation alters the geometry a little bit, and subsequent runs on the same model increases the effect and makes it noticeable compared to the original?</p>

---

## Post #3 by @lassoan (2025-04-08 14:15 UTC)

<p>All resampling/remeshing operations are inherently lossy. In your workflow, always try to minimize the number of times you run lossy operations.</p>

---

## Post #4 by @evaherbst (2025-04-25 16:19 UTC)

<p>Thanks both! Yes the more iterations the worse it is - I do not intend to do a lot of interations in the end, I just noticed sometimes several iterations are nice for a good resampling outcome (upsampling first, then remshing) but the lossy-ness is too much of a problem and I found an alternative pipeline</p>

---
