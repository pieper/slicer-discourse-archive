# Update of server hosting slicer SVN repository

**Topic ID**: 939
**Date**: 2017-08-24
**URL**: https://discourse.slicer.org/t/update-of-server-hosting-slicer-svn-repository/939

---

## Post #1 by @jcfr (2017-08-24 18:22 UTC)

<p>Hi Slicers,</p>
<p><code>svn.slicer.org</code> is running Debian 6, which has gone end of life which means it has no access to security updates.</p>
<p>Kitware Sysadmin team will migrate the server on Tuesday August 29th at 3pm, it should take around 30mins.</p>
<p>During that time, few things will not work:</p>
<ul>
<li><code>git svn dcommit</code></li>
<li>building Slicer from source (indeed, few project (e.g EMSegment) are still checkout from svn)</li>
</ul>
<p>Note also that the associated mysql database running supporting viewvc (and phpmyadmin) will be migrated too.</p>
<p>Here it the list of impacted servers:</p>
<pre><code class="lang-auto">svn.slicer.org
viewvc.slicer.org
svn.na-mic.org
viewvc.na-mic.org
</code></pre>

---

## Post #2 by @pieper (2017-08-24 19:14 UTC)

<p>Thanks for doing this.</p>

---

## Post #3 by @jcfr (2017-08-29 19:15 UTC)

<p>The Kitware team is currently working on upgrading the server.</p>
<p>Cc: <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/fedorov">@fedorov</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #4 by @jcfr (2017-08-29 19:56 UTC)

<p>The migration has been successfully completed.</p>
<p>You can now access <a href="http://viewvc.slicer.org/">http://viewvc.slicer.org/</a>, commit using <code>git svn dcommit</code> and also build Slicer.</p>
<p>You will notice a slight difference in the viewvc UI, this is normal.</p>

---

## Post #5 by @jcfr (2017-08-29 20:01 UTC)

<p>As a side note, we noticed that <a href="http://svn.slicer.org/">http://svn.slicer.org/</a> reports “It works” instead of listing the branches as it is done for <a href="https://subversion.assembla.com/svn/slicerrt/">SlicerRT</a> svn.</p>
<p>This should be addressed shortly.</p>

---

## Post #6 by @jcfr (2017-08-29 20:06 UTC)

<p>Also we are working to make sure <a href="http://viewvc.na-mic.org">http://viewvc.na-mic.org</a> redirects to the expected server. Thanks for your patience.</p>

---

## Post #7 by @jcfr (2017-08-29 21:07 UTC)

<p>Et voila.</p>
<p>We are all set. HTML is now displayed on both <a href="http://svn.slicer.org">http://svn.slicer.org</a> and <a href="http://svn.na-mic.org">http://svn.na-mic.org</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/066d7165412b6f874bb63bec9ab0bbffcba3f840.png" alt="slicer-svn-html" data-base62-sha1="URlpcawDHbcx15vnHWV9o4xala" width="677" height="138"></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3900a1db017f8f28aba13fabe7e860b544a5b963.png" data-download-href="/uploads/short-url/88gzmCsG2kmZeF4XarQejJtgKdl.png?dl=1" title="na-mic-html"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3900a1db017f8f28aba13fabe7e860b544a5b963.png" alt="na-mic-html" data-base62-sha1="88gzmCsG2kmZeF4XarQejJtgKdl" width="690" height="130" data-dominant-color="F7F6F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">na-mic-html</span><span class="informations">707×134 10.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><b>Note: </b>Typo <code>NA-MIC SVN Branches</code> → <code>NA-MIC SVN Repositories</code> should be fixed shortly</p>

---
