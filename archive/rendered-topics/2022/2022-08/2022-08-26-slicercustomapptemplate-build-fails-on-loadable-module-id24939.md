---
topic_id: 24939
title: "Slicercustomapptemplate Build Fails On Loadable Module"
date: 2022-08-26
url: https://discourse.slicer.org/t/24939
---

# SlicerCustomAppTemplate build fails on Loadable Module

**Topic ID**: 24939
**Date**: 2022-08-26
**URL**: https://discourse.slicer.org/t/slicercustomapptemplate-build-fails-on-loadable-module/24939

---

## Post #1 by @brandus1 (2022-08-26 18:44 UTC)

<p>I have a SlicerCustomApplication with a loadable module with this tree structure:</p>
<pre><code class="lang-auto">.
├── CMakeLists.txt
├── Logic
│   ├── CMakeLists.txt
│   ├── vtkKernelFeedMultiply.cxx
│   ├── vtkKernelFeedMultiply.h
│   ├── vtkSlicerFeedMultiplyLogic.cxx
│   └── vtkSlicerFeedMultiplyLogic.h
├── Resources
│   ├── Icons
│   │   └── FeedMultiply.png
│   ├── UI
│   │   ├── qSlicerFeedMultiplyFooBarWidget.ui
│   │   └── qSlicerFeedMultiplyModuleWidget.ui
│   └── qSlicerFeedMultiplyModule.qrc
├── Testing
│   ├── CMakeLists.txt
│   └── Cxx
│       └── CMakeLists.txt
├── Widgets
│   ├── CMakeLists.txt
│   ├── qSlicerFeedMultiplyFooBarWidget.cxx
│   └── qSlicerFeedMultiplyFooBarWidget.h
├── build.sh
├── qSlicerFeedMultiplyModule.cxx
├── qSlicerFeedMultiplyModule.h
├── qSlicerFeedMultiplyModuleWidget.cxx
└── qSlicerFeedMultiplyModuleWidget.h
</code></pre>
<p>the customapp always built correctly while this module was bundled in an Extension. Now for development reasons I had to take this out of such extension and add it directly through the cmake <code>Slicer_EXTENSION_SOURCE_DIRS</code> variable in the app CMakeLists.txt.</p>
<p>Now the build fails with:</p>
<pre><code class="lang-auto">/opt/p/Slicer-build/E/FeedMultiply/qSlicerFeedMultiplyModuleWidgetGenericTest.cxx:51:10: fatal error: 'qSlicerFeedMultiplyModule.h' file not found
#include "qSlicerFeedMultiplyModule.h"
         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1 error generated.
make[2]: *** [E/FeedMultiply/CMakeFiles/qSlicerFeedMultiplyModuleGenericCxxTests.dir/qSlicerFeedMultiplyModuleWidgetGenericTest.cxx.o] Error 1
make[2]: *** Waiting for unfinished jobs....
/opt/p/Slicer-build/E/FeedMultiply/qSlicerFeedMultiplyModuleGenericTest.cxx:49:10: fatal error: 'qSlicerFeedMultiplyModule.h' file not found
#include "qSlicerFeedMultiplyModule.h"
         ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1 error generated.
make[2]: *** [E/FeedMultiply/CMakeFiles/qSlicerFeedMultiplyModuleGenericCxxTests.dir/qSlicerFeedMultiplyModuleGenericTest.cxx.o] Error 1
make[1]: *** [E/FeedMultiply/CMakeFiles/qSlicerFeedMultiplyModuleGenericCxxTests.dir/all] Error 2
make: *** [all] Error 2
</code></pre>
<p>A workaround is commenting the default flag <code>WITH_GENERIC_TESTS</code> in <code>slicerMacroBuildLoadableModule</code> in the module CMakeLists.txt. Then it build correctly</p>
<p>Any suggestion on why this happens?</p>
<p>Thank you very much</p>

---

## Post #2 by @lassoan (2022-08-27 22:35 UTC)

<p>You can compare your CMakeLists.txt files with similar files in other extensions, such as in <a href="https://github.com/SlicerIGT/SlicerIGT">SlicerIGT</a>.</p>

---
