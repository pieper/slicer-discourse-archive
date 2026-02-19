---
topic_id: 43408
title: "Issue With Including Scripted Module In Custom Slicer Based"
date: 2025-06-18
url: https://discourse.slicer.org/t/43408
---

# Issue with Including Scripted Module in Custom Slicer-Based Application

**Topic ID**: 43408
**Date**: 2025-06-18
**URL**: https://discourse.slicer.org/t/issue-with-including-scripted-module-in-custom-slicer-based-application/43408

---

## Post #1 by @software (2025-06-18 14:02 UTC)

<p>Hi all,</p>
<p>I’ve developed a custom Slicer-based application and included a custom scripted module called <code>HemisphereVolumeCalculator</code><br>
In my top-level <code>CMakeLists.txt</code>, I’ve added it using:</p>
<pre data-code-wrap="cmake"><code class="lang-cmake">set(Slicer_EXTENSION_SOURCE_DIRS
  ${Safe_SOURCE_DIR}/Modules/Scripted/HemisphereVolumeCalculator
)
</code></pre>
<p>The module runs fine when I add its path through the <strong>application settings → Additional Module Paths</strong>. However, after building my application from the generated <code>Safe.sln</code> (on Windows), the module does <strong>not</strong> appear in the application interface by default.</p>
<h3><a name="p-126120-questions-1" class="anchor" href="#p-126120-questions-1" aria-label="Heading link"></a><img src="https://emoji.discourse-cdn.com/twitter/red_question_mark.png?v=15" title=":red_question_mark:" class="emoji" alt=":red_question_mark:" loading="lazy" width="20" height="20"> Questions:</h3>
<ol>
<li>Is there anything else I need to do beyond setting <code>Slicer_EXTENSION_SOURCE_DIRS</code> to ensure the module gets built and bundled?</li>
<li>How can I confirm whether the module was recognized or included during the build?</li>
<li>Are there any additional flags (e.g., <code>Slicer_QTSCRIPTEDMODULES_ENABLED</code>) that I need to set manually?</li>
</ol>

---

## Post #2 by @jcfr (2025-06-18 14:13 UTC)

<p>Does the folder <code>Modules/Scripted/HemisphereVolumeCalculator</code> contains a <code>CMakeLists</code> similar to <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate/blob/main/%7B%7Bcookiecutter.project_name%7D%7D/Modules/Scripted/Home/CMakeLists.txt">this one</a> ?</p>
<blockquote>
<ol start="2">
<li>How can I confirm whether the module was recognized or included during the build?</li>
</ol>
</blockquote>
<p>You should see the following output when the inner build is configured:</p>
<pre><code class="lang-auto">[...]
-- --------------------------------------------------
-- Configuring Safe application: SafeApp
-- --------------------------------------------------
...
-- --------------------------------------------------
-- Configuring extension directory: Home
-- Configuring Scripted module: Home
-- --------------------------------------------------
-- Configuring extension directory: HemisphereVolumeCalculator
-- Configuring Scripted module: HemisphereVolumeCalculator
[...]
</code></pre>
<blockquote>
<ol start="3">
<li>Are there any additional flags (e.g., <code>Slicer_QTSCRIPTEDMODULES_ENABLED</code>) that I need to set manually?</li>
</ol>
</blockquote>
<p>Those are related to the Slicer built-in scripted modules  and not the one you are explicitly developing as part of the custom app.</p>

---

## Post #3 by @software (2025-06-18 14:25 UTC)

<p>Thanks for the reply! Here’s how things are currently set up in my custom Slicer app.</p>
<p>This is the relevant part from the <strong>top-level CMakeLists.txt</strong> of my custom application (<code>Safe</code>):</p>
<pre data-code-wrap="cmake"><code class="lang-cmake"># Enable Slicer built-in modules
set(Slicer_CLIMODULES_ENABLED
  ResampleDTIVolume             # Needed by ResampleScalarVectorDWIVolume
  ResampleScalarVectorDWIVolume # Depends on DiffusionApplications, needed by CropVolume
)

set(Slicer_QTLOADABLEMODULES_ENABLED
)

set(Slicer_QTSCRIPTEDMODULES_ENABLED
)

# Disable Slicer built-in modules
set(Slicer_CLIMODULES_DISABLED
)

set(Slicer_QTLOADABLEMODULES_DISABLED
  SceneViews
  SlicerWelcome
  ViewControllers
)

set(Slicer_QTSCRIPTEDMODULES_DISABLED
  DataProbe
  DMRIInstall
  Endoscopy
  LabelStatistics
  PerformanceTests
  SampleData
  SurfaceToolbox
  VectorToScalarVolume
)

# Enable/Disable Slicer custom modules: To create a new module, use the SlicerExtensionWizard.
set(Slicer_EXTENSION_SOURCE_DIRS
  #${Safe_SOURCE_DIR}/Modules/CLI/MyCLIModule
  #${Safe_SOURCE_DIR}/Modules/Loadable/MyLoadableModule
  ${Safe_SOURCE_DIR}/Modules/Scripted/Home
  ${Safe_SOURCE_DIR}/Modules/Scripted/HemisphereVolumeCalculator
)
</code></pre>
<p>And this is the <code>CMakeLists.txt</code> inside the <code>HemisphereVolumeCalculator</code> module directory:</p>
<pre data-code-wrap="cmake"><code class="lang-cmake">#-----------------------------------------------------------------------------
set(MODULE_NAME HemisphereVolumeCalculator)

#-----------------------------------------------------------------------------
slicerMacroBuildScriptedModule(
  NAME ${MODULE_NAME}
  SCRIPTS ${MODULE_NAME}.py
  RESOURCES_DIR Resources/Icons
  WITH_GENERIC_TESTS
)
</code></pre>
<p>The module is placed correctly under the <code>Scripted</code> folder, and I’ve confirmed the paths are valid. But it’s still not showing up in the UI after building the application. Let me know if you see anything I’m missing!</p>

---

## Post #4 by @jcfr (2025-06-18 14:46 UTC)

<p>After re-configuring &amp; building the project from the top-level, the CMake cache variable <code>Slicer_EXTENSION_SOURCE_DIRS</code> set in the inner-build <code>CMakeCache.txt</code> (see <code>&lt;top-level&gt;/Slicer-build/CMakeCache.txt</code>) should include the path <code>/path/to/Modules/Scripted/HemisphereVolumeCalculator</code>.</p>
<p>Could you check this is the case ?</p>
<p>Next, can you check that:</p>
<ul>
<li>The text <code>Configuring Scripted module: HemisphereVolumeCalculator</code> is displayed when configuring the inner project</li>
<li>The relevant module files are copied when you force rebuild only the target <code>CopySlicerPythonScriptFiles</code> after opening the solution file found in the inner build directory</li>
</ul>

---

## Post #5 by @software (2025-06-19 08:28 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a><br>
Thanks! I just updated the module’s <code>CMakeLists.txt</code> according to the one you shared, and after rebuilding, the module now appears in the application<br>
<strong>Before Update:</strong></p>
<pre data-code-wrap="cmake"><code class="lang-cmake">#-----------------------------------------------------------------------------
set(MODULE_NAME HemisphereVolumeCalculator)

#-----------------------------------------------------------------------------
slicerMacroBuildScriptedModule(
  NAME ${MODULE_NAME}
  SCRIPTS ${MODULE_NAME}.py
  RESOURCES_DIR Resources/Icons
  WITH_GENERIC_TESTS
)
</code></pre>
<p><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> <strong>After Update:</strong></p>
<pre data-code-wrap="cmake"><code class="lang-cmake">#-----------------------------------------------------------------------------
set(MODULE_NAME HemisphereVolumeCalculator)

#-----------------------------------------------------------------------------
set(MODULE_PYTHON_SCRIPTS
  ${MODULE_NAME}.py
)

#-----------------------------------------------------------------------------
set(MODULE_PYTHON_RESOURCES
  Resources/Icons/${MODULE_NAME}.png
)

#-----------------------------------------------------------------------------
slicerMacroBuildScriptedModule(
  NAME ${MODULE_NAME}
  SCRIPTS ${MODULE_PYTHON_SCRIPTS}
  RESOURCES ${MODULE_PYTHON_RESOURCES}
)
</code></pre>

---

## Post #7 by @jcfr (2025-06-19 14:54 UTC)

<p>For future reference, note that the <code>RESOURCES_DIR</code> is not a valid argument for the <code>slicerMacroBuildScriptedModule</code>  CMake macro.</p>

---

## Post #8 by @software (2025-06-20 07:49 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a><br>
Okay sir, I see the custom module appears correctly in the application after each build. However, I’m getting an error every time, even though the module is properly packaged.<br>
Could you please advise what might be causing this issue or how I can debug it?</p>
<p>Thank you!<br>
Custom build for ‘E:\Safe\build\CMakeFiles\467e983c5e5c61d75f97be2c5e12c91e\Slicer-mkdir.rule;E:\Safe\build\CMakeFiles\467e983c5e5c61d75f97be2c5e12c91e\Slicer-download.rule;E:\Safe\build\CMakeFiles\467e983c5e5c61d75f97be2c5e12c91e\Slicer-update.rule;E:\Safe\build\CMakeFiles\467e983c5e5c61d75f97be2c5e12c91e\Slicer-patch.rule;E:\Safe\build\CMakeFiles\467e983c5e5c61d75f97be2c5e12c91e\Slicer-configure.rule;E:\Safe\build\CMakeFiles\467e983c5e5c61d75f97be2c5e12c91e\Slicer-build.rule;E:\Safe\build\CMakeFiles\467e983c5e5c61d75f97be2c5e12c91e\Slicer-forceconfigure.rule;E:\Safe\build\CMakeFiles\467e983c5e5c61d75f97be2c5e12c91e\Slicer-install.rule;E:\Safe\build\CMakeFiles\a4776f2d8ebb7610c206d34e471bef41\Slicer-complete.rule;E:\Safe\build\CMakeFiles\aa031ac59c12a6e617a2dfdd12069198\Slicer.rule;E:\Safe\build\slicersources-src\CMakeLists.txt’ exited with code 1.</p>

---
