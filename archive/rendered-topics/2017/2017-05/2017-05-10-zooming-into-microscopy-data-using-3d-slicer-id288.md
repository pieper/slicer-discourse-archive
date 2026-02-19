---
topic_id: 288
title: "Zooming Into Microscopy Data Using 3D Slicer"
date: 2017-05-10
url: https://discourse.slicer.org/t/288
---

# Zooming into microscopy data using 3D Slicer

**Topic ID**: 288
**Date**: 2017-05-10
**URL**: https://discourse.slicer.org/t/zooming-into-microscopy-data-using-3d-slicer/288

---

## Post #1 by @Fernando (2017-05-10 12:50 UTC)

<p>Hi all,</p>
<p>During <a href="https://www.na-mic.org/Wiki/index.php/2016_Summer_Project_Week" rel="nofollow noopener">2016 Summer Slicer Week</a> we worked on a <a href="https://www.na-mic.org/Wiki/index.php/2016_Summer_Project_Week/Brain_atlas_combining_histology_and_MRI" rel="nofollow noopener">project</a> using histology to build an atlas. <a class="mention" href="/u/pieper">@pieper</a> gave me some useful tips for this.</p>
<p>Here’s a video Tina asked me to upload:<br>
<div class="lazyYT" data-youtube-id="VdOux73uWXI" data-youtube-title="Zooming into microscopy data using 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div></p>
<p>Sonia and Steve said this could be interesting for <a class="mention" href="/u/fedorov">@fedorov</a> and the <code>Slicer Pathology</code> extension. More recently, Sonia was in Paris and asked me about the code for the widget. I told her I hadn’t shared it because it was not clean, not integrated and has a lot of limitations. She said I should share it as it is, since someone else might want to contribute to improve it and maybe integrate it into Slicer at some point. I’ve worked a bit in order to integrate the widget into <code>DataProbe.py</code>.</p>
<p>Some of the many caveats:</p>
<ol>
<li>Only 2D images are supported</li>
<li>Only RGB images supported (probably very easy to make it work for grayscale as well)</li>
<li>Currently uses the background image of the red slice</li>
</ol>
<p>Here’s the code: <a href="https://github.com/fepegar/Slicer-DataProbe-Histology/blob/master/DataProbe.py" rel="nofollow noopener">https://github.com/fepegar/Slicer-DataProbe-Histology/blob/master/DataProbe.py</a><br>
It replaces <code>Slicer-build/lib/Slicer-4.7/qt-scripted-modules/DataProbe.py</code>.</p>
<p>I tipically use the widget for images like <a href="https://www.dropbox.com/s/kj8wjbdau3k0u52/TC2_1_rgb_small.nii.gz?dl=0" rel="nofollow noopener">this</a> (that’s a downsampled version, as histology images are usually very large).</p>
<p>Best,<br>
Fernando</p>

---

## Post #2 by @Davide_Punzo (2017-05-10 17:45 UTC)

<p>Hi Fernando, thanks! This utility will be very useful also for my astronomical use cases. I guess the best way to allow extensions to use it, it is to clean and integrate the modifications in the core. The only problem will be to understand if it is useful also for the others and how to integrate it without making the interface too complicated and crowded (e.g., we want it only for the red slice, or also for the other ones? or a menu for swtiching?).</p>

---

## Post #3 by @lassoan (2017-05-10 19:27 UTC)

<p>Probably it’s better to put this into a docking widget (similarly to the Python interactor). The widget can be popped out, moved to another screen, etc. or can be snapped to a side of the screen or below/above any other docking widget. See an example here: <a href="https://github.com/SlicerRt/SlicerDebuggingTools/blob/master/NodeInfo/NodeInfo.py#L224-L257">https://github.com/SlicerRt/SlicerDebuggingTools/blob/master/NodeInfo/NodeInfo.py#L224-L257</a></p>
<p>I would not put anything into already too crowded and too big Data probe widget.</p>

---

## Post #4 by @pieper (2017-05-10 19:46 UTC)

<p>Seems like this could be a generalization of the Slice Intersections<br>
concept, but showing the borders of another slice view as an overlay on an<br>
slice view that has the same orientation and offset.  That would give a lot<br>
of flexibility since it would handle arbitrary orientations and would also<br>
allow panning and zooming of either slice (or showing multiple slice views<br>
at different zoom levels all with their outlines visible in the ones that<br>
are more zoomed out (or multiple insets in the same large image).</p>

---

## Post #5 by @lassoan (2017-05-10 19:51 UTC)

<p>That’s a great idea. We had problems in the past with intersection of nearly-parallel slices anyway (intersection lines showed up in unpredictable locations). If we detect that slices are parallel, we could show intersection with a ribbon around the slice boundary.</p>

---

## Post #6 by @Fernando (2017-05-10 20:16 UTC)

<p>Good ideas! Something like this? (This image is photoshopped)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38a6809811b9e4f4c6632be4ec45d8c4828f2adb.jpeg" data-download-href="/uploads/short-url/859t0GLmH8ksaBMzj96HfXVw4CD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38a6809811b9e4f4c6632be4ec45d8c4828f2adb_2_690x372.jpeg" alt="image" data-base62-sha1="859t0GLmH8ksaBMzj96HfXVw4CD" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38a6809811b9e4f4c6632be4ec45d8c4828f2adb_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38a6809811b9e4f4c6632be4ec45d8c4828f2adb_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38a6809811b9e4f4c6632be4ec45d8c4828f2adb_2_1380x744.jpeg 2x" data-dominant-color="82828D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1440×778 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @lassoan (2017-05-10 20:23 UTC)

<p>Yes. It would be useful to improve slice intersection display also for thick slice reformatting (to show the slice thickness). vtkMRMLModelSliceDisplayableManager should be tuned to display slice intersections differently than regular model nodes (at least when the slice model is nearly parallel to the current slice and when slices are thick). Mantis issue describing incorrect slice intersection display for nearly-parallel slices: <a href="https://www.na-mic.org/Mantis/view.php?id=3360">https://www.na-mic.org/Mantis/view.php?id=3360</a></p>

---
