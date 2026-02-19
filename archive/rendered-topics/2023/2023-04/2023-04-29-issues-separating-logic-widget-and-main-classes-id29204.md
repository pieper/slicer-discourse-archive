---
topic_id: 29204
title: "Issues Separating Logic Widget And Main Classes"
date: 2023-04-29
url: https://discourse.slicer.org/t/29204
---

# Issues separating logic, widget and main classes

**Topic ID**: 29204
**Date**: 2023-04-29
**URL**: https://discourse.slicer.org/t/issues-separating-logic-widget-and-main-classes/29204

---

## Post #1 by @asyeda (2023-04-29 12:15 UTC)

<p>I am trying to separate my module into separate files for readability, and I’ve structured it similar to the Slicer DataProbe: <a href="https://github.com/Slicer/Slicer/tree/01984729eca68f0417ead58d87d3358912f094d4/Modules/Scripted/DataProbe" class="inline-onebox" rel="noopener nofollow ugc">Slicer/Modules/Scripted/DataProbe at 01984729eca68f0417ead58d87d3358912f094d4 · Slicer/Slicer · GitHub</a></p>
<p>Essentially, I have my main ModuleName.py:</p>
<pre><code class="lang-auto">import ModuleLib
class ModuleName(ScriptedLoadableModule):
...
def registerSampleData():
...
class ModuleNameTest(ScriptedLoadableModuleTest):
...
</code></pre>
<p>In the same directory, I have a subdirectory called ModuleNameLib with:<br>
<strong>init</strong>.py:</p>
<pre><code class="lang-auto">from .Logic import ModuleNameLogic
from .Widget import ModuleNameWidget
</code></pre>
<p>Logic.py:</p>
<pre><code class="lang-auto">from . import Widget

class ModuleNameLogic(ScriptedLoadableModuleLogic):
...
</code></pre>
<p>And Widget.py:</p>
<pre><code class="lang-auto">from . import Logic

class ModuleNameWidget(ScriptedLoadableModuleWidget, VTKObservationMixin):
...
</code></pre>
<p>I have also updated my CMakeLists.txt with:</p>
<pre><code class="lang-auto">set(MODULE_PYTHON_SCRIPTS
  ${MODULE_NAME}.py
  ${MODULE_NAME}Lib/__init__
  ${MODULE_NAME}Lib/Logic
  ${MODULE_NAME}Lib/Widget
  )
</code></pre>
<p>When I run the module, I get a blank screen with the viewers on the right but no widget. I’m not sure if I’ve missed anything or made a mistake somewhere - I’m new to Slicer module development so any help would be appreciated. TIA!</p>

---

## Post #2 by @pieper (2023-04-29 13:16 UTC)

<aside class="quote no-group" data-username="asyeda" data-post="1" data-topic="29204">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/3da27b/48.png" class="avatar"> asyeda:</div>
<blockquote>
<p>Logic.py:</p>
<pre><code class="lang-auto">from . import Widget

class ModuleNameLogic(ScriptedLoadableModuleLogic):
</code></pre>
</blockquote>
</aside>
<p>This may not be the only issue, but the logic class shouldn’t know about the widget.  The widget can use the logic to modify data (the nodes in the MRML scene) and the widget should update the GUI based on events that it observes.  this way the GUI can be kept up to date with any scene changes made by it’s own or any other logic.</p>
<p>Good practice is to start with the Extension Wizard and make a module that is working and then incrementally change it to meet your needs, testing that it works at every step.</p>

---

## Post #3 by @asyeda (2023-05-08 15:58 UTC)

<p>The logic class doesn’t actually use the widget, I had included it in the imports since I thought that may avoid the error. I have since removed it. I’ve added the widget class back to the main module file and kept the logic class in its own file based on <a href="https://discourse.slicer.org/t/python-scripted-module-development-reload-feature-for-multiple-files/6363/6">this thread</a> stating that the widget must be in the main module file, and this works fine. <a href="https://discourse.slicer.org/t/is-it-possible-to-split-a-python-extension-into-multiple-files/21713/5">Another thread</a> says that the widget can be kept in its own file, but I am having issues recreating it the same way.</p>
<p>Is there a way to keep the widget separate from the main module class, and if so, how can I correctly point to the right locations so the module class is aware of the widget?</p>

---

## Post #4 by @pieper (2023-05-09 13:37 UTC)

<p>The .py file at the top of the module’s directory is a special convention to have the entry points for the module to facilitate the discovery process.  You can make a GUILib subfolder or similar that has helper classes for the GUI, such as composite widgets that also make use of the logic.  There are several ways to organize this, but looking at the <a href="https://github.com/Slicer/Slicer/tree/main/Modules/Scripted/DICOMLib">DICOMLib</a> folder should give you an idea.  I don’t recall now why this isn’t a subfolder of the DICOM module folder, but in any case it’ll give an idea how widgets and logic are organized.</p>

---
