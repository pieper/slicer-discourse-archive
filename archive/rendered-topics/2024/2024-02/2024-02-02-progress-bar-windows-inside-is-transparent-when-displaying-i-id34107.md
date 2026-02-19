---
topic_id: 34107
title: "Progress Bar Windows Inside Is Transparent When Displaying I"
date: 2024-02-02
url: https://discourse.slicer.org/t/34107
---

# Progress bar window's inside is transparent when displaying it

**Topic ID**: 34107
**Date**: 2024-02-02
**URL**: https://discourse.slicer.org/t/progress-bar-windows-inside-is-transparent-when-displaying-it/34107

---

## Post #1 by @Gabriel_J (2024-02-02 08:20 UTC)

<p>Hello,</p>
<p>I’m developing a Python plugin using the Extension Wizard template as the code basis, and I would like to add a loading bar.</p>
<p>I’ve seen that it can be done like this:</p>
<pre data-code-wrap="python"><code class="lang-python">progress_bar = slicer.util.createProgressDialog(parent=slicer.util.mainWindow(), autoClose=False, labelText="Please wait", windowTitle="Painting contour...", value=0)
progress_bar.setCancelButton(None)
slicer.app.processEvents()
</code></pre>
<p>Here’s a screenshot of what it looks like:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43b8c40a1b107105c25cb099b85508a590bf0de5.jpeg" data-download-href="/uploads/short-url/9F5QF0aeQpLrgHTb1rwGcH1giTr.jpeg?dl=1" title="Screenshot from 2024-01-31 21-47-26" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43b8c40a1b107105c25cb099b85508a590bf0de5_2_690x362.jpeg" alt="Screenshot from 2024-01-31 21-47-26" data-base62-sha1="9F5QF0aeQpLrgHTb1rwGcH1giTr" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43b8c40a1b107105c25cb099b85508a590bf0de5_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43b8c40a1b107105c25cb099b85508a590bf0de5_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43b8c40a1b107105c25cb099b85508a590bf0de5.jpeg 2x" data-dominant-color="686882"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-01-31 21-47-26</span><span class="informations">1368×718 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>How can I make the window appear correctly?<br>
Note that the window is encapsulated within:</p>
<pre data-code-wrap="python"><code class="lang-python">with slicer.util.tryWithErrorDisplay("Failed to compute segmentation.", waitCursor=True):
</code></pre>
<p>and when an error occurs, it displays the error window and the progress bar window correctly (with the bar, the inside text and the window background).</p>
<p>I’m using Slicer 5.4.0 r31938 / 311cb26 on Ubuntu LTS 22.04.3.</p>

---

## Post #2 by @Gabriel_J (2024-02-06 07:51 UTC)

<p>Actually, updating the value of the bar, and using slicer.app.processEvents()<br>
make the background appear, so my issue is no more an issue.</p>

---
