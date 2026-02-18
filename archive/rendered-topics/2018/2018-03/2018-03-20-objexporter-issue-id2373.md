# ObjExporter issue

**Topic ID**: 2373
**Date**: 2018-03-20
**URL**: https://discourse.slicer.org/t/objexporter-issue/2373

---

## Post #1 by @anandmulay3 (2018-03-20 11:05 UTC)

<p>I’m trying to export model in .OBJ file …<br>
debug window error: obj files only support on renderer per window.</p>
<p>Code:</p>
<blockquote>
<blockquote>
<blockquote>
<p>o = vtk.vtkOBJExporter()<br>
o.SetFilePrefix(‘/tmp/obj/fibers’)<br>
lm = slicer.app.layoutManager()<br>
tdv = lm.threeDWidget(0).threeDView()<br>
rw = tdv.renderWindow()<br>
o.SetRenderWindow(rw)<br>
o.Write()</p>
</blockquote>
</blockquote>
</blockquote>
<p>whats wrong in this code… please help</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2018-03-20 17:23 UTC)

<p>There is an (unnecessary) limitation in the vtkOBJExporter that causes the issue. I’ve submitted a pull request with the fix (coincidentally, I’ve just worked on OBJ exporter problems and included this fix as well): <a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4084">https://gitlab.kitware.com/vtk/vtk/merge_requests/4084</a></p>
<p>Until the fix is integrated, you can use a workaround of moving the renderer to another render window. This allows the export to complete successfully and then the application crashes (if the goal is to just export to OBJ then the crash should not be an issue).</p>
<pre><code>lm = slicer.app.layoutManager()
tdv = lm.threeDWidget(0).threeDView()
rw = tdv.renderWindow()
# Move renderer temporarily into another renderWindow
# It will make the application crash, but it allows the scene export to complete successfully.
rw2 = vtk.vtkRenderWindow()
rw2.AddRenderer(rw.GetRenderers().GetFirstRenderer())
o = vtk.vtkOBJExporter()
o.SetFilePrefix('c:/tmp/test')
o.SetRenderWindow(rw2)
o.Write()</code></pre>

---

## Post #3 by @anandmulay3 (2018-03-21 07:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2373">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<pre><code class="lang-auto">lm = slicer.app.layoutManager()
tdv = lm.threeDWidget(0).threeDView()
rw = tdv.renderWindow()
# Move renderer temporarily into another renderWindow
# It will make the application crash, but it allows the scene export to complete successfully.
rw2 = vtk.vtkRenderWindow()
rw2.AddRenderer(rw.GetRenderers().GetFirstRenderer())
o = vtk.vtkOBJExporter()
o.SetFilePrefix('c:/tmp/test')
o.SetRenderWindow(rw2)
o.Write()
</code></pre>
</blockquote>
</aside>
<p>Thank you so much, it works like a charm …Finally got the obj output.<br>
please update once this issue gets resolved or any other non crashing solution you get,</p>
<p>thanks,</p>

---
