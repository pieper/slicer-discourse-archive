---
topic_id: 43847
title: "Designer Failing To Launch On Macos"
date: 2025-07-25
url: https://discourse.slicer.org/t/43847
---

# Designer failing to launch on MacOS

**Topic ID**: 43847
**Date**: 2025-07-25
**URL**: https://discourse.slicer.org/t/designer-failing-to-launch-on-macos/43847

---

## Post #1 by @muratmaga (2025-07-25 21:46 UTC)

<p>I am trying to test a minimal UI file, and when I try to open it with Designer, it fails to launch. I launched the Designer from a terminal window and getting this error about missing encodings module. THis is r33743 (preview from July 8th).</p>
<pre><code class="lang-auto">Last login: Fri Jul 25 14:27:38 on ttys004

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
/Users/amaga/Desktop/Slicer.app/Contents/bin/Designer.app/Contents/MacOS/Designer ; exit;
MLSSC40183:~ amaga$ /Users/amaga/Desktop/Slicer.app/Contents/bin/Designer.app/Contents/MacOS/Designer ; exit;
Designer: The class attribute for the class qSlicerDiffusionTensorVolumeDisplayWidgetPlugin does not match the class name qSlicerDiffusionTensorVolumeDisplayWidget.
QMetaProperty::read: Unable to handle unregistered datatype 'ctkDICOMTableManager*' for property 'ctkDICOMQueryRetrieveWidget::dicomTableManager'
QMetaProperty::read: Unable to handle unregistered datatype 'QTableView*' for property 'ctkDICOMTableView::tblDicomDatabaseView'
Could not find platform independent libraries &lt;prefix&gt;
Could not find platform dependent libraries &lt;exec_prefix&gt;
Python path configuration:
  PYTHONHOME = (not set)
  PYTHONPATH = (not set)
  program name = 'PythonQt'
  isolated = 0
  environment = 1
  user site = 1
  safe_path = 0
  import site = 0
  is in build tree = 0
  stdlib dir = '/Users/svc-dashboard/D/P/A/python-install/lib/python3.12'
  sys._base_executable = '/Users/amaga/Desktop/Slicer.app/Contents/bin/Designer.app/Contents/MacOS/Designer'
  sys.base_prefix = '/Users/svc-dashboard/D/P/A/python-install'
  sys.base_exec_prefix = '/Users/svc-dashboard/D/P/A/python-install'
  sys.platlibdir = 'lib'
  sys.executable = '/Users/amaga/Desktop/Slicer.app/Contents/bin/Designer.app/Contents/MacOS/Designer'
  sys.prefix = '/Users/svc-dashboard/D/P/A/python-install'
  sys.exec_prefix = '/Users/svc-dashboard/D/P/A/python-install'
  sys.path = [
    '/Users/svc-dashboard/D/P/A/python-install/lib/python312.zip',
    '/Users/svc-dashboard/D/P/A/python-install',
    '/Users/svc-dashboard/D/P/A/python-install/lib-dynload',
    '/Users/svc-dashboard/D/P/A/python-install/plat-darwin',
    '/Users/svc-dashboard/D/P/A/python-install/lib/python3.12',
    '/Users/svc-dashboard/D/P/A/python-install/lib/python3.12/lib-dynload',
    '/Users/svc-dashboard/D/P/A/python-install/lib-tk',
    '/Users/svc-dashboard/D/P/A/python-install/lib/python3.12',
    '/Users/svc-dashboard/D/P/A/python-install/lib/python3.12/lib-dynload',
  ]
Fatal Python error: init_fs_encoding: failed to get the Python codec of the filesystem encoding
Python runtime state: core initialized
ModuleNotFoundError: No module named 'encodings'

Current thread 0x0000000202f52200 (most recent call first):
  &lt;no Python frame&gt;
logout

Saving session...
...copying shared history...
...saving history...truncating history files...
...completed.
Deleting expired sessions...6 completed.
</code></pre>
<p>This is my first time with Designer, so some pointers would be great.</p>

---

## Post #2 by @muratmaga (2025-07-25 21:52 UTC)

<p>Some error pops up with 5.8.1 as well.</p>

---

## Post #3 by @chir.set (2025-07-26 09:13 UTC)

<p>You seem to</p>
<ul>
<li>enter a new shell</li>
<li>run a Designer app provided by Slicer with success (it starts)</li>
<li>run Designer without being in Slicer’s environment</li>
<li>exit immediately from the shell.</li>
</ul>
<p>Try this:</p>
<blockquote>
<p>/path/to/Slicer --launch /path/to/Designer</p>
</blockquote>
<p>It always works on Linux.</p>

---

## Post #4 by @muratmaga (2025-07-26 17:34 UTC)

<p>Thanks.</p>
<p>I also figured there is a SlicerDesigner executable, which seems to work. For whatever reason on my Mac Designer executable located at <code>/Users/amaga/Desktop/Slicer.app/Contents/bin/Designer.app/Contents/MacOS/Designer </code> is registered as the default application to open .ui files…</p>
<p>I wasn’t able to change the default application for that. So now I am opening it from the terminal window.</p>

---

## Post #5 by @chir.set (2025-07-26 18:44 UTC)

<p>Great, it works, using whatever launch approach.</p>
<p>One thing that puzzles me on Mac, and that’s diverting from this thread’s subject:<br>
How will Slicer handle the post-Rosetta Mac in 2027?</p>
<p>It seems for now the lack of Qt5 is a problem on Mac Silicon. There is a recently updated <a href="https://github.com/Slicer/Slicer/issues/6388" rel="noopener nofollow ugc">effort</a> to switch to Qt6. I vaguely understood there were licensing issues regarding Qt6. Is there Qt6 out of the box on Mac Silicon?</p>
<p>Apple has dropped Motorola CPUs, then x86_64, and its current M3 (ARMv8.6-A) CPU <em>seems</em> to be still an aarch64 one. But aarch64 seems to be an <em>option</em> for Armv8-R according to wikipedia, and one can bet Apple will drop the aarch64 option in its ARMv8/v9 CPUs in a few years. Is supporting Apple a viable obligation in the long run? My point is that developers will have to dance many tunes as orchestrated by that company, and it won’t fund the promised troubles.</p>
<p>As for <a href="https://gist.github.com/jcfr/487f5d846bc86e374969be5565c6d95e" rel="noopener nofollow ugc">building</a> for aarch64 out of the Mac realm, it just works and Slicer is fully functional.</p>

---
