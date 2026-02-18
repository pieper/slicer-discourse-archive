# .rodata can not be used when making a PIE object

**Topic ID**: 6313
**Date**: 2019-03-28
**URL**: https://discourse.slicer.org/t/rodata-can-not-be-used-when-making-a-pie-object/6313

---

## Post #1 by @Zhiy (2019-03-28 02:59 UTC)

<p>Hi,</p>
<p>I am building Slicer in ubuntu 18.04. I followed every step in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Linux" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Linux</a>. But now I run into a build error: /usr/bin/ld: CMakeFiles/vtkParseJava.dir/vtkParseJava.c.o: relocation R_X86_64_32 against  .rodata can not be used when making a PIE object; recompile with -fPIC.<br>
/usr/bin/ld: …/…/lib/libvtkWrappingTools-8.2.a(vtkParseMain.c.o): relocation R_X86_64_32 against `.rodata’ can not be used when making a PIE object; recompile with -fPIC<br>
…</p>
<p>My environment is:<br>
gcc/g++ 7.3, qt5.12, cmake 3.14, python 2.17.</p>
<p>My cmake command is<br>
cmake -DCMAKE_BUILD_TYPE:STRING=Debug -DQt5_DIR:PATH=/home/me/Qt/5.12.0/gcc_64/lib/cmake/Qt5 -DSlicer_USE_SYSTEM_QT:BOOL=1 -DQT_QMAKE_EXECUTABLE=/home/me/Qt/5.12.0/gcc_64/bin/qmake …/Slicer</p>
<p>Could anyone please help me out? I tried to add -fPIC in CMakeLists.txt as this post, <a href="https://stackoverflow.com/questions/19364969/compilation-fails-with-relocation-r-x86-64-32-against-rodata-str1-8-can-not" rel="nofollow noopener">https://stackoverflow.com/questions/19364969/compilation-fails-with-relocation-r-x86-64-32-against-rodata-str1-8-can-not</a>. But it still doesn’t work.</p>
<p>Thanks a lot.</p>

---

## Post #2 by @phcerdan (2019-03-28 03:37 UTC)

<p>Hi <a class="mention" href="/u/zhiy">@Zhiy</a>,</p>
<p>I would try first with a clean build directory.<br>
the errors show <code>libvtkWrappingTools-8.2.a</code>, which is a static library, when the default option in Slicer is to <code>BUILD_SHARED_LIBS:BOOL=ON</code> but that doesn’t correspond to the CMake options you posted.</p>
<p>Also, <code>QT_QMAKE_EXECUTABLE</code> is a Qt4 option, so you don’t need it.</p>
<p>Clean the build folder (the whole folder, not only the subfolder Slicer-build)<br>
And then try with:</p>
<pre><code class="lang-bash">cmake -DCMAKE_BUILD_TYPE:STRING=Debug \
-DQt5_DIR:PATH=/home/me/Qt/5.12.0/gcc_64/lib/cmake/Qt5 \
-DSlicer_USE_SYSTEM_QT:BOOL=1 \
../Slicer
</code></pre>
<p>This is just a first aid intuition. Let us know if you still hit the problem after that!</p>

---

## Post #3 by @Zhiy (2019-03-28 16:46 UTC)

<p>It solves my problem, except that I also followed the solution of makedev problem in this post: <a href="https://discourse.slicer.org/t/building-failure-on-ubuntu/3215/10" class="inline-onebox">Building failure on Ubuntu</a>. Thank you a lot.</p>

---
