---
topic_id: 12570
title: "Roi To Segmentation Or Model"
date: 2020-07-16
url: https://discourse.slicer.org/t/12570
---

# ROI to Segmentation or Model?

**Topic ID**: 12570
**Date**: 2020-07-16
**URL**: https://discourse.slicer.org/t/roi-to-segmentation-or-model/12570

---

## Post #1 by @manjula (2020-07-16 09:05 UTC)

<p>Hi,</p>
<p>Is there a way to convert a ROI box in to a segment or Model ?</p>
<p>I tried to create a vtkModel object with the centroid of the segment as the center but its orientation is not what i want.  I was simply thinking is there a way of simply converting the ROI box in to a sement or model ?</p>
<p>I guess the problem is with the principle axis direction. But I do not see a argument to set that in the vtkModel.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad0e50dcd179f20380cc75cdf8bc3170a90ef5ca.png" data-download-href="/uploads/short-url/oGVgZf1LVY8i8mxoypVXj45AvKW.png?dl=1" title="Screenshot from 2020-07-16 11-02-07" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad0e50dcd179f20380cc75cdf8bc3170a90ef5ca_2_690x388.png" alt="Screenshot from 2020-07-16 11-02-07" data-base62-sha1="oGVgZf1LVY8i8mxoypVXj45AvKW" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad0e50dcd179f20380cc75cdf8bc3170a90ef5ca_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad0e50dcd179f20380cc75cdf8bc3170a90ef5ca_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/ad0e50dcd179f20380cc75cdf8bc3170a90ef5ca_2_1380x776.png 2x" data-dominant-color="C5C8DD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-07-16 11-02-07</span><span class="informations">1920×1080 279 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-07-16 13:54 UTC)

<p>There are many options for implementing this. What would you like to achieve?</p>

---

## Post #3 by @manjula (2020-07-16 14:55 UTC)

<p>I want to make it work for two purposes.</p>
<ol>
<li>When we are working with Models/Segments only i want to align basic objects like cylinder or cube along the segment bounding box.</li>
</ol>
<p>Something like this, (i use the transform to get it in to somewhat align to show you what i want to do. )<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/1669e7bd31e045064b751e435cc5038903df5376.png" data-download-href="/uploads/short-url/3chp7OOLqSoPrVtq59ueByiRLSK.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/1669e7bd31e045064b751e435cc5038903df5376_2_690x292.png" alt="1" data-base62-sha1="3chp7OOLqSoPrVtq59ueByiRLSK" width="690" height="292" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/1669e7bd31e045064b751e435cc5038903df5376_2_690x292.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/1669e7bd31e045064b751e435cc5038903df5376_2_1035x438.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/6/1669e7bd31e045064b751e435cc5038903df5376_2_1380x584.png 2x" data-dominant-color="8885B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1524×646 280 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li>When we define a ROI of certain size in a volume (e.g CT) convert it directly to a segment. The way did was that use crop volume and use that to make a segment but it would be much convenient if there is a way i can directly use the ROI and convert it to a segment.</li>
</ol>
<p>For example scissor tool with rectangle or circle does not allow us to control the size of area we draw<br>
We can define the height (one length )via symmetric option but we cannot control the other two dimensions ( or Radius of the circle).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/243fb93b0b5eb8d7176092fc8c21e3017d854db3.png" data-download-href="/uploads/short-url/5aFIoptoG5Dk5CUVeVzNYR3nIvF.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/243fb93b0b5eb8d7176092fc8c21e3017d854db3_2_476x499.png" alt="2" data-base62-sha1="5aFIoptoG5Dk5CUVeVzNYR3nIvF" width="476" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/243fb93b0b5eb8d7176092fc8c21e3017d854db3_2_476x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/243fb93b0b5eb8d7176092fc8c21e3017d854db3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/243fb93b0b5eb8d7176092fc8c21e3017d854db3.png 2x" data-dominant-color="20201F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">580×608 188 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2020-07-16 15:17 UTC)

<aside class="quote no-group" data-username="manjula" data-post="3" data-topic="12570">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>When we are working with Models/Segments only i want to align basic objects like cylinder or cube along the segment bounding box.</p>
</blockquote>
</aside>
<p>For this, I would recommend to create a transform from the bounding box or principal component axes and apply that transform to models.</p>
<aside class="quote no-group" data-username="manjula" data-post="3" data-topic="12570">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/manjula/48/80981_2.png" class="avatar"> manjula:</div>
<blockquote>
<p>When we define a ROI of certain size in a volume (e.g CT) convert it directly to a segment. The way did was that use crop volume and use that to make a segment but it would be much convenient if there is a way i can directly use the ROI and convert it to a segment</p>
</blockquote>
</aside>
<p>You can define a box-shaped ROI using Scissors effect in two steps. First step is fill inside in one slice view. Second step is erase outside in an orthogonal view.</p>
<p>You can also define box ROIs using “Surface cut” effect by disabling “Smooth model” option and placing 8 points.</p>

---

## Post #5 by @manjula (2020-07-16 22:23 UTC)

<p>Dear Prof Lasso, Thank you for as always taking time to help.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="12570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>For this, I would recommend to create a transform from the bounding box or principal component axes and apply that transform to models.</p>
</blockquote>
</aside>
<p>What I tried to do before was apply the transformation of the ROI box to the model. It works well if it is a Square. But if it is cylinder or rectangle the long axis can be oriented in a plane that we do not want to. I am not sure if i am explaining my problem this correctly but please have a look at the photos.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7616a7d7557a4a969983947618b96708c6f4060.png" data-download-href="/uploads/short-url/qag5zq9oyk8iamrC24AVNwAjtao.png?dl=1" title="Screenshot from 2020-07-16 23-57-33" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7616a7d7557a4a969983947618b96708c6f4060_2_690x243.png" alt="Screenshot from 2020-07-16 23-57-33" data-base62-sha1="qag5zq9oyk8iamrC24AVNwAjtao" width="690" height="243" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7616a7d7557a4a969983947618b96708c6f4060_2_690x243.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7616a7d7557a4a969983947618b96708c6f4060_2_1035x364.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b7616a7d7557a4a969983947618b96708c6f4060_2_1380x486.png 2x" data-dominant-color="C7CAE3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-07-16 23-57-33</span><span class="informations">1905×672 83.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1481cf735a4b3d39904e1206626ac0daa66216d.png" data-download-href="/uploads/short-url/w8VVOKfvuO06J74mTqANs9Dxuln.png?dl=1" title="Screenshot from 2020-07-16 23-58-14" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1481cf735a4b3d39904e1206626ac0daa66216d_2_690x269.png" alt="Screenshot from 2020-07-16 23-58-14" data-base62-sha1="w8VVOKfvuO06J74mTqANs9Dxuln" width="690" height="269" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1481cf735a4b3d39904e1206626ac0daa66216d_2_690x269.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1481cf735a4b3d39904e1206626ac0daa66216d_2_1035x403.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1481cf735a4b3d39904e1206626ac0daa66216d_2_1380x538.png 2x" data-dominant-color="C9CADC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-07-16 23-58-14</span><span class="informations">1743×681 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As you can see in he last photo if it is a rectangle or a cylinder it can get oriented at 90 degrees to the long axis.</p>
<ol>
<li>I do not know how to apply the  principal component axes to these models. I think if i can do that it will solve the problem. But I hope my problem is clear for you.  Please let me know how to apply the principal component axes ?</li>
</ol>
<p>The way i use to rotate this is by placing a fiducial at the centroid of the model and then rotating the model around that specific point. If i try to apply the transform without this I believe by default in slicer objects simply get transformed around the world origin of the slicer.</p>
<ol start="2">
<li>Is there a simple way of setting the object origin to the center of the model ? so the objects are transformed much easily. For example in any 3D modelling software like Blender, we can simply select the object origin to world origin, object center by volume , weight etc… or to any arbitrary location. This can be achieved in 3D Slicer too by placing a fiducial and transforming around that but is there a simple way of achieving this ?</li>
</ol>
<p>If not It would be a great feature to add.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="12570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can define a box-shaped ROI using Scissors effect in two steps. First step is fill inside in one slice view. Second step is erase outside in an orthogonal view.</p>
</blockquote>
</aside>
<p>I am sorry I am at complete loss. Can you please direct me to a example as i do not understand this at all.</p>
<ol start="3">
<li>Most of the problem in my line of work need segmenting same ROI repeatedly.  Is it possible to make the Scissor draw a circle of prefixed radius ?</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/5920a61c9edcc2a1201de9f46b43cd2b15887a7a.png" alt="Screenshot from 2020-07-16 23-58-56" data-base62-sha1="cIsrzEQBDqqd8qxS3caDhYHW55g" width="352" height="500"></p>
<ol start="4">
<li>
<p>Or the make the scissor to draw a rectangle of fixed x and y length ? <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/daa57069a1b1a821668eaa2427d3a31f19716839.png" data-download-href="/uploads/short-url/vcexuBBGZWwvXSaksbTrI7Krtxv.png?dl=1" title="Screenshot from 2020-07-16 23-59-18" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/daa57069a1b1a821668eaa2427d3a31f19716839_2_690x293.png" alt="Screenshot from 2020-07-16 23-59-18" data-base62-sha1="vcexuBBGZWwvXSaksbTrI7Krtxv" width="690" height="293" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/daa57069a1b1a821668eaa2427d3a31f19716839_2_690x293.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/daa57069a1b1a821668eaa2427d3a31f19716839_2_1035x439.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/daa57069a1b1a821668eaa2427d3a31f19716839.png 2x" data-dominant-color="C3BEBE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-07-16 23-59-18</span><span class="informations">1244×529 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>If the scissor can made to limit the slice cut in positive and negative directions with the prefixed  length in mm like it does in symmetric almost all the ROI problems will be solved in my opinion. The way i do this is by masking the direction i do not want to segment and use the symmetric option but if the slice cut length can be defined for positive and negative cuts it would be great.</p>
</li>
</ol>

---

## Post #6 by @lassoan (2020-07-28 20:40 UTC)

<p>A post was split to a new topic: <a href="/t/interpolated-cropping-slicghtly-changes-voxel-values/12763">Interpolated cropping slicghtly changes voxel values</a></p>

---
