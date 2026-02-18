# Segment comparison returns 0 for all metrics

**Topic ID**: 7386
**Date**: 2019-07-02
**URL**: https://discourse.slicer.org/t/segment-comparison-returns-0-for-all-metrics/7386

---

## Post #1 by @saf (2019-07-02 19:10 UTC)

<p>hello<br>
why I always get 0 even if I use the same data?<br>
I mean even if both data have the same characteristics<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bea30fe6632b606de537c818b914842cfc184b04.png" data-download-href="/uploads/short-url/rcs4R9kKdJDOfsExNaSYX2TiIZK.png?dl=1" title="comp" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bea30fe6632b606de537c818b914842cfc184b04.png" alt="comp" data-base62-sha1="rcs4R9kKdJDOfsExNaSYX2TiIZK" width="542" height="500" data-dominant-color="F5F5F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">comp</span><span class="informations">577×532 8.57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-07-02 19:12 UTC)

<p>Could you share the data sets that you tested with? You can create a segmentation from one of the Slicer sample data sets if you would prefer not to share your own images/segmentations.</p>

---

## Post #3 by @cpinter (2019-07-02 20:35 UTC)

<aside class="quote no-group" data-username="saf" data-post="1" data-topic="7386">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/59ef9b/48.png" class="avatar"> saf:</div>
<blockquote>
<p>even if I use the same data</p>
</blockquote>
</aside>
<p>If you use the same data then the difference is 0, so there is no surprise there.</p>

---

## Post #4 by @saf (2019-07-02 20:48 UTC)

<p>I captured the datasets</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/478929747b44cbc6d5619ab2dd9e5b5d5c9e03f1.png" data-download-href="/uploads/short-url/acPLE4wSlrnwtSZId1lCEgf6VlT.png?dl=1" title="Capture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/478929747b44cbc6d5619ab2dd9e5b5d5c9e03f1_2_690x442.png" alt="Capture1" data-base62-sha1="acPLE4wSlrnwtSZId1lCEgf6VlT" width="690" height="442" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/478929747b44cbc6d5619ab2dd9e5b5d5c9e03f1_2_690x442.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/478929747b44cbc6d5619ab2dd9e5b5d5c9e03f1_2_1035x663.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/478929747b44cbc6d5619ab2dd9e5b5d5c9e03f1.png 2x" data-dominant-color="646470"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1</span><span class="informations">1230×788 18.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31c4b5d440478874c371d2c75758db83148a341f.png" data-download-href="/uploads/short-url/76gQruw0PZuQMX5qwSxZrvSatGf.png?dl=1" title="Capture2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31c4b5d440478874c371d2c75758db83148a341f_2_689x444.png" alt="Capture2" data-base62-sha1="76gQruw0PZuQMX5qwSxZrvSatGf" width="689" height="444" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31c4b5d440478874c371d2c75758db83148a341f_2_689x444.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/31c4b5d440478874c371d2c75758db83148a341f_2_1033x666.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31c4b5d440478874c371d2c75758db83148a341f.png 2x" data-dominant-color="62626D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture2</span><span class="informations">1209×779 16 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @saf (2019-07-03 09:09 UTC)

<p>no, normally, when I use the same data, the dice that will be calculated must be a high value ,<br>
normally I get a good result not 0<br>
but I didn’t always try the same datasets, i tried several different data and I always get 0</p>

---

## Post #6 by @cpinter (2019-07-03 13:16 UTC)

<p>Segment Comparison works for me in the recent versions.</p>
<p>Could you please share your data? The segmentation nrrd files are enough, but a Slicer scene (mrb) would be best. Thanks!</p>

---

## Post #7 by @saf (2019-07-03 14:35 UTC)

<p>the datasets that i have are in nifti type<br>
you can found the datasets here<br>
<a href="https://drive.google.com/open?id=1t_gn_UvqarHlV9bFQ8EmjsaLgZh1SPtp" class="onebox" target="_blank" rel="nofollow noopener">https://drive.google.com/open?id=1t_gn_UvqarHlV9bFQ8EmjsaLgZh1SPtp</a></p>

---

## Post #8 by @cpinter (2019-07-03 15:28 UTC)

<p>Thanks for the data!</p>
<p>For me Segment Comparison works on these segmenations. I loaded them as labelmap, then converted them to segmentation nodes, then used Segment Comparison as normal.</p>
<p>The obvious problem is that the two segmentations do not overlap, so Dice is 0 and Hausdorff distances are super high, but the algorithms work. Not sure what you did differently. Please try to do as I describe above.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a46a4f797db609589a79b75a10ac009d14a29f2.png" data-download-href="/uploads/short-url/3KrLGG23Pwp5UYTXrhdOxyccWQi.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a46a4f797db609589a79b75a10ac009d14a29f2_2_690x296.png" alt="image" data-base62-sha1="3KrLGG23Pwp5UYTXrhdOxyccWQi" width="690" height="296" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a46a4f797db609589a79b75a10ac009d14a29f2_2_690x296.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a46a4f797db609589a79b75a10ac009d14a29f2_2_1035x444.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a46a4f797db609589a79b75a10ac009d14a29f2.png 2x" data-dominant-color="79797A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1228×528 21.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @saf (2019-07-03 16:00 UTC)

<p>can you show me how to load them as labelmap and convert them to segmentation nodes. (by a capture if you want)<br>
because i tried to import them as labelmap but it doesn’t work<br>
i think i made something wrong .<br>
thak you</p>

---

## Post #10 by @cpinter (2019-07-03 18:53 UTC)

<p>This is the easiest:</p>
<ol>
<li>Drag&amp;drop<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ea3557ea99f43b5f4afc8bd049e8125e08f632b.png" data-download-href="/uploads/short-url/i4i6mHD6QZ07QLLtktAxKtnjmDF.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ea3557ea99f43b5f4afc8bd049e8125e08f632b.png" alt="image" data-base62-sha1="i4i6mHD6QZ07QLLtktAxKtnjmDF" width="690" height="87" data-dominant-color="F0EEF1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1122×143 12.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li>Data module<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f9cd7b687323e5ace972ccbb594e86e8eaa5c21.png" alt="image" data-base62-sha1="mLZWZT7QXH9umv6VHt9iMyuoHeN" width="552" height="261"></li>
</ol>

---

## Post #11 by @saf (2019-07-05 11:27 UTC)

<p>thank you  I loaded them as labelmap, but i can’t fount the window of convertion to segmentation nodes.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/3651ee9d6b4c61a03795f18861be873de5309783.png" data-download-href="/uploads/short-url/7KxjY8BPu8diQNCB3bcx39z9QzN.png?dl=1" title="node" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/3651ee9d6b4c61a03795f18861be873de5309783_2_690x365.png" alt="node" data-base62-sha1="7KxjY8BPu8diQNCB3bcx39z9QzN" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/6/3651ee9d6b4c61a03795f18861be873de5309783_2_690x365.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/3651ee9d6b4c61a03795f18861be873de5309783.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/3651ee9d6b4c61a03795f18861be873de5309783.png 2x" data-dominant-color="E1ECF2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">node</span><span class="informations">788×417 45.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @lassoan (2019-07-05 12:21 UTC)

<p>As <span class="mention">@cpinterwrote</span> above, it is in the Data module. Make sure you use at least the latest stable version of Slicer (currently 4.10.2).</p>

---

## Post #14 by @saf (2019-07-05 15:27 UTC)

<p>thank you it works but in Slicer 4.10.1, because in Slicer 4.10.2  i didn’t find the segment comparison module</p>

---

## Post #15 by @lassoan (2019-07-05 16:42 UTC)

<p>Segment Comparison module is provided by SlicerRT extension. You’ll have the module in Slicer-4.10.2, too, if you install SlicerRT.</p>

---

## Post #16 by @saf (2019-07-05 17:11 UTC)

<p>thank you it works<br>
I wish I could find more function than dice and dose, such as (recall, precision, accuracy,…)</p>

---

## Post #17 by @lassoan (2019-07-05 18:06 UTC)

<p>Dice, recall, precision, accuracy could be all very easily added but they are basically all useless metrics, as they are highly dependent on the shape of the segment, may be sensitive to irrelevant errors and sensitive to all kinds of clinically important errors. For example, 90% does not mean anything: a practically perfect segmentation and an extremely low quality segmentation can both get this same score. For thin shapes that I can see in your screenshots, these overlap percentage based give completely meaningless results. These metrics are probably only used because they are trivial to compute and often researchers do not want to spend a lot of time with evaluation - if they get 1-2% better values than those reported in the literature then they consider their work done, publish their paper, and move on.</p>
<p>Hausdorff metric variants have absolute, clinically relevant meaning - I would highly recommend to use them. Identifying anatomical landmark points and surfaces manually and measure distance between them manually gives useful information, too. You also need to spend time with carefully visual assessment of the results to see where errors occur and see if they are clinically important or not.</p>

---
