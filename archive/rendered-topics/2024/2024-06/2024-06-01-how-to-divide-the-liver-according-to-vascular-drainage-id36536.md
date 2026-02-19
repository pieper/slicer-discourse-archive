---
topic_id: 36536
title: "How To Divide The Liver According To Vascular Drainage"
date: 2024-06-01
url: https://discourse.slicer.org/t/36536
---

# How to divide the liver according to vascular drainage？

**Topic ID**: 36536
**Date**: 2024-06-01
**URL**: https://discourse.slicer.org/t/how-to-divide-the-liver-according-to-vascular-drainage/36536

---

## Post #1 by @Gerard_Siker (2024-06-01 09:01 UTC)

<p>Hello everyone,</p>
<p>I’m trying to divide the liver according to vascular drainage.I tried following the tutorial step by step using the SlicerLiver extension. But when I add all the vessel points and click on the button ‘Calculate Vascular Territory Segmentation’, the result is not as shown in the tutorial.</p>
<p>I’m trying to figure out where things went wrong. I would be very happy if someone could help me with this task.</p>

---

## Post #2 by @Gerard_Siker (2024-06-01 09:01 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/4996218413b464b3aba7dd5bbd6191565ca93d8c.jpeg" data-download-href="/uploads/short-url/auYvzYt7x06rgcDxsQHiBDcwssQ.jpeg?dl=1" title="20240601165603" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4996218413b464b3aba7dd5bbd6191565ca93d8c_2_690x349.jpeg" alt="20240601165603" data-base62-sha1="auYvzYt7x06rgcDxsQHiBDcwssQ" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4996218413b464b3aba7dd5bbd6191565ca93d8c_2_690x349.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4996218413b464b3aba7dd5bbd6191565ca93d8c_2_1035x523.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/4996218413b464b3aba7dd5bbd6191565ca93d8c.jpeg 2x" data-dominant-color="ECEFF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20240601165603</span><span class="informations">1126×571 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/be608a0144f06005f6189070bc4a624d9147a385.jpeg" data-download-href="/uploads/short-url/ra9yjk7Qr5uTi7u6caCb3Br68dv.jpeg?dl=1" title="20240601165727" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be608a0144f06005f6189070bc4a624d9147a385_2_690x320.jpeg" alt="20240601165727" data-base62-sha1="ra9yjk7Qr5uTi7u6caCb3Br68dv" width="690" height="320" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be608a0144f06005f6189070bc4a624d9147a385_2_690x320.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be608a0144f06005f6189070bc4a624d9147a385_2_1035x480.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/be608a0144f06005f6189070bc4a624d9147a385_2_1380x640.jpeg 2x" data-dominant-color="8796CB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20240601165727</span><span class="informations">1407×654 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e201c66ff0f77a8d1931c509706b623234622a92.jpeg" data-download-href="/uploads/short-url/wflI7d5EHuYba9PtlXyFxszXF5w.jpeg?dl=1" title="20240601165800" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e201c66ff0f77a8d1931c509706b623234622a92_2_690x354.jpeg" alt="20240601165800" data-base62-sha1="wflI7d5EHuYba9PtlXyFxszXF5w" width="690" height="354" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e201c66ff0f77a8d1931c509706b623234622a92_2_690x354.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e201c66ff0f77a8d1931c509706b623234622a92_2_1035x531.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e201c66ff0f77a8d1931c509706b623234622a92.jpeg 2x" data-dominant-color="7285BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">20240601165800</span><span class="informations">1116×574 60.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @RafaelPalomar (2024-06-06 04:57 UTC)

<p><a class="mention" href="/u/gerard_siker">@Gerard_Siker</a>, it looks to me that you are creating a single vascular territory, therefore the result is a single segment. Instead of creating one vascular territory with multiple segments, try creating multiple vascular territories with one segment each. Let me know if that works for you.</p>

---

## Post #4 by @Gerard_Siker (2024-06-06 08:56 UTC)

<p>Hi Rafael,I created multiple vascular territories as you suggested, but the results didn’t make a difference. The version I used is 3D Slicer 5.6.2.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/4004e52c59bd2186592c25ccb1d1b3c3989cd555.jpeg" data-download-href="/uploads/short-url/98l2QZrUt32h9CsOqbp77Ns8t5b.jpeg?dl=1" title="pic1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/4004e52c59bd2186592c25ccb1d1b3c3989cd555_2_690x336.jpeg" alt="pic1" data-base62-sha1="98l2QZrUt32h9CsOqbp77Ns8t5b" width="690" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/4004e52c59bd2186592c25ccb1d1b3c3989cd555_2_690x336.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/4004e52c59bd2186592c25ccb1d1b3c3989cd555_2_1035x504.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/4004e52c59bd2186592c25ccb1d1b3c3989cd555.jpeg 2x" data-dominant-color="919ACD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic1</span><span class="informations">1261×615 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0c943cd7561dccf64138962915233eb3ce3b334.jpeg" data-download-href="/uploads/short-url/rvsSHvDMlbeOzlXaaRDwx98fCLi.jpeg?dl=1" title="pic2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0c943cd7561dccf64138962915233eb3ce3b334_2_690x330.jpeg" alt="pic2" data-base62-sha1="rvsSHvDMlbeOzlXaaRDwx98fCLi" width="690" height="330" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0c943cd7561dccf64138962915233eb3ce3b334_2_690x330.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c0c943cd7561dccf64138962915233eb3ce3b334_2_1035x495.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0c943cd7561dccf64138962915233eb3ce3b334.jpeg 2x" data-dominant-color="F2F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">pic2</span><span class="informations">1158×555 91.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @RafaelPalomar (2024-06-06 11:27 UTC)

<p><a class="mention" href="/u/gerard_siker">@Gerard_Siker</a>, thanks for giving it a try. This layout should work, but it seems not to be working for me either. <a class="mention" href="/u/olevs">@olevs</a>, could you give it a try? Maybe there is somethign <a class="mention" href="/u/gerard_siker">@Gerard_Siker</a>  and I are missing?</p>
<p><a class="mention" href="/u/gerard_siker">@Gerard_Siker</a>, otherwise, we are about to release a new version. I’m in the process of testing it: I’ll test this carefully there.</p>

---

## Post #6 by @olevs (2024-06-11 08:47 UTC)

<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> This is one of the bugs that is fixed in the new version</p>

---

## Post #7 by @Gerard_Siker (2024-06-12 10:45 UTC)

<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> <a class="mention" href="/u/olevs">@olevs</a> ，Thanks for answering my question, I’m really looking forward to the new version of SliceLliver！</p>

---

## Post #8 by @RafaelPalomar (2024-06-18 10:03 UTC)

<p>Hello <a class="mention" href="/u/gerard_siker">@Gerard_Siker</a>, I have just pushed a new version of Slicer-Liver. Most likely, this will be built into the extension manager sometime during tomorrow. Please, give it a try and let us know about the results.</p>

---

## Post #9 by @Gerard_Siker (2024-06-21 02:34 UTC)

<p><a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb1994bfe5d5da1293a3f24b46b8b74c855cd307.jpeg" data-download-href="/uploads/short-url/zPkErcai8mtmG1jwuI2F0J1bmgT.jpeg?dl=1" title="picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb1994bfe5d5da1293a3f24b46b8b74c855cd307_2_690x409.jpeg" alt="picture1" data-base62-sha1="zPkErcai8mtmG1jwuI2F0J1bmgT" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb1994bfe5d5da1293a3f24b46b8b74c855cd307_2_690x409.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fb1994bfe5d5da1293a3f24b46b8b74c855cd307_2_1035x613.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb1994bfe5d5da1293a3f24b46b8b74c855cd307.jpeg 2x" data-dominant-color="9D99BA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">picture1</span><span class="informations">1158×687 79.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Many thanks to your team for updating the extension!</p>

---

## Post #10 by @lassoan (2024-06-21 02:42 UTC)

<p>This looks nice! <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> <a class="mention" href="/u/olevs">@olevs</a> what algorithm is used for subdivision of the liver based on vasculature?</p>

---

## Post #11 by @olevs (2024-06-21 06:57 UTC)

<p>Just looping through all the liver voxels, and finding the closest centerline point. Code is in <a href="https://github.com/ALive-research/Slicer-Liver/blob/8065aa7a95f1586e79a347f93f47d889e7e8ec6a/LiverSegments/Logic/vtkLiverSegmentsLogic.cxx#L129" rel="noopener nofollow ugc">vtkLiverSegmentsLogic::SegmentClassificationProcessing()</a></p>

---

## Post #12 by @lassoan (2024-06-21 12:59 UTC)

<p>How long does the computation take?</p>
<p>When I needed such partitioning I wanted to achieve the same end result but I was worried about the long computation time. Also, it would just use Euclidean distance (not geodesic distance), so when a vessel could have influence in a region that is separated by the organ boundary (although probably this is not an issue in liver)</p>
<p>So, I ended up using Grow from seed with the “Seed locality” value set to the maximum (so that image content is not taken into account), but I was wondering if this was the simplest solution and if it was accurate enough (grow from seeds does not step in diagonal directions, so it works with block distance instead of Euclidean distance).</p>
<p>Probably fast marching would be the most appropriate tool for this. It should be fast enough and the speed image could be used to restrict marching to be within the segment boundary. It is <a href="https://itk.org/Doxygen/html/classitk_1_1FastMarchingImageFilter.html">implemented in ITK</a>, so it would be quite easy to add it as a segment editor effect.</p>

---
