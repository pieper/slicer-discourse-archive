---
topic_id: 11528
title: "Extension Manager Index Update Timeline"
date: 2020-05-13
url: https://discourse.slicer.org/t/11528
---

# Extension manager index update timeline

**Topic ID**: 11528
**Date**: 2020-05-13
**URL**: https://discourse.slicer.org/t/extension-manager-index-update-timeline/11528

---

## Post #1 by @evan (2020-05-13 20:46 UTC)

<p>After submitting an extension to the Slicer Extension Index via pull request and having that pull request accepted and merged, what is the procedure or general timeframe until that extension will be publicly available on the Slicer Extension Manager?</p>
<p>I have been making sure to check <a href="http://slicer.kitware.com/midas3/slicerappstore" rel="nofollow noopener">the Kitware Slicer Appstore</a>.</p>

---

## Post #2 by @Sam_Horvath (2020-05-13 21:10 UTC)

<p>Once the pull request has been merged, it should be built with the next nightly build.  If it is not showing up in the extension manager, you should check the build dashboard to see if there are errors:</p>
<p>Example: <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=MarkupsToModel" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=MarkupsToModel</a></p>

---

## Post #3 by @Sam_Horvath (2020-05-13 21:22 UTC)

<p>For your extension, here is the error log:<br>
<a href="http://slicer.cdash.org/viewConfigure.php?buildid=1910888" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/viewConfigure.php?buildid=1910888</a></p>
<p>You should remove this line:<br>
</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Auditory-Biophysics-Lab/SlicerBoneThicknessMappingExtension/blob/fb1ed304c02e97ff0d008994aea25dade6ac9e9b/BoneThicknessMapping/CMakeLists.txt#L29" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Auditory-Biophysics-Lab/SlicerBoneThicknessMappingExtension/blob/fb1ed304c02e97ff0d008994aea25dade6ac9e9b/BoneThicknessMapping/CMakeLists.txt#L29" target="_blank" rel="nofollow noopener">Auditory-Biophysics-Lab/SlicerBoneThicknessMappingExtension/blob/fb1ed304c02e97ff0d008994aea25dade6ac9e9b/BoneThicknessMapping/CMakeLists.txt#L29</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="19" style="counter-reset: li-counter 18 ;">
<li>  )</li>
<li>
</li><li>#-----------------------------------------------------------------------------</li>
<li>if(BUILD_TESTING)</li>
<li>
</li><li>  # Register the unittest subclass in the main script as a ctest.</li>
<li>  # Note that the test will also be available at runtime.</li>
<li>  slicer_add_python_unittest(SCRIPT ${MODULE_NAME}.py)</li>
<li>
</li><li>  # Additional build-time testing</li>
<li class="selected">  add_subdirectory(Testing)</li>
<li>endif()</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>since you do not have a testing directory</p>

---

## Post #4 by @evan (2020-05-14 21:28 UTC)

<p>Hi Sam, thanks for the information and especially for looking into my extension! I really appreciate it. I’ve fixed that CMakeList line so fingers crossed for the next nightly!</p>

---
