---
topic_id: 16228
title: "Slicer 4 11 On M1 Not Loading Mrb File"
date: 2021-02-26
url: https://discourse.slicer.org/t/16228
---

# Slicer 4.11 on M1 not loading .mrb file

**Topic ID**: 16228
**Date**: 2021-02-26
**URL**: https://discourse.slicer.org/t/slicer-4-11-on-m1-not-loading-mrb-file/16228

---

## Post #1 by @mohammed_alshakhas (2021-02-26 06:19 UTC)

<p>Problem report for Slicer 4.11.20200930 macosx-amd64: [please describe expected and actual behavior]</p>
<p>i cant load the file , the hierarchy shows nothing being loaded as well .</p>
<p>its quite frustrating ! i need urgent help with this</p>
<p>log<br>
[DEBUG][Qt] 26.02.2021 09:15:02 [] (unknown:0) - Session start time …: 2021-02-26 09:15:02<br>
[DEBUG][Qt] 26.02.2021 09:15:02 [] (unknown:0) - Slicer version …: 4.11.20200930 (revision 29402 / 002be18) macosx-amd64 - installed release<br>
[DEBUG][Qt] 26.02.2021 09:15:02 [] (unknown:0) - Operating system …: macOS / 11.2.1 / 20D74 - 64-bit<br>
[DEBUG][Qt] 26.02.2021 09:15:02 [] (unknown:0) - Memory …: 8192 MB physical, 9216 MB virtual<br>
[DEBUG][Qt] 26.02.2021 09:15:02 [] (unknown:0) - CPU …:  Apple M1, 8 cores, 8 logical processors<br>
[DEBUG][Qt] 26.02.2021 09:15:02 [] (unknown:0) - VTK configuration …: OpenGL2 rendering, Sequential threading<br>
[DEBUG][Qt] 26.02.2021 09:15:02 [] (unknown:0) - Qt configuration …: version 5.15.1, with SSL, requested OpenGL 3.2 (core profile)<br>
[DEBUG][Qt] 26.02.2021 09:15:02 [] (unknown:0) - Developer mode enabled …: no<br>
[DEBUG][Qt] 26.02.2021 09:15:02 [] (unknown:0) - Prefer executable CLI …: yes<br>
[DEBUG][Qt] 26.02.2021 09:15:02 [] (unknown:0) - Application path …: /Applications/Slicer.app/Contents/MacOS<br>
[DEBUG][Qt] 26.02.2021 09:15:02 [] (unknown:0) - Additional module paths …: (none)<br>
[DEBUG][Python] 26.02.2021 09:15:03 [Python] (/Applications/Slicer.app/Contents/lib/Python/lib/python3.6/site-packages/pydicom/datadict.py:432) - Reversing DICOM dictionary so can look up tag from a keyword…<br>
[DEBUG][Python] 26.02.2021 09:15:04 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations<br>
[DEBUG][Python] 26.02.2021 09:15:04 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor<br>
[DEBUG][Python] 26.02.2021 09:15:04 [Python] (/Applications/Slicer.app/Contents/lib/Slicer-4.11/qt-scripted-modules/SubjectHierarchyPlugins/AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics<br>
[DEBUG][Qt] 26.02.2021 09:15:04 [] (unknown:0) - Switch to module:  “Welcome”<br>
[WARNING][Qt] 26.02.2021 09:15:26 [] (unknown:0) - QGestureManager::deliverEvent: could not find the target for gesture<br>
[DEBUG][Qt] 26.02.2021 09:15:44 [] (unknown:0) - Switch to module:  “Data”<br>
[WARNING][Qt] 26.02.2021 09:15:58 [] (unknown:0) - QGestureManager::deliverEvent: could not find the target for gesture</p>

---

## Post #2 by @pieper (2021-02-26 13:15 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="1" data-topic="16228">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>CPU …: Apple M1, 8 cores, 8 logical processors</p>
</blockquote>
</aside>
<p>This is new territory - do other things in Slicer work as expected on this machine?  Are you able to open the mrb file on other machines?</p>

---

## Post #3 by @mohammed_alshakhas (2021-02-26 13:17 UTC)

<p>it was ok till installed 4.11 .<br>
still able to do full work , like i started the work fine . the issue is only when i load saved file in .mrb</p>

---

## Post #4 by @lassoan (2021-02-26 13:39 UTC)

<p>Maybe the temporary folder is not writable. Please check if latest Slicer Preview Release works well (save and load the scene using this same Slicer version).</p>

---

## Post #5 by @mohammed_alshakhas (2021-02-26 13:41 UTC)

<p>can you explain how can i do that  please ?</p>

---

## Post #6 by @lassoan (2021-02-26 13:53 UTC)

<p>You can install <em>Preview Release</em> from <a href="https://download.slicer.org/">here</a> and then check if scene saving and loading works well. This new Slicer version automatically creates a new temporary folder if the current one is not writable.</p>

---

## Post #7 by @mohammed_alshakhas (2021-02-26 14:00 UTC)

<p>did that already , didn’t work <img src="https://emoji.discourse-cdn.com/twitter/cry.png?v=9" title=":cry:" class="emoji" alt=":cry:"></p>

---

## Post #8 by @lassoan (2021-02-26 14:02 UTC)

<p>You can write me a private message (click on my name and then on the email icon) if you are available now for a call with screen sharing.</p>

---

## Post #9 by @lassoan (2021-02-26 14:25 UTC)

<p>We had a quick call and it turned out that the remote cache folder location was not writable. Choosing a writable location fixed the problem.</p>
<p>The latest Slicer Preview Release detected the error and explained what do to in the error popup’s details section. However, probably many users would not read through those messages, so we shouls resolve such errors automatically.</p>
<p>I’ll implement the same solution as for the temp folder - check at startup if the folder exists and writable and create a new folder if it is not.</p>

---

## Post #10 by @lassoan (2021-02-26 17:43 UTC)

<p>An enhancement is now implemented to automatically update the cache folder if it is detected that it is invalid (not writable).</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/pull/5487" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/pull/5487" target="_blank" rel="noopener">ENH: Ensure that remote cache folder is writable</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>lassoan:fix-invalid-cache-folder</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-02-26" data-time="17:42:23" data-timezone="UTC">05:42PM - 26 Feb 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="2 commits changed 3 files with 92 additions and 15 deletions">
        <a href="https://github.com/Slicer/Slicer/pull/5487/files" target="_blank" rel="noopener">
          <span class="added">+92</span>
          <span class="removed">-15</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
