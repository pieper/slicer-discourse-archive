# Interpreting CDash reporting: extension is packaged despite build errors?

**Topic ID**: 856
**Date**: 2017-08-11
**URL**: https://discourse.slicer.org/t/interpreting-cdash-reporting-extension-is-packaged-despite-build-errors/856

---

## Post #1 by @fedorov (2017-08-11 14:03 UTC)

<p>I checked the dashboard today, and I found that one of our extension had a (new) <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1077712">build error</a>:</p>
<pre><code class="lang-auto">Error copying file "@rpath/libITKFactoryRegistration.dylib" to 
  "/.../DCMQI-build/dcmqi-build/_CPack_Packages/Darwin/TGZ/26228-macosx-amd64-DCMQI-
  git95356d4-2017-07-27/Slicer.app/Contents/lib/Slicer-4.7/libITKFactoryRegistration.dylib".
</code></pre>
<p>However, despite of this error, the extension package is available, and it seems to work in Slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8c4e0df28dcd0a4e357d3333e4ff110e1b76517.png" data-download-href="/uploads/short-url/sE5iR45EtcR0LlyZ0YvIKZ8D8wf.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8c4e0df28dcd0a4e357d3333e4ff110e1b76517_2_690x60.png" alt="image" data-base62-sha1="sE5iR45EtcR0LlyZ0YvIKZ8D8wf" width="690" height="60" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8c4e0df28dcd0a4e357d3333e4ff110e1b76517_2_690x60.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8c4e0df28dcd0a4e357d3333e4ff110e1b76517_2_1035x90.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8c4e0df28dcd0a4e357d3333e4ff110e1b76517.png 2x" data-dominant-color="C7C6AA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1124×98 10.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> could this potentially be related to the fixes discussed in <a href="https://discourse.slicer.org/t/no-nightly-mac-binary-since-august-1/836/11" class="inline-onebox">No nightly Mac binary since August 1 - #11 by jcfr</a>?</p>

---

## Post #2 by @jcfr (2017-08-12 19:26 UTC)

<p>Look like a legitimate error associated with packaging. I will have a look.</p>
<p>To clarify, packaging is technically not part of the “build”, it happens afterward.</p>
<p>That said, we drive the packaging using <a>ctest_build</a> and submit the additional results like they were a build output. That is packaging error are reported like “build” errors.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/05f67d75667f002b135e361f0f7e975ebcb7e77f/Extensions/CMake/SlicerBlockBuildPackageAndUploadExtension.cmake#L228-L238" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/05f67d75667f002b135e361f0f7e975ebcb7e77f/Extensions/CMake/SlicerBlockBuildPackageAndUploadExtension.cmake#L228-L238" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/05f67d75667f002b135e361f0f7e975ebcb7e77f/Extensions/CMake/SlicerBlockBuildPackageAndUploadExtension.cmake#L228-L238</a></h4>
<pre class="onebox"><code class="lang-cmake"><ol class="start lines" start="228" style="counter-reset: li-counter 227 ;">
<li># Package extension</li>
<li>if(build_errors GREATER "0")</li>
<li>message(WARNING "Skip extension packaging: ${build_errors} build error(s) occured !")</li>
<li>else()</li>
<li>message("Packaging and uploading extension ${EXTENSION_NAME} to midas ...")</li>
<li>set(package_list)</li>
<li>set(package_target "package")</li>
<li>if(RUN_CTEST_UPLOAD)</li>
<li>  set(package_target "packageupload")</li>
<li>endif()</li>
<li>if(RUN_CTEST_PACKAGES)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @fedorov (2017-08-12 19:44 UTC)

<p>Thanks for looking into this <a class="mention" href="/u/jcfr">@jcfr</a>!</p>
<p>Note that there were no changes to the extension source code between the latest successful build/package (Aug 1, <a href="http://slicer.cdash.org/buildSummary.php?buildid=1073259">http://slicer.cdash.org/buildSummary.php?buildid=1073259</a>) and the date when failure was first observed (Aug 9, <a href="http://slicer.cdash.org/buildSummary.php?buildid=1076906">http://slicer.cdash.org/buildSummary.php?buildid=1076906</a>). In between there were no Mac builds of extensions at all. So it looks like the problem is on the Slicer side.</p>

---

## Post #4 by @fedorov (2017-08-15 13:40 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> the problem I mentioned above persists: <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1079987">http://slicer.cdash.org/viewBuildError.php?buildid=1079987</a></p>
<p>I see the same problem for a large number of other C++ extensions. Is there a plan to address this regression in the Slicer core?</p>

---

## Post #5 by @jcfr (2017-08-21 22:27 UTC)

<p>One of the MacOSX issue is now addressed by <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26296">r26296</a>, I will follow up on the dcmqi error tomorrow.</p>

---

## Post #6 by @jcfr (2017-08-24 07:45 UTC)

<p>macOS packaging issue will be addressed by</p>
<aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/issues/780" target="_blank">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/780" target="_blank">Measurements widgets don't work in dual 3D view</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:31:51" data-timezone="UTC">10:31PM - 12 Mar 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-03-12" data-time="22:31:52" data-timezone="UTC">10:31PM - 12 Mar 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/slicerbot" target="_blank">
          <img alt="slicerbot" src="https://avatars3.githubusercontent.com/u/10277015?v=4" class="onebox-avatar-inline" width="20" height="20">
          slicerbot
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">This issue was created automatically from an original Mantis Issue. Further discussion may take place here.</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #7 by @fedorov (2017-08-24 14:35 UTC)

<p>Thank you <a class="mention" href="/u/jcfr">@jcfr</a> for tracking this down!</p>
<p>I am sure you will let us know if any updates will be needed for the extensions!</p>

---

## Post #8 by @jcfr (2017-08-24 18:40 UTC)

<p>This should be fixed in <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26301">r26301</a></p>

---

## Post #9 by @jcfr (2017-08-25 17:56 UTC)

<p>And here is a follow up commit addressing the remaining issues in Slicer. See <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26305">r26305</a></p>
<p>Corresponding changes in upstream projects are here:</p>
<ul>
<li>ITK: <a href="http://review.source.kitware.com/#/c/22583/">http://review.source.kitware.com/#/c/22583/</a>
</li>
<li>CTK:  <a href="https://github.com/commontk/CTK/pull/745/commits/2b71958a424f7fff01b248aaebce0bcdb4dd25ed">https://github.com/commontk/CTK/pull/745/commits/2b71958a424f7fff01b248aaebce0bcdb4dd25ed</a>
</li>
<li>MINC: <a href="https://github.com/BIC-MNI/libminc/pull/87">https://github.com/BIC-MNI/libminc/pull/87</a>
</li>
</ul>

---
