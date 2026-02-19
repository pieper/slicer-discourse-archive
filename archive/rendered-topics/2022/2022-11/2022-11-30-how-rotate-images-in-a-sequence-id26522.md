---
topic_id: 26522
title: "How Rotate Images In A Sequence"
date: 2022-11-30
url: https://discourse.slicer.org/t/26522
---

# How rotate images in a sequence?

**Topic ID**: 26522
**Date**: 2022-11-30
**URL**: https://discourse.slicer.org/t/how-rotate-images-in-a-sequence/26522

---

## Post #1 by @sunshine (2022-11-30 21:25 UTC)

<p>How to “anti-Transverse” for a sequence? Or, how to do inplane rotation for images in a sequence for 90 degree (not 3D rotation, but 2D in-plane rotation)?</p>
<p>Hi everyone,</p>
<p>I need help fixing a sequence of linear transforms. The sequences are ultrasound data collected using modules “OpenIGTLinkIF” and “Volume Reslice Diver”. However, I probably incorrectly set up the module “Volume Reslice Driver” (as the screenshot shows below) when I was collecting the data, resulting in all ultrasound images rotated for 90 degrees.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c107c99e4574ffc364305400f078ce8f266ce774.png" alt="image" data-base62-sha1="rxCPRR6p00StuDd673qpCcnqjxa" width="690" height="127"></p>
<p>How can I batch-process the sequence to  “anti-Transverse” all the linear transforms, so that all the images can rotate back in 3D while maintaining the 3D position relationship among images in the sequence? In other words, how to let each frame in a sequence <strong>in-plane</strong> rotate 90 degrees instead of a 3D rotation? (What kind of python script function should I write in order to achieve it?)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d4012914e4a296ce674a590ee3a3447501ccfbca.jpeg" data-download-href="/uploads/short-url/uftI1oMhVGGTpm2SepG6rfxWxxE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4012914e4a296ce674a590ee3a3447501ccfbca_2_411x375.jpeg" alt="image" data-base62-sha1="uftI1oMhVGGTpm2SepG6rfxWxxE" width="411" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4012914e4a296ce674a590ee3a3447501ccfbca_2_411x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4012914e4a296ce674a590ee3a3447501ccfbca_2_616x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d4012914e4a296ce674a590ee3a3447501ccfbca_2_822x750.jpeg 2x" data-dominant-color="A9A7A5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1445×1318 220 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you so much in advance!</p>

---

## Post #2 by @lassoan (2022-12-01 01:18 UTC)

<p>You can fix this by applying a simple linear transform to the image (TransducerToProbe) to fix this. Your transform tree will look like this:</p>
<pre><code class="lang-auto">-- ProbeToReference
    +-- TransducerToProbe
        +-- Image_Transducer
</code></pre>
<ul>
<li>ProbeToReference is the transform provided by the tracking system (changing in time, along with the image)</li>
<li>TransducerToProbe transform is responsible for correctly positioning and orienting the image slice relative to the tracking sensor/marker.</li>
<li>Image_Transducer is the image you recorded, it contains a constant transform that is usually used for scaling and moving the image so that its origin is in the transducer’s origin and the Y axis is the sound propagation direction. If in your case the axes are not aligned like this it is not an issue at all, as you can compensate for any errors in the TransducerToProbe transform.</li>
</ul>

---

## Post #4 by @sunshine (2022-12-01 20:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="26522">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<pre><code class="lang-auto">-- ProbeToReference
    +-- TransducerToProbe
        +-- Image_Transducer
</code></pre>
</blockquote>
</aside>
<p>Problem solved! Thank you so much!</p>
<p>BTW, could you please confirm that the error resulted from using the “Transverse” mode in the module “Volume Reslice Diver” when collecting the sequence data? I forgot why I chose that mode. Should I choose it next time when collecting sequence data?</p>

---

## Post #5 by @ungi (2022-12-02 22:39 UTC)

<p>No, Volume Reslice Driver does not change any data, except for the positions of the 2D views. It moves the views to the ultrasound images, not the images to the views.</p>

---

## Post #6 by @sunshine (2022-12-03 00:49 UTC)

<aside class="quote no-group" data-username="ungi" data-post="5" data-topic="26522">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ungi/48/78573_2.png" class="avatar"> ungi:</div>
<blockquote>
<p>except for the positions of the 2D views</p>
</blockquote>
</aside>
<p>Hi Tamas,</p>
<p>Thank you so much for your reply!</p>
<p>Not exactly sure I get your point.</p>
<p>The error in my collected data is from the sequential linear transform matrices, that all of the images in the sequence were (in-plane) rotated for 90 degrees. It was not easy to figure that out, but the error can lead to absolutely wrong 3D information. Till now, I have no idea what lead to the error.</p>

---

## Post #7 by @lassoan (2022-12-03 04:04 UTC)

<aside class="quote no-group" data-username="sunshine" data-post="6" data-topic="26522">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/3ec8ea/48.png" class="avatar"> sunshine:</div>
<blockquote>
<p>The error in my collected data is from the sequential linear transform matrices, that all of the images in the sequence were (in-plane) rotated for 90 degrees. It was not easy to figure that out, but the error can lead to absolutely wrong 3D information. Till now, I have no idea what lead to the error.</p>
</blockquote>
</aside>
<p>The problem was that the TransducerToProbe transform was missing from your transform hierarchy. The image was in <code>Transducer</code> coordinate system, so you had to transform it into the <code>Probe</code> coordinate system before you could apply the <code>ProbeToReference</code> transform.</p>

---

## Post #8 by @sunshine (2022-12-03 20:10 UTC)

<p>Thank you so much for your help!</p>
<p>Never knew that there are four different coordinate systems in this data acquisition procedure.</p>

---
