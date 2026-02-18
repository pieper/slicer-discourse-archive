# Long path using ninja

**Topic ID**: 1702
**Date**: 2017-12-21
**URL**: https://discourse.slicer.org/t/long-path-using-ninja/1702

---

## Post #1 by @dzenanz (2017-12-21 15:08 UTC)

<p>Configuring Slicer with <strong>ninja</strong> as the make program, and VS2015 cl.exe as compiler, I run into the error below. This doesn’t happen with pure VS2015 build in one letter longer build dir (<code>C:/Dev/Sn/</code> vs <code>C:/Dev/Svs/</code>). Is ninja merely more careful, or is this specific to ninja?</p>
<pre><code class="lang-auto">CMake Warning in Modules/Loadable/VolumeRendering/SubjectHierarchyPlugins/CMakeLists.txt:
  The object file directory

    C:/Dev/Sn/Slicer-build/Modules/Loadable/VolumeRendering/SubjectHierarchyPlugins/CMakeFiles/qSlicerVolumeRenderingSubjectHierarchyPluginsPythonQt.dir/

  has 149 characters.  The maximum full path to an object file is 250
  characters (see CMAKE_OBJECT_PATH_MAX).  Object file

    generated_cpp/osm_qSlicerVolumeRenderingSubjectHierarchyPlugins/osm_qSlicerVolumeRenderingSubjectHierarchyPlugins_module_init.cpp.obj

  cannot be safely placed under this directory.  The build may not work
  correctly.
</code></pre>

---

## Post #2 by @lassoan (2017-12-21 15:13 UTC)

<p>This is a warning only. Probably you just haven’t noticed it when you’ve built Slicer with the default generator.</p>

---

## Post #3 by @msmolens (2017-12-21 15:32 UTC)

<p>On a related note, has anyone tried enabling the new long path behavior in Windows 10?</p>
<p>From <a href="https://msdn.microsoft.com/en-us/library/windows/desktop/aa365247(v=vs.85).aspx#maxpath:" class="inline-onebox" rel="noopener nofollow ugc">Naming Files, Paths, and Namespaces - Win32 apps | Microsoft Learn</a></p>
<blockquote>
<p>Starting in Windows 10, version 1607, MAX_PATH limitations have been removed from common Win32 file and directory functions. However, you must opt-in to the new behavior.<br>
…<br>
To enable long path behavior set the registry key at HKLM\SYSTEM\CurrentControlSet\Control\FileSystem LongPathsEnabled (Type: REG_DWORD).</p>
</blockquote>

---

## Post #4 by @dzenanz (2017-12-21 16:00 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="1702">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This is a warning only.</p>
</blockquote>
</aside>
<p>The build stopped soon afterwards. I am now re-running ninja to see what happens.</p>
<aside class="quote no-group" data-username="msmolens" data-post="3" data-topic="1702">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/msmolens/48/139_2.png" class="avatar"> msmolens:</div>
<blockquote>
<p>has anyone tried enabling the new long path behavior in Windows 10</p>
</blockquote>
</aside>
<p>I could try it at home!</p>

---

## Post #5 by @dzenanz (2017-12-21 16:03 UTC)

<p>After re-running ninja, I get the same error:</p>
<pre><code class="lang-auto">-- Configuring done
CMake Warning in Modules/Loadable/VolumeRendering/SubjectHierarchyPlugins/CMakeLists.txt:
  The object file directory

    C:/Dev/Sn/Slicer-build/Modules/Loadable/VolumeRendering/SubjectHierarchyPlugins/CMakeFiles/qSlicerVolumeRenderingSubjectHierarchyPluginsPythonQt.dir/

  has 149 characters.  The maximum full path to an object file is 250
  characters (see CMAKE_OBJECT_PATH_MAX).  Object file

    generated_cpp/osm_qSlicerVolumeRenderingSubjectHierarchyPlugins/osm_qSlicerVolumeRenderingSubjectHierarchyPlugins_module_init.cpp.obj

  cannot be safely placed under this directory.  The build may not work
  correctly.


-- Generating done
-- Build files have been written to: C:/Dev/Sn/Slicer-build
[214/217] Performing build step for 'Slicer'
FAILED: Slicer-prefix/src/Slicer-stamp/Slicer-build
cmd.exe /C "cd /D C:\Dev\Sn\Slicer-build &amp;&amp; "C:\Program Files\CMake\bin\cmake.exe" --build . &amp;&amp; "C:\Program Files\CMake\bin\cmake.exe" -E touch C:/Dev/Sn/Slicer-prefix/src/Slicer-stamp/Slicer-build"
ninja: build stopped: subcommand failed.

C:\Dev\Sn&gt;
</code></pre>

---

## Post #6 by @dzenanz (2017-12-22 02:42 UTC)

<p>Trying to build Slicer in a long path build directory, the build fails when it comes turn to configure ITK. Then it snowballs from there. I guess we need to add extra logic to this check to handle the possibility of longer paths which now exists in Windows.</p>
<pre><code class="lang-auto">50&gt;  CMake Error at CMakeLists.txt:30 (message):
50&gt;    ITK source code directory path length is too long (65 &gt; 50).Please move the
50&gt;    ITK source code directory to a directory with a shorter path.
50&gt;
50&gt;
50&gt;  -- Configuring incomplete, errors occurred!
50&gt;  See also "C:/Dev/Slicer-buildVS2015x64-super-long-path-without-spaces/ITKv4-build/CMakeFiles/CMakeOutput.log".
</code></pre>

---

## Post #7 by @lassoan (2017-12-22 03:23 UTC)

<aside class="quote no-group" data-username="msmolens" data-post="3" data-topic="1702">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/msmolens/48/139_2.png" class="avatar"> msmolens:</div>
<blockquote>
<p>On a related note, has anyone tried enabling the new long path behavior in Windows 10?</p>
</blockquote>
</aside>
<p>It’ll take several years until all build tools will be updated to take advantage of new file path lengths. Also note that often long paths cause build failures by making environment variables too long.</p>
<p>It would be easier to limit file and directory name lengths in VTK and ITK. File path length issues popped up when modularization was introduced in VTK and ITK: it added one more level of directory for all files and increased number of libraries by a factor of 10x - which threw off Visual Studio.</p>

---

## Post #8 by @dzenanz (2017-12-23 19:08 UTC)

<p>Refactoring has already been done, and there is no going back. The support for longer max path was just <a href="https://discourse.itk.org/t/path-length-limitation-in-windows-lifted/545" rel="nofollow noopener">added</a> to ITK.</p>

---

## Post #9 by @lassoan (2017-12-23 20:32 UTC)

<p>Modularization is good, I’m not suggesting to going back, but it is implemented in a way that it puts significant burden on build systems. Hopefully, ITK&amp;VTK build system and/or Visual Studio will be improved at some point, because in large projects like Slicer we are near the limit of having a feasible build.</p>

---

## Post #10 by @dzenanz (2017-12-26 16:32 UTC)

<p>VTK developers plan to overhaul their build system. Once they are done, we plan to plagiarize that for ITK.</p>

---

## Post #11 by @ihnorton (2017-12-26 16:37 UTC)

<p>Do you mind to link to the discussion, if available?</p>

---

## Post #12 by @dzenanz (2017-12-26 20:35 UTC)

<p>I wanted to, but I don’t remember where I saw that.</p>

---

## Post #13 by @ihnorton (2017-12-27 14:36 UTC)

<p>We could make various changes to use the modularized build more effectively (e.g. not passing the full paths to every single library). But we effectively dump all VTK_LIBRARIES to the linker anyway, so modularization was kind of a no-op and comes at the cost of startup time. Processing &gt;600  dynamic libraries is really slow on mac (and to a lesser degree linux): a debug build takes close to 1 min to start on mac, the majority of which is in <code>strcmp</code> during symbol relocations. Release build is somewhat faster of course, but still spends most time doing relocation.</p>
<p>(Apple’s code dump for 10.13 shows big changes in dyld including some files about “caching”, so maybe this improves in High Sierra – but I still haven’t upgraded)</p>

---

## Post #14 by @ihnorton (2017-12-27 16:21 UTC)

<p>Just to clarify, that comment was intended as an observation rather than a complaint per se <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:">. There is enough other low-hanging fruit to go after next time we do build system optimization, and in the worst case we can relink VTK and ITK into single libraries ourself if it is demonstrably faster.</p>

---
