# How to make the edge of the segment smoother?

**Topic ID**: 2723
**Date**: 2018-04-27
**URL**: https://discourse.slicer.org/t/how-to-make-the-edge-of-the-segment-smoother/2723

---

## Post #1 by @trnhx001 (2018-04-27 19:41 UTC)

<p>Hi,</p>
<p>I am a new intern, and my boss requires me to make the edge/border of a segment looks smooth. I am trying to have segment of Aorta. He calls it something like contour/mesh. Right now, the border looks very rough (like connected squares/pixels),</p>
<p>I tried to use Smoothing in Segment Editor, but it only makes the 3D model look smooth. On other three views, the border of the segment looks very rough. Since it is like pixels, the border will leak out or will not reach actually border seen on the CT images.</p>
<p>Moreover, he also wants me to search for any tools to create contour/mesh which is like the mask/segmentation, but you can drags the border around to fit the CT images. It is like polygon, where you can just modify the edge to have the shape you like.</p>
<p>I really appreciate if someone can help me with this.</p>

---

## Post #2 by @lassoan (2018-04-27 20:04 UTC)

<p>To get started, I would recommend to complete all <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">Segmentation tutorials</a>.</p>
<p>To give some more specific answers:</p>
<aside class="quote no-group" data-username="trnhx001" data-post="1" data-topic="2723">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/ed655f/48.png" class="avatar"> trnhx001:</div>
<blockquote>
<p>I tried to use Smoothing in Segment Editor, but it only makes the 3D model look smooth.</p>
</blockquote>
</aside>
<p>You can use Crop volume to crop and resample your input volume to have smaller voxels and so less blocky contours in slice views. You can also choose to display contours in slice views from the 3D closed surface representation of the segmentation (Segmentations module / Display / Advanced / Representation in 2D views: Closed surface).</p>
<aside class="quote no-group" data-username="trnhx001" data-post="1" data-topic="2723">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/ed655f/48.png" class="avatar"> trnhx001:</div>
<blockquote>
<p>Moreover, he also wants me to search for any tools to create contour/mesh which is like the mask/segmentation,</p>
</blockquote>
</aside>
<p>Probably you mean something like Surface cut effect. You need to install SegmentEditorExtraEffects extension to make this effect available in the Segment editor.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="xZwyW6SaoM4" data-video-title="New &quot;Surface cut&quot; and &quot;Mask volume&quot; tools for 3D Slicer segment editor" data-video-start-time="1m25s" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=xZwyW6SaoM4&amp;t=1m25s" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/xZwyW6SaoM4/maxresdefault.jpg" title="New &quot;Surface cut&quot; and &quot;Mask volume&quot; tools for 3D Slicer segment editor" width="" height="">
  </a>
</div>


---

## Post #3 by @trnhx001 (2018-04-30 15:21 UTC)

<p>Hi,</p>
<p>Thank you for your response. I just followed your instructions and installed SegmentEditorExtraEffects extension. However, I do not see option to create masked volume after the surface cut. I wonder if I need the nightly version to have the function. I am using version 4.8.1 right now.</p>

---

## Post #4 by @lassoan (2018-04-30 18:16 UTC)

<p>Mask volume is a separate effect. Create the mask using Surface cut or other effects and then apply it as a mask on a volume using Mask volume effect.</p>

---

## Post #5 by @trnhx001 (2018-04-30 20:18 UTC)

<p>Good afternoon,</p>
<p>I did that successfully. Thank you.</p>
<p>I also set the Representation in 2D views to closed surface. However, whenever I go back to Segmentation Editor, the edge will be blocky again. I also try to resample my input volume, but it seems not help much with the pixelated edge of the segmentation. I wanted to increase the resolution more, but my computer crashes everytime.</p>
<p>Will there be any other methods that can permanently make the edge smooth?</p>

---

## Post #6 by @lassoan (2018-05-01 04:27 UTC)

<aside class="quote no-group" data-username="trnhx001" data-post="5" data-topic="2723">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/ed655f/48.png" class="avatar"> trnhx001:</div>
<blockquote>
<p>I wanted to increase the resolution more, but my computer crashes everytime.</p>
</blockquote>
</aside>
<p>The application crashes because you run out of memory. For finer resolution volume, you may need to increase available memory space. You can either add more physical memory or increase virtual memory size by a few 10 gigabytes. You can also decrease memory need by cropping the volume to the minimum necessary size.</p>
<aside class="quote no-group" data-username="trnhx001" data-post="5" data-topic="2723">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/ed655f/48.png" class="avatar"> trnhx001:</div>
<blockquote>
<p>However, whenever I go back to Segmentation Editor, the edge will be blocky again.</p>
</blockquote>
</aside>
<p>Why is this a problem? What is the clinical need?<br>
If you prefer to see smoother contours in slice views then choose to show closed surface representation in 2D views, as I described above  (Segmentations module / Display / Advanced / Representation in 2D views: Closed surface).</p>

---

## Post #7 by @trnhx001 (2018-05-02 15:36 UTC)

<p>Good morning,</p>
<p>I also tried to increase physical memory, but it seems like it does not help. I may help to give up on this.</p>
<p>I also do not see why this is a problem, but my boss insists to have smooth edge all the time.</p>
<p>Anyway, thank you so much for your help.</p>

---

## Post #8 by @lassoan (2018-05-02 22:25 UTC)

<p>If you prefer to see smooth contours in slice views then choose to show closed surface representation in 2D views, as I described above (Segmentations module / Display / Advanced / Representation in 2D views: Closed surface). You need to have closed surface representation created for this to work. If contours are not smooth then please attach a screenshot.</p>
<p>What is the clinical application: organ, disease, imaging modality, treatment procedure?</p>

---

## Post #9 by @trnhx001 (2018-05-11 16:32 UTC)

<p>Hi Andras,</p>
<p>I think it is for appearance mainly. He wants the segmentation to look smooth in every applications.</p>

---

## Post #10 by @lassoan (2018-05-11 18:29 UTC)

<p>OK. The techniques that I described above should provide smooth segmentation. If you have any specific issue then please post at least a screenshot with exact description of what you would like to improve.</p>

---

## Post #11 by @trnhx001 (2018-05-21 11:13 UTC)

<p>Thank you so much for your help.</p>
<p>I think my supervisor has no issues with your suggested method anymore.</p>
<p>All the best</p>

---
