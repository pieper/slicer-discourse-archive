# Request for feature: polygon based segmentation effect

**Topic ID**: 1389
**Date**: 2017-11-06
**URL**: https://discourse.slicer.org/t/request-for-feature-polygon-based-segmentation-effect/1389

---

## Post #1 by @dcantor (2017-11-06 19:14 UTC)

<p>I am showing slicer to a radiologist and he tells me that other software tools have a polygon based segmentation tool, he mentioned Osirix, I thought of ITK-Snap. Is it possible to develop this tool? it doesn’t seem technically complicated and it is kind of expected by radiologists. Thanks.</p>

---

## Post #2 by @lassoan (2017-11-06 19:22 UTC)

<p>Polygon (in fact, 3D surface) based editing is available if you install SegmentEditorExtraEffects extension. The effect name is “Surface cut”. In general, “Grow from seeds” semi-automatic segmentation almost always works better than polygon-based manual segmentation, so we haven’t spent too much time advertising or improving the latter method.</p>
<p>With “Grow from seeds” effect, you just need to paint a few strokes inside each structures that you need to segment and you get usable segmentation in a few ten seconds.</p>

---

## Post #3 by @dcantor (2017-11-06 22:13 UTC)

<p>Hi Andras,</p>
<p>Thank you for your answer. I will check that extension. There are cases where polygons are in fact more efficient than region growing methods. For instance to segment a highly heterogeneous structure. I am glad to hear this is also included as an extension in Slicer.</p>
<p>Best regards,</p>
<p>Diego</p>

---

## Post #4 by @lassoan (2017-11-06 23:29 UTC)

<p>When there is no visible intensity difference at segment boundary then we recommend slice interpolation:</p>
<ul>
<li>use paint/draw effect on parallel slices - you can skip as many slices in between as you want (if the contour is not changing too quickly between slices then it may be enough to draw on every 5th or 10th slice)</li>
<li>create full segmentation using “Fill between slices” effect.</li>
</ul>
<p>In general, Slicer’s Segment Editor module is quite new, so it may not be as polished as ITK-snap, OsiriX, or Mimics; but it has several unique features and several very powerful effects that probably puts it ahead of all similar software. If you don’t find any feature in Slicer that are available in other software, then let us know and we can help finding it or implement in Slicer as well.</p>

---

## Post #5 by @dcantor (2017-11-07 17:24 UTC)

<p>Hi Andras, I have used fill between slices and I really like it.</p>
<p>Now, I am trying surface cut to but it is extremely slow (and I am not sure I am doing it right, is there a tutorial?):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/227d34895bd1bbef3ad070f4954ca158e6df79e0.jpeg" data-download-href="/uploads/short-url/4V6u47IEvpdLynuUtrIlLCCkk5q.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/227d34895bd1bbef3ad070f4954ca158e6df79e0_2_690x359.jpg" alt="image" data-base62-sha1="4V6u47IEvpdLynuUtrIlLCCkk5q" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/227d34895bd1bbef3ad070f4954ca158e6df79e0_2_690x359.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/227d34895bd1bbef3ad070f4954ca158e6df79e0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/227d34895bd1bbef3ad070f4954ca158e6df79e0.jpeg 2x" data-dominant-color="A6A5A4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">988×515 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I think something as simple as polygon-based segmentation would be a powerful tool to have, in the sense that other tools have it already and it is kind of expected by radiologists.</p>
<p>This would be A tool where you set the control points  and it creates an enclosed region by those points. I don’t think this is technically complicated</p>
<p>Also, this tool be parametric so the boundary is formed by straight lines or a bezier closed curve controlled by such points.</p>
<p>Diego</p>

---

## Post #6 by @lassoan (2017-11-07 18:53 UTC)

<aside class="quote no-group" data-username="dcantor" data-post="5" data-topic="1389">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dcantor/48/782_2.png" class="avatar"> dcantor:</div>
<blockquote>
<p>Now, I am trying surface cut to but it is extremely slow (and I am not sure I am doing it right, is there a tutorial?):</p>
</blockquote>
</aside>
<p>It should be very fast. See a video how to use it here: <a href="https://youtu.be/xZwyW6SaoM4?t=1m15s">https://youtu.be/xZwyW6SaoM4?t=1m15s</a><br>
It would be useful to know why it was slow for you.</p>
<aside class="quote no-group" data-username="dcantor" data-post="5" data-topic="1389">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dcantor/48/782_2.png" class="avatar"> dcantor:</div>
<blockquote>
<p>I think something as simple as polygon-based segmentation would be a powerful tool to have, in the sense that other tools have it already and it is kind of expected by radiologists.</p>
</blockquote>
</aside>
<p>Draw tool allows you to draw polygons (you can place points instead of holding down left mouse button), and delete the last point (by hitting <code>x</code> key), but it’s certainly not as sophisticated as it could be. I’ve added a ticket to track this feature request: <a href="https://issues.slicer.org/view.php?id=4473" class="inline-onebox">Add spline drawing option to Draw effect in Segment editor · Issue #4473 · Slicer/Slicer · GitHub</a></p>

---

## Post #7 by @lassoan (2023-03-21 02:51 UTC)



---
