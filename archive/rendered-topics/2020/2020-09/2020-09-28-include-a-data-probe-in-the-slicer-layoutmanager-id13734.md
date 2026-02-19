---
topic_id: 13734
title: "Include A Data Probe In The Slicer Layoutmanager"
date: 2020-09-28
url: https://discourse.slicer.org/t/13734
---

# Include a data probe in the slicer layoutmanager

**Topic ID**: 13734
**Date**: 2020-09-28
**URL**: https://discourse.slicer.org/t/include-a-data-probe-in-the-slicer-layoutmanager/13734

---

## Post #1 by @Chintha_Siva_Prasad (2020-09-28 13:35 UTC)

<p>How can I include a data probe in the slicer layout manager?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2944d19ee1ee829db963c496f3477e7bd654454.png" data-download-href="/uploads/short-url/wkpDOkZTFsryDhTCWrjPrXfgffC.png?dl=1" title="Screenshot from 2020-09-03 19-50-34" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2944d19ee1ee829db963c496f3477e7bd654454_2_690x387.png" alt="Screenshot from 2020-09-03 19-50-34" data-base62-sha1="wkpDOkZTFsryDhTCWrjPrXfgffC" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2944d19ee1ee829db963c496f3477e7bd654454_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2944d19ee1ee829db963c496f3477e7bd654454_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2944d19ee1ee829db963c496f3477e7bd654454.png 2x" data-dominant-color="E3E7E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-09-03 19-50-34</span><span class="informations">1366×768 148 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I want to insert a data probe in this layout.</p>

---

## Post #2 by @lassoan (2020-09-28 13:58 UTC)

<p>You can insert any Qt widget into the layout using <code>qSlicerSingletonViewFactory</code>. See how <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOM/DICOM.py">DICOM.py</a> displays <code>self.viewWidget</code> as an example.</p>

---

## Post #3 by @Chintha_Siva_Prasad (2020-09-28 14:07 UTC)

<p>I just want to put the native slicer data probe into the layout. I dont want to create any new instances. If I use this approach how can I get dataprobe widget instance of the slicer?</p>

---

## Post #4 by @lassoan (2020-09-28 15:01 UTC)

<p>You can only put a Qt widget at one place at a time, therefore you need to create a new instance of the data probe. You probably need to customize that widget anyway to look good in the view layout.</p>

---

## Post #5 by @Chintha_Siva_Prasad (2020-09-29 05:18 UTC)

<p>How can I create a new data probe instance and connect them to slice nodes?<br>
Isn’t it a hard task? Even if so could you show me how to do that?</p>

---

## Post #6 by @lassoan (2020-09-29 13:39 UTC)

<p>You can instantiate a new data probe like this:</p>
<pre><code class="lang-python">import DataProbe
w = DataProbe.DataProbeInfoWidget()
w.frame.show()
</code></pre>

---
