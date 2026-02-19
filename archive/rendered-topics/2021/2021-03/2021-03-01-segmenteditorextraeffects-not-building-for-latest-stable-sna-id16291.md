---
topic_id: 16291
title: "Segmenteditorextraeffects Not Building For Latest Stable Sna"
date: 2021-03-01
url: https://discourse.slicer.org/t/16291
---

# SegmentEditorExtraEffects not building for latest stable snapshot

**Topic ID**: 16291
**Date**: 2021-03-01
**URL**: https://discourse.slicer.org/t/segmenteditorextraeffects-not-building-for-latest-stable-snapshot/16291

---

## Post #1 by @muratmaga (2021-03-01 17:11 UTC)

<p>An error about MaskVolume:<br>
<a href="https://slicer.cdash.org/build/2166922/configure" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.cdash.org/build/2166922/configure</a></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #2 by @jamesobutler (2021-03-01 17:20 UTC)

<p>Hopefully there are not more instances of this due to the new snapshot being called <code>4.11.20210226</code> instead of <code>4.13.20210226</code></p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/CMakeLists.txt#L42-L45" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/CMakeLists.txt#L42-L45" target="_blank" rel="noopener nofollow ugc">lassoan/SlicerSegmentEditorExtraEffects/blob/master/CMakeLists.txt#L42-L45</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="42" style="counter-reset: li-counter 41 ;">
<li>IF (Slicer_VERSION VERSION_LESS 4.13)</li>
<li>  # Slicer 4.13 and above has Mask volume effect built in</li>
<li>  add_subdirectory(MaskVolume)</li>
<li>ENDIF()</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @lassoan (2021-03-01 17:25 UTC)

<p>I’ve pushed a <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/commit/dc1470d8cc4de37a8ffab97484c74e8425d5ec78">fix</a>.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Calling the snapshot release Slicer-4.11.x may be more trouble than I though after all. For example, I’ve now updated the extension to work with 4.11 snapshot, but this means that the extension will not work with the 4.11 branch. To avoid confusion and more chances for errors, it would be probably better to either backport all the changes to the <a href="https://github.com/Slicer/Slicer/commits/v4.11">4.11</a> branch or change the snapshot version to Slicer-4.13.x.</p>

---

## Post #4 by @jcfr (2021-03-01 17:34 UTC)

<p>To support calling the snapshot release <code>4.13.YYYYMMDD</code> while we actively develop <code>4.13</code> version, we would need to have daily update of the variable <code>Slicer_VERSION_PATCH</code> to be set to the date of the day.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/4ec6541a620aa24559f70c65d363c1da3682902a/CMakeLists.txt#L49" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/4ec6541a620aa24559f70c65d363c1da3682902a/CMakeLists.txt#L49" target="_blank" rel="noopener">Slicer/Slicer/blob/4ec6541a620aa24559f70c65d363c1da3682902a/CMakeLists.txt#L49</a></h4>
<pre class="onebox"><code class="lang-txt"><ol class="start lines" start="39" style="counter-reset: li-counter 38 ;">
<li>endif()</li>
<li>
<li>#-----------------------------------------------------------------------------</li>
<li>if(NOT DEFINED Slicer_VERSION_MAJOR)</li>
<li>  set(Slicer_VERSION_MAJOR "4")</li>
<li>endif()</li>
<li>if(NOT DEFINED Slicer_VERSION_MINOR)</li>
<li>  set(Slicer_VERSION_MINOR "13")</li>
<li>endif()</li>
<li>if(NOT DEFINED Slicer_VERSION_PATCH)</li>
<li class="selected">  set(Slicer_VERSION_PATCH "0")</li>
<li>endif()</li>
<li>project(Slicer VERSION "${Slicer_VERSION_MAJOR}.${Slicer_VERSION_MINOR}.${Slicer_VERSION_PATCH}")</li>
<li>
<li>#-----------------------------------------------------------------------------</li>
<li># Update CMake module path</li>
<li>#------------------------------------------------------------------------------</li>
<li>set(CMAKE_MODULE_PATH</li>
<li>  ${Slicer_SOURCE_DIR}/Extensions/CMake</li>
<li>  ${CMAKE_MODULE_PATH}</li>
<li>  )</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>In the meantime, I suggest doing the following:</p>
<pre><code class="lang-auto">if (Slicer_VERSION VERSION_LESS 4.13 AND NOT Slicer_VERSION EQUAL "4.11.20210226")
</code></pre>

---

## Post #5 by @jcfr (2021-03-01 17:37 UTC)

<p>Or</p>
<pre><code class="lang-auto">if (Slicer_VERSION VERSION_LESS "4.11.20210226")
</code></pre>

---

## Post #6 by @lassoan (2021-03-01 17:53 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="4" data-topic="16291">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>To support calling the snapshot release <code>4.13.YYYYMMDD</code> while we actively develop <code>4.13</code> version, we would need to have daily update of the variable <code>Slicer_VERSION_PATCH</code> to be set to the date of the day.</p>
</blockquote>
</aside>
<p>Or, we can switch the master branch version to 4.15.</p>
<aside class="quote no-group" data-username="jcfr" data-post="5" data-topic="16291" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Or</p>
<pre><code class="lang-auto">if (Slicer_VERSION VERSION_LESS "4.11.20210226")
</code></pre>
</blockquote>
</aside>
<p>Yes, we can always handcraft version checks to fix the problems, but version checks already make the code more complicated, and it is hard to ensure they work well, especially for extensions.</p>
<p>If we keep 4.11 as snapshot version then I think it would be more appropriate to merge all the 4.11 snapshot contents into the 4.11 branch.</p>

---
