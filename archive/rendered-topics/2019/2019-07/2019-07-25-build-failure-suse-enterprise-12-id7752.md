# Build Failure Suse Enterprise 12

**Topic ID**: 7752
**Date**: 2019-07-25
**URL**: https://discourse.slicer.org/t/build-failure-suse-enterprise-12/7752

---

## Post #1 by @sbouix (2019-07-25 12:37 UTC)

<p>Hi, I am trying to compile v4.10.2 on a linux cluster managed by LRZ (<a href="http://lrz.de" rel="nofollow noopener">lrz.de</a>) and compilation fails at this stage:<br>
[ 36%] Linking CXX executable …/…/…/…/bin/qMRMLWidgetsCxxTests<br>
/usr/lib64/gcc/x86_64-suse-linux/4.8/…/…/…/…/x86_64-suse-linux/bin/ld: /home/hpc/pn72sa/ru48vil/software/Qt/5.11.2/gcc_64/lib/libQt5WebEngineCore.so.5.11.2: undefined reference to `dbus_message_get_type@LIBDBUS_1_3’</p>
<p>Any ideas?</p>

---

## Post #2 by @pieper (2019-07-25 13:04 UTC)

<p>Maybe turn off testing (cmake option) and see if you can build the actual application.</p>
<p>Or the singularity option might work.</p>

---

## Post #3 by @sbouix (2019-07-25 13:20 UTC)

<p>I am building without the testing option.<br>
What’s the singularity option?<br>
I shoudl add that I also downloaded the binary, but get some error message when loading a volume about pthreads. Looks like a vtk issue.</p>

---

## Post #4 by @pieper (2019-07-25 13:56 UTC)

<p>I haven’t used it myself, but apparently Singularity helps get around some of these cross-linux dependency issues.  <a href="https://discourse.slicer.org/t/error-when-run-3dslicer-in-singularity-container/7599">It’s apparently able to be used with Slicer</a>.  Probably still requires some help from the cluster sysadmins if you want to install it.</p>
<p>But getting back to the build error, I’m not sure why qMRMLWidgetsCxxTests would be built if testing is turned off.  In any case the Slicer app code should not depend on it, so maybe you can do <code>make -k</code> to build everything and just ignore the failing build of the test (or maybe you’ll get a similar link error on the app level - this looks like a qt issue - you might also try turning off <code>Slicer_BUILD_WEBENGINE_SUPPORT</code>).</p>

---

## Post #5 by @sbouix (2019-07-25 14:03 UTC)

<p>OK, I’ll try a couple of the ideas of turning off some options in CMAKE and see what happens.</p>

---
