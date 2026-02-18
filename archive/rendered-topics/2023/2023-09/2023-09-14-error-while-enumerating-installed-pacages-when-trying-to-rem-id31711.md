# Error while enumerating installed pacages when trying to remote attach from VS code

**Topic ID**: 31711
**Date**: 2023-09-14
**URL**: https://discourse.slicer.org/t/error-while-enumerating-installed-pacages-when-trying-to-remote-attach-from-vs-code/31711

---

## Post #1 by @Samuel_Cheng (2023-09-14 13:36 UTC)

<p>I am a newbie to Slicer extension development and tried to set up python debugging with vs code following the github <a href="https://github.com/SlicerRt/SlicerDebuggingTools" rel="noopener nofollow ugc">instruction</a>. But I got the error as shown below in the Slicer Python Console. I tested it on Ubuntu 20.04, Slicer 5.4.0 r31938 / 311cb26, and VS code 1.82.1.</p>
<p>Thanks on advance</p>
<blockquote>
<p>Python 3.9.10 (main, Aug 19 2023, 11:01:17)<br>
[GCC 7.3.1 20180303 (Red Hat 7.3.1-5)] on linux2</p>
<blockquote>
<blockquote>
<blockquote></blockquote>
</blockquote>
</blockquote>
<p>E+00008.717: Error while enumerating installed packages.</p>
<pre><code>         Traceback (most recent call last):
           File "/home/phsamuel/Downloads/Slicer-5.4.0-linux-amd64/lib/Python/lib/python3.9/site-packages/debugpy/common/log.py", line 361, in get_environment_description
             report("    {0}=={1}\n", pkg.name, pkg.version)
         AttributeError: 'PathDistribution' object has no attribute 'name'
         
         Stack where logged:
           File "/home/phsamuel/Downloads/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/DebuggingTools/lib/Slicer-5.4/qt-scripted-modules/PyDevRemoteDebug.py", line 248, in onConnect
             self.logic.connect()
           File "/home/phsamuel/Downloads/Slicer-5.4.0-linux-amd64/slicer.org/Extensions-31938/DebuggingTools/lib/Slicer-5.4/qt-scripted-modules/PyDevRemoteDebug.py", line 578, in connect
             debugpy.listen(self.getPortNumber())
           File "/home/phsamuel/Downloads/Slicer-5.4.0-linux-amd64/lib/Python/lib/python3.9/site-packages/debugpy/public_api.py", line 31, in wrapper
             return wrapped(*args, **kwargs)
           File "/home/phsamuel/Downloads/Slicer-5.4.0-linux-amd64/lib/Python/lib/python3.9/site-packages/debugpy/server/api.py", line 122, in debug
             ensure_logging()
           File "/home/phsamuel/Downloads/Slicer-5.4.0-linux-amd64/lib/Python/lib/python3.9/site-packages/debugpy/server/api.py", line 61, in ensure_logging
             log.describe_environment("Initial environment:")
           File "/home/phsamuel/Downloads/Slicer-5.4.0-linux-amd64/lib/Python/lib/python3.9/site-packages/debugpy/common/log.py", line 369, in describe_environment
             info("{0}", get_environment_description(header))
           File "/home/phsamuel/Downloads/Slicer-5.4.0-linux-amd64/lib/Python/lib/python3.9/site-packages/debugpy/common/log.py", line 363, in get_environment_description
             swallow_exception("Error while enumerating installed packages.")
           File "/home/phsamuel/Downloads/Slicer-5.4.0-linux-amd64/lib/Python/lib/python3.9/site-packages/debugpy/common/log.py", line 215, in swallow_exception
             _exception(format_string, *args, **kwargs)
</code></pre>
</blockquote>

---

## Post #2 by @lassoan (2023-09-18 12:53 UTC)

<aside class="quote no-group" data-username="Samuel_Cheng" data-post="1" data-topic="31711">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/samuel_cheng/48/18355_2.png" class="avatar"> Samuel_Cheng:</div>
<blockquote>
<p><code>swallow_exception("Error while enumerating installed packages.")</code></p>
</blockquote>
</aside>
<p>It seems that debugpy developers <a href="https://github.com/microsoft/debugpy/issues/1379">messed up something last week or the week before</a>, so there were some broken versions. I’ve just tested the debugger in VS Code and everything works (with debugpy latest version 1.8.0).</p>
<p>You already have debugpy installed in Slicer’s Python environment, so if you want to get the latest version then you can run <code>pip_install('debugpy --upgrade')</code> in the Slicer Python console.</p>

---
