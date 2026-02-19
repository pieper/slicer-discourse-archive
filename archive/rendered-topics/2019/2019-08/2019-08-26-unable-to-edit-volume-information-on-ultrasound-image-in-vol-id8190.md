---
topic_id: 8190
title: "Unable To Edit Volume Information On Ultrasound Image In Vol"
date: 2019-08-26
url: https://discourse.slicer.org/t/8190
---

# Unable to edit volume information on ultrasound image in "Volumes" module

**Topic ID**: 8190
**Date**: 2019-08-26
**URL**: https://discourse.slicer.org/t/unable-to-edit-volume-information-on-ultrasound-image-in-volumes-module/8190

---

## Post #1 by @David_Asgar-Deen (2019-08-26 23:28 UTC)

<p>Hello,</p>
<p>I am currently using 3D Slicer for a volume reconstruction of a series of ultrasound (US) image slices. In my slice controller (containing my live US image), I am unable to change the pixel spacing Volumes module.</p>
<p>For background, I am currently streaming my ultrasound data through a Plus Server (can email .xml file on request as I’m unable to attach it to this post) to 3D Slicer. I am using the OpenIGTLinkIF module (inside Slicer IGT) to connect 3D Slicer and the Plus Server. I proceeded to define the red slice controller as my image and attempted to use the Volumes module to get the proper pixel spacing.</p>
<p>Any help on the topic would be greatly appreciated.</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2019-08-26 23:50 UTC)

<p>Image spacing is embedded in the OpenIGTLink image message, therefore the value that you manually type is immediately overwritten when you get the next image. To have correct image spacing in Slicer, either adjust the OpenIGTLink sender to provide images with the appropriate spacing or in Slicer apply a transform to the image. See <a href="http://www.slicerigt.org/wp/user-tutorial/" rel="nofollow noopener">SlicerIGT tutorials</a> for detailed instructions and explanations.</p>

---

## Post #3 by @David_Asgar-Deen (2019-08-27 00:22 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="8190">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>the OpenIGTLink image message, therefore the value that you manually type is immediately overwritten when you get th</p>
</blockquote>
</aside>
<p>Hello Andras,</p>
<p>Thank you very much for your reply! I was originally using the SlicerIGT tutorials and was unable to find the specific lesson that relates to image spacing. I currently know that my pixel spacing along the transducer probe (marked axis) is 0.1 [mm] and the spacing along the depth of the image (far axis) is 0.085 [mm] but am unsure how to translate this into my .xml file or directly in Slicer. Any further direction on this issue would be greatly appreciated.</p>
<p>I would like to thank you for taking the time to respond to me initially and I look forward to your response!</p>

---

## Post #4 by @lassoan (2019-08-27 00:23 UTC)

<p>Do you have a position tracker attached to your ultrasound probe?</p>

---

## Post #5 by @David_Asgar-Deen (2019-08-27 00:24 UTC)

<p>I do have an Aurora NDI 6DOF EM tracker affixed to the probe on the side. I was going through lesson U-31 to compute the transformation between the tracker position and the image frame.</p>

---

## Post #6 by @lassoan (2019-08-27 01:16 UTC)

<p>OK, if the probe is tracked and calibrated then you can follow <a href="http://www.slicerigt.org/wp/user-tutorial/" rel="nofollow noopener">U-33 and U-34 SlicerIGT tutorials</a> about volume reconstruction. If you have difficulties in setting up your Plus configuration file, then you can post questions on the <a href="https://github.com/PlusToolkit/PlusLib/issues" rel="nofollow noopener">Plus issue tracker</a>.</p>

---

## Post #7 by @David_Asgar-Deen (2019-08-27 19:38 UTC)

<p>Hello Andras,</p>
<p>Thank you very much for the help, I have found out a solution to my problem! I modified the transformation matrix in the .xml to incorporate the scaling. For anyone else looking at this problem the way I set up my transformation matrix is shown in the figure attached. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9a6a8834c73a242b04cce461ca2c403e7ef2c21.png" data-download-href="/uploads/short-url/v3qFPJvMFbPh1C4JKpifOKaiqyJ.png?dl=1" title="Transformation_Matrix" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9a6a8834c73a242b04cce461ca2c403e7ef2c21_2_517x148.png" alt="Transformation_Matrix" data-base62-sha1="v3qFPJvMFbPh1C4JKpifOKaiqyJ" width="517" height="148" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9a6a8834c73a242b04cce461ca2c403e7ef2c21_2_517x148.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9a6a8834c73a242b04cce461ca2c403e7ef2c21_2_775x222.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9a6a8834c73a242b04cce461ca2c403e7ef2c21_2_1034x296.png 2x" data-dominant-color="F5F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Transformation_Matrix</span><span class="informations">1190×342 10.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
