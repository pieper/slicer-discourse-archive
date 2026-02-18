# Mac build error in superclass array initializer in mrml volume rendering properties

**Topic ID**: 2270
**Date**: 2018-03-08
**URL**: https://discourse.slicer.org/t/mac-build-error-in-superclass-array-initializer-in-mrml-volume-rendering-properties/2270

---

## Post #1 by @pieper (2018-03-08 17:29 UTC)

<p>When I build now on mac I get the error below (related to <a href="https://github.com/Slicer/Slicer/commit/f4b50114908e98b1b6226f4b2e75bd95eb01e75b0">this recent commit about volume rendering presets</a>).</p>
<pre><code class="lang-auto">/Users/pieper/slicer4/latest/Slicer/Modules/Loadable/VolumeRendering/MRML/vtkMRMLVolumePropertyNode.cxx:27:19: error: expected '('
  , EffectiveRange{0.0, -1.0}
                  ^
</code></pre>
<details>
<summary>
more of the build errors</summary>
<pre><code class="lang-auto">/Users/pieper/slicer4/latest/Slicer/Modules/Loadable/VolumeRendering/MRML/vtkMRMLVolumePropertyNode.cxx:27:20: warning: expression result unused [-Wunused-value]
  , EffectiveRange{0.0, -1.0}
                   ^~~
/Users/pieper/slicer4/latest/Slicer/Modules/Loadable/VolumeRendering/MRML/vtkMRMLVolumePropertyNode.cxx:27:29: error: expected ';' after expression
  , EffectiveRange{0.0, -1.0}
                            ^
                            ;
/Users/pieper/slicer4/latest/Slicer/Modules/Loadable/VolumeRendering/MRML/vtkMRMLVolumePropertyNode.cxx:27:25: warning: expression result unused [-Wunused-value]
  , EffectiveRange{0.0, -1.0}
                        ^~~~
/Users/pieper/slicer4/latest/Slicer/Modules/Loadable/VolumeRendering/MRML/vtkMRMLVolumePropertyNode.cxx:28:3: error: expected unqualified-id
  , DisabledModify(0)
  ^
2 warnings and 3 errors generated.
</code></pre>
</details>
<p>I can work around it with this patch but I wonder if there’s a better solution:</p>
<pre><code class="lang-auto"> vtkMRMLVolumePropertyNode::vtkMRMLVolumePropertyNode()
   : VolumeProperty(NULL)
-  , EffectiveRange{0.0, -1.0}
   , DisabledModify(0)
 {
+  this-&gt;EffectiveRange[0] = 0.0;
+  this-&gt;EffectiveRange[1] = -1.0;
</code></pre>
<p>This error doesn’t happen on the dashboard machine, maybe because it <a href="http://slicer-devel-archive.65872.n3.nabble.com/MacOSX-factory-build-Transitioning-from-hybrid-quot-llvm-g-quot-to-quot-clang-quot-Update-to-Qt-4-8-6-tt4032198.html#a4032199">uses a custom compiler</a>.  I do not get the build error on linux.</p>
<p>I’m using the standard Xcode clang on mac.  Does anyone else have the same problem?</p>
<pre><code class="lang-auto">Apple LLVM version 9.0.0 (clang-900.0.39.2)
Target: x86_64-apple-darwin17.4.0
Thread model: posix
InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
</code></pre>

---

## Post #2 by @hherhold (2018-03-08 19:19 UTC)

<p>I can build on my Mac - 10.12.6, my compiler:</p>
<pre><code>~/Development/slicer/Slicer:7&gt; llvm-gcc --version
Apple LLVM version 9.0.0 (clang-900.0.39.2)
Target: x86_64-apple-darwin16.7.0
Thread model: posix
InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin</code></pre>

---

## Post #3 by @pieper (2018-03-08 19:28 UTC)

<p>Update: This error only occurs on a Qt4 build (Qt5 build on same machine works) so this is a C++ 11 issue.</p>

---

## Post #4 by @jcfr (2018-03-08 19:29 UTC)

<p>After talking with <a class="mention" href="/u/pieper">@pieper</a>, his build was done against Qt4. This explains the error because in that case, <code>C++98</code> was used.</p>
<p>Until Slicer 5 is out, I suggest we keep the code base compatible with both.</p>

---

## Post #5 by @pieper (2018-03-08 19:29 UTC)

<p>I’m planning to fix it like this, so we’ll remember to fix it when we switch to C++11 only.</p>
<pre><code class="lang-auto">//----------------------------------------------------------------------------
vtkMRMLVolumePropertyNode::vtkMRMLVolumePropertyNode()
  : VolumeProperty(NULL)
#if __cplusplus &gt;= 201103L
  , EffectiveRange{0.0,-1.0}
#endif
  , DisabledModify(0)
{
#if __cplusplus &lt; 201103L
  this-&gt;EffectiveRange[0] = 0.0;
  this-&gt;EffectiveRange[1] = -1.0;
#endif
</code></pre>

---

## Post #6 by @pieper (2018-03-08 19:38 UTC)

<p>Confirmed it builds in both modes and <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27027">committed as r27027</a>.</p>

---
