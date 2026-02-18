# Jupyter notebook with Slicer Preview

**Topic ID**: 11276
**Date**: 2020-04-23
**URL**: https://discourse.slicer.org/t/jupyter-notebook-with-slicer-preview/11276

---

## Post #1 by @smrolfe (2020-04-23 23:04 UTC)

<p>I’m working on a Slicer Jupyter notebook using the latest preview version (Mac OS 4.11.0-2020-04-19) but am getting an error when I try to display any images. The output is a broken image icon with no errors. I get the expected display when I try the same code block using the 4.10 stable kernel. To test I used sample code:</p>
<pre><code class="lang-auto">import SampleData
sampleDataLogic = SampleData.SampleDataLogic()
volume = sampleDataLogic.downloadMRHead()
slicer.app.layoutManager().setLayout(slicer.vtkMRMLLayoutNode.SlicerLayoutFourUpView)

display()
</code></pre>
<p>Are there any know issues with using Jupyter and Slicer Preview?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/1/01ec27be930caed5566a37c2533d6cb46bc83d0a.png" data-download-href="/uploads/short-url/h0r8LlOnF2D0wglfbLoo2IKlvA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01ec27be930caed5566a37c2533d6cb46bc83d0a_2_690x211.png" alt="image" data-base62-sha1="h0r8LlOnF2D0wglfbLoo2IKlvA" width="690" height="211" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01ec27be930caed5566a37c2533d6cb46bc83d0a_2_690x211.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01ec27be930caed5566a37c2533d6cb46bc83d0a_2_1035x316.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/1/01ec27be930caed5566a37c2533d6cb46bc83d0a_2_1380x422.png 2x" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2274×696 84.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @smrolfe (2020-04-24 00:26 UTC)

<p>To clarify, the Slicer app managed by Jupyter is displaying the correct visualization, but it’s not showing up in the notebook when using the preview version.</p>
<p>I’ve also tested using the latest preview version in Windows and have the same error.</p>

---

## Post #3 by @muratmaga (2020-04-24 20:05 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a><br>
Any input into this? This is same for me too (output displays only on the slicer window, not in the notebook).</p>

---

## Post #4 by @lassoan (2020-04-24 20:31 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> what operating system did you try this on?</p>

---

## Post #5 by @smrolfe (2020-04-24 20:47 UTC)

<p>I’ve replicated this on MacOS Mojave and Windows 10.</p>

---

## Post #6 by @pieper (2020-04-24 21:00 UTC)

<p>I don’t use the Jupyter interface myself, so I’m not sure what to suggest.  <a class="mention" href="/u/jcfr">@jcfr</a> might also have ideas.</p>

---

## Post #7 by @lassoan (2020-04-24 21:01 UTC)

<p>I could reproduce the issue and push a fix soon</p>

---

## Post #8 by @lassoan (2020-04-24 21:34 UTC)

<p>I’ve fixed the issue (it was related to byte buffer to string conversion, probably changed because of switching to UTF-8). It should work in tomorrow’s build but until then you can copy-paste this into a cell, run it, and then you can use <code>display2()</code> for capturing screenshot of the view layout:</p>
<pre><code class="lang-python">def display2():
    layoutManager = slicer.app.layoutManager()
    slicer.util.setViewControllersVisible(False)
    slicer.app.processEvents()
    slicer.util.forceRenderAllViews()
    screenshot = layoutManager.viewport().grab()
    slicer.util.setViewControllersVisible(True)
    bArray = qt.QByteArray()
    buffer = qt.QBuffer(bArray)
    buffer.open(qt.QIODevice.WriteOnly)
    screenshot.save(buffer, "PNG")
    slicer.modules.jupyterkernel.executeResultDataValue = bArray.toBase64().data().decode()
    slicer.modules.jupyterkernel.executeResultDataType = "image/png"
</code></pre>

---

## Post #9 by @smrolfe (2020-04-24 21:42 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>! Your temporary solution is working well for me.</p>

---

## Post #10 by @smrolfe (2020-04-27 22:20 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
I tested the updated SlicerJupyter extension in Windows and it is great! It fixes my display issues. It looks like the Mac build failed and is not available in the preview version.</p>

---
