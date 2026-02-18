# How to make a cuboid tube between two points

**Topic ID**: 15555
**Date**: 2021-01-16
**URL**: https://discourse.slicer.org/t/how-to-make-a-cuboid-tube-between-two-points/15555

---

## Post #1 by @slicer365 (2021-01-16 15:17 UTC)

<p>When I use Segment Editor, I can make a tube through Draw tube, but what should I do if I need to make a cuboid tube between two points?</p>

---

## Post #2 by @lassoan (2021-01-16 15:40 UTC)

<p>Can you draw a sketch of what exactly you would like to achieve?</p>

---

## Post #3 by @slicer365 (2021-01-16 15:45 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fef8f2849c09602436d5f5581ab553feddfe9cd.jpeg" alt="u=1840670376,809413264&amp;fm=11&amp;gp=0" data-base62-sha1="bp8YlL5CHAa29ymLkwmA4vcZ0Zf" width="200" height="256"> Like this tube，I need a cuboid,replace it</p>

---

## Post #4 by @lassoan (2021-01-16 15:59 UTC)

<p>There are many options how to achieve this. For example, using Markups to model module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e0c2e6f0bb3d0a6439b338e89b531f6d92f1e3ab.jpeg" data-download-href="/uploads/short-url/w4kwOlD2SjF24H1FQknfGdQbaSD.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e0c2e6f0bb3d0a6439b338e89b531f6d92f1e3ab_2_690x419.jpeg" alt="image" data-base62-sha1="w4kwOlD2SjF24H1FQknfGdQbaSD" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e0c2e6f0bb3d0a6439b338e89b531f6d92f1e3ab_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e0c2e6f0bb3d0a6439b338e89b531f6d92f1e3ab_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e0c2e6f0bb3d0a6439b338e89b531f6d92f1e3ab_2_1380x838.jpeg 2x" data-dominant-color="464649"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1371 456 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Would you prefer to draw a segmentation or just display a tool trajectory?</p>
<p>I’m just curious, Why do you need rectangular cross-section? All the drills, catheters, etc. have circular cross section.</p>

---

## Post #7 by @lassoan (2021-01-16 16:24 UTC)

<p>All the tools for creating such tool guides fully automatically (using a small Python scripted module) is already available in Slicer.</p>
<p>To create a model, probably the easiest is to create the stick first, for example by running this command:</p>
<pre><code class="lang-python">slicer.modules.createmodels.logic().CreateCube(20,30,120)
</code></pre>
<p>then apply a transform to position it, and import it into the segmentation.</p>
<p>You can find examples for most operations in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a>.</p>

---

## Post #8 by @slicer365 (2021-01-16 16:28 UTC)

<p>Thank you very much ,you have helped me solve the problem. <img src="https://emoji.discourse-cdn.com/twitter/blush.png?v=9" title=":blush:" class="emoji" alt=":blush:"></p>

---
