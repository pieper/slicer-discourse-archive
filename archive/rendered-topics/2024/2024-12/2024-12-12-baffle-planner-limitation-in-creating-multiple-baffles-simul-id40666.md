# Baffle Planner: Limitation in Creating Multiple Baffles Simultaneously

**Topic ID**: 40666
**Date**: 2024-12-12
**URL**: https://discourse.slicer.org/t/baffle-planner-limitation-in-creating-multiple-baffles-simultaneously/40666

---

## Post #1 by @JohnWick (2024-12-12 21:17 UTC)

<p>Hi everyone,</p>
<p>I’m experiencing an issue while trying to create two baffles on the same model. Unfortunately, whenever I add a second baffle, it seems to overwrite or delete the first one, as shown in the attached image.</p>
<p>Could anyone please help me figure out how to resolve this problem? I suspect this might be a common issue, so any guidance would be greatly appreciated.</p>
<p>Thank you in advance!<br>
John<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38f48912ec2951fcf77ac94a023d54481143fc88.png" data-download-href="/uploads/short-url/87QEuAIYSjTuQqHNO1X0Fnu3c4U.png?dl=1" title="pic" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38f48912ec2951fcf77ac94a023d54481143fc88_2_690x246.png" alt="pic" data-base62-sha1="87QEuAIYSjTuQqHNO1X0Fnu3c4U" width="690" height="246" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38f48912ec2951fcf77ac94a023d54481143fc88_2_690x246.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38f48912ec2951fcf77ac94a023d54481143fc88_2_1035x369.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38f48912ec2951fcf77ac94a023d54481143fc88_2_1380x492.png 2x" data-dominant-color="707294"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic</span><span class="informations">3390×1210 328 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-12-13 00:39 UTC)

<p>You can have any number of baffle surface models. Tpu can add a new one by right-clicking on the baffle model selector and choose to create new.</p>

---

## Post #3 by @JohnWick (2024-12-13 13:49 UTC)

<p>Dear Andras,</p>
<p>Thank you for your prompt response. Unfortunately, it’s still not working. I started from scratch and followed the steps to create a new baffle from the other closed curve. While it does create a new baffle, it deletes the previous one (Create new model was selected). That’s why I’m reaching out for help. I’ve attached a screenshot that shows the two closed curves, but only one baffle is crated.</p>
<p>Best regards,<br>
John<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3286d090c0ce0b5c73d699af1b7154b7075f983.png" data-download-href="/uploads/short-url/u7ZmdG8jqrWzJKqx7IevfTJV3kT.png?dl=1" title="pic2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3286d090c0ce0b5c73d699af1b7154b7075f983_2_690x263.png" alt="pic2" data-base62-sha1="u7ZmdG8jqrWzJKqx7IevfTJV3kT" width="690" height="263" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3286d090c0ce0b5c73d699af1b7154b7075f983_2_690x263.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3286d090c0ce0b5c73d699af1b7154b7075f983_2_1035x394.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3286d090c0ce0b5c73d699af1b7154b7075f983_2_1380x526.png 2x" data-dominant-color="686A8D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic2</span><span class="informations">3584×1368 347 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2024-12-13 17:23 UTC)

<p>Thank you, I see now. This was an unnecessary limitation, I’ve fixed it now. You can either make <a href="https://github.com/SlicerHeart/SlicerHeart/commit/7b4e534fd1ee1a6a57e5daa6bef9ca2a27c99bb8">this change</a> in the .py script on your computer now, or update the SlicerHeart extension tomorrow.</p>

---

## Post #5 by @JohnWick (2024-12-15 19:15 UTC)

<p>Thank you, Andras! It’s working smoothly now.</p>

---
