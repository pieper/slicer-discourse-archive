# Proposition to modify `slicerMacroBuildAppLibrary`

**Topic ID**: 20043
**Date**: 2021-10-07
**URL**: https://discourse.slicer.org/t/proposition-to-modify-slicermacrobuildapplibrary/20043

---

## Post #1 by @keri (2021-10-07 00:26 UTC)

<p>Hi,</p>
<p>I need to link to my SlicerCAT main target <code>qMyApp</code> (that is added via <code>slicerMacroBuildAppLibrary</code>) from external module.</p>
<p>From that external module I can see that <code>qMyApp</code> target is defined (it is exported in <code>SlicerTargets.cmake</code>) but it doesn’t have <code>INCLUDE_DIRECTORIES</code> property:</p>
<pre data-code-wrap="bash"><code class="lang-bash"># Snippet of code that is part of an external module CMakeLists after Slicer is found
get_target_property(qMyApp_INCLUDE_DIR qMyApp INCLUDE_DIRECTORIES)
message("qMyApp_INCLUDE_DIR: ${qMyApp_INCLUDE_DIR}")
</code></pre>
<p>and the message says <code>qMyApp_INCLUDE_DIR: qMyApp_INCLUDE_DIR-NOTFOUND</code>.</p>
<p>Thus to link <code>qMyApp</code> from external module I need to explicitely link include dirs via <code>target_include_directories(...)</code> for example.</p>
<p>That is  little bit strange as <code>slicerMacroBuildAppLibrary</code> uses <code>include_directories(${include_dirs})</code> and <code>add_library</code> and cmake documentation says (even target is added from <code>.cmake</code> file and dirs included also from there):</p>
<blockquote>
<p>The include directories are added to the <a href="https://cmake.org/cmake/help/latest/prop_dir/INCLUDE_DIRECTORIES.html#prop_dir:INCLUDE_DIRECTORIES" rel="noopener nofollow ugc"> <code>INCLUDE_DIRECTORIES</code> </a> directory property for the current <code>CMakeLists</code> file. They are also added to the <a href="https://cmake.org/cmake/help/latest/prop_tgt/INCLUDE_DIRECTORIES.html#prop_tgt:INCLUDE_DIRECTORIES" rel="noopener nofollow ugc"> <code>INCLUDE_DIRECTORIES</code> </a> target property for each target in the current <code>CMakeLists</code> file. The target property values are the ones used by the generators.</p>
</blockquote>
<p>I think the best solution would be to modify <code>SlicerMacroBuildApplication.cmake</code> and use <code>target_include_directories</code> instead of <code>include_directories</code>. Or to explicitely set property to target within <code>SlicerMacroBuildApplication.cmake</code>.</p>
<p><strong>I also have the related question in order to solve my problem without modifying Slicer’s cmake macro:</strong></p>
<p>How to export <code>qMyApp_INCLUDE_DIR</code> from my SlicerCAT CMakeLists to <code>SlicerConfig.cmake</code>?<br>
For external projects I do that with <code>mark_as_superbuild(qColadaApp_INCLUDE_DIR)</code> but this doesn’t seem to work with SlicerCAT project. There is no <code>qColadaApp_INCLUDE_DIR</code> var in <code>SlicerConfig.cmake</code></p>

---

## Post #2 by @lassoan (2021-10-07 13:15 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> what do you think?</p>

---

## Post #3 by @keri (2021-10-16 23:03 UTC)

<p>I was wrong about the idea that include dirs were not exported to <code>SlicerConfig.cmake</code> because they were included with <code>include_directories</code> instead of <code>target_include_directories</code>.</p>
<p>I looked to other cmake macros like <code>SlicerMacroBuildModule...cmake</code> and understood how include dirs are exported to <code>SlicerConfig.cmake</code></p>
<p>With that I created a <a href="https://github.com/Slicer/Slicer/pull/5950" rel="noopener nofollow ugc">pull request</a> that does export <code>_INCLUDE_DIRS</code> of custom library to <code>SlicerConfig.cmake</code>.</p>

---
