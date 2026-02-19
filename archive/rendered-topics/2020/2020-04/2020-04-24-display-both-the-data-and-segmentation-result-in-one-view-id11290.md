---
topic_id: 11290
title: "Display Both The Data And Segmentation Result In One View"
date: 2020-04-24
url: https://discourse.slicer.org/t/11290
---

# Display both the data and segmentation result in one view

**Topic ID**: 11290
**Date**: 2020-04-24
**URL**: https://discourse.slicer.org/t/display-both-the-data-and-segmentation-result-in-one-view/11290

---

## Post #1 by @Patrice_Gaofei (2020-04-24 13:05 UTC)

<pre><code>             Dear members of the 3DSlicer community,
</code></pre>
<p>I am very new to Slicer and I need your help and suggestions for visualizing my segmentation results. In effect, my task consists of a binary segmentation. I would like to represent both the image and predicted result in one view with a color bar to illustrate the performance of my model. An example of such figure is as follows.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/b/0b53e75dabbb0baa67b4ea78e93a0f3d7d75db31.png" alt="fault" data-base62-sha1="1Cd0WlJA8UPxJrizgYDnYuHwv5f" width="462" height="270"></p>
<p>Any suggestions and/or comments would be highly appreciated</p>

---

## Post #2 by @pieper (2020-04-24 13:36 UTC)

<p>You can display binary segmentations or if you have a parametric result you can use a scalar volume and add a color table and scalar bar in 3D (see the Volumes and Colors modules).  Making the slice planes visible in 3D should give something comparable to the illustration (although to be honest I can’t really parse the example figure well - maybe you can provide more context info).</p>

---

## Post #3 by @Patrice_Gaofei (2020-04-24 16:45 UTC)

<p>Dear sir, I am very grateful for your reply. The figure displayed above consists of 3D seismic data with the corresponding segmentation results. I would like to achieve a figure like that using my own data and the prediction results. Please, could you give me some steps to achieve that based on your experience? I am very new to Slicer and I could not find any tutorial or videos related to what I would like to obtain.</p>
<p>Thank you for your time, patience and support.</p>

---

## Post #4 by @pieper (2020-04-24 18:42 UTC)

<p>I don’t think we have any tutorials quite like that, but as I said above, everything should be available.  Probably it depends a bit on exactly what format your data is in.</p>
<p>Maybe if you can share data like what you are trying to work with someone can create some screenshots for you just so you know where all the controls are.</p>

---

## Post #5 by @lassoan (2020-04-24 18:53 UTC)

<p>From what I can see, the computed output is a scalar volume, so it can be set as foreground volume (right-click on the eye icon of the colored volume in Data module) with a nice colormap (you can select colormap in Volumes module), while keeping the grayscale volume as background.</p>

---

## Post #6 by @Patrice_Gaofei (2020-04-25 02:13 UTC)

<p>Thank you sir for your time and suggestions.<br>
I have converted the data into nii format so that they can be easily uploaded onto Slicer.  Please, could we communicate by email?</p>

---

## Post #7 by @pieper (2020-04-25 16:24 UTC)

<p>Let’s keep the communication on the forum so that others can find it if similar questions come up in the future.</p>
<p>Can you share the data using dropbox, google drive, or similar?</p>

---

## Post #8 by @Patrice_Gaofei (2020-04-26 08:06 UTC)

<p>Thank you sir for your time and patience. A data sample can be accessed using the following link<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cloud.tsinghua.edu.cn/media/img/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://cloud.tsinghua.edu.cn/f/4c38bf31e2864938bae8/" target="_blank" rel="nofollow noopener">Tsinghua Cloud Storage</a>
  </header>
  <article class="onebox-body">
    <img src="https://cloud.tsinghua.edu.cn/media/img/file/192/file.png" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://cloud.tsinghua.edu.cn/f/4c38bf31e2864938bae8/" target="_blank" rel="nofollow noopener">SAMPLES.zip</a></h3>

<p>Share link for SAMPLES.zip.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>It contains a data sample, the label or mask and the corresponding prediction result. I have used the cloud storage system of my university.</p>
<p>I am very grateful for everything</p>

---
