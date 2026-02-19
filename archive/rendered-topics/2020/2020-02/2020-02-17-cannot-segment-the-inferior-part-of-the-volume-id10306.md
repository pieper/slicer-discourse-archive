---
topic_id: 10306
title: "Cannot Segment The Inferior Part Of The Volume"
date: 2020-02-17
url: https://discourse.slicer.org/t/10306
---

# Cannot segment the inferior part of the volume

**Topic ID**: 10306
**Date**: 2020-02-17
**URL**: https://discourse.slicer.org/t/cannot-segment-the-inferior-part-of-the-volume/10306

---

## Post #1 by @doc-xie (2020-02-17 09:01 UTC)

<p>Hi everyone,<br>
In Segment Editor module, the inferior part of the volume cannot be segmented no matter in Scissors or Threshold effect (attached figure).<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d3043786339a43a0a37f40a98bc55e24fb6499e.jpeg" data-download-href="/uploads/short-url/k90J6BtbJ6m3ogelVhEVVNn2mWW.jpeg?dl=1" title="Screen Shot 2020-02-17 at 4.49.26 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d3043786339a43a0a37f40a98bc55e24fb6499e_2_690x429.jpeg" alt="Screen Shot 2020-02-17 at 4.49.26 PM" data-base62-sha1="k90J6BtbJ6m3ogelVhEVVNn2mWW" width="690" height="429" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d3043786339a43a0a37f40a98bc55e24fb6499e_2_690x429.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d3043786339a43a0a37f40a98bc55e24fb6499e_2_1035x643.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8d3043786339a43a0a37f40a98bc55e24fb6499e_2_1380x858.jpeg 2x" data-dominant-color="AEADB7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-02-17 at 4.49.26 PM</span><span class="informations">3356×2090 831 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc9950a76a04c4a4fe344d4ef172eefe3bb08f96.jpeg" data-download-href="/uploads/short-url/A2ANvB3E5jrxVtoY8Oq5EtmJqhU.jpeg?dl=1" title="Screen Shot 2020-02-17 at 4.51.02 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc9950a76a04c4a4fe344d4ef172eefe3bb08f96_2_690x419.jpeg" alt="Screen Shot 2020-02-17 at 4.51.02 PM" data-base62-sha1="A2ANvB3E5jrxVtoY8Oq5EtmJqhU" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc9950a76a04c4a4fe344d4ef172eefe3bb08f96_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc9950a76a04c4a4fe344d4ef172eefe3bb08f96_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc9950a76a04c4a4fe344d4ef172eefe3bb08f96_2_1380x838.jpeg 2x" data-dominant-color="A5A5B4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-02-17 at 4.51.02 PM</span><span class="informations">3354×2038 797 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Version: 4.11.0<br>
System: Mac<br>
Best wishes,<br>
Xie</p>

---

## Post #2 by @doc-xie (2020-02-17 09:04 UTC)

<p>Moreover, the volume can be labeled totally in Editor module.</p>

---

## Post #3 by @JanWitowski (2020-02-17 09:21 UTC)

<p>Can you check that you have correctly set your master volume? If yes, try changing the source segmentation geometry to your input volume:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bf540d03f2886ffa3322ec1e431dafbf72e2551.png" alt="" data-base62-sha1="8ypCDPLGyUsj3zzZvqTQAQ8p649" role="presentation"></p>

---

## Post #4 by @doc-xie (2020-02-17 13:35 UTC)

<p>Thank you very much!<br>
It works well for me now.<br>
Best wishes,<br>
Xie</p>

---
