# Vtk python does not import on today's windows nightly

**Topic ID**: 1868
**Date**: 2018-01-18
**URL**: https://discourse.slicer.org/t/vtk-python-does-not-import-on-todays-windows-nightly/1868

---

## Post #1 by @pieper (2018-01-18 14:05 UTC)

<p>Today’s nightly windows Slicer starts, but all scripted modules are broken.  Today’s nightly on mac works fine for me, as does 4.8.1 on the same windows machine.</p>
<p>The first error message is:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import vtk
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
ImportError: No module named vtk
</code></pre>
<p>probably a vtk9 packaging issue.</p>

---

## Post #2 by @jcfr (2018-01-18 14:33 UTC)

<p>Since nothing was expected to change for the current nightly, I suspect <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26834">r26834</a> introduced the regression.</p>
<p>Cc: <a class="mention" href="/u/adamrankin">@adamrankin</a></p>

---

## Post #3 by @lassoan (2018-01-18 14:39 UTC)

<p>I had the same issue and could fix it locally by modifying SlicerLauncherSettings.ini. I had to add VTK Python packages location <code>&lt;APPLAUNCHER_DIR&gt;/bin/Lib/site-packages</code> to section <code>[PYTHONPATH]</code>. It would be great if somebody could fix the ini file generation.</p>

---

## Post #4 by @adamrankin (2018-01-18 14:49 UTC)

<p>This is beyond my level of knowledge. If Andras’ fix is the correct one, I can implement the change.</p>

---

## Post #5 by @lassoan (2018-01-18 15:25 UTC)

<p>I’m not sure if the correct solution is to add/change paths in launcher settings (by changing External_VTKv9.cmake) or change VTK configuration to deploy site-packages to a different folder.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Could you advise?</p>

---

## Post #6 by @pieper (2018-01-18 15:27 UTC)

<p>I can confirm the fix from Andras works.  The SlicerLauncherSettings.ini file is in the bin directory and in addition to adding the line <code>12\path=&lt;APPLAUNCHER_DIR&gt;/bin/Lib/site-packages</code> you need to increment the last line of the section to <code>size=12</code>.</p>
<p>Other notes: the nightly crashes when started over remote desktop but the 4.8.1 release does not (probably the OpenGL2 issue) and I see the same <a href="https://issues.slicer.org/view.php?id=4496">slowdown in Slice rendering that Andras reported</a>.</p>

---

## Post #7 by @jcfr (2018-01-18 15:32 UTC)

<aside class="quote no-group" data-username="pieper" data-post="1" data-topic="1868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Today’s nightly windows Slicer starts, but all scripted modules are broken</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/pieper">@pieper</a>  Look like you meant “building the current trunk with Qt5 and VTK9 enabled” ?  (there is no <code>bin/Lib/site-packages</code> directory in the current nightly windows package)</p>

---

## Post #8 by @pieper (2018-01-18 15:36 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> I just downloaded and installed 4.9.0-2018-01-17 and I have a bin/Lib/site-packages:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c71fc45907c639db54b2183972d0f343742cd3b.png" alt="image" data-base62-sha1="hKTpYF6vpzlksgunNvmqcGFtToD" width="683" height="202"></p>

---

## Post #9 by @ihnorton (2018-01-23 16:44 UTC)

<p>9 posts were merged into an existing topic: <a href="/t/reslice-performance-issues-on-windows-moved/1914">Reslice performance issues on windows (moved)</a></p>

---

## Post #10 by @jcfr (2018-01-18 15:41 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> This is very strange, the <code>vtkmodules</code> package is not expected to exist in the current nightly. It also doesn’t exist in the install tree used to create the package:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f52f2d7c150138f18445381648c35acb74f87693.png" data-download-href="/uploads/short-url/yZ03ANT2POtOxfEihB6Uh2O64n1.png?dl=1" title="Screenshot from 2018-01-18 10-39-48"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f52f2d7c150138f18445381648c35acb74f87693_2_690x404.png" alt="Screenshot from 2018-01-18 10-39-48" data-base62-sha1="yZ03ANT2POtOxfEihB6Uh2O64n1" width="690" height="404" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f52f2d7c150138f18445381648c35acb74f87693_2_690x404.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f52f2d7c150138f18445381648c35acb74f87693.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f52f2d7c150138f18445381648c35acb74f87693.png 2x" data-dominant-color="EDF0F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2018-01-18 10-39-48</span><span class="informations">881×517 131 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @jcfr (2018-01-18 15:52 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> I confirm that after installing the nightly package (that was built on the factory), it is different from what you have.</p>
<p>I suspect the <code>factory.perklab</code>  site maintained by <a class="mention" href="/u/lassoan">@lassoan</a>  is uploading the installer and that would explain what you observed</p>

---

## Post #12 by @lassoan (2018-01-18 15:55 UTC)

<p>factory.perklab has not been uploading packages for a while (temporarily disabled). I (and probably Steve as well) use the local package folder - <code>c:\D\S4R\Slicer-build\_CPack_Packages\win-amd64\NSIS\Slicer-4.9.0-2018-01-17-win-amd64</code>.</p>

---

## Post #14 by @jcfr (2018-01-18 16:04 UTC)

<aside class="quote no-group quote-post-not-found" data-username="pieper" data-post="13" data-topic="1868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>must happen during the installer step then?</p>
</blockquote>
</aside>
<p>Unlikely, creation of the windows installer consist only in packaging of the install tree.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> It turns out that <code>Slicerbot Perklab</code> is uploading the package. See <a href="http://slicer.kitware.com/midas3/item/338765">http://slicer.kitware.com/midas3/item/338765</a></p>

---

## Post #16 by @jcfr (2018-01-18 16:19 UTC)

<blockquote>
<p>Import of VTK modules when built against Qt5 and VTK9</p>
</blockquote>
<p>This should be fixed by</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/871">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/871" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/871" target="_blank" rel="noopener">Python interpreter/programming issues-Slicer3.6 RC3</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:33:34" data-timezone="UTC">10:33PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:33:35" data-timezone="UTC">10:33PM - 12 Mar 20 UTC</span>
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
    <p class="github-body-container">_This issue was created automatically from an original [Mantis Issue](https://ma<span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ntisarchive.slicer.org/view.php?id=871). Further discussion may take place here._</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #17 by @lassoan (2018-01-18 16:20 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="14" data-topic="1868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>It turns out that Slicerbot Perklab is uploading the package</p>
</blockquote>
</aside>
<p>It is interesting, because the package does not show up in the <a href="http://slicer.cdash.org/index.php?project=Slicer4">dashboard</a> (no yellow boxes in perklab.factory lines). Are uploading to the dashboard and to MIDAS controlled by different settings?</p>

---

## Post #18 by @jcfr (2018-01-18 16:27 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="17" data-topic="1868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Are uploading to the dashboard and to MIDAS controlled by different settings?</p>
</blockquote>
</aside>
<p>Technically, no installer are uploaded to the dashboard. Only a <code>.url</code> file containing a link to the file uploaded on Midas.</p>
<p>I suspect you have the option <code>WITH_PACKAGES</code> enabled (see <a href="https://github.com/Slicer/Slicer/blob/cea9dcfd94bc1b670126c60a06a6950e5ead1c01/CMake/SlicerDashboardScript.TEMPLATE.cmake#L74">here</a>). This would explain why the installer is generated and uploaded.</p>
<p><a href="https://github.com/Slicer/Slicer/blob/cea9dcfd94bc1b670126c60a06a6950e5ead1c01/CMake/SlicerDashboardDriverScript.cmake#L395-L440" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/cea9dcfd94bc1b670126c60a06a6950e5ead1c01/CMake/SlicerDashboardDriverScript.cmake#L395-L440</a></p>
<p>If you want to have the package created by only disable the upload of the package, you could set the option <code>run_ctest_with_upload</code> to <code>0</code>.</p>

---

## Post #25 by @jcfr (2018-01-22 00:21 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="17" data-topic="1868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It turns out that Slicerbot Perklab is uploading the package</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Did you have a chance to disable the upload ?</p>

---

## Post #26 by @lassoan (2018-01-22 05:28 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="25" data-topic="1868">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Did you have a chance to disable the upload ?</p>
</blockquote>
</aside>
<p>I’ve set WITH_PACKAGES option to FALSE, so from tomorrow it should not upload any package.</p>
<p>Do you know why setting run_ctest_with_upload to FALSE did not disable package upload?</p>
<p>I see on the dashboard that there overload.kitware have not been able to build Slicer successfully in the last couple of days. Could you try to fix that?</p>
<p>Also, the dashboard shows that overload.kitware still tries to build the nightly using VS2013. Is that supposed to work? Haven’t we switched to VS2015 along with Qt5 and VTK9?</p>

---
