---
topic_id: 1568
title: "Tcl Related Build Error On Mac"
date: 2017-11-30
url: https://discourse.slicer.org/t/1568
---

# Tcl related build error on Mac

**Topic ID**: 1568
**Date**: 2017-11-30
**URL**: https://discourse.slicer.org/t/tcl-related-build-error-on-mac/1568

---

## Post #1 by @cpinter (2017-11-30 20:20 UTC)

<p>I did a clean build on Mac High Sierra on the latest master and got this build error.</p>
<pre><code>-- tcl: Errors detected - See below.

In file included from /Users/cpinter/Devel/S4R/tcl/tcl/generic/regcomp.c:33:
In file included from /Users/cpinter/Devel/S4R/tcl/tcl/generic/regguts.h:36:
In file included from /Users/cpinter/Devel/S4R/tcl/tcl/generic/regcustom.h:33:
In file included from /Users/cpinter/Devel/S4R/tcl/tcl/generic/regex.h:4:
In file included from /Users/cpinter/Devel/S4R/tcl/tcl/generic/tclInt.h:36:
In file included from /Users/cpinter/Devel/S4R/tcl/tcl/generic/tclPort.h:23:
./tclUnixPort.h:32:10: fatal error: 'errno.h' file not found
#include &lt;errno.h&gt;
         ^~~~~~~~~
1 error generated.
make[3]: *** [regcomp.o] Error 1

CMake Error at /Users/cpinter/Devel/Slicer4/CMake/ExternalProjectForNonCMakeProject.cmake:76 (message):
  tcl: Error in build step.  See
  /Users/cpinter/Devel/S4R/tcl_build_step_output.txt and
  /Users/cpinter/Devel/S4R/tcl_build_step_error.txt
Call Stack (most recent call first):
  /Users/cpinter/Devel/S4R/tcl_build_step.cmake:3 (ExternalProject_Execute)
</code></pre>
<p>Has anyone seen the same? Do I do anything wrong? Here’s how I configure (has not changed in the past two years other than deployment target):</p>
<pre><code>/Applications/CMake.app/Contents/bin/cmake -DCMAKE_BUILD_TYPE:STRING=Release -DQT_QMAKE_EXECUTABLE:FILEPATH=/usr/local/Cellar/qt/4.8.7_3/bin/qmake -DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.13 ../Slicer4</code></pre>

---

## Post #2 by @hherhold (2017-11-30 20:35 UTC)

<p>Did you update Xcode and the command line tools along with High Sierra? errno.h is in /usr/include and is a standard UNIX include file, seems like maybe basic build environment is missing/misconfigured.</p>

---

## Post #3 by @cpinter (2017-11-30 21:34 UTC)

<p>Thanks for the tip! When I started XCode it did install some components. Unfortunately the error didn’t go away even after a clean build.</p>

---

## Post #4 by @hherhold (2017-11-30 21:50 UTC)

<p>Hmm. Do you see errno.h in /usr/include? Also, run the App Store and look under Updates, and see if there’s an entry for Command Line Tools. This is supposed to be updated when you update Xcode, but I’ve seen weird things where I had to update command line tools AND Xcode separately.</p>
<p>Did you do a complete blow-away-the-entire-build-directory and re-run CMake from scratch?</p>

---

## Post #5 by @cpinter (2017-12-04 15:46 UTC)

<p>Thanks for the suggestions, Hollister! I was just able to check these out. There is no usr/include directory at all, so no errno.h either. Yes I did a clean build from scratch. I haven’t found the command line tools in the app store yet, but I keep looking. Do you know what it’s called exactly? Thanks!</p>

---

## Post #6 by @cpinter (2017-12-04 16:30 UTC)

<p>I just realized that the command-line tools can be installed from the command line <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"> The build is going well so far…</p>

---
