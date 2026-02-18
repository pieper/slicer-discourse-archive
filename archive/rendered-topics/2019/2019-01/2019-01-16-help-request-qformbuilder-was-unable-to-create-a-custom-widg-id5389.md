# [Help Request] QFormBuilder was unable to create a custom widget

**Topic ID**: 5389
**Date**: 2019-01-16
**URL**: https://discourse.slicer.org/t/help-request-qformbuilder-was-unable-to-create-a-custom-widget/5389

---

## Post #1 by @adamrankin (2019-01-16 17:12 UTC)

<p>Hello,</p>
<p>Has anyone experienced this error? The widget is question works in another C++ module, but fails when using python and a .ui file</p>
<p><code>QFormBuilder was unable to create a custom widget of the class 'qMRMLVideoCameraIntrinsicsWidget'; defaulting to base class 'qSlicerWidget'.</code></p>
<p>Edit: code to load UI</p>
<pre><code class="lang-python">      scriptedModulesPath = eval('slicer.modules.%s.path' % self.moduleName.lower())
      scriptedModulesPath = os.path.dirname(scriptedModulesPath)
      path = os.path.join(scriptedModulesPath, 'Resources', 'UI', 'q' + self.moduleName + 'Widget.ui')
      self.widget = slicer.util.loadUI(path)
</code></pre>
<p>Edit2: my workaround is to have a placeholder QWidget in the .ui file, and to create the custom widget in code after loading the UI</p>

---

## Post #2 by @adamrankin (2019-01-16 17:36 UTC)

<p>It looks like QFormBuilder/QUiLoader needs the plugin path to contain the *Plugin.dll file. The current implementation has <code>C:\Program Files\Slicer 4.10.0\bin\designer</code> and <code>C:\Program Files\Slicer 4.10.0\lib\QtPlugins\designer</code> in the path.</p>
<p>Two potential solutions are to extend <code>slicer.util.loadUI(filePath)</code> to also accept additional plugin directories, or to copy all <code>*Plugin.dll</code> files from an extension into the above folders, or to intelligently add an extensions <code>QtPlugin</code> directory to the plugin path in <code>slicer.util.loadUI</code></p>

---

## Post #3 by @jcfr (2019-01-16 17:42 UTC)

<p>Instead, I suggest to update:</p>
<ul>
<li>the code updating the launcher settings when installing an extension. See <a href="https://github.com/Slicer/Slicer/blob/be03b25aa21ac68e3bbb1b591ada3f8800c6b9f5/Base/QTCore/qSlicerExtensionsManagerModel.cxx#L634" rel="nofollow noopener">here</a>
</li>
<li>the code generating the AdditionalLauncherSettingsPath used when starting Slicer with a specific extension.  See <a href="https://github.com/Slicer/Slicer/blob/master/Extensions/CMake/SlicerBlockAdditionalLauncherSettings.cmake" rel="nofollow noopener">here</a>
</li>
</ul>

---

## Post #4 by @adamrankin (2019-01-16 17:43 UTC)

<p>Do you think QFormBuilder uses the current path to load Qt plugins?</p>

---

## Post #5 by @jcfr (2019-01-16 17:45 UTC)

<p>Path that contains the plugin mud be added to the env. variable <code>QT_PLUGIN_PATH</code>. Dependencies of the plugin must also be added to <code>PATH</code>, <code>LD_LIBRARY_PATH</code> or <code>DYLD_LIBRARY_PATH</code> depending on the plaform. This last point is most likely already taking care of.</p>

---

## Post #6 by @adamrankin (2019-01-16 17:57 UTC)

<p>Would you recommend to add a [QtPluginPaths] section to an extensions AdditionalLauncherSettings.ini, or adding it to an existing entry ([Paths], [LibraryPaths]) and loading those to the QT_PLUGIN_PATH env var?</p>

---

## Post #7 by @jcfr (2019-01-16 18:01 UTC)

<p>To clarify, here is a snippet of the current <code>SlicerLauncherSettings.ini</code> found in the build tree :</p>
<pre><code class="lang-auto">[...]

[Environment]
additionalPathVariables=QT_PLUGIN_PATH,PYTHONPATH

[...]

[QT_PLUGIN_PATH]
1\path=&lt;APPLAUNCHER_SETTINGS_DIR&gt;/bin
2\path=/home/jcfr/Projects/Slicer-Qt5-VTK9-RelWithDebInfo/CTK-build/CTK-build/bin
3\path=/home/jcfr/Software/Qt5.11.1/5.11.1/gcc_64/plugins
size=3

[...]
</code></pre>
<p>This means that a env. variable <code>QT_PLUGIN_PATH</code> will be set before starting Slicer. Each one of these paths a subdirectory named <code>designer</code>. The same thing should be done in <code>AdditionalLauncherSettings.ini</code>.</p>
<p>Then the launcher will take of creating a unified environment before starting the application.</p>

---

## Post #8 by @adamrankin (2019-01-16 19:22 UTC)

<p>Edit: right. Nevermind!</p>

---

## Post #9 by @jcfr (2019-06-21 06:57 UTC)

<p><a class="mention" href="/u/adamrankin">@adamrankin</a> Thanks again for submitting <a href="https://github.com/Slicer/Slicer/pull/1084" rel="nofollow noopener">PR#1084</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>After applying few tweaks it has been integrated in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28325" rel="nofollow noopener">r28325</a> and issue <a href="https://issues.slicer.org/view.php?id=4670" rel="nofollow noopener">#4670</a> has been resolved.</p>

---
