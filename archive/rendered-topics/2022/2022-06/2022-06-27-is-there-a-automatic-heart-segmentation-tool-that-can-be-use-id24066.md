# Is there a automatic heart segmentation tool that can be used, similar to the ribcage

**Topic ID**: 24066
**Date**: 2022-06-27
**URL**: https://discourse.slicer.org/t/is-there-a-automatic-heart-segmentation-tool-that-can-be-used-similar-to-the-ribcage/24066

---

## Post #1 by @Monkeyking123 (2022-06-27 15:41 UTC)

<p>As in the aforementioned title,<br>
**Is there an automatic heart segmentation tool for segmenting the important heart structures:<br>
Left/Right (Ventricle/Atrium) , Superior/inferior vena cava/pulmonary artery etc</p>
<p>Since some CT scans shows plague and some structures are damaged, so it is hard to manually select precisely each structure for different patient CT scans.</p>
<p>WIll there be a tool in the future, or is there already one(Like Nvidia for tumor segmentation) in the Slicer already?</p>
<p>Thanks for your help!</p>

---

## Post #2 by @lassoan (2022-06-28 03:08 UTC)

<p>I’m not aware of any freely available model for it, but you can train your own. For heart segmentation on good-quality contrasted CT of healthy people you probably don’t need a lot of training data - maybe a few dozens of CT scans (you need more if you need a robust solution for various abonrmalities). You can do the same what <a class="mention" href="/u/rbumm">@rbumm</a> has done recently for lungs - used semi-automatic LungCTAnalyzer extension (internally uses <code>Grow from seeds</code> effect) to generate training data for MONAILabel.</p>

---

## Post #3 by @Monkeyking123 (2022-06-30 01:18 UTC)

<p>Thanks for the detailed reply</p>
<p>It is for the CT scans for people with cancer and its corresponding variants</p>

---

## Post #4 by @whu (2022-06-30 01:37 UTC)

<p>Most of the CT based segmentation paper cite the paper as this:</p>
<p>Tautz L, Neugebauer M, Hüllebrand M, et al. Extraction of open-state mitral valve geometry from CT volumes[J]. International Journal of Computer Assisted Radiology and Surgery, 2018, 13(11): 1741-1754.</p>
<p>But there still exist so much work to reproduce it.</p>
<p>Automatic segmentation may need landmark labels mannully.</p>

---
