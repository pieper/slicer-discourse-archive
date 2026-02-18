# error message "Failed to find python interpreter for CLI"

**Topic ID**: 4749
**Date**: 2018-11-13
**URL**: https://discourse.slicer.org/t/error-message-failed-to-find-python-interpreter-for-cli/4749

---

## Post #1 by @ueda (2018-11-13 14:45 UTC)

<p>Operating system: ubuntu16.04<br>
Slicer version:4.11.0-2018-11-08<br>
Expected behavior:Non error messages<br>
Actual behavior:Error(s): Failed to find python interpreter for CLI</p>
<p>Hellow.<br>
I’m a beginner at python and 3D slicer.<br>
When I activate the 3D slicer from the terminal, I get the following error message:</p>
<p>Error(s):<br>
Failed to find python interpreter for CLI: /home/ueda/bin/Slicer-SuperBuild/Slicer-build/lib/Slicer-4.11/cli-modules/PyCLIModule4Test.py<br>
Fail to instantiate module  “PyCLI4Test”<br>
Object::connect: No such signal qSlicerGPUMemoryComboBox::currentTextChanged(QString) in /home/ueda/bin/Slicer/Modules/Loadable/VolumeRendering/qSlicerVolumeRenderingSettingsPanel.cxx:116<br>
Object::connect:  (sender name:   ‘GPUMemoryComboBox’)<br>
Object::connect:  (receiver name: ‘qSlicerVolumeRenderingSettingsPanel’)<br>
Switch to module:  “Welcome”</p>
<p>How can I solve this error message?</p>

---

## Post #2 by @lassoan (2018-11-15 02:00 UTC)

<p>Python CLIs are only available if Slicer is built with Qt5.</p>
<p><a class="mention" href="/u/ihnorton">@ihnorton</a>, What’s the reason behind trying to find “python” executable <a href="https://github.com/Slicer/Slicer/blob/60adeea3e15d3640e9f68bc8abb6bf1d45b32624/Base/QTCLI/qSlicerCLIExecutableModuleFactory.cxx#L41">here</a>? Can the CLI executed by an any Python interpreter? How do you tell if you want to run the Python file using Slicer’s Python interpreter or another one?</p>

---

## Post #3 by @ihnorton (2018-11-19 17:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="4749">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What’s the reason behind trying to find “python” executable <a href="https://github.com/Slicer/Slicer/blob/60adeea3e15d3640e9f68bc8abb6bf1d45b32624/Base/QTCLI/qSlicerCLIExecutableModuleFactory.cxx#L41">here </a>? Can the CLI executed by an any Python interpreter?</p>
</blockquote>
</aside>
<p>That was to make it work with a local build.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="4749">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>How do you tell if you want to run the Python file using Slicer’s Python interpreter or another one?</p>
</blockquote>
</aside>
<p>I don’t think there is a way to do that right now. A couple ideas:</p>
<ul>
<li>tell people to use the PyCLI as a wrapper to call some other arbitrary command with the correct environment, arguments, etc.</li>
<li>do what <code>bash</code> does: parse the <code>#!</code> line, use that as either absolute path or a target to search for in PATH (ignoring <code>/usr/bin/env</code> if present, at least on Windows). This would be nice because it would work for arbitrary interpreters, but would be tricky because people would need to either arrange their PATH properly, or use an install-step to put the correct absolute path in place (this is what anaconda does, and it works very well).</li>
<li>expose <code>ModuleDescription</code>: then people could call <code>setEntryPoint</code>on the CLI object as needed (actually this might already be possible with a <code>vtkMRMLCommandLineModuleNode</code>)</li>
</ul>

---
