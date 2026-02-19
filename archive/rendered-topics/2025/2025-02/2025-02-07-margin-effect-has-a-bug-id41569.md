---
topic_id: 41569
title: "Margin Effect Has A Bug"
date: 2025-02-07
url: https://discourse.slicer.org/t/41569
---

# Margin effect has a bug?

**Topic ID**: 41569
**Date**: 2025-02-07
**URL**: https://discourse.slicer.org/t/margin-effect-has-a-bug/41569

---

## Post #1 by @cui (2025-02-07 22:06 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6595b6c4b19d4a6259a700d76e004c2c79839749.jpeg" data-download-href="/uploads/short-url/euEZ4UOf9Ik8zzhBrXTJ2szm9BL.jpeg?dl=1" title="666430d163e78d149135c2ae0dfd7fc" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6595b6c4b19d4a6259a700d76e004c2c79839749_2_690x271.jpeg" alt="666430d163e78d149135c2ae0dfd7fc" data-base62-sha1="euEZ4UOf9Ik8zzhBrXTJ2szm9BL" width="690" height="271" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6595b6c4b19d4a6259a700d76e004c2c79839749_2_690x271.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6595b6c4b19d4a6259a700d76e004c2c79839749_2_1035x406.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/6595b6c4b19d4a6259a700d76e004c2c79839749_2_1380x542.jpeg 2x" data-dominant-color="1D1F1F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">666430d163e78d149135c2ae0dfd7fc</span><span class="informations">2853×1124 240 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Why can’t i click the “apply” button???</p>

---

## Post #2 by @muratmaga (2025-02-07 22:08 UTC)

<p>No there is no bug.<br>
It says <strong>Not feasible at current resolution</strong>. You need to change your margin size to a value appropriate for the resolution of your dataset.</p>

---

## Post #3 by @cui (2025-02-08 06:14 UTC)

<p>Thank you! My computer shows that the margin size needs to be set to 8mm<br>
or more before the Apply button can be clicked.<br>
If i want to increase the margin size by 3mm,how should i process my image?Does it need to be resampled?</p>

---

## Post #4 by @muratmaga (2025-02-08 17:58 UTC)

<p>You cannot use a margin size that’s less than the resolution of your data (since the minimum number you can dilate or erode is a single voxel). You can check the resolution of your data from the <code>Volumes</code> module. Based on what you are observing it is probably 7 or 8mm.</p>
<p>If you are certain units and spacing of your dataset is correct, then yes you will have to resample your data to higher resolution to be able to do 3mm erosion on this dataset.</p>

---

## Post #5 by @cui (2025-02-09 09:17 UTC)

<p>Thank you! Your  suggestions is very important for me.</p>

---
