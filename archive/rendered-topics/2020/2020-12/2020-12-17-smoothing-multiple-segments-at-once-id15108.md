---
topic_id: 15108
title: "Smoothing Multiple Segments At Once"
date: 2020-12-17
url: https://discourse.slicer.org/t/15108
---

# Smoothing multiple segments at once

**Topic ID**: 15108
**Date**: 2020-12-17
**URL**: https://discourse.slicer.org/t/smoothing-multiple-segments-at-once/15108

---

## Post #1 by @Hannnonk (2020-12-17 13:03 UTC)

<p>Doing a segmentation of jejunum. When I include the whole jejunum in one segment it “melts together”:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55735fd792943e15e594bd0c6632b236d3a3aa69.jpeg" data-download-href="/uploads/short-url/cbVLXc7TUt0JyuM3BiHBbbEhNwd.jpeg?dl=1" title="jejunum melt" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55735fd792943e15e594bd0c6632b236d3a3aa69.jpeg" alt="jejunum melt" data-base62-sha1="cbVLXc7TUt0JyuM3BiHBbbEhNwd" width="690" height="384" data-dominant-color="7F8D9F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">jejunum melt</span><span class="informations">727×405 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>So then I do it as separate segments. Works better but I get “seams” between segments.\</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55855faba5f43ed6c71f62a4467cbb0d2fbcc751.jpeg" data-download-href="/uploads/short-url/ccykSQPkD8nIFbxYzBfUCCNmfwR.jpeg?dl=1" title="jejunum borders" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55855faba5f43ed6c71f62a4467cbb0d2fbcc751.jpeg" alt="jejunum borders" data-base62-sha1="ccykSQPkD8nIFbxYzBfUCCNmfwR" width="690" height="372" data-dominant-color="8F8B8B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">jejunum borders</span><span class="informations">715×386 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I overlap the segments by a bit and it makes it better …but still there… not a deal breaker but curious if anyone has any ideas to make the jejunum look like one continuous tube</p>

---

## Post #2 by @lassoan (2020-12-17 22:32 UTC)

<p>You can smooth out these tiny seams using <a href="https://discourse.slicer.org/t/new-segment-editing-feature-smoothing-brush/14577">Smoothing brush</a> locally, without affecting any other parts of the segmentation.</p>

---

## Post #3 by @Hannnonk (2021-06-18 12:35 UTC)

<p>I can not make this work. When I try to smoothen the junction between two segments the brush only affects the selected segment?<br>
thanks<br>
KH</p>

---

## Post #4 by @lassoan (2021-06-18 13:08 UTC)

<p>Joint smoothing method is not available for the smoothing brush (when you attempt to do it you should see the <em>“Smoothing brush is not available for joint smoothing method”</em> message).</p>
<p>Instead, if you want to apply joint smoothing in a certain region only, you need to use masking settings:</p>
<ol>
<li>Specify the region that will be smoothed</li>
</ol>
<ul>
<li>Create a new segment, set its name to <code>Mask</code>
</li>
<li>Switch to Paint effect</li>
<li>Allow overlap between segments: in Masking settings (at the bottom) set <code>Modify other segments</code> → <code>Allow overlap</code>
</li>
<li>Paint the region you want to smooth (you can enable <code>Sphere brush</code> option to paint a larger region more quickly)</li>
</ul>
<ol start="2">
<li>Apply joint smoothing restricted to the region designated by the “Mask” segment</li>
</ol>
<ul>
<li>Switch to Smoothing effect</li>
<li>Hide the <code>Mask</code> segment (this will exclude it from the smoothing, as joint smoothing will be only applied to visible segments)</li>
<li>Restrict the effect to the designated region: set <code>Masking</code> / <code>Editable area</code> → <code>Inside Mask</code>
</li>
<li>Select <code>Smoothing method</code> → <code>Joint smoothing</code> and click <code>Apply</code>
</li>
</ul>

---
