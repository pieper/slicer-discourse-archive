---
topic_id: 14796
title: "Cant Get Axial Sagital And Coronal Mri Slices To Display Tog"
date: 2020-11-28
url: https://discourse.slicer.org/t/14796
---

# Can't get axial, sagital, and coronal MRI slices to display together like in tutorial

**Topic ID**: 14796
**Date**: 2020-11-28
**URL**: https://discourse.slicer.org/t/cant-get-axial-sagital-and-coronal-mri-slices-to-display-together-like-in-tutorial/14796

---

## Post #1 by @jsalas424 (2020-11-28 04:18 UTC)

<p>Hello,<br>
I got through the DICOM tutorial, but have hit a wall when loading in my own MRI data. In the tutorial, the series loads in and the 3 slices appear in the 3D viewer together, however when I load in my series, it seperates the 1 into 3 series and I can only see one of the slices at a time in my viewer (screenshots attached).</p>
<p>How can I reproduce the example given in the tutorial? I would be happy to provide a copy of the data since it’s not subject to HIPAA anyways.</p>
<p>I’m ultimately looking to reconstruct 3D volume of the heart from these images.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d24f825952ce1f54965026a8c29fdcaddb921859.jpeg" data-download-href="/uploads/short-url/u0uCdvsh3VxNA5a6yAgCcU2pgjD.jpeg?dl=1" title="Screen Shot 2020-11-27 at 10.36.22 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d24f825952ce1f54965026a8c29fdcaddb921859_2_690x431.jpeg" alt="Screen Shot 2020-11-27 at 10.36.22 PM" data-base62-sha1="u0uCdvsh3VxNA5a6yAgCcU2pgjD" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d24f825952ce1f54965026a8c29fdcaddb921859_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d24f825952ce1f54965026a8c29fdcaddb921859_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d24f825952ce1f54965026a8c29fdcaddb921859_2_1380x862.jpeg 2x" data-dominant-color="35353C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-11-27 at 10.36.22 PM</span><span class="informations">2880×1800 404 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/6/16abab44006946941bfc41b469596dc575f537e5.jpeg" data-download-href="/uploads/short-url/3eyiOEuqGUWjWy6TcKO9d0iMuBn.jpeg?dl=1" title="Screen Shot 2020-11-27 at 10.36.28 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/16abab44006946941bfc41b469596dc575f537e5_2_690x431.jpeg" alt="Screen Shot 2020-11-27 at 10.36.28 PM" data-base62-sha1="3eyiOEuqGUWjWy6TcKO9d0iMuBn" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/16abab44006946941bfc41b469596dc575f537e5_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/16abab44006946941bfc41b469596dc575f537e5_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/16abab44006946941bfc41b469596dc575f537e5_2_1380x862.jpeg 2x" data-dominant-color="434450"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-11-27 at 10.36.28 PM</span><span class="informations">2880×1800 389 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31f7aada41fe1441798c526ac5fbd710b399c450.jpeg" data-download-href="/uploads/short-url/7821iHrV0HNErnNlIWKW9Jo8RDG.jpeg?dl=1" title="Screen Shot 2020-11-27 at 10.36.15 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31f7aada41fe1441798c526ac5fbd710b399c450_2_690x431.jpeg" alt="Screen Shot 2020-11-27 at 10.36.15 PM" data-base62-sha1="7821iHrV0HNErnNlIWKW9Jo8RDG" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31f7aada41fe1441798c526ac5fbd710b399c450_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31f7aada41fe1441798c526ac5fbd710b399c450_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31f7aada41fe1441798c526ac5fbd710b399c450_2_1380x862.jpeg 2x" data-dominant-color="474754"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-11-27 at 10.36.15 PM</span><span class="informations">2880×1800 410 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-11-28 04:38 UTC)

<aside class="quote no-group" data-username="jsalas424" data-post="1" data-topic="14796">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a87d85/48.png" class="avatar"> jsalas424:</div>
<blockquote>
<p>I would be happy to provide a copy of the data since it’s not subject to HIPAA anyways.</p>
</blockquote>
</aside>
<p>Yes, please share the data set (upload somewhere and post the download link here) then we can easily investigate.</p>

---

## Post #3 by @jsalas424 (2020-11-28 12:47 UTC)

<p>Link expires on 12/7 but I can extend if needed!<br>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://trachenet.duckdns.org/core/img/favicon.ico" class="site-icon" width="32" height="32">
      <a href="https://trachenet.duckdns.org/index.php/s/jmHrKRBSxZ2sm3o" target="_blank" rel="noopener nofollow ugc">Nextcloud</a>
  </header>
  <article class="onebox-body">
    <img src="https://trachenet.duckdns.org/core/img/favicon-fb.png" class="thumbnail onebox-avatar" width="200" height="200">

<h3><a href="https://trachenet.duckdns.org/index.php/s/jmHrKRBSxZ2sm3o" target="_blank" rel="noopener nofollow ugc">tfl_loc_multi_iPAT_2_2</a></h3>

<p>Nextcloud - a safe home for all your data</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #4 by @issakomi (2020-11-28 16:33 UTC)

<p>The series contains slices with different orientations, Slicer separated them  into 3 volumes by “image orientation (patient)” attribute. IMHO, very good. Original slices in series look in physical space like that:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3a5b4e6c32acf7ac26bf1161cb08a6d56120caa.png" data-download-href="/uploads/short-url/pDeuvufuotjEJ3TQQZdJCHaXrIK.png?dl=1" title="20201128-135924" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3a5b4e6c32acf7ac26bf1161cb08a6d56120caa_2_250x250.png" alt="20201128-135924" data-base62-sha1="pDeuvufuotjEJ3TQQZdJCHaXrIK" width="250" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3a5b4e6c32acf7ac26bf1161cb08a6d56120caa_2_250x250.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3a5b4e6c32acf7ac26bf1161cb08a6d56120caa_2_375x375.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3a5b4e6c32acf7ac26bf1161cb08a6d56120caa_2_500x500.png 2x" data-dominant-color="373E3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20201128-135924</span><span class="informations">791×791 63.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>AFAIK, it is possible to view slices from <em>red, green and yellow</em> windows at once, if eye symbol is checked in every window (one of 3 volumes at a time, one slice is original and 2 reconstructed)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df3de8343ae551b210a26383b6d71441993639d4.jpeg" data-download-href="/uploads/short-url/vQT6TfkUjJHUkxwaEfVk9yjJgfG.jpeg?dl=1" title="scr" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df3de8343ae551b210a26383b6d71441993639d4_2_690x427.jpeg" alt="scr" data-base62-sha1="vQT6TfkUjJHUkxwaEfVk9yjJgfG" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df3de8343ae551b210a26383b6d71441993639d4_2_690x427.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df3de8343ae551b210a26383b6d71441993639d4_2_1035x640.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df3de8343ae551b210a26383b6d71441993639d4.jpeg 2x" data-dominant-color="79797D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">scr</span><span class="informations">1321×818 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @jsalas424 (2020-11-28 19:12 UTC)

<p>Thanks for the reply. I can’t figure out how you overlayed the volumes like in your first picture.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d52b5e801c7563dacccbc4cb58ebbb57f3405b6.jpeg" data-download-href="/uploads/short-url/djzBTXWh6r9LXvPZaTpUQjkLUH4.jpeg?dl=1" title="Screen Shot 2020-11-28 at 2.09.41 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d52b5e801c7563dacccbc4cb58ebbb57f3405b6_2_690x431.jpeg" alt="Screen Shot 2020-11-28 at 2.09.41 PM" data-base62-sha1="djzBTXWh6r9LXvPZaTpUQjkLUH4" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d52b5e801c7563dacccbc4cb58ebbb57f3405b6_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d52b5e801c7563dacccbc4cb58ebbb57f3405b6_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5d52b5e801c7563dacccbc4cb58ebbb57f3405b6_2_1380x862.jpeg 2x" data-dominant-color="42434F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-11-28 at 2.09.41 PM</span><span class="informations">2880×1800 390 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>When I visualize of the 3 sets, it unchecks the other 2. Like I said earlier, I’m going to need the recreate the 3D volume of the endocardium from this dataset and I’m stuck as how to proceed.</p>
<p>I’m brand new to 3D visualization so thanks ahead of time for the patience!</p>

---

## Post #6 by @issakomi (2020-11-28 19:28 UTC)

<p>1st screen is from another app, in Slicer it is possible to view several volumes at once (<em>eye</em> symbol for every volume in “Volume Rendering”), is is close to that view.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f14e2c022577e86fd0c310e00bd134db4af1a8db.jpeg" data-download-href="/uploads/short-url/yqGyhpSsQkiRuRa4WatvGJ3Lezh.jpeg?dl=1" title="Screenshot at 2020-11-28 20-24-01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f14e2c022577e86fd0c310e00bd134db4af1a8db_2_690x488.jpeg" alt="Screenshot at 2020-11-28 20-24-01" data-base62-sha1="yqGyhpSsQkiRuRa4WatvGJ3Lezh" width="690" height="488" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f14e2c022577e86fd0c310e00bd134db4af1a8db_2_690x488.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f14e2c022577e86fd0c310e00bd134db4af1a8db.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f14e2c022577e86fd0c310e00bd134db4af1a8db.jpeg 2x" data-dominant-color="B8B8C7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot at 2020-11-28 20-24-01</span><span class="informations">861×609 107 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2020-11-28 19:32 UTC)

<p>If you click the eye icon in the data module then the volume is shown in all views. To show different volume in each slice view, you can click “Show view controls” then select the volume in “Background volume selector” - see <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">documentation</a>.</p>

---

## Post #8 by @jsalas424 (2020-11-28 22:04 UTC)

<p>Thank you for the help! I’m one step closer!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/9583dbacb64f5500550580993f402fd3d1bab19c.jpeg" data-download-href="/uploads/short-url/lkFEa4C3hyyqk8IARbetNwrlGSo.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9583dbacb64f5500550580993f402fd3d1bab19c_2_690x431.jpeg" alt="image" data-base62-sha1="lkFEa4C3hyyqk8IARbetNwrlGSo" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9583dbacb64f5500550580993f402fd3d1bab19c_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9583dbacb64f5500550580993f402fd3d1bab19c_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9583dbacb64f5500550580993f402fd3d1bab19c_2_1380x862.jpeg 2x" data-dominant-color="53505B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2880×1800 661 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I managed to set my ROI for the heart, where does one proceed from here for reconstructing a 3D mesh from endocardial volume? I’ve found the segmentations documentation: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html" class="inline-onebox" rel="noopener nofollow ugc">Segmentations — 3D Slicer documentation</a> but am weary I’m missing something since this is my first time. Is there anything else I should be referencing to do this?</p>

---

## Post #9 by @lassoan (2020-11-29 03:55 UTC)

<p>You can segment the endocardial surface using Segment Editor module. These tutorials should help you getting started: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation</a></p>

---
