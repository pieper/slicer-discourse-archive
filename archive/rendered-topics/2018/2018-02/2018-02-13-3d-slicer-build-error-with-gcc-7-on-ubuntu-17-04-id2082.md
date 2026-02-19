---
topic_id: 2082
title: "3D Slicer Build Error With Gcc 7 On Ubuntu 17 04"
date: 2018-02-13
url: https://discourse.slicer.org/t/2082
---

# 3D Slicer Build Error with GCC 7 on Ubuntu 17.04

**Topic ID**: 2082
**Date**: 2018-02-13
**URL**: https://discourse.slicer.org/t/3d-slicer-build-error-with-gcc-7-on-ubuntu-17-04/2082

---

## Post #1 by @AhmadHossam10 (2018-02-13 20:45 UTC)

<p>I am trying to build 3D Slicer but an error occurs, cc1 : warnings are being treated as errors.<br>
I searched for -Werror flag to remove it but I didn’t find it. I edited my CmakeLists.txt and<br>
wrote SET(CMAKE_CXX_FLAGS “-Wno-error”) and SET(CMAKE_C_FLAGS “-Wno-error”) also it didn’t work.<br>
How can I solve this issue ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/1789216e0b4cb2eba6db263dbb937122ed7dc0e3.png" data-download-href="/uploads/short-url/3mcMwRWcuolyAEjy8nvEoNOalfZ.png?dl=1" title="Screenshot%20from%202018-02-13%2016-41-13" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1789216e0b4cb2eba6db263dbb937122ed7dc0e3_2_690x388.png" alt="Screenshot%20from%202018-02-13%2016-41-13" data-base62-sha1="3mcMwRWcuolyAEjy8nvEoNOalfZ" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1789216e0b4cb2eba6db263dbb937122ed7dc0e3_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1789216e0b4cb2eba6db263dbb937122ed7dc0e3_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1789216e0b4cb2eba6db263dbb937122ed7dc0e3_2_1380x776.png 2x" data-dominant-color="39182E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-02-13%2016-41-13</span><span class="informations">1920×1080 315 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @jcfr (2018-02-13 20:57 UTC)

<p>Hi,</p>
<p>Thanks for the report.</p>
<p>On which operating system, using which compiler and with which options are you building ?  Could you share the command line you used to configure and build the project ?</p>
<p>Also what are the values of the CXXFLAGS and CFLAGS environment variables ?</p>

---

## Post #3 by @AhmadHossam10 (2018-02-13 21:01 UTC)

<p>Operating System : Ubuntu 17.10.1<br>
Compiler : GNU 7.2.0<br>
Cmake Command : cmake -DCMAKE_BUILD_TYPE:STRING=Debug -DQT_QMAKE_EXECUTABLE:FILEPATH=/usr/bin/qmake -DSlicer_USE_SYSTEM_QT:BOOL=1 …/Slicer</p>
<p>Make Command : make -j4</p>
<p>Values of CXXFLAGS and CFLAGS are the same of the project I cloned only -WALL flag I removed</p>

---

## Post #4 by @jcfr (2018-02-13 21:36 UTC)

<p>I was able to reproduce the error using Ubuntu 17.10 within a docker image, I will follow up with a fix.</p>

---

## Post #5 by @AhmadHossam10 (2018-02-13 21:41 UTC)

<p>waiting for your fix I have been trying for 3 weeks to solve this error please help</p>

---

## Post #6 by @jcfr (2018-02-13 23:57 UTC)

<p>Thanks for your patience. This issue is now fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26916">r26916</a>.</p>
<p>Please, update your source checkout and try to build again.</p>

---

## Post #7 by @jcfr (2018-02-14 00:11 UTC)

<p>Now addressing remaining issues associated with DCMTK:</p>
<pre><code class="lang-auto">In file included from /usr/include/c++/7/cstdint:35:0,
                 from /home/jcfr/Projects/Slicer-Qt4-VTK7-Ubuntu17.04-Release/DCMTK/ofstd/include/dcmtk/ofstd/ofstdinc.h:279,
                 from /home/jcfr/Projects/Slicer-Qt4-VTK7-Ubuntu17.04-Release/DCMTK/ofstd/include/dcmtk/ofstd/oftypes.h:74,
                 from /home/jcfr/Projects/Slicer-Qt4-VTK7-Ubuntu17.04-Release/DCMTK/ofstd/include/dcmtk/ofstd/ofuuid.h:27,
                 from /home/jcfr/Projects/Slicer-Qt4-VTK7-Ubuntu17.04-Release/DCMTK/ofstd/libsrc/ofuuid.cc:25:
/usr/include/c++/7/bits/c++0x_warning.h:32:2: error: #error This file requires compiler and library support for the ISO C++ 2011 standard. This support must be enabled with the -std=c++11 or -std=gnu++11 compiler options.
 #error This file requires compiler and library support \
  ^~~~~
In file included from /home/jcfr/Projects/Slicer-Qt4-VTK7-Ubuntu17.04-Release/DCMTK/ofstd/include/dcmtk/ofstd/ofuuid.h:27:0,
                 from /home/jcfr/Projects/Slicer-Qt4-VTK7-Ubuntu17.04-Release/DCMTK/ofstd/libsrc/ofuuid.cc:25:
/home/jcfr/Projects/Slicer-Qt4-VTK7-Ubuntu17.04-Release/DCMTK/ofstd/include/dcmtk/ofstd/oftypes.h:111:9: error: 'int64_t' does not name a type; did you mean '__int64_t'?
 typedef int64_t       Sint64;
         ^~~~~~~
         __int64_t
/home/jcfr/Projects/Slicer-Qt4-VTK7-Ubuntu17.04-Release/DCMTK/ofstd/include/dcmtk/ofstd/oftypes.h:125:9: error: 'uint64_t' does not name a type; did you mean '__uint64_t'?
 typedef uint64_t      Uint64;
         ^~~~~~~~
         __uint64_t
/home/jcfr/Projects/Slicer-Qt4-VTK7-Ubuntu17.04-Release/DCMTK/ofstd/include/dcmtk/ofstd/oftypes.h:145:9: error: 'Sint64' does not name a type; did you mean 'Sint16'?
 typedef Sint64 OFintptr_t;
         ^~~~~~
         Sint16
/home/jcfr/Projects/Slicer-Qt4-VTK7-Ubuntu17.04-Release/DCMTK/ofstd/include/dcmtk/ofstd/oftypes.h:150:9: error: 'Uint64' does not name a type; did you mean 'Uint16'?
 typedef Uint64 OFuintptr_t;
         ^~~~~~
         Uint16

</code></pre>

---

## Post #8 by @jcfr (2018-02-14 02:45 UTC)

<p>Build issue associated with  DCMTK has been fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26920">r26920</a></p>
<p>This commit also updates the version of DCMTK used in Slicer to 3.6.3</p>

---

## Post #9 by @jcfr (2018-02-14 03:18 UTC)

<p><a class="mention" href="/u/ahmadhossam10">@AhmadHossam10</a> To move forward, I suggest you build Slicer against Qt5 by passing <code>-DQt5_DIR:PATH=/path/to/lib/cmake/Qt5</code></p>
<p>In few days, we will update the build system so that it defaults to Qt5 and support for Qt4 and C++98 will not actively be maintained and will be removed later this year.</p>
<p>In the mean time, here are few more errors related to ITK:</p>
<pre><code class="lang-auto"> #error This file requires compiler and library support \
  ^~~~~
In file included from /path/to/Slicer-Release/ITKv4/Modules/IO/ImageBase/include/itkImageFileWriter.hxx:34:0,
                 from /path/to/Slicer-Release/ITKv4/Modules/IO/ImageBase/include/itkImageFileWriter.h:226,
                 from /path/to/Slicer-Release/ITKv4/Modules/IO/ImageBase/include/itkImageSeriesWriter.h:23,
                 from /path/to/Slicer-Release/ITKv4/Modules/IO/ImageBase/src/itkImageSeriesWriter.cxx:18:
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:57:36: error: 'true_type' in namespace 'std' does not name a type
     typedef ITK_STD_TR1_NAMESPACE::true_type  TrueType;
                                    ^~~~~~~~~
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:58:36: error: 'false_type' in namespace 'std' does not name a type
     typedef ITK_STD_TR1_NAMESPACE::false_type FalseType;
                                    ^~~~~~~~~~
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h: In static member function 'static void itk::ImageAlgorithm::Copy(const itk::Image&lt;TPixel1, VImageDimension&gt;*, itk::Image&lt;TPixel2, VImageDimension&gt;*, const typename itk::Image&lt;TPixel1, VImageDimension&gt;::RegionType&amp;, const typename itk::Image&lt;TPixel2, VImageDimension&gt;::RegionType&amp;)':
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:104:61: error: 'is_convertible' is not a member of 'std'
                                    , ITK_STD_TR1_NAMESPACE::is_convertible&lt;typename _ImageType1::PixelType,
                                                             ^~~~~~~~~~~~~~
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:104:61: note: suggested alternative: '__convert_to_v'
                                    , ITK_STD_TR1_NAMESPACE::is_convertible&lt;typename _ImageType1::PixelType,
                                                             ^~~~~~~~~~~~~~
                                                             __convert_to_v
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:104:107: error: expected '(' before ',' token
                                    , ITK_STD_TR1_NAMESPACE::is_convertible&lt;typename _ImageType1::PixelType,
                                                                                                           ^
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:105:67: error: expected '(' before '&gt;' token
                                    typename _ImageType2::PixelType&gt;()
                                                                   ^
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:105:69: error: expected primary-expression before ')' token
                                    typename _ImageType2::PixelType&gt;()
                                                                     ^
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h: In static member function 'static void itk::ImageAlgorithm::Copy(const itk::VectorImage&lt;TPixel1, VImageDimension&gt;*, itk::VectorImage&lt;TPixel2, VImageDimension&gt;*, const typename itk::VectorImage&lt;TPixel1, VImageDimension&gt;::RegionType&amp;, const typename itk::VectorImage&lt;TPixel2, VImageDimension&gt;::RegionType&amp;)':
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:125:61: error: 'is_convertible' is not a member of 'std'
                                    , ITK_STD_TR1_NAMESPACE::is_convertible&lt;typename _ImageType1::PixelType,
                                                             ^~~~~~~~~~~~~~
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:125:61: note: suggested alternative: '__convert_to_v'
                                    , ITK_STD_TR1_NAMESPACE::is_convertible&lt;typename _ImageType1::PixelType,
                                                             ^~~~~~~~~~~~~~
                                                             __convert_to_v
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:125:107: error: expected '(' before ',' token
                                    , ITK_STD_TR1_NAMESPACE::is_convertible&lt;typename _ImageType1::PixelType,
                                                                                                           ^
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:126:67: error: expected '(' before '&gt;' token
                                    typename _ImageType2::PixelType&gt;()
                                                                   ^
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:126:69: error: expected primary-expression before ')' token
                                    typename _ImageType2::PixelType&gt;()
                                                                     ^
[908/2327] Linking CXX shared library lib/libITKPath-4.13.so.1
[909/2327] Building CXX object Modules/IO/ImageBase/src/CMakeFiles/ITKIOImageBase.dir/itkImageFileWriter.cxx.o
FAILED: Modules/IO/ImageBase/src/CMakeFiles/ITKIOImageBase.dir/itkImageFileWriter.cxx.o 
/usr/bin/c++  -DITKIOImageBase_EXPORTS -IModules/ThirdParty/KWIML/src -I/path/to/Slicer-Release/ITKv4/Modules/ThirdParty/KWIML/src -IModules/ThirdParty/KWSys/src -I/path/to/Slicer-Release/ITKv4/Modules/ThirdParty/VNL/src/vxl/v3p/netlib -I/path/to/Slicer-Release/ITKv4/Modules/ThirdParty/VNL/src/vxl/vcl -I/path/to/Slicer-Release/ITKv4/Modules/ThirdParty/VNL/src/vxl/core -IModules/ThirdParty/VNL/src/vxl/v3p/netlib -IModules/ThirdParty/VNL/src/vxl/vcl -IModules/ThirdParty/VNL/src/vxl/core -I/path/to/Slicer-Release/ITKv4/Modules/ThirdParty/VNLInstantiation/include -IModules/Core/Common -I/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include -IModules/IO/ImageBase -I/path/to/Slicer-Release/ITKv4/Modules/IO/ImageBase/include -IModules/ThirdParty/KWSys/src/KWSys -Wall -Wcast-align -Wdisabled-optimization -Wextra -Wformat=2 -Winvalid-pch -Wno-format-nonliteral -Wpointer-arith -Wshadow -Wunused -Wwrite-strings -funit-at-a-time -Wno-strict-overflow -Wno-deprecated -Wno-invalid-offsetof -Woverloaded-virtual -Wstrict-null-sentinel  -g -fPIC -fvisibility=hidden -fvisibility-inlines-hidden   -std=c++98 -MD -MT Modules/IO/ImageBase/src/CMakeFiles/ITKIOImageBase.dir/itkImageFileWriter.cxx.o -MF Modules/IO/ImageBase/src/CMakeFiles/ITKIOImageBase.dir/itkImageFileWriter.cxx.o.d -o Modules/IO/ImageBase/src/CMakeFiles/ITKIOImageBase.dir/itkImageFileWriter.cxx.o -c /path/to/Slicer-Release/ITKv4/Modules/IO/ImageBase/src/itkImageFileWriter.cxx
In file included from /usr/include/c++/7/type_traits:35:0,
                 from /path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:24,
                 from /path/to/Slicer-Release/ITKv4/Modules/IO/ImageBase/include/itkImageFileWriter.hxx:34,
                 from /path/to/Slicer-Release/ITKv4/Modules/IO/ImageBase/include/itkImageFileWriter.h:226,
                 from /path/to/Slicer-Release/ITKv4/Modules/IO/ImageBase/src/itkImageFileWriter.cxx:18:
/usr/include/c++/7/bits/c++0x_warning.h:32:2: error: #error This file requires compiler and library support for the ISO C++ 2011 standard. This support must be enabled with the -std=c++11 or -std=gnu++11 compiler options.
 #error This file requires compiler and library support \
  ^~~~~
In file included from /path/to/Slicer-Release/ITKv4/Modules/IO/ImageBase/include/itkImageFileWriter.hxx:34:0,
                 from /path/to/Slicer-Release/ITKv4/Modules/IO/ImageBase/include/itkImageFileWriter.h:226,
                 from /path/to/Slicer-Release/ITKv4/Modules/IO/ImageBase/src/itkImageFileWriter.cxx:18:
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:57:36: error: 'true_type' in namespace 'std' does not name a type
     typedef ITK_STD_TR1_NAMESPACE::true_type  TrueType;
                                    ^~~~~~~~~
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:58:36: error: 'false_type' in namespace 'std' does not name a type
     typedef ITK_STD_TR1_NAMESPACE::false_type FalseType;
                                    ^~~~~~~~~~
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h: In static member function 'static void itk::ImageAlgorithm::Copy(const itk::Image&lt;TPixel1, VImageDimension&gt;*, itk::Image&lt;TPixel2, VImageDimension&gt;*, const typename itk::Image&lt;TPixel1, VImageDimension&gt;::RegionType&amp;, const typename itk::Image&lt;TPixel2, VImageDimension&gt;::RegionType&amp;)':
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:104:61: error: 'is_convertible' is not a member of 'std'
                                    , ITK_STD_TR1_NAMESPACE::is_convertible&lt;typename _ImageType1::PixelType,
                                                             ^~~~~~~~~~~~~~
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:104:61: note: suggested alternative: '__convert_to_v'
                                    , ITK_STD_TR1_NAMESPACE::is_convertible&lt;typename _ImageType1::PixelType,
                                                             ^~~~~~~~~~~~~~
                                                             __convert_to_v
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:104:107: error: expected '(' before ',' token
                                    , ITK_STD_TR1_NAMESPACE::is_convertible&lt;typename _ImageType1::PixelType,
                                                                                                           ^
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:105:67: error: expected '(' before '&gt;' token
                                    typename _ImageType2::PixelType&gt;()
                                                                   ^
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:105:69: error: expected primary-expression before ')' token
                                    typename _ImageType2::PixelType&gt;()
                                                                     ^
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h: In static member function 'static void itk::ImageAlgorithm::Copy(const itk::VectorImage&lt;TPixel1, VImageDimension&gt;*, itk::VectorImage&lt;TPixel2, VImageDimension&gt;*, const typename itk::VectorImage&lt;TPixel1, VImageDimension&gt;::RegionType&amp;, const typename itk::VectorImage&lt;TPixel2, VImageDimension&gt;::RegionType&amp;)':
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:125:61: error: 'is_convertible' is not a member of 'std'
                                    , ITK_STD_TR1_NAMESPACE::is_convertible&lt;typename _ImageType1::PixelType,
                                                             ^~~~~~~~~~~~~~
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:125:61: note: suggested alternative: '__convert_to_v'
                                    , ITK_STD_TR1_NAMESPACE::is_convertible&lt;typename _ImageType1::PixelType,
                                                             ^~~~~~~~~~~~~~
                                                             __convert_to_v
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:125:107: error: expected '(' before ',' token
                                    , ITK_STD_TR1_NAMESPACE::is_convertible&lt;typename _ImageType1::PixelType,
                                                                                                           ^
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:126:67: error: expected '(' before '&gt;' token
                                    typename _ImageType2::PixelType&gt;()
                                                                   ^
/path/to/Slicer-Release/ITKv4/Modules/Core/Common/include/itkImageAlgorithm.h:126:69: error: expected primary-expression before ')' token
                                    typename _ImageType2::PixelType&gt;()
                                                                     ^
</code></pre>

---

## Post #10 by @jcfr (2018-02-14 03:28 UTC)

<p>ITK build error fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26922">r26922</a></p>

---

## Post #11 by @AhmadHossam10 (2018-02-14 08:31 UTC)

<p>I already use c++11 instead of c++98 by updating cmakelists.txt<br>
Thanks very much I will try and build again</p>

---

## Post #12 by @chir.set (2018-02-14 10:53 UTC)

<p>In case it may be of helpful, Slicer builds nicely with Qt5 on Arch Linux using gcc 7.3.0, both in debug and release mode. If you get a working Qt5/VTK9 build, I would like to know if Volume Rendering works flawlessly on your machine, and the details of your GPU chip. TIA for providing the info.</p>

---

## Post #13 by @lassoan (2018-02-14 13:18 UTC)

<aside class="quote no-group" data-username="chir.set" data-post="12" data-topic="2082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chir.set/48/66982_2.png" class="avatar"> chir.set:</div>
<blockquote>
<p>If you get a working Qt5/VTK9 build, I would like to know if Volume Rendering works flawlessly on your machine</p>
</blockquote>
</aside>
<p>Do you mean on Linux or on any computer? If you were interested in hearing about any computers with any OS then it is probably better to post this question as a new topic.</p>

---

## Post #14 by @jcfr (2018-02-14 14:28 UTC)

<aside class="quote no-group" data-username="AhmadHossam10" data-post="11" data-topic="2082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ahmadhossam10/48/1246_2.png" class="avatar"> AhmadHossam10:</div>
<blockquote>
<p>I already use c++11 instead of c++98 by updating cmakelists.txt</p>
</blockquote>
</aside>
<p>If you would like to build with C++11, the recommended and supported approach is this one:</p>
<pre><code class="lang-auto">cmake -DCMAKE_BUILD_TYPE:STRING=Debug \
  -DQt5_DIR:PATH=/path/to/lib/cmake/Qt5 …/Slicer
</code></pre>
<p>This will automatically set variables like <code>CMAKE_CXX_STANDARD</code> and download VTK9.</p>

---

## Post #15 by @chir.set (2018-02-14 15:34 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="2082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you mean on Linux or on any computer?</p>
</blockquote>
</aside>
<p>On Linux. As the OP uses Ubuntu 17.10, I thought it was understood.</p>

---

## Post #16 by @Davide_Punzo (2018-02-15 21:49 UTC)

<p><a class="mention" href="/u/chir.set">@chir.set</a> building on ubuntu 17.10, gcc 6.4, Qt5.10 (debug) I have no issue with the rendering. Tested on various nvidia gpu (760, 970, 1050).</p>

---

## Post #17 by @chir.set (2018-02-16 07:45 UTC)

<aside class="quote no-group" data-username="Davide_Punzo" data-post="16" data-topic="2082">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>Tested on various nvidia gpu (760, 970, 1050).</p>
</blockquote>
</aside>
<p>One last question (going slightly off-topic) : are you using stock open source kernel module or Nvidia proprietary  module ? Thanks.</p>

---

## Post #18 by @Davide_Punzo (2018-02-16 14:29 UTC)

<p>I am currently using 384.111 installed from the ubuntu repository (which I guess are the Nvidia proprietary one)</p>

---

## Post #19 by @AhmadHossam10 (2018-02-18 00:22 UTC)

<p>Everything is fixed except for an error in simpleITK there’s a file that’s not found. Would you please solve this issue ? <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/8446cb5f45d1d4ea9213341cfff49b77b77d16dd.png" data-download-href="/uploads/short-url/iSaHyduu17TdMsizIvVnPtUmau1.png?dl=1" title="Screenshot%20from%202018-02-18%2002-21-24" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8446cb5f45d1d4ea9213341cfff49b77b77d16dd_2_690x388.png" alt="Screenshot%20from%202018-02-18%2002-21-24" data-base62-sha1="iSaHyduu17TdMsizIvVnPtUmau1" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8446cb5f45d1d4ea9213341cfff49b77b77d16dd_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8446cb5f45d1d4ea9213341cfff49b77b77d16dd_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8446cb5f45d1d4ea9213341cfff49b77b77d16dd_2_1380x776.png 2x" data-dominant-color="37172C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-02-18%2002-21-24</span><span class="informations">1920×1080 333 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1dd3beb79c60da296eaee03250bddf48637fff3d.png" data-download-href="/uploads/short-url/4fRvvtViarcLPDROnPTK2UWjaTX.png?dl=1" title="Screenshot%20from%202018-02-18%2002-20-23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dd3beb79c60da296eaee03250bddf48637fff3d_2_690x388.png" alt="Screenshot%20from%202018-02-18%2002-20-23" data-base62-sha1="4fRvvtViarcLPDROnPTK2UWjaTX" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dd3beb79c60da296eaee03250bddf48637fff3d_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dd3beb79c60da296eaee03250bddf48637fff3d_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1dd3beb79c60da296eaee03250bddf48637fff3d_2_1380x776.png 2x" data-dominant-color="412338"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot%20from%202018-02-18%2002-20-23</span><span class="informations">1920×1080 431 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
