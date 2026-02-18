# How to project model node to different slice view according to their projection geometry

**Topic ID**: 31218
**Date**: 2023-08-18
**URL**: https://discourse.slicer.org/t/how-to-project-model-node-to-different-slice-view-according-to-their-projection-geometry/31218

---

## Post #1 by @nnzzll (2023-08-18 08:34 UTC)

<p>I want to get the Projection Slice Intersection of a model node to two slice view.</p>
<p>I have calculated the projection matrix of the 2 images. The projection matrix projects 3D(RAS) coordinate to 2D(image) coordinate.</p>
<p>Is it possible to setup the slice view (or slice node) properties  to get the right projection? If not, how can I do that?</p>

---

## Post #2 by @lassoan (2023-08-18 12:11 UTC)

<p>You can enable projection of a model node into a slice view in Models module → Display → Slice display → Mode: Projection.</p>
<p>If you want to set this mode programmatically, then you can do that by modifying the display node of the model node:</p>
<pre><code class="lang-python">modelNode.GetDisplayNode().SetVisibility2D(True)
modelNode.GetDisplayNode().SetSliceDisplayModeToProjection()
</code></pre>

---

## Post #3 by @nnzzll (2023-08-21 01:44 UTC)

<p><code>modelNode.GetDisplayNode().SetSliceDisplayModeToProjection()</code> This line projects the model node to Axial, Coronal and Sagittal plane, however, the image planes are not parallel to these three planes.</p>
<p>The projection geometry is calculated using DLT algorithm and represented by projection matrix. I want to project the model node using the projection matrix, is it possible?</p>

---

## Post #4 by @lassoan (2023-08-21 06:51 UTC)

<p>You can set slice view planes to any position and orientation, so you can use it for any parallel projection.</p>
<p>If you want to do perspective projection then you can set the transform and the model’s polydata as as inputs in vtkTransformPolyDataFilter and set the result in a new model node for visualization.</p>
<p>If you do stent visualization for augmented/simulated fluroscopy then you may also consider using a 3D view for rendering, as it can render both the DRR and devices in 3D in real-time.</p>

---

## Post #5 by @nnzzll (2023-08-21 11:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="31218">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can set slice view planes to any position and orientation</p>
</blockquote>
</aside>
<p>I noticed that there is a method <code>SetSliceToRASByNTP</code> to set the position and orientation. However, my image is a 2D image, when the position is not the center of the image or orientation is not perpendicular to the Z-axis(IS axis), part of the image is not visible, just like the screenshots below:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09f160147779095061faf8f9f5837b9273b51bd2.png" data-download-href="/uploads/short-url/1pXrmXebAAV374QwqbjoJgwmb4u.png?dl=1" title="Screenshot from 2023-08-21 19-47-17" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09f160147779095061faf8f9f5837b9273b51bd2_2_690x368.png" alt="Screenshot from 2023-08-21 19-47-17" data-base62-sha1="1pXrmXebAAV374QwqbjoJgwmb4u" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09f160147779095061faf8f9f5837b9273b51bd2_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09f160147779095061faf8f9f5837b9273b51bd2_2_1035x552.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/9/09f160147779095061faf8f9f5837b9273b51bd2_2_1380x736.png 2x" data-dominant-color="858697"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-08-21 19-47-17</span><span class="informations">1852×990 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/96c465f4d248cd0c7f1d8a021afc28bbd9a4a738.png" data-download-href="/uploads/short-url/lvKoUXgPwDWuiQsb1834QpNJbqU.png?dl=1" title="Screenshot from 2023-08-21 19-47-46" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96c465f4d248cd0c7f1d8a021afc28bbd9a4a738_2_690x367.png" alt="Screenshot from 2023-08-21 19-47-46" data-base62-sha1="lvKoUXgPwDWuiQsb1834QpNJbqU" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96c465f4d248cd0c7f1d8a021afc28bbd9a4a738_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96c465f4d248cd0c7f1d8a021afc28bbd9a4a738_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/96c465f4d248cd0c7f1d8a021afc28bbd9a4a738_2_1380x734.png 2x" data-dominant-color="8A8B9E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-08-21 19-47-46</span><span class="informations">1853×988 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="31218">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you do stent visualization for augmented/simulated fluroscopy then you may also consider using a 3D view for rendering, as it can render both the DRR and devices in 3D in real-time.</p>
</blockquote>
</aside>
<p>My goal is to do the similar thing but instead of DRR, I’m using a real X-Ray image, so rendering it in 3D view has the similar problem as I mentioned above. How can I solve that?</p>

---
