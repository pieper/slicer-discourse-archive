# Clinical use of Slicer extensions?

**Topic ID**: 1630
**Date**: 2017-12-11
**URL**: https://discourse.slicer.org/t/clinical-use-of-slicer-extensions/1630

---

## Post #1 by @PaulMartinMurphy (2017-12-11 06:32 UTC)

<p>Are there any examples of Slicer extensions that have been commercialized and approved by the FDA for clinical use, or does the Slicer license forbid all such usage?</p>

---

## Post #2 by @ihnorton (2017-12-11 15:09 UTC)

<aside class="quote no-group" data-username="PaulMartinMurphy" data-post="1" data-topic="1630">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/paulmartinmurphy/48/16075_2.png" class="avatar"> PaulMartinMurphy:</div>
<blockquote>
<p>Are there any examples of Slicer extensions that have been commercialized and approved by the FDA for clinical use</p>
</blockquote>
</aside>
<p>I’m vaguely aware of several in the approval process, but it’s not my place to identify them publicly (I’ll leave that to others directly involved if they wish).</p>
<aside class="quote no-group" data-username="PaulMartinMurphy" data-post="1" data-topic="1630">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/paulmartinmurphy/48/16075_2.png" class="avatar"> PaulMartinMurphy:</div>
<blockquote>
<p>does the Slicer license forbid all such usage?</p>
</blockquote>
</aside>
<p>Certainly not – allowing such usage is one of the goals of the license. For reference, here is the <a href="https://github.com/Slicer/Slicer/blob/master/License.txt">Slicer license</a>.</p>
<p>The license is intentionally written without “copyleft” provisions (<a href="https://en.wikipedia.org/wiki/Copyleft">Wikipedia definition</a>), which means that there is no requirement to release your code if you use Slicer as a foundation or incorporate specific algorithms. There is a notice requirement, similar to MIT License. There are, also, patent provisions in the license. The basic wording is similar to Apache v2, which is widely-used and well-understood. The main difference I can see are that the patent grant is only specifically contributor-to-Brigham (with right to sublicense), whereas Apache grant is contributor-to-anyone <em>and</em> Apache also specifies a retaliation clause.</p>
<p>As is hopefully obvious, (a) I’m not an attorney <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> and (b) if this is a concern to you please consult a qualified open source attorney!</p>

---

## Post #3 by @ihnorton (2017-12-11 15:50 UTC)

<p>See also:</p>
<p><a href="https://www.slicer.org/wiki/CommercialUse" class="onebox" target="_blank">https://www.slicer.org/wiki/CommercialUse</a></p>

---

## Post #4 by @lassoan (2017-12-11 16:37 UTC)

<p>There are many examples for commercial applications and clinical use, but there are just a few products that are commercially available and acknowledge publicly that they are based on Slicer (most of them are not publicly announced yet, or they were products that were developed up to some point but did not make it to the marketplace).</p>
<p>I’m helping out in multiple Slicer-based product development projects that seek FDA approval within 1-2 years. We coordinate our efforts with Kitware and others so that we can share between all products those parts of the design history file that describe the Slicer platform (software process, requirement specifications, verification and validation plans, test results, etc.). In the long term, we may even share these documentation publicly, so that anybody who builds products based on Slicer can use it as a starting point.</p>
<p>Let us know if you were interested in more details or want to chat about specific questions in private (you can send private messages through this forum).</p>

---

## Post #5 by @pieper (2017-12-12 15:15 UTC)

<aside class="quote no-group" data-username="ihnorton" data-post="2" data-topic="1630">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>There are, also, patent provisions in the license. The basic wording is similar to Apache v2, which is widely-used and well-understood. The main difference I can see are that the patent grant is only specifically contributor-to-Brigham (with right to sublicense)</p>
</blockquote>
</aside>
<p>Right - the idea here is that all contributions to Slicer require the contributor to grant sublicense to everyone under the terms of the Slicer license.</p>
<p>Of course a productization effort needs to review the whole license agreement and other context, but be sure to note the section highlighted below – it is meant to say explicitly that anyone who uses the code commercially is wholly responsible to meet all regulatory requirements.</p>
<p><a href="https://github.com/Slicer/Slicer/blob/b6210f278eb0029bd7058b0f824f3f7cc65ee103/License.txt#L147-L156" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/b6210f278eb0029bd7058b0f824f3f7cc65ee103/License.txt#L147-L156</a></p>

---
