# In the "KEEP_LARGEST_ISLAND", is there a size limit for the largest island?

**Topic ID**: 19780
**Date**: 2021-09-21
**URL**: https://discourse.slicer.org/t/in-the-keep-largest-island-is-there-a-size-limit-for-the-largest-island/19780

---

## Post #1 by @jumbojing (2021-09-21 11:29 UTC)

<p>在应用<code>KEEP_LARGEST_ISLAND</code>时, 我得到了"0 island, 2 ignored", 可能是因为我"cropped volume"的太小了?</p>
<blockquote>
<p>When applying <code>KEEP_LARGEST_ISLAND</code>, I got “0 island, 2 ignored”. Maybe it is because my “cropped volume” is too small?</p>
</blockquote>

---

## Post #2 by @jumbojing (2021-09-21 11:40 UTC)

<p>How to change the “MinimumSize” of island.<br>
既然是"the largest island", 为何还要限制尺寸呢?感觉逻辑有问题呀</p>
<blockquote>
<p>Since it is “the largest island”, why do we need to limit the size? I feel that there is a problem with the logic.</p>
</blockquote>
<p><a class="mention" href="/u/lassoan">@lassoan</a>@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a>@RafaelPalomar</p>

---

## Post #3 by @lassoan (2021-09-21 18:04 UTC)

<p>Good catch. “Keep largest island” mode expects that the island you want to get is sufficiently big, but it is possible that you want to extract an island that is smaller than the currently set minimum size. We’ll keep the “Minimum size” option enabled for “Keep largest island” mode.</p>
<p>As a workaround, you can switch to “Remove small island” option, set the minimum size to a 1, then switch back to “Keep largest island” mode.</p>

---

## Post #4 by @jumbojing (2021-09-25 02:04 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> How to get the only one largest island? How to set the number of islands?</p>

---

## Post #5 by @lassoan (2021-09-25 02:05 UTC)

<p>Largest island option returns the largest island (one island).</p>

---

## Post #6 by @jumbojing (2021-09-25 02:10 UTC)

<pre><code class="lang-auto">    segmentEditorWidget.setActiveEffectByName("Islands")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("Operation", "KEEP_LARGEST_ISLAND")
    minSize = 1
    effect.setParameter("MinimumSize", minSize)
    effect.setParameter("maxNumberOfSegments", 1)

    effect.self().onApply()
</code></pre>
<pre><code class="lang-auto">3 islands created (0 ignored)
</code></pre>
<p>what’s wrong? above</p>

---

## Post #7 by @lassoan (2021-09-25 02:12 UTC)

<p>There is nothing wrong. Largest island option returns the largest island (one island). The debug message indicated that 3 islands were larger than the minimum size.</p>

---

## Post #8 by @jumbojing (2021-09-25 02:14 UTC)

<p>Thanks, I see… <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=10" title=":+1:" class="emoji" alt=":+1:"></p>

---
