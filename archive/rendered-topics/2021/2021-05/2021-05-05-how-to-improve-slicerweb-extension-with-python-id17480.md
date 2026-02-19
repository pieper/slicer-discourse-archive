---
topic_id: 17480
title: "How To Improve Slicerweb Extension With Python"
date: 2021-05-05
url: https://discourse.slicer.org/t/17480
---

# How to improve SlicerWeb extension with python?

**Topic ID**: 17480
**Date**: 2021-05-05
**URL**: https://discourse.slicer.org/t/how-to-improve-slicerweb-extension-with-python/17480

---

## Post #1 by @Pedro_Vitor_Abreu (2021-05-05 19:35 UTC)

<p>Hello there, I’m new with Slicer and this is my first topic, so I hope I get it to make it clear and straightforward.</p>
<p>I’ve been trying to create a comunication between a Django server and Slicer. The Django server then would have a button that would be used to export opened segmentation files.</p>
<p>My main option was to use <a href="https://github.com/pieper/SlicerWeb" rel="noopener nofollow ugc">SlicerWeb</a> extension, but I find that it can’t export segmentation files, though it can export volume files opened in Slicer perfectly well.</p>
<p>Is there any advice on how I could do that? I’ve been looking into the code of SlicerWeb but I couldn’t figure it out how to start. I guess that I could create a new function into SlicerWeb for a purpose like that.</p>
<p>Thanks<br>
Pedro</p>

---

## Post #2 by @pieper (2021-05-05 21:31 UTC)

<p>Hi Pedro -</p>
<p>The SlicerWeb code should probably be refactored at some point, but for now it can be extended by adding a branch in <a href="https://github.com/Slicer/Slicer/blob/44a0a9a2873c3915fc8de7a179902e27749b141d/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L656-L698">this set of if statements</a> to create a new rest endpoint, for example <code>&lt;root&gt;/slicer/segmentations</code> that would map to a request handler like <a href="https://github.com/Slicer/Slicer/blob/44a0a9a2873c3915fc8de7a179902e27749b141d/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L656-L698">this one for volumes</a> through which you can either download or upload via nrrd format.  It would just need to be call some of <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations">the segmentation api</a> in the request handler.</p>
<p>Hope that helps.</p>

---

## Post #3 by @Pedro_Vitor_Abreu (2021-05-09 16:15 UTC)

<p>Hey Steve, thanks for the solution!</p>
<p>I’ll take a look at these codes you indicated. Definitely it’s gonna help me.</p>
<p>Thanks again!<br>
Pedro</p>

---
