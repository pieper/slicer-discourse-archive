---
topic_id: 16067
title: "Segmenting Out Of Border Of Main Volume"
date: 2021-02-18
url: https://discourse.slicer.org/t/16067
---

# Segmenting out of border of main volume

**Topic ID**: 16067
**Date**: 2021-02-18
**URL**: https://discourse.slicer.org/t/segmenting-out-of-border-of-main-volume/16067

---

## Post #1 by @Aep93 (2021-02-18 20:54 UTC)

<p>Hello, I want to modify my segmentation by adding some details that are out of the borders of my main volume. However, it seems that the segment editor does not draw anything out of the borders of my master volume. Can anyone help me to solve this problem?<br>
Thanks in advance.</p>

---

## Post #2 by @lassoan (2021-02-18 21:33 UTC)

<p>See this documentation section for instructions: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries" class="inline-onebox">Segment editor — 3D Slicer documentation</a></p>

---

## Post #3 by @Aep93 (2021-02-19 01:04 UTC)

<p>Thank you very much <a class="mention" href="/u/lassoan">@lassoan</a> for your help. I used crop volume to extend the borders of my current volume by increasing the area in ROI. The final volume was successfully generated. The size of the main volume file was 400 Mb and the size of the new volume if 600Mb and it is acceptable I think. However, when I want to paint in the segment editor, I get the following error:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2dcbcf7b6c8d2517564af55283d2781368cdc669.png" alt="image" data-base62-sha1="6x89bjbZrRUPp2tQgHrnkjhrVSp" width="497" height="334"></p>
<p>It is really weird to me because I have about 100 GB of RAM and the fact that the size of both volumes are close to each other tells me there should not be drastic changes in calculation time. Can you please let me know your comments in this regard?<br>
Thanks in advance</p>

---

## Post #4 by @lassoan (2021-02-19 03:36 UTC)

<p>What was the size and scalar type of the volume that Crop volume module created? Could you copy-paste a screenshot of Volume’s module Volume Information section?</p>

---

## Post #5 by @Aep93 (2021-02-19 05:34 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. Here is the information of my new volume:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2ca6ce7454d53a8b493fb984a6a76d572ce6e15.png" alt="image" data-base62-sha1="u4JXICLXCeUuPlpgF7jGmYaUJ6d" width="678" height="323"></p>
<p>I found that 40Gb of my RAM is occupied when I just load the edited volume.<br>
Are there any possibilities to solve this problem?<br>
I do not want to reduce the quality and resolution of my current segmentation and it is an important factor for me.</p>

---

## Post #6 by @lassoan (2021-02-19 13:23 UTC)

<p>Size of this segmentation is 40GB. So, you will not get far with just 100GB RAM, because master volume will be resampled to match the same geometry (there goes another 40GB), while you are editing, previous states are saved to allow undo (which, depending on the size of the segments may take up to 40GB each). If you want to be sure that you don’t run out of memory when processing a data set, I would recommend to have at least 400GB memory space. Ideally, all physical RAM (for full-speed access), but if that is not feasible then you can just allocate more swap space. Also make sure you use latest Slicer Stable or Preview Release, as they contain memory usage optimizations for multiple segments (non-overlapping segments share a single labelmap).</p>
<p>However, to keep both speed memory usage under control, it is much better if you can reduce the size of the segmentation by increasing Spacing scale in Crop volume module. Spacing scale of 2 will decrease memory usage by a factor of 8.</p>

---

## Post #7 by @Aep93 (2021-02-19 17:52 UTC)

<p>Thank you very much for your response <a class="mention" href="/u/lassoan">@lassoan</a>.</p>

---

## Post #8 by @mau_igna_06 (2021-09-04 12:13 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="16067">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Also make sure you use latest Slicer Stable or Preview Release, as they contain memory usage optimizations for multiple segments (non-overlapping segments share a single labelmap).</p>
</blockquote>
</aside>
<p>I just had an idea. All segments could share a single labelmap. This can be done if each segment HU value is a prime number and overlapping segments HU value is the multiplication of the involved segments HU values. A lookup table would be updated when a new segment is created to know how to decode if there is overlap with other segments for visualization. So this would be computationally cheap.</p>
<p>The idea came up from <a href="https://en.wikipedia.org/wiki/G%C3%B6del_numbering" rel="noopener nofollow ugc">Gödel numbering</a>.</p>
<p>Do you think this is feasible <a class="mention" href="/u/lassoan">@lassoan</a>?</p>
<p>EDIT: here is an example</p>
<p>Suppose there are 3 segments each with a prime number HU value and that they overlap:<br>
segment1 → HU: 2<br>
segment2 → HU: 3<br>
segment3 → HU: 5</p>
<p>So the labelmap would save those HU values where there is no overlap. Where there is overlap it would be:<br>
segment1 AND segment2 → HU: 2x3 = 6<br>
segment1 AND segment3 → HU: 2x5 = 10<br>
segment2 AND segment3 → HU: 3x5 = 15<br>
segment1 AND segment2 AND segment3 → HU: 2x3x5 = 30</p>
<p>The prime factorization of the overlapping segments HU values can be saved on a lookupTable to know what are the segments that are overlapping for a given HU value.</p>

---

## Post #9 by @lassoan (2021-09-04 12:55 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="8" data-topic="16067">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>All segments could share a single labelmap.</p>
</blockquote>
</aside>
<p>This already works like this. Segments are organized into layers and within the layer we can store hundreds of non-overlapping segments. If a segment gets overlapping with others then it is moved into a new layer.</p>
<p>The prime factorization is a cool idea, but there would be some practical issues: performance could suffer and you would still need to keep a simple labelmap in memory so that you can process and visualize the data, because none of the existing algorithms could work with a volume encoded such way.</p>

---

## Post #10 by @mau_igna_06 (2021-09-04 13:53 UTC)

<blockquote>
<p>The prime factorization is a cool idea, but there would be some practical issues: performance could suffer and you would still need to keep a simple labelmap in memory so that you can process and visualize the data, because none of the existing algorithms could work with a volume encoded such way.</p>
</blockquote>
<p>I understand that algorithms should be adapted to work with this encoding.</p>
<p>But why performance could suffer? Searching for a factorization on a lookupTable is much faster than executing a factorization algorithm? Although I think this encoding may it not suitable for real-time usage of the data like visualization.</p>
<p>Would at least this encoding be useful for storage of the labelmap on the disk (saving up space)?</p>

---

## Post #11 by @lassoan (2021-09-04 18:22 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="10" data-topic="16067">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>But why performance could suffer? Searching for a factorization on a lookupTable is much faster than executing a factorization algorithm?</p>
</blockquote>
</aside>
<p>Accessing a segment in a labelmap stored in layers (the current implementation) is very fast because for each voxel you only need to perform a single integer comparison.</p>
<p>If you store voxels using prime factorization then for each voxel you need to do a table lookup to get the list of labels at that position and then a search for a label value in that list. I would guess that these would take at least a magnitude longer time than a single comparison operator.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="10" data-topic="16067">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>Would at least this encoding be useful for storage of the labelmap on the disk (saving up space)?</p>
</blockquote>
</aside>
<p>For storage efficient efficiency, we use zlib to reduce size of the 4D (3D+layers) labelmap. It uses Huffman coding, which may result in better compression than a basic factorization, and since zlib implementation is quite well optimized, it is probably faster than a custom compression.</p>
<p>But even if it turns out that you can achieve higher compression ratio on some data sets with some special compression method, it would be still unlikely to become popular, because saving a little disk space would rarely justify the extra complexity and compatibility issues. Optimized zlib is accessible on all platforms and languages, while a new algorithm would take a lot of efforts to develop, optimize, and make widely available. Even incredibly powerful companies have hard time introducing new compression schemes (see how Google struggles with making webp popular).</p>

---

## Post #12 by @mau_igna_06 (2021-09-04 19:19 UTC)

<p>Thank you Andras for such a great answer</p>

---
