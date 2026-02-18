# Is it possible to perform this kind of slicing (attached below) for 3D data generated from multiple slices?

**Topic ID**: 21937
**Date**: 2022-02-12
**URL**: https://discourse.slicer.org/t/is-it-possible-to-perform-this-kind-of-slicing-attached-below-for-3d-data-generated-from-multiple-slices/21937

---

## Post #1 by @hdyk (2022-02-12 17:13 UTC)

<p>Hello.<br>
I am creating a 3D dataset from multiple slices I obtained from measurement. The generated 3D dataset has a shape similar to a ball.</p>
<p>I was able to slice the dataset and see the inside in X and Y direction.</p>
<p>My question is, is it possible to perform this kind of slicing as shown by image below?<br>
If it is possible could anyone please share any reference I can refer to?</p>
<p>Because I would like to put the final result for demonstration purpose.</p>
<p>Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65dcd9c4278fa77a98febdc515740e74b3d780d1.jpeg" data-download-href="/uploads/short-url/ex7otNE1ZpeOT0NbfhYGybywmC5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/65dcd9c4278fa77a98febdc515740e74b3d780d1_2_500x500.jpeg" alt="image" data-base62-sha1="ex7otNE1ZpeOT0NbfhYGybywmC5" width="500" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/65dcd9c4278fa77a98febdc515740e74b3d780d1_2_500x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/65dcd9c4278fa77a98febdc515740e74b3d780d1_2_750x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/65dcd9c4278fa77a98febdc515740e74b3d780d1_2_1000x1000.jpeg 2x" data-dominant-color="9C9B79"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×1280 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-02-12 17:28 UTC)

<p>Yes, this is supported, see example here:</p>
<aside class="quote quote-modified" data-post="7" data-topic="118">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/hide-data-inside-roi-when-volume-rendering/118/7">Hide data inside ROI when Volume Rendering</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Also note that you can get almost the same result by showing slice views (with thresholding enabled for the volume, to remove black borders) and a skin surface model (slice clipping enabled to be able to see inside the head). 
Example (<a href="https://1drv.ms/u/s!Arm_AFxB9yqHr5BI0Hag1rewSdETWg">download the scene from here</a>): 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/e6d24c90190c1e4315521adc7bae274d303e861e.gif" data-download-href="/uploads/short-url/wVWnFZhfQCwWyiXKAJMVk58R6OO.gif?dl=1" title="ClipIntoBrainS.gif">[image]</a>
  </blockquote>
</aside>

<p>          <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/e6d24c90190c1e4315521adc7bae274d303e861e.gif" target="_blank" rel="noopener" class="onebox">
            <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/e6d24c90190c1e4315521adc7bae274d303e861e.gif" width="555" height="500">
          </a>
</p>

---

## Post #3 by @hdyk (2022-02-13 05:59 UTC)

<p>Thank you for your kind answer, Mr. Lassoan.<br>
It is exactly what I would love to do.</p>
<p>However, when I clicked the apply button, I got a dark area inside the clipping box (which I thought that the area inside the box should be removed, as I attached here). Did I perhaps not do it correctly?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d262572c33a75ae8638108ab57ff2dc040ab8718.png" data-download-href="/uploads/short-url/u18XFoMDESTi3v8UqhCsaWViSFi.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d262572c33a75ae8638108ab57ff2dc040ab8718_2_668x500.png" alt="Capture" data-base62-sha1="u18XFoMDESTi3v8UqhCsaWViSFi" width="668" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d262572c33a75ae8638108ab57ff2dc040ab8718_2_668x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d262572c33a75ae8638108ab57ff2dc040ab8718.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d262572c33a75ae8638108ab57ff2dc040ab8718.png 2x" data-dominant-color="5A5B6E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">873×653 85 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For your information, my input slices are RGB JPG images, because normally I would like to show the final result in color.</p>
<p>Thank you.</p>

---

## Post #4 by @lassoan (2022-02-13 13:42 UTC)

<p>Crop volume module was not used in the example above. You can follow these steps instead’</p>
<ul>
<li>create a segment that defines the region within you want to show the structures, such as the skin, brain, or bone surface; in the example above the skin surface was segmented (Segment Editor module)</li>
<li>show intersecting slices
<ul>
<li>use the segment to blank out the volume outside that region (Segment Editor module, Mask volume effect)</li>
<li>show the blanked out volume in slice views using thresholding (Volumes module)</li>
</ul>
</li>
<li>show clipped outer surface:
<ul>
<li>export the segment to a model (Data module, right-click on the segment)</li>
<li>enable slice clipping for that model (Models module)</li>
</ul>
</li>
</ul>
<p>Let us know if you need help with any of the steps.</p>

---
