---
topic_id: 12101
title: "Build Issue With Slicer 4 10 2 On Centos8"
date: 2020-06-18
url: https://discourse.slicer.org/t/12101
---

# Build Issue with Slicer-4.10.2 on centOS8

**Topic ID**: 12101
**Date**: 2020-06-18
**URL**: https://discourse.slicer.org/t/build-issue-with-slicer-4-10-2-on-centos8/12101

---

## Post #1 by @DavidCai1246 (2020-06-18 19:39 UTC)

<p>Operating system: centOS8<br>
Slicer version: 4.10.2</p>
<p>I’m following the instructions on <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#BUILD_Slicer" rel="nofollow noopener">nightly build</a>.</p>
<p>However when I start building the slicer, I get the following error:<br>
[ 10%] No install step for ‘DCMTK’<br>
[ 10%] Completed ‘DCMTK’<br>
[ 10%] Built target DCMTK<br>
make: *** [Makefile:95: all] Error 2</p>
<p>If I run make without the -j option I get:</p>
<p>Creating ‘bin/./Modules/Setup.local’<br>
…/…/lib/libpython2.7.so: undefined reference to `minor’</p>
<p>…/…/lib/libpython2.7.so: undefined reference to `major’</p>
<p>…/…/lib/libpython2.7.so: undefined reference to `makedev’<br>
collect2: error: ld returned 1 exit status<br>
make[5]: *** [CMakeBuild/python/CMakeFiles/python.dir/build.make:92: bin/python] Error 1<br>
make[4]: *** [CMakeFiles/Makefile2:3596: CMakeBuild/python/CMakeFiles/python.dir/all] Error 2<br>
make[3]: *** [Makefile:141: all] Error 2<br>
make[2]: *** [CMakeFiles/python.dir/build.make:118: python-prefix/src/python-stamp/python-build] Error 2<br>
make[1]: *** [CMakeFiles/Makefile2:1032: CMakeFiles/python.dir/all] Error 2<br>
make: *** [Makefile:95: all] Error 2</p>
<p>Thank you in advance for any help or suggestions!</p>

---

## Post #2 by @lassoan (2020-06-18 20:17 UTC)

<p>I would not recommend to develop anything for Slicer-4.10, as we will soon release Slicer-5 and then Slicer-4.10 will not be used anymore. Slicer-5 will be based on latest Slicer-4.11, it uses Python3, and contains lots of important new features and improvements.</p>

---

## Post #4 by @DavidCai1246 (2020-06-18 21:01 UTC)

<p>I would still like th have slicer 4.10.2 built on my system because it is the most recent stable release</p>

---

## Post #5 by @muratmaga (2020-06-19 04:34 UTC)

<p>The term ‘stable’ doesn’t mean that preview version is unstable. In fact, when Slicer 5.0 ‘stable’ is released in the next few months, it will be based on the current 4.11 preview as <a class="mention" href="/u/lassoan">@lassoan</a> indicated above, at which time 4.10.2 will be considered ‘unsupported’.</p>
<p>If you are just starting with Slicer, you will be investing a lot time learning things that won’t apply to the new upcoming stable version.</p>

---

## Post #6 by @DavidCai1246 (2020-06-20 03:47 UTC)

<p>I see, thank you very much!</p>

---

## Post #7 by @DavidCai1246 (2020-06-20 03:47 UTC)

<p>Thats a good point and I agree, thank you very much!</p>

---
