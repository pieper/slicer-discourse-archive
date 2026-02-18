# Including header files (in an extension build)

**Topic ID**: 492
**Date**: 2017-06-13
**URL**: https://discourse.slicer.org/t/including-header-files-in-an-extension-build/492

---

## Post #1 by @lcoram (2017-06-13 15:03 UTC)

<p>Hi All,</p>
<p>I have an extension which contains two modules. One of these modules has a folder “ITKFilters” which contains .h and .hxx files. These don’t get built, but need to be linked. We used to recompile ITK with the filter inside, but we want to make the module/extension standalone - so you don’t need a modified version of ITK/Slicer. I can compile it by having the MODULE_INCLUDE_DIRECTORIES include the source folder (${CMAKE_CURRENT_SOURCE_DIR}/ITKFilters) when the extension is compiled outside Slicer. However, when I try to build the extension during the Slicer compilation (using Slicer_Remote_Add) the folder does not appear to be linked (I get an error about missing a .h file).</p>
<p>Slicer_Remote_Add(NorMIT-Plan<br>
GIT_REPOSITORY "${git_protocol}://github.com/TheInterventionCentre/NorMIT-Plan"<br>
GIT_TAG "90e7c84571f19bf7db65b5eb17e0c465278737f0"<br>
OPTION_NAME Slicer_BUILD_NorMIT-Plan<br>
LABELS REMOTE_MODULE<br>
)<br>
list_conditional_append(Slicer_BUILD_NorMIT-Plan Slicer_REMOTE_DEPENDENCIES NorMIT-Plan)</p>
<p>Is there something I am not understanding about how Slicer_Remote_Add works? Is there a way to get cmake to copy the folder over to the build, so I can link it from there?</p>
<p>Thanks for your help,</p>
<p>Louise</p>
<p>Operating system: OSX 10.10.5<br>
Slicer version: 4.6.0 - master</p>

---

## Post #2 by @lassoan (2017-06-13 15:13 UTC)

<p>To add more extensions to your Slicer build you just have to add paths of your extensions to the Slicer_EXTENSION_SOURCE_DIRS variable when you configure Slicer build. See detailed description of all Slicer build customization options (custom application name, startup message, included/excluded modules, etc.) here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#CONFIGURE_and_generate_Slicer_solution_files">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#CONFIGURE_and_generate_Slicer_solution_files</a>.</p>

---

## Post #3 by @lcoram (2017-06-13 15:35 UTC)

<p>I think maybe I was a bit misleading with the question. I had no problem using Slicer_Remote_Add when I only had folders in my module that contained cmake files (what was in the folders was compiled) but it no longer works once my module contains a folder with only .h/.hxx files, as something is different about how the cmake works when it is made / compiled inside Slicer vs made / compiled separately (linked to a Slicer build).</p>
<p>Andras - are you saying it will compile the way I expect it to if I use the extension_source_dirs instead of slicer_remote_add?</p>
<p>Thanks again,</p>
<p>Louise</p>

---

## Post #4 by @jcfr (2017-06-13 15:35 UTC)

<aside class="quote no-group" data-username="lcoram" data-post="1" data-topic="492">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/e79b87/48.png" class="avatar"> lcoram:</div>
<blockquote>
<p>One of these modules has a folder “ITKFilters” which contains .h and .hxx files. These don’t get built, but need to be linked. We used to recompile ITK with the filter inside, but we want to make the module/extension standalone - so you don’t need a modified version of ITK/Slicer.</p>
</blockquote>
</aside>
<p>If you have a custom ITK filter, you could make it is a proper “ITK remote module”. It will then be possible to compile it as an ITK module against an ITK build tree (that could be the one from Slicer or your own ITK build tree).</p>
<p>Here is an example of remote module: <a href="https://github.com/InsightSoftwareConsortium/ITKModuleTemplate" class="inline-onebox">GitHub - InsightSoftwareConsortium/ITKModuleTemplate: A template to start an ITK Module</a></p>

---

## Post #5 by @jcfr (2017-06-13 15:38 UTC)

<aside class="quote no-group" data-username="lcoram" data-post="3" data-topic="492">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/e79b87/48.png" class="avatar"> lcoram:</div>
<blockquote>
<p>Andras - are you saying it will compile the way I expect it to if I use the extension_source_dirs instead of slicer_remote_add?</p>
</blockquote>
</aside>
<p>The function <code>Slicer_Add_Remove</code> ultimately end up passing the extension source directory to Slicer as <code>Slicer_EXTENSION_SOURCE_DIRS</code>.</p>
<p>Reading the following comment may be helpful:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/CMakeLists.txt#L1012-L1038">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/CMakeLists.txt#L1012-L1038" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/CMakeLists.txt#L1012-L1038" target="_blank" rel="noopener">Slicer/Slicer/blob/main/CMakeLists.txt#L1012-L1038</a></h4>



    <pre class="onebox"><code class="lang-txt">
      <ol class="start lines" start="1012" style="counter-reset: li-counter 1011 ;">
          <li>  Utilities/Scripts/setupSlicerEnvironment.sh</li>
          <li>  )</li>
          <li>foreach(f ${files})</li>
          <li>  configure_file(</li>
          <li>    ${CMAKE_CURRENT_SOURCE_DIR}/${f}.in</li>
          <li>    ${CMAKE_CURRENT_BINARY_DIR}/${f}</li>
          <li>    )</li>
          <li>endforeach()</li>
          <li></li>
          <li>#-----------------------------------------------------------------------------</li>
          <li># Includes</li>
          <li>#-----------------------------------------------------------------------------</li>
          <li>include_directories(</li>
          <li>  ${CMAKE_CURRENT_SOURCE_DIR}/CMake</li>
          <li>  ${CMAKE_CURRENT_SOURCE_DIR}</li>
          <li>  ${CMAKE_CURRENT_BINARY_DIR}</li>
          <li>  )</li>
          <li></li>
          <li>#-----------------------------------------------------------------------------</li>
          <li># Subdirectories</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/main/CMakeLists.txt#L1012-L1038" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @lassoan (2017-06-13 15:40 UTC)

<aside class="quote no-group quote-modified" data-username="lcoram" data-post="1" data-topic="492">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/e79b87/48.png" class="avatar"> lcoram:</div>
<blockquote>
<p><a href="http://github.com/TheInterventionCentre/NorMIT-Plan" class="inline-onebox">GitHub - TheInterventionCentre/NorMIT-Plan</a></p>
</blockquote>
</aside>
<p>Everything should work well if you specify additional extensions through Slicer_EXTENSION_SOURCE_DIRS.</p>
<p>Can you share the source code? In <a href="http://github.com/TheInterventionCentre/NorMIT-Plan" class="inline-onebox">GitHub - TheInterventionCentre/NorMIT-Plan</a> I did not see any ITKFilters directory. Normally you put these files in the Logic directory. If you add them in subdirectories then make sure to add the directory to the list of include directories defined for that target.</p>

---

## Post #7 by @lcoram (2017-06-13 20:37 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="6" data-topic="492">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a href="http://github.com/TheInterventionCentre/NorMIT-Pla" rel="noopener nofollow ugc">github.com/TheInterventionCentre/NorMIT-Pla</a></p>
</blockquote>
</aside>
<p>Hi Andras and JC,</p>
<p>We were compiling the ITK filter as a remote filter (so it follows that convention), but we would like to create an extension that can be used with “vanilla” Slicer and not just with one where the ITK has been recompiled with the extra filter. I believe the most transparent way to do this for now is to package the filter along with the module. Or is there a different way of doing things?<br>
(Another way I had tried was to use ExternalProject_Add to get and insert the filter into ITK and then recompile ITK with the filter on)</p>
<p>The code is in Github, just on a branch called “vessel_segmentation_integration”, for the folder containing the filters check inside the VesselSegmentation folder:<br>
<a href="https://github.com/TheInterventionCentre/NorMIT-Plan/tree/feature/vessel_segmentation_integration" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/TheInterventionCentre/NorMIT-Plan/tree/feature/vessel_segmentation_integration</a></p>
<p>From what JC posted it looks like if I add the label remote_extension inside the slicer_remote_add, then it will add the extension source directories.<br>
LABELS REMOTE_EXTENSION</p>
<p>Thanks for your help as always,<br>
Louise</p>

---

## Post #8 by @lassoan (2017-06-13 22:31 UTC)

<p>If you want to make your ITK filters available for non-Slicer users then it is a good idea to distribute them as remote ITK modules (as far as I know, your extension can load additional remote ITK modules; you don’t need to change anything in the Slicer core build).</p>
<p>If you only plan to use those ITK filters in Slicer modules then put those files in the module Logic directory. Don’t create a new directory, as all algorithms are expected to be in the module Logic classes.</p>
<p>For your modules you must not use slicer_remote_add macro, as it would require changing Slicer source code. Instead, with specifying your custom extensions using cmake -DSlicer_EXTENSION_SOURCE_DIRS you can incorporate extensions into a custom Slicer build without making any modification in the Slicer source code.</p>
<p>Note that custom Slicer builds may not be compatible with Slicer extensions in the Extension manager (and depending on what Slicer version you build it from, extensions may not even show up in the Extension manager), so these custom builds are only useful for heavily customized, stripped-down versions of Slicer. If you create such custom build, it is strongly recommended to change the application name and other settings to distinguish it from regular Slicer builds.</p>

---
