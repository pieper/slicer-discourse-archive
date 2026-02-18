# Version is different ? soure VS download

**Topic ID**: 23638
**Date**: 2022-05-30
**URL**: https://discourse.slicer.org/t/version-is-different-soure-vs-download/23638

---

## Post #1 by @janus_zhu (2022-05-30 08:14 UTC)

<p>Version up to current time(2022-05-30)</p>
<p>1.Git soure is:<br>
set(Slicer_REVISION “<strong>30876</strong>”)</p>
<p>2.Download url(<a href="https://download.slicer.org/" rel="noopener nofollow ugc">https://download.slicer.org/</a>) version is  <strong>30976</strong></p>
<p>3.When make:</p>
<pre><code class="lang-auto">[...]
Configuring Slicer requires admin account [OFF]
Configuring Slicer install root [$LOCALAPPDATA/NA-MIC]
Configuring Slicer release type [Experimental]
Configuring Slicer version [5.1.0-2022-05-29]
Configuring Slicer revision [30876]
Configuring VTK
Slicer_VTK_RENDERING_BACKEND is OpenGL2
Slicer_VTK_SMP_IMPLEMENTATION_TYPE is TBB
Slicer_VTK_VERSION_MAJOR is 9
Configuring Slicer with Qt 5.15.2 (using modules: Core, Widgets, Network, OpenGL, PrintSupport, UiTools, Xml, XmlPatterns, Svg, Sql, Multimedia, MultimediaWidgets, WebEngine, WebEngineWidgets, WebChannel, Script, LinguistTools, Test, )
[...]
</code></pre>

---

## Post #2 by @jcfr (2022-05-30 17:06 UTC)

<p>Following <a href="https://github.com/Slicer/Slicer/commit/813b9215fcf40fe4c4299598c20695a07ba4fdd2">Slicer@813b9215f</a>  of  <code>2022-04-30</code>, we allocated 100 commits for the maintenance of the 5.0 release.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/813b9215fcf40fe4c4299598c20695a07ba4fdd2/CMakeLists.txt#L310-L316">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/813b9215fcf40fe4c4299598c20695a07ba4fdd2/CMakeLists.txt#L310-L316" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/813b9215fcf40fe4c4299598c20695a07ba4fdd2/CMakeLists.txt#L310-L316" target="_blank" rel="noopener">Slicer/Slicer/blob/813b9215fcf40fe4c4299598c20695a07ba4fdd2/CMakeLists.txt#L310-L316</a></h4>



    <pre class="onebox">      <code class="lang-txt">
        <ol class="start lines" start="310" style="counter-reset: li-counter 309 ;">
            <li>set(_commit_count_offsets</li>
            <li>  # Value is chosen to provide continuity of revisions when switching from SVN to git</li>
            <li>  # at SVN revision=28825 / git hash 47deb76d7556e40de4e25e585c4b24a63a153da5 in official Slicer repository</li>
            <li>  # (https://github.com/Slicer/Slicer.git).</li>
            <li>  "3037"</li>
            <li>  # Allocate revisions for patch releases between v5.0.0 and v5.1.0</li>
            <li>  "100"</li>
        </ol>
      </code>
    </pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>This explains the difference of the computed revision before and after this commit.</p>

---
