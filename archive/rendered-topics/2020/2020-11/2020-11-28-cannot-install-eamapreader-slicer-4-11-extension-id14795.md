# Cannot install EAMapReader-Slicer-4.11 extension 

**Topic ID**: 14795
**Date**: 2020-11-28
**URL**: https://discourse.slicer.org/t/cannot-install-eamapreader-slicer-4-11-extension/14795

---

## Post #1 by @jsalas424 (2020-11-28 03:08 UTC)

<p>Problem report for Slicer 4.11.20200930 macosx-amd64</p>
<p>I am trying to install the following extension: <a href="https://github.com/stephan1312/SlicerEAMapReader#readme" rel="noopener nofollow ugc">https://github.com/stephan1312/SlicerEAMapReader#readme</a></p>
<p>Expected Behavior:</p>
<p>In the extension manager select “Install from file” and install the EAMapReader.zip file.</p>
<p>Actual Behavior:</p>
<p>Fails to install extension. Logs attached. I renamed the file “EAMapReader.zip” but still nothing. I moved all the files to my desktop and tried from there - no luck.</p>
<pre><code class="lang-auto">[DEBUG][Qt] 27.11.2020 17:07:14 [] (unknown:0) - Session start time .......: 2020-11-27 17:07:14
[DEBUG][Qt] 27.11.2020 17:07:14 [] (unknown:0) - Slicer version ...........: 4.11.20200930 (revision 29402 / 002be18) macosx-amd64 - installed release
[DEBUG][Qt] 27.11.2020 17:07:14 [] (unknown:0) - Operating system .........: Mac OS X / 10.15.7 / 19H2 - 64-bit
[DEBUG][Qt] 27.11.2020 17:07:14 [] (unknown:0) - Memory ...................: 8192 MB physical, 3072 MB virtual
[DEBUG][Qt] 27.11.2020 17:07:14 [] (unknown:0) - CPU ......................: GenuineIntel Intel(R) Core(TM) i7-8557U CPU @ 1.70GHz, 4 cores, 8 logical processors
[DEBUG][Qt] 27.11.2020 17:07:14 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, Sequential threading
[DEBUG][Qt] 27.11.2020 17:07:14 [] (unknown:0) - Qt configuration .........: version 5.15.1, with SSL, requested OpenGL 3.2 (core profile)
[DEBUG][Qt] 27.11.2020 17:07:14 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 27.11.2020 17:07:14 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 27.11.2020 17:07:14 [] (unknown:0) - Application path .........: /Applications/Slicer.app/Contents/MacOS
[DEBUG][Qt] 27.11.2020 17:07:14 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 27.11.2020 17:07:15 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pydicom/datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword...
[DEBUG][Python] 27.11.2020 17:07:16 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 27.11.2020 17:07:16 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 27.11.2020 17:07:16 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 27.11.2020 17:07:16 [] (unknown:0) - Switch to module:  "Welcome"
[CRITICAL][FD] 27.11.2020 17:07:32 [] (unknown:0) - [37846:123139:1127/170732.996236:ERROR:gl_context_cgl.cc(118)] Error creating context.
[WARNING][Qt] 27.11.2020 17:07:35 [] (unknown:0) - A cookie associated with a cross-site resource at http://www.nitrc.org/ was set without the `SameSite` attribute. A future release of Chrome will only deliver cookies with cross-site requests if they are set with `SameSite=None` and `Secure`. You can review cookies in developer tools under Application&gt;Storage&gt;Cookies and see more details at https://www.chromestatus.com/feature/5088147346030592 and https://www.chromestatus.com/feature/5633521622188032.
[CRITICAL][Qt] 27.11.2020 17:07:49 [] (unknown:0) - ctk::copyDirRecursively: Failed to copy nonexistent directory "/Applications/Slicer.app/Contents/Extensions-29402/EAMapReader/SlicerEAMapReader-master/Slicer.app/Contents/Extensions-29402/EAMapReader"
[CRITICAL][Qt] 27.11.2020 17:07:49 [] (unknown:0) - "Failed to copy directory /Applications/Slicer.app/Contents/Extensions-29402/EAMapReader/SlicerEAMapReader-master/Slicer.app/Contents/Extensions-29402/EAMapReader into directory /Applications/Slicer.app/Contents/Extensions-29402/EAMapReader-XXXXXX"
[CRITICAL][Qt] 27.11.2020 17:08:22 [] (unknown:0) - ctk::copyDirRecursively: Failed to copy nonexistent directory "/Applications/Slicer.app/Contents/Extensions-29402/EAMapReader/EAMapReader-Slicer-4.11/Slicer.app/Contents/Extensions-29402/EAMapReader"
[CRITICAL][Qt] 27.11.2020 17:08:22 [] (unknown:0) - "Failed to copy directory /Applications/Slicer.app/Contents/Extensions-29402/EAMapReader/EAMapReader-Slicer-4.11/Slicer.app/Contents/Extensions-29402/EAMapReader into directory /Applications/Slicer.app/Contents/Extensions-29402/EAMapReader-XXXXXX"
[CRITICAL][Qt] 27.11.2020 17:09:05 [] (unknown:0) - ctk::copyDirRecursively: Failed to copy nonexistent directory "/Applications/Slicer.app/Contents/Extensions-29402/EAMapReader/EAMapReader-Slicer-4.11/Slicer.app/Contents/Extensions-29402/EAMapReader"
[CRITICAL][Qt] 27.11.2020 17:09:05 [] (unknown:0) - "Failed to copy directory /Applications/Slicer.app/Contents/Extensions-29402/EAMapReader/EAMapReader-Slicer-4.11/Slicer.app/Contents/Extensions-29402/EAMapReader into directory /Applications/Slicer.app/Contents/Extensions-29402/EAMapReader-XXXXXX"
[CRITICAL][Qt] 27.11.2020 17:09:42 [] (unknown:0) - ctk::copyDirRecursively: Failed to copy nonexistent directory "/Applications/Slicer.app/Contents/Extensions-29402/EAMapReader/SlicerEAMapReader-master/Slicer.app/Contents/Extensions-29402/EAMapReader"
[CRITICAL][Qt] 27.11.2020 17:09:42 [] (unknown:0) - "Failed to copy directory /Applications/Slicer.app/Contents/Extensions-29402/EAMapReader/SlicerEAMapReader-master/Slicer.app/Contents/Extensions-29402/EAMapReader into directory /Applications/Slicer.app/Contents/Extensions-29402/EAMapReader-XXXXXX"
[CRITICAL][Qt] 27.11.2020 17:12:01 [] (unknown:0) - ctk::copyDirRecursively: Failed to copy nonexistent directory "/Applications/Slicer.app/Contents/Extensions-29402/EAMapReader/EAMapReader-Slicer-4.11/Slicer.app/Contents/Extensions-29402/EAMapReader"
[CRITICAL][Qt] 27.11.2020 17:12:01 [] (unknown:0) - "Failed to copy directory /Applications/Slicer.app/Contents/Extensions-29402/EAMapReader/EAMapReader-Slicer-4.11/Slicer.app/Contents/Extensions-29402/EAMapReader into directory /Applications/Slicer.app/Contents/Extensions-29402/EAMapReader-XXXXXX"
[CRITICAL][Qt] 27.11.2020 17:14:28 [] (unknown:0) - ctk::copyDirRecursively: Failed to copy nonexistent directory "/Applications/Slicer.app/Contents/Extensions-29402/EAMapReader/EAMapReader-Slicer-4.11/Slicer.app/Contents/Extensions-29402/EAMapReader"
[CRITICAL][Qt] 27.11.2020 17:14:28 [] (unknown:0) - "Failed to copy directory /Applications/Slicer.app/Contents/Extensions-29402/EAMapReader/EAMapReader-Slicer-4.11/Slicer.app/Contents/Extensions-29402/EAMapReader into directory /Applications/Slicer.app/Contents/Extensions-29402/EAMapReader-XXXXXX"
</code></pre>

---

## Post #2 by @jsalas424 (2020-11-28 16:58 UTC)

<p>Dev confirmed that installation from .zip has issues on Mac. They have provided guidance to successfully install it here:<br>
</p><aside class="onebox githubissue">
  <header class="source">
      <a href="https://github.com/stephan1312/SlicerEAMapReader/issues/2#issuecomment-735048915" target="_blank" rel="noopener nofollow ugc">github.com/stephan1312/SlicerEAMapReader</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/stephan1312/SlicerEAMapReader/issues/2#issuecomment-735048915" target="_blank" rel="noopener nofollow ugc">Can't install extension "Failed to copy directory" - MacOS Catalina </a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-11-27" data-time="22:13:43" data-timezone="UTC">10:13PM - 27 Nov 20 UTC</span>
      </div>

        <div class="date">
          closed <span class="discourse-local-date" data-format="ll" data-date="2020-11-28" data-time="13:07:20" data-timezone="UTC">01:07PM - 28 Nov 20 UTC</span>
        </div>

      <div class="user">
        <a href="https://github.com/Jsalas424" target="_blank" rel="noopener nofollow ugc">
          <img alt="Jsalas424" src="https://avatars3.githubusercontent.com/u/51519895?v=4" class="onebox-avatar-inline" width="20" height="20">
          Jsalas424
        </a>
      </div>
    </div>
  </div>
</div>

<div class="github-row">
  <p class="github-content">Hi,
I downloaded SlicerEAMapReader-master.zip and tried to install your extension but the following error:
Failed to copy directory /Applications/Slicer.app/Contents/Extensions-29402/EAMapReader/SlicerEAMapReader-master/Slicer.app/Contents/Extensions-29402/EAMapReader into directory /Applications/Slicer.app/Contents/Extensions-29402/EAMapReader-XXXXXX
I unzipped...</p>
</div>

<div class="labels">
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
