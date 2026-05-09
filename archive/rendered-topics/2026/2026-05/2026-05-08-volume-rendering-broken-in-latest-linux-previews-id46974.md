---
topic_id: 46974
title: "Volume Rendering Broken In Latest Linux Previews"
date: 2026-05-08
url: https://discourse.slicer.org/t/46974
---

# Volume rendering broken in latest Linux previews?

**Topic ID**: 46974
**Date**: 2026-05-08
**URL**: https://discourse.slicer.org/t/volume-rendering-broken-in-latest-linux-previews/46974

---

## Post #1 by @muratmaga (2026-05-08 18:49 UTC)

<p>I am using the preview build from May 5th on Ubuntu, and I can’t get the MRHead (or any of the baked data) to render. When I drag and drop volume object to the 3D viewer, application fails catastrophically, without any error on the console or in the command line.</p>
<p>Same if I were to use the Volume Rendering module. Here is all the log from the failed session:</p>
<pre><code class="lang-auto">[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - Session start time .......: 20260508_113958
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - Slicer version ...........: 5.11.0-2026-05-05 (revision 34535 / c59af2b) linux-amd64 - installed release
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - Operating system .........: Linux / 6.8.0-106-generic / #106-Ubuntu SMP PREEMPT_DYNAMIC Fri Mar  6 07:58:08 UTC 2026 / UTF-8 - 64-bit
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - Memory ...................: 515582 MB physical, 2047 MB virtual
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - CPU ......................: AuthenticAMD AMD Ryzen Threadripper PRO 3995WX 64-Cores, 64 cores, 128 logical processors
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - Qt configuration .........: version 5.15.2, with SSL, requested OpenGL 3.2 (core profile)
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - DCMTK configuration ......: version 3.7.0, no SSL
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - Internationalization .....: disabled, language=
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - Developer mode ...........: enabled
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - Application path .........: /home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/bin
[DEBUG][Qt] 08.05.2026 11:39:58 [] (unknown:0) - Additional module paths ..: (none)
[WARNING][VTK] 08.05.2026 11:39:58 [vtkCacheManager (0x2b9d5930)] (vtkCacheManager.cxx:1068) - Cache pruning is disabled as no sentinel file is found in the cache directory.
[INFO][Stream] 08.05.2026 11:39:58 [] (unknown:0) -
[WARNING][Python] 08.05.2026 11:40:02 [Python] (/home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/lib/Python/lib/python3.12/site-packages/pydicom/misc.py:82) - get_frame_offsets is deprecated and will be removed in v4.0
[DEBUG][Python] 08.05.2026 11:40:03 [Python] (/home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/lib/Slicer-5.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 08.05.2026 11:40:03 [Python] (/home/maga/Downloads/Slicer-5.11.0-2026-05-05-linux-amd64/lib/Slicer-5.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:40) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 08.05.2026 11:40:03 [] (unknown:0) - Switch to module:  "Data"
[WARNING][VTK] 08.05.2026 11:40:41 [vtkCacheManager (0x3b1c7a60)] (vtkCacheManager.cxx:407) - Cache directory does not contain sentinel file .slicer-cache. Destructive cache operations are disabled until the sentinel is created.
[DEBUG][Qt] 08.05.2026 11:40:41 [] (unknown:0) - "Volume" Reader has successfully read the file "/home/maga/.cache/slicer.org/Slicer/SlicerIO/MR-head.nrrd" "[0.14s]"
[DEBUG][Qt] 08.05.2026 11:40:50 [] (unknown:0) - Switch to module:  "VolumeRendering"

</code></pre>

---

## Post #2 by @pieper (2026-05-08 19:02 UTC)

<p>With today’s linux nightly I couldn’t even download any sample data.  When I loaded local data the volume rendering did work.</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/home/exouser/Downloads/Slicer-5.11.0-2026-05-07-linux-amd64/bin/../lib/Slicer-5.11/qt-scripted-modules/SampleData.py", line 457, in &lt;lambda&gt;
    b.connect("clicked()", lambda s=source: logic.downloadFromSource(s))
                                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/exouser/Downloads/Slicer-5.11.0-2026-05-07-linux-amd64/bin/../lib/Slicer-5.11/qt-scripted-modules/SampleData.py", line 912, in downloadFromSource
    filePath = self.downloadFileIntoCache(uri, fileName, checksum, forceDownload=forceDownload)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/exouser/Downloads/Slicer-5.11.0-2026-05-07-linux-amd64/bin/../lib/Slicer-5.11/qt-scripted-modules/SampleData.py", line 836, in downloadFileIntoCache
    return self.downloadFile(uri, destFolderPath, name, checksum, forceDownload=forceDownload)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/exouser/Downloads/Slicer-5.11.0-2026-05-07-linux-amd64/bin/../lib/Slicer-5.11/qt-scripted-modules/SampleData.py", line 1168, in downloadFile
    self.logMessage(_("Verifying checksum"))
  File "/home/exouser/Downloads/Slicer-5.11.0-2026-05-07-linux-amd64/bin/../lib/Slicer-5.11/qt-scripted-modules/SampleData.py", line 473, in logMessage
    self.log.insertHtml(message)
    ^^^^^^^^
AttributeError: 'SampleDataWidget' object has no attribute 'log'
</code></pre>

---

## Post #3 by @chir.set (2026-05-08 19:13 UTC)

<p>With <code>5.11.0-2026-05-07 r34537 / 785744e</code> on Arch, MRHead is downloaded but volume rendering does crash the application.</p>

---
