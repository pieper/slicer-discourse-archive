# Load python script from harddisk in Slicers´s Python Interactor?

**Topic ID**: 17399
**Date**: 2021-04-30
**URL**: https://discourse.slicer.org/t/load-python-script-from-harddisk-in-slicers-s-python-interactor/17399

---

## Post #1 by @rbumm (2021-04-30 19:16 UTC)

<p>I was looking for that for ages about a month ago, so I just want to share the solution here (it may be obvious to you experts):</p>
<p>You can load and run a python script from the hard drive in the Python interactor (one-line command) with</p>
<pre><code class="lang-auto">    &gt;&gt; exec(open("filename.py").read())

</code></pre>
<p>This works in Slicer 4.11+ and seems to require Python3.</p>
<p>In Windows I used:</p>
<pre><code class="lang-auto">    &gt;&gt; exec(open(r"C:\Users\Yourname\Python\test.py").read())

</code></pre>
<p>Use slashes and do not forget the initial “r” …</p>
<p>Regards<br>
Rudolf</p>

---

## Post #2 by @pieper (2021-04-30 19:23 UTC)

<p>Yes, that’s a very handy pattern.  I use it a lot for quick testing.  It has the advantage that any global variables define in the .py file are still around in the python terminal for further testing.  I typically put that command with the path as a comment at the top of my script file so I can easily copy-paste it into the terminal when I start a new slicer.</p>

---

## Post #3 by @rbumm (2021-04-30 19:24 UTC)

<p>Haha that is exactly what I did, but forgot about my comment and searched the whole internet again  today <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #4 by @dalv.silvermann (2022-10-13 20:37 UTC)

<p>Dear Rudolf Bumm,<br>
Amazing! I’ve try to find this solution more than year I think :0)<br>
PS Also thanks for your MONAI label video presentation in summer '22!</p>

---

## Post #5 by @lassoan (2022-10-25 05:01 UTC)

<p>FYI, I’ve made some improvements in the past few days (will be available in the Slicer Preview Release from Wednesday):</p>
<ul>
<li>Instead of <code>exec(open(path).read())</code> you can hit <kbd>Ctrl</kbd>-<kbd>r</kbd>. Last path is remembered, so you can rerun a script using <kbd>Ctrl</kbd>-<kbd>r</kbd>, <kbd>Enter</kbd>.</li>
<li>If you copy-paste code into an empty line then instead of line-by-line execution, the entire code on the clipboard is executed at once (fixing the annoying indentation errors due to presence of empty lines).</li>
</ul>

---

## Post #6 by @pieper (2022-10-25 12:41 UTC)

<p>I wish we could try to follow ipython hotkey behavior wherever possible. <code>Ctrl-r</code> is incremental backward search in ipython and other readline based prompt systems and it’s a commonly used shortcut. Many of the common keyboard shortcuts](<a href="https://jakevdp.github.io/PythonDataScienceHandbook/01.02-shell-keyboard-shortcuts.html" class="inline-onebox">Keyboard Shortcuts in the IPython Shell | Python Data Science Handbook</a>) like <code>Ctrl-e</code> , <code>Ctrl-y</code> etc work already in our python interactor and if we are adding features it’s nice to follow existing patterns.</p>
<p>But I should also add that I like the new features - they will save a lot of time!</p>

---

## Post #7 by @lassoan (2022-10-25 12:48 UTC)

<p>It should not be a problem to switch the Ctrl-R shortcut to a more standard one now, especially because previously this feature have been practically unusable. I can push an update today. What should be the keyboard shortcut?</p>

---

## Post #8 by @pieper (2022-10-25 12:51 UTC)

<p>Thanks!</p>
<p>I’m not sure what would be best.  Let’s discuss at the developer meeting.  There are some existing cross platform issues we could address at the same time and come up with a good scheme so that slicer hotkeys are as compatible as possible with other hotkey conventions.</p>

---

## Post #9 by @lassoan (2022-10-25 13:19 UTC)

<p>I’ll also add Ctrl-l for clearing the terminal.</p>
<p>Ctrl-r for reverse search could be useful and it would not be hard to add, especially if we do it in a popup window instead of struggling with using the terminal window for it (IPython shell uses a special mode with the <code>(reverse-i-search)</code> prompt, while we could simply open a small search box).</p>
<p>We could also easily add Ctrl-k/u to cut content before/after the cursor, but it seems marginally useful (you can do Shift+Home/End, Ctrl-x instead).</p>
<p>However, most other shortcuts don’t seem to make sense for me, such as using</p>
<ul>
<li>Ctrl-a/e instead of Home/End keys</li>
<li>Ctrl-b/f instead of left/right arrow keys</li>
<li>Ctrl-p/n instead of up/down arrow keys</li>
<li>Ctrl-d instead of Delete key</li>
<li>Ctrl-t for switching the previous two characters (really, a shortcut for this??)</li>
<li>Ctrl-y instead of Ctrl-v for pasting</li>
</ul>

---

## Post #10 by @pieper (2022-10-25 15:37 UTC)

<p>Ctrl-r is the one I really care about.  The rest are very common for people used to emacs-based features.<br>
For me, even the chrome text window I’m using on mac allows Ctrl-[bfnpeatkyt] and that’s handy for people like me who are used to them from bash or ipython.  Yes, even Ctrl-t to transpose two characters works, although I don’t use that one.</p>
<p>After discussion on the slicer dev call, we think Ctrl-g is not otherwise used and can be associated with the concept of ‘go’.</p>

---
