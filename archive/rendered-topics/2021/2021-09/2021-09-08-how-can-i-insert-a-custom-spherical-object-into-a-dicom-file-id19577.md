---
topic_id: 19577
title: "How Can I Insert A Custom Spherical Object Into A Dicom File"
date: 2021-09-08
url: https://discourse.slicer.org/t/19577
---

# How can I insert a custom spherical object into a DICOM file?

**Topic ID**: 19577
**Date**: 2021-09-08
**URL**: https://discourse.slicer.org/t/how-can-i-insert-a-custom-spherical-object-into-a-dicom-file/19577

---

## Post #1 by @Maya (2021-09-08 16:47 UTC)

<p>Hi there! I was wondering if there is a way to insert a custom spherical object into a DICOM file. I would like to segment CT images along the outer edges of that spherical object. Grateful for any instructions on how to do that. I’m a new 3D slicer user and am using version 4.11.20210226.</p>
<p>Best,<br>
Maya</p>

---

## Post #2 by @lassoan (2021-09-08 17:09 UTC)

<p>You can use Segment Editor module to draw a sphere using the “Paint” effect. Enable “Sphere brush” option. You can click the “%” sign next to the brush size selector to specify sphere size in millimeter.</p>
<p>You can use the sphere that you drew as a mask for further segmentation or burn it into the volume using “Mask volume” effect.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">This page</a> is a good starting point for learning about how to use segmentations.</p>

---

## Post #3 by @Maya (2021-09-08 17:12 UTC)

<p>Dear Mr. Lasso,</p>
<p>thank you for your quick response! I actually want to insert an ellipsoidal sphere. Is there a way to do that?</p>
<p>Thank you so much in advance!</p>
<p>Best,<br>
Maya</p>

---

## Post #4 by @lassoan (2021-09-08 17:55 UTC)

<p>You need to create the ellipsoid as a model node and import it into a the segmentation.</p>
<p>You can create an ellipsoid by creating a sphere (for example, using “Create models” module in SlicerIGT extension), then move it and stretch it using Transforms module. You can enable interactive translation/rotation/scaling in Display / Interaction / Visible in 3D view (click “More options” and check “Enable scaling” to allow stretching).</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03784d01d3d005aef4a3f70660caaf78159a87e9.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03784d01d3d005aef4a3f70660caaf78159a87e9.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/03784d01d3d005aef4a3f70660caaf78159a87e9.mp4</a>
    </source></video>
  </div><p></p>

---

## Post #5 by @Maya (2021-09-08 23:26 UTC)

<p>That is extremely helpful, thank you so much! I tried installing the SlicerIGT extension but unfortunately did not manage to do so. Could you kindly explain to me how I can do that?</p>
<p>Thank you for your time and efforts.</p>
<p>Best,<br>
Maya</p>

---

## Post #6 by @lassoan (2021-09-09 01:18 UTC)

<p>The extensions server is being migrated to a new version, until the transition is completed the Slicer Stable Release requires manual extension download and install. The extensions manager works well in the latest Slicer Preview Release, so I would recommend to use that now if you want to install extensions.</p>

---

## Post #7 by @Maya (2021-09-09 20:30 UTC)

<p>Dear Mr. Lasso,</p>
<p>thank you so much for your reply! I have managed installing the extension and creating the sphere per your instructions. How do I now display the sphere in the DICOMS? Can I create a sphere with specific dimensions too? Best,<br>
Maya</p>

---

## Post #8 by @lassoan (2021-09-10 03:22 UTC)

<aside class="quote no-group" data-username="Maya" data-post="7" data-topic="19577">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/cab0a1/48.png" class="avatar"> Maya:</div>
<blockquote>
<p>Can I create a sphere with specific dimensions too?</p>
</blockquote>
</aside>
<p>You specified the dimension in Create Models module.</p>
<aside class="quote no-group" data-username="Maya" data-post="7" data-topic="19577">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/cab0a1/48.png" class="avatar"> Maya:</div>
<blockquote>
<p>How do I now display the sphere in the DICOMS?</p>
</blockquote>
</aside>
<p>What software you would like to import the sphere into?<br>
Would you like to paste the ellipsoid into the image (make it appear as a bright or dark object)?<br>
Or would you like to export the ellipsoid as a DICOM Segmentation Object? Or as an RT structure set?<br>
What is your overall goal?</p>

---

## Post #9 by @Maya (2021-09-10 03:39 UTC)

<p>Dear Mr. Lasso,</p>
<p>Thanks again for your swift reply!<br>
I‘m not sure where I specified the dimensions of the sphere. I only stretched it using the transform module but was not able to design it with specific dimensions. How can I make the ellipsoid have the<br>
dimensions 45mm x 26mm for example?</p>
<p>I would like to paste the ellipsoid into axial CT slices (red window) and make it appear as a bright object (or rather as an ellipsis on the 2 dimensional CT images). I would like to manually segment the area where that ellipsoid touches the chest wall, using the ellipsoid as guidance.</p>
<p>Do you think that that is possible? Thank you so much for your time and efforts.</p>
<p>Best,<br>
Maya</p>

---

## Post #10 by @lassoan (2021-09-10 03:45 UTC)

<aside class="quote no-group" data-username="Maya" data-post="9" data-topic="19577">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/cab0a1/48.png" class="avatar"> Maya:</div>
<blockquote>
<p>How can I make the ellipsoid have the<br>
dimensions 45mm x 26mm for example?</p>
</blockquote>
</aside>
<p>In Create models module, you can type 10.0mm size and then use Surface toolbox and set scaling factor of 4.5, 4.5, 2.6.</p>
<aside class="quote no-group" data-username="Maya" data-post="9" data-topic="19577">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/cab0a1/48.png" class="avatar"> Maya:</div>
<blockquote>
<p>I would like to paste the ellipsoid into axial CT slices (red window) and make it appear as a bright object (or rather as an ellipsis on the 2 dimensional CT images).</p>
</blockquote>
</aside>
<p>You can use import this model into the segmentation and paste it into the volume using Mask volume effect in Segment Editor module.</p>
<aside class="quote no-group" data-username="Maya" data-post="9" data-topic="19577">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/cab0a1/48.png" class="avatar"> Maya:</div>
<blockquote>
<p>I would like to manually segment the area where that ellipsoid touches the chest wall, using the ellipsoid as guidance.</p>
</blockquote>
</aside>
<p>I don’t understand this exactly. What would you like to segment, for what clinical purpose? Would you like segment the chest wall so that you can measure breast volume?</p>

---

## Post #11 by @Maya (2021-09-10 11:55 UTC)

<p>Dear Mr. Lasso,</p>
<p>thank you so much, I managed to create the ellipsoid with custom dimensions!</p>
<p>However, I still am unable to import the ellipsoid into the axial (red) view of the DICOMS. I clicked on Mask Volume, chose the operation „fill inside“. I clicked on „apply“, but the ellipsoid does not show in the CT Images. Is there anything else I have to consider?</p>
<p>I‘d like to make these measurements for research purposes. I’m a researcher at MGH working on a project in interventional radiology. For this project I am looking at CT images during cryoablation. The ellipsoid represents the iceball (per manufacturer manual) and I‘d like to measure the pleural surface, that is in contact with said iceball.</p>
<p>Thank you SO much for your help, I appreciate your time and efforts a lot!</p>
<p>Best,<br>
Maya</p>

---

## Post #12 by @lassoan (2021-09-10 20:04 UTC)

<aside class="quote no-group" data-username="Maya" data-post="11" data-topic="19577">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/cab0a1/48.png" class="avatar"> Maya:</div>
<blockquote>
<p>I clicked on „apply“, but the ellipsoid does not show in the CT Images. Is there anything else I have to consider?</p>
</blockquote>
</aside>
<p>Click the “eye” icon next to the “Output Volume” selector to see the created output volume.</p>
<aside class="quote no-group" data-username="Maya" data-post="11" data-topic="19577">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/cab0a1/48.png" class="avatar"> Maya:</div>
<blockquote>
<p>The ellipsoid represents the iceball (per manufacturer manual) and I‘d like to measure the pleural surface, that is in contact with said iceball.</p>
</blockquote>
</aside>
<p>You can perform this computation conveniently in Slicer. For example, you can get the intersection of the pleural surface and the iceball model using “Combine models” module (in Sandbox extension) and then see the surface area in Models module / Information section.</p>

---

## Post #13 by @Maya (2021-09-10 20:07 UTC)

<p>Dear Mr. Lasso,</p>
<p>I have clicked the eye icon, but the ellipsoid does not show up in the axial CT image unfortunately. Do I have to determine a certain “fill value”? What is the input, what is the output volume?</p>
<p>Best,<br>
Maya</p>

---

## Post #14 by @lassoan (2021-09-10 21:56 UTC)

<aside class="quote no-group" data-username="Maya" data-post="13" data-topic="19577">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/cab0a1/48.png" class="avatar"> Maya:</div>
<blockquote>
<p>I have clicked the eye icon, but the ellipsoid does not show up in the axial CT image unfortunately</p>
</blockquote>
</aside>
<p>Look at the output after you clicked “Apply”.</p>
<aside class="quote no-group" data-username="Maya" data-post="13" data-topic="19577">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/cab0a1/48.png" class="avatar"> Maya:</div>
<blockquote>
<p>Do I have to determine a certain “fill value”?</p>
</blockquote>
</aside>
<p>It is completely up to you. Use a larger value for brighter filling.</p>
<aside class="quote no-group" data-username="Maya" data-post="13" data-topic="19577">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/cab0a1/48.png" class="avatar"> Maya:</div>
<blockquote>
<p>What is the input, what is the output volume?</p>
</blockquote>
</aside>
<p>It is up to you. You can leave the default setting, which will use the current master volume as input and create a new output volume.</p>

---

## Post #15 by @Maya (2021-09-13 13:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="19577">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can perform this computation conveniently in Slicer. For example, you can get the intersection of the pleural surface and the iceball model using “Combine models” module (in Sandbox extension) and then see the surface area in Models module / Information section.</p>
</blockquote>
</aside>
<p>Hi Mr. Lasso, I managed to import the model into the axial view! Now I was wondering how I can get the intersection of the pleural surface and the iceball model. I have installed the Sandbox extension and clicked on “Combine models”. The ellipsoid I created is Input model A, how can I define the pleural surface as input model B? Will I have to segment the pleural surface manually or is there another way?</p>
<p>Thank you so much for your help!!</p>
<p>Best,<br>
Maya</p>

---

## Post #16 by @lassoan (2021-09-13 13:33 UTC)

<aside class="quote no-group" data-username="Maya" data-post="15" data-topic="19577">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/cab0a1/48.png" class="avatar"> Maya:</div>
<blockquote>
<p>Will I have to segment the pleural surface manually or is there another way?</p>
</blockquote>
</aside>
<p>Is the surface generated by LungCTAnalyzer extension what you need?</p>
<div class="youtube-onebox lazy-video-container" data-video-id="U9PUX-jLF0A" data-video-title="Easy creation of lung masks from lung CT in 3D Slicer" data-video-start-time="89" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=U9PUX-jLF0A&amp;t=89" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/U9PUX-jLF0A/maxresdefault.jpg" title="Easy creation of lung masks from lung CT in 3D Slicer" width="" height="">
  </a>
</div>


---
