# Build fails on Linux : configuration incomplete

**Topic ID**: 10898
**Date**: 2020-03-29
**URL**: https://discourse.slicer.org/t/build-fails-on-linux-configuration-incomplete/10898

---

## Post #1 by @chir.set (2020-03-29 18:59 UTC)

<p>My weekly build fails today when configuring Slicer itself :</p>
<blockquote>
<p>– Setting CPACK_PACKAGE_INSTALL_DIRECTORY to ‘Slicer 4.11.0-2020-03-28’<br>
– Setting CPACK_PACKAGE_DESCRIPTION_FILE to ‘/home/arc/src/Slicer/README.txt’<br>
– Setting CPACK_RESOURCE_FILE_LICENSE to ‘/home/arc/src/Slicer/License.txt’<br>
– Setting CPACK_PACKAGE_DESCRIPTION_SUMMARY to ‘Medical Visualization and Processing Environment for Research’<br>
– Configuring incomplete, errors occurred!<br>
See also “/home/arc/src/Slicer-SuperBuild-clang/Slicer-build/CMakeFiles/CMakeOutput.log”.<br>
See also “/home/arc/src/Slicer-SuperBuild-clang/Slicer-build/CMakeFiles/CMakeError.log”.</p>
</blockquote>
<p>Please see CMakeError.log for <a href="https://pastebin.com/EgQfUPyr" rel="noopener nofollow ugc">gcc</a> and <a href="https://pastebin.com/uYxxTeVx" rel="noopener nofollow ugc">clang</a>.</p>
<p>Slicer is configured in empty superbuild directories as such :</p>
<blockquote>
<p>export CFLAGS=" -I/usr/include/tirpc"<br>
export CXXFLAGS=“-I/usr/include/tirpc”<br>
cmake -DSlicer_VTK_VERSION_MAJOR:INT=8 -DQt5_DIR:PATH=/usr/lib/cmake/Qt5 -DSlicer_USE_PYTHONQT_WITH_OPENSSL:BOOL=ON -DBUILD_TESTING:BOOL=OFF -DCMAKE_BUILD_TYPE:STRING=Release -DADDITIONAL_CXX_FLAGS:STRING=-I/usr/include/tirpc …/Slicer</p>
</blockquote>
<p>Please advise for a fix.</p>
<p>Regards.</p>

---

## Post #2 by @lassoan (2020-03-30 04:50 UTC)

<p>You can find the actual CMake error message further up (it starts with <code>CMake Error</code> and contains a description of the problem and a call stack). Information in CMakeError.log and CMakeOutput.log are generally useless (they are too low-level).</p>

---

## Post #3 by @chir.set (2020-03-30 07:42 UTC)

<p>The only CMake Error I could find is :</p>
<blockquote>
<p>CMake Error at Libs/CMakeLists.txt:105 (add_subdirectory):<br>
The source directory</p>
<pre><code>/home/arc/src/Slicer-SuperBuild/vtkAddon
</code></pre>
<p>does not contain a CMakeLists.txt file.</p>
</blockquote>
<p>In effect, Slicer-SuperBuild/vtkAddon is empty.</p>
<p>Using cmake version 3.16.5.</p>

---

## Post #4 by @cpinter (2020-03-30 08:03 UTC)

<p>You just need to start the superbuild one more time and it will complete successfully. Here’s the ticket to track it</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/4774" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/4774" target="_blank">Ensure remote project source download  always complete before inner build starts</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-26" data-time="15:30:15" data-timezone="UTC">03:30PM - 26 Mar 20 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/jcfr" target="_blank">
          <img alt="jcfr" src="https://avatars0.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">It looks like the external project in charge of downloading the source doesn't depend on the Slicer inner build project
 
...</p>
</div>

<div class="labels">
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">priority:medium</span>
    <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">type:bug</span>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>By the way since this is not yet fixed, I wonder why the factory builds do not fail.</p>

---

## Post #5 by @chir.set (2020-03-30 14:59 UTC)

<p>Yes, it does build when issuing make again.<br>
Thanks.</p>

---
