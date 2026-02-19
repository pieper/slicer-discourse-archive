---
topic_id: 21696
title: "Loading Dicom Ct Rt Structure Is Incomplete"
date: 2022-01-29
url: https://discourse.slicer.org/t/21696
---

# Loading DICOM CT+RT Structure is incomplete

**Topic ID**: 21696
**Date**: 2022-01-29
**URL**: https://discourse.slicer.org/t/loading-dicom-ct-rt-structure-is-incomplete/21696

---

## Post #1 by @Fabian_Jichi (2022-01-29 16:28 UTC)

<p>Hello,</p>
<p>I loaded different DICOM series that already have contours that need some editing. First problem is that the loaded contour is broken sometimes like in this pictures:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/2811bf09ea68ec67df5971077692e3cd178585d2.png" alt="image" data-base62-sha1="5It7raPVkFGd9s84ZHEM1ZQJf4C" width="625" height="312"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2f5929f1a180f613fe5132986d83d1f3c63ec431.png" alt="image" data-base62-sha1="6KRtn9hm1aZmgfWDZ223q1MaEx3" width="573" height="409"></p>
<p>First I thought is just something visual in 3d Slicer that will not affect me, because I export the files to DICOM after finish the work, but when I looked at the contour in other software, the contour is really broken for body.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d52e36ba439427067c2be639f30497a6ada7996e.jpeg" alt="image" data-base62-sha1="upSIfJPVVINgm9Hia6W2wlEnDI2" width="456" height="469"></p>
<p>Another problem would be that when I draw an additional contour that wasn’t marked before (e.g. Esophagus), it removes the BODY contour in the place where I draw the esophagus.</p>
<p>With esophagus and body visible:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1bdeb0365a7216042b9d4d25df365c5d67ac86b.png" alt="image" data-base62-sha1="yuxY0sjpX9lMqqiUuufcudfbJOz" width="656" height="447"></p>
<p>With only body visible:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5db30aeafba48a66ce066280f35703d29ffac012.png" alt="image" data-base62-sha1="dmU078mdnETbYyRz5j3PsXzqz06" width="685" height="390"></p>
<p>The gap is obvious. And also checked that in another software and body looks like this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c042148530d28383f5ef53e7f7df0d435e0a15f9.jpeg" alt="image" data-base62-sha1="rqNfwzNwpcIYS7Xip5IWR051BAB" width="430" height="412"></p>
<p>I hope it’s possible for me to get some support.</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2022-01-29 16:30 UTC)

<p>It may be either invalid input data or a software bug. Which Slicer version do you use? Can you share the data set (upload dropbox, onedrive, etc. and post the link here)?</p>

---

## Post #3 by @lassoan (2022-01-29 16:35 UTC)

<aside class="quote no-group" data-username="Fabian_Jichi" data-post="1" data-topic="21696">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fabian_jichi/48/14045_2.png" class="avatar"> Fabian_Jichi:</div>
<blockquote>
<p>Another problem would be that when I draw an additional contour that wasn’t marked before (e.g. Esophagus), it removes the BODY contour in the place where I draw the esophagus.</p>
</blockquote>
</aside>
<p>You can choose in Segment Editor masking settings (at the bottom) if you want to overwrite other segments or allow overlap between segments.</p>

---

## Post #4 by @Fabian_Jichi (2022-01-29 18:19 UTC)

<p>Okay, with the second thing I’m ok, I will search for that setting. Thank you!</p>
<p>For the first thing, another example of the issue is:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ec0e07edda09d3c11b5ce752119319ba57649be.jpeg" data-download-href="/uploads/short-url/i5joGHzPt3B806b6ccC50jAyj0y.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ec0e07edda09d3c11b5ce752119319ba57649be_2_654x500.jpeg" alt="image" data-base62-sha1="i5joGHzPt3B806b6ccC50jAyj0y" width="654" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7ec0e07edda09d3c11b5ce752119319ba57649be_2_654x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ec0e07edda09d3c11b5ce752119319ba57649be.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7ec0e07edda09d3c11b5ce752119319ba57649be.jpeg 2x" data-dominant-color="35312C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">844×645 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I can share with you one CT scan from my dataset:</p>
<p><a href="https://we.tl/t-YVwzRdRwVg" class="onebox" target="_blank" rel="noopener nofollow ugc">https://we.tl/t-YVwzRdRwVg</a></p>
<p>Thank you for your help!</p>

---

## Post #5 by @Fabian_Jichi (2022-01-29 18:35 UTC)

<p>One thing that I noticed now playing with 3d Slicer now is that there are issues with DICOM export. I use the last version of the software, and I switched also to the preview version. The idea is that: if I have a CT scan, I edit it or add structures and then export it, the already existing structures in the original DICOM files are sometimes broke.</p>
<p>To give an example, if I have a CT with lung contour and I load it in 3d Slicer, it looks great, after that let’s say that I add a new structure spinal cord, and export the new DICOM files. If I load these new files to 3d Slicer, then the Spinal Cord I draw looks perfect, but the old lung gets some problems. It’s an intuition based on some experience with the application, nothing proved.</p>

---

## Post #6 by @cpinter (2022-01-31 13:56 UTC)

<p>Do you have the same problem with the loaded structures in the 3D view? Sometimes the 2D display of certain surfaces have this issue. By default, the 2D display of structures shows the labelmap not the surface, but it’s good to make sure.</p>

---

## Post #7 by @Fabian_Jichi (2022-01-31 14:06 UTC)

<p>On 3D view it look normal, but of course I don’t have access in the middle of the 3D volume to see if there is any problem.</p>
<p>Anyway, my interest is in 2D to export the structures.</p>

---

## Post #8 by @cpinter (2022-01-31 14:11 UTC)

<p>As I said it is a 2D <em>display</em> issue, so if it is the thing I asked about, then your export will not have this problem.</p>
<p>There are two things you can do to verify:</p>
<ol>
<li>Make the segmentation semi-transparent (that’s your way to “have access in the middle of the 3D volume”) and see if there are lines or not</li>
<li>Make sure the 2D views are showing the binary labelmap. If what you have is what you see in this screenshot then the problem is with the data or it is an import bug as <a class="mention" href="/u/lassoan">@lassoan</a> suggests.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24f49c1fd3dcad3c56981e175a7ceffd7e83976e.png" data-download-href="/uploads/short-url/5gVgjwXSrrKmeAqRSrsfBKTUGl0.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24f49c1fd3dcad3c56981e175a7ceffd7e83976e.png" alt="image" data-base62-sha1="5gVgjwXSrrKmeAqRSrsfBKTUGl0" width="414" height="499" data-dominant-color="F1F2F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">483×582 25.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @Fabian_Jichi (2022-01-31 15:47 UTC)

<p>Thank you for your input,</p>
<p>I don’t think it is a data problem, because I viewed this data in other software and also with matplotlib in python and there everything it’s ok.<br>
The problem persist in the software and in the exported DICOM files from 3d Slicer.<br>
Basically the simples example, if I load a DICOM series (that doesn’t have any problem because I verified) and export exactly the same series from 3d Slicer to DICOM, and the view it with matplotlib, the problem is appear.</p>
<p>About your question regarding 3D view, as you can see in this picture, the problem persist on 3D view also:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48c3a2519f64eee92fce46e31d26782b3a6cdcf4.jpeg" data-download-href="/uploads/short-url/anHwmdoxMLZSHcaiE2bvrdh46SU.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48c3a2519f64eee92fce46e31d26782b3a6cdcf4_2_690x284.jpeg" alt="image" data-base62-sha1="anHwmdoxMLZSHcaiE2bvrdh46SU" width="690" height="284" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/48c3a2519f64eee92fce46e31d26782b3a6cdcf4_2_690x284.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48c3a2519f64eee92fce46e31d26782b3a6cdcf4.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/48c3a2519f64eee92fce46e31d26782b3a6cdcf4.jpeg 2x" data-dominant-color="988595"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">866×357 66.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Also regarding setting representation for 2D views on binary labelmap, the software doesn’t allow me to do set “binary labelmap”, I see the option, I click on it and nothing happens.</p>
<p>Thank you for support!</p>

---

## Post #10 by @lassoan (2022-02-01 06:33 UTC)

<p>I’ve checked the data set and the contours are incorrect. See for example for the body contour:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e87f244510b1ae0fc61d6a994ac2d4d7c5ae401.jpeg" data-download-href="/uploads/short-url/i3lqlH5Tp7Sxr6r1jxALrCWAuHv.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7e87f244510b1ae0fc61d6a994ac2d4d7c5ae401_2_680x500.jpeg" alt="image" data-base62-sha1="i3lqlH5Tp7Sxr6r1jxALrCWAuHv" width="680" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7e87f244510b1ae0fc61d6a994ac2d4d7c5ae401_2_680x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7e87f244510b1ae0fc61d6a994ac2d4d7c5ae401_2_1020x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7e87f244510b1ae0fc61d6a994ac2d4d7c5ae401_2_1360x1000.jpeg 2x" data-dominant-color="3E594B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1657×1218 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It seems that the labelmap to contour conversion in Plastimatch fails if the contour goes outside (or touches the boundary) of the reference CT image.</p>
<aside class="quote no-group" data-username="Fabian_Jichi" data-post="9" data-topic="21696">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fabian_jichi/48/14045_2.png" class="avatar"> Fabian_Jichi:</div>
<blockquote>
<p>Also regarding setting representation for 2D views on binary labelmap, the software doesn’t allow me to do set “binary labelmap”, I see the option, I click on it and nothing happens.</p>
</blockquote>
</aside>
<p>First you need to create the “binary labelmap” representation by clicking on “Create” button next to “Binary labelmap” in the Representations section in Segmentations module.</p>
<p>The data set contains an extremely high number of contour points (in many cases about 1500 points per slice), so the conversion can take 5-10 minutes.</p>
<p><a class="mention" href="/u/gcsharp">@gcsharp</a> This RTSTRUCT was generated by Plastimatch, so maybe you can help with these questions:</p>
<ul>
<li>Is it a known limitation that if the contour touches the reference CT edge then the contour points will be discarded? Does this occur with the latest Plastimatch version?</li>
<li>The contours contain many points (about 1500 per slice in many cases). Doesn’t this cause trouble in treatment planning systems? Could an option be added to decimate the contour polyline (e.g., with a filter like <a href="https://vtk.org/doc/nightly/html/classvtkDecimatePolylineFilter.htmlils">this</a>)?</li>
</ul>

---

## Post #11 by @gcsharp (2022-02-01 16:37 UTC)

<p>Hi Andras,</p>
<ol>
<li>No I’m not aware, thank you for investigating.  Do you already have an example data set that I could use for testing?</li>
<li>It could cause problems in some cases. There is already code for segment decimation, but it could be improved.  The most user friendly approach is probably decimating to a fixed limit (e.g. decimate to maximum 500 points per contour).  Also probably best to make this behavior it optional.  Your thoughts?</li>
</ol>
<p>Greg</p>

---

## Post #12 by @lassoan (2022-02-01 17:43 UTC)

<aside class="quote no-group" data-username="gcsharp" data-post="11" data-topic="21696">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>No I’m not aware, thank you for investigating. Do you already have an example data set that I could use for testing?</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/fabian_jichi">@Fabian_Jichi</a> Do you still have the segmentation in labelmap or segmentation format that you used as input for the RTSTRUCT export (that generated the files that you shared)?</p>
<aside class="quote no-group" data-username="gcsharp" data-post="11" data-topic="21696">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gcsharp/48/863_2.png" class="avatar"> gcsharp:</div>
<blockquote>
<p>The most user friendly approach is probably decimating to a fixed limit (e.g. decimate to maximum 500 points per contour). Also probably best to make this behavior it optional. Your thoughts?</p>
</blockquote>
</aside>
<p>I would try vtkDecimatePolylineFilter or similar filters in ITK (if there is any) to see how well they work on these contours. If they work well then they could be used to Plastimatch to simplify the contour. The stopping condition for decimation should be ideally some kind of maximum error metric instead of maximum number of points.</p>

---
