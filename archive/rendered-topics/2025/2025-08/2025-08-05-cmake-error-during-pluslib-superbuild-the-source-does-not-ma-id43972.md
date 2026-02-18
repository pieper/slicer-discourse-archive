# CMake Error during PlusLib SuperBuild: "The source does not match..."

**Topic ID**: 43972
**Date**: 2025-08-05
**URL**: https://discourse.slicer.org/t/cmake-error-during-pluslib-superbuild-the-source-does-not-match/43972

---

## Post #1 by @Jaeseong (2025-08-05 15:40 UTC)

<p>Hi everyone,</p>
<p>I’m encountering an error during the building of <strong>Pluslib</strong>, which is a dependency for <strong>Slicer</strong> on <strong>Ubuntu</strong>. My goal is to acquire <strong>ultrasound images</strong> from a <strong>Windows machine</strong> using the <strong>PLUS server</strong>.</p>
<p>I followed the instructions in this link: <a href="https://github.com/PlusToolkit/PlusBuild/blob/master/Docs/BuildInstructionsLinux.md" class="inline-onebox" rel="noopener nofollow ugc">PlusBuild/Docs/BuildInstructionsLinux.md at master · PlusToolkit/PlusBuild · GitHub</a></p>
<p><strong>Error Message:</strong></p>
<pre><code class="lang-auto">[ 73%] Performing configure step for 'PlusLib'
CMake Error: The source "/home/user/devel/PlusBuild/PlusBuild-bin/PlusLib/CMakeLists.txt" does not match the source "/home/user/Slicer-SuperBuild-Debug/RapidJSON/CMakeLists.txt" used to generate cache. Re-run cmake with a different source directory.
make[2]: *** [CMakeFiles/PlusLib.dir/build.make:100: PlusLib-prefix/src/PlusLib-stamp/PlusLib-configure] Error 1
make[1]: *** [CMakeFiles/Makefile2:983: CMakeFiles/PlusLib.dir/all] Error 2
make: *** [Makefile:101: all] Error 2
</code></pre>
<p><strong>What I’ve tried so far:</strong></p>
<ol>
<li>
<p>I completely deleted the build directory (<code>PlusBuild-bin</code>) and started the build from scratch.</p>
</li>
<li>
<p>I manually removed <code>CMakeCache.txt</code> and the <code>CMakeFiles</code> directory and then re-ran CMake.</p>
</li>
</ol>
<p>Neither of these steps resolved the issue.</p>
<p><strong>My environment:</strong></p>
<ul>
<li>
<p>Ubuntu 22.04 LTS</p>
</li>
<li>
<p>Slicer 5.6.2 (To use SlicerRos2)</p>
</li>
</ul>
<p>Any insights into why this error might be occurring and what I might be missing would be greatly appreciated.</p>
<p>Thank you in advance for your help.</p>

---
