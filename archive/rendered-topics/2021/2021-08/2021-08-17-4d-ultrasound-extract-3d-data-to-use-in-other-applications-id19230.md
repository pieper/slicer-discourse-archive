# 4D ultrasound - extract 3D data to use in other applications?

**Topic ID**: 19230
**Date**: 2021-08-17
**URL**: https://discourse.slicer.org/t/4d-ultrasound-extract-3d-data-to-use-in-other-applications/19230

---

## Post #1 by @arumiat (2021-08-17 15:06 UTC)

<p>Hi Slicer community,</p>
<p>I’ve been sent a cardiac dataset which appears to be a number of volumes extracted directly from an ultrasound machine (I am attaching a video of all the volumes available).<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/081a8a7efc8991698c9d252278a613970f5901cb.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/081a8a7efc8991698c9d252278a613970f5901cb.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/081a8a7efc8991698c9d252278a613970f5901cb.mp4</a>
    </source></video>
  </div><p></p>
<p>I have never worked with such a dataset before &amp; am interested in anyone has any tips on topics / areas I should familiarise myself with to understand more.</p>
<p>Ultimately I’d like to extract the volumes into a format that we could query in 3D in Unity for instance, a bit like we have done for this CT data → <a href="https://rumble.com/vbcwdg-canine-echocardiography-simulator-mobile-phone-3d-veterinary-learning-ivala.html" class="inline-onebox" rel="noopener nofollow ugc">Canine echocardiography simulator mobile phone - 3D Veterinary Learning, IVALA</a>.</p>
<p>It would be cool for a learner to be able to ‘slice’ through the ultrasound 3D volume in realtime and have the 2D view reflect what they are seeing.</p>
<p>A good start would rpobably be if there were a way to convert a volume into a set of images?</p>
<p>At the moment these volumes are single files with no recognisable extension.</p>
<p>Any tips welcomed!</p>

---

## Post #2 by @pieper (2021-08-17 17:57 UTC)

<p>As far as I can tell those are all just recordings of 2D sequences, not true 4D ultrasound data.  You would need to record a sweep, ideally with a tracked probe, or use a natively 3D probe.</p>

---

## Post #3 by @arumiat (2021-08-18 07:59 UTC)

<p>Thank you <a class="mention" href="/u/pieper">@pieper</a> .</p>
<p>Is a ‘natively probe’ a specific thing or did you just mean to type ‘native’ ?</p>
<p>I will ask them also about their machine &amp; capabilities.</p>

---

## Post #4 by @pieper (2021-08-18 14:54 UTC)

<p>By " a natively 3D probe" I mean a <a href="https://en.wikipedia.org/wiki/3D_ultrasound">probe that acquires a volume</a> rather than a slice.</p>

---

## Post #5 by @lassoan (2021-08-21 03:51 UTC)

<p>Pixel data in these series seem to contain only screen capture videos. This is very common in ultrasound imaging. In addition to this, the series may also contain 3D/4D volume in private tags. SlicerHeart extension can extract these volumes from some kind of data sets. See more information <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/Docs/ImageImportExport.md">here</a>.</p>

---
