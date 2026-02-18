# Model alignment 

**Topic ID**: 14527
**Date**: 2020-11-10
**URL**: https://discourse.slicer.org/t/model-alignment/14527

---

## Post #1 by @had_al-a (2020-11-10 19:45 UTC)

<p>I’m an orthodontic postgraduate student. I’m trying to superimpose “align” 2 models and do some 3d measurements. Every time I use the CMF, I chose the points for alignment and then change their radius for ROI and choose other points for the 3d measurement using Q3DC, the 2 models don’t get aligned at all or not well. I don’t know why? Can someone help, my defense is in less than a month and I need the results as soon as possible.</p>

---

## Post #2 by @manjula (2020-11-10 20:02 UTC)

<p>I think you can do that with good accuracy with the 3D Slicer.</p>
<p>Have a look at SlicerCMF tutorial here.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="hsZrjNsXZbs" data-video-title="3K Surface Registration" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=hsZrjNsXZbs" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/hsZrjNsXZbs/maxresdefault.jpg" title="3K Surface Registration" width="" height="">
  </a>
</div>

<p>If it does not work you can do get it to work with the SlicerIGT fiducial registration</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="8364" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"><a href="https://discourse.slicer.org/t/stl-models-alignment-and-volume-measurement/8364/5">STL models - Alignment and Volume measurement</a></div>
<blockquote>
<p>If you can accurately identify landmark points then you may use Fiducial registration wizard module (in SlicerIGT extension) to register based manually placed landmarks. See U-12 <a href="http://www.slicerigt.org/wp/user-tutorial/" rel="noopener nofollow ugc">SlicerIGT tutorial </a> for step-by-step instructions.</p>
</blockquote>
</aside>

---

## Post #3 by @had_al-a (2020-11-11 08:26 UTC)

<p>It actually worked. Thank you so much. Now, I need a “color map” and a “cross section” to check for the accuracy of the superimposition.</p>

---

## Post #4 by @manjula (2020-11-11 08:37 UTC)

<p>You need to calculate model to model distance and then visualize it in shape population view.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="FCCa2A77fV8" data-video-title="5 Quantification of Changes: Compute the Surface Distances" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=FCCa2A77fV8" target="_blank" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/FCCa2A77fV8/maxresdefault.jpg" title="5 Quantification of Changes: Compute the Surface Distances" width="" height="">
  </a>
</div>

<p>You can clip the model view with many tools easy clip dynamic modeler etc…</p>

---

## Post #5 by @had_al-a (2020-11-11 08:39 UTC)

<p>I already tried that. When I pressed apply in the model to model distance, it kept uploading and never stopped even after passing 100%!!!</p>

---

## Post #6 by @manjula (2020-11-11 11:22 UTC)

<p>well something must be wrong as you dont see a percentage in progress bar when it is calculating. You only see a time status as running with timer. percent completion comes only after it is finished. i think there is a problem with your workflow most probably rather than a bug.</p>

---
