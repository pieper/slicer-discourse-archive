---
topic_id: 3277
title: "Build Error On Macosx And Linux With Itkpython Enabled"
date: 2018-06-25
url: https://discourse.slicer.org/t/3277
---

# Build error on MacOSX and Linux with ITKPython enabled

**Topic ID**: 3277
**Date**: 2018-06-25
**URL**: https://discourse.slicer.org/t/build-error-on-macosx-and-linux-with-itkpython-enabled/3277

---

## Post #1 by @Alex_Vergara (2018-06-25 11:35 UTC)

<p>Same setup here</p>
<p>Operating system: OSX 10.13<br>
Slicer: Newest nightly (Jun 25 2018)<br>
Qt: Qt5 web installer (last)<br>
CMake: 3.11.0<br>
Xcode: 9.4.1</p>
<p>but my errors are at DCMTK package.</p>
<pre><code class="lang-bash">[  0%] Building CXX object ofstd/libsrc/CMakeFiles/ofstd.dir/ofchrenc.cc.o
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:539:28: error: no class named 'Implementation' in 'OFCharacterEncoding'
class OFCharacterEncoding::Implementation {};
      ~~~~~~~~~~~~~~~~~~~~~^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:577:31: error: out-of-line definition of 'getLocaleEncoding' does not match any declaration in 'OFCharacterEncoding'
OFString OFCharacterEncoding::getLocaleEncoding()
                              ^~~~~~~~~~~~~~~~~
/opt/local/include/dcmtk/ofstd/ofchrenc.h:97:21: note: member declaration does not match because it is const qualified
    const OFString &amp;getLocaleEncoding() const;
                    ^                   ~~~~~
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:587:29: error: out-of-line definition of 'supportsConversionFlags' does not match any declaration in 'OFCharacterEncoding'
OFBool OFCharacterEncoding::supportsConversionFlags(const unsigned flags)
                            ^~~~~~~~~~~~~~~~~~~~~~~
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:598:5: error: member initializer 'TheImplementation' does not name a non-static data member or base class
  : TheImplementation()
    ^~~~~~~~~~~~~~~~~~~
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:605:27: error: no member named 'TheImplementation' in 'OFCharacterEncoding'
  : TheImplementation(rhs.TheImplementation)
                      ~~~ ^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:619:5: error: use of undeclared identifier 'TheImplementation'
    TheImplementation = rhs.TheImplementation;
    ^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:619:29: error: no member named 'TheImplementation' in 'OFCharacterEncoding'
    TheImplementation = rhs.TheImplementation;
                        ~~~ ^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:624:22: error: out-of-line definition of 'operator bool' does not match any declaration in 'OFCharacterEncoding'
OFCharacterEncoding::operator OFBool() const
                     ^~~~~~~~
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:626:34: error: use of undeclared identifier 'TheImplementation'
    return OFstatic_cast(OFBool, TheImplementation);
                                 ^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:630:29: error: out-of-line definition of 'operator!' does not match any declaration in 'OFCharacterEncoding'
OFBool OFCharacterEncoding::operator!() const
                            ^~~~~~~~
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:632:13: error: use of undeclared identifier 'TheImplementation'
    return !TheImplementation;
            ^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:636:29: error: out-of-line definition of 'operator==' does not match any declaration in 'OFCharacterEncoding'
OFBool OFCharacterEncoding::operator==(const OFCharacterEncoding&amp; rhs) const
                            ^~~~~~~~
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:638:37: error: no member named 'TheImplementation' in 'OFCharacterEncoding'
    return TheImplementation == rhs.TheImplementation;
                                ~~~ ^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:638:12: error: use of undeclared identifier 'TheImplementation'
    return TheImplementation == rhs.TheImplementation;
           ^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:641:29: error: out-of-line definition of 'operator!=' does not match any declaration in 'OFCharacterEncoding'
OFBool OFCharacterEncoding::operator!=(const OFCharacterEncoding&amp; rhs) const
                            ^~~~~~~~
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:643:37: error: no member named 'TheImplementation' in 'OFCharacterEncoding'
    return TheImplementation != rhs.TheImplementation;
                                ~~~ ^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:643:12: error: use of undeclared identifier 'TheImplementation'
    return TheImplementation != rhs.TheImplementation;
           ^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:655:31: error: out-of-line definition of 'getConversionFlags' does not match any declaration in 'OFCharacterEncoding'
unsigned OFCharacterEncoding::getConversionFlags() const
                              ^~~~~~~~~~~~~~~~~~
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:665:34: error: out-of-line definition of 'setConversionFlags' does not match any declaration in 'OFCharacterEncoding'
OFCondition OFCharacterEncoding::setConversionFlags(const unsigned flags)
                                 ^~~~~~~~~~~~~~~~~~
19 errors generated.
make[2]: *** [ofstd/libsrc/CMakeFiles/ofstd.dir/ofchrenc.cc.o] Error 1
make[1]: *** [ofstd/libsrc/CMakeFiles/ofstd.dir/all] Error 2
make: *** [all] Error 2
</code></pre>

---

## Post #2 by @lassoan (2018-06-25 12:29 UTC)

<p>A post was merged into an existing topic: <a href="/t/building-3dslicer-from-source-using-gcc-7-1/884/20">Building 3DSlicer from source using gcc 7.1</a></p>

---

## Post #3 by @Alex_Vergara (2018-06-25 11:27 UTC)

<p>When I try all the above it always stop at the DCMTK package with the following errors. Is there something I am missing?</p>
<pre><code class="lang-bash">[  0%] Building CXX object ofstd/libsrc/CMakeFiles/ofstd.dir/ofchrenc.cc.o
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:539:28: error: no class named 'Implementation' in 'OFCharacterEncoding'
class OFCharacterEncoding::Implementation {};
      ~~~~~~~~~~~~~~~~~~~~~^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:577:31: error: out-of-line definition of 'getLocaleEncoding' does not match any declaration in 'OFCharacterEncoding'
OFString OFCharacterEncoding::getLocaleEncoding()
                              ^~~~~~~~~~~~~~~~~
/opt/local/include/dcmtk/ofstd/ofchrenc.h:97:21: note: member declaration does not match because it is const qualified
    const OFString &amp;getLocaleEncoding() const;
                    ^                   ~~~~~
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:587:29: error: out-of-line definition of 'supportsConversionFlags' does not match any declaration in 'OFCharacterEncoding'
OFBool OFCharacterEncoding::supportsConversionFlags(const unsigned flags)
                            ^~~~~~~~~~~~~~~~~~~~~~~
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:598:5: error: member initializer 'TheImplementation' does not name a non-static data member or base class
  : TheImplementation()
    ^~~~~~~~~~~~~~~~~~~
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:605:27: error: no member named 'TheImplementation' in 'OFCharacterEncoding'
  : TheImplementation(rhs.TheImplementation)
                      ~~~ ^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:619:5: error: use of undeclared identifier 'TheImplementation'
    TheImplementation = rhs.TheImplementation;
    ^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:619:29: error: no member named 'TheImplementation' in 'OFCharacterEncoding'
    TheImplementation = rhs.TheImplementation;
                        ~~~ ^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:624:22: error: out-of-line definition of 'operator bool' does not match any declaration in 'OFCharacterEncoding'
OFCharacterEncoding::operator OFBool() const
                     ^~~~~~~~
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:626:34: error: use of undeclared identifier 'TheImplementation'
    return OFstatic_cast(OFBool, TheImplementation);
                                 ^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:630:29: error: out-of-line definition of 'operator!' does not match any declaration in 'OFCharacterEncoding'
OFBool OFCharacterEncoding::operator!() const
                            ^~~~~~~~
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:632:13: error: use of undeclared identifier 'TheImplementation'
    return !TheImplementation;
            ^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:636:29: error: out-of-line definition of 'operator==' does not match any declaration in 'OFCharacterEncoding'
OFBool OFCharacterEncoding::operator==(const OFCharacterEncoding&amp; rhs) const
                            ^~~~~~~~
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:638:37: error: no member named 'TheImplementation' in 'OFCharacterEncoding'
    return TheImplementation == rhs.TheImplementation;
                                ~~~ ^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:638:12: error: use of undeclared identifier 'TheImplementation'
    return TheImplementation == rhs.TheImplementation;
           ^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:641:29: error: out-of-line definition of 'operator!=' does not match any declaration in 'OFCharacterEncoding'
OFBool OFCharacterEncoding::operator!=(const OFCharacterEncoding&amp; rhs) const
                            ^~~~~~~~
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:643:37: error: no member named 'TheImplementation' in 'OFCharacterEncoding'
    return TheImplementation != rhs.TheImplementation;
                                ~~~ ^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:643:12: error: use of undeclared identifier 'TheImplementation'
    return TheImplementation != rhs.TheImplementation;
           ^
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:655:31: error: out-of-line definition of 'getConversionFlags' does not match any declaration in 'OFCharacterEncoding'
unsigned OFCharacterEncoding::getConversionFlags() const
                              ^~~~~~~~~~~~~~~~~~
/Users/alex/GIT/build/slicer/DCMTK/ofstd/libsrc/ofchrenc.cc:665:34: error: out-of-line definition of 'setConversionFlags' does not match any declaration in 'OFCharacterEncoding'
OFCondition OFCharacterEncoding::setConversionFlags(const unsigned flags)
                                 ^~~~~~~~~~~~~~~~~~
19 errors generated.
make[2]: *** [ofstd/libsrc/CMakeFiles/ofstd.dir/ofchrenc.cc.o] Error 1
make[1]: *** [ofstd/libsrc/CMakeFiles/ofstd.dir/all] Error 2
make: *** [all] Error 2
</code></pre>

---

## Post #4 by @mschumaker (2018-06-25 19:06 UTC)

<p>It makes more sense to have this as its own topic. I think the solution to this problem is going to be very different than the solution to mine was, though I can’t immediately see what it is.</p>
<p>One thing that did end up helping in my case was to avoid using Xcode. I changed my CMake configuration to generate unix makefiles, and I started the superbuild with ‘make’ from the terminal.</p>

---

## Post #5 by @Alex_Vergara (2018-06-26 07:35 UTC)

<p>Ok after some very deep digging I found the problem was the use of native icu library within the ofstd piece within DCMTK. Simply putting DCMTK_WITH_ICU to OFF and DCMTK_ENABLE_CHARSET_CONVERSION to  inside DCMTK-build folder ccmake configuration, allows the compiling of DCMTK package. Now another error arises, I will keep searching for a solution</p>
<pre><code class="lang-bash">/Users/alex/GIT/build/slicer/ITKv4/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_math.h:159:5: error: 'auto' not allowed in function return type
    auto isnan(Args&amp;&amp;... args) -&gt; decltype(std::isnan(std::forward&lt;Args&gt;(args)...)) {
    ^~~~
/Users/alex/GIT/build/slicer/ITKv4/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_math.h:159:31: error: expected ';' at end of declaration
    auto isnan(Args&amp;&amp;... args) -&gt; decltype(std::isnan(std::forward&lt;Args&gt;(args)...)) {
                              ^
                              ;
/Users/alex/GIT/build/slicer/ITKv4/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_math.h:159:32: error: cannot use arrow operator on a type
    auto isnan(Args&amp;&amp;... args) -&gt; decltype(std::isnan(std::forward&lt;Args&gt;(args)...)) {
                               ^
/Users/alex/GIT/build/slicer/ITKv4/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_math.h:163:5: error: 'auto' not allowed in function return type
    auto isinf(Args&amp;&amp;... args) -&gt; decltype(std::isinf(std::forward&lt;Args&gt;(args)...)) {
    ^~~~
/Users/alex/GIT/build/slicer/ITKv4/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_math.h:163:31: error: expected ';' at end of declaration
    auto isinf(Args&amp;&amp;... args) -&gt; decltype(std::isinf(std::forward&lt;Args&gt;(args)...)) {
                              ^
                              ;
/Users/alex/GIT/build/slicer/ITKv4/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_math.h:163:32: error: cannot use arrow operator on a type
    auto isinf(Args&amp;&amp;... args) -&gt; decltype(std::isinf(std::forward&lt;Args&gt;(args)...)) {
                               ^
/Users/alex/GIT/build/slicer/ITKv4/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_math.h:167:5: error: 'auto' not allowed in function return type
    auto isfinite(Args&amp;&amp;... args) -&gt; decltype(std::isfinite(std::forward&lt;Args&gt;(args)...)) {
    ^~~~
/Users/alex/GIT/build/slicer/ITKv4/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_math.h:167:34: error: expected ';' at end of declaration
    auto isfinite(Args&amp;&amp;... args) -&gt; decltype(std::isfinite(std::forward&lt;Args&gt;(args)...)) {
                                 ^
                                 ;
/Users/alex/GIT/build/slicer/ITKv4/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_math.h:167:35: error: cannot use arrow operator on a type
    auto isfinite(Args&amp;&amp;... args) -&gt; decltype(std::isfinite(std::forward&lt;Args&gt;(args)...)) {
                                  ^
/Users/alex/GIT/build/slicer/ITKv4/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_math.h:171:5: error: 'auto' not allowed in function return type
    auto isnormal(Args&amp;&amp;... args) -&gt; decltype(std::isnormal(std::forward&lt;Args&gt;(args)...)) {
    ^~~~
/Users/alex/GIT/build/slicer/ITKv4/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_math.h:171:34: error: expected ';' at end of declaration
    auto isnormal(Args&amp;&amp;... args) -&gt; decltype(std::isnormal(std::forward&lt;Args&gt;(args)...)) {
                                 ^
                                 ;
/Users/alex/GIT/build/slicer/ITKv4/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_math.h:171:35: error: cannot use arrow operator on a type
    auto isnormal(Args&amp;&amp;... args) -&gt; decltype(std::isnormal(std::forward&lt;Args&gt;(args)...)) {
                                  ^
/Users/alex/GIT/build/slicer/ITKv4/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_math.h:175:5: error: 'auto' not allowed in function return type
    auto max(Args&amp;&amp;... args) -&gt; decltype(std::max(std::forward&lt;Args&gt;(args)...)) {
    ^~~~
/Users/alex/GIT/build/slicer/ITKv4/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_math.h:175:29: error: expected ';' at end of declaration
    auto max(Args&amp;&amp;... args) -&gt; decltype(std::max(std::forward&lt;Args&gt;(args)...)) {
                            ^
                            ;
/Users/alex/GIT/build/slicer/ITKv4/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_math.h:175:30: error: cannot use arrow operator on a type
    auto max(Args&amp;&amp;... args) -&gt; decltype(std::max(std::forward&lt;Args&gt;(args)...)) {
                             ^
/Users/alex/GIT/build/slicer/ITKv4/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_math.h:179:5: error: 'auto' not allowed in function return type
    auto min(Args&amp;&amp;... args) -&gt; decltype(std::min(std::forward&lt;Args&gt;(args)...)) {
    ^~~~
/Users/alex/GIT/build/slicer/ITKv4/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_math.h:179:29: error: expected ';' at end of declaration
    auto min(Args&amp;&amp;... args) -&gt; decltype(std::min(std::forward&lt;Args&gt;(args)...)) {
                            ^
                            ;
/Users/alex/GIT/build/slicer/ITKv4/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_math.h:179:30: error: cannot use arrow operator on a type
    auto min(Args&amp;&amp;... args) -&gt; decltype(std::min(std::forward&lt;Args&gt;(args)...)) {
                             ^
/Users/alex/GIT/build/slicer/ITKv4/Modules/ThirdParty/VNL/src/vxl/core/vnl/vnl_math.h:184:5: error: 'auto' not allowed in function return type
    auto cuberoot(Args&amp;&amp;... args) -&gt; decltype(std::cbrt(std::forward&lt;Args&gt;(args)...)) {
    ^~~~
fatal error: too many errors emitted, stopping now [-ferror-limit=]
</code></pre>

---

## Post #6 by @fedorov (2018-06-26 14:05 UTC)

<p>I was able to build DCMTK in the current Slicer master (<a href="https://github.com/Slicer/Slicer/commit/4c0b0b15276aedc0e12d77e2227536426979d773">this hash</a>) on Mac without problems, and without changing any of the default configuration setting.</p>
<p>macOS: 10.13.5<br>
Xcode: 9.4.1<br>
clang: Apple LLVM version 9.1.0 (clang-902.0.39.2)<br>
cmake: 3.11.4</p>

---

## Post #7 by @Alex_Vergara (2018-06-26 14:09 UTC)

<p>Ok, above error is caused by the Slicer_BUILD_ITKPython option set to ON. After this the support for I18n should be disabled if you don’t have English system (the vtkMRML piece will complain about non existing file</p>
<pre><code class="lang-bash">make[5]: *** No rule to make target `/Users/alex/GIT/slicer/Libs/MRML/Widgets/Resources/Translations/qMRMLWidgets_fr.ts', needed by `Libs/MRML/Widgets/qMRMLWidgets_fr.qm'.  Stop.
</code></pre>
<p>) This must be fixed since it allows python use of ITK in plugins.</p>
<p>When you set Both options to OFF slicer starts compiling up to the MRLM package which complains about vtkMultiVolume.h was not built. Still digging</p>

---

## Post #8 by @fedorov (2018-06-26 14:14 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="7" data-topic="3277">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>above error is caused by the Slicer_BUILD_ITKPython option set to ON</p>
</blockquote>
</aside>
<p>I confirm I did not change the default OFF setting for this option.</p>

---

## Post #9 by @fedorov (2018-06-26 14:48 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="7" data-topic="3277">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>This must be fixed since it allows python use of ITK in plugins</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/alex_vergara">@Alex_Vergara</a> note that there are 2 mechanisms that expose ITK in python in Slicer:</p>
<ol>
<li><a href="http://www.simpleitk.org/">SimpleITK</a> (enabled by default)</li>
<li><a href="http://itkpythonpackage.readthedocs.io/en/latest/Quick_start_guide.html">ITKPython</a> (disabled by default)</li>
</ol>
<p>Perhaps you have a reason to access 2, but I wanted to make sure you are aware of 1.</p>
<p>Here’s the explanation of <a class="mention" href="/u/thewtex">@thewtex</a> about the differences between these two wrappings (from his response on LinkedIn to my question about <a href="https://blog.kitware.com/itk-is-on-pypi-pip-install-itk-is-here/">the blog post announcing ITK python</a>):</p>
<blockquote>
<p>The relative pros are,</p>
<p>For itk:</p>
<ul>
<li>Covers the entire toolkit, including processing with PointSet’s, Mesh’s, SpecializedCoordinatesImage, etc.</li>
<li>Retains the pipeline so very large images can be analyzed through streamed processing</li>
<li>The wrapping and packaging for externally developed modules is straightforward and can be built on free GitHub CI services (documentation for this is in progress)</li>
</ul>
<p>For SimpleITK:</p>
<ul>
<li>It does not have the pipeline but has a procedural interface, which is more  intuitive out of the gate for folks coming from the Matlab world</li>
</ul>
</blockquote>

---

## Post #10 by @Alex_Vergara (2018-06-26 15:45 UTC)

<p>Thank to both of you. I have handled all the build errors except the vtkMultiVolume one. I still don’t know which option to set in VTK to enable the build of it. copying from GitHub doesn’t work since it now complains about</p>
<pre><code class="lang-bash">In file included from /Users/alex/GIT/slicer/Modules/Loadable/VolumeRendering/MRMLDM/vtkMRMLVolumeRenderingDisplayableManager.cxx:52:
/Users/alex/GIT/build/slicer/VTKv9-build/Rendering/Volume/vtkMultiVolume.h:82:51: error: only virtual member functions can be marked 'override'
    void SetProperty(vtkVolumeProperty* property) override;
</code></pre>

---

## Post #11 by @fedorov (2018-06-26 15:48 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="10" data-topic="3277">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>I have handled all the build errors except the vtkMultiVolume one</p>
</blockquote>
</aside>
<p>I think this might be the feature that is still being developed, and maybe some issues have not yet been identified. <a class="mention" href="/u/cpinter">@cpinter</a> should be able to comment on this one most authoritatively.</p>

---

## Post #12 by @Alex_Vergara (2018-06-26 15:54 UTC)

<p>Ok just to start to, the default PythonQT configuration uses python2.7 (impossible to change right now) while VTK9 highly encourages python3 flavor, just a glitch.</p>
<p>I can’t see the vtkMultiVolume.h file in the default VTK clone from Slicer, it is in GitHub otherwise. maybe the problem is only to update VTK.</p>
<p>I see my problem, I left the VTK_MAJOR_VERSION in 7 which does not contain the vtkMultiVolume.h thing, changed to 9 and voilà. I think version 9 shall be the default to prevent this issue, since the MRML module explicitly depends on it.</p>

---

## Post #13 by @Alex_Vergara (2018-06-26 17:36 UTC)

<p>OK now the build stops at CTK</p>
<pre><code class="lang-bash">/Users/alex/GIT/build/slicer/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets/moc_ctkVTKMagnifyView.cpp:87:63: error: unknown type name 'QVTKWidget'; did you mean 'QWidget'?
        case 0: _t-&gt;enteredObservedWidget((*reinterpret_cast&lt; QVTKWidget*(*)&gt;(_a[1]))); break;
                                                              ^~~~~~~~~~
                                                              QWidget
/Users/alex/Qt/5.11.1/clang_64/lib/QtWidgets.framework/Headers/qwidget.h:128:24: note: 'QWidget' declared here
class Q_WIDGETS_EXPORT QWidget : public QObject, public QPaintDevice
                       ^
/Users/alex/GIT/build/slicer/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets/moc_ctkVTKMagnifyView.cpp:87:43: error: cannot initialize a parameter of type 'QVTKOpenGLWidget *' with an lvalue of type 'QWidget *'
        case 0: _t-&gt;enteredObservedWidget((*reinterpret_cast&lt; QVTKWidget*(*)&gt;(_a[1]))); break;
                                          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/alex/GIT/build/slicer/CTK/Libs/Visualization/VTK/Widgets/ctkVTKMagnifyView.h:137:49: note: passing argument to parameter 'widget' here
  void enteredObservedWidget(QVTKOpenGLWidget * widget);
                                                ^
/Users/alex/GIT/build/slicer/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets/moc_ctkVTKMagnifyView.cpp:88:60: error: unknown type name 'QVTKWidget'; did you mean 'QWidget'?
        case 1: _t-&gt;leftObservedWidget((*reinterpret_cast&lt; QVTKWidget*(*)&gt;(_a[1]))); break;
                                                           ^~~~~~~~~~
                                                           QWidget
/Users/alex/Qt/5.11.1/clang_64/lib/QtWidgets.framework/Headers/qwidget.h:128:24: note: 'QWidget' declared here
class Q_WIDGETS_EXPORT QWidget : public QObject, public QPaintDevice
                       ^
/Users/alex/GIT/build/slicer/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets/moc_ctkVTKMagnifyView.cpp:88:40: error: cannot initialize a parameter of type 'QVTKOpenGLWidget *' with an lvalue of type 'QWidget *'
        case 1: _t-&gt;leftObservedWidget((*reinterpret_cast&lt; QVTKWidget*(*)&gt;(_a[1]))); break;
                                       ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/alex/GIT/build/slicer/CTK/Libs/Visualization/VTK/Widgets/ctkVTKMagnifyView.h:138:46: note: passing argument to parameter 'widget' here
  void leftObservedWidget(QVTKOpenGLWidget * widget);
                                             ^
/Users/alex/GIT/build/slicer/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets/moc_ctkVTKMagnifyView.cpp:94:52: error: unknown type name 'QVTKWidget'; did you mean 'QWidget'?
            using _t = void (ctkVTKMagnifyView::*)(QVTKWidget * );
                                                   ^~~~~~~~~~
                                                   QWidget
/Users/alex/Qt/5.11.1/clang_64/lib/QtWidgets.framework/Headers/qwidget.h:128:24: note: 'QWidget' declared here
class Q_WIDGETS_EXPORT QWidget : public QObject, public QPaintDevice
                       ^
/Users/alex/GIT/build/slicer/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets/moc_ctkVTKMagnifyView.cpp:95:51: error: static_cast from 'void (ctkVTKMagnifyView::*)(QVTKOpenGLWidget *)' to '_t'
      (aka 'void (ctkVTKMagnifyView::*)(QWidget *)') is not allowed
            if (*reinterpret_cast&lt;_t *&gt;(_a[1]) == static_cast&lt;_t&gt;(&amp;ctkVTKMagnifyView::enteredObservedWidget)) {
                                                  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/alex/GIT/build/slicer/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets/moc_ctkVTKMagnifyView.cpp:101:52: error: unknown type name 'QVTKWidget'; did you mean 'QWidget'?
            using _t = void (ctkVTKMagnifyView::*)(QVTKWidget * );
                                                   ^~~~~~~~~~
                                                   QWidget
/Users/alex/Qt/5.11.1/clang_64/lib/QtWidgets.framework/Headers/qwidget.h:128:24: note: 'QWidget' declared here
class Q_WIDGETS_EXPORT QWidget : public QObject, public QPaintDevice
                       ^
/Users/alex/GIT/build/slicer/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets/moc_ctkVTKMagnifyView.cpp:102:51: error: static_cast from 'void (ctkVTKMagnifyView::*)(QVTKOpenGLWidget *)' to '_t'
      (aka 'void (ctkVTKMagnifyView::*)(QWidget *)') is not allowed
            if (*reinterpret_cast&lt;_t *&gt;(_a[1]) == static_cast&lt;_t&gt;(&amp;ctkVTKMagnifyView::leftObservedWidget)) {
                                                  ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/Users/alex/GIT/build/slicer/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets/moc_ctkVTKMagnifyView.cpp:188:47: error: unknown type name 'QVTKWidget'
void ctkVTKMagnifyView::enteredObservedWidget(QVTKWidget * _t1)
                                              ^
/Users/alex/GIT/build/slicer/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets/moc_ctkVTKMagnifyView.cpp:195:44: error: unknown type name 'QVTKWidget'
void ctkVTKMagnifyView::leftObservedWidget(QVTKWidget * _t1)
                                           ^
10 errors generated.
make[5]: *** [Libs/Visualization/VTK/Widgets/CMakeFiles/CTKVisualizationVTKWidgets.dir/moc_ctkVTKMagnifyView.cpp.o] Error 1
make[5]: *** Waiting for unfinished jobs....
/Users/alex/GIT/build/slicer/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets/moc_ctkVTKAbstractView.cpp:187:20: error: use of undeclared identifier 'QVTKWidget'; did you mean 'VTKWidget'?
        case 16: { QVTKWidget* _r = _t-&gt;VTKWidget();
                   ^~~~~~~~~~
                   VTKWidget
/Users/alex/GIT/build/slicer/CTK/Libs/Visualization/VTK/Widgets/ctkVTKAbstractView.h:153:34: note: 'VTKWidget' declared here
  Q_INVOKABLE QVTKOpenGLWidget * VTKWidget() const;
                                 ^
/Users/alex/GIT/build/slicer/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets/moc_ctkVTKAbstractView.cpp:187:20: error: call to non-static member function without an object argument
        case 16: { QVTKWidget* _r = _t-&gt;VTKWidget();
                   ^~~~~~~~~~
/Users/alex/GIT/build/slicer/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets/moc_ctkVTKAbstractView.cpp:187:32: error: use of undeclared identifier '_r'
        case 16: { QVTKWidget* _r = _t-&gt;VTKWidget();
                               ^
/Users/alex/GIT/build/slicer/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets/moc_ctkVTKAbstractView.cpp:188:43: error: unknown type name 'QVTKWidget'; did you mean 'QWidget'?
            if (_a[0]) *reinterpret_cast&lt; QVTKWidget**&gt;(_a[0]) = std::move(_r); }  break;
                                          ^~~~~~~~~~
                                          QWidget
/Users/alex/Qt/5.11.1/clang_64/lib/QtWidgets.framework/Headers/qwidget.h:128:24: note: 'QWidget' declared here
class Q_WIDGETS_EXPORT QWidget : public QObject, public QPaintDevice
                       ^
/Users/alex/GIT/build/slicer/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets/moc_ctkVTKAbstractView.cpp:188:76: error: use of undeclared identifier '_r'
            if (_a[0]) *reinterpret_cast&lt; QVTKWidget**&gt;(_a[0]) = std::move(_r); }  break;
                                                                           ^
/Users/alex/GIT/build/slicer/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets/moc_ctkVTKChartView.cpp:198:8: error: use of undeclared identifier 'QVTKWidget'; did you mean 'QWidget'?
    { &amp;QVTKWidget::staticMetaObject, qt_meta_stringdata_ctkVTKChartView.data,
       ^~~~~~~~~~
       QWidget
/Users/alex/Qt/5.11.1/clang_64/lib/QtWidgets.framework/Headers/qwidget.h:128:24: note: 'QWidget' declared here
class Q_WIDGETS_EXPORT QWidget : public QObject, public QPaintDevice
                       ^
/Users/alex/GIT/build/slicer/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets/moc_ctkVTKChartView.cpp:213:12: error: use of undeclared identifier 'QVTKWidget'; did you mean 'QWidget'?
    return QVTKWidget::qt_metacast(_clname);
           ^~~~~~~~~~
           QWidget
/Users/alex/Qt/5.11.1/clang_64/lib/QtWidgets.framework/Headers/qwidget.h:128:24: note: 'QWidget' declared here
class Q_WIDGETS_EXPORT QWidget : public QObject, public QPaintDevice
                       ^
/Users/alex/GIT/build/slicer/CTK-build/CTK-build/Libs/Visualization/VTK/Widgets/moc_ctkVTKChartView.cpp:218:11: error: use of undeclared identifier 'QVTKWidget'; did you mean 'QWidget'?
    _id = QVTKWidget::qt_metacall(_c, _id, _a);
          ^~~~~~~~~~
          QWidget
/Users/alex/Qt/5.11.1/clang_64/lib/QtWidgets.framework/Headers/qwidget.h:128:24: note: 'QWidget' declared here
class Q_WIDGETS_EXPORT QWidget : public QObject, public QPaintDevice
                       ^
5 errors generated.
make[5]: *** [Libs/Visualization/VTK/Widgets/CMakeFiles/CTKVisualizationVTKWidgets.dir/moc_ctkVTKAbstractView.cpp.o] Error 1
3 errors generated.
make[5]: *** [Libs/Visualization/VTK/Widgets/CMakeFiles/CTKVisualizationVTKWidgets.dir/moc_ctkVTKChartView.cpp.o] Error 1
make[4]: *** [Libs/Visualization/VTK/Widgets/CMakeFiles/CTKVisualizationVTKWidgets.dir/all] Error 2
make[3]: *** [all] Error 2
make[2]: *** [CTK-prefix/src/CTK-stamp/CTK-build] Error 2
make[1]: *** [CMakeFiles/CTK.dir/all] Error 2
make: *** [all] Error 2
</code></pre>
<p>it is like the QVTKWidget is not built</p>

---

## Post #14 by @Alex_Vergara (2018-06-26 18:37 UTC)

<p>hm I erased the whole CTK folder and relaunched the build and apparently the PythonQT library was not built in my previous try when I changed VTK versions so CTK is building now.</p>
<p>Apparently everything is fine now, except for the high annoyance that some parts are made with python 2.7 (like PythonQT) and others are made on python3 (like VTK).</p>

---

## Post #15 by @cpinter (2018-06-26 22:46 UTC)

<p>The error comes from including a VTK header, in which a virtual function is overridden without specifying the virtual keyword in the subclass. This being an error seems to be excessive, and also seems to be compiler specific. In any case, this is a bug in VTK core.</p>
<p>For reference, this line throws the error</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://gitlab.kitware.com/vtk/vtk/blob/master/Rendering/Volume/vtkMultiVolume.h#L82">
  <header class="source">
      <img src="https://gitlab.kitware.com/uploads/-/system/appearance/favicon/1/KitwareMarkIcon.png" class="site-icon" width="32" height="32">

      <a href="https://gitlab.kitware.com/vtk/vtk/blob/master/Rendering/Volume/vtkMultiVolume.h#L82" target="_blank" rel="noopener">GitLab</a>
  </header>

  <article class="onebox-body">
    <img src="https://gitlab.kitware.com/uploads/-/system/project/avatar/13/vtk_logo-main1.png" class="thumbnail onebox-avatar" width="146" height="146">

<h3><a href="https://gitlab.kitware.com/vtk/vtk/blob/master/Rendering/Volume/vtkMultiVolume.h#L82" target="_blank" rel="noopener">Rendering/Volume/vtkMultiVolume.h · master · VTK / VTK · GitLab</a></h3>

  <p>Visualization Toolkit</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
overriding this function</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://gitlab.kitware.com/vtk/vtk/blob/master/Rendering/Core/vtkVolume.h#L69">
  <header class="source">
      <img src="https://gitlab.kitware.com/uploads/-/system/appearance/favicon/1/KitwareMarkIcon.png" class="site-icon" width="32" height="32">

      <a href="https://gitlab.kitware.com/vtk/vtk/blob/master/Rendering/Core/vtkVolume.h#L69" target="_blank" rel="noopener">GitLab</a>
  </header>

  <article class="onebox-body">
    <img src="https://gitlab.kitware.com/uploads/-/system/project/avatar/13/vtk_logo-main1.png" class="thumbnail onebox-avatar" width="146" height="146">

<h3><a href="https://gitlab.kitware.com/vtk/vtk/blob/master/Rendering/Core/vtkVolume.h#L69" target="_blank" rel="noopener">Rendering/Core/vtkVolume.h · master · VTK / VTK · GitLab</a></h3>

  <p>Visualization Toolkit</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #16 by @Alex_Vergara (2018-06-27 08:40 UTC)

<p>Everything compiled fine but when I launch slicer then this happens</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4bdd07d6124224bcbc541d4db59efe2a991d7d5.png" data-download-href="/uploads/short-url/wDxxp1fIIYNrMyxNytE9IVhYPTD.png?dl=1" title="13" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4bdd07d6124224bcbc541d4db59efe2a991d7d5_2_574x500.png" alt="13" data-base62-sha1="wDxxp1fIIYNrMyxNytE9IVhYPTD" width="574" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4bdd07d6124224bcbc541d4db59efe2a991d7d5_2_574x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4bdd07d6124224bcbc541d4db59efe2a991d7d5_2_861x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4bdd07d6124224bcbc541d4db59efe2a991d7d5_2_1148x1000.png 2x" data-dominant-color="F0F0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">13</span><span class="informations">1472×1281 243 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I think it is something related with QT not found in path or something</p>

---

## Post #17 by @Alex_Vergara (2018-06-27 10:50 UTC)

<p>OK, fresh clone (today 27/June/2018), QT5 in custom folder installed from QT5 network installer,</p>
<p>in ccmake unmark SimpleITK, mark PythonQT, leave unmarked ITKPython as won’t work.</p>
<p>now it runs smoothly. Plugins downloaded from extension manager are not loading</p>
<pre><code class="lang-bash">Error(s):
    Cannot load library /Users/alex/GIT/build/slicer/Slicer-build/_CPack_Packages/macosx-amd64/DragNDrop/Slicer-4.9.0-2018-06-20-macosx-amd64/Slicer.app/Contents/Extensions-27262/SlicerRT/lib/Slicer-4.9/qt-loadable-modules/libqSlicerBeamsModule.dylib: (dlopen(/Users/alex/GIT/build/slicer/Slicer-build/_CPack_Packages/macosx-amd64/DragNDrop/Slicer-4.9.0-2018-06-20-macosx-amd64/Slicer.app/Contents/Extensions-27262/SlicerRT/lib/Slicer-4.9/qt-loadable-modules/libqSlicerBeamsModule.dylib, 133): Library not loaded: @rpath/Frameworks/QtMultimedia.framework/Versions/5/QtMultimedia
  Referenced from: /Users/alex/GIT/build/slicer/Slicer-build/_CPack_Packages/macosx-amd64/DragNDrop/Slicer-4.9.0-2018-06-20-macosx-amd64/Slicer.app/Contents/Extensions-27262/SlicerRT/lib/Slicer-4.9/qt-loadable-modules/libqSlicerBeamsModule.dylib
  Reason: image not found)
</code></pre>

---

## Post #18 by @ihnorton (2018-06-27 11:57 UTC)

<p>Plugins from the extension manager are not generally compatible with a local build, you need to build them locally also.</p>

---

## Post #19 by @Alex_Vergara (2018-06-27 13:06 UTC)

<p>I just do</p>
<pre><code class="lang-bash">echo "export DYLD_FRAMEWORK_PATH=/Users/alex/Qt/5.11.1/clang_64/lib" &gt; /Users/alex/.bash_profile
</code></pre>
<p>and everything magically starts working</p>
<p>edit: Actually it only worked temporarily since this only affects bash, for it to work completely you shall add this to ~/.MacOSX/environment.plist</p>
<pre><code class="lang-xml">&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs$
&lt;plist version="1.0"&gt;
&lt;dict&gt;
        &lt;key&gt;DYLD_FRAMEWORK_PATH&lt;/key&gt;
        &lt;string&gt;/Users/alex/Qt/5.11.1/clang_64/lib&lt;/string&gt;
&lt;/dict&gt;
&lt;/plist&gt;
</code></pre>

---

## Post #20 by @ihnorton (2018-06-27 13:13 UTC)

<p>Yes, on Mac technically you can do that (or fix the RPATH manually). It’s not a supported configuration so YMMV – don’t complain if the nightly build ABI changes and it stops working <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=5" title=":smile:" class="emoji" alt=":smile:"></p>

---

## Post #21 by @Alex_Vergara (2018-06-27 13:48 UTC)

<p>I shall develop a Slicer Module so I need the whole package running everywhere, so yeah I am ready to accept challenges.</p>

---

## Post #22 by @fedorov (2018-06-27 14:01 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="21" data-topic="3277" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>I shall develop a Slicer Module so I need the whole package running everywhere, so yeah I am ready to accept challenges.</p>
</blockquote>
</aside>
<p>If you need PythonQT that is not available in the nightly, you will need to take care of a lot of packaging both for the application and the modules. Before you spend too much time on this, I would check if <code>make package</code> in <code>Slicer-build</code> directory generates usable binaries for the platforms you need to support. I don’t know if anyone tested that.</p>

---

## Post #23 by @Alex_Vergara (2018-06-27 14:09 UTC)

<p>Already tested, it works! And it accepts extensions from the WebManager!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/34f5c3f02255497362e738a84c052223471b5969.png" data-download-href="/uploads/short-url/7yvnsrDO60qwnze40USCDywTpOx.png?dl=1" title="40" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34f5c3f02255497362e738a84c052223471b5969_2_690x185.png" alt="40" data-base62-sha1="7yvnsrDO60qwnze40USCDywTpOx" width="690" height="185" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34f5c3f02255497362e738a84c052223471b5969_2_690x185.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34f5c3f02255497362e738a84c052223471b5969_2_1035x277.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/34f5c3f02255497362e738a84c052223471b5969_2_1380x370.png 2x" data-dominant-color="CCCDD1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">40</span><span class="informations">2274×610 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
