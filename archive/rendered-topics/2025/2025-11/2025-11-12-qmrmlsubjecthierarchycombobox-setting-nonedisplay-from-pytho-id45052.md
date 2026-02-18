# qMRMLSubjectHierarchyComboBox: Setting noneDisplay from Python segfaults

**Topic ID**: 45052
**Date**: 2025-11-12
**URL**: https://discourse.slicer.org/t/qmrmlsubjecthierarchycombobox-setting-nonedisplay-from-python-segfaults/45052

---

## Post #1 by @shai-ikko (2025-11-12 16:08 UTC)

<p>Hi,</p>
<p>I’m trying to write a SegmentEditorEffect to apply a mask to all volumes in a study (related to <a href="https://discourse.slicer.org/t/applying-manipulations-to-all-volumes-in-a-study/44479" class="inline-onebox">Applying manipulations to all volumes in a study</a> ). I want the result to go into a study, so where <code>MaskVolume</code> has a volume-selection combobox, I’m trying to get a study-selection one. Naturally, this is an instance of <code>qMRMLSubjectHierarchyComboBox</code>. By default, I want it to be a new study, so I’m setting <code>noneEnabled = True</code> and trying to set <code>noneDisplay</code> to a string like “(Create a new study)”. This causes Slicer (5.8.1 on Linux) to segfault.</p>
<p>I’m saying that this was the problem, not only because commenting out that line “solved” the problem, but also because I ran Slicer under a gdb and got this where the SIGSEGV was received:</p>
<pre><code class="lang-auto">#0  0x00007ffff3701102 in QStandardItem::child(int, int) const () from .../Slicer-5.8.1-linux-amd64/bin/../lib/Slicer-5.8/libQt5Gui.so.5
#1  0x00007ffedcc3d360 in qMRMLSubjectHierarchyModel::setNoneDisplay(QString const&amp;) ()
   from .../Slicer-5.8.1-linux-amd64/bin/../lib/Slicer-5.8/qt-loadable-modules/libqSlicerSubjectHierarchyModuleWidgets.so
#2  0x00007ffedcca3c5e in ?? () from .../Slicer-5.8.1-linux-amd64/bin/../lib/Slicer-5.8/qt-loadable-modules/libqSlicerSubjectHierarchyModuleWidgets.so
#3  0x00007ffedcca403b in qMRMLSubjectHierarchyComboBox::qt_metacall(QMetaObject::Call, int, void**) ()
   from .../Slicer-5.8.1-linux-amd64/bin/../lib/Slicer-5.8/qt-loadable-modules/libqSlicerSubjectHierarchyModuleWidgets.so
#4  0x00007ffff2cacad0 in QMetaProperty::write(QObject*, QVariant const&amp;) const () from .../Slicer-5.8.1-linux-amd64/bin/../lib/Slicer-5.8/libQt5Core.so.5
#5  0x00007fffe37636cc in ?? () from .../Slicer/Slicer-5.8.1-linux-amd64/bin/../lib/Slicer-5.8/libPythonQt.so
#6  0x00007fffb71075df in PyObject_SetAttr () from .../Slicer-5.8.1-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#7  0x00007fffb70798e9 in _PyEval_EvalFrameDefault () from .../Slicer-5.8.1-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
#8  0x00007fffb71c0b37 in _PyEval_EvalCode () from .../Slicer-5.8.1-linux-amd64/bin/../lib/Python/lib/libpython3.9.so
...
</code></pre>
<p>Is this known? Has this code changed recently? I know 5.10.0 is just out, haven’t had a chance to play with it yet. I did search for related (open and closed) issues, and found none.</p>

---

## Post #2 by @jamesobutler (2025-11-12 16:30 UTC)

<p>At least on Windows the following snippet appears to work for me with Slicer 5.8.1 and Slicer 5.10.0. It was also successfully when I tried Slicer 5.10.0 on macOS. Can you try this code snippet?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/125b2a6ab5eeedfbc4a286510e31cd62560fedfc.png" alt="{DF5333E0-C3BA-45E5-A100-D085102D352F}" data-base62-sha1="2CnUNkGKUwYUQlWQGonl08iy2qo" width="219" height="56"></p>
<pre data-code-wrap="python"><code class="lang-python">import SampleData
SampleData.SampleDataLogic().downloadMRHead()
subject_hierarchy_combobox = slicer.qMRMLSubjectHierarchyComboBox()
subject_hierarchy_combobox.setMRMLScene(slicer.mrmlScene)
subject_hierarchy_combobox.show()
subject_hierarchy_combobox.noneEnabled = True
subject_hierarchy_combobox.noneDisplay = "(Create a new study)"
</code></pre>

---

## Post #3 by @shai-ikko (2025-11-13 09:35 UTC)

<p>Yes, that snippet works for me too (I tried also a variation without loading any data, which is more like how I saw the segfault).</p>
<p>I’ll try to create a reproduction I can share.</p>

---

## Post #4 by @shai-ikko (2025-11-13 09:38 UTC)

<pre><code class="lang-auto">subject_hierarchy_combobox = slicer.qMRMLSubjectHierarchyComboBox()
# subject_hierarchy_combobox.setMRMLScene(slicer.mrmlScene)
subject_hierarchy_combobox.show()
subject_hierarchy_combobox.noneEnabled = True
subject_hierarchy_combobox.noneDisplay = "(Create a new study)"

</code></pre>
<p>This (setting the noneDisplay without/before setting the scene) segfaults.</p>

---

## Post #5 by @cpinter (2025-11-14 09:27 UTC)

<p>This should fix it</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/8853">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/8853" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/8853" target="_blank" rel="noopener">COMP: Fix crash when setting none display in SH combobox with no scene</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>cpinter:sh-combobox-none-crash</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2025-11-14" data-time="09:25:21" data-timezone="UTC">09:25AM - 14 Nov 25 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/cpinter" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/1325980?v=4" class="onebox-avatar-inline" width="20" height="20">
            cpinter
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 1 additions and 1 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/8853/files" target="_blank" rel="noopener">
            <span class="added">+1</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Re https://discourse.slicer.org/t/qmrmlsubjecthierarchycombobox-setting-nonedisp<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/8853" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">lay-from-python-segfaults/45052</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>I didn’t even build this because it seems so trivial but based on the call stack I’m pretty sure this fixes it. It makes sense that there is no scene item found in the combobox’s model if there is no scene set to it.</p>
<p>Thanks for the detailed report <a class="mention" href="/u/shai-ikko">@shai-ikko</a> !</p>

---
