# Threshold range in 3D Slicer is [0, 99]

**Topic ID**: 7760
**Date**: 2019-07-25
**URL**: https://discourse.slicer.org/t/threshold-range-in-3d-slicer-is-0-99/7760

---

## Post #1 by @mli (2019-07-25 18:21 UTC)

<p>Hi guys,</p>
<p>I am trying to segment CT image. The data format is .nrrd and I can import it to Slicer successfully. I checked the import data and the voxel value is HU, which is from about -1000 to 1000.</p>
<p>However, when I use the Threshold feature in Segment Editor, the threshold range is limited to [0, 99], and I can not change it. I also tried to choose different Automatic Threshold (auto-&gt;maximum, minimum-&gt;auto, as lower, as upper), but it does not make any change.</p>
<p>I am a new user to Slicer. Am I missing something? Any suggestions are greatly appreciated. Thank you very much!</p>
<p>Best regards,<br>
Mohan</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69eee0402089aaa91914001e319c12416dd40b1f.jpeg" data-download-href="/uploads/short-url/f77VhalHTzWgnqnrHsqrc5TE3RJ.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/69eee0402089aaa91914001e319c12416dd40b1f_2_690x325.jpeg" alt="PNG" data-base62-sha1="f77VhalHTzWgnqnrHsqrc5TE3RJ" width="690" height="325" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/69eee0402089aaa91914001e319c12416dd40b1f_2_690x325.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/69eee0402089aaa91914001e319c12416dd40b1f_2_1035x487.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/69eee0402089aaa91914001e319c12416dd40b1f_2_1380x650.jpeg 2x" data-dominant-color="8A8A92"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1929×909 343 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2019-07-25 18:21 UTC)

<p>Does it work correctly in latest Stable Release or in recent Preview Release? If not, could you please send the application log (menu: Help / Report a bug)?</p>

---

## Post #3 by @Jini (2019-10-30 09:00 UTC)

<p>Hello,<br>
I have the same problem, that the Threshold range is limited to 99.00. I will Range from -1500 to 1500. What I can do?</p>

---

## Post #4 by @lassoan (2019-10-30 11:01 UTC)

<p>Slider range should match range of intensity values in your volume. Please attach the application log to see any hint about what went wrong.</p>

---

## Post #5 by @Jini (2019-10-30 11:04 UTC)

<p>Problem report for Slicer 4.10.2 win-amd64: [please describe expected and actual behavior]</p>
<p>Hello,</p>
<p>my Problem is that the Threshold range go only from 0.00 to 99.00. But I will<br>
-1500 to 1500 Range. Can you help me what the Problem is ?</p>
<p>Thanks</p>

---

## Post #6 by @Jini (2019-11-01 10:13 UTC)

<p>Hi,<br>
I have two Slicer Version in my work PC. But both have problem. In Version 4.10.2 I can not croped the Volume. In Version 4.11. I can select the Threshold Range but the Apply function is not work and I dont get 3D Modell. My data have 10GB. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/765e2f53fcba6c6c1400cefee868404b72fbd8ba.jpeg" data-download-href="/uploads/short-url/gT88aatjyR4szbYPPrg0eUy82q6.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/765e2f53fcba6c6c1400cefee868404b72fbd8ba_2_690x360.jpeg" alt="PNG" data-base62-sha1="gT88aatjyR4szbYPPrg0eUy82q6" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/765e2f53fcba6c6c1400cefee868404b72fbd8ba_2_690x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/765e2f53fcba6c6c1400cefee868404b72fbd8ba_2_1035x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/765e2f53fcba6c6c1400cefee868404b72fbd8ba_2_1380x720.jpeg 2x" data-dominant-color="B0B0B8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1916×1001 646 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2019-11-01 11:21 UTC)

<p>If your data set size is 10GB then you need about 100GB memory space to ensure you don’t run out of memory while performing various processing.</p>
<p>How much RAM do you have? How much virtual memory have you configured in system settings?</p>

---

## Post #8 by @Jini (2019-11-01 10:29 UTC)

<p>In Version 4.11.0 I have tha Trashold Range, but I can not appply and make 3D Modell.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b54523e64c5983d236f11e548bf6b5cdb500b404.jpeg" data-download-href="/uploads/short-url/pRAynb4IvXVodTQ6mipi2jsInxG.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b54523e64c5983d236f11e548bf6b5cdb500b404_2_690x361.jpeg" alt="PNG" data-base62-sha1="pRAynb4IvXVodTQ6mipi2jsInxG" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b54523e64c5983d236f11e548bf6b5cdb500b404_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b54523e64c5983d236f11e548bf6b5cdb500b404_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b54523e64c5983d236f11e548bf6b5cdb500b404_2_1380x722.jpeg 2x" data-dominant-color="9EA3A7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1914×1003 779 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> . My PC have 64 RAM<br>
Intel(R) Core™ i7-9700 CPU 3.00GHz  64Bit. Why the Slicer not work ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b54523e64c5983d236f11e548bf6b5cdb500b404.jpeg" data-download-href="/uploads/short-url/pRAynb4IvXVodTQ6mipi2jsInxG.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b54523e64c5983d236f11e548bf6b5cdb500b404_2_690x361.jpeg" alt="PNG" data-base62-sha1="pRAynb4IvXVodTQ6mipi2jsInxG" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b54523e64c5983d236f11e548bf6b5cdb500b404_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b54523e64c5983d236f11e548bf6b5cdb500b404_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b54523e64c5983d236f11e548bf6b5cdb500b404_2_1380x722.jpeg 2x" data-dominant-color="9EA3A7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1914×1003 779 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks</p>

---

## Post #9 by @Jini (2019-11-01 11:26 UTC)

<p>64 RAM Intel® Core™ i7-9700 CPU 3.00GHz  64Bit</p>

---

## Post #10 by @lassoan (2019-11-01 11:41 UTC)

<p>What operating system do you use? How much virtual memory have you configured in system settings?</p>

---

## Post #11 by @Jini (2019-11-01 12:03 UTC)

<p>Windows 10 Enterprise and graphic card NVIDIA GeForce RTX 2070</p>

---

## Post #12 by @lassoan (2019-11-01 12:39 UTC)

<p>Configure 100GB virtual memory in your system settings and let us know if it helped.</p>

---

## Post #13 by @lassoan (2019-11-01 16:02 UTC)

<p>I’ve tested loading of a 10GB volume then segmenting in Segment editor using Threshold effect then create 3D model by enabling “Show 3D”. I’ve found a bug that caused Slicer to exit during model generation, but I’ve fixed it now, so Slicer Preview Release that you download tomorrow or later (revision 28581 or later) should work well.</p>

---

## Post #14 by @Jini (2019-11-04 08:27 UTC)

<p>Hello,<br>
I have with the new Version the same problem today. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/929e2d8b9bad3afaff1819e2656e265200cf758e.jpeg" data-download-href="/uploads/short-url/kV2BwLsqU6pHOhUAcUCfp1dZ7oq.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/929e2d8b9bad3afaff1819e2656e265200cf758e_2_690x372.jpeg" alt="PNG" data-base62-sha1="kV2BwLsqU6pHOhUAcUCfp1dZ7oq" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/929e2d8b9bad3afaff1819e2656e265200cf758e_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/929e2d8b9bad3afaff1819e2656e265200cf758e_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/929e2d8b9bad3afaff1819e2656e265200cf758e_2_1380x744.jpeg 2x" data-dominant-color="9FA4A7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1920×1036 793 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #15 by @Jini (2019-11-04 11:24 UTC)

<p>What mean this flag in Slicer? and the Data Volum is 22GB and by apply i get this error in picture.<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86886fa848ec93a1934cc0981666fa82620b6de9.png" alt="flagge" data-base62-sha1="jc8ieMwjfYDSMzzaX14JatFCDY5" width="531" height="92"><br>
Can you please help me?</p>

---

## Post #16 by @lassoan (2019-11-04 11:57 UTC)

<p>Task manager shows that you are running out of memory. The error message tells the same. Configure 50-100GB more virtual memory or crop and/or downsanple the image before starting segmentation.</p>
<p>The flag allows you to indicate for yourself that you a segment is correct and complete. It is essential when you have hundreds of segments. See details here: <a href="https://discourse.slicer.org/t/new-feature-search-and-filter-in-segments-table/7827" class="inline-onebox">New feature: Search and filter in segments table</a></p>

---

## Post #17 by @Jini (2019-12-03 11:33 UTC)

<p>Hi,<br>
3D Slicer is not work for DICOM Data.<br>
I have the hard disk rate system expanded to 3TB. I can only open a finished 3D reconstruction, but I can not load a DICOM. What could be the problem?</p>
<p>PC:<br>
intel Core i7-9700 CPU 3,00GHz<br>
64GB<br>
64Bit<br>
Windows 10 Version 1803<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/10a90b958a7aae961241aa48b16997beff6dbdab.png" alt="PC" data-base62-sha1="2nnOFIWBkXtrKdjp9mWDUOiPwXp" width="469" height="272"><br>
D-Laufwerk: 2,72TB<br>
C-Laufwerk : 238GB</p>
<p>Can you please help?</p>
<p>Thanks</p>

---

## Post #18 by @pieper (2019-12-03 13:58 UTC)

<p>Did you try the things listed here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/FAQ/DICOM" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.10/FAQ/DICOM</a></p>

---

## Post #19 by @Nicholas.jacobson (2020-12-08 00:42 UTC)

<p>Hi All,<br>
I seem to be running into the same issue with my threshold range. It is coming in at -2038.26 to 11956.00 which is way above HU units range of -1000 to 1000. Am I missing something or is this an error?</p>
<p>nick<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6f92247d9ed4d464c3317b457eddf6b8c9266e6e.png" alt="image" data-base62-sha1="fV06HOkwMsdnsWcMJ4CA26mYe3Y" width="627" height="218"></p>

---

## Post #20 by @lassoan (2020-12-08 02:03 UTC)

<p>The displayed threshold range is the volume’s intensity range. If it has these large numbers then it means that your volume has such large numbers in it. Even a single outlier single voxel value will alter the min/max value. You can get voxel position of these outliers using numpy:</p>
<pre><code class="lang-python">a = array('MRHead')
import numpy as np
indices = np.where(a&gt;200)
for i in range(len(indices[0])):
    print(f"voxel {i+1}: index = {indices[2][i]} {indices[1][i]} {indices[0][i]}, value = {a[indices[0][i],indices[1][i],indices[2][i]]}")
</code></pre>

---
