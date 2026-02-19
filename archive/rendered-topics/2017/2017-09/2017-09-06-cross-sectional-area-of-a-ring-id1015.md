---
topic_id: 1015
title: "Cross Sectional Area Of A Ring"
date: 2017-09-06
url: https://discourse.slicer.org/t/1015
---

# Cross Sectional Area of a Ring

**Topic ID**: 1015
**Date**: 2017-09-06
**URL**: https://discourse.slicer.org/t/cross-sectional-area-of-a-ring/1015

---

## Post #1 by @victoria.rose (2017-09-06 17:54 UTC)

<p>I am looking to calculate the cross sectional area at multiple points around the ring (I tried to mark where I would like to slice the ring and measure the area using pairs of fiducials in the image below).</p>
<p>I am not sure what the best method is as the orientation of the slice is constantly changing, so I’m just looking for an idea of what add-on or method would be best. Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ebb246889d2b85c9f1cb84b30ccebe398acad4e.jpeg" data-download-href="/uploads/short-url/26jDmISbHdABbbUkMlpOpQHY8aO.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/0ebb246889d2b85c9f1cb84b30ccebe398acad4e_2_552x500.jpg" alt="image" data-base62-sha1="26jDmISbHdABbbUkMlpOpQHY8aO" width="552" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/0ebb246889d2b85c9f1cb84b30ccebe398acad4e_2_552x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ebb246889d2b85c9f1cb84b30ccebe398acad4e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0ebb246889d2b85c9f1cb84b30ccebe398acad4e.jpeg 2x" data-dominant-color="757594"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">700×634 76 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2017-09-06 23:41 UTC)

<p>You can define a curved path and reslice the image along that path as shown in this video:</p>
<div class="lazyYT" data-youtube-id="thExIlffL0I" data-youtube-title="Curved multi-planar reconstruction (MPR) view in 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>Once you have the slice views in correct orientation, you can use the ruler tool (available in the toolbar) to measure diameter.</p>

---

## Post #3 by @victoria.rose (2017-09-12 14:12 UTC)

<p>Perfect that is exactly what I was looking for!</p>
<p>I want to loop through screen shots for each frame of a created path (~30). Is it possible to code a loop taking snapshots and labeling them in the Python interactor?</p>
<p>Thanks!</p>

---

## Post #4 by @lassoan (2017-09-12 15:30 UTC)

<p>It’s easy to create screen captures from scripts, see examples in the script repository:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture</a></p>
<p>If you are interested in Python scripting, you could modify the Endoscopy module to save each timepoint’s transform into a Sequence module creates a sequence node and saves transforms into it). After that you can use the ScreenCapture module’s <code>sequence</code> animation mode to record a movie.</p>
<p>THe implementation would be probably about 20-30 lines of code in <a href="http://Endoscopy.py">Endoscopy.py</a>. You can have a look at <a href="https://github.com/moselhy/SlicerSequenceRegistration">SequenceRegistration</a> module for an example how to create a sequence node and store transforms in it. I would be happy to help if you stuck at any point with the implementation.</p>

---

## Post #5 by @victoria.rose (2017-09-13 14:50 UTC)

<p>Thanks for the code links, they were very helpful! Although I’m sure that is a much more elegant way to accomplish what I need, I am very new to Python and Slicer so I wrote a basic script to take images (and slice location) at specified points of the transform:</p>
<pre><code>lm = slicer.app.layoutManager()
yellow = lm.sliceWidget('Yellow')
yellowLogic = yellow.sliceLogic()
height = []

layoutName = 'Yellow'
imagePathPattern = 'C:/image-%d.png'
count = 25

slicer.modules.endoscopy.widgetRepresentation().self().frameSlider.value = 0
for step in range(count+1):
    image = qt.QPixmap.grabWidget(view).toImage()
    image.save(imagePathPattern % step)
    slicer.modules.endoscopy.widgetRepresentation().self().frameSlider.value = slicer.modules.endoscopy.widgetRepresentation().self().frameSlider.value + 1
    view.forceRender()
    height.append(yellowLogic.GetSliceOffset())

print height
</code></pre>
<p>I am sure it’s rough code but it gets the job done. Thanks again!</p>

---
