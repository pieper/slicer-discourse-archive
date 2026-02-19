---
topic_id: 2428
title: "Save Segmentation Directly To Stl Or Obj Files"
date: 2018-03-26
url: https://discourse.slicer.org/t/2428
---

# Save segmentation directly to STL or OBJ files

**Topic ID**: 2428
**Date**: 2018-03-26
**URL**: https://discourse.slicer.org/t/save-segmentation-directly-to-stl-or-obj-files/2428

---

## Post #1 by @lassoan (2018-03-26 16:14 UTC)

<p>We often received questions about how to export segmentation to STL file for 3D printing. We’ve added a simplified, dedicated tool to make this step easier.</p>
<p>1-minute demo video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="WfuYPVYA5cA" data-video-title="Export Slicer image segmentation to STL or OBJ file" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=WfuYPVYA5cA" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/WfuYPVYA5cA/maxresdefault.jpg" title="Export Slicer image segmentation to STL or OBJ file" width="" height="">
  </a>
</div>

<p>Main features:</p>
<ul>
<li>Export STL file: each segment as a separate file or all segments merged into a single mesh</li>
<li>Export OBJ file: all segments are saved in one file, segment colors and opacities are preserved</li>
<li>Export all or visible segments only</li>
<li>Coordinate system can be LPS (for compatibility external software) or RAS (for compatibility with current default model save in Slicer)</li>
</ul>
<p>The tool is available in Segment editor module (“Segmentations” button / drop-down arrow / “Export to files”) and in Segmentations module (“Export to files” section).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b9e77aace22e8fdd5d5ce55e5c3aca9e6755564.png" alt="image" data-base62-sha1="8vpGvQ4s5LG6ymMZLSNYn5MFJ3u" width="601" height="418"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b84e7fe940c2694661735669be71fb9848de5e8.png" alt="image" data-base62-sha1="mbML0wphMPH9dQ8R2smJo2ywDos" width="346" height="210"></p>

---

## Post #2 by @J_Scales (2018-03-26 18:01 UTC)

<p>Out of interest in the video what is viewer you are using for STL visualization?</p>
<p>Ah found it, Mixed Reality viewer for Windows 10.</p>

---

## Post #3 by @labixin (2019-01-16 07:18 UTC)

<p>Dear Andras,</p>
<p>I have succeeded in exporting all segments together in one file. But I still have two questions. The first is about exporting STL file. What do you mean by “all segments merged into a single mesh” when ticked the box “Merge into single file”? Does the single mesh still compose of different segments or just merge into one mesh? I have export STL file to Solidworks and found three parts the same in Slicer (as shown in the following figure). The second is that when exporting OBJ file, I found another solid apart from the three segments (a very small spot??). I really don’t know where it may be from. Could you give some advice? Thank you very much!</p>
<p>Best regards,<br>
Crayon<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/520930821fd6ae183ca4e5666fb9fa76ca6d8bd9.jpeg" data-download-href="/uploads/short-url/bHIQ8E1EqmQ2hzKinKX8PjlT5s5.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/520930821fd6ae183ca4e5666fb9fa76ca6d8bd9_2_689x360.jpeg" alt="2" data-base62-sha1="bHIQ8E1EqmQ2hzKinKX8PjlT5s5" width="689" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/520930821fd6ae183ca4e5666fb9fa76ca6d8bd9_2_689x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/520930821fd6ae183ca4e5666fb9fa76ca6d8bd9_2_1033x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/520930821fd6ae183ca4e5666fb9fa76ca6d8bd9.jpeg 2x" data-dominant-color="6E6F74"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1268×663 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2019-01-16 12:51 UTC)

<aside class="quote no-group" data-username="labixin" data-post="3" data-topic="2428">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>What do you mean by “all segments merged into a single mesh” when ticked the box “Merge into single file”?</p>
</blockquote>
</aside>
<p>If merge is enabled then all mesh points and triangles of the three segments are included in a single file. If you want to manage the segments separately then turn off this option.</p>
<aside class="quote no-group" data-username="labixin" data-post="3" data-topic="2428">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/labixin/48/1965_2.png" class="avatar"> labixin:</div>
<blockquote>
<p>I really don’t know where it may be from. Could you give some advice?</p>
</blockquote>
</aside>
<p>If you did not intend to create that segment and don’t need it then you can delete it.</p>

---

## Post #5 by @labixin (2019-01-16 13:12 UTC)

<p>I got it. Thank you!</p>

---

## Post #6 by @lassoan (2021-03-14 14:10 UTC)

<p>2 posts were split to a new topic: <a href="/t/keep-dicom-coordinate-system-when-exporting-segmentation/16533">Keep DICOM coordinate system when exporting segmentation</a></p>

---

## Post #7 by @rjk (2021-04-15 08:35 UTC)

<p>Newbie here requesting a hand:</p>
<p>I exported using “export segments to files” a segmentation of several structures, with color and opacity set for each, into a merged OBJ but upon loading it back into Slicer none of the color and opacity settings were preserved. The entire model was default yellow. Additionally, when I tried to scale the size down for the sake of storage space, but whether the slider is 1 or 0.3 the output file size remains the same.</p>
<p>Any advice for these 2 newbie issues? Thanks!</p>

---

## Post #8 by @rbumm (2021-04-15 10:55 UTC)

<p>This is a great new function. Thank you !</p>

---

## Post #9 by @lassoan (2021-04-15 12:33 UTC)

<aside class="quote no-group" data-username="rjk" data-post="7" data-topic="2428">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/ed655f/48.png" class="avatar"> rjk:</div>
<blockquote>
<p>I exported using “export segments to files” a segmentation of several structures, with color and opacity set for each, into a merged OBJ but upon loading it back into Slicer none of the color and opacity settings were preserved. The entire model was default yellow. Additionally, when I tried to scale the size down for the sake of storage space, but whether the slider is 1 or 0.3 the output file size remains the same.</p>
</blockquote>
</aside>
<p>“Export to files” feature is for exporting for 3D printing or visualization/processing in external software. If you want to preserve colors and all other display properties then save the segmentation using File / Save.</p>
<p>When an OBJ file is loaded into Slicer then the texture/color information is ignored but the <code>MaterialIds</code> cell array is made available in the mesh. This array contains a different value for each segment, and you can choose to use this value for coloring in Models module’s Scalars section. If you choose a color table that matches the original segment colors then you can make the model appear similarly as it was exported.</p>
<aside class="quote no-group" data-username="rjk" data-post="7" data-topic="2428">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/ed655f/48.png" class="avatar"> rjk:</div>
<blockquote>
<p>Additionally, when I tried to scale the size down for the sake of storage space, but whether the slider is 1 or 0.3 the output file size remains the same</p>
</blockquote>
</aside>
<p>This feature is for scaling of coordinates (for example, if you want to have your model coordinates to be defined in meters instead of millimeters). You can find explanation of all parameters in tooltips.</p>

---
