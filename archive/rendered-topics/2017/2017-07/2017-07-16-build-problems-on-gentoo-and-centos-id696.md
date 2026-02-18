# Build problems on Gentoo and CentOS

**Topic ID**: 696
**Date**: 2017-07-16
**URL**: https://discourse.slicer.org/t/build-problems-on-gentoo-and-centos/696

---

## Post #1 by @vnpavanelli (2017-07-16 12:09 UTC)

<p>I’m having some problems building 3D Slicer on Gentoo, I’m using GCC 7 and GCC 6, could not try on GCC 4 since it got some libraries problems with the ABI changes.</p>
<p>Can someone orient me about what GCC version and maybe Linux distro is best to build? I would like to use Gentoo, but if another works its a start for me.</p>
<p>I’ve tried also CentOS 7 with no luck, maybe I’m missing something. Been following the instructions on <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions</a></p>
<p>The errors on Gentoo I’m stuck now are all like this:<br>
Slicer-SuperBuild-Debug/SimpleITK/Code/Common/include/Ancillary/TypeList.h:328:43: error: expected primary-expression before ‘&gt;’ token<br>
visitor.CLANG_TEMPLATE operator()( );</p>
<p>And on CentOS I got:<br>
[  1%] Completed ‘BRAINSTools’<br>
[  1%] Built target BRAINSTools<br>
make[2]: *** No rule to make target <code>zlib-prefix/src/zlib-stamp/zlib-/root/src/Slicer-SuperBuild-Debug/version-zlib.txt', needed by</code>zlib-prefix/src/zlib-stamp/zlib-generate_project_description’.  Stop.<br>
make[1]: *** [CMakeFiles/zlib.dir/all] Error 2</p>
<p>Thanks in advance!</p>

---

## Post #2 by @pieper (2017-07-16 19:19 UTC)

<p>I’ve never used Gentoo, but things usually build fine on ubuntu.</p>
<p>You might try building ITK outside of Slicer and see if you can  figure out the error that way.</p>
<p>Best,<br>
Steve</p>

---

## Post #3 by @fedorov (2017-07-17 02:30 UTC)

<p>It may have to do with your compiler applying C++11 by default.</p>
<p>Can you let us know what is the output of <code>gcc -v</code>?</p>

---

## Post #4 by @fedorov (2017-07-17 02:34 UTC)

<p>Sorry I didn’t read carefully your initial post that you use GCC 7 and 6.</p>
<p>As you can see from <a href="https://gcc.gnu.org/gcc-6/changes.html">https://gcc.gnu.org/gcc-6/changes.html</a>, GCC 6 default mode is C++14. As far as I know, you cannot compile Slicer with C++14, and I am not sure if/how you could configure your build to properly propagate flags to enforce C++98 throughout the superbuild.</p>
<p>This discussion <em>may</em> be helpful: <a href="https://github.com/QIICR/dcmqi/issues/235">https://github.com/QIICR/dcmqi/issues/235</a>.</p>

---

## Post #5 by @vnpavanelli (2017-07-17 06:38 UTC)

<p>Thank you very much <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/fedorov">@fedorov</a> !<br>
I’m trying right now on Ubuntu 16.04 that have the GCC 5, it seems to be working.</p>
<p>That discussion is very helpful, will try later to make it works with the GCC 6/7, maybe I can contribute a little with the project.</p>

---
