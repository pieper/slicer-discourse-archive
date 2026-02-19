---
topic_id: 8162
title: "Using Slicer And Slicer Modules From Command Line"
date: 2019-08-24
url: https://discourse.slicer.org/t/8162
---

# Using Slicer and Slicer Modules from Command-Line

**Topic ID**: 8162
**Date**: 2019-08-24
**URL**: https://discourse.slicer.org/t/using-slicer-and-slicer-modules-from-command-line/8162

---

## Post #1 by @matt-warkentin (2019-08-24 18:28 UTC)

<p>Hi,</p>
<p>I am fairly expert in <code>R</code> and other languages, but I am admittedly relatively novice with <code>python</code> (though I am working to improve).</p>
<p>I think I am conceptually unclear on what it means to run <code>Slicer</code>/<code>Slicer</code> modules from the command line. Should running <code>Slicer</code> from the command-line be conceptually viewed as a running code/scripts inside a complete <code>python</code> environment (like a <code>conda</code> environment), whereby it contains a <code>python</code> interpreter and all necessary dependencies/modules? Could someone perhaps provide a high-level conceptual overview that might clarify what it actually means to run <code>Slicer</code> modules at the command-line?</p>
<p>I feel like connecting some of these dots may lead to a “eureka” moment for me, and I can begin to further appreciate using <code>Slicer</code> from the command-line. If it helps to place this into a more specific context, I am interested in learning how to perform batch <code>pyradiomics</code> feature extraction using the <code>SlicerRadiomicsCLI</code> module.</p>
<p>I have had no issues running the stand-alone <code>pyradiomics</code> CLI-tool, however, learning how to run effectively run <code>Slicer</code> modules from the command-line has broader benefit, given the large number of useful modules for other important image processing tasks.</p>
<p>Thanks you.</p>

---

## Post #2 by @pieper (2019-08-26 14:45 UTC)

<p>Hi Matt -</p>
<p>It sounds like you are on the right track - we try to support many different ways of accessing Slicer functionality but sometimes you do need to investigate a bit to decide what’s the most streamlined way to accomplish what you need.  Some of these practices are changing a bit now that we have Python3 support.</p>
<p>For streamlined batch processing and command line use, the python interpreter (<code>PythonSlicer</code>) can be used to access all the packages installed in Slicer, but won’t have the application context so many things won’t be available (e.g. rendering etc).  You can use <code>slicer.util.pip_install()</code> to add custom packages.</p>
<p>From a shell, you can run many of the CLI modules as commands, using Slicer’s launcher (e.g. <code>Slicer --launch BRAINSFit</code>), which is a very lightweight way to access the ITK based C++ code.</p>
<p>Or if you need a full environment where you can access any of the code you can use the full Slicer application and pass it whatever startup script you want (the expense is a little extra startup overhead).</p>
<p>Hope that helps,<br>
Steve</p>

---

## Post #3 by @matt-warkentin (2019-08-26 16:06 UTC)

<p>Hi Steve,</p>
<p>Thanks for the detailed reply. Could you perhaps clarify what you mean when you say I could use the <code>PythonSlicer</code> python interpreter? I know what a python interpreter is, in general, is the <code>PythonSlicer</code> interpreter just the python interpreter that is available to use inside the Slicer GUI (i.e. View &gt; Python Interactor)? Or is this something different entirely?</p>

---

## Post #4 by @pieper (2019-08-26 19:28 UTC)

<p>Hi Matt -</p>
<p><code>PythonSlicer</code> is an executable provided in the bin directory of the Slicer binaries.  It’s the same version of python that’s included with the app, but it acts like a normal <code>python</code> (or <code>python3</code>) executable in terms of running scripts.  So you can use it in place of regular python to make use of the Slicer environment for batch / cli operations.</p>
<p>Best,<br>
Steve</p>

---

## Post #5 by @matt-warkentin (2019-08-26 20:10 UTC)

<p>Oh, okay, I did not know that was provided with the Slicer binary. I was able to locate this <code>PythonSlicer</code> executable and run it with success. Thank you very much for clarifying.</p>
<p>Is <code>PythonSlicer</code> the interpreter that is used when one uses the Slicer kernel in a Jupyter Notebook? Or is this different yet again?</p>

---

## Post #6 by @pieper (2019-08-26 20:49 UTC)

<p>It’s basically the same python code and environment, but where <code>PythonSlicer</code> is a headless interpreter, SlicerJupyter allows you to control a running Slicer application via the notebook.  So Jupyter is basically doing the same thing as the python console in Slicer.</p>

---

## Post #7 by @matt-warkentin (2019-08-27 19:29 UTC)

<p>So, I tried to run <code>pyradiomics</code> from a shell using Slicer by locating what I thought was the correct <code>python</code> script (<code>SlicerRadiomics.py</code>) located in <code>Slicer &gt; Contents &gt; Extensions &gt; SlicerRadiomics &gt; lib &gt; Slicer-4.10 &gt; qt-scripted-modules</code> and ran the following code:</p>
<pre><code class="lang-auto">Slicer --no-main-window --python-script SlicerRadiomics.py
</code></pre>
<p>However, this did not seem to work. Am I on the right track?</p>
<p><strong>EDIT</strong>: I decided to try using the <code>pyradiomics</code> binary located in <code>Slicer &gt; Contents &gt; Extensions &gt; SlicerRadiomics &gt; bin</code> and it seems to work…</p>
<pre><code class="lang-auto">python pyradiomics --help
</code></pre>

---

## Post #8 by @pieper (2019-08-27 19:44 UTC)

<p>Note that here you might want to launch <code>PythonSlicer</code> so that you are sure to have the same python and pyradiomics installation as you have in the Slicer application.  (SlicerRadiomics extension is the GUI wrapper that bundles pyradiomics into Slicer).</p>

---

## Post #9 by @matt-warkentin (2019-08-27 20:08 UTC)

<p>I must be doing something wrong but I was able to successfully extract features using</p>
<pre><code class="lang-auto">Slicer --no-main-window --python-script pyradiomics image.nrrd mask.nrrd
</code></pre>
<p>and</p>
<pre><code class="lang-auto">python pyradiomics image.nrrd mask.nrrd
</code></pre>
<p>Which uses the python interpreter found in my <code>$PATH</code> (<code>/anaconda3/bin/python</code>), but not when I do:</p>
<pre><code class="lang-auto">PythonSlicer pyradiomics image.nrrd mask.nrrd
</code></pre>
<blockquote>
<p>Traceback (most recent call last):<br>
File “pyradiomics”, line 7, in <br>
from radiomics.scripts.<strong>init</strong> import parse_args<br>
ImportError: No module named radiomics.scripts.<strong>init</strong></p>
</blockquote>

---

## Post #10 by @pieper (2019-08-27 20:22 UTC)

<p>Right, that makes sense.  You need to run it like: <code>./Slicer --launch PythonSlicer</code> so it has the right environment (paths to the python libraries).</p>
<p>The first form you tried uses the <code>Slicer</code> application as the interpreter, which is why you need the extra options to turn off the main window and run the script - this uses the same basic python environment, but with the extra overhead of the GUI app.  The second form uses your anaconda install, which might work too but also might have different packages or versions than the Slicer python.</p>

---

## Post #11 by @matt-warkentin (2019-08-27 20:45 UTC)

<p>Thank you for your patience. I don’t think I am clear on what exactly <code>Slicer --launch PythonSlicer</code> is really doing. When I run that code, a <code>Slicer</code> GUI is opened and nothing else appears to happen; so I don’t see the clear difference between using <code>Slicer --python-script</code> and <code>Slicer --launch SlicerPython</code>.</p>

---

## Post #12 by @lassoan (2019-08-27 20:57 UTC)

<aside class="quote no-group" data-username="pieper" data-post="10" data-topic="8162">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Right, that makes sense. You need to run it like: <code>./Slicer --launch PythonSlicer</code></p>
</blockquote>
</aside>
<p>PythonSlicer inherits all the settings from the Slicer launcher, so it should not be necessary to run it using <code>. /Slicer</code>. Have you experienced issues running when simply running <code>PythonSlicer</code>?</p>

---

## Post #13 by @pieper (2019-08-27 21:17 UTC)

<p>Yes, I did test that.  Running <code>PythonSlicer</code> without the launcher I cannot <code>import radiomics</code> but with the launcher I can (on linux nightly from 2019-08-22).</p>

---

## Post #14 by @matt-warkentin (2019-08-27 22:13 UTC)

<p>I anticipated when running <code>Slicer --launch PythonSlicer</code> that it would just open a python interpreter in the shell; but it seems to also open the Slicer GUI. Is this the expected behaviour?</p>
<p>Because calling <code>PythonSlicer</code> alone of course just opens a python interpreter.</p>

---

## Post #15 by @pieper (2019-08-28 00:12 UTC)

<p>Ah, are you on mac?  The launcher is part of the mac build tree but not the official entrypoint for the app in the binaries now that I think about it.  On linux Slicer --launch PythonSlicer does just bring up the interpreter.</p>

---

## Post #16 by @matt-warkentin (2019-08-28 01:17 UTC)

<p>Yes, sorry. I should’ve provided that context. I am currently running <code>Slicer 4.10.1</code> on a Macbook Pro running <code>Mojave 10.14.4</code>.</p>

---

## Post #17 by @lassoan (2019-08-28 14:48 UTC)

<p>Could you please try the latest stable (4.10.2) and latest preview versions, too?</p>

---

## Post #18 by @pieper (2019-08-28 18:39 UTC)

<aside class="quote no-group" data-username="matt-warkentin" data-post="16" data-topic="8162" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matt-warkentin/48/4962_2.png" class="avatar"> matt-warkentin:</div>
<blockquote>
<p>Yes, sorry. I should’ve provided that context. I am currently running <code>Slicer 4.10.1</code> on a Macbook Pro running <code>Mojave 10.14.4</code> .</p>
</blockquote>
</aside>
<p>Yes, for that case maybe you need to stick with the <code>--no-main-window --python-script</code> approach - it’s a bit more overhead but maybe it doesn’t matter.</p>

---

## Post #19 by @matt-warkentin (2019-08-28 18:56 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Yes, I can try these more recent versions. I won’t have the chance to test them for maybe two weeks as I am travelling for work. But I promise to test things out when I get back home and I will report back.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> Good to know. Thank you very much for your help.</p>
<p>One last question – I am under the impression that some Slicer functionality/modules rely on using <code>plastimatch</code>. Does this mean the <code>plastimatch</code> binary is buried somewhere inside the Slicer file tree? I’m wondering if by installing Slicer, one now has the <code>plastimatch</code> binary behind-the-scenes which can be exposed at the command-line.</p>

---

## Post #20 by @pieper (2019-08-28 19:24 UTC)

<aside class="quote no-group" data-username="matt-warkentin" data-post="19" data-topic="8162">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matt-warkentin/48/4962_2.png" class="avatar"> matt-warkentin:</div>
<blockquote>
<p>Slicer functionality/modules rely on using <code>plastimatch</code> . Does this mean the <code>plastimatch</code> binary is buried somewhere inside the Slicer file tree?</p>
</blockquote>
</aside>
<p>I believe you get most if not all <code>plastimatch</code> features via <a href="http://slicerrt.github.io/">SlicerRT</a>.  (I’m sure someone will correct me if I’m wrong on that!).</p>

---

## Post #21 by @lassoan (2019-08-28 21:34 UTC)

<p>Plastimatch contains a wide variety of features. We only enable building of the core radiation therapy features.</p>
<aside class="quote no-group" data-username="matt-warkentin" data-post="19" data-topic="8162">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matt-warkentin/48/4962_2.png" class="avatar"> matt-warkentin:</div>
<blockquote>
<p>Does this mean the <code>plastimatch</code> binary is buried somewhere inside the Slicer file tree?</p>
</blockquote>
</aside>
<p>It is not buried at all but nicely linked into Slicer modules and a few command-line applications (as far as I remember, statically). You can run command-line applications using Slicer launcher, without starting the Slicer application GUI.</p>

---

## Post #22 by @matt-warkentin (2019-08-28 21:49 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I didn’t mean to be snide with my “buried” comment; I just meant located somewhere in the internal file structure.</p>
<p>Based on the previous discussion with <a class="mention" href="/u/pieper">@pieper</a>, I was under the impression that since I am running on Mac OS, that the Slicer launcher wouldn’t work as anticipated? Or is this meant to be resolved when I upgrade to a more recent build?</p>

---

## Post #23 by @pieper (2019-08-28 23:06 UTC)

<aside class="quote no-group" data-username="matt-warkentin" data-post="22" data-topic="8162">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/matt-warkentin/48/4962_2.png" class="avatar"> matt-warkentin:</div>
<blockquote>
<p>Based on the previous discussion with <a class="mention" href="/u/pieper">@pieper</a>, I was under the impression that since I am running on Mac OS, that the Slicer launcher wouldn’t work as anticipated? Or is this meant to be resolved when I upgrade to a more recent build?</p>
</blockquote>
</aside>
<p>No, this wouldn’t have changed - for mac we don’t use the installer because there are constraints about how apps need to be structured (e.g. to allow for signing the binaries).  The open question is how environments are shared between <code>Slicer</code> and <code>PythonSlicer</code> - maybe there’s a fix such that <code>PythonSlicer</code> can import the same packages without needing the launcher.</p>

---

## Post #24 by @matt-warkentin (2019-08-28 23:48 UTC)

<p>These installation technicalities are definitely not something I have any real knowledge of. But yes, I agree that your proposed fix would indeed be nice, if possible.</p>

---

## Post #25 by @lassoan (2019-08-29 00:01 UTC)

<aside class="quote no-group" data-username="pieper" data-post="23" data-topic="8162">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>maybe there’s a fix such that <code>PythonSlicer</code> can import the same packages without needing the launcher.</p>
</blockquote>
</aside>
<p>PythonSlicer inherits settings from the ini file of Slicer, starting from 4.10.2 or so. <a class="mention" href="/u/jcfr">@jcfr</a> why do you think there could be a difference between Slicer and PythonSlicer on Mac?</p>

---

## Post #26 by @jcfr (2019-08-29 12:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="25" data-topic="8162">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/jcfr">@jcfr</a> why do you think there could be a difference between Slicer and PythonSlicer on Mac?</p>
</blockquote>
</aside>
<p>On MacOS, Slicer.app (or the executable found in Slicer.app/Contents/MacOS) is not a launcher but the actual executable. That said, env. variables are read from a launcher settings file (to be consistent across platform).</p>
<p>PythonSlicer on all platform (including macOS) are inheriting settings from <code>SlicerLauncherSettings.ini</code></p>
<p>What make you think it is not the case ? What would be a small example to reproduce the problem ?</p>

---

## Post #27 by @lassoan (2019-08-29 13:27 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="26" data-topic="8162">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>What make you think it is not the case ? What would be a small example to reproduce the problem ?</p>
</blockquote>
</aside>
<p>The problem/inconsistency is this:</p>
<aside class="quote no-group" data-username="pieper" data-post="13" data-topic="8162">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Running <code>PythonSlicer</code> without the launcher I cannot <code>import radiomics</code> but with the launcher I can (on linux nightly from 2019-08-22).</p>
</blockquote>
</aside>

---

## Post #28 by @pieper (2019-08-29 19:58 UTC)

<p>The reason is that <code>PythonSlicer</code> doesn’t add the python site-packages paths from the installed extensions so they can’t be imported.</p>

---

## Post #29 by @kayarre (2020-08-14 03:17 UTC)

<p>Using an old version of Slicer I was able to use the following command with KDE</p>
<pre><code class="lang-auto">$ ./Slicer --launch konsole &amp;
</code></pre>
<p>on nightly release<br>
I am now using linux mint with gnom and this doesn’t appear to work anymore using something like</p>
<pre><code class="lang-auto">$ ./Slicer --launch gnome-terminal
</code></pre>
<p>did this feature go away or what am I doing wrong, or is it related to nightly?</p>

---

## Post #30 by @lassoan (2020-08-14 03:48 UTC)

<p>Everything should still work the same way.</p>
<aside class="quote no-group" data-username="kayarre" data-post="29" data-topic="8162">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p>and this doesn’t appear to work anymore</p>
</blockquote>
</aside>
<p>What do you mean by doesn’t appear to work? What happens? Do you see any error message?</p>
<p>Can you launch other executables?<br>
Do other options work (you can get a list by calling --help)?</p>
<p>If you install an earlier Slicer Preview Release then does it work better? (you can download them by <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Where_can_I_download_Slicer.3F">specifying additional arguments on the download page</a>).</p>

---

## Post #31 by @kayarre (2020-08-14 03:54 UTC)

<p>ok good, needed to make sure I eliminated any issues between chair and keyboard.<br>
here are a couple of the attempts. I haven’t tried with konsole as I don’t have a kde environment close by.</p>
<pre><code class="lang-auto">~/tools/Slicer-4.11.0-2020-08-12-linux-amd64/Slicer --launch gnome-terminal
Failed to import the site module
Traceback (most recent call last):
  File "/home/sansomk/tools/Slicer-4.11.0-2020-08-12-linux-amd64/bin/../lib/Python/lib/python3.6/site.py", line 553, in &lt;module&gt;
    main()
  File "/home/sansomk/tools/Slicer-4.11.0-2020-08-12-linux-amd64/bin/../lib/Python/lib/python3.6/site.py", line 539, in main
    known_paths = addusersitepackages(known_paths)
  File "/home/sansomk/tools/Slicer-4.11.0-2020-08-12-linux-amd64/bin/../lib/Python/lib/python3.6/site.py", line 282, in addusersitepackages
    user_site = getusersitepackages()
  File "/home/sansomk/tools/Slicer-4.11.0-2020-08-12-linux-amd64/bin/../lib/Python/lib/python3.6/site.py", line 258, in getusersitepackages
    user_base = getuserbase() # this will also set USER_BASE
  File "/home/sansomk/tools/Slicer-4.11.0-2020-08-12-linux-amd64/bin/../lib/Python/lib/python3.6/site.py", line 248, in getuserbase
    USER_BASE = get_config_var('userbase')
  File "/home/sansomk/tools/Slicer-4.11.0-2020-08-12-linux-amd64/lib/Python/lib/python3.6/sysconfig.py", line 601, in get_config_var
    return get_config_vars().get(name)
  File "/home/sansomk/tools/Slicer-4.11.0-2020-08-12-linux-amd64/lib/Python/lib/python3.6/sysconfig.py", line 550, in get_config_vars
    _init_posix(_CONFIG_VARS)
  File "/home/sansomk/tools/Slicer-4.11.0-2020-08-12-linux-amd64/lib/Python/lib/python3.6/sysconfig.py", line 421, in _init_posix
    _temp = __import__(name, globals(), locals(), ['build_time_vars'], 0)
ModuleNotFoundError: No module named '_sysconfigdata_m_linux_x86_64-linux-gnu
</code></pre>
<pre><code class="lang-auto">~/tools/Slicer-4.11.0-2020-08-12-linux-amd64/Slicer --launch terminator
  File "/home/sansomk/tools/Slicer-4.11.0-2020-08-12-linux-amd64/bin/../lib/Python/lib/python3.6/site.py", line 177
    file=sys.stderr)
        ^
SyntaxError: invalid syntax

</code></pre>

---

## Post #32 by @lassoan (2020-08-14 04:04 UTC)

<p>Try specifying <code>PYTHONNOUSERSITE=1</code> environment variable. If it does not help then check out discussion in <a href="https://discourse.slicer.org/t/cant-start-slicer-on-linux-on-one-machine/8175/21">this topic</a>, maybe it helps.</p>

---
