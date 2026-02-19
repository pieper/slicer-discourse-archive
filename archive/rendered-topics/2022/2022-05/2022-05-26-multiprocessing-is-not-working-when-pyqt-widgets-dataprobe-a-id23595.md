---
topic_id: 23595
title: "Multiprocessing Is Not Working When Pyqt Widgets Dataprobe A"
date: 2022-05-26
url: https://discourse.slicer.org/t/23595
---

# Multiprocessing is not working when PyQt widgets , DataProbe and DicomLib are used.

**Topic ID**: 23595
**Date**: 2022-05-26
**URL**: https://discourse.slicer.org/t/multiprocessing-is-not-working-when-pyqt-widgets-dataprobe-and-dicomlib-are-used/23595

---

## Post #1 by @roopesh (2022-05-26 14:40 UTC)

<p>I am running an algorithm in a python script using command line with --python-script command, which has  a custom button created in slicer UI, when I trigger this button , algorithm will start, which is using multiprocessing and creating spawn type context object and runs several processes. When I did that I am getting error as below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4dbc8e51422b4e604441d5182882b6a7042e0c50.png" data-download-href="/uploads/short-url/b5GK9BVanWBOKoWDdIBEP8nSoCY.png?dl=1" title="Screenshot from 2022-05-26 16-40-21" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4dbc8e51422b4e604441d5182882b6a7042e0c50_2_690x220.png" alt="Screenshot from 2022-05-26 16-40-21" data-base62-sha1="b5GK9BVanWBOKoWDdIBEP8nSoCY" width="690" height="220" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4dbc8e51422b4e604441d5182882b6a7042e0c50_2_690x220.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4dbc8e51422b4e604441d5182882b6a7042e0c50_2_1035x330.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4dbc8e51422b4e604441d5182882b6a7042e0c50_2_1380x440.png 2x" data-dominant-color="383838"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2022-05-26 16-40-21</span><span class="informations">1441×461 89.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I removed the places wherever I am using QtWidgets, DataProbe and DicomLib then the python script is running multiprocessing and algorithm  successfully.  These libraries are required for my complete functionality, so I can’t remove them.  Please help me here.</p>

---

## Post #2 by @roopesh (2022-05-31 03:58 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Please help me out here, its kinda urgent.</p>

---

## Post #3 by @lassoan (2022-05-31 04:08 UTC)

<p>Most objects are only usable on a single thread. Therefore, you usually cannot simply run the same code in a processing thread that works on the main thread.</p>
<p>You can only run processing in the worker threads and you must not access GUI widgets and application objects. See <a href="https://github.com/pieper/SlicerParallelProcessing" class="inline-onebox">GitHub - pieper/SlicerParallelProcessing: Slicer modules for running subprocesses to operate on data in parallel</a> extension for examples of how you can implement parallel processing in Python in Slicer.</p>

---
