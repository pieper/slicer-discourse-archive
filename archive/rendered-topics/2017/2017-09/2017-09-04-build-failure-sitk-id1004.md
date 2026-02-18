# Build failure SITK

**Topic ID**: 1004
**Date**: 2017-09-04
**URL**: https://discourse.slicer.org/t/build-failure-sitk/1004

---

## Post #1 by @gcsharp (2017-09-04 22:11 UTC)

<p>Hi,</p>
<p>I get the following error from a fresh build from source.  Linux, gcc 7.2, QT5.  Any idea?</p>
<p>Greg</p>
<pre><code>[ 61%] Building CXX object Code/Common/src/CMakeFiles/SimpleITKCommon.dir/sitkImage.cxx.o
In file included from /home/gsharp/build/slicer-4/Slicer-build/SimpleITK/Code/Common/include/sitkPixelIDTypeLists.h:26:0,
                 from /home/gsharp/build/slicer-4/Slicer-build/SimpleITK/Code/Common/include/sitkMemberFunctionFactoryBase.h:26,
                 from /home/gsharp/build/slicer-4/Slicer-build/SimpleITK/Code/Common/include/sitkDetail.h:21,
                 from /home/gsharp/build/slicer-4/Slicer-build/SimpleITK/Code/Common/include/sitkImage.h:23,
                 from /home/gsharp/build/slicer-4/Slicer-build/SimpleITK/Code/Common/src/sitkImage.cxx:18:
/home/gsharp/build/slicer-4/Slicer-build/SimpleITK/Code/Common/include/Ancillary/TypeList.h: In member function ‘void typelist::Visit&lt;TTypeList&gt;::operator()(Predicate&amp;)’:
/home/gsharp/build/slicer-4/Slicer-build/SimpleITK/Code/Common/include/Ancillary/TypeList.h:328:43: error: expected primary-expression before ‘&gt;’ token
     visitor.CLANG_TEMPLATE operator()&lt;Head&gt;( );</code></pre>

---

## Post #2 by @jcfr (2017-09-05 01:10 UTC)

<p>Hi Greg,</p>
<p>For now, SimpleITK has to be disabled.</p>
<p>Jc</p>

---

## Post #3 by @jcfr (2017-09-05 05:03 UTC)

<p>Hi <a class="mention" href="/u/gcsharp">@gcsharp</a>,</p>
<p>This should be fixed in  <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26339">r26339</a>  and <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26340">r26340</a></p>
<p>Let us know how it goes,</p>
<p>Thanks<br>
Jc</p>

---
