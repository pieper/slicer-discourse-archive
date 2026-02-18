# Binded with PythonQt class not visible on Linux but visible on Windows (SlicerCAT)

**Topic ID**: 33493
**Date**: 2023-12-21
**URL**: https://discourse.slicer.org/t/binded-with-pythonqt-class-not-visible-on-linux-but-visible-on-windows-slicercat/33493

---

## Post #1 by @keri (2023-12-21 18:22 UTC)

<p>Hi,</p>
<p>Among many classes that are successivle binded with PythonQt and <strong>accessible</strong> from python there are few that are binded but <strong>not accessible</strong> on Linux even though there are <strong>accessible</strong> on Windows.</p>
<p>For example there is a class called <code>ColadaReader</code> that is derived from <code>QDialog</code> and has default constructor.<br>
On Windows this works as expected:</p>
<pre data-code-wrap="python"><code class="lang-python">import qColadaAppPythonQt
reader = qColadaPythonQt.qColadaReader()
</code></pre>
<p>but the same project compiled on any Ubuntu 20.04 or CentOS 7 produce an exception:</p>
<pre><code class="lang-auto">import qColadaAppPythonQt
reader = qColadaAppPythonQt.qColadaReader()
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
AttributeError: module 'qColadaAppPythonQt' has no attribute 'qColadaReader'
</code></pre>
<p>At the same time <code>qColadaReader</code> works as expected from C++ side.</p>
<p>To investigate the problem I list the exported symbols:</p>
<pre><code class="lang-auto">nm -D qColadaAppPythonQt.so
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c9a758912de0104e69b9432f1c489555a35f5e7.png" alt="image" data-base62-sha1="1NuEIHpcupgRLbsSOl3nzSexwcD" width="453" height="132"></p>
<p>As you can see there is <code>qColadaReader</code> in the list.</p>
<p>Then I tried <code>ldd qColadaAppPythonQt</code> shows that there are some dependecies:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d945ca6a81883f463062d577209dad51aa818c1.png" alt="image" data-base62-sha1="b4iD0wjT3OVZUuShGxsoJ8QnPK9" width="633" height="285"><br>
but paths to them are written in <code>ColadaLauncherSettings.ini</code> in <code>[LibraryPaths]</code> section so they should be loaded. And as I said it works from C++ side.</p>
<p>I also tried to explicitly add a decorator for that class but that didn’t helped. I think the class is binded but cant be loaded.</p>
<p>I’m a little bit confused but maybe somebody experienced have ideas what may be the reason of that?</p>

---

## Post #2 by @keri (2023-12-22 10:51 UTC)

<p>I’ve found a problem.</p>
<p><code>qColadaReader</code> is a base class for <code>qColadaSegyReader</code>.<br>
<code>qColadaReader</code> is a class of <code>qColadaApp</code> library.<br>
<code>qColadaSegyReader</code> is a class of a module <code>qSlicerSeismicModuleWidgets</code>.</p>
<p>If I build extenstion externally then <code>qColadaReader</code> is in <code>qColadaAppPythonQt</code>.<br>
But if I build it during a Superbuild (application+extensions) then both <code>qColadaReader</code> and <code>qColadaSegyReader</code> are located in <code>qSlicerSeismicModuleWidgetsPythonQt</code>.</p>
<p>The question now is how to tell PythonQt to leave <code>qColadaReader</code> in <code>qColadaAppPythonQt</code> and <code>qColadaSegyReader</code> in <code>qSlicerSeismicModuleWidgetsPythonQt</code>…</p>

---
