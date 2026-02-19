---
topic_id: 3069
title: "How Can I Modify Slicers Pythonpath Variable"
date: 2018-06-04
url: https://discourse.slicer.org/t/3069
---

# How can I modify Slicer's PYTHONPATH variable?

**Topic ID**: 3069
**Date**: 2018-06-04
**URL**: https://discourse.slicer.org/t/how-can-i-modify-slicers-pythonpath-variable/3069

---

## Post #1 by @mangotee (2018-06-04 16:37 UTC)

<p>Hi all,</p>
<p>afaik, Slicer does not inherit the system’s environment variables at startup, does it? If so, where does the python kernel in Slicer read its PYTHONPATH environment variable from? I have a few convenience functions which I currently have to import manually in the python console after every startup via:<br>
import sys<br>
sys.path.append("/path/to/my/utility/code")<br>
For my native python kernel (anaconda env) in my OS (Mac), I put that info into ~/.bash_profile:<br>
export PYTHONPATH=/path/to/my/utility/code:$PYTHONPATH<br>
in order to access my custom code in all projects.<br>
So, two questions:</p>
<ol>
<li>Is there an equivalent I can do for Slicer, such that my utility paths are loaded at startup?</li>
<li>I regularly replace my Slicer nightly build with the latest version. Apart from “losing” all my extensions, I would then lose this path as well. Is there a way to make ideally both (extensions and PYTHONPATH) persistent?</li>
</ol>
<p>Many thanks in advance!!<br>
Cheers,<br>
Ahmad</p>

---

## Post #2 by @lassoan (2018-06-04 17:57 UTC)

<p>You can put such initialization code in .slicerrc.py file in your HOME folder. See details here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_systematically_execute_custom_python_code_at_startup_.3F">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#How_to_systematically_execute_custom_python_code_at_startup_.3F</a></p>

---

## Post #3 by @mangotee (2018-06-04 20:42 UTC)

<p>That’s great, many thanks for the quick response! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"><br>
About question 2: Is there any way to restore my extensions and my additional module paths after installing a new version of Slicer (e.g. a new nightly build), i.e. making them persistent? If not, I will keep re-loading/re-entering them manually.<br>
Again, many thanks for your help!</p>

---

## Post #4 by @lassoan (2018-06-04 21:33 UTC)

<p>In recent nightly builds, in the extension manager you can reinstall all previously installed extension by a few clicks.</p>
<p>If you want to add local modules (not installed through the extension manager) then you can do it manually in the slicerrc file. For example:</p>
<p>moduleFactory = slicer.app.moduleManager().factoryManager()<br>
moduleFactory.registerModule(qt.QFileInfo(‘c:/D/SlicerDebuggingToolsExtension/PyDevRemoteDebug/PyDevRemoteDebug.py’))<br>
moduleFactory.loadModules([‘PyDevRemoteDebug’])</p>

---

## Post #5 by @mangotee (2018-06-05 06:30 UTC)

<p>OK, that’s excellent… many thanks for these tips!</p>

---
