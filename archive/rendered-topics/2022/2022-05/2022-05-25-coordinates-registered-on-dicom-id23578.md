---
topic_id: 23578
title: "Coordinates Registered On Dicom"
date: 2022-05-25
url: https://discourse.slicer.org/t/23578
---

# Coordinates registered on DICOM

**Topic ID**: 23578
**Date**: 2022-05-25
**URL**: https://discourse.slicer.org/t/coordinates-registered-on-dicom/23578

---

## Post #1 by @Takahashi (2022-05-25 01:43 UTC)

<p>I want to integrate the coordinates acquired by 3DSlicer and Checkpoint software (Stratovan) in one file.<br>
Before integrating, I checked the coherence of coordinates for several anatomical landmarks registered with the two software. Then, they were completely different from each other, both in value and the plus/minus sign.</p>
<p>Both were registered on the same DICOM data, not STL.<br>
In 3DSlicer, I used “load DICOM” to import data.</p>
<p>Do you have any idea for the reason and any resolution?<br>
Do they have the different coordinate system? or, should I take another process when importing DICOM data?</p>
<p>Operating system: Mac OS<br>
Slicer version: 4.11</p>
<p>Thank you in advance,</p>

---

## Post #2 by @muratmaga (2022-05-25 03:06 UTC)

<aside class="quote no-group" data-username="Takahashi" data-post="1" data-topic="23578">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/f1d935/48.png" class="avatar"> Takahashi:</div>
<blockquote>
<p>Before integrating, I checked the coherence of coordinates for several anatomical landmarks registered with the two software. Then, they were completely different from each other, both in value and the plus/minus sign.</p>
</blockquote>
</aside>
<p>I do not now what coordinate system Checkpoint uses. You need to get that information from them. Slicer internally uses RAS coordinates, while DICOM uses LPS (as far as I know). That transformation is simply  a sign (but not a value) difference in the first two axis. So a point at 100,100,100 recorded under RAS should would be equivalent to -100, -100, 100 in LPS.</p>
<p>If your data was imported into Slicer through the DICOM module, and no error/warning was generated you shouldn’t really need any other modification.</p>

---

## Post #3 by @Takahashi (2022-05-25 07:25 UTC)

<p>Thank you for your reply.</p>
<p>My data was imported into Slicer through DICOM module.<br>
I heard before that the data is imported into a different morpho-space when it is imported through “load DICOM” , and through “load data” with unchecked of “single file”.</p>
<p>Do you have any idea for the effect on the coordinates?</p>
<p>Thank you.</p>

---

## Post #4 by @pieper (2022-05-25 12:07 UTC)

<p>I agree with <a class="mention" href="/u/muratmaga">@muratmaga</a>, Slicer’s coordinates are well defined and you can easily understand them with a little research.  I don’t know Checkpoint, but for any commercial software you are dependent on the vendor to define and explain their conventions.  If they don’t, well, you are stuck reverse engineering.</p>
<p><a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Coordinate_systems</a></p>

---

## Post #5 by @lassoan (2022-05-25 12:20 UTC)

<p>You could post screenshots of both Slicer and Checkpoint that shows how they display the coordinates. For example, it is possible that you compare voxel coordinates to physical coordinates.</p>

---

## Post #6 by @muratmaga (2022-05-25 15:54 UTC)

<aside class="quote no-group" data-username="Takahashi" data-post="3" data-topic="23578">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/f1d935/48.png" class="avatar"> Takahashi:</div>
<blockquote>
<p>I heard before that the data is imported into a different morpho-space when it is imported through “load DICOM” , and through “load data” with unchecked of “single file”.</p>
</blockquote>
</aside>
<p>That was in quite older versions. If you were working with DICOMs, you should use the DICOM module to import data into Slicer.</p>

---

## Post #7 by @Takahashi (2022-05-26 12:18 UTC)

<p>Thank you for sharing.<br>
As <a class="mention" href="/u/lassoan">@lassoan</a> suggested, I’m preparing for share the screenshots.</p>
<p>I think that the differences could come from XYZ and RAS coordinate systems.<br>
(It may be a basic inquiry, but is it right that XYZ is voxel coordinates and RAS is physical coordinates?)<br>
Does Slicer have any modules or programs to transform coordinates from RAS to XYZ?</p>

---

## Post #8 by @Takahashi (2022-05-27 04:32 UTC)

<p>Here I attached the screenshots of both Slicer and Checkpoint software.<br>
Sample names are concealed with black boxes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/662a228ade8a5d2a1963b6f4489313d236cb8e40.jpeg" data-download-href="/uploads/short-url/ezMYur8hFfvqLa7FD12AyraSYlG.jpeg?dl=1" title="Checkpoint" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/662a228ade8a5d2a1963b6f4489313d236cb8e40_2_690x397.jpeg" alt="Checkpoint" data-base62-sha1="ezMYur8hFfvqLa7FD12AyraSYlG" width="690" height="397" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/662a228ade8a5d2a1963b6f4489313d236cb8e40_2_690x397.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/662a228ade8a5d2a1963b6f4489313d236cb8e40_2_1035x595.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/662a228ade8a5d2a1963b6f4489313d236cb8e40_2_1380x794.jpeg 2x" data-dominant-color="929292"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Checkpoint</span><span class="informations">1920×1105 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5f429c29d7b20ce139ef5d75ce0e3aad50145306.png" data-download-href="/uploads/short-url/dAI4oSvuAfXFXsFcx6YM4oP4sTQ.png?dl=1" title="Checkpoint_export_landmarks" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f429c29d7b20ce139ef5d75ce0e3aad50145306_2_690x402.png" alt="Checkpoint_export_landmarks" data-base62-sha1="dAI4oSvuAfXFXsFcx6YM4oP4sTQ" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f429c29d7b20ce139ef5d75ce0e3aad50145306_2_690x402.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f429c29d7b20ce139ef5d75ce0e3aad50145306_2_1035x603.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5f429c29d7b20ce139ef5d75ce0e3aad50145306_2_1380x804.png 2x" data-dominant-color="E2E2E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Checkpoint_export_landmarks</span><span class="informations">1645×960 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06d314dca12c5d01106c2c75f51c4176245390f9.jpeg" data-download-href="/uploads/short-url/Yn6uYxSCATCqOe9GlN39idJ0kV.jpeg?dl=1" title="Slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06d314dca12c5d01106c2c75f51c4176245390f9_2_690x431.jpeg" alt="Slicer" data-base62-sha1="Yn6uYxSCATCqOe9GlN39idJ0kV" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06d314dca12c5d01106c2c75f51c4176245390f9_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06d314dca12c5d01106c2c75f51c4176245390f9_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06d314dca12c5d01106c2c75f51c4176245390f9_2_1380x862.jpeg 2x" data-dominant-color="A19FA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer</span><span class="informations">1920×1201 201 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @muratmaga (2022-05-27 20:38 UTC)

<p>Given the checkpoint reports landmarks in hundreds range, those are likely IJK coordinates of the voxel data. Slicer always report in the physical coordinates (in this case RAS) converting those to millimeters. If you expand the data probe module (where you covered the subject name), you will see those as well, when you hover your mice over that point (see below)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db2687fc7656c0104983f53a4bbc999d9ffe4f6c.png" data-download-href="/uploads/short-url/vgH7mpTtPiZk1ilfmgIWfPkFB24.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db2687fc7656c0104983f53a4bbc999d9ffe4f6c_2_690x118.png" alt="image" data-base62-sha1="vgH7mpTtPiZk1ilfmgIWfPkFB24" width="690" height="118" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/b/db2687fc7656c0104983f53a4bbc999d9ffe4f6c_2_690x118.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db2687fc7656c0104983f53a4bbc999d9ffe4f6c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db2687fc7656c0104983f53a4bbc999d9ffe4f6c.png 2x" data-dominant-color="E8E8E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">719×123 21.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @lassoan (2022-05-27 22:49 UTC)

<p><a class="mention" href="/u/takahashi">@Takahashi</a> Could you place your landmark points in Checkpoint in the 8 corners of the image cube? From those coordinates most likely we can tell what coordinate system that software is using.</p>
<p>By the way, is there any specific reason for using the Checkpoint software instead of 3D Slicer?</p>

---

## Post #11 by @Takahashi (2022-05-30 06:22 UTC)

<p>Thanks.<br>
Do you mean that the values shown in the line “B” indicates IJK coordinates?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/760f4a18c5c04181753ff9620c7694262266cb02.jpeg" data-download-href="/uploads/short-url/gQp68vEAIzbjCJ7xULkdoC4VnuG.jpeg?dl=1" title="2022-05-30 15.16.25" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/760f4a18c5c04181753ff9620c7694262266cb02_2_690x408.jpeg" alt="2022-05-30 15.16.25" data-base62-sha1="gQp68vEAIzbjCJ7xULkdoC4VnuG" width="690" height="408" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/760f4a18c5c04181753ff9620c7694262266cb02_2_690x408.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/760f4a18c5c04181753ff9620c7694262266cb02_2_1035x612.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/760f4a18c5c04181753ff9620c7694262266cb02_2_1380x816.jpeg 2x" data-dominant-color="A7A7AD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2022-05-30 15.16.25</span><span class="informations">1920×1138 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @Takahashi (2022-05-30 06:37 UTC)

<p>Thank you for your recommend.<br>
Could  you tell the difference in the coordinates system by this image?<br>
(Points 4-11 are eight corners landmarks)</p>
<p>I wish I could register the whole landmarks by Slicer, but we have more than a hundred of coordinates acquired by Checkpoint and we want to use them again in a new study. Now, we want to add landmarks which can be acquired only by Slicer in addition to previous landmarks.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12b5f90e9321de711650fb1ce943372b9375aee0.png" data-download-href="/uploads/short-url/2Fwt6ZT8gltKZJpYlVJWGA24E9i.png?dl=1" title="8points_landmarks_checkpoint" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12b5f90e9321de711650fb1ce943372b9375aee0.png" alt="8points_landmarks_checkpoint" data-base62-sha1="2Fwt6ZT8gltKZJpYlVJWGA24E9i" width="288" height="500" data-dominant-color="DBDBDB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">8points_landmarks_checkpoint</span><span class="informations">492×853 24 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #13 by @muratmaga (2022-05-30 17:55 UTC)

<p>Yes, but it represents the IJK coordinates of the voxel where mouse is pointing at (You can see that RAS values are not identical to your F-1 point). You should be able to write a little script which will convert RAS coordinates to IJK.</p>
<p>However, my suggestion would have been to use Slicer for everything. so Instead trying to migrate Slicer data to checkpoint, migrate checkpoint coordinates to Slicer once and for all, and continue your data collection and do your analysis in Slicer.</p>

---

## Post #14 by @lassoan (2022-05-30 19:16 UTC)

<p>These are the 8 corner coordinates in the screenshot above:</p>
<pre><code class="lang-auto">4	44.2	-78.9	24.4
5	44.3	-78.9	-44.8
6	202.3	-78.9	-45.5
7	202.3	-78.1	24.5
8	44.4	151	24.5
9	45.4	150	-45.5
10	202	151	-45.5
11	202	151	24.5
</code></pre>
<p>These look like anatomical coordinates in millimeters.</p>
<p>Could you mark these points (in the same order) in 3D Slicer as well and copy-paste them here to see what the relationship is between them? Please do not copy screenshot but go to Markups module, Control points section, select all the rows in the table, hit Ctrl-C to copy the coordinates to the clipboard; you can then paste that into your Slicer forum post.</p>

---

## Post #15 by @Takahashi (2022-06-01 05:11 UTC)

<p>Here are the eight corner coordinates in 3DSlicer.</p>
<ul>
<li>
4  -26.00  -79.46  78.44</li>
<li>5   44.37  -79.01   80.10</li>
<li>6	  43.36	  79.10	  80.10</li>
<li>7	   -27.01	  78.66	  78.44</li>
<li>8   -20.57   -79.43   -151.27</li>
<li>9	  49.815	  -78.98	  -149.61</li>
<li>10	  48.80	  79.14	  -149.61</li>
<li>11	  -21.587	  78.69	  -151.27
</li>
</ul>

---

## Post #16 by @Takahashi (2022-06-01 05:22 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="13" data-topic="23578">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>You should be able to write a little script which will convert RAS coordinates to IJK.</p>
</blockquote>
</aside>
<p>Sould I run the script using Slicer, or any other software like MATLAB or R?</p>
<p>Or, if I may migrate checkpoint coordinates to Slicer, is there any script to convert IJK coordinates to RAS?</p>

---

## Post #17 by @Takahashi (2022-06-02 11:47 UTC)

<p>I apologize for late response.<br>
Here are the eight corner coordinates in 3DSlicer.</p>
<pre><code class="lang-auto">4	-26.00  -79.46  78.44
5	44.37  -79.01   80.10
6	43.36   79.10   80.10
7	-27.01   78.66   78.44
8	49.815   -78.98   -149.61
9	49.815   -78.98   -149.61
10	48.80   79.14   -149.61
11	-21.587   78.69   -151.27
</code></pre>
<p>I hope this could be helpful for understanding the relationship of two landmarks.<br>
Any ideas would be appreciated. Thank you.</p>

---
