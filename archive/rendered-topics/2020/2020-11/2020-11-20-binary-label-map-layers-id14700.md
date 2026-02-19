---
topic_id: 14700
title: "Binary Label Map Layers"
date: 2020-11-20
url: https://discourse.slicer.org/t/14700
---

# binary label map layers

**Topic ID**: 14700
**Date**: 2020-11-20
**URL**: https://discourse.slicer.org/t/binary-label-map-layers/14700

---

## Post #1 by @dzf (2020-11-20 04:40 UTC)

<p>Operating system: windows 10<br>
Slicer version: 4.11.20200930<br>
Expected behavior: keep every segment in different layer when saving after annotation<br>
Actual behavior:  all segments merged in one layer</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1dbc347c7ecd9c5ae4bcbe6f315c3016c93fe9d.jpeg" data-download-href="/uploads/short-url/rEWZt9jgNj6OzDPaEI6B0XoguJv.jpeg?dl=1" title="0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1dbc347c7ecd9c5ae4bcbe6f315c3016c93fe9d_2_690x372.jpeg" alt="0" data-base62-sha1="rEWZt9jgNj6OzDPaEI6B0XoguJv" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1dbc347c7ecd9c5ae4bcbe6f315c3016c93fe9d_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c1dbc347c7ecd9c5ae4bcbe6f315c3016c93fe9d_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1dbc347c7ecd9c5ae4bcbe6f315c3016c93fe9d.jpeg 2x" data-dominant-color="929A9E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">0</span><span class="informations">1035×558 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d34434de9a72bf9f49f9506f557587727ae380e7.jpeg" data-download-href="/uploads/short-url/u8WSrh6wYTJB8okI7Ntw5sY8INp.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d34434de9a72bf9f49f9506f557587727ae380e7_2_690x370.jpeg" alt="1" data-base62-sha1="u8WSrh6wYTJB8okI7Ntw5sY8INp" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d34434de9a72bf9f49f9506f557587727ae380e7_2_690x370.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d34434de9a72bf9f49f9506f557587727ae380e7_2_1035x555.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d34434de9a72bf9f49f9506f557587727ae380e7.jpeg 2x" data-dominant-color="A2AAAD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1035×556 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7789cae8112f43bdaaf34f3c170f1208ef114a1.jpeg" data-download-href="/uploads/short-url/zjelpkEgpYFMnYD9SwFaUvkWmbf.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f7789cae8112f43bdaaf34f3c170f1208ef114a1_2_690x376.jpeg" alt="2" data-base62-sha1="zjelpkEgpYFMnYD9SwFaUvkWmbf" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f7789cae8112f43bdaaf34f3c170f1208ef114a1_2_690x376.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f7789cae8112f43bdaaf34f3c170f1208ef114a1_2_1035x564.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7789cae8112f43bdaaf34f3c170f1208ef114a1.jpeg 2x" data-dominant-color="939CA0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1035×565 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @dzf (2020-11-20 04:40 UTC)

<p>Operating system: windows10<br>
Slicer version: 4.11.20200930<br>
Expected behavior: every segment in different layers after saving<br>
Actual behavior: all segments are automatically collapse 1 layer after saving.<br>
how can i solve it?</p>

---

## Post #3 by @lassoan (2020-11-20 04:49 UTC)

<p>A few years ago we did not collapse layers and it led to lots of complaints an inefficiencies. Therefore, I would recommend to keep using the collapsed format and use these code snippets to retrieve metadata and pixel data of segments: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_information_from_segmentation_nrrd_file_header">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_information_from_segmentation_nrrd_file_header</a></p>
<p>If this does not work for you then you can submit a feature request to <a href="http://issues.slicer.org">issues.slicer.org</a> asking for adding a flag to the storage node that can disable automatic collapsing on save.</p>

---

## Post #4 by @dzf (2020-11-25 11:33 UTC)

<p>thank you for your reply, i try your suggestion but can not solve my problem. if all segments are in one layer, and my question is when  the  segments in different layers, I can get the volume information of every segment by exporting the binary labelmap for every segment, and the volume information of each segement is correct, but now, all segments in one layer,  when i export the binary labelmap, the volume of each segment is same as each other, and the volume information actually is the volume of the combination of all segments, this is incorrect for me. how can i get the volume information of each segment correctly?</p>

---

## Post #5 by @lassoan (2020-11-25 14:18 UTC)

<aside class="quote no-group" data-username="dzf" data-post="4" data-topic="14700">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/ed655f/48.png" class="avatar"> dzf:</div>
<blockquote>
<p>how can i get the volume information of each segment correctly?</p>
</blockquote>
</aside>
<p>You can use <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html">Segment Statistics module</a> to get volume of each segment (and many other metrics, such as surface, bounding box, mean intensity, sphericity, principal axes, …).</p>
<p>If you prefer to compute these yourself then you can extract a single labelmap from a numpy array by indexing, for example you can get segment with label value 5 from <code>mylabelmap</code> numpy array like this <code>segment5 = mylabelmap[mylabelmap==5]</code>.</p>

---
