---
topic_id: 36260
title: "Display Gridlines"
date: 2024-05-19
url: https://discourse.slicer.org/t/36260
---

# Display gridlines

**Topic ID**: 36260
**Date**: 2024-05-19
**URL**: https://discourse.slicer.org/t/display-gridlines/36260

---

## Post #1 by @YLX (2024-05-19 11:05 UTC)

<p>Hello, I would like to know how to display gridlines in 3d slice software? Because I want to measure some of the lowest and highest points of the skull, after importing the skull data, there will be a large error due to subjectivity. So I would like to know if it is possible to add grid lines in the display interface to help me locate the landmarks I need more accurately.</p>
<p>Operating system:<br>
Slicer version: 5.6.1<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @philippepellerin (2024-05-19 15:00 UTC)

<p>create a transform, then display the grid(in the transform module)</p>

---

## Post #3 by @Tina_Kapur (2024-05-20 01:13 UTC)

<p>Please see this thread and let us know if it is helpful to you in making measurements and solving your problem:</p><aside class="quote quote-modified" data-post="1" data-topic="29127">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/q2577040659/48/16942_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/create-gridlines-in-3d-view-similar-to-the-effect-in-the-figure/29127/1">Create gridlines in 3D view, similar to the effect in the figure</a> <a class="badge-category__wrapper " href="/c/support/feature-requests/9"><span data-category-id="9" style="--category-badge-color: #F1592A; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #3AB54A;" data-parent-category-id="11" data-drop-close="true" class="badge-category --has-parent" title="This category is for submitting ideas about what enhancements or new features should be added to 3D Slicer. Make your voice heard by voting on feature requests - by opening the topic and clicking the Vote button or by creating a new topics. Slicer developers will make it a priority to work on feature requests that have more votes."><span class="badge-category__name">Feature requests</span></span></a>
  </div>
  <blockquote>
    <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/20d7a99cda47addfd7a196c9e87b2f6911004c97.png" data-download-href="/uploads/short-url/4GxkHEig6Ixy2T7FlEkJZsb9Rxt.png?dl=1" title="Snipaste_2023-04-26_10-33-11" rel="noopener nofollow ugc">[Snipaste_2023-04-26_10-33-11]</a>
  </blockquote>
</aside>


---

## Post #4 by @YLX (2024-05-20 02:55 UTC)

<p>Thank you for the method provided by the teacher. I tried the python code in the link and found that there seemed to be a grid in the three views below, but the main picture still did not show the grid I wanted. Also, I would like to ask how to add mesh customization for Slicermorpho?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/5688e3125e1d15fa114d88c7a139c19d732360ca.jpeg" data-download-href="/uploads/short-url/clwlaJlOksIOGJLorQAC7xZ8JbY.jpeg?dl=1" title="8N6YVI$J%DBG(2OOW$MRAAK" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5688e3125e1d15fa114d88c7a139c19d732360ca_2_690x373.jpeg" alt="8N6YVI$J%DBG(2OOW$MRAAK" data-base62-sha1="clwlaJlOksIOGJLorQAC7xZ8JbY" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5688e3125e1d15fa114d88c7a139c19d732360ca_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5688e3125e1d15fa114d88c7a139c19d732360ca_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5688e3125e1d15fa114d88c7a139c19d732360ca_2_1380x746.jpeg 2x" data-dominant-color="B9B9C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">8N6YVI$J%DBG(2OOW$MRAAK</span><span class="informations">1920×1040 248 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @YLX (2024-05-20 03:09 UTC)

<p>To add a point, I am importing data in stl format for operation</p>

---

## Post #6 by @philippepellerin (2024-05-21 09:09 UTC)

<p>By using the transform module( ceate a new transform for your volume) you will display a grid in 3D as well as in 2D. The grid is fully parametrable and can, even be moved itself by a second transform, see the screen grabs<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f811de330d784465beda09c82c9bf9f74b6f2b02.jpeg" data-download-href="/uploads/short-url/zowH45JEQgbv5qyF0M7g2uNcaH0.jpeg?dl=1" title="Screenshot 2024-05-21 at 10.52.57" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f811de330d784465beda09c82c9bf9f74b6f2b02_2_657x500.jpeg" alt="Screenshot 2024-05-21 at 10.52.57" data-base62-sha1="zowH45JEQgbv5qyF0M7g2uNcaH0" width="657" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f811de330d784465beda09c82c9bf9f74b6f2b02_2_657x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f811de330d784465beda09c82c9bf9f74b6f2b02_2_985x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f811de330d784465beda09c82c9bf9f74b6f2b02_2_1314x1000.jpeg 2x" data-dominant-color="9C97A3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-21 at 10.52.57</span><span class="informations">1920×1459 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/573d3dd1583cff95f45962dfb7d506de8a8e1f09.jpeg" data-download-href="/uploads/short-url/crKKrRRe92bUjIFnOBpwl8r0N9D.jpeg?dl=1" title="Screenshot 2024-05-21 at 10.53.23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/573d3dd1583cff95f45962dfb7d506de8a8e1f09_2_657x500.jpeg" alt="Screenshot 2024-05-21 at 10.53.23" data-base62-sha1="crKKrRRe92bUjIFnOBpwl8r0N9D" width="657" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/573d3dd1583cff95f45962dfb7d506de8a8e1f09_2_657x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/573d3dd1583cff95f45962dfb7d506de8a8e1f09_2_985x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/573d3dd1583cff95f45962dfb7d506de8a8e1f09_2_1314x1000.jpeg 2x" data-dominant-color="9C97A4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-21 at 10.53.23</span><span class="informations">1920×1459 197 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb1051604b21e9f70628a66751e33556967950bd.jpeg" data-download-href="/uploads/short-url/xxtajNXirsHkoMOCtFFWUCyrwYJ.jpeg?dl=1" title="Screenshot 2024-05-21 at 10.53.42" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb1051604b21e9f70628a66751e33556967950bd_2_657x500.jpeg" alt="Screenshot 2024-05-21 at 10.53.42" data-base62-sha1="xxtajNXirsHkoMOCtFFWUCyrwYJ" width="657" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb1051604b21e9f70628a66751e33556967950bd_2_657x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb1051604b21e9f70628a66751e33556967950bd_2_985x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/b/eb1051604b21e9f70628a66751e33556967950bd_2_1314x1000.jpeg 2x" data-dominant-color="95919B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-05-21 at 10.53.42</span><span class="informations">1920×1459 256 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @cpinter (2024-05-21 09:31 UTC)

<aside class="quote no-group" data-username="YLX" data-post="4" data-topic="36260">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/y/c57346/48.png" class="avatar"> YLX:</div>
<blockquote>
<p>I tried the python code in the link and found that there seemed to be a grid in the three views below, but the main picture still did not show the grid</p>
</blockquote>
</aside>
<p>The code works, I just tried. If you paid attention you saw in the console and the log that you need to switch to parallel projection.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29dbda985a2b6654e3f398616684b292521fd5d4.png" data-download-href="/uploads/short-url/5YiBSWWkVyNb19CapcGB6GRscLi.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/29dbda985a2b6654e3f398616684b292521fd5d4.png" alt="image" data-base62-sha1="5YiBSWWkVyNb19CapcGB6GRscLi" width="689" height="500" data-dominant-color="9295C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">741×537 15.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @YLX (2024-05-22 03:16 UTC)

<p>Thank you very much for your guidance. I followed your method, but there was another problem. When I selected the Regin option, the screen flashed back, is it the cause of my computer’s low configuration?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57e67fa2f480288b4a21ec5723c2a24600ff090c.png" data-download-href="/uploads/short-url/cxBnC1wyKToV6UzUktTAVEoNWJ6.png?dl=1" title="OI@6W5W8@2E%0@THCGCO06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57e67fa2f480288b4a21ec5723c2a24600ff090c_2_690x373.png" alt="OI@6W5W8@2E%0@THCGCO06" data-base62-sha1="cxBnC1wyKToV6UzUktTAVEoNWJ6" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57e67fa2f480288b4a21ec5723c2a24600ff090c_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57e67fa2f480288b4a21ec5723c2a24600ff090c_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57e67fa2f480288b4a21ec5723c2a24600ff090c_2_1380x746.png 2x" data-dominant-color="6B6B5F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">OI@6W5W8@2E%0@THCGCO06</span><span class="informations">1920×1040 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e293e7d8da682a0c2cba6634677676741f2e603.jpeg" data-download-href="/uploads/short-url/mz9NW0StVkOXQKcxeu0QzZmkhIT.jpeg?dl=1" title="f9530fdabaaca4451295a1155f1482bc" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e293e7d8da682a0c2cba6634677676741f2e603_2_666x500.jpeg" alt="f9530fdabaaca4451295a1155f1482bc" data-base62-sha1="mz9NW0StVkOXQKcxeu0QzZmkhIT" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e293e7d8da682a0c2cba6634677676741f2e603_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e293e7d8da682a0c2cba6634677676741f2e603_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e293e7d8da682a0c2cba6634677676741f2e603_2_1332x1000.jpeg 2x" data-dominant-color="959594"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">f9530fdabaaca4451295a1155f1482bc</span><span class="informations">1920×1440 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @YLX (2024-05-22 03:19 UTC)

<p>Thank you very much for your guidance, I would like to ask how to customize the code? Is that I open any data, do not need to re-enter the code, can directly use custom options, so as to set up a grid display?</p>

---
