---
topic_id: 25767
title: "Us Vessel Segmentation"
date: 2022-10-19
url: https://discourse.slicer.org/t/25767
---

# US vessel segmentation

**Topic ID**: 25767
**Date**: 2022-10-19
**URL**: https://discourse.slicer.org/t/us-vessel-segmentation/25767

---

## Post #1 by @whu (2022-10-19 02:43 UTC)

<p>Hello,  Here I used the US device to scan the femoral vein, and get some MP4 videos.<br>
The images like this:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3b07a9fe398fc973d85273f473f9fa6d9ba57ce.jpeg" alt="18" data-base62-sha1="pDBzrIZbWmKphxzqf0s9YPDUVtk" width="240" height="416"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38dad443c0d7cedf88a3cd9a3d146d85cf0b1fb9.jpeg" alt="2" data-base62-sha1="86XzOvwta1eubcBA63PA9P3p6yt" width="240" height="416"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e970be9d91e882ce3acf5035291775fd47975c2.jpeg" alt="23" data-base62-sha1="mCX3tqQeCHkKLELHjlxU5PyKgkq" width="240" height="416"></p>
<p>Now, I want to do the vessel segmetation, especially the traditional method.<br>
As suggest, get the magnitude of the intensity gradient in SimVascular, but that is CT based data, here is US.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88b87b257cf038a4f1a20b82bb1107be6b14d70c.jpeg" data-download-href="/uploads/short-url/jvubskaqq7tu3TXze4Wlo8gXahu.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88b87b257cf038a4f1a20b82bb1107be6b14d70c_2_690x375.jpeg" alt="image" data-base62-sha1="jvubskaqq7tu3TXze4Wlo8gXahu" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88b87b257cf038a4f1a20b82bb1107be6b14d70c_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88b87b257cf038a4f1a20b82bb1107be6b14d70c.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88b87b257cf038a4f1a20b82bb1107be6b14d70c.jpeg 2x" data-dominant-color="17191C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">735×400 52.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
please share some suggestions using simple filter and python based package.<br>
thanks.</p>

---

## Post #2 by @lassoan (2022-10-19 05:09 UTC)

<p>Nowadays the most common approach for this kind of segmentation tasks is to train a unet network for this. You can create training data sets using SlicerAIGT extension’s “Single Slice Segmentation” module (it is specifically developed for ultrasound image sequence segmentation). I think there are a number of examples for ultrasound segmentation networks in the <a href="https://github.com/SlicerIGT/aigt">extension’s repository</a>.</p>
<p>Do you track your ultrasound probe (e.g., using an optical or electromagnetic tracker)? If not yet, then you can use <a href="http://plustoolkit.org/">Plus toolkit</a> for that. It integrates nicely with 3D Slicer.</p>

---

## Post #3 by @adrianoderosa (2022-11-30 16:35 UTC)

<aside class="quote no-group" data-username="whu" data-post="1" data-topic="25767">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/7ab992/48.png" class="avatar"> whu:</div>
<blockquote>
<p>SimVascular</p>
</blockquote>
</aside>
<p>Dear Andras, I’m new to 3d slice, where can I find a tutorial to create the training dataset for segmentation unet?<br>
Thank you in advance<br>
Adriano</p>

---
