# Update: Slicer 4.10.1 patch release will be initiated tomorrow morning

**Topic ID**: 5367
**Date**: 2019-01-15
**URL**: https://discourse.slicer.org/t/update-slicer-4-10-1-patch-release-will-be-initiated-tomorrow-morning/5367

---

## Post #1 by @jcfr (2019-01-15 01:12 UTC)

<p>Now that remaining issues preventing the successful packaging of Qt designer with Slicer have been fixed, the Slicer patch release 4.10.1 will be created tomorrow morning. (read <a href="https://discourse.slicer.org/t/workflow-that-brings-together-a-few-modules-as-tabs-in-a-unifying-parent-module/5314/14">here</a> to understand the motivation)</p>
<p>The patch release will be based of the current master branch.</p>
<p>Thanks for your patience,</p>

---

## Post #2 by @lassoan (2019-01-15 04:57 UTC)

<p>I’ve tried an installed Slicer on Windows to generate scripteddesigner extension using Extension Wizard and edit its GUI using Qt Designer and it worked perfectly. Thanks a lot <a class="mention" href="/u/jcfr">@jcfr</a>!</p>

---

## Post #3 by @jcfr (2019-01-15 14:56 UTC)

<p>I also just confirmed <code>./bin/SlicerDesigner</code> work on macOS and Linux <img src="https://emoji.discourse-cdn.com/twitter/tada.png?v=6" title=":tada:" class="emoji" alt=":tada:"></p>

---

## Post #4 by @jcfr (2019-01-15 22:44 UTC)

<p>Update: Tonight regular build will most likely be disabled and the “build factories” will use that time to build the patch release.</p>

---

## Post #5 by @jcfr (2019-01-16 04:04 UTC)

<p>Update:</p>
<ul>
<li>patch release is being generated, you can track the progress looking at <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2019-01-16#Experimental-Packages" rel="nofollow noopener">CDash</a>
</li>
<li>git and svn repository have been tagged, see <a href="https://www.slicer.org/wiki/Release_Details#Slicer_4.10.1" rel="nofollow noopener">https://www.slicer.org/wiki/Release_Details#Slicer_4.10.1</a>
</li>
</ul>
<p>Notes:</p>
<ul>
<li>commits from master branch have been cherry-picked onto the Slicer-4-10 branch.</li>
</ul>

---

## Post #6 by @hjmjohnson (2019-01-16 14:36 UTC)

<p>Has the tagging been successful?  <a href="https://github.com/Slicer/Slicer/releases/tag/v4.10.1" rel="nofollow noopener">https://github.com/Slicer/Slicer/releases/tag/v4.10.1</a></p>
<p>Can the backlog of PR’s start to be addressed?</p>
<p>Thanks.</p>
<p>Hans</p>

---

## Post #7 by @jcfr (2019-01-16 14:53 UTC)

<p>We will indeed address the back log of PR shortly.</p>
<p>In the mean time here is an update:</p>
<ul>
<li>packages successfully generated on all platforms</li>
</ul>
<p>Next steps:</p>
<ul>
<li>sign and upload packages</li>
<li>remaining tasks listed in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/ReleaseProcess#Day_2:_Post_release" rel="nofollow noopener">Post release</a> guide.</li>
</ul>

---

## Post #8 by @jcfr (2019-01-16 18:19 UTC)

<p>Update:</p>
<ul>
<li>Windows package has been signed</li>
<li>Linux and Windows packages have been marked as 4.10.1 release</li>
</ul>
<p>Notes:</p>
<ul>
<li>macOS package will be signed only Friday. The hardware token holding the keys and used on the signing machine will only be available later in the week.</li>
<li>regular nightly build have been resumed and will be available tomorrow.</li>
</ul>
<p>Thanks for your patience,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3b0c208e42134b7ae81ee1b60bbe6e6691ded4a.png" data-download-href="/uploads/short-url/rV9O9ojHYwuE8C66hR2bnlz7VAm.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3b0c208e42134b7ae81ee1b60bbe6e6691ded4a.png" alt="image" data-base62-sha1="rV9O9ojHYwuE8C66hR2bnlz7VAm" width="690" height="133" data-dominant-color="EFF5F9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">699×135 8.01 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #9 by @jcfr (2019-01-18 15:38 UTC)

<p>Update:</p>
<ul>
<li>macOS package has been signed</li>
<li><a href="https://en.wikipedia.org/wiki/3DSlicer">Wikipedia</a> page and <a href="https://www.nitrc.org/frs/?group_id=50">nitrc</a> website updated</li>
<li>ExtensionStats module provided by <a href="https://github.com/fbudin69500/SlicerDeveloperToolsForExtensions">SlicerDeveloperToolsForExtensions</a> updated</li>
</ul>
<p>Notes:</p>
<ul>
<li>discourse post and announcement will be posted on early next week. In the mean time, review and update <a href="https://docs.google.com/document/d/1AODemQcv9Md0f_BtGo8ZIvzMXdm4gt6UxWR9ABJDr4s/edit">this google document</a></li>
</ul>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6de81cc7e15ff1144193f72eb4e468dc2d631138.png" alt="image" data-base62-sha1="fGhlfW9d0SHZvqrgvm6Pn3tPv2E" width="684" height="131"></p>

---
