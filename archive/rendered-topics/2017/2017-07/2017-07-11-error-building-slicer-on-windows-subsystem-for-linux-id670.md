# Error Building Slicer on Windows Subsystem for Linux

**Topic ID**: 670
**Date**: 2017-07-11
**URL**: https://discourse.slicer.org/t/error-building-slicer-on-windows-subsystem-for-linux/670

---

## Post #1 by @edwardwang1 (2017-07-11 20:12 UTC)

<p>Hi all,</p>
<p>I am trying to build Slicer via the Windows Subsystem for Linux with Anaconda instead of default Python. Following the steps of the Slicer Wiki, I am able to get past the Cmake step. However, I run into an error during make, and I believe it is due do the following:</p>
<p>/mnt/g/SlicerCustom/Slicer/Slicer-Superbuild/PCRE-prefix/src/PCRE/missing: line 81: aclocal-1.15: command not found<br>
WARNING: ‘aclocal-1.15’ is missing on your system.<br>
You should only need it if you modified ‘acinclude.m4’ or<br>
’<a href="http://configure.ac" rel="nofollow noopener">configure.ac</a>’ or m4 files included by ‘<a href="http://configure.ac" rel="nofollow noopener">configure.ac</a>’.<br>
The ‘aclocal’ program is part of the GNU Automake package:<br>
<a href="http://www.gnu.org/software/automake" rel="nofollow noopener">http://www.gnu.org/software/automake</a><br>
It also requires GNU Autoconf, GNU m4 and Perl in order to run:<br>
<a href="http://www.gnu.org/software/autoconf" rel="nofollow noopener">http://www.gnu.org/software/autoconf</a><br>
<a href="http://www.gnu.org/software/m4/" rel="nofollow noopener">http://www.gnu.org/software/m4/</a><br>
<a href="http://www.perl.org/" rel="nofollow noopener">http://www.perl.org/</a><br>
– Looking for mknod<br>
make[3]: *** [/mnt/g/SlicerCustom/Slicer/Slicer-Superbuild/PCRE-prefix/src/PCRE/aclocal.m4] Error 127<br>
make[2]: *** [PCRE-prefix/src/PCRE-stamp/PCRE-build] Error 2<br>
make[1]: *** [CMakeFiles/PCRE.dir/all] Error 2</p>
<p>Any thoughts on solving this issue?<br>
Thanks,<br>
Edward</p>

---

## Post #2 by @lassoan (2017-07-11 20:19 UTC)

<p>It is an interesting experiment to see if WSL is complete enough so that you can build a complex project like Slicer, but as far as I know, applications with graphical user interface are not officially supported by WSL.</p>
<p>On Windows, it makes the most sense to build using native tools. VS2013 Community Edition is free.</p>
<p>If you prefer working in a Linux environment on Windows then you can use Docker or a virtual machine (VirtualBox, Hyper-V).</p>

---

## Post #3 by @jcfr (2017-07-11 21:22 UTC)

<p>It may also be worth exploring building using the dockcross-windows-x64 docker image bundling <code>MXE/MinGW-w64</code> toolchain.</p>
<p>See <a href="https://github.com/dockcross/dockcross">https://github.com/dockcross/dockcross</a></p>

---
