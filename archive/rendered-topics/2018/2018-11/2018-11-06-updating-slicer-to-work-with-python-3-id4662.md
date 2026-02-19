---
topic_id: 4662
title: "Updating Slicer To Work With Python 3"
date: 2018-11-06
url: https://discourse.slicer.org/t/4662
---

# Updating slicer to work with python 3

**Topic ID**: 4662
**Date**: 2018-11-06
**URL**: https://discourse.slicer.org/t/updating-slicer-to-work-with-python-3/4662

---

## Post #1 by @kayarre (2018-11-06 19:31 UTC)

<p>I am interested in having slicer work with python 3 as I am already using python 3 in other parts of my workflow, and would be nice to not have make my scripts compatible across both.</p>
<p>I have heard that this is planned but didn’t know if was formerly documented all the pieces that will be affected by the transition?</p>
<p>What would be required to do this, what pieces need to be updated and made compatible?</p>
<p>~Kurt</p>

---

## Post #2 by @jcfr (2018-11-07 05:57 UTC)

<p>Thanks for reaching out.</p>
<blockquote>
<p>would be nice to not have make my scripts compatible across both.</p>
</blockquote>
<p>If you are not using feature specific to python 3, your scripts will be compatible. To ensure this is the case, you could also make sure of the <a href="https://pythonhosted.org/six">Six: Python 2 and 3 Compatibility Library</a>, it is available in Slicer.</p>
<blockquote>
<p>all the pieces that will be affected by the transition?</p>
</blockquote>
<p>Assuming your code is forward compatible with python 3 (you could for example look at <a href="https://python-future.org/compatible_idioms.html">Cheat Sheet: Writing Python 2-3 compatible code</a>, most of the infrastructure change will be transparent for your project.</p>
<p>Indeed, the Slicer build-system API that will be unaffected, only the implementation of CMake function like <a href="https://github.com/Slicer/Slicer/blob/36997169adf0e323015fb368aeb3ea9ecdb2e793/CMake/SlicerMacroBuildModuleQtLibrary.cmake#L239-L260">SlicerMacroBuildModuleQtLibrary</a> will be changed internally. And other change will also be specific to Slicer core, and will be related to class like <a href="https://github.com/Slicer/Slicer/blob/master/Base/QTCore/qSlicerScriptedUtils_p.h">qSlicerScriptedUtils</a>. But that should not affect the building and distribution of your project.</p>

---

## Post #3 by @jcfr (2019-03-16 20:17 UTC)

<p>This past week, we were busy modernizing the Slicer code base. See <a href="https://discourse.slicer.org/t/c-11-modernization-update-to-itk5-removal-of-obsolete-qt4-and-vtk7-support/6165" class="inline-onebox">C++11 modernization, update to ITK5, removal of obsolete Qt4 and VTK7 support</a></p>
<p>This delayed the transition to Python 3. The associated effort will be resumed on March 25th.</p>
<p>In the mean time, here is a work-in-progress topic based on some preliminary work from  <a class="mention" href="/u/ihnorton">@ihnorton</a></p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/1118">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/1118" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/1118" target="_blank" rel="noopener">Glyph visualization inconsistent across viewers</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:37:58" data-timezone="UTC">10:37PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:37:58" data-timezone="UTC">10:37PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank" rel="noopener">
          <img alt="slicerbot" src="https://avatars.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>

    <div class="labels">
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=1118). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Cc: <a class="mention" href="/u/bpaniagua">@bpaniagua</a> <a class="mention" href="/u/andinet_enquobahrie">@Andinet_Enquobahrie</a></p>

---

## Post #4 by @jcfr (2019-04-02 14:16 UTC)

<p>Hi,</p>
<p>Slicer can now start with Python 3 !  A little more work to finalize the update of scripted modules but we are getting there.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/51ef01cb2da456351ae01b397e7b00c10abb2ad9.png" alt="image" data-base62-sha1="bGOKcLpx7GGOfCwvz6nYXFJVmVb" width="397" height="163"></p>
<p>Jc</p>

---

## Post #5 by @Alex_Vergara (2019-04-04 14:54 UTC)

<p>Still not available on nightly <img src="https://emoji.discourse-cdn.com/twitter/cry.png?v=12" title=":cry:" class="emoji" alt=":cry:" loading="lazy" width="20" height="20"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b15c8967407a3542d70399e5e9446f3c2f56bb91.png" alt="image" data-base62-sha1="pj0LOT4HeYI5CNN0A7PXetK2AIF" width="554" height="212"></p>

---

## Post #6 by @jcfr (2019-04-04 17:09 UTC)

<aside class="quote no-group quote-modified" data-username="Alex_Vergara" data-post="5" data-topic="4662" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>Still not available on nightly :’(</p>
</blockquote>
</aside>
<p>Sorry for the confusion, the support for Python3 is currently only available through this PR. See <a href="https://github.com/Slicer/Slicer/pull/1118" class="inline-onebox">Glyph visualization inconsistent across viewers · Issue #1118 · Slicer/Slicer · GitHub</a></p>

---

## Post #7 by @jcfr (2019-04-04 20:21 UTC)

<p>The pull request is now reading for testing.</p>
<p>Next steps (before merging):</p>
<ul>
<li>test packaging</li>
<li>update migration guide</li>
</ul>
<p>Then (after merging):</p>
<ul>
<li>update few extensions</li>
</ul>
<p>Open questions:</p>
<ul>
<li>(1) should we package dependency (potentially specified in a <code>requirement.txt</code>) in extensions</li>
<li>or (2) should we install them when the extension is installed.</li>
</ul>

---

## Post #8 by @lassoan (2019-04-04 21:58 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="7" data-topic="4662">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<ul>
<li>(1) should we package dependency (potentially specified in a <code>requirement.txt</code> ) in extensions</li>
<li>or (2) should we install them when the extension is installed</li>
</ul>
</blockquote>
</aside>
<p>Leaner extension packages would be nicer and probably version requirements could be managed more flexibly if python packages would be downloaded dynamically. However, it should be possible to install extensions from file, without network connection.</p>

---

## Post #9 by @jcfr (2019-04-11 20:04 UTC)

<p>Updates:</p>
<ul>
<li>Local testing is completed. Linux, macOS and Windows packages can be generated.</li>
<li>Migration guide has been updated:
<ul>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide#Python_2_to_Python_3" rel="nofollow noopener"> Slicer 5.0: API changes since 4.10 - Python 2 to Python 3</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide#Slicer_5.0:_Python2_to_Python3" rel="nofollow noopener"> Slicer Extension updates - Slicer 5.0: Python2 to Python3</a></li>
</ul>
</li>
<li>Changes will be integrated this afternoon.</li>
</ul>
<p>Slicer has been updated to only support building against Python3 and all python scripts available in the main Slicer code base are only compatible with Python3.</p>
<p>On the other hand, extensions (e.g <a href="https://github.com/fedorov/MultiVolumeExplorer/pull/44" rel="nofollow noopener">MultiVolumeExplorer</a>, <a href="https://github.com/fedorov/MultiVolumeImporter/pull/38" rel="nofollow noopener">MultiVolumeImporter</a> and <a href="https://github.com/SimpleITK/SlicerSimpleFilters/pull/16" rel="nofollow noopener">SlicerSimpleFilters</a> are expected to support both Python2 and Python3. More details about the different approach in the migration guide liked above.</p>

---

## Post #10 by @jcfr (2019-04-11 20:09 UTC)

<p>Set of changes concluding the transition to Python3 has been integrated in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28100" rel="nofollow noopener">r28100</a> to <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28129" rel="nofollow noopener">r28129</a></p>
<p>Notes:</p>
<ul>
<li>Given the extend of the change, developers are expected to perform a clean build.</li>
</ul>

---

## Post #11 by @jcfr (2019-04-11 20:12 UTC)

<p>Next:</p>
<ul>
<li>Fix failing tests</li>
<li>Integrate SciPy</li>
<li>Submit Pull Requests for updating few more extensions. This will provide additional examples.</li>
<li>Finalize plan to support  requirements for installing dependencies from the Python Package Index (<a href="https://pypi.org/" rel="nofollow noopener">https://pypi.org/</a>)</li>
</ul>

---

## Post #12 by @lassoan (2019-04-12 02:17 UTC)

<p>You are awesome Jc! I’ve started a build on Windows, I’ll let you know if I run into any issues.</p>

---

## Post #13 by @lassoan (2019-04-12 15:43 UTC)

<p>After fixing Python’s <a href="https://github.com/Slicer/Slicer/pull/1118#issuecomment-482436689" rel="nofollow noopener">Modules_io_iomodule.c</a>, Windows build succeeded in both release and debug mode.</p>
<p>In release mode, everything seems to work fine - great!  In debug mode, Slicer hangs at startup. See a fix here: <a href="https://github.com/lassoan/Slicer/tree/python-startup-hang-in-debug-mode" rel="nofollow noopener">https://github.com/lassoan/Slicer/tree/python-startup-hang-in-debug-mode</a>. <a class="mention" href="/u/jcfr">@jcfr</a> could you please review and merge?</p>

---

## Post #14 by @jcfr (2019-04-12 16:47 UTC)

<blockquote>
<p>After fixing Python’s <a href="https://github.com/Slicer/Slicer/pull/1118#issuecomment-482436689">Modules_io_iomodule.c</a>, Windows build succeeded in both release and debug mode.</p>
</blockquote>
<p>Thanks for looking into this. I will update <a href="https://github.com/python-cmake-buildsystem/python-cmake-buildsystem" class="inline-onebox">GitHub - python-cmake-buildsystem/python-cmake-buildsystem: A cmake buildsystem for compiling Python</a> to integrate this.</p>
<blockquote>
<p>In debug mode, Slicer hangs at startup. See a fix here: <a href="https://github.com/lassoan/Slicer/tree/python-startup-hang-in-debug-mode">https://github.com/lassoan/Slicer/tree/python-startup-hang-in-debug-mode</a>. <a class="mention" href="/u/jcfr">@jcfr</a> could you please review and merge?</p>
</blockquote>
<p>Thanks for the patch. I will review and integrate shortly.</p>

---

## Post #15 by @lassoan (2019-04-12 18:51 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> Should we add a wiki page or online spreadsheet where we can quickly add any issues that we find (to make sure we don’t forget about them or work on them in parallel)? Mantis would be too heavyweight for this.</p>
<p>For example, I’ve just found that <code>restart()</code> Python function does not work anymore (has no effect).</p>

---

## Post #16 by @jcfr (2019-04-12 18:58 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="15" data-topic="4662">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Should we add a wiki page</p>
</blockquote>
</aside>
<p>I started to document these type of problems here: <a href="https://www.slicer.org/wiki/Documentation/Labs/Slicer5-roadmap#Python3" class="inline-onebox">Documentation/Labs/Slicer5-roadmap - Slicer Wiki</a></p>

---

## Post #17 by @MARKRONSON (2019-04-19 18:00 UTC)

<p>hey <a class="mention" href="/u/jcfr">@jcfr</a>,<br>
thanks for all your replies…i was having the similar sort of question and your solutions worked for me.<br>
best regards!!</p>

---
