---
topic_id: 20607
title: "Vscode Debugging Error Bug In Debugging Wrapper"
date: 2021-11-12
url: https://discourse.slicer.org/t/20607
---

# VSCode debugging error, bug in debugging wrapper?

**Topic ID**: 20607
**Date**: 2021-11-12
**URL**: https://discourse.slicer.org/t/vscode-debugging-error-bug-in-debugging-wrapper/20607

---

## Post #1 by @mikebind (2021-11-12 20:49 UTC)

<p>When I try to use python debugging of a custom python Slicer module using VSCode, I now regularly get the following error</p>
<pre><code class="lang-auto">Exception in thread ptvsd.EventLoop:
Traceback (most recent call last):
  File "C:/Users/mikeb/AppData/Local/NA-MIC/Slicer 4.13.0-2021-10-14/NA-MIC/Extensions-30315/DebuggingTools/lib/Slicer-4.13/qt-scripted-modules\ptvsd-4.1.3\ptvsd\wrapper.py", line 1292, in done
    fut.result()
  File "C:/Users/mikeb/AppData/Local/NA-MIC/Slicer 4.13.0-2021-10-14/NA-MIC/Extensions-30315/DebuggingTools/lib/Slicer-4.13/qt-scripted-modules\ptvsd-4.1.3\ptvsd\futures.py", line 40, in result
    reraise(self._exc_info)
  File "C:/Users/mikeb/AppData/Local/NA-MIC/Slicer 4.13.0-2021-10-14/NA-MIC/Extensions-30315/DebuggingTools/lib/Slicer-4.13/qt-scripted-modules\ptvsd-4.1.3\ptvsd\reraise3.py", line 8, in reraise
    raise exc_info[1].with_traceback(exc_info[2])
  File "C:/Users/mikeb/AppData/Local/NA-MIC/Slicer 4.13.0-2021-10-14/NA-MIC/Extensions-30315/DebuggingTools/lib/Slicer-4.13/qt-scripted-modules\ptvsd-4.1.3\ptvsd\futures.py", line 155, in callback
    x = it.send(fut.result())
  File "C:/Users/mikeb/AppData/Local/NA-MIC/Slicer 4.13.0-2021-10-14/NA-MIC/Extensions-30315/DebuggingTools/lib/Slicer-4.13/qt-scripted-modules\ptvsd-4.1.3\ptvsd\wrapper.py", line 2274, in on_completions
    for item in list(xml.comp):
  File "C:/Users/mikeb/AppData/Local/NA-MIC/Slicer 4.13.0-2021-10-14/NA-MIC/Extensions-30315/DebuggingTools/lib/Slicer-4.13/qt-scripted-modules\ptvsd-4.1.3\ptvsd\untangle.py", line 87, in __getattr__
    "'%s' has no attribute '%s'" % (self._name, key)
AttributeError: 'xml' has no attribute 'comp'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.13.0-2021-10-14\lib\Python\Lib\threading.py", line 916, in _bootstrap_inner
    self.run()
  File "C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.13.0-2021-10-14\lib\Python\Lib\threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "C:/Users/mikeb/AppData/Local/NA-MIC/Slicer 4.13.0-2021-10-14/NA-MIC/Extensions-30315/DebuggingTools/lib/Slicer-4.13/qt-scripted-modules\ptvsd-4.1.3\ptvsd\futures.py", line 113, in run_forever
    f(*args)
  File "C:/Users/mikeb/AppData/Local/NA-MIC/Slicer 4.13.0-2021-10-14/NA-MIC/Extensions-30315/DebuggingTools/lib/Slicer-4.13/qt-scripted-modules\ptvsd-4.1.3\ptvsd\futures.py", line 72, in invoke_callbacks
    cb(self)
  File "C:/Users/mikeb/AppData/Local/NA-MIC/Slicer 4.13.0-2021-10-14/NA-MIC/Extensions-30315/DebuggingTools/lib/Slicer-4.13/qt-scripted-modules\ptvsd-4.1.3\ptvsd\wrapper.py", line 1294, in done
    traceback.print_exc(file=sys.__stderr__)
  File "C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.13.0-2021-10-14\lib\Python\Lib\traceback.py", line 163, in print_exc
    print_exception(*sys.exc_info(), limit=limit, file=file, chain=chain)
  File "C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.13.0-2021-10-14\lib\Python\Lib\traceback.py", line 105, in print_exception
    print(line, file=file, end="")
OSError: [WinError 1] Incorrect function
</code></pre>
<p>Debugging works normally until I get this error, and then it seems broken after that.  I can still type things in the debugging console window in VSCode, but I get no responses anymore (i.e. anything I type at the debugging console prompt yields no response).</p>
<p>Before I get the error, there are very active auto-complete options as I type at the console, then usually after a few commands entered there (like checking variable values, function returns, normal and very simple debugging stuff) the error is thrown at what seems like random times.  For example, in the middle of while I’m typing, or while I’m paused trying to remember something.  Not usually right after I’ve pressed return.</p>
<p>Looking at the error message, it seems like it might have to do with a case where a list of auto-completions is missing (I’m guessing the list of autocomplete options might be normally be in <code>xml.comp</code>, and that isn’t getting initialized in the case where the error occurs).  Since I don’t think the error has anything to do with my code, I’m a little surprised that other users aren’t running into this all the time, as it is now happening very consistently for me.</p>
<p>I am using Slicer 4.13.0-2021-10-14 on Windows 10 and Visual Studio Code 1.62.2.</p>
<p>Any suggestions?  A temporary workaround where I could turn off the autocomplete suggestions in the debug console in VSCode would be OK for me. They’re handy, but the inability to run a debug session for longer than ~45 seconds is hard to get around.</p>

---

## Post #2 by @mikebind (2021-11-12 21:20 UTC)

<p>I found an easy way to reproducibly get to the error. Connect the debugger, trigger getting to a breakpoint, then, at the debugging console prompt, type the same letter repeatedly until there are no more autocomplete suggestions, and then type one more of that letter. On typing that last letter, the error is reproducibly triggered for me.</p>
<p>This behavior supports that it is due to a bug in the autocompletion code.  I have reproduced by setting breakpoints in different modules, so it doesn’t seem to depend on which module is currently being debugged.</p>

---

## Post #3 by @lassoan (2021-11-13 14:19 UTC)

<p>VSCode debugging often breaks because each IDE version only works with a specific range of ptvsd versions. Usually latest versions are compatible, but maybe they don’t release new versions for Python-3.6 anymore or just not test thoroughly with this old Python version. We are working on updating our Python version, so that might help.</p>
<p>I usually use PyCharm for debugging as I find its Python console and automatic reattaching more convenient. It often breaks after updating PyCharm (and they fix it in patch releases), so it seems that they don’t really test the debugger either.</p>

---

## Post #4 by @mikebind (2021-11-13 18:08 UTC)

<p>Thanks, I’ll try PyCharm and see if that works for me.</p>

---
