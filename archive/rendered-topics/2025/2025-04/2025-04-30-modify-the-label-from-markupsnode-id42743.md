# Modify the Label from markupsNode

**Topic ID**: 42743
**Date**: 2025-04-30
**URL**: https://discourse.slicer.org/t/modify-the-label-from-markupsnode/42743

---

## Post #1 by @SANTIAGO_PENDON_MING (2025-04-30 09:10 UTC)

<p>Hi to everyone! A quick one for today:</p>
<p>Is possible to edit the blue text?</p>
<p>To my current work I don’t want to show the height: 2.000 mm</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/8/1831a6b8e45fee239eba20f18397f360b2f38566.jpeg" data-download-href="/uploads/short-url/3s1PRYrKkc9adngxjbz2jtT4APc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/1831a6b8e45fee239eba20f18397f360b2f38566_2_690x211.jpeg" alt="image" data-base62-sha1="3s1PRYrKkc9adngxjbz2jtT4APc" width="690" height="211" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/1831a6b8e45fee239eba20f18397f360b2f38566_2_690x211.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/1831a6b8e45fee239eba20f18397f360b2f38566_2_1035x316.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/8/1831a6b8e45fee239eba20f18397f360b2f38566_2_1380x422.jpeg 2x" data-dominant-color="7D676A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1478×452 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks to all <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @chir.set (2025-04-30 09:55 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="1" data-topic="42743">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>Is possible to edit the blue text?</p>
</blockquote>
</aside>
<p>You can do that in the ‘Measurement’ collapsible pane of the Markups module’s widget.</p>

---

## Post #3 by @SANTIAGO_PENDON_MING (2025-04-30 10:13 UTC)

<p>Hi <a class="mention" href="/u/chir.set">@chir.set</a> . Can you provide an example? Or more detailed explanation?<br>
(I want to do that using Python code)<br>
Thanks for the quick answer</p>

---

## Post #4 by @chir.set (2025-04-30 12:51 UTC)

<aside class="quote no-group" data-username="SANTIAGO_PENDON_MING" data-post="3" data-topic="42743">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/santiago_pendon_ming/48/66060_2.png" class="avatar"> SANTIAGO_PENDON_MING:</div>
<blockquote>
<p>using Python code</p>
</blockquote>
</aside>
<p>This should be straightforward:</p>
<pre><code class="lang-auto">cylinder = getNode("SH")
heightMeasurement = cylinder.GetMeasurement("height")
heightMeasurement.SetEnabled(False)
</code></pre>

---
