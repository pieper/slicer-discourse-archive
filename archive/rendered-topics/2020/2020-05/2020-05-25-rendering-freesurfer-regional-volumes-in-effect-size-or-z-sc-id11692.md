# Rendering Freesurfer regional volumes in Effect size or Z-score ColourMaps

**Topic ID**: 11692
**Date**: 2020-05-25
**URL**: https://discourse.slicer.org/t/rendering-freesurfer-regional-volumes-in-effect-size-or-z-score-colourmaps/11692

---

## Post #1 by @p.wib (2020-05-25 12:57 UTC)

<p>Hi</p>
<p>I am analyzing the volume of 20 Freesurfer automated segmented structures, which can be visualized label statistics as per FreeSurfer’s atlas labels.</p>
<p>As I have several MR subjects, groups and time points, without creating a GLM .mgh Freesurfer files, is it possible to input each of the group mean differences (e.g. Cohen’s d effect size or Z-score) and project these difference with color-gradient labels?</p>
<p>Thanks!<br>
Pierre</p>

---

## Post #2 by @pieper (2020-05-25 16:13 UTC)

<p>There’s nothing pre-programmed for that exact calculation I think, but it should be pretty straightforward to write a script for that.  You can get all the scalar data as numpy arrays and perform all the statisics.</p>

---

## Post #3 by @p.wib (2020-05-26 01:27 UTC)

<p>Thanks, Steve. I think I wasn’t clear with my question. I already have the effect sizes statistics. I just need to input these numbers so that I can get a color-gradient label maps. Is it possible, and where, to input the effect size or Z-scores in color-gradient?</p>
<p>Thanks</p>

---

## Post #4 by @pieper (2020-05-26 17:45 UTC)

<p>Okay, thanks for the clarification.  Are these z scores defined per-vertex of the freesurfer model?  If so you can assign these as scalar field data for the model, easiest to do that with a numpy array, something <a href="https://gist.github.com/pieper/f9da3e0a73c70981b48d0747132526d5#file-guide-py-L48-L54">like this</a>.</p>

---

## Post #5 by @coco (2024-03-12 15:47 UTC)

<p>Hi Pierre, I have the same paradigm here (trying to visualise segments based on size statistics. wondering if you managed to get this to work ?<br>
If so, could you share a script, please ?<br>
s</p>

---
