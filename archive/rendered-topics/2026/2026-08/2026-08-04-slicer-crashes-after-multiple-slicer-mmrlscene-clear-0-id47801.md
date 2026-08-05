---
topic_id: 47801
title: "Slicer crashes after multiple slicer.mmrlScene.Clear(0)"
date: 2026-08-04
url: https://discourse.slicer.org/t/47801
last_bumped: 2026-08-04T15:52:41.050Z
---

# Slicer crashes after multiple slicer.mmrlScene.Clear(0)

**Topic ID**: 47801
**Date**: 2026-08-04
**URL**: https://discourse.slicer.org/t/slicer-crashes-after-multiple-slicer-mmrlscene-clear-0/47801

---

## Post #1 by @Deep_Learning (2026-08-04 14:02 UTC)

<p>When processing numerous studies with a Clear(0) after each, I eventually get a fatal exception crash.</p>
<p>Work flow is define convenience functions in the python console, (load mrb, process, save, Clear, repeat).</p>
<p>Of course I could restart() rather than clear.</p>
<p>Is there something else that I can clear in the python console?  I would like to keep my defined python functions and not restart due to the restart time.  Of course I know that I could define the functions in .slicerrc.py and they would be there after restart.</p>

---

## Post #2 by @pieper (2026-08-04 15:52 UTC)

<p>If you can come up with specific steps to replicate the crash you should file a bug report.  That would be the best for everyone.</p>
<p>If you just want to clear the text from the python console you can use <code>slicer.app.pythonConsole().reset()</code></p>
<p>Yes, .slicerrc.py would be a good way to get your functions included at startup.</p>
<p>Regarding restart time that is a pain point we are actively working on,  See:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/9332">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/9332" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/9332" target="_blank" rel="noopener">PERF: Parallel file prefetching at startup (#9332)</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>lassoan:parallel-file-prefetching-at-startup</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-08-04" data-time="06:06:35" data-timezone="UTC">06:06AM - 04 Aug 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="1 commits changed 12 files with 1363 additions and 30 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/9332/files" target="_blank" rel="noopener">
            <span class="added">+1363</span>
            <span class="removed">-30</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">This pull request implements parallel prefetching of libraries, which makes appl<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/9332" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">ication startup about 5 seconds faster on Windows.

At application startup, thousands of files are read from disk and some go through heavy processing (e.g., libraries are scanned for malware before being loaded). This is mostly done on a single thread, without saturating disk and CPU resources.

This commit adds a file prefetcher component that reads a list of files from disk in parallel, to make loading of those files later during startup faster.

On Windows the first time a shared library is mapped after it has been created or modified (which includes the first launch after an installation and the first after a reboot), the Microsoft Defender anti-malware filter scans the whole file before the mapping completes. The scan is CPU bound and far outweighs the read. The loader maps libraries one at a time, on the thread that needs them, so the scans are serialized even though the scanning service can run them in parallel. Therefore, on Windows, prefetching all shared library files in parallel makes the cold application startup (i.e., after a reboot) up to about 5-10 seconds faster. Therefore, prefetching is enabled by default on Windows.

The same mechanism on macOS, only results in modest improvement (about 0.4 seconds), because malware and signature scanning only happens once, after installation. The operating system checks all signatures on a single thread, so making this operation parallel does not decrease the startup time. Therefore, prefetching is disabled by default on macOS.

There has been no thorough testing on Linux, but it seems that library loading is supposed to be already fast on Linux, so significant startup speed improvement is only expected in certain environments (e.g., slow network drives). Therefore, prefetching is disabled by default on Linux.

Whole files are read rather than a prefix, and read rather than mapped as data files, because reading just the first 1MB of the files or loading them as libraries did not improved the speed.

List of files to be prefetched is determined by recording the list of loaded libraries at each startup and storing it in a file. Therefore libraries needed by Slicer extensions, Python packages, and Qt plugins are all covered. The list lives beside the revision-specific settings file, which is the application's existing answer to where an installation may write, so an installation in a read-only directory can still refresh it.

What the prefetch did is added to the --report-startup-timing report.

Two environment variables can adjust the behavior. SLICER_STARTUP_FILE_PREFETCH can force enable/disable library prefetch by setting it to 1 or 0. SLICER_STARTUP_FILE_PREFETCH_THREADS can set a maximum number of threads that may prefetch the files.

The file prefetching mechanism can be excluded from the build by setting Slicer_BUILD_STARTUP_FILE_PREFETCH CMake variable to OFF.

see #9203</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/9328">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/9328" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/9328" target="_blank" rel="noopener">PERF: Load large Python libraries only when they are first used (#9328)</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>lassoan:lazyload-large-python-libs</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-08-02" data-time="04:08:29" data-timezone="UTC">04:08AM - 02 Aug 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/lassoan" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
            lassoan
          </a>
        </div>

        <div class="lines" title="3 commits changed 19 files with 250 additions and 77 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/9328/files" target="_blank" rel="noopener">
            <span class="added">+250</span>
            <span class="removed">-77</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">On Windows, Slicer cold start time was 20 seconds on the latest main branch.
Wi<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/9328" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">th the fixes in this pull request, the starting time is about 14 seconds.

numpy, scipy, pydicom and the libraries they pull in were imported while the
application started, either from slicer/__init__.py or from the module bodies of
scripted modules that are registered on every launch. Profiling showed these
imports to be a large fraction of Python startup time, and a session that never
touches DICOM or does any array work never needs them.

Move the large package imports out of the application startup:

- Add slicer.util.LazyImport, which resolves a module (or a "pkg.mod:name"
  module attribute) on first attribute access or call, so existing name.attr
  usage stays unchanged.
- Stop importing numpy and scipy eagerly in slicer/__init__.py. The eager import
  was a workaround for an application hang when they were first imported under
  output redirection on Windows 11 (issue #5945); if that recurs, the removed
  block can be restored from the history of this commit.
- Defer the DICOM modules' pydicom, highdicom, requests/dicomweb_client and
  numpy imports to the functions that use them. Importing pydicom in particular
  pulls in its example-data downloader (requests, charset_normalizer) and all
  pixel-data codec handlers. The DICOM SOP Class UID constants that the TID1500
  plugin used to evaluate in its class body (which forced an import of pydicom
  when the class was defined) are now read from pydicom.uid in the two methods
  that compare against them, both of which already work with pydicom datasets.
- Defer numpy in the Endoscopy fly-through and the WebServer request handler,
  and charset_normalizer in SlicerWizard, which the ExtensionWizard module pulls
  in transitively.

Two tests relied on these packages being imported during startup and are updated
accordingly: test_slicer_packaging used numpy as an example of a package that is
present in sys.modules, and SegmentEditorLogicTest used vtk.util.numpy_support
without importing it (which only worked because another module imported it at
startup). Code in extensions may need the same change, as vtk.util is only
available after something imports it.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/9326">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/9326" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/9326" target="_blank" rel="noopener">PERF: Drop hardcoded VTK base-class imports; rely on pruned wrapping DEPENDS (#9326)</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>pieper:lazy-vtk-drop-hardcoded-imports</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-07-31" data-time="15:56:28" data-timezone="UTC">03:56PM - 31 Jul 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/pieper" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
            pieper
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 12 additions and 38 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/9326/files" target="_blank" rel="noopener">
            <span class="added">+12</span>
            <span class="removed">-38</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Follow-on to #9306 (lazy `vtk` shim). The shim needs each wrapped subclass's VTK<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/9326" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">
base class imported before the subclass's Python type is built. That was handled
by importing a hand-maintained list of ~28 core `vtkmodules` explicitly in
`slicer/__init__.py`, because at the time the generated wrapping `DEPENDS`
dropped every VTK dependency.

That list is no longer needed. With the corresponding vtkAddon change, each
wrapped module's generated init imports exactly the VTK modules that provide its
direct base classes (the `DEPENDS`, pruned from the full link line to the
base-class providers), so subclasses resolve their bases automatically as the
kits load.

Removing the hardcoded list is strictly better: it is derived from the actual
class hierarchy rather than hand-maintained (and so covers extension modules
that define their own wrapped classes), and it no longer force-loads heavy
modules (`vtkRenderingOpenGL2`, `vtkRenderingVolumeOpenGL2`, `vtkChartsCore`)
that are not base-class providers at startup.

Measured on macOS: 29 of 125 VTK Python modules loaded after a full GUI startup
(none of the rendering/IO/Charts tail), `isinstance(slicer.vtkMRMLScene(),
vtk.vtkObject)` is True, and warm startup drops about 1s (5.9s → 4.9s).

**Depends on** the vtkAddon DEPENDS-pruning change (Slicer/vtkAddon#71). Before
merge this PR must also bump the vtkAddon `GIT_TAG` in `SuperBuild.cmake` to the
merged vtkAddon commit; without the pruned vtkAddon the wrapped modules still
list every VTK module and startup gains nothing. Opened as a draft until then.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/9311">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/9311" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/9311" target="_blank" rel="noopener">ENH: Pre-warm the macOS first-launch library scan behind a progress splash (#9311)</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>pieper:sharedlib-prewarm</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-07-24" data-time="20:40:12" data-timezone="UTC">08:40PM - 24 Jul 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/pieper" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/126077?v=4" class="onebox-avatar-inline" width="20" height="20">
            pieper
          </a>
        </div>

        <div class="lines" title="1 commits changed 4 files with 767 additions and 0 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/9311/files" target="_blank" rel="noopener">
            <span class="added">+767</span>
            <span class="removed">-0</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">## What this is

The first time each newly built or freshly downloaded shared li<span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/9311" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">brary is loaded, the operating system inspects it and caches the verdict per file — on macOS a `syspolicyd` / **XProtect** security scan (~0.13 s per Mach-O, measured), on Windows an antivirus scan, cold filesystem caches everywhere. Slicer ships **~900 libraries**, so the first launch of a new build or a freshly downloaded copy can spend **a minute or two** on this at near-zero CPU, showing a blank Dock icon and no window, before startup even really begins. Later launches take seconds.

This adds a **pre-warm** that performs that inspection up front, behind an optional native progress splash, so the wait is visible and explained instead of a frozen/absent window.

### Honest scope: this is a first-launch **experience** fix, not a speedup

The security scan is **serialized by the system daemon** (single-threaded system-wide — verified: an 8-worker parallel version gave *no* speedup and was removed). So the pre-warm **does not make the total launch faster** — the cost is unavoidable. What it buys:

- the unavoidable wait becomes a **native progress window with an accurate ETA** ("Preloading 3D Slicer libraries… about a minute left") instead of a blank screen, and
- a **stamp file limits the work to when it's actually needed**: after a new build or download, and once per session after a reboot (which clears the OS caches). The splash is only shown when the run is predicted to exceed **2 seconds**, so ordinary launches stay silent.

## How it works

- **macOS primitive:** each library is mapped with `PROT_EXEC`, which makes the kernel run the *identical* scan and cache it — without `dlopen`, dependency resolution, or spawning a process. (Other platforms load in a disposable worker.)
- **`SlicerPrewarm.py`** — the sequential warm-up, a boot-session-aware stamp, and native progress splashes for macOS (AppKit), Windows (user32), and X11, all drawn through `ctypes` with **no GUI-toolkit dependency**.
- Three entry points: an automatic **`prewarm` build target** (freshly built libs at end of build), the **macOS bundle bootstrap** (a small compiled `CFBundleExecutable` shim that pre-warms before `exec`-ing the real app, preserving the process identity), and an **in-app hook** for extension / additional-module paths known only at runtime.
- Disable with `SLICER_DISABLE_STARTUP_PREWARM=1`.

## Relationship to prior discussion

Addresses the first-launch experience described in **#9203** (Improve startup speed) and **#8638** (Improve Slicer startup experience). Concrete points from that discussion this acts on:

- **macOS has no launcher** (and therefore no launcher splash) — so the launcher-splash handoff fix (#8808, Win/Linux) doesn't cover the macOS cold first launch. The bundle bootstrap here is the macOS analog: it puts *something* on screen during the wait.
- The reported failure mode — *"nothing appears for ~10 s, the user thinks it failed and relaunches, producing a 2nd instance"* — is directly what the progress splash is meant to prevent on first launch. (This PR does **not** add single-instance locking; that's a separate mitigation.)
- Per the discussion, this intentionally **does not** add an XML launcher↔app progress protocol — it uses a self-contained native splash instead.

Complementary to **#9306** (lazy VTK Python modules), which reduces the *actual* Python-import work at every startup. That PR is a genuine `PERF` speedup; this one is first-launch transparency for a cost that can't be reduced — the two are independent (no shared files) and address different parts of the same "startup feels slow" problem, which is why they're separate PRs.

## Status / notes

- Draft. Primarily exercised on macOS arm64; the Windows/X11 splashes are implemented but need testing on those platforms.
- The pre-warm is a no-op on a normal warm launch (stamp check only) and never blocks or aborts startup — any failure (unwritable stamp, splash init failure, etc.) is swallowed.
- Not addressed here (possible follow-ups from the same discussion): skipping instantiation of testing modules when developer mode is off, and preventing a second instance during a slow first launch.

🤖 Generated with [Claude Code](https://claude.com/claude-code)</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
