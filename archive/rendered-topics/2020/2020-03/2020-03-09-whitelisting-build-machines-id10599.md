# Whitelisting build machines

**Topic ID**: 10599
**Date**: 2020-03-09
**URL**: https://discourse.slicer.org/t/whitelisting-build-machines/10599

---

## Post #1 by @adamrankin (2020-03-09 13:48 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a></p>
<p>Hey guys,</p>
<p>I’d like to move our extension repo to our own server (exceeded git-lfs limits on GitHub), but our servers aren’t public facing. If I wanted to whitelist the build machines (instead of just *.kitware.com), can I whitelist overload, metroplex, and factory-south-macos?</p>
<p>Thanks,<br>
Adam</p>
<p><em>Edit: are those the specific names (<a href="http://overload.kitware.com" rel="noopener nofollow ugc">overload.kitware.com</a>, <a href="http://metroplex.kitware.com" rel="noopener nofollow ugc">metroplex.kitware.com</a>, <a href="http://factory-south-macos.kitware.com" rel="noopener nofollow ugc">factory-south-macos.kitware.com</a>)?</em></p>

---

## Post #2 by @lassoan (2020-03-09 14:41 UTC)

<aside class="quote no-group" data-username="adamrankin" data-post="1" data-topic="10599">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/adamrankin/48/155_2.png" class="avatar"> adamrankin:</div>
<blockquote>
<p>I’d like to move our extension repo to our own server (exceeded git-lfs limits on GitHub)</p>
</blockquote>
</aside>
<p>How did you manage to exceed git-lfs limits (what kind of data you found useful to store in the repository that was too big)?</p>
<p>Did you find git-lfs a robust solution overall (when we evaluated it about a year ago I read lots of complaints about various errors that were hard to diagnose and clean up)?</p>
<p>Did you consider using CMake’s ExternalData infrastructure instead? It can work with almost any kind server, including github releases, which do not have any restriction on the amount of data you store there (this is how we host <a href="https://github.com/Slicer/SlicerTestingData/releases">SlicerTestingData</a>).</p>

---

## Post #3 by @adamrankin (2020-03-09 18:02 UTC)

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/VASST/SlicerVASST/blob/master/GuidedUSCal/Resources/Models/cnn_model_best.keras.h5" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/VASST/SlicerVASST/blob/master/GuidedUSCal/Resources/Models/cnn_model_best.keras.h5" target="_blank" rel="nofollow noopener">VASST/SlicerVASST/blob/master/GuidedUSCal/Resources/Models/cnn_model_best.keras.h5</a></h4>
<pre><code class="lang-h5">version https://git-lfs.github.com/spec/v1
oid sha256:263d55fa66729510db414714768d7efb703bc425c738dcbc89a1c11d3a9b0c66
size 32102256
</code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>So far, no issues at all except for exceeded data cap.</p>
<p>I have not tried the ExternalData infrastructure.</p>

---

## Post #4 by @lassoan (2020-03-09 19:12 UTC)

<p>Github releases would be good fit for storing CNN models.</p>
<p>You can download the files using <code>slicer.util.downloadFile</code> at runtime as needed. The file is automatically cached locally and re-downloaded only when needed. Correct download and consistency is checked using md5/sha sums.</p>
<p><a href="https://github.com/Slicer/SlicerTestingData/blob/master/process_release_data.py">process_release_data.py</a> utility script allows batch synchronization of all files between a local folder and a github repository in a way that the github release URLs can be used in CMake ExternalData (so CMake can download the files automatically at configuration time).</p>

---

## Post #5 by @Sam_Horvath (2020-03-09 21:58 UTC)

<p>Hi all:</p>
<p>Those are the names, don’t know if whitelisting them by name will work.  They are on our internal network.</p>
<p>Sam</p>

---
