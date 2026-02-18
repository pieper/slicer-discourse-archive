# Watermark feature

**Topic ID**: 8252
**Date**: 2019-09-01
**URL**: https://discourse.slicer.org/t/watermark-feature/8252

---

## Post #1 by @muratmaga (2019-09-01 22:29 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a>.</p>
<p>We finished our first SlicerMorph workshop and our trainees pretty much feel in love with Slicer and its capabilities (check out <a href="https://twitter.com/SlicerMorph/status/1168022612313686016" rel="nofollow noopener">https://twitter.com/SlicerMorph/status/1168022612313686016</a> for some visualizations). We got four more to go, and I am hoping Slicer will have even large following within the biosciences community. Even the alpha version of SlicerAnimator liked quite a bit.</p>
<p>Anyways, I thought it would be cool to display an optional small watermark in the volume rendering window that will essentially show the nice sticker Kitware designed (from this thread <a href="https://discourse.slicer.org/t/feedback-on-slicer-sticker-design/6395" class="inline-onebox">Feedback on Slicer Sticker design</a>).</p>
<p>I am sure a lot of them would proudly display, if it is only a single click to enable it. I would.</p>

---

## Post #2 by @pieper (2019-09-01 23:43 UTC)

<p>(First - thanks for posting the images from the workshop - glad it went well!)</p>
<p>A watermark is a great idea.  There’s actually a <a href="https://vtk.org/doc/nightly/html/classvtkLogoWidget.html" rel="nofollow noopener">vtkLogoWidget</a> that was added to support exactly this use case in Slicer (search for ‘watermark’ on <a href="https://www.slicer.org/wiki/Slicer3:VisualBlog" rel="nofollow noopener">this page</a>) but we never ended up enabling it for whatever reason.</p>
<p>Anyway, if you want to try it out here’s a snippet that works in any recent slicer.  I’m sure we can improve the esthetics.</p>
<pre><code class="lang-auto">import os

logoURL = 'https://www.slicer.org/w/images/7/71/3DSlicerLogo-DesktopIcon-128x128.png'
pngPath = os.path.join(slicer.app.temporaryPath, "SlicerLogo.png")
slicer.util.downloadFile(logoURL, pngPath)

reader = vtk.vtkPNGReader()
reader.SetFileName(pngPath)
reader.Update()

logoRepresentation = vtk.vtkLogoRepresentation()
logoRepresentation.SetImage(reader.GetOutput())
logoRepresentation.SetPosition(0,0)
logoRepresentation.SetPosition2(.2, .2)
logoRepresentation.GetImageProperty().SetOpacity(.7)

logoWidget = vtk.vtkLogoWidget()
renderWindow = slicer.app.layoutManager().threeDWidget(0).threeDView().renderWindow()
logoWidget.SetInteractor(renderWindow.GetInteractor())
logoWidget.SetRepresentation(logoRepresentation)

logoWidget.On()
renderWindow.Render()

</code></pre>

---

## Post #3 by @lassoan (2019-09-04 02:46 UTC)

<p>I’ve added watermark option to Screen Capture module (in Advanced section):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09e06aa583db44081c9695e441b89559f328154b.png" data-download-href="/uploads/short-url/1pn6FrILC7HN4O2UJcUE2uvurxx.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/9/09e06aa583db44081c9695e441b89559f328154b.png" alt="image" data-base62-sha1="1pn6FrILC7HN4O2UJcUE2uvurxx" width="690" height="472" data-dominant-color="F2F1F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1079×739 42.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Example watermark with opacity = 100%:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/2/22fb614f3b26fc3a5e092277aaf60d8930fd6bb5.jpeg" alt="image" data-base62-sha1="4ZsOqJXeXsztRmywaGvOoT4jDhP" width="588" height="496"></p>
<p>Example watermark with opacity = 40%:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5ac873bd8d5e3c63084ad46cc899f31589049267.jpeg" data-download-href="/uploads/short-url/cX6rdxPSqPN299Kz6QGelfHSNSL.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ac873bd8d5e3c63084ad46cc899f31589049267_2_508x500.jpeg" alt="image" data-base62-sha1="cX6rdxPSqPN299Kz6QGelfHSNSL" width="508" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5ac873bd8d5e3c63084ad46cc899f31589049267_2_508x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5ac873bd8d5e3c63084ad46cc899f31589049267.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5ac873bd8d5e3c63084ad46cc899f31589049267.jpeg 2x" data-dominant-color="575661"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">588×578 99.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The feature will be available in Preview Release rev28477.</p>

---

## Post #4 by @muratmaga (2019-09-04 03:14 UTC)

<p>thanks <a class="mention" href="/u/lassoan">@lassoan</a> !!!</p>

---

## Post #5 by @lassoan (2023-03-21 03:13 UTC)



---
