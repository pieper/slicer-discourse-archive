# How to access vtkRenderer from CLI

**Topic ID**: 269
**Date**: 2017-05-04
**URL**: https://discourse.slicer.org/t/how-to-access-vtkrenderer-from-cli/269

---

## Post #1 by @DanC (2017-05-04 21:51 UTC)

<p>Hi all.<br>
I would like to update the renderer as the vtk poly data changes(vtkPolyDataWriter) within a CLI loop.<br>
Is there a way to force the renderer to re-render?<br>
It seems that it would be possible from a python script, but not a CLI module?</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2017-05-04 22:13 UTC)

<aside class="quote no-group" data-username="DanC" data-post="1" data-topic="269">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/77aa72/48.png" class="avatar"> DanC:</div>
<blockquote>
<p>It seems that it would be possible from a python script, but not a CLI module?</p>
</blockquote>
</aside>
<p>Right - a CLI is meant to be able to run independent of Slicer (just using command line arguments) so it doesn’t know about renderers or the rest of the GUI.</p>
<p>Sometimes a reasonable approach is to write the inner loop in the CLI and then call it repeatedly from a scripted module that triggers the redraws.</p>

---

## Post #3 by @jcfr (2017-05-04 22:17 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="269">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>call it repeatedly from a scripted module that triggers the redraws.</p>
</blockquote>
</aside>
<p>Worth noting that by unchecking the option <code>Prefer CLI executable</code> in <code>Settings -&gt; Modules</code>, the CLI will be called as a function pointer and overhead of writing input and output to disk is removed.</p>

---
