---
topic_id: 1079
title: "How Can I Trasform A Model In This Way"
date: 2017-09-18
url: https://discourse.slicer.org/t/1079
---

# How can I trasform a model in this way?

**Topic ID**: 1079
**Date**: 2017-09-18
**URL**: https://discourse.slicer.org/t/how-can-i-trasform-a-model-in-this-way/1079

---

## Post #1 by @Ramttoong (2017-09-18 14:10 UTC)

<p>I used the ‘representation’ tap in the ‘Model’ module (surface → wireframe).<br>
But, its pattern is not clear (messy).<br>
How can I trasform a model in this way? (added a picture)<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f6591f82e2cd4b3086d5954c71242118138dc5b.png" data-download-href="/uploads/short-url/mK5wUV4DJX7KHpxg2aFvmWktUyD.png?dl=1" title="untitiled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f6591f82e2cd4b3086d5954c71242118138dc5b_2_690x383.png" alt="untitiled" data-base62-sha1="mK5wUV4DJX7KHpxg2aFvmWktUyD" width="690" height="383" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f6591f82e2cd4b3086d5954c71242118138dc5b_2_690x383.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f6591f82e2cd4b3086d5954c71242118138dc5b.png 2x" data-dominant-color="7B75B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">untitiled</span><span class="informations">1215×676 610 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2017-09-18 14:53 UTC)

<aside class="quote no-group" data-username="Ramttoong" data-post="1" data-topic="1079">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/edb3f5/48.png" class="avatar"> Ramttoong:</div>
<blockquote>
<p>But, its pattern is not clear (messy).</p>
</blockquote>
</aside>
<p>What do you mean? The mesh in the picture above looks nice.</p>
<aside class="quote no-group" data-username="Ramttoong" data-post="1" data-topic="1079">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/edb3f5/48.png" class="avatar"> Ramttoong:</div>
<blockquote>
<p>How can I trasform a model in this way?</p>
</blockquote>
</aside>
<p>What do you mean? In what way?</p>

---

## Post #3 by @Ramttoong (2017-09-20 00:31 UTC)

<p>Add a picture. (It’s not my work, just example made by another man.)</p>
<p>I adjusted the transparency by ‘opacity’, but it was not like that above.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f6591f82e2cd4b3086d5954c71242118138dc5b.png" data-download-href="/uploads/short-url/mK5wUV4DJX7KHpxg2aFvmWktUyD.png?dl=1" title="untitiled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f6591f82e2cd4b3086d5954c71242118138dc5b_2_690x383.png" alt="untitiled" data-base62-sha1="mK5wUV4DJX7KHpxg2aFvmWktUyD" width="690" height="383" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f6591f82e2cd4b3086d5954c71242118138dc5b_2_690x383.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/f/9f6591f82e2cd4b3086d5954c71242118138dc5b_2_1035x574.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f6591f82e2cd4b3086d5954c71242118138dc5b.png 2x" data-dominant-color="7B75B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">untitiled</span><span class="informations">1215×676 610 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2017-09-20 00:34 UTC)

<p>In Models module, Display / Representation section, change Representation from <code>Surface</code> (default) to <code>Wireframe</code>.</p>

---

## Post #5 by @brhoom (2018-10-17 11:15 UTC)

<p>Here is the python script</p>
<pre><code> n= getNode('muModel')
 d=n.GetDisplayNode()
 d.SetRepresentation(slicer.vtkMRMLDisplayNode.WireframeRepresentation)</code></pre>

---
