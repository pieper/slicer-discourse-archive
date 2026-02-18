# Linux build instructions lead to using Qt 5.9.5 on Ubuntu 18.04

**Topic ID**: 13188
**Date**: 2020-08-27
**URL**: https://discourse.slicer.org/t/linux-build-instructions-lead-to-using-qt-5-9-5-on-ubuntu-18-04/13188

---

## Post #1 by @cpinter (2020-08-27 09:38 UTC)

<p>I followed the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#pre-requisites">build instructions for Linux</a>, and the prerequisites install command for Ubuntu apparently downloaded Qt 5.9.5, at least this is what the CMake configure output said.</p>
<p>The Ubuntu version mentioned in the instructions is 20.04, and what I use is the older 18.04.<br>
Is the old Qt version due to the older Ubuntu version? Is it verified that the instructions on 20.04 by default download 5.15.0?</p>
<p>Anyway I started installing Qt with the online installer. What I’d like to know is first if the instructions are correct for 20.04, and if yes, if there is a similarly easy way for 18.04?</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2020-10-04 13:00 UTC)

<p>I can confirm that the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#ubuntu-20-04-focal-fossa">20.04 instructions</a> on the docs work.</p>

---

## Post #3 by @Saima (2021-04-14 05:50 UTC)

<p>I got the errors below the build debug slicer failed. I followed instructions on <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html#ubuntu-20-04-focal-fossa" class="inline-onebox" rel="noopener nofollow ugc">GNU/Linux Systems — 3D Slicer documentation</a></p>
<p>fstd/libsrc/CMakeFiles/ofstd.dir/build.make:62: recipe for target ‘ofstd/libsrc/CMakeFiles/ofstd.dir/ofchrenc.cc.o’ failed<br>
make[5]: *** [ofstd/libsrc/CMakeFiles/ofstd.dir/ofchrenc.cc.o] Error 1<br>
CMakeFiles/Makefile2:2304: recipe for target ‘ofstd/libsrc/CMakeFiles/ofstd.dir/all’ failed<br>
make[4]: *** [ofstd/libsrc/CMakeFiles/ofstd.dir/all] Error 2<br>
Makefile:140: recipe for target ‘all’ failed<br>
make[3]: *** [all] Error 2<br>
CMakeFiles/DCMTK.dir/build.make:113: recipe for target ‘DCMTK-prefix/src/DCMTK-stamp/DCMTK-build’ failed<br>
make[2]: *** [DCMTK-prefix/src/DCMTK-stamp/DCMTK-build] Error 2<br>
CMakeFiles/Makefile2:699: recipe for target ‘CMakeFiles/DCMTK.dir/all’ failed<br>
make[1]: *** [CMakeFiles/DCMTK.dir/all] Error 2<br>
Makefile:94: recipe for target ‘all’ failed<br>
make: *** [all] Error 2</p>
<p>can anyone help me fix the build on ubuntu 18.04.</p>

---

## Post #4 by @lassoan (2021-04-18 05:07 UTC)

<p>We don’t use Ubuntu 18.04 anymore, so we cannot provide specific build instructions, but if you figure out how to do it then please let us know and we will add it to the documentation.</p>
<p>About the specific error: you haven’t included the actual error message (just the status report that the build failed), so we don’t know what could have caused it. If you upload the complete build log somewhere and post the link here then we might be able to give advice.</p>

---
