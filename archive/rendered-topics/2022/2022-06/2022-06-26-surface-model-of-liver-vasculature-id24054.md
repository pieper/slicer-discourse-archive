# Surface model of liver vasculature

**Topic ID**: 24054
**Date**: 2022-06-26
**URL**: https://discourse.slicer.org/t/surface-model-of-liver-vasculature/24054

---

## Post #1 by @orxshi (2022-06-26 20:01 UTC)

<p>Hi</p>
<p>I am looking for a ready-to-download surface model of liver vasculature. Only the arteries (PHA, RHA, LHA and their child segments) are required for radioembolization simulation. Is there a sample to download?</p>

---

## Post #2 by @RafaelPalomar (2022-06-27 10:24 UTC)

<p>Hello <a class="mention" href="/u/orxshi">@orxshi</a></p>
<p>we are working in a Slicer extension that can be used to generate this data (<a href="https://github.com/ALive-research/Slicer-Liver" rel="noopener nofollow ugc">Slicer-Liver</a>). This week we will be available in <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/" rel="noopener nofollow ugc">Project Week 37</a> if you would like to have a chat on it. There is also a nice project (<a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation" rel="noopener nofollow ugc">RVesselXLiverSegmentation</a>) which is somehow complementary to our work.</p>
<p>When it comes to data. We have models based on veins, not arteries. The segmens can be computed with the  Slicer-Liver extension that we will try to release during this week in the extension manager.</p>
<p>Rafael</p>

---

## Post #3 by @orxshi (2022-06-27 11:30 UTC)

<p>I have tried to use RVesselXLiverSegmentation but extracting arteries and veins is beyond my anatomy knowledge. Until I get together with my doctor friend I need a ready-made model of arteries/veins. However, at this stage I am also OK with any branched tubular geometry resembling arteries or veins.</p>
<p>Can Slicer-Liver extract veins from CT scans without user intervention?</p>

---

## Post #4 by @RafaelPalomar (2022-06-27 19:13 UTC)

<p>I see. Do you only need a single model? Slicer-liver comes with a testing dataset of 1 liver with segmented portal/hepatic veins. 3D reconstruction of that is automatic in 3D Slicer and with Slicer-Liver you could use the segments extraction to manually extract the segments. Segments extraction is not very tedious and hopefully will be ready during this week.</p>

---
