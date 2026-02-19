---
topic_id: 1690
title: "How To Apply Intensity Normalization To Mri Mha With Slicer"
date: 2017-12-19
url: https://discourse.slicer.org/t/1690
---

# How to apply intensity normalization to MRI(.mha) with Slicer

**Topic ID**: 1690
**Date**: 2017-12-19
**URL**: https://discourse.slicer.org/t/how-to-apply-intensity-normalization-to-mri-mha-with-slicer/1690

---

## Post #1 by @hei6775 (2017-12-19 14:58 UTC)

<p>Hi,<br>
I am working with a project of brain segmentation and need to preprocess my MRI(from BRATS2015). I have applied N4ITK within Slicer, but I cannot find out how to apply intensity normalization with Slicer 4.6.2. Or is there any normal ways I can use to normalize my MRI.<br>
And,I want to look the histogram of MRI 3D image.how to do it?<br>
Thank you all!!!</p>

---

## Post #2 by @pieper (2017-12-19 16:19 UTC)

<p>You can use SimpleFilters and the NormalizeImageFilter and then look at the histogram in the Volumes module.</p>
<p>HTH,<br>
Steve</p>

---

## Post #3 by @hei6775 (2017-12-20 09:22 UTC)

<p>hi,i apply on my files.But the result is not my want to get.I want to get like:<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9126229b4f4b109b447f517386c24cc2a6ae63e7.png" data-download-href="/uploads/short-url/kI2W7Cvmc7EfTXAD0TfhA3w3lzh.png?dl=1" title="01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/9126229b4f4b109b447f517386c24cc2a6ae63e7_2_690x265.png" alt="01" data-base62-sha1="kI2W7Cvmc7EfTXAD0TfhA3w3lzh" width="690" height="265" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/9126229b4f4b109b447f517386c24cc2a6ae63e7_2_690x265.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9126229b4f4b109b447f517386c24cc2a6ae63e7.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/9126229b4f4b109b447f517386c24cc2a6ae63e7.png 2x" data-dominant-color="FCF8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">01</span><span class="informations">819×315 35.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @hei6775 (2017-12-20 09:24 UTC)

<p>yes,but it has some problem</p>

---

## Post #5 by @pieper (2017-12-20 14:41 UTC)

<p>If you want to normalize all the images to the same range then you’ll need to write a small script.  There’s not built-in tool that does that.  If you are comfortable writing a script but want specific suggestions let us know.</p>

---

## Post #6 by @lassoan (2017-12-20 15:36 UTC)

<p>For more refined, interactive plotting, you can create a histogram and show in a plot view, as it is done in this example: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_histogram_plot_of_a_volume" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/bacf5bb20045a5d547179ad820d35156b7084fa6.jpeg" data-download-href="/uploads/short-url/qEB4uaKuQ4N7ciwvklzusngWFzU.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bacf5bb20045a5d547179ad820d35156b7084fa6_2_690x484.jpg" alt="image" data-base62-sha1="qEB4uaKuQ4N7ciwvklzusngWFzU" width="690" height="484" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bacf5bb20045a5d547179ad820d35156b7084fa6_2_690x484.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bacf5bb20045a5d547179ad820d35156b7084fa6_2_1035x726.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/bacf5bb20045a5d547179ad820d35156b7084fa6_2_1380x968.jpg 2x" data-dominant-color="605E59"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2185×1533 515 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @kayarre (2018-09-10 18:12 UTC)

<p>This is very helpful, how would you suggest doing this if you want compare the histograms of multiple images as in the images above?</p>
<p>basically make a loop around this for each image? is there a way to get the histogram that is already shown in the volumes module and plot that blue line for each image?</p>

---

## Post #8 by @lassoan (2018-09-10 18:24 UTC)

<aside class="quote no-group" data-username="kayarre" data-post="7" data-topic="1690">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>how would you suggest doing this if you want compare the histograms of multiple images as in the images above?</p>
</blockquote>
</aside>
<p>You can add any number of series in a chart. So, yes, you can just iterate through all relevant volume nodes, create a plot series for each, and add it to the chart.</p>
<aside class="quote no-group" data-username="kayarre" data-post="7" data-topic="1690">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>is there a way to get the histogram that is already shown in the volumes module</p>
</blockquote>
</aside>
<p>Volumes module only computes histogram for the currently selected volume and I’m not sure that even this histogram is exposed through a public API.</p>
<p>Since you can compute the histogram in near-zero time, with a single line of code, with full control of histogram bins, it makes sense to follow the method shown in the example Python script.</p>
<p>Note that in recent nightly builds, <code>slicer.util.plot</code> function can even furher simplify the syntax:</p>
<pre><code># Get a volume node
import SampleData
volumeNode = SampleData.SampleDataLogic().downloadMRHead()

# Plot histogram
import numpy as np
histogram = np.histogram(arrayFromVolume(volumeNode), bins=50)
chartNode = plot(histogram, xColumnIndex = 1)
</code></pre>

---
