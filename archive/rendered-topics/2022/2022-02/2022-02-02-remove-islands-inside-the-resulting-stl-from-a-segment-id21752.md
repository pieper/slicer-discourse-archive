---
topic_id: 21752
title: "Remove Islands Inside The Resulting Stl From A Segment"
date: 2022-02-02
url: https://discourse.slicer.org/t/21752
---

# Remove islands inside the resulting STL from a segment

**Topic ID**: 21752
**Date**: 2022-02-02
**URL**: https://discourse.slicer.org/t/remove-islands-inside-the-resulting-stl-from-a-segment/21752

---

## Post #1 by @anon29823344 (2022-02-02 13:24 UTC)

<p>Operating system: Windows 10 Pro. Version: 21H2. Build: 19044.1466<br>
Slicer version: 4.11.20210226 r29738 / 7a593c8</p>
<p>Hello all.</p>
<p>This is my first question in the forum, so I hope this topic is not repeated (at least I couldn’t find it).</p>
<p>I need to solve a problem that I found during multiple segmentation tasks of CBCT dental scans by using the Segment Editor module. In particular, I am segmenting the teeth, mandible and the maxilla, and inside all of them, there are multiple “islands” that I can’t remove with the Islands method. I tried the following:<br>
- remove islands smaller than a fixed number of voxels (with different voxel sizes),<br>
- keep the largest island (both for mandible and maxilla),<br>
- split islands into segments,<br>
but in any case, I could not remove these parts.</p>
<p>I attach some images of that problem (images are snapshots from MeshLab software due to I don’t know how I can see those islands with slicer in an easy way) where I hope you can see the islands inside the STL resulting from the segmentations done.</p>
<p>Can somebody help me with this problem? How can I remove these islands inside the STL? These islands are really considered “islands” by Slicer? Is there a way to check them in Slicer instead of using MeshLab or other software?</p>
<p>I take this opportunity to ask the Slicer community what methodology each of you uses to segment these types of images, with the goal of both improving my work and contributing to a piece of shared knowledge in this type of segmentation. In my case, I use to apply a Grow From Seeds for tooth segmentation but it is a very rough segmentation and I have to invest a lot of time in debugging it. For the jaw segmentation, I usually apply a threshold between the maximum value of HU and a value around 500 HU, this way I remove the air and much of the soft tissue and then, after manual cleaning, I subtract the segmentation made by the teeth. If you want I can upload photos of how I do it.</p>
<p>I hope I have explained it well. Thanks in advance for your time.</p>
<p>Best regards.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/051cb2aef4ae0a160b0a2057c08eaf47989f1da6.jpeg" data-download-href="/uploads/short-url/JdS5S4y1AG10gIuSoVBXmtKBSu.jpeg?dl=1" title="snapshot-2-3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/051cb2aef4ae0a160b0a2057c08eaf47989f1da6_2_690x183.jpeg" alt="snapshot-2-3" data-base62-sha1="JdS5S4y1AG10gIuSoVBXmtKBSu" width="690" height="183" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/051cb2aef4ae0a160b0a2057c08eaf47989f1da6_2_690x183.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/051cb2aef4ae0a160b0a2057c08eaf47989f1da6_2_1035x274.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/051cb2aef4ae0a160b0a2057c08eaf47989f1da6_2_1380x366.jpeg 2x" data-dominant-color="AA818B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">snapshot-2-3</span><span class="informations">2732×725 337 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bb11eb2c98fe461cd6bcc381d11a73c0fba97eca.jpeg" data-download-href="/uploads/short-url/qGTG0jVcGURannxOUG2vwa2pfoC.jpeg?dl=1" title="snapshot-4-5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb11eb2c98fe461cd6bcc381d11a73c0fba97eca_2_690x183.jpeg" alt="snapshot-4-5" data-base62-sha1="qGTG0jVcGURannxOUG2vwa2pfoC" width="690" height="183" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb11eb2c98fe461cd6bcc381d11a73c0fba97eca_2_690x183.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb11eb2c98fe461cd6bcc381d11a73c0fba97eca_2_1035x274.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bb11eb2c98fe461cd6bcc381d11a73c0fba97eca_2_1380x366.jpeg 2x" data-dominant-color="A27E8C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">snapshot-4-5</span><span class="informations">2728×727 297 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a02d68de1b8669289ddbd0a56c1b1cb831dc4251.jpeg" data-download-href="/uploads/short-url/mQZGt2HnHjDydEoVaPsS7IxstH3.jpeg?dl=1" title="snapshot-6-8" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a02d68de1b8669289ddbd0a56c1b1cb831dc4251_2_690x184.jpeg" alt="snapshot-6-8" data-base62-sha1="mQZGt2HnHjDydEoVaPsS7IxstH3" width="690" height="184" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a02d68de1b8669289ddbd0a56c1b1cb831dc4251_2_690x184.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a02d68de1b8669289ddbd0a56c1b1cb831dc4251_2_1035x276.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a02d68de1b8669289ddbd0a56c1b1cb831dc4251_2_1380x368.jpeg 2x" data-dominant-color="8C85A3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">snapshot-6-8</span><span class="informations">2726×727 270 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eeb23cb169f4814881a9f652c6f67fea9cf2a407.png" data-download-href="/uploads/short-url/y3BvzbGLvNL7EVJDqpvS9ikxG0D.png?dl=1" title="snapshot-9" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eeb23cb169f4814881a9f652c6f67fea9cf2a407_2_690x367.png" alt="snapshot-9" data-base62-sha1="y3BvzbGLvNL7EVJDqpvS9ikxG0D" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eeb23cb169f4814881a9f652c6f67fea9cf2a407_2_690x367.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/e/eeb23cb169f4814881a9f652c6f67fea9cf2a407_2_1035x550.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/eeb23cb169f4814881a9f652c6f67fea9cf2a407.png 2x" data-dominant-color="8783A2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">snapshot-9</span><span class="informations">1365×727 81.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/dbd7848ec3b61cb14e07b337013c59131cd0f833.png" alt="snapshot-10" data-base62-sha1="vmOjgGA3vE3F0daD3gCUJZlbPID" width="407" height="307"></p>

---

## Post #2 by @mikebind (2022-02-03 00:07 UTC)

<p>If these “islands” are truly disconnected from the rest of the segment, then Slicer’s Islands tool should remove them.  However, it is sometimes the case that there are small regions which are connected via a very thin bridge to the rest of the segment.  These do not count as separate islands because they maintain a connection.  However, when exporting to STL or viewing in 3D, there is typically some smoothing applied, and this smoothing can have the effect of eliminating the small bridge in the 3D visualization or the exported mesh.  Thus the mesh can have islands which are not truly islands in the segmentation it is generated from.  These will not be identified by the Islands tool because they are not islands in the segmentation.</p>
<p>What can you do about this?  There are multiple approaches you could take which come to mind.  Which is best will depend on your images and your segmentation goals.</p>
<ul>
<li>You could smooth the images (e.g. with a median filter) to make them less noisy before segmentation</li>
<li>You could smooth the segment using the “Smoothing” tool in segment editor after your initial threshold segmentation.  You could try this with either a “Median” smoothing or with an “Opening” smoothing.  “Opening” will perform a morphological erosion followed by a morphological dilation with the net effect of removing structures smaller than the kernel size while maintaining larger structures.</li>
</ul>
<p>If I were in your position, I would probably start by trying the second approach using “Opening”, followed by keeping the largest island, and see how that looks.</p>
<aside class="quote no-group" data-username="anon29823344" data-post="1" data-topic="21752">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/7bcc69/48.png" class="avatar"> anon29823344:</div>
<blockquote>
<p>Is there a way to check them in Slicer instead of using MeshLab or other software?</p>
</blockquote>
</aside>
<p>It looks from your last screenshot like you eventually had some success seeing the segment structure in 3D in Slicer.  If you want the 3D surface to be transparent, you can control that in the “Display” section of the “Segmentations” module, using the 3D visibility opacity slider.</p>

---

## Post #3 by @mikebind (2022-02-03 01:13 UTC)

<p>One way to check whether smoothing is giving rise to the islands is to turn off smoothing and see if those regions are connected in that case.  You can turn of smoothing by going to the “Segmentations” module, and in the “Representations” section, next to “Closed Surface”, click the “Update” button, which will open another window:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b11fe503975a5704635657c743a399619ca3d5d1.png" data-download-href="/uploads/short-url/pgUQsquQmXl68H41M30EB6SgPrr.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b11fe503975a5704635657c743a399619ca3d5d1_2_690x468.png" alt="image" data-base62-sha1="pgUQsquQmXl68H41M30EB6SgPrr" width="690" height="468" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b11fe503975a5704635657c743a399619ca3d5d1_2_690x468.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b11fe503975a5704635657c743a399619ca3d5d1_2_1035x702.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b11fe503975a5704635657c743a399619ca3d5d1_2_1380x936.png 2x" data-dominant-color="D4D5D6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2606×1768 254 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
In that window, click on the path, and then on the “Smoothing factor” in the conversion parameters, and change the smoothing factor to 0.   Then click the “Convert” button to generate a mesh with no smoothing applied.</p>

---
