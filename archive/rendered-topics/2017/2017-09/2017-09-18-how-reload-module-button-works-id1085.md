---
topic_id: 1085
title: "How Reload Module Button Works"
date: 2017-09-18
url: https://discourse.slicer.org/t/1085
---

# How reload module button works?

**Topic ID**: 1085
**Date**: 2017-09-18
**URL**: https://discourse.slicer.org/t/how-reload-module-button-works/1085

---

## Post #1 by @ktdiedrich (2017-09-18 13:18 UTC)

<p>Hi,<br>
Is  the “Reload” button supposed to work in a ScriptedLoadableModuleTemplate right after creating it in the Extension Wizard? Or does something have to be set in the code?</p>
<p>I created a couple  ScriptedLoadableTemplateModule with the Extension Wizard and then made some small changes to <a href="http://ScriptedLoadableModuleTemplate.py" rel="nofollow noopener">ScriptedLoadableModuleTemplate.py</a>: self.parent.contributors and self.parent.acknowledgementText and pressed “Reload” but the changes don’t show up until I press “Restart Slicer” button and restart Slicer.</p>
<p>The “Enable Developer Mode” is checked.<br>
It’s Slicer 4.6.2 on Mac OS X, binary version. I’m only tying to add in Python Modules.<br>
I added the new ScriptedLoadableModuleTemplate directory (which are outside the Slicer installation directory) to the “Additional module paths:” and the added modules show up with the current changes when Slicer starts.</p>
<p>Best regards,<br>
Karl</p>

---

## Post #2 by @lassoan (2017-09-19 14:59 UTC)

<p>Use the latest nightly version, it should work correctly there. If you have trouble with latest nightly version, too, then let us know.</p>

---

## Post #3 by @ihnorton (2017-11-27 16:44 UTC)

<p>Would it make sense to have the Python (script) CMake install step create a symlink from the runtime directory to the original script source in the source directory, on platforms where user symlink is supported? This would avoid the rebuild (make/ninja/etc.) step required to copy modified scripts from source tree to runtime directory before they can be reloaded…</p>
<p>I guess this could be as simple as changing the <code>copy</code> command to <code>create_symlink</code> in <a href="https://github.com/commontk/CTK/blob/master/CMake/ctkMacroCompilePythonScript.cmake#L120-L123">ctkMacroCompilePythonScript</a>. But I think that will break packaging unless the copy step is done somewhere else, or if CPack can be told to follow symlinks.  cc <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #4 by @lassoan (2017-11-28 03:29 UTC)

<p>During development, I just add the source folder (not the install folder) to “Additional module paths” for scripted modules.</p>

---

## Post #5 by @pieper (2017-11-28 13:48 UTC)

<p>Hi Karl - changing the template after generating the module shouldn’t have any effect but changes to the generated scripted module should take effect after hitting the Reload button.</p>
<p>Like <a class="mention" href="/u/lassoan">@lassoan</a> during development I use Reload all the time.  I don’t put the code in the Slicer tree and I typically don’t rebuild scripted modules during development.  I run Slicer with the --additional-module-paths option followed by the list of module directories I want to test (since I often have several going at once and don’t want to change my settings).</p>
<p><a class="mention" href="/u/ihnorton">@ihnorton</a> I prefer to avoid things like symlinks that are not consistent across platforms.</p>

---

## Post #6 by @ihnorton (2017-11-28 14:45 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="1085">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>I prefer to avoid things like symlinks that are not consistent across platforms.</p>
</blockquote>
</aside>
<p>Alright. Win10 Fall Creators Update does (finally) provide unprivileged symlinks, but it will take a while before that can be generally relied upon.</p>

---
