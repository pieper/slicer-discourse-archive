---
topic_id: 4422
title: "Update Slicer 4 10 Release Will Be Initiated Tomorrow Mornin"
date: 2018-10-17
url: https://discourse.slicer.org/t/4422
---

# Update: Slicer 4.10 release will be initiated tomorrow morning

**Topic ID**: 4422
**Date**: 2018-10-17
**URL**: https://discourse.slicer.org/t/update-slicer-4-10-release-will-be-initiated-tomorrow-morning/4422

---

## Post #1 by @jcfr (2018-10-17 01:57 UTC)

<p>Tonight we will let the regular nightly build take place, then after we confirm the <strong>build complete on all platforms</strong> with <strong>all tests passing</strong> and <strong>package</strong> successfully created and <strong>working</strong>, we will abort the nightly build script and initiate the build of the release package.</p>
<p>In the mean time, few more commits will be integrated:</p>
<ul>
<li><s>fix for <a href="https://issues.slicer.org/view.php?id=4513">issue 4513</a></s> <strong>done</strong></li>
<li><s>pull request <a href="https://github.com/Slicer/Slicer/pull/1029">1029</a></s> <strong>will be integrated after the release</strong></li>
<li><s>few fixes to the extension manager restore tab</s> <strong>done</strong></li>
</ul>
<p>Also, since we will abort the nightly build, you should <strong>not</strong> expect all nightly extensions to be available, instead they will be available with the upcoming release.</p>
<p>References:</p>
<ul>
<li><a href="https://discourse.slicer.org/t/update-toward-slicer-4-10-0/2486" class="inline-onebox">Update: Toward Slicer 4.10.0</a></li>
</ul>

---

## Post #2 by @jcfr (2018-10-17 17:46 UTC)

<p>Great news, the dashboard is green [1] and packages can be installed on all platforms, we will tag the repo shortly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f45921b829948ec46d19fbd99b05504ed63d30e.png" data-download-href="/uploads/short-url/bjgM2dQqBxzMksCDroVDw8XH0tM.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f45921b829948ec46d19fbd99b05504ed63d30e_2_690x97.png" alt="image" data-base62-sha1="bjgM2dQqBxzMksCDroVDw8XH0tM" width="690" height="97" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f45921b829948ec46d19fbd99b05504ed63d30e_2_690x97.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f45921b829948ec46d19fbd99b05504ed63d30e_2_1035x145.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/f/4f45921b829948ec46d19fbd99b05504ed63d30e_2_1380x194.png 2x" data-dominant-color="B2C4C1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1517×215 34.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>[1] with a splash of orange because of warnings. These will be addressed or ignored with CTest exceptions later.</p>

---

## Post #3 by @jcfr (2018-10-17 20:21 UTC)

<p>3 posts were split to a new topic: <a href="/t/why-dont-we-see-linux-test-result-reported-on-cdash/4446">Why don’t we see Linux test result reported on CDash?</a></p>

---

## Post #4 by @jcfr (2018-10-18 03:36 UTC)

<p>Update:</p>
<ul>
<li>Revision for 4.10.0 is <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=27501">r27501</a>
</li>
<li>Release progress can be tracked on CDash with <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2018-10-17&amp;filtercount=1&amp;showfilters=1&amp;field1=groupname&amp;compare1=61&amp;value1=Experimental-Packages">this link</a>
<ul>
<li>You should <strong>NOT</strong> expect nightly build tonight.</li>
<li>The release scripts also take care of building the corresponding extensions.</li>
<li>Updated release scripts are in the <a href="https://github.com/Slicer/DashboardScripts">Slicer/DashboardScripts</a> repository</li>
</ul>
</li>
<li>Both SVN and Git repositories have been tagged, and maintenance branches created.</li>
<li>The <a href="https://www.slicer.org/wiki/Release_Details">Release Details</a> page has been updated</li>
<li>The <a href="https://github.com/Slicer/SlicerBuildEnvironment">SlicerBuildEnvironment</a> docker image used to build the Linux release and all associated extensions has been created.
<ul>
<li>It is available dockerhub as <a href="https://microbadger.com/images/slicer/buildenv-qt5-centos7:slicer-4.10">slicer/qt5-centos7:slicer-4.10</a>
</li>
<li>A  maintainer document explaining <a href="https://github.com/Slicer/SlicerBuildEnvironment#maintainers">how to create a tagged build environment image</a> has been created</li>
<li>The <strong>Slicer Release Process</strong> document on the wiki has been <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/ReleaseProcess#Tag_and_publish_SlicerBuildEnvironment_docker_image">updated to reference it</a>
</li>
</ul>
</li>
</ul>
<p>Remaining tasks:</p>
<ul>
<li>See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/ReleaseProcess#Day_2:_Post_release">ReleaseProcess#Day_2:_Post_release</a>
</li>
</ul>
<p>Notes:</p>
<ul>
<li>The dashboard project has not been renamed from <code>Slicer4</code> to <code>SlicerStable</code>. This will happen for either Slicer 4.10.1 or Slicer 5.0.0. This is tracked by <a href="https://issues.slicer.org/view.php?id=4644">issue 4644</a>
</li>
</ul>

---

## Post #5 by @fedorov (2018-10-18 14:31 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> I do not know if this is a transient issue, and whether it is related to the new release (the name of the build directory includes ‘4100’), but there is this new build error for the dcmqi extension: <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1402918" class="inline-onebox">CDash</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6690605cdf49872ffe650381f593cba40aed51b.png" data-download-href="/uploads/short-url/nK8gRq155d6EHSK42Iu2FMZgq8P.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6690605cdf49872ffe650381f593cba40aed51b_2_690x194.png" alt="image" data-base62-sha1="nK8gRq155d6EHSK42Iu2FMZgq8P" width="690" height="194" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6690605cdf49872ffe650381f593cba40aed51b_2_690x194.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/6/a6690605cdf49872ffe650381f593cba40aed51b_2_1035x291.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6690605cdf49872ffe650381f593cba40aed51b.png 2x" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1125×317 41.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @jcfr (2018-10-18 15:42 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="5" data-topic="4422">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p>whether it is related to the new release (the name of the build directory includes ‘4100’)</p>
</blockquote>
</aside>
<p>Good catch. This is fixed in the following commit, I will delete the current extension build tree on <code>factory-south-macos</code> and re-launch the extension build script.</p>
<p>As a side note, the build were submitted on <code>SlicerPreview</code> but they should have been submitted on <code>Slicer4</code> (soon to be <code>SlicerStable</code>). This is where the next submission will be posted.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/DashboardScripts/commit/50121ef82b8c4bebd37a5d4daf41cb9ac444e71e">
  <header class="source">

      <a href="https://github.com/Slicer/DashboardScripts/commit/50121ef82b8c4bebd37a5d4daf41cb9ac444e71e" target="_blank" rel="noopener">github.com/Slicer/DashboardScripts</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/DashboardScripts/commit/50121ef82b8c4bebd37a5d4daf41cb9ac444e71e" target="_blank" rel="noopener">factory-south-macos: Use correct value for CMAKE_OSX_DEPLOYMENT_TARGET</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2018-10-18" data-time="15:39:11" data-timezone="UTC">03:39PM - 18 Oct 18 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="changed 1 files with 1 additions and 1 deletions">
        <a href="https://github.com/Slicer/DashboardScripts/commit/50121ef82b8c4bebd37a5d4daf41cb9ac444e71e" target="_blank" rel="noopener">
          <span class="added">+1</span>
          <span class="removed">-1</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">The value 10.6 was left over when the script was created based of the
previous r<span class="show-more-container"><a href="https://github.com/Slicer/DashboardScripts/commit/50121ef82b8c4bebd37a5d4daf41cb9ac444e71e" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">unning on "factory-macos".

See https://discourse.slicer.org/t/update-slicer-4-10-release-will-be-initiated-tomorrow-morning/4422/5?u=jcfr

Reported-by: Andrey Fedorov &lt;fedorov@bwh.harvard.edu&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @jcfr (2018-10-19 01:37 UTC)

<p>Updates:</p>
<ul>
<li>
<p>Wiki has been updated. The <a href="https://www.slicer.org/wiki/News">News </a> page has been updated with a banner at the top to reference the Slicer forum. History of the transition has also been <a href="https://www.slicer.org/wiki/News#2018_and_beyond">documented</a> on that same page.</p>
</li>
<li>
<p>mantis release list has been updated</p>
</li>
<li>
<p>A priori no nightly build tonight. Indeed, in the process of signing the package, I also realized they had the wrong name, the dashboard driver script has been fixed and package are being regenerated.</p>
</li>
</ul>
<p><a href="https://github.com/Slicer/Slicer/commit/b5386721e8162d5a3c07575d3335359039a4a38d" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/commit/b5386721e8162d5a3c07575d3335359039a4a38d</a></p>

---

## Post #8 by @spujol (2018-10-19 15:37 UTC)

<p>Hello JC<br>
Do you have a date for slicer 4.10 binaries?<br>
Thank you!<br>
Sonia</p>
<details>
<summary>
Original post in French</summary>
<p>Hello JC</p>
<p>Tu as une date pour les binaries de Slicer 4.10 ?</p>
<p>Merci!</p>
<p>Sonia</p>
</details>

---

## Post #9 by @jcfr (2018-10-19 22:54 UTC)

<h2><a name="p-16741-updates-1" class="anchor" href="#p-16741-updates-1" aria-label="Heading link"></a>Updates</h2>
<ul>
<li>
<p>Release packages are back with the expected name. See <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2018-10-18&amp;filtercount=1&amp;showfilters=1&amp;field1=groupname&amp;compare1=61&amp;value1=Experimental-Packages">CDash report</a></p>
</li>
<li>
<p>Windows package has been signed and is available for download.</p>
</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f08b6b69b7098374f33fe97f3d3afd2eda3797a.png" data-download-href="/uploads/short-url/kpkWJA0dl6UwmHFVugGCYoyFduG.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f08b6b69b7098374f33fe97f3d3afd2eda3797a.png" alt="image" data-base62-sha1="kpkWJA0dl6UwmHFVugGCYoyFduG" width="269" height="151"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">269×151 4.22 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>Linux package has been marked as release and re-upload, it should shortly appear in the Nightly category.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/8872ba9d6a72eb6dfe24656fc379789417b47f81.png" data-download-href="/uploads/short-url/jt4JYURXD2UfjUmAZSHXj4nKlyN.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/8872ba9d6a72eb6dfe24656fc379789417b47f81.png" alt="image" data-base62-sha1="jt4JYURXD2UfjUmAZSHXj4nKlyN" width="251" height="138"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">251×138 3.59 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>Note that the macOS is <strong>NOT</strong> listed yet because I am looking into way for signing it.</li>
</ul>
<h2><a name="p-16741-next-steps-2" class="anchor" href="#p-16741-next-steps-2" aria-label="Heading link"></a>Next steps</h2>
<ul>
<li>Hopefully sign the macOS package and mark it as release.</li>
<li>Update external website: nitrc and wikipedia</li>
<li>Finalize release announcements</li>
<li>Version NA-MIC data Update external website</li>
<li>Update ExtensionStats extension</li>
</ul>
<h2><a name="p-16741-more-details-3" class="anchor" href="#p-16741-more-details-3" aria-label="Heading link"></a>More details</h2>
<h3><a name="p-16741-release-packages-4" class="anchor" href="#p-16741-release-packages-4" aria-label="Heading link"></a>Release packages</h3>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6f415c07ed5b1bb9e8642d0f30de468f435c587.png" data-download-href="/uploads/short-url/uFz7XdH6RUrb7Gqmde0Om5N4b6n.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6f415c07ed5b1bb9e8642d0f30de468f435c587_2_690x134.png" alt="image" data-base62-sha1="uFz7XdH6RUrb7Gqmde0Om5N4b6n" width="690" height="134" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6f415c07ed5b1bb9e8642d0f30de468f435c587_2_690x134.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6f415c07ed5b1bb9e8642d0f30de468f435c587_2_1035x201.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6f415c07ed5b1bb9e8642d0f30de468f435c587_2_1380x268.png 2x" data-dominant-color="BFCCBF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1490×290 38.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The one test failure is related to test <a href="http://slicer.cdash.org/testDetails.php?test=9226290&amp;build=1403617">test_FiducialLayoutSwitchBug19141</a> and is most likely a false positive:</p>
<pre><code class="lang-auto">Checking the difference between fiducial RAS position [33.4975, 79.4042, -10.2143] and volume RAS as derived from the fiducial display position (33.857864050053124, 78.85677006484119, -11.214302062988281) :  1.19563619402
RAS coordinate difference is too large as well!
Expected &lt; 1 but got 1.19564
</code></pre>
<h3><a name="p-16741-extension-packages-5" class="anchor" href="#p-16741-extension-packages-5" aria-label="Heading link"></a>Extension packages</h3>
<p>There are a total of 143 description files in the <a href="https://github.com/Slicer/ExtensionsIndex/tree/4.10">4.10 branch</a> of the extensions index repository.</p>
<p>A total of <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2018-10-19&amp;filtercombine=and&amp;filtercombine=and&amp;filtercount=2&amp;showfilters=1&amp;filtercombine=and&amp;field1=groupname&amp;compare1=61&amp;value1=Extensions-4.10-Nightly&amp;field2=buildname&amp;compare2=65&amp;value2=27501">397 build reports</a> were submitted on October 19th and the remaining on October 18th including:</p>
<ul>
<li><a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2018-10-19&amp;filtercombine=and&amp;filtercount=3&amp;showfilters=1&amp;filtercombine=and&amp;field1=groupname&amp;compare1=61&amp;value1=Extensions-4.10-Nightly&amp;field2=buildname&amp;compare2=65&amp;value2=27501&amp;field3=site&amp;compare3=61&amp;value3=metroplex.kitware">123 build reports</a> on October 19th with the remaining <a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2018-10-18&amp;filtercount=3&amp;showfilters=1&amp;filtercombine=and&amp;field1=groupname&amp;compare1=61&amp;value1=Extensions-4.10-Nightly&amp;field2=buildname&amp;compare2=65&amp;value2=27501&amp;field3=site&amp;compare3=61&amp;value3=metroplex.kitware">20 build reports</a> on the October 18th on Linux</li>
<li><a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2018-10-19&amp;filtercount=3&amp;showfilters=1&amp;filtercombine=and&amp;field1=groupname&amp;compare1=61&amp;value1=Extensions-4.10-Nightly&amp;field2=buildname&amp;compare2=65&amp;value2=27501&amp;field3=site&amp;compare3=61&amp;value3=factory-south-macos.kitware">143 build reports</a> on macOS on October 19th</li>
<li><a href="http://slicer.cdash.org/index.php?project=Slicer4&amp;date=2018-10-19&amp;filtercount=3&amp;showfilters=1&amp;filtercombine=and&amp;field1=groupname&amp;compare1=61&amp;value1=Extensions-4.10-Nightly&amp;field2=buildname&amp;compare2=65&amp;value2=27501&amp;field3=site&amp;compare3=61&amp;value3=overload.kitware">131 build reports</a> on Windows on October 19th. Not submitted are 12 extension reports:
<ul>
<li>DiffusionQC</li>
<li>DTIAtlasBuilder</li>
<li>LesionSpotlight</li>
<li>MatlabBridge</li>
<li>OpenCVExample</li>
<li>PathReconstruction</li>
<li>PortPlacement</li>
<li>ShapeQuantifier</li>
<li>ShapeVariationAnalyzer</li>
<li>SlicerPathology</li>
<li>SlicerVASST</li>
<li>SlicerVideoCameras</li>
</ul>
</li>
</ul>

---

## Post #10 by @jcfr (2018-10-20 02:58 UTC)

<p>Update:</p>
<ul>
<li>
<p><strong>sign the macOS package</strong>: This will wait Monday, the manager of our Apple account need to accept the updated <em>Apple Developer Program License Agreement</em> before we can access our existing certificates. (Note that the tagged package will still appear as generated on October 19th like the Linux and Windows one.)</p>
</li>
<li>
<p><strong>nightly build</strong>: after we are done investigating the extension build failure on Windows, the nightly will be restarted.</p>
</li>
</ul>

---

## Post #11 by @jcfr (2018-10-22 23:49 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="10" data-topic="4422">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p><strong>sign the macOS package</strong> : This will wait Monday,</p>
</blockquote>
</aside>
<p>To follow up, now that the new license terms have been accepted, I was able to download the signing certificate. Next step will be to also get the associated private key and this should happen tomorrow.</p>
<aside class="quote no-group" data-username="jcfr" data-post="10" data-topic="4422">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>nightly build</p>
</blockquote>
</aside>
<p>Nightly build have been resumed on all platforms. I will share more details about extensions build failure later.</p>

---

## Post #12 by @jcfr (2018-10-25 04:38 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="11" data-topic="4422">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>Next step will be to also get the associated private key and this should happen tomorrow</p>
</blockquote>
</aside>
<p>Good news, we were able to sign the DMG package along with all the executables, libraries and frameworks.  (thanks to my  colleague Chuck A.). Basically the process is:</p>
<ul>
<li>Extract the eula from the DMG</li>
<li>Mount the DMG</li>
<li>Fix up broken embedded frameworks</li>
<li>Sign the app bundle with --deep</li>
<li>Unmount the dmg</li>
<li>Re-insert the eula</li>
<li>Sign the DMG</li>
</ul>
<p>That said, when starting the application, the verification process was still failing complaining that <em>the identity of the developer cannot be confirmed</em> which was surprising because command like <code>spctl -a -t exec -vv ./Slicer.app</code> returned that the application was accepted.</p>
<p>It turns out that the libraries and executables bundled in the package still contain references to rpath referencing the build directories. This is causing the verification  process to fail. Until  now, this was not an issue because the library loader tries all paths until it finds a good one.</p>
<p>Inspecting the system log revealed error like this one:</p>
<pre><code class="lang-auto">Oct 24 23:50:08 factory-south CoreServicesUIAgent[3231]: Error -60005 creating authorization
Oct 24 23:50:24 factory-south CoreServicesUIAgent[3231]: File /Users/kitware/Desktop/Slicer.app/Contents/lib/Slicer-4.10/cli-modules/libACPCTransformLib.dylib failed on rPathCmd /Volumes/Dashboards/Stable/Slicer-4100-build/CTK-build/CMakeExternals/Install/lib/lib/Slicer-4.10/libMRMLCore.dylib
Oct 24 23:50:24 factory-south CoreServicesUIAgent[3231]: Fails dylib check
</code></pre>
<p>An internet search then revealed a similar error within Qt (that is now fixed), see <a href="https://bugreports.qt.io/browse/QTBUG-61413" class="inline-onebox">Loading...</a>.</p>
<p>Later tomorrow, we will patch all libraries removing references to the build tree and re-sign.</p>
<p>Thanks for your patience,</p>

---

## Post #13 by @jcfr (2018-10-26 21:44 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="12" data-topic="4422">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>That said, when starting the application, the verification process was still failing complaining that <em>the identity of the developer cannot be confirmed</em> which was surprising because command like <code>spctl -a -t exec -vv ./Slicer.app</code> returned that the application was accepted.</p>
</blockquote>
</aside>
<h3><a name="p-17042-definitive-way-to-check-that-the-signature-is-correct-1" class="anchor" href="#p-17042-definitive-way-to-check-that-the-signature-is-correct-1" aria-label="Heading link"></a>definitive way to check that the signature is correct</h3>
<p>Further reading revealed that to check if code-signing on macOS works as expected, the package must be downloaded from a website or sent by email, this ensures that the downloaded package is quarantined and will ensure that gatekeeper proceed to the verification.</p>
<p>Source: <a href="https://developer.apple.com/library/archive/documentation/Security/Conceptual/CodeSigningGuide/Procedures/Procedures.html#//apple_ref/doc/uid/TP40005929-CH4-TNTAG201" class="inline-onebox">Code Signing Tasks</a></p>
<p>To check that files are quarantined after downloading, you could do this:</p>
<pre data-code-wrap="bash"><code class="lang-bash">$ ls -l@ ~/Desktop/Slicer.app/Contents/
total 8
drwxr-xr-x@  2 kitware  staff    68 Oct 19 00:33 Extensions-27501
        com.apple.quarantine      61
drwxr-xr-x@ 24 kitware  staff   816 Oct 19 01:54 Frameworks
        com.apple.quarantine      61
-rw-r--r--@  1 kitware  staff  1377 Oct 18 22:48 Info.plist
        com.apple.quarantine      61
[...]
</code></pre>
<h3><a name="p-17042-improved-signing-scripts-2" class="anchor" href="#p-17042-improved-signing-scripts-2" aria-label="Heading link"></a>improved signing scripts</h3>
<p>Further testing revealed issues with the script that should new be addressed.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/KitwareMedical/slicer-macos-codesign-scripts/commits/master">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" alt="" width="32" height="32">

      <a href="https://github.com/KitwareMedical/slicer-macos-codesign-scripts/commits/master" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/344;"><img src="https://opengraph.githubassets.com/b56f41ceba7a023b6e8cbb840815571b3fcd46527bc27ab477b9737847e2f1f2/KitwareMedical/slicer-macos-codesign-scripts" class="thumbnail" alt="" width="690" height="345"></div>

<h3><a href="https://github.com/KitwareMedical/slicer-macos-codesign-scripts/commits/master" target="_blank" rel="noopener">Commits · KitwareMedical/slicer-macos-codesign-scripts</a></h3>

  <p>macOS shell script to extract, codesign, and re-packsign a dmg package. Also create a pkg installer. - Commits · KitwareMedical/slicer-macos-codesign-scripts</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Also, after we are done with this release, the Slicer build system will be improved and the script will be simplified.</p>
<h3><a name="p-17042-why-does-it-take-so-long-3" class="anchor" href="#p-17042-why-does-it-take-so-long-3" aria-label="Heading link"></a>why does it take so long ?</h3>
<p>It is the first time we sign Slicer-based macOS package, after we are done addressing the issues with this release. Follow-up macOS releases of Slicer will happen more quickly.</p>
<h3><a name="p-17042-next-4" class="anchor" href="#p-17042-next-4" aria-label="Heading link"></a>next</h3>
<p>Later this evening or tomorrow, I should have access to our dedicated code-signing macOS workstation, this should allow us to code-sign the current release as well as more efficiently sign packages in the future.</p>

---

## Post #14 by @lassoan (2018-10-27 15:08 UTC)

<p>Thank you Jc for working on this. This will make Slicer installation much easier on MacOS.</p>
<p>Instead of packaging of 4.10.0, would it be possible to release 4.10.1 instead (from the content of current master)? There have been a few fixes (freesurfer surface reading, updates of imported nodes in subject hierarchy tree, vector to scalar volume converter, vector volume segmentation fix, etc. ) which are all low risk and would be useful to have in the stable version.</p>

---

## Post #15 by @Andinet_Enquobahrie (2018-10-28 19:24 UTC)

<p>I would suggest finishing packaging 4.10 properly first. So, we do everything right and fully.</p>
<p>Then after a week or two, we can start looking at 4.10.1 release. In the meantime, folks will have more time to test and report issues on the 4.10 release</p>
<p>My 2 cents<br>
Andinet</p>

---

## Post #16 by @jcfr (2018-10-29 21:20 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="13" data-topic="4422">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>our dedicated code-signing macOS workstation</p>
</blockquote>
</aside>
<p>Good news. I now have access to our macOS signing station and a quick test this afternoon confirmed I could unlock the keychain and access the key from the hardware token.</p>
<p>But in the mean time, the hardware token was un-plugged from the keyboard USB plug and plugged on the back of the wrong macOS workstation … (indeed there are multiple macOS stacked).</p>
<p>This will be addressed tomorrow morning.</p>
<p>In the short term we will be able to manually sign all future macOS stable releases like we already do for windows releases.</p>
<p>And longer term, we will also have our infrastructure ready for automatically signing macOS and windows releases every night.</p>

---

## Post #17 by @jcfr (2018-11-01 19:11 UTC)

<p>Et voila. macOS package is now signed and uploaded, it should be available on <a href="http://download.slicer.org">download.slicer.org</a> shortly.</p>
<p>In the mean time, you can download if from <a href="http://slicer.kitware.com/midas3/folder/5380">http://slicer.kitware.com/midas3/folder/5380</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/facc7099f7ef37a74db8e1e04ee94daa2e6d878c.png" alt="image" data-base62-sha1="zMFnqUHLTxED7imsFadvZZw7Icc" width="625" height="278"></p>
<p>Thanks to my colleague Chuck for his help setting up our macOS signing server as well as <a class="mention" href="/u/ihnorton">@ihnorton</a>, <a class="mention" href="/u/fedorov">@fedorov</a>,  <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/rkikinis">@rkikinis</a> for testing.</p>
<p>We can now resolve issue <a href="https://issues.slicer.org/view.php?id=2708">2708: Gatekeeper - Mac OSX 10.8 - Can’t open because it s from an unidentified developer</a> opened back in 2012.</p>
<p>For more details, see updated <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/ReleaseProcess#Manually_sign_packages">Manually sign package</a> step from the Slicer Release Process.</p>

---

## Post #18 by @jcfr (2018-11-01 19:27 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="17" data-topic="4422">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>it should be available on <a href="http://download.slicer.org">download.slicer.org</a> shortly.</p>
</blockquote>
</aside>
<p>Here it is <img src="https://emoji.discourse-cdn.com/twitter/tada.png?v=12" title=":tada:" class="emoji" alt=":tada:" loading="lazy" width="20" height="20"></p>
<p></p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e47b061c408c91a7757783d1eeae95f937796d5f.png" data-download-href="/uploads/short-url/wBerjZDaBV9I6mnHtYin9dDapYP.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e47b061c408c91a7757783d1eeae95f937796d5f.png" alt="image" data-base62-sha1="wBerjZDaBV9I6mnHtYin9dDapYP" width="690" height="148" data-dominant-color="F1F7FB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">751×162 6.57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><p></p>
<p>And as you may notice, the built date appears as <code>2018-11-01</code> which in fact set based on the creation date of the item in the data system and not the build date. See <a href="https://github.com/mhalle/slicer4-download/blob/4ec9e217808d491b6c6b2ea42de79c1266e07540/slicer4-parselogs/bitstream.py#L33">here</a> and <a href="https://github.com/mhalle/slicer4-download/blob/4ec9e217808d491b6c6b2ea42de79c1266e07540/slicer4-downloadserver/__init__.py#L89">here</a>.</p>

---

## Post #19 by @jcfr (2018-11-01 20:52 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/white_check_mark.png?v=15" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20">  External websites updated</p>
<h3><a name="p-17289-wikipediaorg-1" class="anchor" href="#p-17289-wikipediaorg-1" aria-label="Heading link"></a><code>wikipedia.org</code></h3>
<ul>
<li>Updated version of Slicer. Page has also been updated to remove <code>Tcl</code> has an external dependency.</li>
<li>And worth noting the <code>Critisism</code> section has been removed by some third party. Details <a href="https://en.wikipedia.org/w/index.php?title=3DSlicer&amp;type=revision&amp;diff=853872868&amp;oldid=850676084">here</a></li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec53c07d020366b332dcc83767ddf86a4ca10b54.png" data-download-href="/uploads/short-url/xIE7tOHdK1DwHSTM8t1DsmlvfkE.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec53c07d020366b332dcc83767ddf86a4ca10b54.png" alt="image" data-base62-sha1="xIE7tOHdK1DwHSTM8t1DsmlvfkE" width="351" height="372"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">351×372 26.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3><a name="p-17289-nitrcorg-2" class="anchor" href="#p-17289-nitrcorg-2" aria-label="Heading link"></a><code>nitrc.org</code></h3>
<ul>
<li>Updated date of release associated with nitric download list.</li>
<li>Updated the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/ReleaseProcess#Update_external_website">Update_external_website</a> step of the Slicer Release Process with corresponding details.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/174d8a2b8b5b4bce2eab60f5f91b6a146faec465.png" data-download-href="/uploads/short-url/3k96OwNHKIIGdTQfHxbWNu7NOKh.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/174d8a2b8b5b4bce2eab60f5f91b6a146faec465_2_690x124.png" alt="image" data-base62-sha1="3k96OwNHKIIGdTQfHxbWNu7NOKh" width="690" height="124" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/174d8a2b8b5b4bce2eab60f5f91b6a146faec465_2_690x124.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/174d8a2b8b5b4bce2eab60f5f91b6a146faec465.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/174d8a2b8b5b4bce2eab60f5f91b6a146faec465.png 2x" data-dominant-color="9397C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">876×158 9.36 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #20 by @rkikinis (2018-11-01 21:05 UTC)

<p>we should update the <a href="http://slicer.org" rel="nofollow noopener">slicer.org</a> top page.</p>

---

## Post #21 by @rkikinis (2018-11-01 21:20 UTC)

<p>I downloaded slicer and installed it. Everything works like a charm on the MAC. No error messages, just the notification that the software was downloaded from <a href="http://kitware.com" rel="nofollow noopener">kitware.com</a></p>
<p>I am very happy. Thanks to all who contributed to this.</p>
<p>Best</p>
<p>Ron</p>

---

## Post #22 by @jcfr (2018-11-01 21:37 UTC)

<aside class="quote no-group" data-username="rkikinis" data-post="20" data-topic="4422">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rkikinis/48/791_2.png" class="avatar"> rkikinis:</div>
<blockquote>
<p>we should update the <a href="http://slicer.org">slicer.org</a> top page.</p>
</blockquote>
</aside>
<p>This is indeed the last step of the release process. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/ReleaseProcess#Publish_Slicer_Announcement">Publish_Slicer_Announcement</a></p>
<p>Unless you think differently, I suggest we finalize the update as soon as we are ready to publish the document “Slicer 4.10: Summary, Highlights and Changelog”. See <a href="https://discourse.slicer.org/t/slicer-4-10-summary-highlights-and-changelog/4610" class="inline-onebox">Slicer 4.10: Summary, Highlights and Changelog</a></p>

---

## Post #23 by @rkikinis (2018-11-01 21:55 UTC)

<p>Hi JC</p>
<p>Thanks for the clarifications.<br>
Sounds good.</p>
<p>Best</p>
<p>Ron</p>

---

## Post #24 by @Fernando (2018-11-04 17:34 UTC)

<p>I have updated the <code>brew</code> cask:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Homebrew/homebrew-cask/pull/54491">
  <header class="source">

      <a href="https://github.com/Homebrew/homebrew-cask/pull/54491" target="_blank" rel="noopener nofollow ugc">github.com/Homebrew/homebrew-cask</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Homebrew/homebrew-cask/pull/54491" target="_blank" rel="noopener nofollow ugc">Update slicer to 4.10.0.27501,896287</a>
      </h4>

    <div class="branches">
      <code>Homebrew:master</code> ← <code>fepegar:cask_repair_update-slicer</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2018-11-04" data-time="17:31:43" data-timezone="UTC">05:31PM - 04 Nov 18 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/fepegar" target="_blank" rel="noopener nofollow ugc">
            <img alt="fepegar" src="https://avatars.githubusercontent.com/u/12688084?v=4" class="onebox-avatar-inline" width="20" height="20">
            fepegar
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 2 additions and 2 deletions">
          <a href="https://github.com/Homebrew/homebrew-cask/pull/54491/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+2</span>
            <span class="removed">-2</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">After making all changes to the cask:

- [x] `brew cask audit --download {{cask_<span class="show-more-container"><a href="https://github.com/Homebrew/homebrew-cask/pull/54491" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">file}}` is error-free.
- [x] `brew cask style --fix {{cask_file}}` left no offenses.
- [x] The commit message includes the cask’s name and version.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #25 by @fedorov (2018-11-05 18:49 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> just realized that nightly packages are not still signed. I guess this was expected, but took me a bit by surprise.</p>

---

## Post #26 by @jcfr (2018-11-05 19:02 UTC)

<blockquote>
<p>nightly packages are not still signed</p>
</blockquote>
<p>That is correct.  Signing is a semi-automatic process requiring user interaction.</p>
<p>The good news is that we are now all the piece to move forward with setting up our automated signing infrastructure.</p>

---

## Post #29 by @jcfr (2019-01-10 16:59 UTC)

<p>Following this week hangout <a href="https://discourse.slicer.org/t/2019-1-7-hangout/5305/3?u=jcfr" class="inline-onebox">2019.1.7 Hangout</a>, Slicer 4.10.1 will be released next week.</p>

---
