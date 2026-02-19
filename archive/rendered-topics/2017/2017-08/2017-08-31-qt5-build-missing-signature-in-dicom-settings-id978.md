---
topic_id: 978
title: "Qt5 Build Missing Signature In Dicom Settings"
date: 2017-08-31
url: https://discourse.slicer.org/t/978
---

# Qt5 build missing signature in DICOM settings

**Topic ID**: 978
**Date**: 2017-08-31
**URL**: https://discourse.slicer.org/t/qt5-build-missing-signature-in-dicom-settings/978

---

## Post #1 by @pieper (2017-08-31 14:16 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a>, <a class="mention" href="/u/jcfr">@jcfr</a> looks like a compatibility issue with the property wrapping after this commit.  It works for me on gcc5.4 build but not with gcc6.3.</p>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/commit/ee5c8703642cf8f42e9594bc780cb0801623b39d" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    
<h4>
  <a href="https://github.com/Slicer/Slicer/commit/ee5c8703642cf8f42e9594bc780cb0801623b39d" target="_blank" rel="nofollow noopener">ENH: Added option to disable DICOM reference check</a>
</h4>

  <pre class="message" style="white-space: pre-wrap;">- Added checkbox in the DICOM references dialog to not check for references again. Selection is saved regardless of pressed button
- Added generic options group in Application Settings / DICOM where this setting can be changed
- Added optional constructor argument to DICOMLoadable for easy conversion from qSlicerDICOMLoadable (useful for debugging when the otherwise deprecated python DICOMLoadable class is used internally)

Integrating https://github.com/Slicer/Slicer/pull/767

git-svn-id: http://svn.slicer.org/Slicer4/trunk@26325 3bd1e089-480b-0410-8dfb-8563597acbee</pre>

<div class="date">
  by <a href=""></a>
  on <a href="https://github.com/Slicer/Slicer/commit/ee5c8703642cf8f42e9594bc780cb0801623b39d" target="_blank" rel="nofollow noopener">08:22PM - 30 Aug 17</a>
</div>

<div class="github-commit-stats">
  changed <strong>4 files</strong>
  with <strong>89 additions</strong>
  and <strong>33 deletions</strong>.
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<pre><code class="lang-auto">Python 2.7.13 (default, Aug 14 2017, 18:33:39) 
[GCC 6.3.0 20170516] on linux2
&gt;&gt;&gt; 
Traceback (most recent call last):
  File "/home/researcher/Slicer-superbuild/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/DICOM.py", line 90, in performPostModuleDiscoveryTasks
    self.settingsPanel = DICOMSettingsPanel()
  File "/home/researcher/Slicer-superbuild/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/DICOM.py", line 145, in __init__
    self.ui = _ui_DICOMSettingsPanel(self)
  File "/home/researcher/Slicer-superbuild/Slicer-build/lib/Slicer-4.7/qt-scripted-modules/DICOM.py", line 128, in __init__
    "DICOM/automaticallyLoadReferences", loadReferencesComboBox, "currentUserDataAsString", qt.SIGNAL("currentIndexChanged (int)"))
ValueError: Could not find matching overload for given arguments:
('DICOM/automaticallyLoadReferences', ctkComboBox(0x5560310dce60) , 'currentUserDataAsString', u'2currentIndexChanged (int)')
 The following slots are available:
registerProperty(QString settingKey, QObject object, QString objectProperty, QByteArray propertySignal, QString settingLabel, SettingOptions options, QSettings settings) -&gt; void
registerProperty(QString settingKey, QObject object, QString objectProperty, QByteArray propertySignal, QString settingLabel, SettingOptions options) -&gt; void
registerProperty(QString settingKey, QObject object, QString objectProperty, QByteArray propertySignal, QString settingLabel) -&gt; void
registerProperty(QString settingKey, QObject object, QString objectProperty, QByteArray propertySignal) -&gt; void

</code></pre>

---

## Post #2 by @cpinter (2017-08-31 15:48 UTC)

<p>It’s strange that gcc version affects wrapping. If I understand correctly this does not affect the nightly right?</p>

---

## Post #3 by @pieper (2017-08-31 16:02 UTC)

<p>Sorry!  You’re right <a class="mention" href="/u/cpinter">@cpinter</a> it’s not the version of gcc it’s the version of Qt.  The error happens on my Qt5 builds, not on Qt4, so no it doesn’t affect the nightly builds.</p>

---
