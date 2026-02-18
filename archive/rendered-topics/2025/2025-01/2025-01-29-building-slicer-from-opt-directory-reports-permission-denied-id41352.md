# Building Slicer from /opt directory reports "permission denied" error

**Topic ID**: 41352
**Date**: 2025-01-29
**URL**: https://discourse.slicer.org/t/building-slicer-from-opt-directory-reports-permission-denied-error/41352

---

## Post #1 by @ferhue (2025-01-29 12:00 UTC)

<p>I am getting an error when compiling Slicer on Ubu22.04 (from git master, cloned on Jan24) but it is a bit cryptic. Could you let me know what could be happening?</p>
<p>After 3 hours of building, it ends with:</p>
<pre><code class="lang-auto">-- Setting CPACK_PACKAGE_NAME to 'Slicer'
-- Setting CPACK_PACKAGE_VENDOR to 'slicer.org'
-- Setting CPACK_PACKAGE_VERSION_MAJOR to '5'
-- Setting CPACK_PACKAGE_VERSION_MINOR to '9'
-- Setting CPACK_PACKAGE_VERSION_PATCH to '0'
-- Setting CPACK_PACKAGE_VERSION to '5.9.0-2025-01-28'
-- Setting CPACK_PACKAGE_INSTALL_DIRECTORY to 'Slicer 5.9.0-2025-01-28'
-- Setting CPACK_PACKAGE_DESCRIPTION_FILE to '/opt/Slicer_src/README.md'
-- Setting CPACK_RESOURCE_FILE_LICENSE to '/opt/Slicer_src/License.txt'
-- Setting CPACK_PACKAGE_DESCRIPTION_SUMMARY to 'Medical Visualization and Processing Environment for Research'
-- Configuring incomplete, errors occurred!
make[2]: *** [CMakeFiles/Slicer.dir/build.make:127: Slicer-prefix/src/Slicer-stamp/Slicer-configure] Error 1
make[1]: *** [CMakeFiles/Makefile2:1826: CMakeFiles/Slicer.dir/all] Error 2
make: *** [Makefile:91: all] Error 2
</code></pre>

---

## Post #2 by @jcfr (2025-01-29 12:03 UTC)

<p>Thanks for the report <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"></p>
<p>The actual error is likely reported earlier in the log, it would be great if you could scroll up to identify it <img src="https://emoji.discourse-cdn.com/twitter/ok_hand.png?v=12" title=":ok_hand:" class="emoji" alt=":ok_hand:" loading="lazy" width="20" height="20"></p>
<p>Once we understand the issue, we will consider adding additional checks earlier so that “root” problem is reported earlier.</p>

---

## Post #3 by @ferhue (2025-01-29 12:16 UTC)

<p>Thanks for the hint, I see this mid-wise in the build:</p>
<pre><code class="lang-auto">
CMake Error: Could not open file for write in copy operation /opt/Slicer_src/Utilities/Scripts/SlicerWizard/__version__.py.tmp
CMake Error: : System Error: Permission denied
CMake Error at Utilities/Scripts/SlicerWizard/CMakeLists.txt:12 (configure_file):
  configure_file Problem configuring file
</code></pre>

---

## Post #4 by @jcfr (2025-01-29 12:28 UTC)

<p>Thanks for looking this up! That’s helpful.</p>
<p>It looks like you’re building the project in the <code>/opt/</code> directory, which is likely owned by the <code>root</code> user. This is probably causing the error we’re seeing.</p>
<p>In this case, <code>__version__.py</code> needs to be configured within the source tree<sup class="footnote-ref"><a href="#footnote-121875-1" id="footnote-ref-121875-1">[1]</a></sup>, but it’s likely not writable in your setup.</p>
<p>To resolve this, you can:</p>
<ol>
<li>Build and develop from your home directory, or</li>
<li>Update the permissions for <code>/opt/Slicer_src</code>.</li>
</ol>
<p>Unless you have a specific reason to build in <code>/opt/</code>, I recommend option (1).</p>
<hr class="footnotes-sep">

<ol class="footnotes-list">
<li id="footnote-121875-1" class="footnote-item"><p><a href="https://github.com/Slicer/Slicer/blob/50c891821df013133a4de0c4e7e9ed514c17ae5e/Utilities/Scripts/SlicerWizard/CMakeLists.txt#L7-L16" class="inline-onebox">Slicer/Utilities/Scripts/SlicerWizard/CMakeLists.txt at 50c891821df013133a4de0c4e7e9ed514c17ae5e · Slicer/Slicer · GitHub</a> <a href="#footnote-ref-121875-1" class="footnote-backref">↩︎</a></p>
</li>
</ol>

---

## Post #5 by @ferhue (2025-01-29 12:48 UTC)

<p>Thanks a lot for the swift clarification!</p>
<p>As a suggestion, since it’s not overly common that the build dir interacts with the source dir, may I suggest the following (pseudocode) improvement in the main CMakeLists, to inform the user about the error more easily/quickly? So that error happens right away, not after x hours and in the middle of the log.</p>
<pre><code class="lang-auto">if(CMAKE_VERSION VERSION_GREATER "3.21.0") 
   file(COPY_FILE  ${CMAKE_SOURCE_DIR}/README.md ${CMAKE_SOURCE_DIR}/Utilities/Scripts/SlicerWizard/.tmp_txt RESULT result)
   if(NOT result)
      message(ERROR "You need write permissions in the source dir")
   endif()
endif()
</code></pre>
<p>Thanks again!</p>
<p>PS: This would also help with: <a href="https://discourse.slicer.org/t/variable-slicer-wc-last-changed-date-is-expected-to-be-defined/25389/9" class="inline-onebox">Variable Slicer_WC_LAST_CHANGED_DATE is expected to be defined - #9 by miniminic</a></p>

---

## Post #6 by @pieper (2025-01-29 13:40 UTC)

<p>I typically use /opt/s as a build directory on mac (need to create it first and change permissions with sudo).  Keeping the build directory short avoids path length errors.</p>

---
