# How to verify size of .ply model uploaded into Slicer?

**Topic ID**: 13133
**Date**: 2020-08-22
**URL**: https://discourse.slicer.org/t/how-to-verify-size-of-ply-model-uploaded-into-slicer/13133

---

## Post #1 by @flemingrachelc (2020-08-22 17:55 UTC)

<p>Hello!</p>
<p>I was wondering if there is a way to verify the size/scale of a .ply model uploaded directly into 3D Slicer from repositories such as Morphosource? I have the x res, y res, and z res from the specimen page, but am not sure how to use it if not working with a volume.</p>
<p>-Rachel</p>

---

## Post #2 by @pieper (2020-08-22 17:58 UTC)

<p>You can adjust the size by putting the loaded model into a transform.  You can create a linear transform and then type the scaling factors into the main diagonal.  Then if needed you can harden the model (applies the transform to the vertices and removes it from the transform) and save in the new size.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms</a></p>

---

## Post #3 by @flemingrachelc (2020-08-22 18:12 UTC)

<p>Thanks for your quick response, Steve! I’m not quite sure what to use as a scaling factor since I have nothing to use as a reference. For more context, I am looking at this ear bone from an extinct frog: <a href="https://www.morphosource.org/Detail/MediaDetail/Show/media_id/4803" rel="nofollow noopener">https://www.morphosource.org/Detail/MediaDetail/Show/media_id/4803</a><br>
…which is 7 mm across when measuring in 3D Slicer, but the ear bones of extant frogs are usually about  2 mm long. It could be correct, but if I could verify that somehow, that’d be great!<br>
-Rachel</p>

---

## Post #4 by @lassoan (2020-08-22 18:14 UTC)

<p>You can verify the size/scale by measuring a known distance on the model using markups Line tool on the toolbar:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/602e8f70ef453d0da46c0c2a255329f0145a06e6.png" data-download-href="/uploads/short-url/dIRAIlBh63Zk7M6N5Uyxa8uK31I.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/602e8f70ef453d0da46c0c2a255329f0145a06e6_2_443x499.png" alt="image" data-base62-sha1="dIRAIlBh63Zk7M6N5Uyxa8uK31I" width="443" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/602e8f70ef453d0da46c0c2a255329f0145a06e6_2_443x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/602e8f70ef453d0da46c0c2a255329f0145a06e6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/602e8f70ef453d0da46c0c2a255329f0145a06e6.png 2x" data-dominant-color="656971"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">521×588 29 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If the measured size does not match what you expect then use the ratio as scaling factor. For scaling, you can use “Surface Toolbox” module (a bit simpler to use than Transforms module, as it applies and hardens the transforms to a new model in one step).</p>

---

## Post #5 by @lassoan (2020-08-22 18:22 UTC)

<aside class="quote no-group" data-username="flemingrachelc" data-post="3" data-topic="13133">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/flemingrachelc/48/5704_2.png" class="avatar"> flemingrachelc:</div>
<blockquote>
<p>I am looking at this ear bone from an extinct frog: <a href="https://www.morphosource.org/Detail/MediaDetail/Show/media_id/4803">https://www.morphosource.org/Detail/MediaDetail/Show/media_id/4803 </a><br>
…which is 7 mm across when measuring in 3D Slicer, but the ear bones of extant frogs are usually about 2 mm long.</p>
</blockquote>
</aside>
<p>I had a look and the ply model is in mm, so it is loaded into Slicer with correct size.</p>
<p>The <code>FMNH_PR_2512_COLUMELLA.tif</code> image file is loaded with 1mm spacing by default and you need to set the correct values in Volumes module / Volume information / Image spacing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/978aac23714931fb8d24640e9cf9d6e0c16a8f2d.jpeg" data-download-href="/uploads/short-url/lCBcxI9oei02wWflJsR1wCUUGJv.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/978aac23714931fb8d24640e9cf9d6e0c16a8f2d_2_690x441.jpeg" alt="image" data-base62-sha1="lCBcxI9oei02wWflJsR1wCUUGJv" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/978aac23714931fb8d24640e9cf9d6e0c16a8f2d_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/978aac23714931fb8d24640e9cf9d6e0c16a8f2d_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/978aac23714931fb8d24640e9cf9d6e0c16a8f2d_2_1380x882.jpeg 2x" data-dominant-color="484747"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1444 698 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @flemingrachelc (2020-08-22 18:32 UTC)

<p>Oh! I totally overlooked the fact that they also provided the image stack! Thanks so much for looking into this, Andras!</p>
<p>-Rachel</p>

---
