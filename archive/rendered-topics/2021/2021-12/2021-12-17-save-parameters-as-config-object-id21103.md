# Save parameters as config object

**Topic ID**: 21103
**Date**: 2021-12-17
**URL**: https://discourse.slicer.org/t/save-parameters-as-config-object/21103

---

## Post #1 by @Karthik (2021-12-17 01:36 UTC)

<p>Hi.<br>
I have written a scripted module which has some parameters in the form of sliderwidgets. Currently, I am saving these as .cfg file through the code and reading them next time the same module is instantiated. I was wondering if Slicer has a way to save the current state (values) of these parameters which can then be loaded back and the values would be restored. I know that we can save the mrml scene, but I only want to save the parameter values. Is this possible?</p>

---

## Post #2 by @Alex_Vergara (2021-12-17 07:40 UTC)

<p>That is what I did in my module, watch this file <a href="https://gitlab.com/opendose/opendose3d/-/blob/develop/OpenDose3D/Logic/config.py" class="inline-onebox" rel="noopener nofollow ugc">OpenDose3D/Logic/config.py · develop · OpenDose / SlicerOpenDose3D · GitLab</a></p>

---

## Post #3 by @Mik (2021-12-17 08:44 UTC)

<p>You can use QSettings if module contains Qt. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOM/DICOM.py#L81-L83" rel="noopener nofollow ugc">For example</a></p>
<pre><code class="lang-auto">import qt
value = 10.1
settings = qt.QSettings()
# save value
settings.setValue('MyModule/MyValue', value)
...
# load value
newValue = settings.value('MyModule/MyValue')
</code></pre>

---

## Post #4 by @Alex_Vergara (2021-12-17 16:08 UTC)

<aside class="quote no-group" data-username="Mik" data-post="3" data-topic="21103">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/958977/48.png" class="avatar"> Mik:</div>
<blockquote>
<p>You can use QSettings if module contains Qt.</p>
</blockquote>
</aside>
<p>Isn’t this dangerous? You have no control where the config file is located and you offuscate qt settings with your stuff</p>

---

## Post #5 by @Mik (2021-12-18 04:57 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="4" data-topic="21103">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>Isn’t this dangerous? You have no control where the config file is located and you offuscate qt settings with your stuff</p>
</blockquote>
</aside>
<p>User can define a config file name explicitly in constructor, without using Slicer config file.</p>
<p>With empty constructor QSettings uses <a href="https://github.com/Slicer/Slicer/blob/master/Base/QTApp/qSlicerApplicationHelper.cxx" rel="noopener nofollow ugc">application defined parameters</a>. There are not so many places where config file is stored by default (see Basic usage: <a href="https://doc.qt.io/qt-5/qsettings.html#basic-usage" class="inline-onebox" rel="noopener nofollow ugc">QSettings Class | Qt Core 5.15.16</a> and Platform-specific notes: <a href="https://doc.qt.io/qt-5/qsettings.html#platform-specific-notes" class="inline-onebox" rel="noopener nofollow ugc">QSettings Class | Qt Core 5.15.16</a> for QSettings).</p>
<p>In my case Slicer config file has groups for different modules: Markups, SubjectHierarchy, VolumeRendering. Linux file name path: <code>/home/user/.config/NA-MIC/Slicer.ini</code></p>

---
