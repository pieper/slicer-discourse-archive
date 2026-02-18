# How can we fill air gaps 

**Topic ID**: 34567
**Date**: 2024-02-27
**URL**: https://discourse.slicer.org/t/how-can-we-fill-air-gaps/34567

---

## Post #1 by @FAUSTINE1 (2024-02-27 14:16 UTC)

<p>hi all,</p>
<p>I am segmenting the geometries of the spine, brain, spinal cord and lungs from a CT scan using Threshold effect. I would like to export to an .stl file but there is a lot of air gaps appearing. When I am trying to paint and fill those air gaps manually it changes on the CT scan but not on the label map volume. this means that if I convert it to stl they will still be appearing. could you please tell me how could I fill them ?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c16545d4761cd1f941f1fc22fa04dcba9d0dbfd.png" data-download-href="/uploads/short-url/mgOke0XdTpsCR98xFza2101FeA5.png?dl=1" title="Screenshot 2024-02-27 at 14.14.55" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c16545d4761cd1f941f1fc22fa04dcba9d0dbfd.png" alt="Screenshot 2024-02-27 at 14.14.55" data-base62-sha1="mgOke0XdTpsCR98xFza2101FeA5" width="164" height="500" data-dominant-color="6F7A58"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-02-27 at 14.14.55</span><span class="informations">410×1244 2.61 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks!</p>
<p>Faustine</p>

---

## Post #2 by @lassoan (2024-02-27 14:22 UTC)

<p>To avoid air gaps all you need to do is to start with a solid body segment. You can get it from TotalSegmentator or MONAIAuto3DSeg. You can then add the other segments to this segmentation.</p>
<p>Note that TotalSegmentator and MONAIAuto3DSeg can segment body, spine, lungs (and a 100+ other segments) fully automatically. You can train your own models for anything that is missing (e.g., spinal cord, brain).</p>

---

## Post #4 by @lassoan (2024-02-27 19:53 UTC)

<p>You can create a solid body segment and then add all the other segments. Since there was no air in the body originally and you only painted in additional segments, there will be no air in the resulting segmentation.</p>

---
