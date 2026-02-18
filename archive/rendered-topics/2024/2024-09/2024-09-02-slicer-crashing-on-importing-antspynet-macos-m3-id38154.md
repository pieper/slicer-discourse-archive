# Slicer Crashing on importing antspynet (macOS M3)

**Topic ID**: 38154
**Date**: 2024-09-02
**URL**: https://discourse.slicer.org/t/slicer-crashing-on-importing-antspynet-macos-m3/38154

---

## Post #1 by @IVarha (2024-09-02 13:44 UTC)

<p>Hello I am creating a slicer extension and using antspynet in my development. Previously I used it on windows and it was working fine. I tried to install it in windows environment and it worked well.<br>
I tested imports on my python 3.9 local instance. It works for it.</p>
<p>I tested it with python provided by slicer as well but not get any meaningful logs:</p>
<p>PyDev console: starting.<br>
Python 3.9.10 (main, Apr  5 2024, 00:33:09)<br>
[Clang 14.0.6 (<a href="https://github.com/tru/llvm-release-build" rel="noopener nofollow ugc">https://github.com/tru/llvm-release-build</a> 686807a176470032c208f2 on darwin<br>
import antspynet<br>
error: [/Applications/Slicer.app/Contents/bin/./python-real] exit abnormally - Report the problem.<br>
Process finished with exit code 1</p>

---

## Post #2 by @lassoan (2024-09-12 01:44 UTC)

<p>It seems that antspynet uses tensorflow. Since the medical image computing community largely switched to pytorch, Slicer core developers no longer invest time into tensorflow support. If you need to use tensorflow then you need to investigate this issue yourself (if you have any specific questions then feel free to ask here), or you can install a Python environment where tensorflow works and call that from Slicer.</p>

---

## Post #3 by @IVarha (2024-09-16 08:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="38154">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>you can install a Python environment where tensorflow works and call that from Slicer</p>
</blockquote>
</aside>
<p>That is exactly what I used in the end.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="38154">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Slicer core developers no longer invest time into tensorflow support</p>
</blockquote>
</aside>
<p>Is there any reason why it fails in Slicer but works on general python environment? I have some problems with debugging it as I even don’t see any reasonable failing logs. Maybe it is possible to allow user use their installed python instance instead of PythonSlicer?</p>

---

## Post #4 by @muratmaga (2024-09-17 15:59 UTC)

<aside class="quote no-group" data-username="IVarha" data-post="3" data-topic="38154">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ivarha/48/66704_2.png" class="avatar"> IVarha:</div>
<blockquote>
<p>Is there any reason why it fails in Slicer but works on general python environment? I have some problems with debugging it as I even don’t see any reasonable failing logs. Maybe it is possible to allow user use their installed python instance instead of PythonSlicer?</p>
</blockquote>
</aside>
<p>Most likely library and build chain clashes…</p>

---
