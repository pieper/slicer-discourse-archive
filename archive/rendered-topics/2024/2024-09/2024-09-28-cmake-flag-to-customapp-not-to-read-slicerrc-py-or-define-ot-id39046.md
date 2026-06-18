---
topic_id: 39046
title: "CMake Flag to CustomApp not to read `slicerrc.py` or define other file?"
date: 2024-09-28
url: https://discourse.slicer.org/t/39046
last_bumped: 2026-06-17T11:43:56.849Z
---

# CMake Flag to CustomApp not to read `slicerrc.py` or define other file?

**Topic ID**: 39046
**Date**: 2024-09-28
**URL**: https://discourse.slicer.org/t/cmake-flag-to-customapp-not-to-read-slicerrc-py-or-define-other-file/39046

---

## Post #1 by @apparrilla (2024-09-28 17:10 UTC)

<p>Hi everyone!<br>
I´ve some trouble betweeen CustomApp and normal Slicer because first one read slicerrc.py file. Is ther any way to complie CustomApp not to read this file or define a custom rc file to be saved instead?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2024-09-29 03:39 UTC)

<p>Good catch! Custom Slicer applications should be completely independent from standard 3D Slicer applications. By default, a custom application’s startup script name should be determined by the application name, such as <code>.&lt;applicationname&gt;rc.py</code>.</p>
<p>It should be also possible to disable using a startup script for a custom application. It is probably already feasible by setting a custom environment variable in the launcher or by passing <code>--ignore-slicerrc</code> argument to the main application in the launcher, but it would be nice to have a dedicated CMake option or application configuration flag for it.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> scary do you think?</p>

---

## Post #3 by @apparrilla (2024-09-29 06:30 UTC)

<p>Even should be nice to link it to “Slicer_STORE_SETTINGS_IN_APPLICATION_HOME_DIR” flag not to loose portability…</p>

---

## Post #4 by @pieper (2024-09-29 12:19 UTC)

<p>Agreed, the custom app should be completely independent of Slicer in terms of settings, rc file, etc.</p>

---

## Post #5 by @jcfr (2024-09-30 13:44 UTC)

<p>In the past, we have applied a patch like the following. Generalizing as discussed above would indeed be sensible.</p>
<pre data-code-wrap="diff"><code class="lang-diff">diff --git a/Base/QTCore/qSlicerCoreCommandOptions.cxx b/Base/QTCore/qSlicerCoreCommandOptions.cxx
index 41bc603fb53..df309efdb5b 100644
--- a/Base/QTCore/qSlicerCoreCommandOptions.cxx
+++ b/Base/QTCore/qSlicerCoreCommandOptions.cxx
@@ -128,8 +128,9 @@ bool qSlicerCoreCommandOptions::ignoreRest() const
 bool qSlicerCoreCommandOptions::ignoreSlicerRC()const
 {
   Q_D(const qSlicerCoreCommandOptions);
-  return d-&gt;ParsedArgs.value("ignore-slicerrc").toBool() ||
-      this-&gt;isTestingEnabled();
+  //return d-&gt;ParsedArgs.value("ignore-slicerrc").toBool() ||
+  //    this-&gt;isTestingEnabled();
+  return true;
 }
</code></pre>

---

## Post #6 by @cpinter (2024-09-30 13:57 UTC)

<p><a class="mention" href="/u/apparrilla">@apparrilla</a> I have been using conditions like this to differentiate how the slicerrc file is used in each case. This may be useful in the short term.</p>
<pre><code class="lang-auto">if slicer.app.mainApplicationName == 'Slicer':
</code></pre>
<p>If we are redesigning this part, I suggest moving the file to another place, to decrease the number of paths where relevant Slicer related files are stored, and to make it easier to find files for any given application. More concretely, the user folder’s root only contains this one file, but I think we could move it to where the app’s main configuration file is located: <code>AppData/Roaming/[org.name]</code> (on Windows). Then we may want to change its name as well to correspond to the application name.</p>

---

## Post #7 by @apparrilla (2026-02-11 17:44 UTC)

<p>Hi everyone again!</p>
<p>Is there any update for this task? Is there any new flag to add to CMakeList.txt to redirect my CustomSlicer to an internal rc.py saved in anywhere as c:/user/applicationname/?</p>
<p>Thanks on advance!</p>

---

## Post #8 by @jamesobutler (2026-06-17 11:43 UTC)

<p>I have issued the following PR to address items mentioned here so that custom apps use a custom app named rc file or can configure in a build option to turn off rc file support.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/9240">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/9240" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/9240" target="_blank" rel="noopener nofollow ugc">ENH: Add unique Slicerrc file for custom apps with ability to turn off (#9240)</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>jamesobutler:slicerrc-custom-apps</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-06-17" data-time="11:42:30" data-timezone="UTC">11:42AM - 17 Jun 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/jamesobutler" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
            jamesobutler
          </a>
        </div>

        <div class="lines" title="2 commits changed 6 files with 51 additions and 16 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/9240/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+51</span>
            <span class="removed">-16</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This addresses the items discussed in https://discourse.slicer.org/t/cmake-flag-<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/9240" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">to-customapp-not-to-read-slicerrc-py-or-define-other-file/39046.

1. Per [comment](https://discourse.slicer.org/t/cmake-flag-to-customapp-not-to-read-slicerrc-py-or-define-other-file/39046/6?u=jamesobutler) the default location when no existing rc files exists is now the slicerHome location rather than in the user directory root.
2. .slicerrc.py is no longer used by Slicer custom applications, but instead use their own application named rc file `.&lt;mainApplicationName&gt;rc.py`. 
3. Slicer custom applications can also configure to turn off application RC startup script usage entirely with a new build option `Slicer_USE_SLICERRC`. This is by default on, but can be configured to be turned off. When the app configures it off, the settings dialog entry for specifying the startup path location is hidden as well as the command line flag `ignore-slicerrc` not being added as it would be irrelevant.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
