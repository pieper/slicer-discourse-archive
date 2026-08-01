---
topic_id: 47781
title: "PyTorch install fails on Windows with WinError 206 — PythonSlicer.exe is not longPathAware"
date: 2026-07-31
url: https://discourse.slicer.org/t/47781
last_bumped: 2026-07-31T19:40:47.733Z
---

# PyTorch install fails on Windows with WinError 206 — PythonSlicer.exe is not longPathAware

**Topic ID**: 47781
**Date**: 2026-07-31
**URL**: https://discourse.slicer.org/t/pytorch-install-fails-on-windows-with-winerror-206-pythonslicer-exe-is-not-longpathaware/47781

---

## Post #1 by @pboarantes (2026-07-31 18:31 UTC)

<p><strong>Environment</strong></p>
<ul>
<li>3D Slicer 5.12.3, Windows 11</li>
<li>Default install path: <code>C:\Users\&lt;user&gt;\AppData\Local\slicer.org\3D Slicer 5.12.3\</code></li>
<li>Extensions: TotalSegmentator, PyTorch, NNUNet</li>
<li>torch 2.13.0+cu130 / torchvision 0.28.0+cu130 (selected automatically by light-the-torch)</li>
<li>GPU: RTX 5070 Ti</li>
</ul>
<p><strong>Disclosure up front:</strong> I am a physician, not a software engineer. I worked through this with Claude (Anthropic) over a long debugging session. Every command below was run on my machine and the end state works, but please review critically rather than trusting it on my authority.</p>
<hr>
<h2><a name="p-135211-symptom-1" class="anchor" href="#p-135211-symptom-1" aria-label="Heading link"></a>Symptom</h2>
<p>First run of TotalSegmentator → Apply. The PyTorch extension downloads the wheel and then dies:</p>
<pre><code class="lang-auto">Installing collected packages: torch, torchvision
ERROR: Could not install packages due to an OSError: [WinError 206] The filename or extension is too long:
'C:\Users\&lt;user&gt;\AppData\Local\slicer.org\3D Slicer 5.12.3\lib\Python\Lib\site-packages\torch-2.13.0+cu130.dist-info\licenses\third_party\kineto\libkineto\third_party\dynolog\third_party\prometheus-cpp\3rdparty\googletest\googlemock\scripts\generator'
</code></pre>
<p>followed by:</p>
<pre><code class="lang-auto">ModuleNotFoundError: No module named 'torchgen'
</code></pre>
<p>and, on the next attempt:</p>
<pre><code class="lang-auto">File ".../PyTorchUtils.py", line 162, in torchInstalled
    metadataPath = [p for p in importlib.metadata.files('torch') if 'METADATA' in str(p)][0]
TypeError: 'NoneType' object is not iterable
</code></pre>
<h2><a name="p-135211-root-cause-2" class="anchor" href="#p-135211-root-cause-2" aria-label="Heading link"></a>Root cause</h2>
<p>Three things combine, and none of them is user misconfiguration:</p>
<ol>
<li><strong>The default install prefix is long.</strong> <code>...\3D Slicer 5.12.3\lib\Python\Lib\site-packages\</code> is 86 characters on its own for a 5-character username. Longer usernames make it worse.</li>
<li><strong>Recent torch wheels ship a deeply nested third-party license tree.</strong> Under <code>.dist-info/licenses/</code>, the upstream directory structure is preserved. The deepest branch reaches <code>licenses\third_party\kineto\libkineto\third_party\dynolog\third_party\prometheus-cpp\3rdparty\googletest\googlemock\scripts\generator\</code> — roughly 162 characters of suffix. Directory plus prefix is already ~248 characters; the files inside push it past the 260-character <code>MAX_PATH</code> limit. This is the part that changed: older torch wheels did not carry this tree, which is why the same install path worked in previous Slicer releases.</li>
<li><strong>Enabling long paths in the registry does not help.</strong> Per Microsoft’s documentation, two conditions must both be met: the <code>LongPathsEnabled</code> registry value must be 1 <strong>and</strong> the application manifest must include the <code>longPathAware</code> element. pip runs as a subprocess of <code>PythonSlicer.exe</code>, which does not declare it. CPython’s own <code>python.exe</code> does, so this is specific to the Slicer launcher.</li>
</ol>
<p>I set <code>LongPathsEnabled=1</code> and rebooted before understanding point 3, and the failure was byte-for-byte identical.</p>
<h2><a name="p-135211-two-secondary-problems-that-make-this-hard-to-diagnose-3" class="anchor" href="#p-135211-two-secondary-problems-that-make-this-hard-to-diagnose-3" aria-label="Heading link"></a>Two secondary problems that make this hard to diagnose</h2>
<p><strong>Retrying never recovers.</strong> When pip dies partway through, it may already have written a valid <code>torch-2.13.0+cu130.dist-info</code> with METADATA. On the next run pip reports <code>Requirement already satisfied: torch&gt;=2.1.2</code> and skips reinstallation, while <code>import torch</code> still fails. The site-packages tree has to be wiped manually before any retry.</p>
<p><strong>The error message is misleading.</strong> A partial install leaves <code>site-packages\torch\</code> without <code>__init__.py</code>. Python 3.3+ treats that as a namespace package and imports it successfully as an empty module, so instead of <code>ModuleNotFoundError</code> you get:</p>
<pre><code class="lang-auto">AttributeError: module 'torch' has no attribute '__version__'
</code></pre>
<p>which looks like a version-detection bug rather than a broken install.</p>
<h2><a name="p-135211-workaround-4" class="anchor" href="#p-135211-workaround-4" aria-label="Heading link"></a>Workaround</h2>
<p><strong>Simplest, and what I would recommend to anyone hitting this:</strong> reinstall Slicer to a short path such as <code>C:\Slicer5123\</code> instead of the default. That removes ~48 characters of prefix and the wheel installs normally with no further intervention.</p>
<p><strong>If you cannot reinstall,</strong> the path below works but has a trap in it. In an <strong>elevated</strong> PowerShell, with Slicer closed:</p>
<p>powershell</p>
<pre><code class="lang-auto">$slicer = "$env:LOCALAPPDATA\slicer.org\3D Slicer 5.12.3"
$sp     = "$slicer\lib\Python\Lib\site-packages"
$py     = "$slicer\bin\PythonSlicer.exe"

# 1. remove any partial install from earlier attempts
Get-ChildItem $sp | Where-Object { $_.Name -match '^(torch|torchvision|torchaudio|torchgen|functorch)([-.]|$)' } |
  Remove-Item -Recurse -Force

# 2. short temp directory (pip unpacks there before copying)
New-Item -ItemType Directory C:\t -Force | Out-Null
$env:TMP = "C:\t"; $env:TEMP = "C:\t"

# 3. install into a short path
&amp; $py -m pip install --target C:\sp --upgrade --no-deps `
  "torch==2.13.0+cu130" "torchvision==0.28.0+cu130" `
  --index-url https://download.pytorch.org/whl/cu130

# 4. move into site-packages (rename is a single FS operation, so MAX_PATH does not apply)
Get-ChildItem C:\sp -Directory | Where-Object { $_.Name -ne 'bin' } | ForEach-Object {
    $destino = Join-Path $sp $_.Name
    if (Test-Path $destino) { Remove-Item $destino -Recurse -Force }
    [System.IO.Directory]::Move($_.FullName, $destino)
}

# 5. REQUIRED: reset ACLs, or Slicer (unelevated) cannot read the files
icacls "$sp" /reset /T /C /Q
</code></pre>
<p><strong>Step 5 is not optional.</strong> Files created under <code>C:\</code> by an elevated shell inherit the root ACL, and the move preserves it. Slicer then runs unelevated and gets <code>PermissionError: [WinError 5] Access is denied</code>. Worse, <code>os.path.exists()</code> swallows access errors and returns <code>False</code>, so the file appears to be missing when it is actually unreadable — I lost a fair amount of time on that. Reset the whole <code>site-packages</code> tree, not just the <code>torch*</code> directories: the torch wheel also installs <code>functorch</code>, and I initially missed it.</p>
<p>Verify in the Slicer Python console:</p>
<p>python</p>
<pre><code class="lang-auto">import torch, torchgen
print(torch.__version__, torch.cuda.is_available(), torch.cuda.get_device_name(0))
</code></pre>
<p>Expected: <code>2.13.0+cu130 True NVIDIA GeForce RTX 5070 Ti</code>. After that, TotalSegmentator’s Apply proceeds normally.</p>
<h2><a name="p-135211-suggested-fixes-5" class="anchor" href="#p-135211-suggested-fixes-5" aria-label="Heading link"></a>Suggested fixes</h2>
<ol>
<li><strong>Add <code>longPathAware</code> to the <code>PythonSlicer.exe</code> manifest at build time.</strong> This is the structural fix and it removes the whole class of problem, not just torch:</li>
</ol>
<p>xml</p>
<pre><code class="lang-auto">   &lt;application xmlns="urn:schemas-microsoft-com:asm.v3"&gt;
     &lt;windowsSettings&gt;
       &lt;longPathAware xmlns="http://schemas.microsoft.com/SMI/2016/WindowsSettings"&gt;true&lt;/longPathAware&gt;
     &lt;/windowsSettings&gt;
   &lt;/application&gt;
</code></pre>
<ol start="2">
<li><strong>Make <code>PyTorchUtils.torchInstalled()</code> defensive.</strong> It currently raises <code>TypeError</code> when <code>importlib.metadata.files('torch')</code> returns <code>None</code>, and <code>PermissionError</code> when a file in the RECORD is unreadable. Returning <code>False</code> on either would at least let the extension attempt a clean reinstall instead of dead-ending.</li>
<li><strong>Consider warning at install time</strong> if the Slicer installation path is long enough that <code>site-packages</code> plus a typical deep wheel would exceed <code>MAX_PATH</code>.</li>
</ol>
<p>Happy to test patches or provide any additional logs.</p>

---

## Post #2 by @jamesobutler (2026-07-31 19:40 UTC)

<p>Thanks for providing the details. Yes, it is something we are aware of in regards to PyTorch’s 2.13 release.</p>
<aside class="onebox githubissue" data-onebox-src="https://github.com/Slicer/Slicer/issues/6037#issuecomment-5023722563">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/issues/6037#issuecomment-5023722563" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Issue" data-github-private-repo="false">
	  <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/Slicer/issues/6037#issuecomment-5023722563" target="_blank" rel="noopener nofollow ugc">Enable long file path support on Windows</a>
    </h4>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-11-24" data-time="04:08:30" data-timezone="UTC">04:08AM - 24 Nov 21 UTC</span>
      </div>


      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>
    </div>

    <div class="labels">
        <span style="display:inline-block;margin-top:2px;background-color: #B8B8B8;padding: 2px;border-radius: 4px;color: #fff;margin-left: 3px;">
          Type: Enhancement
        </span>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Files that have longer path than `MAX_PATH` (260 characters) cannot be accessed <span class="show-more-container"><a href="" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">in Slicer.

Such files can be created on any file system that supports longer paths, by using UNC path convention (i.e., adding the `\\?\UNC\` prefix to a path), because when a Win32 API function is called with an UNC path then Windows does not interpret the path (so path length limitations do not apply), but the name is forwarded it directly to the file system.

Long file paths can be also created by applications that have `longPathAware` element enabled in their manifest if "Win32 Long Paths" are enabled on the computer by editing the registry or group policies (see https://docs.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation?tabs=cmd).

## Describe the solution you'd like

Slicer and all the libraries that it uses should stop relying on fixed path length (`MAX_PATH` constant) on Windows and then in Slicer's application manifest `longPathAware` element could be set to enabled. This would allow Slicer to access (read/write/create/delete) files with long names on Windows.

## Describe alternatives you've considered

Using UNC files at specific critical locations (where receiving long paths is more likely, for example in the DICOM importer) could alleviate some problems. However, this solution would only be partial and much more complex than using the proposed solution.

## Additional context

https://discourse.slicer.org/t/slicerqr-development/15954/205</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You may have installed torch using the Slicer PyTorch extension prior to yesterday’s integration of the following commit where we are temporarily trying to avoid installation of PyTorch 2.13 on Windows. If you upgrade your Slicer PyTorch extension (or uninstall and reinstall with a new download), it should enforce to avoid version 2.13.</p>
<aside class="onebox githubcommit" data-onebox-src="https://github.com/fepegar/SlicerPyTorch/commit/74f8216f4841d84b8ceca3026aa18d022be78e78">
  <header class="source">

      <a href="https://github.com/fepegar/SlicerPyTorch/commit/74f8216f4841d84b8ceca3026aa18d022be78e78" target="_blank" rel="noopener nofollow ugc">github.com/fepegar/SlicerPyTorch</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Commit">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 14 16" aria-hidden="true"><path fill-rule="evenodd" d="M10.86 7c-.45-1.72-2-3-3.86-3-1.86 0-3.41 1.28-3.86 3H0v2h3.14c.45 1.72 2 3 3.86 3 1.86 0 3.41-1.28 3.86-3H14V7h-3.14zM7 10.2c-1.22 0-2.2-.98-2.2-2.2 0-1.22.98-2.2 2.2-2.2 1.22 0 2.2.98 2.2 2.2 0 1.22-.98 2.2-2.2 2.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/fepegar/SlicerPyTorch/commit/74f8216f4841d84b8ceca3026aa18d022be78e78" target="_blank" rel="noopener nofollow ugc">Do not install torch 2.13 on Windows (#23)</a>
    </h4>

    <div class="github-info">
      <div class="date">
        committed <span class="discourse-local-date" data-format="ll" data-date="2026-07-30" data-time="22:14:52" data-timezone="UTC">10:14PM - 30 Jul 26 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener nofollow ugc">
          <img alt="" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="changed 1 files with 25 additions and 0 deletions">
        <a href="https://github.com/fepegar/SlicerPyTorch/commit/74f8216f4841d84b8ceca3026aa18d022be78e78" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+25</span>
          <span class="removed">-0</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">torch 2.13 ships PEP 639 license files that reproduce PyTorch's vendored
source <span class="show-more-container"><a href="https://github.com/fepegar/SlicerPyTorch/commit/74f8216f4841d84b8ceca3026aa18d022be78e78" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">tree inside torch-&lt;version&gt;.dist-info/licenses. The deepest collected
path is 162 characters relative to site-packages, while Windows limits
directory creation to MAX_PATH-12 (248 characters). Installation therefore
fails with "[WinError 206] The filename or extension is too long" whenever the
path of site-packages is longer than 86 characters, which a default Slicer
installation is exactly at. The failed installation leaves a partially
extracted torch package behind that is hard to remove, because deleting those
files hits the same path length limit.

Exclude torch 2.13.* on Windows, along with torchvision 0.28.*, which requires
torch 2.13 and would pull it back in. This can be reverted once PyTorch no
longer collects the deeply nested license files.

See Slicer/light-the-torch#176 and pytorch/pytorch#185813.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>PyTorch maintainers themselves are ultimately working on change that will drop some of the long paths that became an issue in their 2.13 release. See the following open work:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/pytorch/pytorch/pull/185813">
  <header class="source">

      <a href="https://github.com/pytorch/pytorch/pull/185813" target="_blank" rel="noopener nofollow ugc">github.com/pytorch/pytorch</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/pytorch/pytorch/pull/185813" target="_blank" rel="noopener nofollow ugc">[ROCm][Windows] Audit license-files: explicit enumeration + audit test (#183434) (#185813)</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>tvukovic-amd:audit-license-files-183434</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-06-01" data-time="12:53:35" data-timezone="UTC">12:53PM - 01 Jun 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/tvukovic-amd" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/127323445?v=4" class="onebox-avatar-inline" width="20" height="20">
            tvukovic-amd
          </a>
        </div>

        <div class="lines" title="15 commits changed 8 files with 638 additions and 19 deletions">
          <a href="https://github.com/pytorch/pytorch/pull/185813/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+638</span>
            <span class="removed">-19</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Fix for [pytorch/pytorch#183434](https://github.com/pytorch/pytorch/issues/18343<span class="show-more-container"><a href="https://github.com/pytorch/pytorch/pull/185813" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">4).

The PEP 639 migration (#180237) replaced the old concatenated `LICENSE` blob with per-file `license-files` in `pyproject.toml`. The existing recursive globs:

```toml
license-files = [
    "LICENSE",
    "third_party/**/LICENSE",
    "third_party/**/LICENSE.txt",
    "third_party/**/LICENSE.rst",
    "third_party/**/COPYING.BSD",
]
```

matched **107 files** in the source tree, but only **~59** represent code that actually ships in the wheel. The remainder are over-collection from nested submodule vendoring — tests, docs, bindings, build tools, and dynolog transitive deps.

This caused two concrete problems:

1. **Windows `MAX_PATH` failures** — PEP 639 copies each license into the wheel under `.dist-info/licenses/`, doubling path length. Deep dynolog paths (up to **135 characters** relative) exceeded Windows limits during packaging.
2. **Incorrect license surface** — including files like `cpr/test/LICENSE` (GPL-3.0) in the distribution metadata, even though that code is never compiled or linked into PyTorch.

## How the explicit list was derived

The 59 paths in `pyproject.toml` were **not** picked manually one-by-one. They are the output of a repeatable audit that mirrors the issue author's "conservative exclusion" (which estimated ~61 paths on ~108 glob matches; this tree yields **107 discovered → 59 shipped**).

### Step 1 — Start from the old glob universe

Run the same patterns PyTorch used before the audit:

```toml
LICENSE
third_party/**/LICENSE
third_party/**/LICENSE.txt
third_party/**/LICENSE.rst
third_party/**/COPYING.BSD
```

This finds every candidate license file the recursive globs would have collected (**107 files** in the current tree).

### Step 2 — Apply exclusion rules

Each candidate is classified using structural rules in `test/test_license.py`. Paths that match non-shipping trees — tests, docs, googletest, bindings, dynolog transitive deps, deep nested vendoring — are **excluded**.

### Step 3 — Whatever survives = explicit list

The shipped set is computed directly from discovery minus exclusion:

```python
shipped = [path for path in discovered if not is_excluded(path)]
# → 59 paths
```

Those 59 paths are what go into `pyproject.toml` `license-files`. The list is the **output of the audit**, not a separate manual pick.

### Step 4 — Test locks it in

`test_pyproject_license_metadata` asserts:

```python
project["license-files"] == shipped
project["license"] == spdx_from(shipped)
```

If a submodule is added or moved, the test fails until `pyproject.toml` and the exclusion rules are updated together.



cc @jeffdaily @sunway513 @jithunnair-amd @pruthvistony @ROCmSupport @jataylo @hongxiayang @naromero77amd @pragupta @jerrymannil @xinyazhang</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
