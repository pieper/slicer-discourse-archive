# How to remove the bone in volume rendering

**Topic ID**: 15548
**Date**: 2021-01-16
**URL**: https://discourse.slicer.org/t/how-to-remove-the-bone-in-volume-rendering/15548

---

## Post #1 by @chendong9416 (2021-01-16 03:37 UTC)

<p>how to remove the bone in volume rendering, and adjust the opacity of the aorta to make it semitransparent?</p>
<p>thanks!</p>

---

## Post #2 by @lassoan (2021-01-16 05:18 UTC)

<p>On vascular CT images, bone and opacified vessel intensities are about the same, so in general you cannot remove bones without removing vessels, too.</p>
<p>To remove nodes, you can use Segment Editor module to segment the bones and blank out that region in the CT using Mask volume effect (or segment the aorta and blank out what is outside). Mask volume effect is provided by SegmentEditorExtraEffects extension.</p>

---

## Post #3 by @chendong9416 (2021-01-16 05:56 UTC)

<p>does scissors exist in volume rendering, just like in segment area?</p>

---

## Post #4 by @lassoan (2021-01-16 05:58 UTC)

<p>You use scissors effect on the segment that you will use to mask the volume. See this video for step-by-step tutorial:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="xZwyW6SaoM4" data-video-title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=xZwyW6SaoM4" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/xZwyW6SaoM4/maxresdefault.jpg" title='New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor' width="" height="">
  </a>
</div>


---

## Post #5 by @chendong9416 (2021-01-16 11:35 UTC)

<p>thanks, the first problem was solved</p>

---

## Post #6 by @rbumm (2021-01-16 14:15 UTC)

<p>Second problem: Go to “Segmentations”, select the Aorta segmentation, go to “Advanced” and find the 3D slider. Take it back until you are satisfied with the opacity result.</p>

---

## Post #7 by @chendong9416 (2021-01-16 15:03 UTC)

<p>i already tried this way by using local threshold and 3D opacity adjust, and confirmed that it works, but my question is how to realize semitransparent in volume rendering, thanks anyway.</p>

---

## Post #8 by @lassoan (2021-01-16 15:35 UTC)

<p>You can render general anatomy (including all bones) using volume rendering with reduced-opacity and display vasculature using segmentation. You can adjust volume rendering opacity in Volume rendering / Display / Advanced / Scalar opacity mapping -&gt; drag the control points down to make regions less opaque (more transparent). You can adjust segmentation opacity in Segmentations module Display / 3D slider.</p>
<p>Alternatively, you can display everything using multi-volume rendering:</p>
<ul>
<li>show non-masked volume with reduced opacity</li>
<li>show masked volume (that only contain the aorta) with higher opacity</li>
<li>enable multi-volume rendering: in Volume rendering module / Display / Rendering -&gt; choose “VTK multi-volume (experimental)”</li>
</ul>

---
