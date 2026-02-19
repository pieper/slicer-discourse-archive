---
topic_id: 18730
title: "How To Fill In An Existing Segment"
date: 2021-07-14
url: https://discourse.slicer.org/t/18730
---

# how to fill in an existing segment

**Topic ID**: 18730
**Date**: 2021-07-14
**URL**: https://discourse.slicer.org/t/how-to-fill-in-an-existing-segment/18730

---

## Post #1 by @art (2021-07-14 12:48 UTC)

<p>Operating system: windows 10 64bit<br>
Slicer version: 4.11.2020<br>
Expected behavior: I am trying to segment a liver in non-contrast CT. The steps are as follows:</p>
<ol>
<li>threshold HU 0~100 for masking.</li>
<li>paint liver in multiple axial slices.</li>
<li>use fill between slices to get volume segmentation of liver.</li>
<li>The result is a pretty good definition of liver volume. HOWEVER, inside the liver VOI, there are multiple small pixel sized holes in the liver because of the initial threshold. I would like to fill in these holes.</li>
<li>I select the liver VOI → paint → in the masking section, I changed the editable intensity range set to -1024~3071, change the editable area to “inside segment_1” (which is the liver VOI).</li>
<li>Then using a sphere shaped paint brush, i paint the whole liver. I expected the liver pixel holes to “fill up” within the boundaries of liver VOI, as the masking is fully open, and the editable area is within the liver VOI.</li>
</ol>
<p>Actual behavior: painting anywhere in the CT doesn’t do anything in this setting. no paints on any area, either within the liver VOI or outside the VOI. Only by changing the editable area to “everywhere” does the paint brush paint anything. but this will not solve my problem as I have to re-paint the liver again, and worry about the margins. “inside all segments” does not work either, as the paint brush paints outside the liver VOI. it also does not fill in the small pixels inside the liver VOI.</p>
<p>Sorry for the long question. any help will be appreciated.</p>
<p>Thanks!<br>
Art</p>

---

## Post #2 by @pieper (2021-07-14 14:47 UTC)

<p>It sounds like you could use the Island tools.</p>

---

## Post #3 by @lassoan (2021-07-15 14:14 UTC)

<aside class="quote no-group" data-username="art" data-post="1" data-topic="18730">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/art/48/11615_2.png" class="avatar"> art:</div>
<blockquote>
<p>“inside segment_1” (which is the liver VOI).</p>
</blockquote>
</aside>
<p>This will prevent all painting outside your liver segment. Holes are outside the segment, too, so you won’t be able to fill them, so do not select this masking option, just use the default (Editable area: everywhere; Editable intensity range: disabled; Modify other segments: all).</p>
<p>You can fill in holes one by one using Islands effect as <a class="mention" href="/u/pieper">@pieper</a> suggested above, or you can get all the internal holes filled fully automatically using “Wrap solidify” effect (provided by SurfaceWrapSolidify extension).</p>

---
