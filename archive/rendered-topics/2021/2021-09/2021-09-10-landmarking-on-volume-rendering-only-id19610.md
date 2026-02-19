---
topic_id: 19610
title: "Landmarking On Volume Rendering Only"
date: 2021-09-10
url: https://discourse.slicer.org/t/19610
---

# Landmarking on Volume Rendering Only?

**Topic ID**: 19610
**Date**: 2021-09-10
**URL**: https://discourse.slicer.org/t/landmarking-on-volume-rendering-only/19610

---

## Post #1 by @ebryson (2021-09-10 15:29 UTC)

<p>Hi,</p>
<p>A few colleagues have asked me if they have to make a model before they add landmarks, or if they can just load the volume, bring up the volume rending and start placing landmarks. The program allows you to do that but does it negatively effect the accuracy of your landmarks in anyway, or is it okay to do?</p>
<p>Thanks!</p>

---

## Post #2 by @muratmaga (2021-09-10 16:11 UTC)

<p>Short answer, if you are careful the difference will be quite small and shouldn’t affect your results.</p>
<p>More detailed answer is when you build a model from a volume you already determined what the surface would be and it won’t change any longer. So you have no potential for error in terms of where that landmark should (apart from your uncertainty). These are the positive sides of landmarking on models. On the other hand, you have to invest in time building the model, and in the end most models do not produce as much anatomical detail a nice volume rendering of the volume they came from (because you possibly have to downsample, smoothen the details etc). Plus, if some of your landmarks are internal, they harder to do in models.</p>
<p>If you are inclined towards doing landmarking on the volume rendering, I would suggest creating a volume rendering property that works for all your scans (this should be possible, if the scan and reconstruction settings are consistent across your specimens) and use that consistently to increase repeatability (if you constantly adjust your volume property, the resultant rendering will change and your landmark coordinates will change accordingly).</p>
<p>Finally, if your downstream analysis calls for models (e.g., you want to use semiLMPatches, or ALPACA or something outside of Slicer), building the model is unavoidable, and you might as well do the landmarking on models. We discuss these issues briefly in the SlicerMorph paper (<a href="https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.13669" rel="noopener nofollow ugc">https://besjournals.onlinelibrary.wiley.com/doi/10.1111/2041-210X.13669</a>), you may want to take a look at that.</p>
<p>In the end, this is a a very simple experiment you can do it for yourself (or your colleagues can do). Just do landmarks 3-4 specimen initially in the volume rendering, and then on the model derived from those volumes and measure the difference.</p>

---

## Post #3 by @ebryson (2021-09-10 16:36 UTC)

<p>Thank you, I’ll pass this on!</p>

---
