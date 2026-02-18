# Get Qt sender in Python slot

**Topic ID**: 18247
**Date**: 2021-06-21
**URL**: https://discourse.slicer.org/t/get-qt-sender-in-python-slot/18247

---

## Post #1 by @cpinter (2021-06-21 10:42 UTC)

<p>Hi all,</p>
<p>I have been debugging a strange issue, and maybe someone here can help.</p>
<p>When I load a scene in a Slicer custom app, an SH combobox <code>currentItemChanged</code> signal is emitted from an unknown place. There is nothing in the code that would set the selection programmatically (only the usual one in <code>updateGUIFromMRML</code> but with <code>blockSignals</code>), and I confirmed that it is not triggered by <code>setMRMLScene</code>. Unfortunately without knowing where this signal comes from, I cannot fix this issue in a good way.</p>
<p>My question is: how to get the sender in a Python slot? The <a href="https://doc.qt.io/qt-5/qobject.html#sender">sender</a> function does not work, because it returns <code>None</code> in all cases apparently.</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2021-06-21 12:57 UTC)

<p>If you hook up a debugger you can set a breakpoint in the slot (or in a C++ method you call from the python code if needed) and the stacktrace should give you a hint, particularly if the signal comes from C++.  Even if it comes from python you will see if it comes from a timer or other event.  Good luck!</p>

---

## Post #3 by @lassoan (2021-06-21 13:25 UTC)

<p>This question has come up in the <a href="https://sourceforge.net/p/pythonqt/discussion/631393/thread/a5cae166/?limit=25#db84">PythonQt discussion forum</a>. There was no usable answer there (they were satisfied with using lambda), but you could ask again either there or on <a href="https://github.com/MeVisLab/pythonqt/issues">github</a>.</p>
<p>I agree with <a class="mention" href="/u/pieper">@pieper</a> that running it in a debugger seems to be a good option. I think Visual Studio can even do mixed debugging - step through Python and C++ stacks (but I don’t remember if I have ever used it or just read about it).</p>

---

## Post #4 by @cpinter (2021-06-21 15:43 UTC)

<p>Thank you for the answers! Luckily I think this specific issue can be debugged on Windows (the application is primarily for Linux and some in-house libraries are Linux only) and I’ll try the suggested approach on Windows.</p>

---

## Post #5 by @finetjul (2021-06-21 16:01 UTC)

<p><code>currentItemChanged</code> may get called when your model gets populated (when the first item is added)  or unpopulated (when the current item gets removed). By observing all the signals emitted on the <code>model</code> itself that may give you a clue.</p>
<p>Alternatively, you should be able to set breakpoint with QtCreator on Linux (it was working back in the days <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> )</p>
<p>Hth,<br>
Julien.</p>

---

## Post #6 by @pieper (2021-06-21 16:06 UTC)

<aside class="quote no-group" data-username="finetjul" data-post="5" data-topic="18247">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/finetjul/48/146_2.png" class="avatar"> finetjul:</div>
<blockquote>
<p>Alternatively, you should be able to set breakpoint with QtCreator on Linux (it was working back in the days <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> )</p>
</blockquote>
</aside>
<p>Still worked great last time I checked a few months ago <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---
