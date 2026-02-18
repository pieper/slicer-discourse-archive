# Model to Model Distance 

**Topic ID**: 5324
**Date**: 2019-01-10
**URL**: https://discourse.slicer.org/t/model-to-model-distance/5324

---

## Post #1 by @emrobert (2019-01-10 02:07 UTC)

<p>Operating system: OS X MAC<br>
Slicer version: 4.8.1<br>
Expected behavior: I expected ShapePopulationViewer to show up under the Surface Models tab once I downloaded the Model to Model Distance extension module<br>
Actual behavior: I downloaded the extension successfully and I was able to create the color map but when I went under Surface Models there was no tab for ShapePopulationViewer and so I could not actually create the color map.</p>

---

## Post #2 by @lassoan (2019-01-10 02:11 UTC)

<p>Shape Population Viewer will show up if you download Shape Population Viewer extension. It may be also bundled in <a href="http://salt.slicer.org/" rel="nofollow noopener">SlicerSALT</a> installation packages.</p>
<p>Note that Slicer-4.8.1 is more than a year old. We only support latest stable (Slicer-4.10) version, and some fixes and features (such as example Shape Population Viewer) may only be available in latest nightly versions.</p>

---

## Post #3 by @emrobert (2019-01-10 16:49 UTC)

<p>Thank you for your help! I downloaded Slicer 10.0 and I still can’t find Shape Population Viewer as an extension. I can download it as a separate file but I can’t figure out how to get it to work with Slicer. I am able to download the MeshStats and ShapeQuantifier extensions but not shape population viewer and all I need to do is create a color map. Any suggestions are welcome! Thanks again!</p>

---

## Post #4 by @jamesobutler (2019-01-10 17:51 UTC)

<p>I can confirm that the ShapePopulationViewer extension is available for download from the Extension Wizard within today’s nightly Slicer 4.11.0-2019-01-07.</p>
<p>There is an error building the extension for Slicer 4.10 because it is looking for a branch that no longer exists. <a class="mention" href="/u/jcfr">@jcfr</a> I see in <a href="https://github.com/NIRALUser/ShapePopulationViewer/issues/33" rel="nofollow noopener">NIRALUser/ShapePopulationViewer #33</a> that you encouraged a change to this branch name. Do you know what tag can be used so that ShapePopulationViewer can work for Slicer 4.10 stable as well?</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/ExtensionsIndex/blob/4.10/ShapePopulationViewer.s4ext#L9-L10" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/ExtensionsIndex/blob/4.10/ShapePopulationViewer.s4ext#L9-L10" target="_blank" rel="nofollow noopener">Slicer/ExtensionsIndex/blob/4.10/ShapePopulationViewer.s4ext#L9-L10</a></h4>
<pre class="onebox"><code class="lang-s4ext"><ol class="start lines" start="9" style="counter-reset: li-counter 8 ;">
<li>scmurl git://github.com/NIRALUser/ShapePopulationViewer.git</li>
<li>scmrevision release</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/ExtensionsIndex/blob/master/ShapePopulationViewer.s4ext#L9-L10" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/ExtensionsIndex/blob/master/ShapePopulationViewer.s4ext#L9-L10" target="_blank" rel="nofollow noopener">Slicer/ExtensionsIndex/blob/master/ShapePopulationViewer.s4ext#L9-L10</a></h4>
<pre class="onebox"><code class="lang-s4ext"><ol class="start lines" start="9" style="counter-reset: li-counter 8 ;">
<li>scmurl git://github.com/jcfr/ShapePopulationViewer.git</li>
<li>scmrevision 8112d7b1253a94426b510a53779c20118e483c1a</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @jcfr (2019-01-10 18:11 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="4" data-topic="5324">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>There is an error building the extension for Slicer 4.10 because it is looking for a branch that no longer exists</p>
</blockquote>
</aside>
<p>This is now fixed in <a href="https://github.com/Slicer/ExtensionsIndex/commit/cb64e3349fd328692433884bf43e09806830e585" class="inline-onebox">Fix ShapePopulationViewer scmrevision · Slicer/ExtensionsIndex@cb64e33 · GitHub</a></p>

---
