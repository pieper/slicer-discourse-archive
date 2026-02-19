---
topic_id: 33887
title: "Beginner Question Liver Volumetry"
date: 2024-01-21
url: https://discourse.slicer.org/t/33887
---

# Beginner question: liver volumetry

**Topic ID**: 33887
**Date**: 2024-01-21
**URL**: https://discourse.slicer.org/t/beginner-question-liver-volumetry/33887

---

## Post #1 by @ThomasHusson (2024-01-21 01:08 UTC)

<p>Hello !<br>
I’m a resident in surgery, interested in liver volumetry prior to hepatectomy.<br>
In the team which I work with, we use an expensive software made by Fujifilm, called Synapse.<br>
It has 2 features that I need in 3D slicer, and I can’t find a tutorial.</p>
<p>First : I want to extract the whole liver<br>
For that, I found a plugin called RVX that is pretty fast and accurate to make “liver in” and “liver out”<br>
See picture there :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/3/5309f3df4314913ac828a6b989119acf14644be3.jpeg" data-download-href="/uploads/short-url/bQAX73Ao1eQqqwBUfk5uRcYwpNx.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5309f3df4314913ac828a6b989119acf14644be3_2_690x361.jpeg" alt="image" data-base62-sha1="bQAX73Ao1eQqqwBUfk5uRcYwpNx" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5309f3df4314913ac828a6b989119acf14644be3_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5309f3df4314913ac828a6b989119acf14644be3_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/3/5309f3df4314913ac828a6b989119acf14644be3_2_1380x722.jpeg 2x" data-dominant-color="393837"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1005 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But, my problem is when I go to another tab of 3Dslicer, i lose the informations of “liver in” and “liver out” that was made by the plugin. See the tab “segmentation” here :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/7532ac2250812dea53ac882d8a6bdfaf7f9ee81c.jpeg" data-download-href="/uploads/short-url/gIMqBFQQfl5pzODtlxZ2pYBhddW.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/7532ac2250812dea53ac882d8a6bdfaf7f9ee81c_2_690x352.jpeg" alt="image" data-base62-sha1="gIMqBFQQfl5pzODtlxZ2pYBhddW" width="690" height="352" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/7532ac2250812dea53ac882d8a6bdfaf7f9ee81c_2_690x352.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/7532ac2250812dea53ac882d8a6bdfaf7f9ee81c_2_1035x528.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/7532ac2250812dea53ac882d8a6bdfaf7f9ee81c_2_1380x704.jpeg 2x" data-dominant-color="3A3738"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×980 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How can I export the data to the whole software ?</p>
<p>Second question : I want to do volume measurements, not 3D reconstruction :<br>
So how to know the total volume of “liver in”, in mililiters / cm3 ?</p>
<p>And third question, that is the hardest : I want to do hepatectomies :<br>
How to trace lines on my CT scan (or on the 3D reconstruction), that can simulates a surgery (i.e right/left hepatectomy), and to know the volume of the resected lesion ?</p>
<p>On fujifilm synapse, I trace lines on different slices of the ct scan, then the software reconstruct the section between the different lines. Is it possible to do the same ?</p>
<p>Thanks a lot !</p>
<p>Thomas</p>

---

## Post #2 by @pieper (2024-01-21 18:20 UTC)

<p>I haven’t gone through it myself but the tutorial here looks really good:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/bb6e8b7c023d8fbc2859a9f6b128a195d8c3ff4cef4572b15689a13a229b4f9e/R-Vessel-X/SlicerRVXLiverSegmentation" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation" target="_blank" rel="noopener">GitHub - R-Vessel-X/SlicerRVXLiverSegmentation: 3D Slicer plugin for Liver...</a></h3>

  <p>3D Slicer plugin for Liver Anatomy Annotation by R-Vessel-X - GitHub - R-Vessel-X/SlicerRVXLiverSegmentation: 3D Slicer plugin for Liver Anatomy Annotation by R-Vessel-X</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You can also check other SegmentEditor tutorials for general use of the resulting segmentations and you may be able to use those tools to emulate surgery.  However SlicerLiver is much more specialized for this task.  Also check SegmentStatistics for info on getting the volume metrics.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/ALive-research/Slicer-Liver">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/ALive-research/Slicer-Liver" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/b5b7809fbe1f19e2cbd7cb2567cbaaf26741afba58d851148e9eab89f00c5053/ALive-research/Slicer-Liver" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/ALive-research/Slicer-Liver" target="_blank" rel="noopener">GitHub - ALive-research/Slicer-Liver: 3D Slicer extension for liver analysis...</a></h3>

  <p>3D Slicer extension for liver analysis and therapy planning - GitHub - ALive-research/Slicer-Liver: 3D Slicer extension for liver analysis and therapy planning</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @ThomasHusson (2024-01-22 22:16 UTC)

<p>Hey !<br>
Thanks for the answer !</p>
<p>Just tried “liver” plugin and I still do have a problem.</p>
<p>I arrived on this screen by using the sample data :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a36f22a88948ba19213b4c6758a07650893bc4f.jpeg" data-download-href="/uploads/short-url/61rM2Rxe6QDBbaFH2f2sqJaSO75.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a36f22a88948ba19213b4c6758a07650893bc4f_2_690x414.jpeg" alt="image" data-base62-sha1="61rM2Rxe6QDBbaFH2f2sqJaSO75" width="690" height="414" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a36f22a88948ba19213b4c6758a07650893bc4f_2_690x414.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a36f22a88948ba19213b4c6758a07650893bc4f_2_1035x621.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a36f22a88948ba19213b4c6758a07650893bc4f_2_1380x828.jpeg 2x" data-dominant-color="595665"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1153 166 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>BUT :<br>
I still have a problem with volumetry.<br>
I would like to know the volume of liver on either side of my resection line.</p>
<p>I can’t find a way to do it… If some one have an idea ?</p>
<p>Thanks a lot;</p>
<p>Thomas</p>

---

## Post #4 by @pieper (2024-01-22 23:23 UTC)

<p>Looks like you are very close. Maybe <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> can suggest the next step?</p>

---

## Post #5 by @Numan_Kutaiba (2024-01-23 16:52 UTC)

<p>Go to Segment Statistics.<br>
Select the scalar volume (source images) and segmentation volume, then hit Apply. It will generate a table with volume and density measurements.</p>

---

## Post #6 by @ThomasHusson (2024-01-23 19:54 UTC)

<p>Some news here !<br>
Just succeed, but only one time…<br>
I have another problem !!<br>
First of all : I use the total liver volume by first exporting it from RVX plugin, to a .stl file.<br>
Then, I import the stl file in “segment editor” of 3Dslicer (it is the only way I found to make the plugin communicate with the rest of the software).</p>
<p>Then, as <a class="mention" href="/u/finetjul">@finetjul</a> wisely told me, I used one of the scissors tool. I suceed one time !<br>
But when I wanted to try another time with another CT scan, 3D slicer doesn’t answer anymore, or I need to wait &gt; 15minutes</p>
<p>It says that I have to convert to binary labelmap data, then load for a lot and a lot of time until I force to quit the software.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c840690223a49a3608ecaa0a687d131ecc2f6254.jpeg" data-download-href="/uploads/short-url/szvuwkQ3XVPvX2g70ovDDnjjAUY.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c840690223a49a3608ecaa0a687d131ecc2f6254_2_690x368.jpeg" alt="image" data-base62-sha1="szvuwkQ3XVPvX2g70ovDDnjjAUY" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c840690223a49a3608ecaa0a687d131ecc2f6254_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c840690223a49a3608ecaa0a687d131ecc2f6254_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c840690223a49a3608ecaa0a687d131ecc2f6254_2_1380x736.jpeg 2x" data-dominant-color="444545"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1024 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Does someone have an idea ? Maybe exporting in another format than STL ?</p>
<p>AND second question :<br>
When I succeed, I used the surface cut tool.<br>
Sometimes it does this :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1746fe231e920e43cc6de3f6692a92b177474243.jpeg" data-download-href="/uploads/short-url/3jV59a3LlqUDnjHbbiMsAPB9dCP.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1746fe231e920e43cc6de3f6692a92b177474243_2_690x431.jpeg" alt="image" data-base62-sha1="3jV59a3LlqUDnjHbbiMsAPB9dCP" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1746fe231e920e43cc6de3f6692a92b177474243_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1746fe231e920e43cc6de3f6692a92b177474243_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/1746fe231e920e43cc6de3f6692a92b177474243_2_1380x862.jpeg 2x" data-dominant-color="3A3937"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1200 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>but sometimes, and I don’t know why, it does this :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7e779253faaa6086a3d5c1092439641de5db1bd.jpeg" data-download-href="/uploads/short-url/nXlFkE6UpUyVoCxzIKum8fgdy21.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7e779253faaa6086a3d5c1092439641de5db1bd_2_596x500.jpeg" alt="image" data-base62-sha1="nXlFkE6UpUyVoCxzIKum8fgdy21" width="596" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7e779253faaa6086a3d5c1092439641de5db1bd_2_596x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7e779253faaa6086a3d5c1092439641de5db1bd_2_894x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7e779253faaa6086a3d5c1092439641de5db1bd_2_1192x1000.jpeg 2x" data-dominant-color="454A45"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1726×1446 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Does anyone have an idea for these two problems ? I’m almost there !</p>
<p>Thanks a lot</p>
<p>Thomas</p>

---

## Post #7 by @finetjul (2024-01-24 06:35 UTC)

<p>Regarding the first question, your overall volume seems too big and does not fit your computer memory. You might want to reduce the size of your volume first (“Crop volume” module)</p>
<p>Regarding the second question, you do not seem to have the latest version of the SurfaceCut tool.</p>

---

## Post #8 by @RafaelPalomar (2024-01-24 13:48 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="33887" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Looks like you are very close. Maybe <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> can suggest the next step?</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/thomashusson">@ThomasHusson</a>, with Slicer-Liver you can do liver volumetry computations. I see in your screenshot that you were very close (the resection volumetry group widget is what you need)</p>
<p>1 ) Create a volumetry output table (in your screenshot you  had none created).<br>
2) Your reference volume node looks correct, as well as your segmentation node.<br>
3)  Our volumetry calculations are based on seed points that you can mix (for instance if you want to combine different liver segments with a resection. Your case looks more simple you would need to create a new markups list and place a seed inside the resected liver segmentation.</p>
<p>Please, let us know if this works for you or if you need further assistance.</p>
<p>I’m sure <a class="mention" href="/u/ruoyanmeng">@RuoyanMeng</a> and <a class="mention" href="/u/dalbenziog">@dalbenzioG</a> will react if I’m missing anyhing</p>

---

## Post #9 by @RuoyanMeng (2024-01-24 14:13 UTC)

<p>Hi <a class="mention" href="/u/thomashusson">@ThomasHusson</a><br>
As <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> said you are very close! I created a simple instruction based on your screenshot, you can try to do the following steps above on your current actions. Let me know if you have further questions <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e18273d10a94614c145fcca6f4aad4f2973f328e.png" data-download-href="/uploads/short-url/waWVhgEcNlQ50FmV9Yx0IlKDZr8.png?dl=1" title="example (1)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e18273d10a94614c145fcca6f4aad4f2973f328e_2_690x416.png" alt="example (1)" data-base62-sha1="waWVhgEcNlQ50FmV9Yx0IlKDZr8" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e18273d10a94614c145fcca6f4aad4f2973f328e_2_690x416.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e18273d10a94614c145fcca6f4aad4f2973f328e.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e18273d10a94614c145fcca6f4aad4f2973f328e.png 2x" data-dominant-color="5B5765"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">example (1)</span><span class="informations">892×539 251 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @RafaelPalomar (2024-01-24 14:57 UTC)

<p>Way better than my explaination. Thanks <a class="mention" href="/u/ruoyanmeng">@RuoyanMeng</a>!</p>

---

## Post #11 by @ThomasHusson (2024-02-12 20:02 UTC)

<p>Hey, update needed here!<br>
I finally managed to do it on many patient files.</p>
<p>I used totalsegmentator, which I found better because it doesn’t take the IVC or portal trunk for the liver. I had a surestimation of the total liver volume using RVX.<br>
Also, totalsegmentator doesn’t need time to ‘convert’ the data, which was a problem because it took a lot of time with RVX.</p>
<p>I drew the hepatectomy using the Draw tool and the Fill between Slices tool.</p>
<p>I’m going to record a video for a tutorial that I’ll post here, in French with English subtitles.</p>
<p>Thank you very much for all your answers, I wouldn’t be able to do it without you!</p>

---

## Post #12 by @ThomasHusson (2024-02-13 16:00 UTC)

<p>EDIT :<br>
I have a problem using “Fill between slices” : see topic here : <a href="https://discourse.slicer.org/t/fill-between-slices-issue-need-help/34297" class="inline-onebox">Fill between slices issue : need help!</a></p>
<p>If anybody here have an idea, I (again) need your help!<br>
Thank you very much +++</p>

---

## Post #13 by @RafaelPalomar (2024-02-15 14:11 UTC)

<aside class="quote no-group" data-username="ThomasHusson" data-post="12" data-topic="33887">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/thomashusson/48/68560_2.png" class="avatar"> ThomasHusson:</div>
<blockquote>
<p>I have a problem using “Fill between slices”</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/thomashusson">@ThomasHusson</a>, I’m curious. Was it anything that didn’t work for you using the instructions <a class="mention" href="/u/ruoyanmeng">@RuoyanMeng</a> provided?</p>

---

## Post #15 by @ThomasHusson (2024-02-25 17:55 UTC)

<p>Hi there. I found a solution using the intersect tool.<br>
Regarding the R-vesselX plugin, I didn’t use it because I couldn’t figure out how to trace a line directly on the CT scan as I did using the cut option.<br>
Even placing ROI directly, I haven’t found how! Should I place it on each side of a line?</p>
<p>Using 3D reconstruction rather than directly on the CT scan is a problem because 3D reconstruction would be needed to easily trace a line (e.g. following a vein).<br>
I found it much more difficult to manipulate the fiducials on the 3D reconstruction if the vascular reconstruction wasn’t done first.</p>
<p>If the line could be traced directly on the CT scan, like the cut tool does in SegmentEditor, that would solve my problems!<br>
Maybe using points with ROI as <a class="mention" href="/u/ruoyanmeng">@RuoyanMeng</a> said? I haven’t found how …</p>
<p>Thank you very much</p>

---

## Post #16 by @roeg (2024-03-19 11:50 UTC)

<p>This is a great question!! I am an expert at contouring Liver Volumes in my Institution. In fact, i am the only expert. 18 years. Liver and spleen volumes from MRI. With acute accuracy. But i really would like to explore what 3D slicer has to offer. If i did master this software, it would be the tip of the iceberg for my clinical customers.<br>
cheers<br>
John Roeger UHN. Toronto Canada</p>

---

## Post #17 by @RafaelPalomar (2024-03-19 13:06 UTC)

<p><a class="mention" href="/u/roeg">@roeg</a>, for the Slicer-Liver extension we have been working with CT imaging, but if you can get good liver segmentations on MRI, the extension would operate the same way. Let us know about your experience if you end up trying the extension and ask any questions you may encounter.</p>

---

## Post #18 by @roeg (2024-03-20 19:04 UTC)

<p>Thank you for the reply. My work is ongoing…( have lots of cases) but will be looking more and more into your product. I have a lot of new software as well… I also excel at clinical coverage, so very busy schedule. Looking forward<br>
sincerely<br>
John Roeger<br>
3D Technical Specialist<br>
INR/VIR Clinical Technologist/Specialist</p>

---

## Post #19 by @psychicpotato (2024-09-19 17:48 UTC)

<p>Thanks so much - this worked!</p>

---

## Post #20 by @ThomasHusson (2024-09-19 18:46 UTC)

<p>Hey, update here</p><div class="youtube-onebox lazy-video-container" data-video-id="FywayDfP9t0" data-video-title="Liver Volumetry Using 3DSlicer - Tutorial" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=FywayDfP9t0" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/FywayDfP9t0/maxresdefault.jpg" title="Liver Volumetry Using 3DSlicer - Tutorial" width="690" height="388">
  </a>
</div>
<p>
Here is my tutorial, french voice over<br>
Thank you all !!</p>

---

## Post #21 by @johny723 (2025-02-14 01:48 UTC)

<p>Hi, I am not able to figure out how to get volumes of the resected liver and remaining parenchym. I have followed the instructions, I can create the resection plane and adjust its points, I can place one point to each side of the resection plane, but it seems impossible to get the numbers of the individual parts of the liver parenchyma. Can you please help me?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/102dea6808ad67e6645e15c18a78339f5348ca2a.jpeg" data-download-href="/uploads/short-url/2j80PkvjTasn1dV649cVEV6w0qu.jpeg?dl=1" title="Snímka obrazovky 2025-02-14 024729" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/102dea6808ad67e6645e15c18a78339f5348ca2a_2_690x319.jpeg" alt="Snímka obrazovky 2025-02-14 024729" data-base62-sha1="2j80PkvjTasn1dV649cVEV6w0qu" width="690" height="319" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/102dea6808ad67e6645e15c18a78339f5348ca2a_2_690x319.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/102dea6808ad67e6645e15c18a78339f5348ca2a_2_1035x478.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/102dea6808ad67e6645e15c18a78339f5348ca2a_2_1380x638.jpeg 2x" data-dominant-color="A59F9E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snímka obrazovky 2025-02-14 024729</span><span class="informations">1910×885 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #22 by @RafaelPalomar (2025-02-20 08:54 UTC)

<p><a class="mention" href="/u/johny723">@johny723</a>, make sure that your resection surface markup completely exceeds the liver parenchyma all around. The underlying algorithm for volume calculation can leak if the resection does not mark a clear delimitation between resected/remnant tissue. As far as I can see, the rest of your parameters look correct. Below an example where it works (note that my resection goes well beyond the liver parenchyma).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69df1a7b38269514d4f7785ef3e7b8ca61a77b85.jpeg" data-download-href="/uploads/short-url/f6A88MTBznrPC9YFttAuIGstdMp.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69df1a7b38269514d4f7785ef3e7b8ca61a77b85_2_690x395.jpeg" alt="image" data-base62-sha1="f6A88MTBznrPC9YFttAuIGstdMp" width="690" height="395" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69df1a7b38269514d4f7785ef3e7b8ca61a77b85_2_690x395.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69df1a7b38269514d4f7785ef3e7b8ca61a77b85_2_1035x592.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/9/69df1a7b38269514d4f7785ef3e7b8ca61a77b85_2_1380x790.jpeg 2x" data-dominant-color="BFB8B6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1917×1098 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #23 by @johny723 (2025-02-21 01:25 UTC)

<p>Thank you, the points needed to be quite far away from the liver. It is working now!</p>
<p>I have another question. How do I actually resect the liver into 2 parts on each side of the resecion plane? Having a 3d model of the resected part and the remnant would be great. Is it possible to create an arbitrary plane using Bezier surface and then divide the given segment ( liver, spleen, etc, you name it) according to the resection plane? Thank you!</p>

---

## Post #24 by @RafaelPalomar (2025-02-21 09:47 UTC)

<p><a class="mention" href="/u/johny723">@johny723</a>, the points don’t really need to be quite far, you just have to make sure that the boundary of the resection is not inside the parenchyma; leaving a small margin out helps making sure this effectively happens. For visualization purposes, you can (1) compute the distance map, (2) select the newly generated distance map for the resection and (3) mark the “Preview resection” box. This will cut off the excess of the resection for a better visualization.</p>
<p>In the volumetry section of Slicer-Liver you can use the “Generate Segments…” button to generate the segmentation with individual separated segments. Here is a picture leveraging on all features you ask:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a87675c5a95acca413324331ea40c2ac8e97855.jpeg" data-download-href="/uploads/short-url/htWlRnS57fZ04HFpRgG20LdBhu5.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a87675c5a95acca413324331ea40c2ac8e97855_2_690x419.jpeg" alt="image" data-base62-sha1="htWlRnS57fZ04HFpRgG20LdBhu5" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a87675c5a95acca413324331ea40c2ac8e97855_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a87675c5a95acca413324331ea40c2ac8e97855_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a87675c5a95acca413324331ea40c2ac8e97855_2_1380x838.jpeg 2x" data-dominant-color="959AAB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1168 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #25 by @johny723 (2025-03-10 19:14 UTC)

<p>Sorry for a delayed answer.</p>
<p>I dont have any " Generate segments based on selected resections and ROI markers" button on my screen.</p>
<p>Wh<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef4b7d1734b16553d5ee490e6685f1f8b20581a3.png" data-download-href="/uploads/short-url/y8TQDUy7eCFoylTWKNlQIHpRQKD.png?dl=1" title="Snímka obrazovky 2025-03-10 200713" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef4b7d1734b16553d5ee490e6685f1f8b20581a3_2_387x499.png" alt="Snímka obrazovky 2025-03-10 200713" data-base62-sha1="y8TQDUy7eCFoylTWKNlQIHpRQKD" width="387" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef4b7d1734b16553d5ee490e6685f1f8b20581a3_2_387x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/f/ef4b7d1734b16553d5ee490e6685f1f8b20581a3_2_580x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef4b7d1734b16553d5ee490e6685f1f8b20581a3.png 2x" data-dominant-color="F4F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snímka obrazovky 2025-03-10 200713</span><span class="informations">674×870 37.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
at am I doing wrong?</p>

---

## Post #26 by @johny723 (2025-03-10 19:29 UTC)

<p>What do I have to do to make the “Generate segments…” appear?<br>
Could you please make a step by step tutorial?</p>

---

## Post #27 by @RafaelPalomar (2025-03-18 12:06 UTC)

<p>The documentation for Slicer-Liver is at <a href="https://github.com/ALive-research/Slicer-Liver" class="inline-onebox" rel="noopener nofollow ugc">GitHub - ALive-research/Slicer-Liver: 3D Slicer extension for liver analysis and therapy planning</a>, with a walk-through of of all the functionality of the extension.</p>
<p>The image below, which is extracted from the documentation highlights the button to generate the segments:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa0919eac2da8e828a2559136dda3b8965dadaa8.jpeg" data-download-href="/uploads/short-url/zFURKsEGQcuvW30NdpGfIgTNLqU.jpeg?dl=1" title="Slicer-Liver_screenshot_23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa0919eac2da8e828a2559136dda3b8965dadaa8_2_690x427.jpeg" alt="Slicer-Liver_screenshot_23" data-base62-sha1="zFURKsEGQcuvW30NdpGfIgTNLqU" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa0919eac2da8e828a2559136dda3b8965dadaa8_2_690x427.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa0919eac2da8e828a2559136dda3b8965dadaa8_2_1035x640.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa0919eac2da8e828a2559136dda3b8965dadaa8_2_1380x854.jpeg 2x" data-dominant-color="AFB0BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer-Liver_screenshot_23</span><span class="informations">1569×971 331 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Make sure you have the latest version of Slicer and Slicer-Liver as this functionality has been recently added. This may explain if you did not find the button.</p>

---

## Post #28 by @ThomasHusson (2025-03-28 19:07 UTC)

<p>For those who used TotalSegmentator : just add English subtitles on my YouTube Tutorial :</p><div class="youtube-onebox lazy-video-container" data-video-id="FywayDfP9t0" data-video-title="Liver Volumetry Using 3DSlicer - Tutorial" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=FywayDfP9t0" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/FywayDfP9t0/maxresdefault.jpg" title="Liver Volumetry Using 3DSlicer - Tutorial" width="690" height="388">
  </a>
</div>


---

## Post #29 by @psychicpotato (2025-04-03 18:33 UTC)

<p>Hey <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a></p>
<p>Sorry to bug you on this, but I’m having the same problem <a class="mention" href="/u/johny723">@johny723</a> is experiencing. While being able to resect the liver using the curved plane, and calculating the volume of the resected segments in the volumetry module (the output table reads nicely), I’m unable to find get the ‘Generate segments based on selected resections and ROI markers’ button to appear.</p>
<p>I’m currently running Slicer 5.8.1, and running the SlicerLiver extension a767755.</p>
<p>Any pointers are hugely appreciated! Thanks so much.</p>

---

## Post #30 by @RafaelPalomar (2025-04-04 10:20 UTC)

<p>Hello <a class="mention" href="/u/psychicpotato">@psychicpotato</a>. I’ve been reviewing this case and I have pushed some changes to Slicer-Liver. These changes should enable the missing button. The extension will be most likely available from tomorrow, when a new build is triggered. I’ll check on Monday to make sure everything’s in order.</p>

---

## Post #31 by @psychicpotato (2025-04-04 13:22 UTC)

<p>Amazing - thanks so much <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a>!</p>

---

## Post #32 by @RafaelPalomar (2025-04-07 10:36 UTC)

<p><a class="mention" href="/u/johny723">@johny723</a>, <a class="mention" href="/u/psychicpotato">@psychicpotato</a>. I tested the extension earlier this morning and it builds now with the segmentation separation based on  a resection. We are currently working on a video tutorial, however, there are written instructions at <a href="https://github.com/ALive-research/Slicer-Liver?tab=readme-ov-file#resection-volumetry" rel="noopener nofollow ugc">https://github.com/ALive-research/Slicer-Liver?tab=readme-ov-file#resection-volumetry</a>.</p>
<p>Let me know if this works for you.</p>

---

## Post #33 by @psychicpotato (2025-04-07 18:51 UTC)

<p>Hey <a class="mention" href="/u/rafaelpalomar">@RafaelPalomar</a> - Fantastic! Working as intended, I’m able to see the button, transect the volume into 2 separate segmentations, and output the resulting OBJ files. Thanks so much for the quick turnover!!</p>

---

## Post #34 by @johny723 (2025-04-10 20:26 UTC)

<p>It finally works. Thank you!</p>

---
