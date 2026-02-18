# 3D model annotation at original resolution

**Topic ID**: 23264
**Date**: 2022-05-03
**URL**: https://discourse.slicer.org/t/3d-model-annotation-at-original-resolution/23264

---

## Post #1 by @NicolasRannou (2022-05-03 15:23 UTC)

<p>Hi, is it possible to annotate the vertices of a 3D model and keep the original vertex information?</p>
<p>I have a big 3d file (STL) of the mouth. I must classify each vertex of the model as Tooth, Jaw, or Preparation. Is there a way to do so without losing the original vertex information? All I can find at the moment requires data to be converted to a label map, hence losing the original information.</p>
<p>Alternatively, is it possible to “split” the mesh into separate smaller 3d models?</p>
<p>The workaround I can currently think of is to generate a high-res segmentation label map and then match the vertices from the original model to the closest one in the segmentation’s models.</p>
<p>Thanks!<br>
Nicolas</p>

---

## Post #2 by @pieper (2022-05-03 19:10 UTC)

<p>Hi <a class="mention" href="/u/nicolasrannou">@NicolasRannou</a> <img src="https://emoji.discourse-cdn.com/twitter/wave.png?v=12" title=":wave:" class="emoji" alt=":wave:" loading="lazy" width="20" height="20"></p>
<p>Did you try <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/probevolumewithmodel.html?highlight=Probe%20Volume%20With%20Model">ProbeVolumeWithModel</a>?</p>

---

## Post #3 by @NicolasRannou (2022-05-09 07:03 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>, thanks for the suggestion.<br>
I didn’t try and I’ll give it a shot, it seems promising!</p>
<p>Thanks!</p>

---
