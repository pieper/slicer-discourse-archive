# CT data type, why int16?

**Topic ID**: 34522
**Date**: 2024-02-24
**URL**: https://discourse.slicer.org/t/ct-data-type-why-int16/34522

---

## Post #1 by @mau_igna_06 (2024-02-24 20:01 UTC)

<p>Hi,</p>
<p>I have been working with CTs since a few years now so I have seen lots of them. I’ve had the observation the scalar range difference is always between 8k or 5k (e.g: min=-3024, max=1890), but the datatype used on them allows int16 range, which means from -32768 to +32767.</p>
<p>That means that probably one could get away with using 2 or 3 less bits to represent each voxel value on the CT (i.e. int14 or int13, though not supported by real computer architectures). And I wondered if I could use less even bits without losing interpretability of the CT, so I used SimpleFilters to “scale down” a int16 CT to int8 (see pictures below respectively)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3ff888cf0d4f9f5b3f496d2d8455a54444895ca.jpeg" data-download-href="/uploads/short-url/ufqdTfwpbC8HpbRK9QyL6ImJcxA.jpeg?dl=1" title="Screenshot from 2024-02-24 16-34-42" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3ff888cf0d4f9f5b3f496d2d8455a54444895ca_2_690x453.jpeg" alt="Screenshot from 2024-02-24 16-34-42" data-base62-sha1="ufqdTfwpbC8HpbRK9QyL6ImJcxA" width="690" height="453" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3ff888cf0d4f9f5b3f496d2d8455a54444895ca_2_690x453.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3ff888cf0d4f9f5b3f496d2d8455a54444895ca_2_1035x679.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3ff888cf0d4f9f5b3f496d2d8455a54444895ca_2_1380x906.jpeg 2x" data-dominant-color="4C4B4A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-02-24 16-34-42</span><span class="informations">1907×1254 83.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>That draws me to the question, seeing that is possible to run SlicerTotalSegmentator on this CT in a couple of minutes, and that int8 is 256 times smaller than int16, would it be possible to re-train TotalSegmentator to work with int8 CTs to return results in around 1 second?</p>
<p>Your thoughts are welcomed <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @lassoan (2024-02-25 14:31 UTC)

<p>Often 8 bits per pixel could be enough if you need to distinguish bone from soft tissues. However, there are important use cases where 8-bits dynamic range for the entire CT image is insufficient, for example when differentiating between soft tissues (common in brain CT images) or doing digital subtraction (difference between native and opacified images). It would be also somewhat inconvenient to manage the scaling information that converts HU to image-specific 8-bit intensity range.</p>
<aside class="quote no-group" data-username="mau_igna_06" data-post="1" data-topic="34522">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>int8 is 256 times smaller than int16</p>
</blockquote>
</aside>
<p>Int8 is just 2x smaller not a big difference. But more importantly, all computations in the neural network is done in floats anyway.</p>
<p>You have a good point in that it is important to pay attention how you convert segmentation inputs/outputs between the external int8 or int16 and the internal float, as it greatly affects memory usage and therefore computation time. We recently reduced MONAIAuto3DSeg computation time on a 16GB laptop from 800 seconds to 120 seconds by converting output to int16 earlier (by reducing memory need from 17GB to 3 GB).</p>

---
