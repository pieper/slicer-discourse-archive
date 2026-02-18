# Add_subdirectory() fails with ‘-features=no%anachronisms’

**Topic ID**: 20395
**Date**: 2021-10-27
**URL**: https://discourse.slicer.org/t/add-subdirectory-fails-with-features-no-anachronisms/20395

---

## Post #1 by @joachim (2021-10-27 22:34 UTC)

<p>I started working on my own loadable module based on <em>Extension Wizard</em>. My module has a subfolder containing <a href="https://github.com/libusb/hidapi" rel="noopener nofollow ugc">a library</a> that my module depends on. This library is a CMake project. But in my module’s <code>CMakeLists.txt</code>, the line <code>add_subdirectory( path-to-library )</code> fails during cmake:</p>
<pre><code class="lang-auto">Determining if the CXX compiler accepts the flag -features=no%anachronisms passed with the following output:
Change Dir: /opt/e/SlicerNDOF-debug/CMakeFiles/CMakeTmp

Run Build Command(s):/usr/bin/make cmTC_27b52/fast &amp;&amp; /Applications/Xcode.app/Contents/Developer/usr/bin/make  -f CMakeFiles/cmTC_27b52.dir/build.make CMakeFiles/cmTC_27b52.dir/build
Building CXX object CMakeFiles/cmTC_27b52.dir/src.cxx.o
/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++   -features=no%anachronisms -arch x86_64 -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX11.1.sdk -mmacosx-version-min=10.15 -std=c++11 -o CMakeFiles/cmTC_27b52.dir/src.cxx.o -c /opt/e/SlicerNDOF-debug/CMakeFiles/CMakeTmp/src.cxx
clang: error: unknown argument: '-features=no%anachronisms'
make[1]: *** [CMakeFiles/cmTC_27b52.dir/src.cxx.o] Error 1
make: *** [cmTC_27b52/fast] Error 2


Source file was:
int main() { return 0;}
</code></pre>
<p>This compiler check seems to be <a href="https://github.com/Slicer/Slicer/blob/955326ccbd0a7855a776a4da9d458f24fc2306f3/CMake/ITKPlatformSpecificChecks.cmake#L115" rel="noopener nofollow ugc">something that the Slicer build introduces</a> (?) and something that my library’s cmake doesn’t like. The library builds with no problem on its own.</p>
<p>Do you know how to fix this?</p>

---
