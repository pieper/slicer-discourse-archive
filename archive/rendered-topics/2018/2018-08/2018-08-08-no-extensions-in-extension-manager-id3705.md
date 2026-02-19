---
topic_id: 3705
title: "No Extensions In Extension Manager"
date: 2018-08-08
url: https://discourse.slicer.org/t/3705
---

# No extensions in extension manager

**Topic ID**: 3705
**Date**: 2018-08-08
**URL**: https://discourse.slicer.org/t/no-extensions-in-extension-manager/3705

---

## Post #1 by @torquil (2018-08-08 11:49 UTC)

<p>Hi! After installing Slicer 4.9.0 2018-08-07, there are no extensions listed in the extension manager.</p>
<p>In the application settings, the “Extensions server URL” is <a href="http://slicer.kitware.com/midas3" rel="nofollow noopener">http://slicer.kitware.com/midas3</a>, which I have not changed.</p>
<p>In the extensions manager, I get the message: “No extensions found for win:64-bit, revision: ‘27339’. Please try a different combination”.</p>
<p>If I go to <a href="https://slicer.kitware.com/midas3/slicerappstore" rel="nofollow noopener">https://slicer.kitware.com/midas3/slicerappstore</a> with a web browser, I get the same error.</p>
<p>This is the whole Slicer error log:</p>
<p>“Session start time …: 2018-08-08 13:37:45<br>
Slicer version …: 4.9.0-2018-08-07 (revision 27339) win-amd64 - installed release<br>
Operating system …: Windows / Professional / (Build 9200) - 64-bit<br>
Memory …: 16262 MB physical, 16262 MB virtual<br>
CPU …: GenuineIntel , 8 cores, 8 logical processors<br>
VTK configuration …: OpenGL2 rendering, TBB threading<br>
Developer mode enabled …: no<br>
Prefer executable CLI …: yes<br>
Additional module paths …: (none)<br>
Popen([‘git’, ‘version’], cwd=C:\Program Files\Slicer 4.9.0-2018-08-07, universal_newlines=False, shell=None)<br>
Popen([‘git’, ‘version’], cwd=C:\Program Files\Slicer 4.9.0-2018-08-07, universal_newlines=False, shell=None)<br>
Scripted subject hierarchy plugin registered: Annotations<br>
Scripted subject hierarchy plugin registered: SegmentEditor<br>
Scripted subject hierarchy plugin registered: SegmentStatistics<br>
Switch to module: “Welcome”<br>
An OpenGL Core Profile was requested, but it is not supported on the current platform. Falling back to a non-Core profile. Note that this might cause rendering issues.”</p>
<p>Best regards,<br>
Torquil Sørensen</p>

---

## Post #2 by @Sunny (2018-08-08 10:29 UTC)

<p>I am facing this same problem (“No extensions found for win:64-bit, revision: ‘27339’. Please try a different combination”) with the latest Nightly build which I downloaded from the Slicer homepage.</p>
<p>Appreciate your help, thanks!</p>

---

## Post #3 by @cpinter (2018-08-08 10:50 UTC)

<p>Indeed, for some reason there are only extensions for Linux and Mac at this moment. It is possible that the factory computers have not finished the builds yet. You can wait to see if this is true, or download yesterday’s nightly that looks OK on the dashboard:<br>
<a href="http://download.slicer.org/?offset=-1" class="onebox" target="_blank">http://download.slicer.org/?offset=-1</a></p>

---

## Post #4 by @ihnorton (2018-08-08 13:49 UTC)

<p>note: I moved two posts in to this thread from an old one (<a href="https://discourse.slicer.org/t/no-extensions-for-latest-nightly/865/5">No extensions for latest nightly</a>)</p>
<p><a class="mention" href="/u/torquil">@torquil</a> please see suggestion above.</p>

---

## Post #5 by @Sam_Horvath (2018-08-08 14:01 UTC)

<p>Windows extension builds are now coming up from the factory machine.  It seems to be later than they have been in the past.  I will take a look at the factory system log to see if something weird happened.  If not, perhaps we should consider moving the factory build start earlier.</p>

---

## Post #6 by @torquil (2018-08-09 11:03 UTC)

<p>Thanks people, it is working again now.</p>

---

## Post #7 by @Sam_Horvath (2018-08-09 14:58 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a></p>
<p>So I think we should consider moving the start time earlier for the nightly build, or changing up the build order.  Currently, we build the stable extensions before the preview (except if its Sunday …?).  Each build (slicer, stable extensions, preview extensions) appears to be taking ~4 hrs according to the logs, so most days the preview extensions don’t finish until late morning.</p>

---

## Post #8 by @jcfr (2018-08-09 15:33 UTC)

<p>This was originally done to accommodate <a class="mention" href="/u/fedorov">@fedorov</a>. See <a href="https://github.com/Slicer/DashboardScripts/commit/41b143d1fa3e9c665498918f3361c00deb8938ca">Slicer/DashboardScripts@41b143d1f</a> for more background</p>
<p>Also, for either the Preview or Stable extension, considering that some extension used branches like <code>origin/master-XY</code> or <code>origin/master</code>, we have no way of knowing if we can skip the build of the index or not.</p>
<p>We could also update the nighty build time. It is currently set in <a href="https://github.com/Slicer/Slicer/blob/master/CTestConfig.cmake">Slicer/CTestConfig.cmake</a> as <code>3:00:00 UTC</code> (<code>23:00 EDT</code>). May be we could start all nightly build at (8pm) <code>20:00 EDT</code> (<code>0:00:00 UTC</code>) ?</p>
<p>For reference, the order of build is specified here:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/DashboardScripts/blob/cbacb3abab4aff9e6e577d23d2716c793a299766/overload.bat#L36-L44" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/DashboardScripts/blob/cbacb3abab4aff9e6e577d23d2716c793a299766/overload.bat#L36-L44" target="_blank">Slicer/DashboardScripts/blob/cbacb3abab4aff9e6e577d23d2716c793a299766/overload.bat#L36-L44</a></h4>
<pre class="onebox"><code class="lang-bat"><ol class="start lines" start="36" style="counter-reset: li-counter 35 ;">
<li>call :fastdel "D:\D\P\S-0-E-b"</li>
<li>call :fastdel "D:\D\S\S-481-E-b"</li>
<li>if "%IS_WEEKEND%"=="1" (</li>
<li>call :slicerextensions_preview_nightly</li>
<li>call :slicerextensions_stable_nightly</li>
<li>) else (</li>
<li>call :slicerextensions_stable_nightly</li>
<li>call :slicerextensions_preview_nightly</li>
<li>)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #9 by @fedorov (2018-08-09 15:37 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="8" data-topic="3705">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p>This was originally done to accommodate <a class="mention" href="/u/fedorov">@fedorov</a></p>
</blockquote>
</aside>
<p><a class="mention" href="/u/jcfr">@jcfr</a>, according to <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a>:</p>
<aside class="quote no-group" data-username="Sam_Horvath" data-post="7" data-topic="3705">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar"> Sam_Horvath:</div>
<blockquote>
<p>Currently, we build the stable extensions before the preview</p>
</blockquote>
</aside>
<p>However, the comment from the commit you mentioned states that it should implement the behavior suggested by Sam:</p>
<blockquote>
<p>Lacking automatic detection of the 4.5 extensions index changes and<br>
building of the modified extensions only, it is proposed that the order<br>
between 4.5 and nightly is changed manually on as needed basis. It is<br>
expected that nightly builds will be changing at a faster pace than 4.5,<br>
thus it is natural to have nightly built in the first place.</p>
</blockquote>
<p>So I think something changed since that commit, if indeed stable extensions are built before the preview.</p>

---

## Post #10 by @lassoan (2018-08-09 15:51 UTC)

<p>Another option would be to show yesterday’s nightly build (…?offset=-1) on the download page. Developers and advanced users would know that a more recent, potentially incomplete build is available for early testing.</p>

---

## Post #11 by @Sam_Horvath (2018-08-09 16:20 UTC)

<p>The change to building stable before nighlt/preview on weekedays occured here:</p><aside class="onebox githubcommit" data-onebox-src="https://github.com/Slicer/DashboardScripts/commit/d8507c2983659f0293705f613c610160068de333#diff-fa3827b70d282260aba2befb7f945454">
  <header class="source">

      <a href="https://github.com/Slicer/DashboardScripts/commit/d8507c2983659f0293705f613c610160068de333#diff-fa3827b70d282260aba2befb7f945454" target="_blank" rel="noopener">github.com/Slicer/DashboardScripts</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/DashboardScripts/commit/d8507c2983659f0293705f613c610160068de333" target="_blank" rel="noopener">nightly script: Update to build Slicer 4.8 extensions first</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2017-10-19" data-time="04:33:20" data-timezone="UTC">04:33AM - 19 Oct 17 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jcfr" target="_blank" rel="noopener">
          <img alt="jcfr" src="https://avatars.githubusercontent.com/u/219043?v=4" class="onebox-avatar-inline" width="20" height="20">
          jcfr
        </a>
      </div>

      <div class="lines" title="changed 3 files with 12 additions and 14 deletions">
        <a href="https://github.com/Slicer/DashboardScripts/commit/d8507c2983659f0293705f613c610160068de333" target="_blank" rel="noopener">
          <span class="added">+12</span>
          <span class="removed">-14</span>
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

## Post #12 by @lassoan (2018-08-09 22:41 UTC)

<p>If there is no specific technical reason to build stable extension first, I would change the order to build nightly Slicer core and extensions first.</p>

---
