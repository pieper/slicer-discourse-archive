---
topic_id: 11277
title: "Get Image Intensity Histogram Of A Segment"
date: 2020-04-23
url: https://discourse.slicer.org/t/11277
---

# Get image intensity histogram of a segment

**Topic ID**: 11277
**Date**: 2020-04-23
**URL**: https://discourse.slicer.org/t/get-image-intensity-histogram-of-a-segment/11277

---

## Post #1 by @Benjamin_Coiffard (2020-04-23 21:36 UTC)

<p>I also need to export voxel intensities of a segmentation to analyse the histogram offline with my software. I applied this script in Python. What next? Where may I find the results?</p>

---

## Post #2 by @lassoan (2020-04-24 00:22 UTC)

<p>You can get the histogram of a segment in 6 lines of Python code as shown <strong><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-histogram-of-a-segmented-region">here</a></strong>. Just copy paste the example code into Slicer’s Python console to try it.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24e85549325158434201593fd038a04879f81941.png" data-download-href="/uploads/short-url/5guXxOGb5r8hu796KUd6UmwRJ3X.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24e85549325158434201593fd038a04879f81941_2_690x441.png" alt="image" data-base62-sha1="5guXxOGb5r8hu796KUd6UmwRJ3X" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24e85549325158434201593fd038a04879f81941_2_690x441.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24e85549325158434201593fd038a04879f81941_2_1035x661.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/24e85549325158434201593fd038a04879f81941_2_1380x882.png 2x" data-dominant-color="9B9B9B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1444 667 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @Benjamin_Coiffard (2020-05-04 12:18 UTC)

<p>Hi Andras,<br>
Thank you very much for answering.<br>
Your example doesn’t work but most likely because it has to be adapted to my node names? Here a copy of an example with the data names. Could you adapt the script to my situation? It will allow me to understand how it works and then being capable to fit the script to my other situations.<br>
I noticed that it is now possible to export the histogram in the Parenchyma Analysis module of CIP but the data are only available from -1024 to -350 HU and I need the whole data.<br>
Thank you very much for your help.<br>
I really appreciate it<br>
Regards<br>
Benjamin</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/4998a773e9ad1a4e4fd965730c38f71b4cf05ec4.jpeg" data-download-href="/uploads/short-url/av3UKixrih7WKjxgvcbRJtLQjNG.jpeg?dl=1" title="Example" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4998a773e9ad1a4e4fd965730c38f71b4cf05ec4_2_690x431.jpeg" alt="Example" data-base62-sha1="av3UKixrih7WKjxgvcbRJtLQjNG" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4998a773e9ad1a4e4fd965730c38f71b4cf05ec4_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4998a773e9ad1a4e4fd965730c38f71b4cf05ec4_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/9/4998a773e9ad1a4e4fd965730c38f71b4cf05ec4_2_1380x862.jpeg 2x" data-dominant-color="CCCCCD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Example</span><span class="informations">2880×1800 510 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2020-05-04 14:15 UTC)

<p>The link above points to a complete example, including generating sample data, to make sure that you can start from something that works and you can modify it step-by-step to do exactly what you need. If you work with your own data then replace “Generate input data” section and just set <code>masterVolumeNode</code> and <code>segmentationNode</code> to your nodes (e.g., <code>segmentationNode=getNode('Segmentation')</code>).</p>

---

## Post #5 by @Benjamin_Coiffard (2020-05-04 16:14 UTC)

<p>It works !!! Thanks so much +++++<br>
Sorry for my ignorance, I’m just a beginner in coding…<br>
Much appreciate<br>
Have a nice day<br>
B</p>

---

## Post #6 by @martflar (2023-01-17 18:41 UTC)

<p>Hi,<br>
Thanks for the really good example, I have an other problem.<br>
I am trying to make a histogram of a segment made using the Grow From Seeds module, but i can´t make it work.</p>
<p>This is the output format from the function i see in 3D slicer<br>
self.extentGrowthRatio = 0.1<br>
masterImageExtent = (0, 447, 0, 447, 0, 111)<br>
labelsEffectiveExtent = (100, 267, 61, 189, 35, 76)<br>
labelsExpandedExtent = [84, 283, 49, 201, 31, 80]</p>
<p>It would be great if someone could help with some code!</p>

---

## Post #7 by @lassoan (2023-01-17 18:49 UTC)

<aside class="quote no-group" data-username="martflar" data-post="6" data-topic="11277">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/db5fbb/48.png" class="avatar"> martflar:</div>
<blockquote>
<p>I am trying to make a histogram of a segment made using the Grow From Seeds module, but i can´t make it work.</p>
</blockquote>
</aside>
<p>It does not matter what segmentation tools you used for creating your segmentation. After you finished segmentation using <code>Grow from seeds</code>, click <code>Apply</code> and proceed the same way as you would do after using any other tool.</p>

---

## Post #8 by @martflar (2023-01-17 19:12 UTC)

<p>Thanks, Andreas, but I am still struggeling (sorry, real noobie here)<br>
For my imput data i use</p>
<p>segmentationNode=getNode(‘Segmentation’)<br>
masterVolumeNode=getNode(‘Segmentation’)</p>
<p>But i have no ideas on how to find the segmentID from the Grow From Seeds function<br>
I really appreciate such a quick answer on an old thread! <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @lassoan (2023-01-17 19:28 UTC)

<aside class="quote no-group" data-username="martflar" data-post="8" data-topic="11277">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/db5fbb/48.png" class="avatar"> martflar:</div>
<blockquote>
<p>masterVolumeNode=getNode(‘Segmentation’)</p>
</blockquote>
</aside>
<p>Use the grayscale volume as masterVolumeNode.</p>
<aside class="quote no-group" data-username="martflar" data-post="8" data-topic="11277">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/db5fbb/48.png" class="avatar"> martflar:</div>
<blockquote>
<p>i have no ideas on how to find the segmentID</p>
</blockquote>
</aside>
<p>You get the segment ID when you create the segment, you can store that and use later when you need it.</p>
<p>You can also get all the segment IDs by calling:</p>
<pre><code>segmentationNode.GetSegmentation().GetSegmentIDs()
</code></pre>
<p>If you want to get the segment ID from the segment name that you see in the application GUI:</p>
<pre><code>segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName(segmentName)
</code></pre>

---

## Post #10 by @martflar (2023-01-17 20:35 UTC)

<p>Thank you very much! Now it works! This was very helpful <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---
