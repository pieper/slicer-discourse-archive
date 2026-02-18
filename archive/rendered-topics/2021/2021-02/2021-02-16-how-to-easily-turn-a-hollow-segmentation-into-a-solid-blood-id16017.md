# How to easily turn a hollow segmentation into a solid (blood pool) segmentation

**Topic ID**: 16017
**Date**: 2021-02-16
**URL**: https://discourse.slicer.org/t/how-to-easily-turn-a-hollow-segmentation-into-a-solid-blood-pool-segmentation/16017

---

## Post #1 by @Jezza (2021-02-16 20:04 UTC)

<p>Operating system: macOS Catalina 10.15.7<br>
Slicer version: 4.11 20200930</p>
<p>Hi,</p>
<p>I’m aware that it is possible to turn a hollow segmentation (e.g artery) into a solid (blood pool) version. This is done using the following:</p>
<ul>
<li>Logical operators effect, Invert operation =&gt; Apply</li>
<li>Islands effect, Keep largest island =&gt; Apply</li>
</ul>
<p>If I erase parts of my original segment, this technique no longer works, because the “invert” tool will <strong>still</strong> appliy over the original segment volume, meaning that the inverted segment will not be an <em>isoltated island</em> that can be removed using the “keep largest island” tool.</p>
<p>I want to know how to control the target volume of the “invert” tool. How can I adjust it so that it matches my modified segmentation which no longer has the same volume as it originally had?</p>

---

## Post #2 by @lassoan (2021-02-16 20:09 UTC)

<p>I would recommend to delete the “bridges” at the opening of the vessel to isolate the vessel lumen from the background. You can use Paint or Scissors effect for this.</p>

---

## Post #3 by @Jezza (2021-02-16 20:26 UTC)

<p>Hi Iassoan, could you clarify what you mean by “bridges”? Once I’ve inverted my model it becomes very hard to find the section I need to delete. Since my vessel is curved, I’m forced to make the modifications in the 3D window to be accurate.</p>

---

## Post #4 by @lassoan (2021-02-17 04:34 UTC)

<p>You can make the segmentation semi-transparent so that you can clearly see all the vessel endpoints in the 3D view and you can snip the ends with Scissors effect.</p>

---

## Post #5 by @Yvonne (2023-05-20 20:03 UTC)

<p>Hi Jeremy,</p>
<p>I’m hoping to do the same thing on an artery following your tips. I can do the inversion easily, however, after clicking on ‘keep the largest island’, nothing changes.</p>
<p>Have you encountered this before? Thanks in advance <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Yvonne</p>

---
