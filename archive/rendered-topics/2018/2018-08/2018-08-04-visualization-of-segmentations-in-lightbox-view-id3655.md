# Visualization of segmentations in lightbox view

**Topic ID**: 3655
**Date**: 2018-08-04
**URL**: https://discourse.slicer.org/t/visualization-of-segmentations-in-lightbox-view/3655

---

## Post #1 by @dcantor (2018-08-04 05:24 UTC)

<p>Hello slicers!</p>
<p>I just noticed that segmentations do not appear in the Lightbox  view. I am attaching an image for reference:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa30ebfe6f1286296d316e3fe5a686fffe2ac2d3.png" data-download-href="/uploads/short-url/zHibim8lbZiCcScKvXKYE4FtYUH.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa30ebfe6f1286296d316e3fe5a686fffe2ac2d3_2_690x315.png" alt="image" data-base62-sha1="zHibim8lbZiCcScKvXKYE4FtYUH" width="690" height="315" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa30ebfe6f1286296d316e3fe5a686fffe2ac2d3_2_690x315.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa30ebfe6f1286296d316e3fe5a686fffe2ac2d3_2_1035x472.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa30ebfe6f1286296d316e3fe5a686fffe2ac2d3_2_1380x630.png 2x" data-dominant-color="8E8E8D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1392×636 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In my example, the segmentation occurs over a series of consecutive slices but it does not show in this view. Is this a bug?</p>
<p>Thanks,</p>
<p>Diego</p>

---

## Post #2 by @lassoan (2018-08-04 07:09 UTC)

<p>Lightbox view has not been maintained/improved in recent years because it would have been too much work to make all features lightbox-view-compatible and we are not aware that many people use it. Most likely dynamic lightbox view will be replaced by a module that generates static lightbox image.</p>

---

## Post #3 by @dcantor (2018-08-04 13:25 UTC)

<p>I think a functionality where you can see the outline of the pathology/tumour in a 2D series would be really useful to radiologists in general. Maybe something to consider to increase user adoption.</p>
<p>Regards,</p>
<p>Diego</p>

---

## Post #4 by @lassoan (2018-08-04 13:51 UTC)

<p>My impression is that ability to see anatomy in dynamic reformatted slice views, 3D views, and in virtual reality made lightbox viewing less relevant. Do you have specific use case in mind and important requirements for lightbox views? Who would use it, how, and for what purposes?</p>

---

## Post #5 by @dcantor (2018-08-04 14:21 UTC)

<p>Hi Andras,</p>
<p>I understand where you are coming from. The request to visualize the outline of a tumour in a 2D series (please refer to the image in my original post) actually came from one of the radiologists I work with. She is using a different tool and I was trying to show her how to do this in Slicer.</p>
<p>Diego</p>

---

## Post #6 by @pieper (2018-08-04 19:21 UTC)

<p><a class="mention" href="/u/dcantor">@dcantor</a> the <a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/CompareVolumes">CompareVolumes</a> module provides functionality like you are looking for.  Currently it shows the full volume in a 3x3 layout but  the <a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/CompareVolumes">underlying code</a> can do other layouts so just a couple lines of python code would be needed.</p>

---

## Post #7 by @fedorov (2018-08-06 12:59 UTC)

<aside class="quote no-group" data-username="dcantor" data-post="5" data-topic="3655">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dcantor/48/782_2.png" class="avatar"> dcantor:</div>
<blockquote>
<p>The request to visualize the outline of a tumour in a 2D series (please refer to the image in my original post) actually came from one of the radiologists I work with. She is using a different tool and I was trying to show her how to do this in Slicer.</p>
</blockquote>
</aside>
<p>Diego, can you ask the radiologist about why that particular way of looking at the series is preferred? Is it because she wants to quickly see all slices where tumor is contoured for efficiency purposes, or she wants to see all of the slices to evaluate agreement/inconsistencies between the slices? It would be interesting to understand the reasons.</p>
<p>I also work with radiologists in prostate cancer MRI applications, and they never brought it up to have this feature. In my experience, scrolling through the series with the segmentation overlay is what they need.</p>

---

## Post #8 by @lassoan (2020-03-25 23:31 UTC)

<p>FYI, a new lightbox view generation feature was added that is compatible with segmentations. See details here: <a href="https://discourse.slicer.org/t/new-lightbox-contact-image-mode-in-screen-capture-module/10840" class="inline-onebox">New lightbox (contact image) mode in screen capture module</a></p>

---
