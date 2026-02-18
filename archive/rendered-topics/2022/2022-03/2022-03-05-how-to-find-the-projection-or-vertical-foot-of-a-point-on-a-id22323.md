# How to find the projection or vertical foot of a point on a line?

**Topic ID**: 22323
**Date**: 2022-03-05
**URL**: https://discourse.slicer.org/t/how-to-find-the-projection-or-vertical-foot-of-a-point-on-a-line/22323

---

## Post #1 by @jumbojing (2022-03-05 10:29 UTC)

<p>How to find the projection or vertical foot of a point on a line?<br>
by python</p>

---

## Post #2 by @jumbojing (2022-03-05 11:40 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/569493686a501452726b08c92aab48b130a9ab06.png" data-download-href="/uploads/short-url/clVnQF5PFYOp5HNYKCm6Bgsc6lU.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/569493686a501452726b08c92aab48b130a9ab06_2_690x218.png" alt="image" data-base62-sha1="clVnQF5PFYOp5HNYKCm6Bgsc6lU" width="690" height="218" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/569493686a501452726b08c92aab48b130a9ab06_2_690x218.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/569493686a501452726b08c92aab48b130a9ab06_2_1035x327.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/569493686a501452726b08c92aab48b130a9ab06.png 2x" data-dominant-color="45455E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1311×415 17.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>好吧, 这其实是个简单的几何问题如图:<br>
可以先求出PA和PO<sup class="footnote-ref"><a href="#footnote-74966-1" id="footnote-ref-74966-1">[1]</a></sup>的长度,然后用勾股定理求出AO的长度,再用<a href="https://github.com/jumbojing/PedicleScrewSimulator-1/blob/fda7d17841cb6b1a5dcb788fd8555f469010827b/PedicleScrewSimulatorWizard/Helper.py#L178-L198" rel="noopener nofollow ugc">Helper.p2pexLine()</a>, 就可以求出来了. 方法有点笨…不知道谁还有更好的方法呢?</p>
<blockquote>
<p>Well, this is actually a simple geometric problem as shown in the figure: You can first find the lengths of PA and PO[1], then use the Pythagorean theorem to find the length of AO, and then use Helper.p2pexLine(), you can find it  . The method is a bit stupid…do not know who has a better method?</p>
</blockquote>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-74966-1" class="footnote-item"><p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#measure-distances-of-points-from-a-line" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a> <a href="#footnote-ref-74966-1" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---
