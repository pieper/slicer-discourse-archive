# How do I view the 3D rendering of CT dental images?

**Topic ID**: 43718
**Date**: 2025-07-15
**URL**: https://discourse.slicer.org/t/how-do-i-view-the-3d-rendering-of-ct-dental-images/43718

---

## Post #1 by @Wonderer (2025-07-15 04:25 UTC)

<p>Dr. “A” provided a USB drive with 348 zipped {dot} dcm images which are just that, images. I took the drive to another Dr.'s office Dr. “B” and they were unable to generate any 3D renderings and could only see the images which did not help them.</p>
<p>On my computer with 3D slicer, and “AutomatedDentalTools”, I can see slices (yay) and the 3D grid but no renderings in 3D. What else do I need to do to enable Dr. B to see the 3D renderings? I’m thinking I will bring my laptop into their office or send them screen captures of the 3D images once I can generate them.</p>

---

## Post #2 by @muratmaga (2025-07-15 05:03 UTC)

<p>If you successfully imported the dicom sequence into Slicer, you can use the <code>Volume Rendering</code> with the CBCT preset (assuming that’s what these are) to create the 3D renderings.</p>

---

## Post #3 by @Wonderer (2025-07-15 22:19 UTC)

<p>I deeply appreciate the response as I am almost totally lost!</p>
<p>The files are dental CT scans.</p>
<p>I have looked at the [Volume Rendering] Module and only only see [Volume:] with my files next to it and below [Inputs] then [Display] and [Preset] underneath and in [Select a Preset]  I don’t see any CBCT presets. All of the presets start with “CT”, “MR”, “DT1”, “US” or “uTC” (I’m not sure about the 1 because it is so small). I suspect that I have the wrong menu displayed.</p>
<p>I guess I should have stated that I am totally new at this but fascinated. I am working my way through the “<a href="https://slicer.readthedocs.io/en/5.8/user_guide/modules/volumerendering.html" class="inline-onebox" rel="noopener nofollow ugc">Volume rendering — 3D Slicer documentation</a>” file but am hoping to shortcut having to learn all of this to give the dentist some images to save a tooth. <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=14" title=":grin:" class="emoji" alt=":grin:" loading="lazy" width="20" height="20"></p>
<p>BTW, I have somehow decreased the default contrast in the other three windows so they are now difficult to view.</p>

---

## Post #4 by @Wonderer (2025-07-15 23:22 UTC)

<p>I have now managed to see a static rendering of the roof of the mouth. So getting there I guess.</p>

---

## Post #5 by @Wonderer (2025-07-15 23:45 UTC)

<p>The program hung and I restarted and reloaded the data files. Now the contrast looks good.</p>

---

## Post #6 by @muratmaga (2025-07-16 01:22 UTC)

<aside class="quote no-group" data-username="Wonderer" data-post="3" data-topic="43718">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/e99b99/48.png" class="avatar"> Wonderer:</div>
<blockquote>
<p>I don’t see any CBCT presets.</p>
</blockquote>
</aside>
<p>You are correct, I was wrong. I thought there was a CBCT preset, but apparently not. not sure how it will work for your dataset, but <strong>US-Fetal</strong>, and <strong>CT-Chest-Contrast-Enhanced</strong> presets give good enough rendering for a sample CBCT dataset provided with Slicer. Start with those, and use the SHIFT slider to adjust the levels.</p>

---

## Post #7 by @Wonderer (2025-07-16 22:29 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="2" data-topic="43718">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>CBCT preset</p>
</blockquote>
</aside>
<p>Now there is a rendering (not sure how) of all of the teeth. How is one tooth and the portion of jaw isolated for 3D rendering?</p>

---
