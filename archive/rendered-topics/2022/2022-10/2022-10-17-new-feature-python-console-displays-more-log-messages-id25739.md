# New feature: Python console displays more log messages

**Topic ID**: 25739
**Date**: 2022-10-17
**URL**: https://discourse.slicer.org/t/new-feature-python-console-displays-more-log-messages/25739

---

## Post #1 by @lassoan (2022-10-17 21:39 UTC)

<p>Until now, the Python console only displayed Python outputs and Python log messages. Therefore, if a Python command executed a VTK method and that VTK method logged an error or warning, it was not immediately visible for the developer (the developer had to notice the change in the log icon, click on it, and scroll down to see the new message).</p>
<p>In latest Slicer Preview Release (Slicer 5.1.0-2022-10-15 and later), <strong>the Python console displays log messages from all sources</strong> - Python, Qt, VTK, ITK.</p>
<p>For example:</p>
<p>Old behavior (return value indicates error but no hint on what went wrong):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/9964f12107a884930bf2f0e3c69c0c999baa2c18.png" data-download-href="/uploads/short-url/lSZjQaG58N7YUVNF5G9hGJ1o79u.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/9964f12107a884930bf2f0e3c69c0c999baa2c18.png" alt="image" data-base62-sha1="lSZjQaG58N7YUVNF5G9hGJ1o79u" width="690" height="100" data-dominant-color="1F2123"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1034×150 3.69 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>New behavior:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc4c45efb59ff45266786a6a4168fef2e3388a42.png" data-download-href="/uploads/short-url/qRLb64f8dYPzJSBJNQUa0tVONcS.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc4c45efb59ff45266786a6a4168fef2e3388a42.png" alt="image" data-base62-sha1="qRLb64f8dYPzJSBJNQUa0tVONcS" width="690" height="107" data-dominant-color="212122"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1168×182 6.55 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If the extra messages are not desirable (e.g., because they cause too much distraction for a developer) then <strong>the log level can be adjusted in Application Settings → Python → Log level</strong>. Default log level is <code>Warning</code>, which means that warnings and error log messages are displayed. Set level to <code>None</code> to prevent displaying any log messages (as it was before). Set level to <code>Debug</code> to show all available messages.</p>

---

## Post #2 by @jamesobutler (2022-10-29 04:45 UTC)

<p>It’s great to see log messages from VTK in the python console as you show in your images above!</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Is this change supposed to impact the functionality that is the <code>Slicer_BUILD_WIN32_CONSOLE_LAUNCHER</code> option with local Slicer builds? With that option on Windows we would see a console window open in addition to the Slicer main window and that would contain all the logging output from python, Qt, VTK, ITK sources.  Currently with the latest Slicer preview, modules that have any python logging do not display these messages to the Win32 console window. These python logging messages are only seen when viewing the actual log file or in the python console (of course as long as the message is within the Application Settings-&gt;Python-&gt;Log level).</p>

---

## Post #3 by @lassoan (2022-10-29 18:14 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="25739">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Currently with the latest Slicer preview, modules that have any python logging do not display these messages to the Win32 console window</p>
</blockquote>
</aside>
<p>Previously, Slicer relied on standard output for Python logging (the Python logger printed on the standard output and the application logger captured that output). This was too restrictive (it was not possible to make log messages appear in the Python console without appearing twice in the application log). Now they are independently configurable and so the previous limitations are gone.</p>
<p>If you want Python logs to be printed on the process output then you can register a Python log handler to do that, the same way as you would do in any other Python environment.</p>

---

## Post #4 by @jamesobutler (2022-10-29 20:00 UTC)

<p>With these latest changes, is there any value to still have <code>Slicer_BUILD_WIN32_CONSOLE_LAUNCHER</code> as a a default build option if building Python support is a default option which supports viewing all the output on the python console? I’m thinking about some new python Slicer developers that may get confused about where to look for logging output.</p>

---

## Post #5 by @lassoan (2022-10-29 20:18 UTC)

<p>For typing Python commands or debugging Python code I would recommend using the Python console.</p>
<p>For checking what happened in the application, the application log viewer has the slight advantages (filtering, grouping, and clearing) compared to the Python console.</p>
<p>For reporting errors, the Help/Report a bug has some advantages (easier to copy all messages, previous sessions are available).</p>
<p>The only use that I see for the process output is when there is no application GUI.</p>

---

## Post #6 by @lassoan (2023-02-03 14:42 UTC)

<p>A post was split to a new topic: <a href="/t/display-external-process-output-in-module-gui/27617">Display external process output in module GUI</a></p>

---

## Post #7 by @adeguet1 (2023-04-07 17:49 UTC)

<p>Is there a way to set the Python log level from Python?  I looked in <code>slicer.app</code> and didn’t find anything obvious.  I have some code that intentionally calls methods that trigger warnings/errors to probe/test a configuration and would like to temporarily disable the logs.  Something like:</p>
<p>oldLevel = slicer.app.python.getLogLevel()<br>
slicer.app.python.setLogLevel(‘None’)<br>
run_some_tests()<br>
slicer.app.python.setLogLevel(oldLevel)</p>

---

## Post #8 by @jamesobutler (2023-04-07 18:19 UTC)

<p>You can set the Python log level from the Slicer settings:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8af028d848dea334ffe89e4241540e7841c700b.png" alt="image" data-base62-sha1="qlMOkao6eIQNvmeHznJ0yWjYMvV" width="645" height="238"></p>
<p>Using code, <code>slicer.app</code> contains <code>slicer.app.setPythonConsoleLogLevel()</code> which you can use such as <code>slicer.app.setPythonConsoleLogLevel(ctk.ctkErrorLogLevel.Error)</code> to set it to the Error level. Unfortunately it appears that the None level isn’t working correctly from python. This functionality was originally included as part of <a href="https://github.com/Slicer/Slicer/commit/12fcde42d8b47566eb39de395a516701759d1716" rel="noopener nofollow ugc">this commit</a>.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; ctk.ctkErrorLogLevel.None
  File "&lt;console&gt;", line 1
    ctk.ctkErrorLogLevel.None
                         ^
SyntaxError: invalid syntax
</code></pre>

---

## Post #9 by @lassoan (2023-04-07 22:07 UTC)

<p>Log level in the Python console is a user preference. Modules can of course can change it, but doing so would upset users. If you want to change the level to avoid excessive amount of error/warning messages then I would recommend to fix the root cause of those.</p>
<aside class="quote no-group" data-username="jamesobutler" data-post="8" data-topic="25739">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p><code>ctk.ctkErrorLogLevel.None</code></p>
</blockquote>
</aside>
<p>This is due to the unfortunate naming of the enum. <code>None</code> is a Python keyword that cannot be redefined. We could rename it or add an alias.</p>

---

## Post #10 by @jamesobutler (2023-04-07 22:37 UTC)

<p>How about any of the following ideas?<br>
<code>ctk.ctkErrorLogLevel.Null</code><br>
<code>ctk.ctkErrorLogLevel.NoneLog</code><br>
<code>ctk.ctkErrorLogLevel.NoLog</code><br>
<code>ctk.ctkErrorLogLevel.Off</code><br>
<code>ctk.ctkErrorLogLevel.Silent</code></p>

---

## Post #11 by @lassoan (2023-04-07 23:09 UTC)

<p><code>Off</code> sounds good to me. We could deprecate <code>None</code> but keep it around for a while for backward compatibility.</p>

---

## Post #12 by @adeguet1 (2023-04-08 01:58 UTC)

<p>I agree that module shouldn’t change user preferences.  In my case, I’m trying to run some unit tests that will intentionally trigger some warnings and errors while testing the returned values.  At that point, all the tests succeed but the user will see multiple errors and warnings.  To avoid this confusion, I was wondering if there was a way to temporarily pause the logs.  In my initial post, I also asked if there was a way to get the current log level so I could restore it at the end.  This is mostly cosmetic so if the feature doesn’t exist it’s not big deal.</p>

---

## Post #13 by @jamesobutler (2023-04-08 02:25 UTC)

<p>During a run of unit tests isn’t it actually desired to see warnings and errors? Your concerns about the user seeing it doesn’t seem to match the type of action because a regular end user isn’t going to be running unit tests.</p>

---

## Post #14 by @lassoan (2023-04-08 12:09 UTC)

<p>For testing, you can connect a vtkErrorSink to any VTK class, which captures errors and warnings so that they are not logged. The error sink also counts the messages if each type do that you can easily check if the expected errors/warnings are present. Would this be sufficient for you?</p>

---

## Post #15 by @adeguet1 (2023-04-10 14:20 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> vtkErrorSink looks like the perfect fit for unit testing, I will definitely investigate.  Thank you for steering me away from the Python console log level.</p>

---
