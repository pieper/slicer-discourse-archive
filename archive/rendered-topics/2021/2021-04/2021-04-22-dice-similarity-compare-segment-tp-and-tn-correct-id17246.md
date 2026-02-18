# Dice Similarity compare segment TP and TN correct?

**Topic ID**: 17246
**Date**: 2021-04-22
**URL**: https://discourse.slicer.org/t/dice-similarity-compare-segment-tp-and-tn-correct/17246

---

## Post #1 by @Focus (2021-04-22 09:02 UTC)

<p>I use this module to compare segment and I use the same model. I don’t know why TruePositve value is less than TrueNegative value. I think this algorithm is measure from the box of pink. Am I true?? that the area outside the segment is TN and the segment model is a TP. I write on the picture down below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff2b3dc5fbb0234f720920278b1e8d72d42ddfe5.png" data-download-href="/uploads/short-url/ApkoJRn3XfNX8DbpQHAdRASRUW1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff2b3dc5fbb0234f720920278b1e8d72d42ddfe5_2_690x346.png" alt="image" data-base62-sha1="ApkoJRn3XfNX8DbpQHAdRASRUW1" width="690" height="346" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff2b3dc5fbb0234f720920278b1e8d72d42ddfe5_2_690x346.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff2b3dc5fbb0234f720920278b1e8d72d42ddfe5_2_1035x519.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/f/ff2b3dc5fbb0234f720920278b1e8d72d42ddfe5_2_1380x692.png 2x" data-dominant-color="C8C9DF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1893×951 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Focus (2021-04-22 09:10 UTC)

<p>I found this documentation source module and I think is it wrong measure? formula that dice similarity is use Union instead of intersect.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fce113a8192f470734c43e0aadc4a2709cc7e2cc.png" data-download-href="/uploads/short-url/A54xVY2DNBTxVDQoBLVGBjhfO6o.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fce113a8192f470734c43e0aadc4a2709cc7e2cc.png" alt="image" data-base62-sha1="A54xVY2DNBTxVDQoBLVGBjhfO6o" width="690" height="124" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1115×201 11.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I surf on the internet that dice similarity look like this. Can anyone tell me that I got it right?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec81e8faf06d6d59a3f11592d0706294f923ffcd.png" alt="image" data-base62-sha1="xKf0S9eZB2WScjIwmLssmmVQ2Bv" width="243" height="214"></p>

---

## Post #3 by @mikebind (2021-04-22 21:23 UTC)

<p>On a quick look, this seems OK to me.  TP is less than TN because there are more voxels where the object isn’t present than where it is present.  20% of the voxels are object, and 80% are not object. Dice value is 1 because 2 * (0.2 * N) / (0.2<em>N + 0.2</em>N) = 1 (where N = number of voxels). The intersection of A and B is 0.2<em>N because A has volume 0.2</em>N and B has volume 0.2*N and all of those voxels are in the same place (because A=B) in your example.</p>

---

## Post #4 by @Focus (2021-04-23 12:44 UTC)

<p>Thank you for your support.</p>

---
