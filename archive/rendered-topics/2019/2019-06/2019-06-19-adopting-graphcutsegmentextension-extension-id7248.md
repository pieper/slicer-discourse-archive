# Adopting GraphCutSegmentExtension extension?

**Topic ID**: 7248
**Date**: 2019-06-19
**URL**: https://discourse.slicer.org/t/adopting-graphcutsegmentextension-extension/7248

---

## Post #1 by @jcfr (2019-06-19 17:46 UTC)

<p>Dear Slicers,</p>
<p>The GraphCutSegmentExtension extension implements loadable module allowing to perform interactive segmentation using start shape prior for graph cut.</p>
<p>This is described in more details in <a href="http://imagine.enpc.fr/~de-la-gm/cours/UPEM/projects/Star%20Shape%20Prior%20for%20Graph-Cut%20Image.pdf">this publication</a></p>
<p>Associated repository is <a href="https://github.com/DaphneCD/GraphCutSegmentExtension" class="inline-onebox">GitHub - DaphneCD/GraphCutSegmentExtension: GraphCutSegmentExtension</a></p>
<h2><a name="p-25462-question-1" class="anchor" href="#p-25462-question-1" aria-label="Heading link"></a>Question</h2>
<p>Considering that the original developers do not have interested in maintaining the extension, is there any interest from the community in adopting the extension ?</p>
<h2><a name="p-25462-anticipated-work-2" class="anchor" href="#p-25462-anticipated-work-2" aria-label="Heading link"></a>Anticipated work</h2>
<ul>
<li>Create a SegmentEditor effect</li>
</ul>
<h2><a name="p-25462-illustrations-3" class="anchor" href="#p-25462-illustrations-3" aria-label="Heading link"></a>Illustrations</h2>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4fbbe44cecc1a64790dcc29acc5f6b95c7b2787.png" data-download-href="/uploads/short-url/s6AWnxf3mfYntLvT1lH6HOGTZtB.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c4fbbe44cecc1a64790dcc29acc5f6b95c7b2787.png" alt="image" data-base62-sha1="s6AWnxf3mfYntLvT1lH6HOGTZtB" width="128" height="128"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">128×128 13.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a22af3454efddb6a7a576bfd5efebeb42569af3d.png" data-download-href="/uploads/short-url/n8BmZbnIRFy0uQx5wih0JaJuTHn.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a22af3454efddb6a7a576bfd5efebeb42569af3d_2_690x415.png" alt="image" data-base62-sha1="n8BmZbnIRFy0uQx5wih0JaJuTHn" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a22af3454efddb6a7a576bfd5efebeb42569af3d_2_690x415.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a22af3454efddb6a7a576bfd5efebeb42569af3d_2_1035x622.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a22af3454efddb6a7a576bfd5efebeb42569af3d_2_1380x830.png 2x" data-dominant-color="B2B2B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1680×1011 202 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2019-06-20 00:26 UTC)

<p>I’ll have a look and see if this segmentation method has some special properties that makes it better than existing semiautomatic methods (grow from seeds, fast marching, watershed, etc).</p>

---

## Post #3 by @lassoan (2019-06-20 01:19 UTC)

<p>The method is similar to Fast marching (works on a single segment, grows from a seed point). A potential advantage can be that it might be constrained to segment blob or star-shaped structures, so it might be less likely to leak.</p>
<p>In a number of files there are some ambiguous comments like “The code is for research use only”. If this means that the authors don’t take any responsibility for any errors that the code may have, then that’s fine. However, if they mean that they restrict usage of the extension then I would just abandon it.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> have you been able to contact the authors? Did they clarify what license they distribute this extension with?</p>

---

## Post #4 by @jcfr (2019-06-20 17:30 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="7248">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>have you been able to contact the authors?</p>
</blockquote>
</aside>
<p>Yes</p>
<aside class="quote no-group quote-modified" data-username="lassoan" data-post="3" data-topic="7248">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>In a number of files there are some ambiguous comments like “The code is for research use only”. If this means that the authors don’t take any responsibility for any errors that the code may have, then that’s fine. However, if they mean that they restrict usage of the extension then I would just abandon it.<br>
[…]<br>
Did they clarify what license they distribute this extension with?</p>
</blockquote>
</aside>
<p>The <a href="https://github.com/DaphneCD/GraphCutSegmentExtension/blob/master/License.txt">license file</a> found in the repository corresponds to Apache 2 license, but you are right the mention of “The code is for research use only” could be understood in multiple ways.</p>
<p>I will follow up with the original developers now to clarify this.</p>

---

## Post #5 by @jcfr (2019-06-20 17:59 UTC)

<p>Here is an update from the original maintainers:</p>
<blockquote>
<p>Dear Jean-Christophe,<br>
We do not have any issues with this code being used for any purposes,<br>
Olga.</p>
</blockquote>
<p><a class="mention" href="/u/lassoan">@lassoan</a> After you fork the repository in the Slicer organization or any other location of your convenience, it should be quite easy to integrate the outstanding pull requests.</p>

---

## Post #6 by @lassoan (2019-06-20 18:43 UTC)

<p>OK, I’ll fork the extension in the Slicer organization and merge your pull request.</p>

---
