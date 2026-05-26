---
topic_id: 47098
title: "Slicer 5 11 0 Crashes Immediately When Switching To Nnintera"
date: 2026-05-20
url: https://discourse.slicer.org/t/47098
---

# Slicer 5.11.0 crashes immediately when switching to nnInteractive module

**Topic ID**: 47098
**Date**: 2026-05-20
**URL**: https://discourse.slicer.org/t/slicer-5-11-0-crashes-immediately-when-switching-to-nninteractive-module/47098

---

## Post #1 by @aabrown100-git (2026-05-20 18:27 UTC)

<p>Using Slicer 5.11.0 on 2026 Macbook pro, M5 Pro chip.</p>
<p>After installing the nnInteractive extension and restarting Slicer, when I switch to the nnInteractive module, it tries to install some dependencies. Almost immediately, Slicer quits.</p>
<p>No issue when performing the same steps in Slicer 5.10.0.</p>
<p>Perhaps related to recent version compatibility changes to nnUnet? <a href="https://discourse.slicer.org/t/nnunet-fails-with-modulenotfounderror-no-module-named-torchvision-ops/46802/5" class="inline-onebox">nnUNet fails with ModuleNotFoundError: No module named 'torchvision.ops' - #5 by lassoan</a></p>

---

## Post #2 by @lassoan (2026-05-20 19:14 UTC)

<p>nnInteractive extension barely installs any dependencies, so I’m surprised that it runs into issues. It just needs <code>requests_toolbelt</code>, <code>scikit-image</code>, and (for testing) <code>matplotlib</code>. Could you please install these manually, for example: <code>pip_install("requests_toolbelt")</code>, and see if any of them causing trouble?</p>

---

## Post #3 by @aabrown100-git (2026-05-21 21:27 UTC)

<p>Thanks for the suggestion. I installed <code>requests_toolbelt</code>, <code>scikit-image</code> and <code>matplotlib</code> manually through the Python console (e.g. <code>slicer.util.pip_install("requests_toolbelt")</code>) and that worked fine. In fact, when I switched back to <code>nnInteractive</code> module, it didn’t try to install dependencies and didn’t crash at all. And the module worked perfectly fine.</p>
<p>This is what Codex found regarding the crash</p>
<pre><code class="lang-auto">My current suspicion is that this is a macOS/Slicer-preview startup UI issue in nnInteractive, not a missing requests_toolbelt import.

In the extension code, SlicerNNInteractiveWidget.setup() immediately calls self.install_dependencies() before the rest of the module UI is initialized. That dependency-install path can create a modal Qt progress dialog via slicer.util.createProgressDialog(...).

From the crash report, the failure happens while Slicer is switching into the module and building its widget. The backtrace goes through:

qSlicerAbstractCoreModule::widgetRepresentation()
qSlicerModulePanel::setModule(QString const&amp;)
PythonQt...
QDialog::setVisible(bool)
QWidgetPrivate::setVisible(bool)
QWidget::create(...)
QWindowPrivate::create(...)
-[NSWindow initWithContentRect:styleMask:backing:defer:]
-[NSPanel _initContent:styleMask:backing:defer:contentView:]
Then AppKit raises an Objective-C exception and Slicer aborts with SIGABRT.

So the crash appears to be happening in the module’s dependency-install/dialog creation path during startup, rather than later in the server/networking code.
</code></pre>

---

## Post #4 by @lassoan (2026-05-23 17:42 UTC)

<p>I’ve submitted a pull request that reworks the dependency installation, which should resolve the hanging that you observed.</p>
<p>In this PR, I’ve also implemented automatic installation of the nnInteractive server on Linux and Windows, so the user does not need to manually install anything.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/coendevente/SlicerNNInteractive/pull/95">
  <header class="source">

      <a href="https://github.com/coendevente/SlicerNNInteractive/pull/95" target="_blank" rel="noopener">github.com/coendevente/SlicerNNInteractive</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/coendevente/SlicerNNInteractive/pull/95" target="_blank" rel="noopener">Add internal server option to avoid asking users to set up a server manually (#95)</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>lassoan:add-internal-server</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-05-23" data-time="16:19:31" data-timezone="UTC">04:19PM - 23 May 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="2 commits changed 7 files with 693 additions and 315 deletions">
          <a href="https://github.com/coendevente/SlicerNNInteractive/pull/95/files" target="_blank" rel="noopener">
            <span class="added">+693</span>
            <span class="removed">-315</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This pull request automatically sets up and starts/stops the nnInteractive serve<span class="show-more-container"><a href="https://github.com/coendevente/SlicerNNInteractive/pull/95" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">r and all its dependencies on compatible computers. The user can simply install the Slicer extension and start segmenting.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Jean_Pinson (2026-05-26 08:10 UTC)

<p>Hello <a class="mention" href="/u/aabrown100-git">@aabrown100-git</a> !! Does nninteractive works on mac ? I though it was dedicated for nvidia GPU !?</p>

---
