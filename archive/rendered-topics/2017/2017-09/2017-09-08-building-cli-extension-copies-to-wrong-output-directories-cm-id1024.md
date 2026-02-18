# Building CLI Extension copies to wrong output directories (cmake issue)

**Topic ID**: 1024
**Date**: 2017-09-08
**URL**: https://discourse.slicer.org/t/building-cli-extension-copies-to-wrong-output-directories-cmake-issue/1024

---

## Post #1 by @mschwier (2017-09-08 21:01 UTC)

<p>I hope I might find some help here. I recently started working on the PkModeling extension an I am trying to get it to build on various continuous integration platforms (Appveyor for Win and Travis CI for Linux and Mac).</p>
<p><a href="https://github.com/michaelschwier/PkModeling/tree/CI" class="onebox" target="_blank" rel="nofollow noopener">https://github.com/michaelschwier/PkModeling/tree/CI</a></p>
<p>I got the build working on Appveyor but it copies some of the generated files to the wrong output. So the expected output would be “[pkmodeling-build]/bin/Release” (expected files there are: PkModeling.exe, PkModelingLib.dll, PkModelingTest.exe, PkSolver.lib, PkModeling.xml). This works fine when I also build all the dependencies (ITK, DCMTK, ZLIB). However, to avoid building these dependencies on the CI platform I download them pre-built and then tell cmake to use those instead of building them again:</p>
<pre><code>cmake -G "Visual Studio 12 2013 Win64" -DITK_DIR:PATH=C:\ITK-install\lib\cmake\ITK-4.10 -DSlicerExecutionModel_DIR:PATH=C:\SlicerExecutionModel\SlicerExecutionModel-build -DDCMTK_DIR:PATH=C:\DCMTK-install\cmake -DZLIB_ROOT:PATH=c:\zlib-install -DZLIB_INCLUDE_DIR:PATH=c:\zlib-install\include -DZLIB_LIBRARY:FILEPATH=c:\zlib-install\lib\zlib.lib c:\pkmodeling
</code></pre>
<p>And now suddenly the files “PkModeling.exe” and “PkModelingLib.dll” are going to “[pkmodeling-build]/CLI/bin/Release” and the XML is going nowhere <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=9" title=":confused:" class="emoji" alt=":confused:"> The output directories are defined around line 120 in the main CMakeLists.txt. But I think the SEMMacroBuildCLI from Slicer Execution Model is also setting output dirs. However I can’t seem to figure out why the little difference in calling cmake causes this behavior.</p>
<p>I fixed this with a hack in the appveyor.yml by copying the files via cmd, so that the test can run. But this does not seem like the right way <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>

---

## Post #2 by @jcfr (2017-09-08 21:33 UTC)

<p>Nice work adding support for CI <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=15" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>You will find below some more details to help you make progress</p>
<blockquote>
<p>the XML is going nowhere</p>
</blockquote>
<p>That is strange, here is the code taking care of this:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerExecutionModel/blob/fa5f22e6346f8115381c1a242c4c50afe0ee8a50/CMake/SEMMacroBuildCLI.cmake#L203-L209">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerExecutionModel/blob/fa5f22e6346f8115381c1a242c4c50afe0ee8a50/CMake/SEMMacroBuildCLI.cmake#L203-L209" target="_blank" rel="noopener">github.com/Slicer/SlicerExecutionModel</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerExecutionModel/blob/fa5f22e6346f8115381c1a242c4c50afe0ee8a50/CMake/SEMMacroBuildCLI.cmake#L203-L209" target="_blank" rel="noopener">CMake/SEMMacroBuildCLI.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/SlicerExecutionModel/blob/fa5f22e6346f8115381c1a242c4c50afe0ee8a50/CMake/SEMMacroBuildCLI.cmake#L203-L209" rel="noopener"><code>fa5f22e63</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="203" style="counter-reset: li-counter 202 ;">
          <li>get_filename_component(cli_xml_filename ${cli_xml_file} NAME)</li>
          <li>add_custom_command(TARGET ${CLP} POST_BUILD</li>
          <li>  COMMAND ${CMAKE_COMMAND} -E copy_if_different</li>
          <li>    ${cli_xml_file}</li>
          <li>    ${LOCAL_SEM_RUNTIME_OUTPUT_DIRECTORY}/${CMAKE_CFG_INTDIR}/${cli_xml_filename}</li>
          <li>  COMMENT "Copying XML file '${cli_xml_filename}' along side the executable"</li>
          <li>  )</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<h3><a name="p-4223-details-about-handling-of-_output_directory-and-install__destination-1" class="anchor" href="#p-4223-details-about-handling-of-_output_directory-and-install__destination-1" aria-label="Heading link"></a>Details about handling of <code>*_OUTPUT_DIRECTORY</code> and <code>INSTALL_*_DESTINATION</code></h3>
<p>When building against SlicerExecutionModel, by default the output_dirs and install_dirs are the one used to configure/build  SlicerExecutionModel specifying variables like:</p>
<ul>
<li><code>SlicerExecutionModel_DEFAULT_CLI_${type}_OUTPUT_DIRECTORY</code></li>
<li><code>SlicerExecutionModel_DEFAULT_CLI_INSTALL_${type}_DESTINATION</code></li>
</ul>
<p>with <code>${type}</code> being any of <code>RUNTIME</code>,  <code>LIBRARY</code>  or <code>ARCHIVE</code>,</p>
<p>If for some reason, the default install and output dirs used to configure SlicerExecutionModel are not satisfactory. These can be globally overridden in the project by setting these variables before calling the macro:</p>
<ul>
<li><code>SlicerExecutionModel_CLI_${type}_OUTPUT_DIRECTORY</code></li>
<li><code>SlicerExecutionModel_CLI_INSTALL_${type}_DESTINATION</code></li>
</ul>
<p>Last, these can also be overridden on a per CLI basis by passing parameters to the macro:</p>
<ul>
<li><code>${type}_OUTPUT_DIRECTORY</code></li>
<li><code>INSTALL_${type}_DESTINATION</code></li>
</ul>
<p>The logic can be found here for output dir:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerExecutionModel/blob/fa5f22e6346f8115381c1a242c4c50afe0ee8a50/CMake/SEMMacroBuildCLI.cmake#L182-L194">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerExecutionModel/blob/fa5f22e6346f8115381c1a242c4c50afe0ee8a50/CMake/SEMMacroBuildCLI.cmake#L182-L194" target="_blank" rel="noopener">github.com/Slicer/SlicerExecutionModel</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerExecutionModel/blob/fa5f22e6346f8115381c1a242c4c50afe0ee8a50/CMake/SEMMacroBuildCLI.cmake#L182-L194" target="_blank" rel="noopener">CMake/SEMMacroBuildCLI.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/SlicerExecutionModel/blob/fa5f22e6346f8115381c1a242c4c50afe0ee8a50/CMake/SEMMacroBuildCLI.cmake#L182-L194" rel="noopener"><code>fa5f22e63</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="182" style="counter-reset: li-counter 181 ;">
          <li># Define default Output directories if it applies</li>
          <li>foreach(type RUNTIME LIBRARY ARCHIVE)</li>
          <li>  if(NOT DEFINED LOCAL_SEM_${type}_OUTPUT_DIRECTORY)</li>
          <li>    if(NOT DEFINED SlicerExecutionModel_CLI_${type}_OUTPUT_DIRECTORY)</li>
          <li>      set(LOCAL_SEM_${type}_OUTPUT_DIRECTORY ${SlicerExecutionModel_DEFAULT_CLI_${type}_OUTPUT_DIRECTORY})</li>
          <li>    else()</li>
          <li>      set(LOCAL_SEM_${type}_OUTPUT_DIRECTORY ${SlicerExecutionModel_CLI_${type}_OUTPUT_DIRECTORY})</li>
          <li>    endif()</li>
          <li>    if(LOCAL_SEM_VERBOSE)</li>
          <li>      message(STATUS "Defaulting ${type}_OUTPUT_DIRECTORY to ${LOCAL_SEM_${type}_OUTPUT_DIRECTORY}")</li>
          <li>    endif()</li>
          <li>  endif()</li>
          <li>endforeach()</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>and here for install destination:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/SlicerExecutionModel/blob/fa5f22e6346f8115381c1a242c4c50afe0ee8a50/CMake/SEMMacroBuildCLI.cmake#L212-L223">
  <header class="source">

      <a href="https://github.com/Slicer/SlicerExecutionModel/blob/fa5f22e6346f8115381c1a242c4c50afe0ee8a50/CMake/SEMMacroBuildCLI.cmake#L212-L223" target="_blank" rel="noopener">github.com/Slicer/SlicerExecutionModel</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerExecutionModel/blob/fa5f22e6346f8115381c1a242c4c50afe0ee8a50/CMake/SEMMacroBuildCLI.cmake#L212-L223" target="_blank" rel="noopener">CMake/SEMMacroBuildCLI.cmake</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/SlicerExecutionModel/blob/fa5f22e6346f8115381c1a242c4c50afe0ee8a50/CMake/SEMMacroBuildCLI.cmake#L212-L223" rel="noopener"><code>fa5f22e63</code></a>
</div>



    <pre class="onebox"><code class="lang-cmake">
      <ol class="start lines" start="212" style="counter-reset: li-counter 211 ;">
          <li># Define default install destination if it applies</li>
          <li>foreach(type RUNTIME LIBRARY ARCHIVE)</li>
          <li>  if(NOT DEFINED LOCAL_SEM_INSTALL_${type}_DESTINATION)</li>
          <li>    if(NOT DEFINED SlicerExecutionModel_CLI_INSTALL_${type}_DESTINATION)</li>
          <li>      set(LOCAL_SEM_INSTALL_${type}_DESTINATION ${SlicerExecutionModel_DEFAULT_CLI_INSTALL_${type}_DESTINATION})</li>
          <li>    else()</li>
          <li>      set(LOCAL_SEM_INSTALL_${type}_DESTINATION ${SlicerExecutionModel_CLI_INSTALL_${type}_DESTINATION})</li>
          <li>    endif()</li>
          <li>    if(LOCAL_SEM_VERBOSE)</li>
          <li>      message(STATUS "Defaulting INSTALL_${type}_DESTINATION to ${LOCAL_SEM_INSTALL_${type}_DESTINATION}")</li>
          <li>    endif()</li>
          <li>  endif()</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @mschwier (2017-09-08 22:41 UTC)

<p>Thanks, explicitly passing the output dirs to the macro helped with the libs and exes already. Now I’ll see about the xml.</p>

---

## Post #4 by @mschwier (2017-09-11 20:03 UTC)

<p>OK, found the problem with the XML copying: I was cloning a branch, which didn’t contain the code to copy the XML yet. <img src="https://emoji.discourse-cdn.com/twitter/roll_eyes.png?v=5" title=":roll_eyes:" class="emoji" alt=":roll_eyes:"></p>

---
