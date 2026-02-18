# Margin Tool does not change anything

**Topic ID**: 46002
**Date**: 2026-01-30
**URL**: https://discourse.slicer.org/t/margin-tool-does-not-change-anything/46002

---

## Post #1 by @Silver_Fish (2026-01-30 13:21 UTC)

<p>Hi!</p>
<p>I want the brown segmentation shrink a little, and the yellow segmentation grow a little, only on the edges of both segmentations. So I selected “inside all visible segments.” But nothing changes after clicking “Apply.” Even if I make the margin size very large, nothing changes. What should I change to fix the problem?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bcbc1a02f7e46f4f8c0fd46d2a90ee757508c0bc.jpeg" data-download-href="/uploads/short-url/qVCLKXp7E864mKHbp5FTOTCLlqk.jpeg?dl=1" title="Screenshot 2026-01-28 at 11.28.37 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bcbc1a02f7e46f4f8c0fd46d2a90ee757508c0bc_2_622x500.jpeg" alt="Screenshot 2026-01-28 at 11.28.37 AM" data-base62-sha1="qVCLKXp7E864mKHbp5FTOTCLlqk" width="622" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bcbc1a02f7e46f4f8c0fd46d2a90ee757508c0bc_2_622x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bcbc1a02f7e46f4f8c0fd46d2a90ee757508c0bc_2_933x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bcbc1a02f7e46f4f8c0fd46d2a90ee757508c0bc_2_1244x1000.jpeg 2x" data-dominant-color="ADB0AC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2026-01-28 at 11.28.37 AM</span><span class="informations">1920×1542 264 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @mikebind (2026-01-30 17:04 UTC)

<p>Try setting the editable region to “Inside critical structures” (the segment you want to shrink), and then select the segment you want to grow and grow it by your desired margin.  I suspect that while your masking settings seem OK to me, there is either a bug or a complication in applying them, and this is an alternative approach that should achieve the same thing.</p>

---

## Post #3 by @cpinter (2026-02-02 10:00 UTC)

<p>I agree that it should work like this. Especially as you say that you tried larger margins… The only thing I can think of is maybe the invisible segments are interfering somehow. If you delete them (just for the sake of debugging) and try the same thing does it work?</p>
<p>What Slicer version do you use? Is it possible for you to share this scene?</p>

---

## Post #4 by @Silver_Fish (2026-02-18 04:05 UTC)

<p>Thank you. I agree it could generally achieve the similar purpose, but I thought in theory the two approaches are different.<br>
When selecting “Inside all visibal segments,” shrink of critical structures should only change the segmentation in-between <em>it</em> and <em>dental material</em>, but both segments as a whole will not shrink(so the edge between <em>critical structure</em> and <em>box</em> will not change).<br>
When selecting “"Inside critical structures” only, the entire <em>critical structure</em> segments will shrink, and that will include the edge inbetween <em>critical structure</em> and <em>box</em>.</p>

---

## Post #5 by @Silver_Fish (2026-02-18 04:07 UTC)

<p>I was using 5.11.0 I believe. Sorry I might lose the track of this file. If I can, how would I share the scene?</p>

---

## Post #6 by @Silver_Fish (2026-02-18 04:15 UTC)

<p>But I have a similar problem in another file. Here’s a video recording for it. <a href="https://drive.google.com/file/d/1Mq9AKCVHwiC-zbx2QyQlk-SWhOCxNnUu/view?usp=share_link" rel="noopener nofollow ugc">Video Recording: Bug for Segmentation - Editable Area</a></p>
<p>I want to change the pink edge into <em>dental material</em>. At first when I select Editable Area as “Inside critical structures,” I can’t paint anything. But when I select “everything,” you can see that the painter tool is working.</p>
<p>Even if I try to select “Inside visible segmentation” and only let dental material and critical structures as visible, I still cannot paint anything.</p>
<p>I’m using Slicer 5.11.0-2026-01-21.</p>

---

## Post #7 by @cpinter (2026-02-18 11:54 UTC)

<p>Save the scene into an MRB file (see in <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#save-data">documentation</a> if unsure) then share the file via the same drive you shared the video with.</p>
<p>I watched the video and I think the first painting attempt should work. Now the only thing that occurs to me is that the geometry of the segmentation and the underlying image might be different. If you use “inside critical structures” but with “Sphere brush” checked, does it make a difference?</p>
<p>Thanks!</p>

---
