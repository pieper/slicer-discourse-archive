# Issues with "fill between slices

**Topic ID**: 3186
**Date**: 2018-06-14
**URL**: https://discourse.slicer.org/t/issues-with-fill-between-slices/3186

---

## Post #1 by @goetzf (2018-06-14 20:19 UTC)

<p>Slicer version 4.9.0-2018-05-30</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Model Name:</th>
<th>iMac</th>
</tr>
</thead>
<tbody>
<tr>
<td>Model Identifier:</td>
<td>iMac18,3</td>
</tr>
<tr>
<td>Processor Name:</td>
<td>Intel Core i7</td>
</tr>
<tr>
<td>Processor Speed:</td>
<td>4.2 GHz</td>
</tr>
<tr>
<td>Number of Processors:</td>
<td>1</td>
</tr>
<tr>
<td>Total Number of Cores:</td>
<td>4</td>
</tr>
<tr>
<td>L2 Cache (per Core):</td>
<td>256 KB</td>
</tr>
<tr>
<td>L3 Cache:</td>
<td>8 MB</td>
</tr>
<tr>
<td>Memory:</td>
<td>64 GB</td>
</tr>
</tbody>
</table>
</div><p>I have been segmenting every 2nd, 4th or 6th section and then filling between slices. I get some weird results like in the attached image:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62d0107859c00d6789a9b9f6c897dd49a0491f20.jpeg" data-download-href="/uploads/short-url/e68zcXOz9swtWV0wiGCNnO7saic.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62d0107859c00d6789a9b9f6c897dd49a0491f20_2_515x500.jpg" alt="image" data-base62-sha1="e68zcXOz9swtWV0wiGCNnO7saic" width="515" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/62d0107859c00d6789a9b9f6c897dd49a0491f20_2_515x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62d0107859c00d6789a9b9f6c897dd49a0491f20.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62d0107859c00d6789a9b9f6c897dd49a0491f20.jpeg 2x" data-dominant-color="808E8C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">693×672 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The adjacent image looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/739ca067e2e5135b8f771523d21679e8bb0eb646.jpeg" data-download-href="/uploads/short-url/guKtLatH9WAWt1gpPnfPTOqJ4x0.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/739ca067e2e5135b8f771523d21679e8bb0eb646_2_544x500.jpg" alt="image" data-base62-sha1="guKtLatH9WAWt1gpPnfPTOqJ4x0" width="544" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/739ca067e2e5135b8f771523d21679e8bb0eb646_2_544x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/739ca067e2e5135b8f771523d21679e8bb0eb646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/739ca067e2e5135b8f771523d21679e8bb0eb646.jpeg 2x" data-dominant-color="61A399"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">770×707 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Why would it interpolate that as a square?<br>
Also, why can’t I edit the layer to refine the interpolation?</p>
<p>Thank you for any help on this subject.</p>
<p>Freya</p>

---

## Post #2 by @lassoan (2018-06-14 20:45 UTC)

<aside class="quote no-group" data-username="goetzf" data-post="1" data-topic="3186">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/b38774/48.png" class="avatar"> goetzf:</div>
<blockquote>
<p>I get some weird results like in the attached image</p>
</blockquote>
</aside>
<p>Fill between slices effect requires that slice views are aligned with segmentation axes. Download Slicer nightly build tomorrow or later. That version shows a warning button if there is a misalignment and clicking it will align your slice viewers to the volume.</p>
<aside class="quote no-group" data-username="goetzf" data-post="1" data-topic="3186">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/b38774/48.png" class="avatar"> goetzf:</div>
<blockquote>
<p>Also, why can’t I edit the layer to refine the interpolation?</p>
</blockquote>
</aside>
<p>You can edit the interpolation while the Fill between segments is active - then you have to provide a complete segmentation in that slice. After you applied Fill between segments, then you should be able to make any small adjustments. If it does not work then maybe it is caused by the same misalignment as described above and the same fix applies.</p>

---
