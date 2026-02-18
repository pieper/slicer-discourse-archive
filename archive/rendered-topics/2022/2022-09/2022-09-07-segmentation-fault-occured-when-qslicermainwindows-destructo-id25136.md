# Segmentation fault occured when qSlicerMainWindow's destructor called

**Topic ID**: 25136
**Date**: 2022-09-07
**URL**: https://discourse.slicer.org/t/segmentation-fault-occured-when-qslicermainwindows-destructor-called/25136

---

## Post #1 by @nnzzll (2022-09-07 06:33 UTC)

<p>I’m developing a custom application of Slicer.<br>
When the program exits, a Segmentation fault occured during calling the destructor of <code>qSlicerMainWindow</code><br>
Here is the call traceback by gdb:</p>
<pre><code class="lang-auto">#0  0x00007fffedaa1f01 in std::__atomic_base&lt;int&gt;::load (
    __m=std::memory_order_relaxed, this=0x6f00740065006c)
    at /usr/include/c++/7/bits/atomic_base.h:396
#1  QAtomicOps&lt;int&gt;::load&lt;int&gt; (_q_value=...)
    at /opt/Qt5.12.3/5.12.3/gcc_64/include/QtCore/qatomic_cxx11.h:227
#2  0x00007fffedaa1021 in QBasicAtomicInteger&lt;int&gt;::load (
    this=0x6f00740065006c)
    at /opt/Qt5.12.3/5.12.3/gcc_64/include/QtCore/qbasicatomic.h:103
#3  0x00007fffeda9f569 in QtPrivate::RefCount::ref (this=0x6f00740065006c)
    at /opt/Qt5.12.3/5.12.3/gcc_64/include/QtCore/qrefcount.h:55
#4  0x00007fffedb03b15 in QList&lt;ctkLayoutViewFactory*&gt;::QList (
    this=0x7fffffffda40, l=...)
    at /opt/Qt5.12.3/5.12.3/gcc_64/include/QtCore/qlist.h:812
#5  0x00007fffedb02dd0 in ctkLayoutFactory::registeredViewFactories (
    this=0x555557b3e990)
    at /home/nzl/vela/build/CTK/Libs/Widgets/ctkLayoutFactory.cpp:99
#6  0x00007fffee752717 in qMRMLLayoutManager::mrmlViewFactories (
    this=0x555557b3e990)
    at /home/nzl/vela/build/slicersources-src/Libs/MRML/Widgets/qMRMLLayoutManager.cxx:779
#7  0x00007fffee75287d in qMRMLLayoutManager::mrmlViewFactory (
    this=0x555557b3e990, viewClassName=...)
    at /home/nzl/vela/build/slicersources-src/Libs/MRML/Widgets/qMRMLLayoutManag---Type &lt;return&gt; to continue, or q &lt;return&gt; to quit---
er.cxx:794
#8  0x00007fffee753150 in qMRMLLayoutManager::mrmlSliceLogics (
    this=0x555557b3e990)
    at /home/nzl/vela/build/slicersources-src/Libs/MRML/Widgets/qMRMLLayoutManager.cxx:928
#9  0x00007fffef7b94cc in qSlicerMainWindow::~qSlicerMainWindow (
    this=0x555556f76cb0, __in_chrg=&lt;optimized out&gt;)
    at /home/nzl/vela/build/slicersources-src/Base/QTApp/qSlicerMainWindow.cxx:774
</code></pre>
<p>I have no idea with these information, can anyone tell me what happened and how to solve it ?</p>

---
