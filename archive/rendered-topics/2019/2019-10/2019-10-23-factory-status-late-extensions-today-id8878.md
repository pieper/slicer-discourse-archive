---
topic_id: 8878
title: "Factory Status Late Extensions Today"
date: 2019-10-23
url: https://discourse.slicer.org/t/8878
---

# Factory status: Late extensions today

**Topic ID**: 8878
**Date**: 2019-10-23
**URL**: https://discourse.slicer.org/t/factory-status-late-extensions-today/8878

---

## Post #1 by @Sam_Horvath (2019-10-23 16:19 UTC)

<p>Extensions are running late for the most recent nightly build.  They should be up by this afternoon.</p>

---

## Post #2 by @adamrankin (2019-10-23 18:19 UTC)

<p>Any idea what’s going on with the repo conflict issue? It seems to be occurring often.</p>

---

## Post #3 by @Sam_Horvath (2019-10-23 18:22 UTC)

<p>One of the tests is using test data in the repo (a mrml scene) and it writing back to it.  I need to rewrite the test but haven’t had the time.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/d596340895ed6e54bc164a6715b3b030654129ee/Modules/CLI/ExecutionModelTour/ExecutionModelTour.cxx#L92" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/d596340895ed6e54bc164a6715b3b030654129ee/Modules/CLI/ExecutionModelTour/ExecutionModelTour.cxx#L92" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/d596340895ed6e54bc164a6715b3b030654129ee/Modules/CLI/ExecutionModelTour/ExecutionModelTour.cxx#L92</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="82" style="counter-reset: li-counter 81 ;">
<li>scene-&gt;Import();</li>
<li>
</li>
<li>vtkMRMLNode *node = scene-&gt;GetNodeByID( transform1ID );</li>
<li>if( node )</li>
<li>  {</li>
<li>  vtkMRMLNode *outNode = scene-&gt;GetNodeByID( transform2ID );</li>
<li>
</li>
<li>  if( outNode )</li>
<li>    {</li>
<li>    outNode-&gt;Copy( node );</li>
<li class="selected">    scene-&gt;Commit( transform2Filename.c_str() );</li>
<li>    }</li>
<li>  else</li>
<li>    {</li>
<li>    std::cerr &lt;&lt; "No output transform found! Specified transform ID = " &lt;&lt; transform2ID &lt;&lt; std::endl;</li>
<li>    return EXIT_FAILURE;</li>
<li>    }</li>
<li>  }</li>
<li>else</li>
<li>  {</li>
<li>  std::cerr &lt;&lt; "No input transform found! Specified transform ID = " &lt;&lt; transform1ID &lt;&lt; std::endl;</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/CLI/ExecutionModelTour/Testing/CMakeLists.txt" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/CLI/ExecutionModelTour/Testing/CMakeLists.txt" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/CLI/ExecutionModelTour/Testing/CMakeLists.txt</a></h4>
<pre><code class="lang-txt">
#-----------------------------------------------------------------------------
set(INPUT ${CMAKE_CURRENT_SOURCE_DIR}/../Data/Input)

set(CLP ${MODULE_NAME})

if(NOT DEFINED SEM_DATA_MANAGEMENT_TARGET)
  set(SEM_DATA_MANAGEMENT_TARGET ${CLP}Data)
endif()

#-----------------------------------------------------------------------------
add_executable(${CLP}Test ${CLP}Test.cxx)
add_dependencies(${CLP}Test ${CLP})
target_link_libraries(${CLP}Test ${CLP}Lib ${SlicerExecutionModel_EXTRA_EXECUTABLE_TARGET_LIBRARIES})
set_target_properties(${CLP}Test PROPERTIES LABELS ${CLP})
set_target_properties(${CLP}Test PROPERTIES FOLDER ${${CLP}_TARGETS_FOLDER})

set(testname ${CLP}Test)
ExternalData_add_test(${SEM_DATA_MANAGEMENT_TARGET}
  NAME ${testname} COMMAND ${SEM_LAUNCH_COMMAND} $&lt;TARGET_FILE:${CLP}Test&gt;
</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/master/Modules/CLI/ExecutionModelTour/Testing/CMakeLists.txt" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
