# Missing qt library references

**Topic ID**: 11816
**Date**: 2020-06-01
**URL**: https://discourse.slicer.org/t/missing-qt-library-references/11816

---

## Post #1 by @kayarre (2020-06-01 16:09 UTC)

<p>it appears the nightly linux build is expecting at qt library that isn’t there.</p>
<pre><code class="lang-auto">$ ./Slicer-4.11.0-2020-05-30-linux-amd64/Slicer
/tools/Slicer-4.11.0-2020-05-30-linux-amd64/bin/SlicerApp-real: error while loading shared libraries: libQt5QmlModels.so.5: cannot open shared object file: No such file or directory
</code></pre>

---

## Post #2 by @Sam_Horvath (2020-06-01 16:18 UTC)

<aside class="quote no-group" data-username="kayarre" data-post="1" data-topic="11816">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kayarre/48/3606_2.png" class="avatar"> kayarre:</div>
<blockquote>
<p><code>libQt5QmlModels</code></p>
</blockquote>
</aside>
<p>Looking into this, likely needs to be added to the CPack</p>

---
