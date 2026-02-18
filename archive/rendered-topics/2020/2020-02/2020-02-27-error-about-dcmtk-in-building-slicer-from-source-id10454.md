# Error about DCMTK in Building Slicer from source

**Topic ID**: 10454
**Date**: 2020-02-27
**URL**: https://discourse.slicer.org/t/error-about-dcmtk-in-building-slicer-from-source/10454

---

## Post #1 by @Akash23 (2020-02-27 04:33 UTC)

<p>Dear all,<br>
Could you help me solve my problem as follows please?<br>
Operating system: Ubuntu 18 (subsystem of windows 10)<br>
Slicer version: pulled most recent commit<br>
gcc/g++ version: 7.4<br>
Qt version: 5.14<br>
cmake version: 3.13<br>
I ran the cmake command as:</p>
<pre><code class="lang-auto">cmake -DCMAKE_BUILD_TYPE:STRING=Debug  -DQt5_DIR:PATH=/home/me/Qt5.14.0/5.14.0/gcc_64/lib/cmake/Qt5  -DSlicer_USE_SYSTEM_QT:BOOL=1 ../Slicer 
</code></pre>
<p>Actual behavior:</p>
<pre><code class="lang-auto">error: ‘DCMTK_CHAR_MODULO’ was not declared in this scope
     static const OFBool is_modulo                   = DCMTK_CHAR_MODULO;
                                                       ^~~~~~~~~~~~~~~~~
/home/me/MyProjects/Slicer-SuperBuild-Debug/DCMTK/ofstd/include/dcmtk/ofstd/oflimits.h:1044:55: note: suggested alternative: ‘DCMTK_SHARED’
     static const OFBool is_modulo                   = DCMTK_CHAR_MODULO;
                                                       ^~~~~~~~~~~~~~~~~
                                                       DCMTK_SHARED
/home/me/MyProjects/Slicer-SuperBuild-Debug/DCMTK/ofstd/include/dcmtk/ofstd/oflimits.h:1057:55: error: ‘DCMTK_CHAR_TRAPS’ was not declared in this scope
     static const OFBool traps                       = DCMTK_CHAR_TRAPS;
                                                       ^~~~~~~~~~~~~~~~
/home/me/MyProjects/Slicer-SuperBuild-Debug/DCMTK/ofstd/include/dcmtk/ofstd/oflimits.h:1057:55: note: suggested alternative: ‘DCMTK_SHARED’
     static const OFBool traps                       = DCMTK_CHAR_TRAPS;
                                                       ^~~~~~~~~~~~~~~~
                                                       DCMTK_SHARED
/home/me/MyProjects/Slicer-SuperBuild-Debug/DCMTK/ofstd/include/dcmtk/ofstd/oflimits.h:1085:55: error: ‘DCMTK_SIGNED_CHAR_MODULO’ was not declared in this scope
     static const OFBool is_modulo                   = DCMTK_SIGNED_CHAR_MODULO;
                                                       ^~~~~~~~~~~~~~~~~~~~~~~~
/home/me/MyProjects/Slicer-SuperBuild-Debug/DCMTK/ofstd/include/dcmtk/ofstd/oflimits.h:1085:55: note: suggested alternative: ‘DCMTK_SIGNED_CHAR_DIGITS10’
     static const OFBool is_modulo                   = DCMTK_SIGNED_CHAR_MODULO;
                                                       ^~~~~~~~~~~~~~~~~~~~~~~~
                                                       DCMTK_SIGNED_CHAR_DIGITS10
/home/me/MyProjects/Slicer-SuperBuild-Debug/DCMTK/ofstd/include/dcmtk/ofstd/oflimits.h:1094:55: error: ‘DCMTK_SIGNED_CHAR_TRAPS’ was not declared in this scope
     static const OFBool traps                       = DCMTK_SIGNED_CHAR_TRAPS;
                                                       ^~~~~~~~~~~~~~~~~~~~~~~
/home/me/MyProjects/Slicer-SuperBuild-Debug/DCMTK/ofstd/include/dcmtk/ofstd/oflimits.h:1094:55: note: suggested alternative: ‘DCMTK_SIGNED_CHAR_DIGITS10’
     static const OFBool traps
</code></pre>

---

## Post #2 by @fedorov (2020-02-27 04:40 UTC)

<p>I doubt this is the reason, but note that the minimum required version of cmake is 3.13.4, and your log reports 3.13. This should be easy to fix.</p>
<p>Also, can you check if DCMTK is not installed in some other system-wide location on your system? This can cause problems sometime, due to use of conflicting header (this issue may be relevant: <a href="https://github.com/QIICR/dcmqi/issues/395">https://github.com/QIICR/dcmqi/issues/395</a>).</p>

---
