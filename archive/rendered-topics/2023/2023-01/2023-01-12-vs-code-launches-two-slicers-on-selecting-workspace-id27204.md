# VS Code launches two Slicers on selecting workspace

**Topic ID**: 27204
**Date**: 2023-01-12
**URL**: https://discourse.slicer.org/t/vs-code-launches-two-slicers-on-selecting-workspace/27204

---

## Post #1 by @cpinter (2023-01-12 10:33 UTC)

<p>Hi all,</p>
<p>I’ve used VS Code with Slicer without problems in the past. However, for about a week, something strange and annoying happens when I start VS Code or when I switch workspaces:<br>
two Slicer instances are launched, opening their whole UI, starting with this message<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d7804fb266865689e5a0dee45deadd75a1c105d.png" alt="image" data-base62-sha1="b3jU9BOPC0fw1FyUjyPSt5mP9o1" width="428" height="209"></p>
<p>The strange thing is that these Slicers are not the ones I specified as the interpreter, which is <code>"python.defaultInterpreterPath": c:\\d\\S5R\\python-install\\bin\\PythonSlicer.exe</code>, but installed 5.0.2’s which I don’t know where VS Code knows about.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.app.slicerHome
'C:/Users/pinte/AppData/Local/NA-MIC/Slicer 5.0.2/bin/..'
</code></pre>
<p>The splash screen popped up before as well on startup or workspace switch, but this is new and I have no idea how to get rid of these 5.0.2 startups. Thanks for any help!</p>

---

## Post #2 by @ebrahim (2023-01-12 15:03 UTC)

<blockquote>
<p>The splash screen popped up before as well on startup or workspace switch, but this is new and I have no idea how to get rid of these 5.0.2 startups.</p>
</blockquote>
<p>I’ve also been getting a Slicer splash screen on VS Code launch.<br>
I’m on Ubuntu 20.04.</p>

---

## Post #3 by @cpinter (2023-01-12 15:37 UTC)

<p>The splash screen is OK, my problem is different, and it is a blocking issue for me. Please focus on that if you have any insight.</p>

---

## Post #4 by @lassoan (2023-01-12 18:15 UTC)

<p>VS Code (and its Python and Jupyter extensions) is very opinionated. It makes lots of assumptions about your Python environment and uses low-level hacks that only work well if all those assumptions are correct (e.g., if you use a standard Python environment).</p>
<p>It seems that the VS Code Python plugin <a href="https://github.com/microsoft/vscode-python/blob/main/pythonFiles/interpreterInfo.py">queries interpreter parameters at startup</a> via an <a href="https://github.com/microsoft/vscode-python/blob/main/pythonFiles/get_output_via_markers.py">output capture wrapper script</a> for all interpreters it knows about.</p>
<p>VS Code assumes that launching a Python interpreter is an invisible, very lightweight operation. It is true for many cases, it would be no problem for PythonSlicer.exe interpreter, etc. but the assumption is not true for Slicer.exe, which is not a lightweight process.</p>
<p>The solution is probably to remove Slicer.exe from the list of interpreters that VS Code knows about. One possible solution (from <a href="https://stackoverflow.com/a/52849570">here</a>) is to temporarily remove Slicer.exe, start VS Code, and select the no-longer-existing Slicer.exe Python interpreter. But maybe you can find the list of interpreters somewhere else and remove Slicer.exe from that list.</p>

---

## Post #5 by @cpinter (2023-01-12 20:06 UTC)

<p>Thank you very much, looking into it!</p>

---

## Post #6 by @JACKCHAN000 (2023-03-28 16:09 UTC)

<p>Hello, I am having the same problem.<br>
Any solution to solve this problem?</p>

---

## Post #7 by @lassoan (2023-03-28 19:13 UTC)

<aside class="quote no-group" data-username="JACKCHAN000" data-post="6" data-topic="27204">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jackchan000/48/65425_2.png" class="avatar"> JACKCHAN000:</div>
<blockquote>
<p>Any solution to solve this problem?</p>
</blockquote>
</aside>
<p>Yes. You need to remove Slicer.exe from the list of Python interpreters in Visual Studio Code as described above (or just tolerate this annoyance - it has no side effects, other than you need to close these Slicer instances that VS Code decided to launch).</p>

---

## Post #8 by @JACKCHAN000 (2023-03-29 12:05 UTC)

<p>But I can’t find any interpreters about slicer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/1525f902f902c3ddd846c26cc09b0db050716c0c.png" data-download-href="/uploads/short-url/315nKjM4o2T5QxBBwMXxhVJBClm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/1525f902f902c3ddd846c26cc09b0db050716c0c_2_690x261.png" alt="image" data-base62-sha1="315nKjM4o2T5QxBBwMXxhVJBClm" width="690" height="261" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/1525f902f902c3ddd846c26cc09b0db050716c0c_2_690x261.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/5/1525f902f902c3ddd846c26cc09b0db050716c0c_2_1035x391.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/1525f902f902c3ddd846c26cc09b0db050716c0c.png 2x" data-dominant-color="2B2F35"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1070×405 47.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
When I launch vscode, it will start searching slicer kernel.json file.<br>
No error is returned if I set permission for not allowing any program to access.</p>

---
