# Autocomplete code lines for slicer in an IDE?

**Topic ID**: 7390
**Date**: 2019-07-02
**URL**: https://discourse.slicer.org/t/autocomplete-code-lines-for-slicer-in-an-ide/7390

---

## Post #1 by @Amine (2019-07-02 22:05 UTC)

<p>new to slicer development, saw this tutorial and they seem to use an IDE that supports autocompleting statements unique to slicer as in the python interactor:</p>
<p>            <iframe width="480" height="360" src="https://www.youtube.com/embed/njoTEisxAJ4?feature=oembed&amp;wmode=opaque&amp;list=PLJWCUXz3GeAfmYLiFcKus_c0jcsMnVsgb" frameborder="0" allowfullscreen="" seamless="seamless" sandbox="allow-same-origin allow-scripts allow-forms allow-popups allow-popups-to-escape-sandbox allow-presentation"></iframe>
</p>
<p>what IDE could i use for that feature ( or how to add slicer API support to IDEs like pycharm?)<br>
Thanks for your help.</p>

---

## Post #2 by @lassoan (2019-07-03 13:22 UTC)

<p>The easiest and most robust way of getting auto-complete in an IDE is to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions" rel="nofollow noopener">attach a Python debugger</a> put a breakpoint in the code where you want to add more code, and make the code stop there.</p>
<p>Auto-complete without debugging relies on static code analysis, which does not work very well for the dynamically constructed Python-wrapped C++ objects that Slicer and its libraries use, but you can give it a try. Specify “PythonSlicer” executable as your Python interpreter for the IDE. I’ve found that Eclipse (LiClipse) auto-complete and documentation lookup works reasonable well. Last time I tried, PyCharm’s skeleton generation failed for many components. I have <a href="https://youtrack.jetbrains.com/issue/PY-31590" rel="nofollow noopener">reported the issue</a>, but there was no follow-up. The issue can be fixed manually by patching of the skeleton generator, but maybe Python wrapping of VTK should be improved instead to make it more friendly to current IDEs.</p>

---

## Post #3 by @Amine (2019-07-03 13:41 UTC)

<p>i will try that, thanks a lot!!</p>

---

## Post #4 by @jcfr (2019-07-08 13:43 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="7390">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>but maybe Python wrapping of VTK should be improved instead to make it more friendly to current IDEs</p>
</blockquote>
</aside>
<p>Would have some more specific feedback regarding this ?</p>

---

## Post #5 by @lassoan (2019-07-09 03:24 UTC)

<p>I think this is already on David Gobbi’s radar - see for example <a href="https://discourse.vtk.org/t/vtk-8-2-python-and-vscode/704/3" rel="nofollow noopener">https://discourse.vtk.org/t/vtk-8-2-python-and-vscode/704/3</a></p>

---

## Post #6 by @park (2025-02-03 14:08 UTC)

<p>Hello,</p>
<p>I understand that Slicer’s Python auto-complete is not fully supported. <a href="https://discourse.slicer.org/t/developing-slicer-modules-in-visual-studio-visual-studio-code/9496/25">Through previous discussions and various configuration attempts</a>, I was able to confirm that auto-completion works to some extent when Slicer is connected to a debugger. However, after resetting my VSCode settings to reproduce the setup, I found that while debugging still works fine, auto-completion no longer functions.</p>
<p>Would you happen to know if there are any additional settings required to enable auto-completion while debugging? Also, I would appreciate any suggestions on how to improve the development experience.</p>
<p>Thank you in advance for your guidance.</p>

---

## Post #7 by @pieper (2025-02-10 16:41 UTC)

<p>Personally I find the python console in Slicer the best way to debug and autocomplete.  I don’t find existing IDEs as useful,</p>
<p>With some extra work, the <a href="https://github.com/SlicerMorph/SlicerScriptEditor">ScriptEditor</a> code could be made really powerful for development and debugging, since it has access to everything needed during the completion callback (it can introspect the python API in addition to already allocated variables).  If people have time to invest that’s where I would focus.</p>

---
