# Sharing python code between (scripted loadable) modules

**Topic ID**: 24921
**Date**: 2022-08-25
**URL**: https://discourse.slicer.org/t/sharing-python-code-between-scripted-loadable-modules/24921

---

## Post #1 by @shai-ikko (2022-08-25 13:30 UTC)

<p>Hi,</p>
<p>I’m trying to add some functionality to Slicer, and I want to make a couple of separate modules which will use the same underlying libraries. It’s not clear to me if there’s a nice way to do this without explicit <code>sys.path</code> manipulation.</p>
<p>I’ve seen <a href="https://discourse.slicer.org/t/importing-custom-python-module-into-scripted-extension/11673" class="inline-onebox">Importing custom python module into scripted extension</a> and <a href="https://discourse.slicer.org/t/python-scripted-module-code-organization/6339" class="inline-onebox">Python scripted module code organization</a> which seem to imply that code to be imported into a module needs to sit in a sub-folder in the module, but that is not suitable for sharing code between modules; and I’ve seen <a href="https://discourse.slicer.org/t/specifying-dependencies-of-a-custom-extension-in-the-s4ext-file/21582/2" class="inline-onebox">Specifying dependencies of a custom extension in the .s4ext file - #2 by jamesobutler</a> which seems to imply that modules can depend on other modules to provide importables, but the example module there does not seem to import anything from its named dependencies…</p>
<p>Am I missing anything?</p>
<p>My hope is to be able to include both the separate modules, and their common infrastructure, in a single extension, but that is not a hard requirement.</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2022-08-25 14:38 UTC)

<p>If one module provides a set of libraries it should be available to other modules that are loaded in the same Slicer session (e.g. import the Logic class from another module).  You should never need to duplicate code or manipulate any python path variables manually.</p>

---

## Post #3 by @talmazov (2022-08-25 23:07 UTC)

<p>Hey,<br>
I should chime-in since you referenced a topic I posted previously. In my case I have a custom library that was shared by two separate applications - a TCP/IP socket class. Let’s call it <code>sock.py</code><br>
to use sock.py in a slicer scripted module I had to setup the directory structure as so</p>
<pre><code class="lang-auto">WidgetRootDir
 |
 | - slicerWidget.py
 | - subdirectory
      | - __init__.py
      | - sock.py
</code></pre>
<p><code>__init__.py</code> contains</p>
<blockquote>
<p>from .sock import *</p>
</blockquote>
<p>And slicerWidget.py imports as so</p>
<blockquote>
<p>from subdirectory import sock</p>
</blockquote>
<p>If you need to access another slicer module this is a clean way of doing so <a href="https://discourse.slicer.org/t/setting-widget-variable-from-python-code-on-slicer-exe-start/23908/13" class="inline-onebox">Setting widget variable from --python-code on Slicer.exe start - #13 by talmazov</a></p>
<p>I hope this helps</p>
<p>~ Georgi</p>

---
