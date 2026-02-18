# openDialog does not load node into scene

**Topic ID**: 23874
**Date**: 2022-06-14
**URL**: https://discourse.slicer.org/t/opendialog-does-not-load-node-into-scene/23874

---

## Post #1 by @mholden8 (2022-06-14 20:02 UTC)

<p>When using the openDialog function in the Slicer IO Manager, the selected node is not loaded into the scene.</p>
<p>For example, when I run the code below (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/IO#How_to_open_a_registered_a_dialog_.3F" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Developers/IO - Slicer Wiki</a>), nothing happens after selecting a volume file to load.</p>
<pre><code class="lang-auto"> io = slicer.app.ioManager()
 params = {}
 io.openDialog("VolumeFile", slicer.qSlicerFileDialog.Read, params)
</code></pre>
<p>Is there a new preferred way to load files using a registered dialog?</p>
<p>Slicer version: 5.1.0-2022-05-16<br>
OS: Windows 10</p>

---

## Post #2 by @pieper (2022-06-14 20:26 UTC)

<p>thanks for the report.  yes, that appears to be a regression.  For me either the code you pasted or <code>slicer.util.openAddVolumeDialog()</code> brings up a native dialog and always returns <code>False</code>.  Can you file an issue on slicer github?</p>
<p>As a workaround, you can do something like this:</p>
<pre><code class="lang-auto">d = qt.QFileDialog()
d.exec()
slicer.util.loadVolume(d.selectedFiles()[0])
</code></pre>

---

## Post #3 by @mholden8 (2022-06-14 21:15 UTC)

<p>Thanks for the workaround. I have filed an issue on Slicer Github here: <a href="https://github.com/Slicer/Slicer/issues/6429" class="inline-onebox" rel="noopener nofollow ugc">openDialog does not load node into scene · Issue #6429 · Slicer/Slicer · GitHub</a>.</p>

---
