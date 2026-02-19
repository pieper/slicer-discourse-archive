---
topic_id: 31177
title: "Mrb Optimization File Size And Loading Time"
date: 2023-08-16
url: https://discourse.slicer.org/t/31177
---

# .mrb optimization (file size and loading time)

**Topic ID**: 31177
**Date**: 2023-08-16
**URL**: https://discourse.slicer.org/t/mrb-optimization-file-size-and-loading-time/31177

---

## Post #1 by @Deep_Learning (2023-08-16 16:38 UTC)

<p>I have been using a merged segmentation/volume sequence and saving it as .mrb.<br>
Works great… drag and drop…<br>
Basiclly 20 volumes and segmentations:  512x512x320x20.</p>
<p>Any tips on optimization for file size (now 3.1 Gb) and loading time (3 min).</p>
<p>Cropping will work.  Files seem well compressed.<br>
I’m not sure what precision the masks and volumes are being stored with…</p>
<p>Any tips would be greatly appreciated.</p>

---

## Post #2 by @pieper (2023-08-16 17:14 UTC)

<p>If you save as mrml instead of mrb and you can uncheck the compress option for saving volumes.  It will take more disk space but the load/save times should be much faster.  It’s not much harder to manage a directory of the files with the mrml file than it is to manage the mrb.</p>

---

## Post #3 by @muratmaga (2023-08-16 17:16 UTC)

<aside class="quote no-group" data-username="Deep_Learning" data-post="1" data-topic="31177">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deep_learning/48/15345_2.png" class="avatar"> Deep_Learning:</div>
<blockquote>
<p>Any tips on optimization for file size (now 3.1 Gb) and loading time (3 min).</p>
</blockquote>
</aside>
<p>Is there anyway to use lpzip instead of regular zip to package mrb? Parallelization will be great.<br>
<a href="https://www.nongnu.org/lzip/plzip.html">Plzip - A massively parallel lossless data compressor (nongnu.org)</a></p>
<p>But i just saw it is gpl.</p>

---

## Post #4 by @pieper (2023-08-16 17:24 UTC)

<p>Last time I looked there wasn’t a good parallel compression option, code was either GPL, like Plzip, or not cross platform.</p>
<p>If saving uncompressed doesn’t help enough and you are willing to do some python coding then doing something like saving and loading the volume sequences as zarr might be worth the (probably small) effort.  Here’s an example down that path: <a href="https://gist.github.com/pieper/0e7edcf70c844925ea104e07aedbe92a" class="inline-onebox">Display NGFF volume data in 3D Slicer · GitHub</a></p>

---
