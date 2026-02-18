# Exporting plots from Slicer

**Topic ID**: 5711
**Date**: 2019-02-09
**URL**: https://discourse.slicer.org/t/exporting-plots-from-slicer/5711

---

## Post #1 by @muratmaga (2019-02-09 06:37 UTC)

<p>Beyond screen capture, what is the option to export a plot from Slicer. If possible in SVG format or at least some bitmap?</p>

---

## Post #2 by @lassoan (2019-02-09 14:14 UTC)

<p>VTK should be able to export plots as postscript file (see <a href="https://vtk.org/doc/nightly/html/classvtkGL2PSExporter.html" rel="nofollow noopener">https://vtk.org/doc/nightly/html/classvtkGL2PSExporter.html</a>). You may also experiment with anti-aliasing options and view size to get high-quality output suitable for printing.</p>

---

## Post #3 by @muratmaga (2019-02-09 17:04 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>. Will take a careful look. Cursory examination suggests it is dependent on a library called gl2ps (<a href="http://www.geuz.org/gl2ps/" rel="nofollow noopener">http://www.geuz.org/gl2ps/</a>), is this available with the VTK distributed with Slicer, or would it require custom build?</p>

---

## Post #4 by @pieper (2019-02-09 17:43 UTC)

<p>I didn’t try with a plot, but the class does work in Slicer as shown below.  Looks like we just need to add an accessor to get the renderWindow from a chart view.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; e = vtk.vtkGL2PSExporter()
&gt;&gt;&gt; e.SetFileFormatToSVG()
&gt;&gt;&gt; lm = slicer.app.layoutManager()
&gt;&gt;&gt; e.SetRenderWindow(lm.sliceWidget('Red').sliceView().renderWindow())
&gt;&gt;&gt; e.SetFilePrefix('/tmp/red')
&gt;&gt;&gt; e.Update()
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/562a4e2a4302a6e0efe6ff48bbb057226ecbc5e3.png" data-download-href="/uploads/short-url/cifHttdbDirHnX7E7piX4amIWjx.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/562a4e2a4302a6e0efe6ff48bbb057226ecbc5e3_2_690x316.png" alt="image" data-base62-sha1="cifHttdbDirHnX7E7piX4amIWjx" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/562a4e2a4302a6e0efe6ff48bbb057226ecbc5e3_2_690x316.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/562a4e2a4302a6e0efe6ff48bbb057226ecbc5e3.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/562a4e2a4302a6e0efe6ff48bbb057226ecbc5e3.png 2x" data-dominant-color="59585A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">909×417 73.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @muratmaga (2019-02-09 19:00 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> my specific concerns is the Plots. Slice view is straightforward with available Snapshot tool.<br>
SVG is more relevant for plots, as the user can modify the colors/symbols etc…</p>

---

## Post #6 by @pieper (2019-02-09 19:28 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="5711">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> my specific concerns is the Plots.</p>
</blockquote>
</aside>
<p>Of course I know that!</p>
<p>This was just a demo to show you that the gl2ps code is bundled with Slicer.  The plots should work the same if one used their render window instead of the slice view render window.</p>

---

## Post #7 by @pieper (2019-02-10 00:00 UTC)

<p>I <a href="https://github.com/Slicer/Slicer/commit/13dc03cb1ffbd1599a6ffa4823254155263c5db8">added a hook</a> to export plots svg, which is available via python for now.  I’m thinking it would make sense to add a Save As button to the qMRMLPlotViewControllerWidget for this.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08eb84373bdbd1985432f1229e5543cf27237360.png" data-download-href="/uploads/short-url/1gUpvGvPESwCfarIZWI3hWYJ0Hu.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08eb84373bdbd1985432f1229e5543cf27237360_2_690x356.png" alt="image" data-base62-sha1="1gUpvGvPESwCfarIZWI3hWYJ0Hu" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08eb84373bdbd1985432f1229e5543cf27237360_2_690x356.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08eb84373bdbd1985432f1229e5543cf27237360_2_1035x534.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08eb84373bdbd1985432f1229e5543cf27237360_2_1380x712.png 2x" data-dominant-color="F6F6F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1628×840 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @pieper (2019-02-11 16:08 UTC)

<p>I went ahead and added a Save button to the plot controller popup.  I also confirmed the SVG output is in vector form, not raster, so it should look good in print or at least it won’t have rasterization effects).</p>

---
