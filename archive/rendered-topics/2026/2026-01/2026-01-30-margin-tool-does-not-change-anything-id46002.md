---
topic_id: 46002
title: "Margin Tool does not change anything"
date: 2026-01-30
url: https://discourse.slicer.org/t/46002
last_bumped: 2026-03-06T11:07:56.688Z
---

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

## Post #8 by @Silver_Fish (2026-02-24 22:58 UTC)

<p>Hi! Here is the MRB file for it. <a href="https://drive.google.com/file/d/1OWPzDUpL3AQ1JLyFzMnFgAYHsUk_o_Tw/view?usp=share_link" rel="noopener nofollow ugc">MRB file - bug for segmentation - editable area</a></p>

---

## Post #9 by @mhalle (2026-02-24 23:16 UTC)

<p>slicer-skill says this after looking at this thread and the relevant code, might be worth a try:</p>
<p>Technical Analysis of the Margin + Masking Interaction</p>
<p>Looking at the source code, the Margin effect uses ModificationModeSet when applying results (SegmentEditorMarginEffect.py:213). Here’s why “inside all visible segments” masking effectively nullifies it:</p>
<p>The code path:</p>
<ol>
<li>processMargin() (SegmentEditorMarginEffect.py:168-213) computes the grown/shrunk labelmap using vtkITKImageMargin, then calls:<br>
self.scriptedEffect.modifySelectedSegmentByLabelmap(<br>
modifierLabelmap, slicer.qSlicerSegmentEditorAbstractEffect.ModificationModeSet)</li>
<li>ModifySegmentByLabelmap() (vtkSlicerSegmentEditorLogic.cxx:1663) applies masking. When mask mode is not “Everywhere” (line 1722), it:
<ul>
<li>Calls UpdateMaskLabelmap() → calls GenerateEditMask()</li>
<li>GenerateEditMask() (vtkMRMLSegmentationNode.cxx:591-682) generates a binary mask that is 1 inside all visible segments and 0 outside</li>
<li>Applies this mask to the modifier labelmap (line 1821), zeroing out any voxels outside visible segments</li>
</ul>
</li>
<li>The critical “Set” mode preservation (lines 1823-1847): Because ModificationModeSet replaces the entire segment, the code preserves the segment’s existing content outside the mask region — it adds back the original segment data wherever the mask blocked editing.</li>
</ol>
<p>Why growing fails:</p>
<p>The expanded voxels from the Margin filter are, by definition, outside all existing visible segments. The mask zeros them out. Result: no change.</p>
<p>Why shrinking fails:</p>
<p>The Margin filter produces a smaller labelmap. But ModificationModeSet + masking preserves the original segment data outside the mask. The voxels that should be removed at segment edges get added back. Result: no change.</p>
<p>The paint issue (post <span class="hashtag-raw">#6</span>):</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a>’s hypothesis about geometry misalignment is likely correct. If the segmentation’s labelmap grid doesn’t align with the source volume, the “Inside [segment]” mask can end up empty at the paint location. The “Sphere brush” test would confirm this because it samples in world coordinates rather than relying on exact voxel alignment.</p>
<hr>
<p>Possible Fixes / Workarounds</p>
<p>For the user’s immediate goal (shift boundary between two segments):</p>
<ol>
<li>Workaround: Use the Logical Operators effect — copy the brown segment, shrink it with masking set to “Everywhere,” then subtract the shrunken copy from brown<br>
and add the difference to yellow.</li>
<li>Workaround: Set masking to “Everywhere” but use the Overwrite mode set to “Visible segments” — this way growing yellow will automatically eat into brown at<br>
their shared boundary.</li>
</ol>
<p>For the underlying bug: The Margin effect could potentially bypass masking for the computation itself and only use masking to constrain which boundaries are affected, rather than having the general masking pipeline mask the result. This would require changes to how the Margin effect interacts with the masking system.</p>

---

## Post #10 by @Silver_Fish (2026-02-25 00:25 UTC)

<p>And also: I remember in the past, I wanted to use scissor tool but only to cut in a limited depth. Since the scissors tool will cut with an infinite depth, so I was thinking of creating a volume mask and make it the editable area, so that scissors only cut things off within that masked volume.</p>
<p>I created the volume mask using “fill between slices”, but when I make it the editable area and used scissors tool, I found that scissors tool still cut to finite depth, which include voxels outside of the masked editable area.</p>
<p>Back then I was confused and didn’t proceed. Now I found that they are all about “editable area”, so maybe this description also helps with debug? I will add a video if I could reproduce the scene.</p>

---

## Post #11 by @jumbojing (2026-02-27 00:45 UTC)

<p>发件人：Michael Halle <a href="mailto:notifications@slicer.discoursemail.com">notifications@slicer.discoursemail.com</a><br>
收件人：gelamb@sina.com<br>
主题：[Slicer] Margin Tool does not change anything<br>
日期：2026年02月25日 07点16分</p>
<p>Someone replied to a topic you are Watching.</p>
<p>Hi Michael: My VPN is down. I can’t access Google, GitHub, Slicer extensions, or any external sites.</p>
<p>Please give me clear, detailed instructions and a full prompt for what you want me to test in 3D Slicer. I will try it and let you know what happens.</p>

---

## Post #12 by @drnoorfatima (2026-03-06 11:07 UTC)

<p>The Margin effect and any non-Everywhere masking mode are fundamentally incompatible due to how <code>ModificationModeSet</code> interacts with <code>GenerateEditMask</code>.</p>
<p>For anyone hitting this right now, here are two working workarounds depending on what you are trying to do:</p>
<p><strong>If you just need the Margin tool to actually work:</strong> Set Editable area to “Everywhere” before hitting Apply. This bypasses the mask conflict entirely. The Margin computation runs clean.</p>
<p><strong>If you need to shift a boundary between two specific segments</strong> (the original use case in this thread): Skip Margin entirely and use Python approach. I can write you the script you can dm me.</p>

---
