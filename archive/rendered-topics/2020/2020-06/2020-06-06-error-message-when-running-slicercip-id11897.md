---
topic_id: 11897
title: "Error Message When Running Slicercip"
date: 2020-06-06
url: https://discourse.slicer.org/t/11897
---

# Error message when running slicerCIP

**Topic ID**: 11897
**Date**: 2020-06-06
**URL**: https://discourse.slicer.org/t/error-message-when-running-slicercip/11897

---

## Post #1 by @shahrokh (2020-06-06 12:02 UTC)

<p>Hello Developers and Users 3DSlicer</p>
<p>I want to run SlicerCIP (SlicerCIP4-10-2) in my computer with the following specifications:</p>
<blockquote>
<p>sn@MP:~$ uname --all<br>
Linux MP 5.3.0-53-generic #47~18.04.1-Ubuntu SMP Thu May 7 13:10:50 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux</p>
</blockquote>
<blockquote>
<p>sn@MP:~$ python --version<br>
Python 2.7.17</p>
</blockquote>
<blockquote>
<p>sn@MP:~$ python3 --version<br>
Python 3.6.9</p>
</blockquote>
<p>When I run SlicerCIP4-10-2, I get the following error message:</p>
<blockquote>
<p>sn@MP:~$ cd ./SlicerCIP4-10-2/</p>
</blockquote>
<blockquote>
<p>sn@MP:~/SlicerCIP4-10-2$ ./SlicerCIP4-10-2<br>
Error processing line 1 of /home/sn/SlicerCIP4-10-2/lib/Python/lib/python2.7/site-packages/._easy-install.pth:</p>
<p>Traceback (most recent call last):<br>
File “/home/sn/SlicerCIP4-10-2/bin/…/lib/Python/lib/python2.7/site.py”, line 156, in addpackage<br>
if not dircase in known_paths and os.path.exists(dir):<br>
File “/home/sn/SlicerCIP4-10-2/bin/…/lib/Python/lib/python2.7/genericpath.py”, line 26, in exists<br>
os.stat(path)<br>
TypeError: stat() argument 1 must be encoded string without null bytes, not str</p>
<p>Remainder of file ignored<br>
Error processing line 1 of /home/sn/SlicerCIP4-10-2/lib/Python/lib/python2.7/site-packages/._setuptools.pth:</p>
<p>Traceback (most recent call last):<br>
File “/home/sn/SlicerCIP4-10-2/bin/…/lib/Python/lib/python2.7/site.py”, line 156, in addpackage<br>
if not dircase in known_paths and os.path.exists(dir):<br>
File “/home/sn/SlicerCIP4-10-2/bin/…/lib/Python/lib/python2.7/genericpath.py”, line 26, in exists<br>
os.stat(path)<br>
TypeError: stat() argument 1 must be encoded string without null bytes, not str</p>
<p>Remainder of file ignored<br>
Error(s):<br>
Cannot load library /home/sn/SlicerCIP4-10-2/SlicerCIP4-10-2-Extensions/Chest_Imaging_Platform/lib/Slicer-4.10/qt-loadable-modules/libqSlicerAirwayInspectorModule.so: (libvtkSlicerAirwayInspectorModuleLogic.so: cannot open shared object file: No such file or directory)<br>
Error(s):<br>
Cannot load library /home/sn/SlicerCIP4-10-2/SlicerCIP4-10-2-Extensions/Chest_Imaging_Platform/lib/Slicer-4.10/qt-loadable-modules/libqSlicerParticlesDisplayModule.so: (libvtkSlicerParticlesDisplayModuleLogic.so: cannot open shared object file: No such file or directory)<br>
Error(s):<br>
Cannot load library /home/sn/SlicerCIP4-10-2/SlicerCIP4-10-2-Extensions/Chest_Imaging_Platform/lib/Slicer-4.10/qt-loadable-modules/libqSlicerRegionTypeModule.so: (libvtkSlicerRegionTypeModuleLogic.so: cannot open shared object file: No such file or directory)<br>
Failed to import ._<strong>init</strong>: Traceback (most recent call last):<br>
File “/home/sn/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py”, line 14, in <br>
exec(importStr)<br>
File “”, line 1, in <br>
ImportError: No module named _<strong>init</strong></p>
<p>Failed to import ._AbstractScriptedSubjectHierarchyPlugin: Traceback (most recent call last):<br>
File “/home/sn/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py”, line 14, in <br>
exec(importStr)<br>
File “”, line 1, in <br>
ImportError: No module named _AbstractScriptedSubjectHierarchyPlugin</p>
<p>Failed to import ._AnnotationsSubjectHierarchyPlugin: Traceback (most recent call last):<br>
File “/home/sn/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py”, line 14, in <br>
exec(importStr)<br>
File “”, line 1, in <br>
ImportError: No module named _AnnotationsSubjectHierarchyPlugin</p>
<p>Failed to import ._SegmentEditorSubjectHierarchyPlugin: Traceback (most recent call last):<br>
File “/home/sn/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py”, line 14, in <br>
exec(importStr)<br>
File “”, line 1, in <br>
ImportError: No module named _SegmentEditorSubjectHierarchyPlugin</p>
<p>Failed to import ._SegmentStatisticsSubjectHierarchyPlugin: Traceback (most recent call last):<br>
File “/home/sn/SlicerCIP4-10-2/lib/Slicer-4.10/qt-scripted-modules/SubjectHierarchyPlugins/<strong>init</strong>.py”, line 14, in <br>
exec(importStr)<br>
File “”, line 1, in <br>
ImportError: No module named _SegmentStatisticsSubjectHierarchyPlugin</p>
<p>Switch to module:  “Welcome”<br>
Switch to module:  “”<br>
Switch to module:  “”<br>
…</p>
</blockquote>
<p>Although I get error messages mentioned above, but Slicer is opened.<br>
Why do I get the error? Do these errors affect performance of “Chest Imaging Platform” module in 3DSlicer? What can I do to avoid/solve this error?</p>
<p>Please help me.<br>
Thanks a lot.<br>
Shahrokh</p>

---

## Post #2 by @pieper (2020-06-06 21:52 UTC)

<p>Hmm, looks like an issue with the packaging of the customized app.  I tried it and most things seem to work anyway.</p>
<p>I’d suggest using the nightly, but unfortunately the extension is broken.  I’ve submitted a pull request.</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/acil-bwh/ChestImagingPlatform/pull/31" target="_blank">github.com/acil-bwh/ChestImagingPlatform</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/acil-bwh/ChestImagingPlatform/pull/31" target="_blank">COMP: fix namespace for new itk</a>
    </h4>

    <div class="branches">
      <code>acil-bwh:develop</code> ← <code>pieper:fix-itk-pack</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-06-06" data-time="21:15:11" data-timezone="UTC">09:15PM - 06 Jun 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/pieper" target="_blank">
          <img alt="pieper" src="https://avatars0.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
          pieper
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 2 additions and 2 deletions">
        <a href="https://github.com/acil-bwh/ChestImagingPlatform/pull/31/files" target="_blank">
          <span class="added">+2</span>
          <span class="removed">-2</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @shahrokh (2020-06-07 04:34 UTC)

<p>Dear Steve<br>
At now, I install Chest_Imaging_Platform extension in Slicer-4.8.1. I do not get any error message.</p>
<p>Thanks a lot.<br>
Shahrokh</p>

---

## Post #4 by @lassoan (2020-06-13 14:21 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>’s fix went through and so CIP is available in most recent Slicer-4.11. Please use this version, as it would help us discover and fix any potential issues before the new release.</p>

---
