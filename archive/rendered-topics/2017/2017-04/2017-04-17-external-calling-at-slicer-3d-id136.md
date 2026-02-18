# External calling at Slicer 3D

**Topic ID**: 136
**Date**: 2017-04-17
**URL**: https://discourse.slicer.org/t/external-calling-at-slicer-3d/136

---

## Post #1 by @Alba_Garcia_de_la_Ca (2017-04-17 22:18 UTC)

<p>Hi everybody,</p>
<p>I am programming an extension module for Slicer 3D. In one step I need to call an external command (Elastix). At this point is when I obtain the following error:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/6e7cf603bea688a3821efdb228bd5f65599bcb13.jpg" data-download-href="/uploads/short-url/fLqfsRSXFIBl5IoAXjj9iVBmkSL.jpg?dl=1" title="image.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6e7cf603bea688a3821efdb228bd5f65599bcb13_2_690x25.jpg" width="690" height="25" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/6e7cf603bea688a3821efdb228bd5f65599bcb13_2_690x25.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e7cf603bea688a3821efdb228bd5f65599bcb13.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6e7cf603bea688a3821efdb228bd5f65599bcb13.jpeg 2x" data-dominant-color="D5D5D4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.jpg</span><span class="informations">845×31 34.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I have not been able to solve it yet. Do you know how get rid of this problem? It works when I execute the call in a terminal.</p>
<p>I look forward to hearing from you. Thanks in advance.</p>
<p>Sincerely,</p>
<p>Alba.</p>

---

## Post #2 by @ihnorton (2017-04-17 22:40 UTC)

<p>Hi Alba,</p>
<p>My guess is that the Slicer version of the <code>libcrypto</code> ends up in your PATH/LD_LIBRARY_PATH before the system library paths, and conflicts with the version expected by <code>libgdmCommon</code> (the elastix copy of it).</p>
<p>What type of extension is this, Python or C++ (CLI)?</p>

---

## Post #3 by @lassoan (2017-04-17 23:36 UTC)

<p>This issue has been discussed before - see <a href="http://slicer-devel.65872.n3.nabble.com/Calling-elastix-in-Slicer-td4028906.html">this page</a>. The problem was what Isaiah described above (preferred library paths set up by the Slicer launcher caused loading of wrong version of some shared libraries).</p>
<p>I think the best would be to add a new extension to Slicer that contains Elastix. Alba, would you be interested/have time to work on this?</p>

---

## Post #4 by @Alba_Garcia_de_la_Ca (2017-04-20 20:16 UTC)

<p>Hi Isaiah!</p>
<p>Thank you so much for the quick response!</p>
<p>It is a Python extension. After reading Andras referenced’s page it seems I have solved it this way:</p>
<p><em>import os</em><br>
<em>os.system(‘elastix’)</em><br>
<em>os.environ[‘ITK_AUTOLOAD_PATH’] = ‘’</em></p>
<p>I am still working with it!</p>

---

## Post #5 by @Alba_Garcia_de_la_Ca (2017-04-20 20:25 UTC)

<p>Hi Andras!</p>
<p>Thank you so much too for the quick response!</p>
<p>After reading that page it seems I have solved it with this commands:</p>
<p><em>import os</em><br>
<em>os.system(‘elastix’)</em><br>
<em>os.environ[‘ITKAUTOLOAD_PATH’] = ‘’</em></p>
<p>Now my time is limited but it would be a great idea…and I guess it would help us. Maybe after I finish my final degree project I could improve it with an Elastix extension</p>

---

## Post #6 by @lassoan (2017-04-21 02:35 UTC)

<p>I’ve added Elastix as an extension to Slicer - download the nightly build of Slicer tomorrow and install it from the extension manager. It includes the Elastix toolbox, so you don’t have to manually install or configure anything.</p>

---

## Post #7 by @Alba_Garcia_de_la_Ca (2017-05-15 18:37 UTC)

<p>Thank you so much Andras for adding this extension to Sli3r. It has been really helpful! ^º^</p>
<p>Regards!</p>

---

## Post #8 by @lassoan (2017-05-15 20:16 UTC)

<p>You’re welcome. Just a small remark: <a href="http://slic3r.org/">Slic3r</a> is a very different application with a similar name. This one is 3DSlicer or just Slicer.</p>

---
