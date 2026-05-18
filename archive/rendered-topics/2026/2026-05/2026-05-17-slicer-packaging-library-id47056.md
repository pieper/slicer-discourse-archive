---
topic_id: 47056
title: "Slicer Packaging Library"
date: 2026-05-17
url: https://discourse.slicer.org/t/47056
---

# Slicer.packaging library

**Topic ID**: 47056
**Date**: 2026-05-17
**URL**: https://discourse.slicer.org/t/slicer-packaging-library/47056

---

## Post #1 by @muratmaga (2026-05-17 05:50 UTC)

<p>I came across this blog post on Linked in <a href="https://www.kitware.com/improving-python-dependency-handling-for-3d-slicer-extension-development/" rel="noopener nofollow ugc">https://www.kitware.com/improving-python-dependency-handling-for-3d-slicer-extension-development/</a></p>
<p>The post says it is already integrated into the Slicer preview preview build. This is definitely a great future and imrpovement, however, I don’t recall seeing anything about this in this forum.</p>
<p>I would be good to cross-post these announcements on the forum as well. Linked in is good for outreach, but the community is here.</p>

---

## Post #2 by @pieper (2026-05-17 07:56 UTC)

<p>There was a lot of discussion about this on the slicer-dev meetings, the agenda and minutes of which show up on the forum.  E.g. <a href="https://discourse.slicer.org/t/2026-03-24-weekly-meeting/46543/3">here</a> and of course in the corresponding pull request thread, so people watching the repo would be notified.  The info is there, but maybe not flagged in a way that gets everyone’s attention.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/9010">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/9010" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/9010" target="_blank" rel="noopener">Improve python package installation utilities (#9010)</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>ebrahimebrahim:python-dependency-handling-improvements</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-01-29" data-time="19:06:19" data-timezone="UTC">07:06PM - 29 Jan 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/ebrahimebrahim" target="_blank" rel="noopener">
            <img alt="" src="https://avatars.githubusercontent.com/u/1879759?v=4" class="onebox-avatar-inline" width="20" height="20">
            ebrahimebrahim
          </a>
        </div>

        <div class="lines" title="5 commits changed 21 files with 3354 additions and 133 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/9010/files" target="_blank" rel="noopener">
            <span class="added">+3354</span>
            <span class="removed">-133</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container"># Python Dependency Handling Improvements

## Summary

This PR introduces a <span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/9010" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">new `slicer.packaging` module for managing Python dependencies in Slicer extensions. The goal is to provide a standardized, user-friendly way to check, prompt for, and install Python packages. The existing `slicer.util.pip_install` and `slicer.util.pip_uninstall` functions are retained as backward-compatible wrappers that delegate to `slicer.packaging`.

**New/updated functions:**

| Function | Purpose |
|----------|---------|
| `slicer.packaging.load_requirements(path)` | Load a `requirements.txt` file into `Requirement` objects |
| `slicer.packaging.load_pyproject_dependencies(path)` | Load `[project.dependencies]` from a `pyproject.toml` file into `Requirement` objects |
| `slicer.packaging.pip_check(reqs)` | Check if requirements are satisfied (pure Python, no subprocess). Accepts a string, a list of strings, a `Requirement`, or a list of `Requirement`s. |
| `slicer.packaging.pip_install(...)` | Canonical home; extended with modal progress dialog, non-blocking mode, status bar feedback, `--no-deps` support, and a discouraged `skip_packages` workaround for transitive dependency conflicts. Also available as `slicer.util.pip_install` (backward-compatible wrapper) |
| `slicer.packaging.pip_ensure(reqs, requester="...")` | High-level: checks, prompts, installs with progress, and offers restart if updated packages were already imported. Accepts the same flexible input as `pip_check`. |

All install functions support optional `constraints` (constraints file), `no_deps_requirements` (packages to install with `--no-deps`), and `skip_packages` (packages to exclude from the transitive dependency tree) parameters.

**Typical usage in an extension:**

```python
import slicer.packaging

reqs = slicer.packaging.load_requirements(self.resourcePath("requirements.txt"))
slicer.packaging.pip_ensure(reqs, requester="MyExtension")
import my_dependency  # Now safe
```

Or, with `pyproject.toml`:

```python
import slicer.packaging

reqs = slicer.packaging.load_pyproject_dependencies(self.resourcePath("pyproject.toml"))
slicer.packaging.pip_ensure(reqs, requester="MyExtension")
import my_dependency  # Now safe
```

With `skip_packages` (for extensions that need to exclude certain transitive dependencies; **discouraged workaround**, see [the script repository](https://github.com/Slicer/Slicer/blob/main/Docs/developer_guide/script_repository/packaging.md) for guidance):

```python
import slicer.packaging

skipped = slicer.packaging.pip_ensure(
    "nnunetv2&gt;=2.3",
    skip_packages=["SimpleITK", "torch", "requests"],
    requester="SlicerNNUNet",
)
# skipped contains the requirement strings that were excluded
```

**Behavior of `pip_install`:**

Four operating modes:

- `show_progress=True, blocking=True` : Modal progress dialog (new default behavior)
- `show_progress=True, blocking=False`: Status bar messages
- `show_progress=False, blocking=True`: Busy cursor only (the previous default behavior, except with a busy cursor now added)
- `show_progress=False, blocking=False`: No visual indication that anything is happening (without looking at python console); specify callbacks to create more reasonable custom behaviors.

## Changes

The PR is organized as 5 commits, each a self-contained change:

1. **`ENH: Add slicer.packaging module for managing Python dependencies`**
   - `Base/Python/slicer/packaging.py` (new) — `load_requirements`, `load_pyproject_dependencies`, `pip_check`, `pip_ensure`, `pip_install`, `pip_uninstall`, the non-blocking infrastructure, the modal progress dialog, the restart prompt, and the `skip_packages` workaround
   - `Base/Python/slicer/util.py` — backward-compatible `pip_install` / `pip_uninstall` wrappers that delegate to `slicer.packaging`; updated error messages to point at the canonical name
   - `Base/Python/slicer/tests/test_slicer_packaging.py` (new) — full unit test suite for the new module
   - `Base/Python/slicer/tests/test_slicer_util_pip.py` (new) — focused tests for the back-compat wrappers
   - `Base/Python/CMakeLists.txt` — register the new module
   - `Applications/SlicerApp/Testing/Python/CMakeLists.txt` — register the test files

2. **`DOC: Document slicer.packaging in the developer guide`**
   - `Docs/developer_guide/script_repository/packaging.md` (new) — full "Python package management" section in the script repository
   - `Docs/developer_guide/script_repository.md` — include directive
   - `Docs/developer_guide/python_faq.md` — point developers at `slicer.packaging`, recommend `pip_ensure` as the high-level workflow, refresh the best-practices list to reflect that `pip_ensure` handles confirmation on its own
   - `Docs/developer_guide/script_repository/gui.md`, `models.md`, `plots.md` — sweep existing examples to use the canonical name
   - `Docs/developer_guide/slicer.md` — wire `slicer.packaging` into the auto-generated API reference

3. **`ENH: Show slicer.packaging usage in the new scripted module template`**
   - `Utilities/Templates/Modules/Scripted/TemplateKey.py` — commented-out `pip_ensure` example at the top of `onApplyButton`
   - `Utilities/Templates/Modules/Scripted/Resources/requirements.txt` (new) — blank scaffold
   - `Utilities/Templates/Modules/Scripted/CMakeLists.txt` — list the requirements file as a module resource
   - `Utilities/Scripts/SlicerWizard/TemplateManager.py` — recognize `requirements.txt` as a template file so it actually rides along when the wizard generates a new module

4. **`BUG: Clean up Python interactor startup`**
   - `Base/Python/slicerqt.py` (renamed from `Base/Python/slicer/slicerqt.py`) — moved out of the `slicer/` package directory so that CTK's `executeFile` no longer puts `bin/Python/slicer/` on `sys.path[0]` (which silently shadowed any same-named PyPI package, including the one we wanted for this PR). The wildcard `from slicer.util import *` is replaced with an explicit 5-name list (`array`, `exit`, `getNode`, `getNodesByClass`, `mainWindow`).
   - `Base/QTGUI/qSlicerPythonManager.cxx` — updated path
   - `Base/Python/CMakeLists.txt` — register the new location

5. **`BUG: Allow i18n translation functions to work without Qt`**
   - `Base/Python/slicer/i18n.py` — `translate()` no longer crashes when `slicer.app` is unavailable; it returns the untranslated text instead. This is what made it possible to wrap user-facing strings in `slicer.packaging` with `_()` while keeping the module headless-safe.

---

&lt;details&gt;
&lt;summary&gt;&lt;strong&gt;Testing Snippets (click to expand)&lt;/strong&gt;&lt;/summary&gt;

Convenient snippets to quickly try things. First, run this once in the Python console:

```python
import slicer.packaging
```

### load_requirements

```python
import tempfile, os
with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
    f.write("numpy&gt;=1.20\npandas&gt;=2.0\nscipy\n")
    path = f.name
reqs = slicer.packaging.load_requirements(path)
print([f"{r.name}: {r.specifier}" for r in reqs])
os.unlink(path)
```

### load_pyproject_dependencies

```python
import tempfile, os
with tempfile.NamedTemporaryFile(mode='w', suffix='.toml', delete=False) as f:
    f.write("[project]\ndependencies = [\n")
    f.write('    "numpy&gt;=1.20",\n    "pandas&gt;=2.0",\n    "scipy",\n]\n')
    path = f.name
reqs = slicer.packaging.load_pyproject_dependencies(path)
print([f"{r.name}: {r.specifier}" for r in reqs])
os.unlink(path)
```

### pip_check

```python
# Simple string syntax
slicer.packaging.pip_check("numpy&gt;=1.0")          # True
slicer.packaging.pip_check("numpy&gt;=99999.0")       # False
slicer.packaging.pip_check("nonexistent-package-xyz")  # False

# Multiple requirements in a single space-separated string
slicer.packaging.pip_check("numpy&gt;=1.0 scipy&gt;=1.0")  # True

# Markers that don't apply are considered satisfied
slicer.packaging.pip_check("foo; sys_platform == 'nonexistent'")  # True

# A list of strings also works
slicer.packaging.pip_check(["numpy&gt;=1.0", "scipy&gt;=1.0"])  # True

# Or a packaging.requirements.Requirement object, if you already have one
from packaging.requirements import Requirement
slicer.packaging.pip_check(Requirement("numpy&gt;=1.0"))  # True
```

### pip_install with progress dialog (default)

```python
# Default: shows modal progress dialog, blocks until complete
# (If already installed, completes quickly with "already satisfied")
slicer.packaging.pip_install("scikit-image", requester="ReviewTest")
```

To see the full installation flow, uninstall first:
```python
slicer.packaging.pip_uninstall("scikit-image")
slicer.packaging.pip_install("scikit-image", requester="ReviewTest")
```

If it's still too fast, try putting "torch" as the package :)

### pip_install without progress dialog

```python
# Busy cursor only, no dialog
slicer.packaging.pip_install("scikit-image", show_progress=False)
```

### Non-blocking pip_install with status bar messages

```python
slicer.packaging.pip_install("scikit-image", blocking=False, requester="ReviewTest")
```

### Non-blocking pip_install with custom callbacks

```python
def onLog(line):
    print(f"[pip] {line}")

def onComplete(code):
    print(f"Done! Return code: {code}")

# Using --help to see callbacks firing with lots of output
slicer.packaging.pip_install("--help", blocking=False, show_progress=False, logCallback=onLog, completedCallback=onComplete)
```

### Backward-compat wrappers in slicer.util

The old `slicer.util.pip_install` and `slicer.util.pip_uninstall` still work; they delegate to `slicer.packaging`. Quick sanity check:

```python
slicer.util.pip_install("charset-normalizer")
slicer.util.pip_uninstall("charset-normalizer")
```

### Check if pip install is in progress

```python
slicer.packaging.pip_install("scikit-image", blocking=False, requester="ReviewTest")
print(slicer.packaging.isPipInstallInProgress())  # probably True
```

versus just this:

```python
print(slicer.packaging.isPipInstallInProgress())  # False
```

### pip_ensure

```python
# With prompt dialog (default). Does nothing if already installed --
# uninstall first if you want to see the full install flow:
#   slicer.packaging.pip_uninstall("charset-normalizer")
slicer.packaging.pip_ensure("charset-normalizer&gt;=3.0", requester="ReviewTest")

# Without install prompt
slicer.packaging.pip_ensure("charset-normalizer&gt;=3.0", prompt_install=False, requester="ReviewTest")
```

### pip_ensure restart prompt

After installation, `pip_ensure` checks if any updated packages were already imported in the current session. If so, it shows a "Restart Recommended" dialog with details (old → new versions). The user can restart immediately or continue.

```python
import numpy  # Ensure numpy is in sys.modules

# Reinstall numpy (already imported) -- should trigger restart prompt
slicer.packaging.pip_uninstall("numpy")
slicer.packaging.pip_ensure("numpy&gt;=1.0", requester="ReviewTest")
# A "Restart Recommended" dialog should appear because numpy was already imported
```

To disable the restart prompt: `slicer.packaging.pip_ensure("numpy&gt;=1.0", prompt_restart=False)`

### With constraints file

```python
import tempfile, os

# Create a constraints file that pins charset-normalizer
with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
    f.write("charset-normalizer==3.3.2\n")
    constraints_path = f.name

# Install requests (which depends on charset-normalizer) with the constraint
slicer.packaging.pip_install("requests", constraints=constraints_path)
os.unlink(constraints_path)
```

### With skip_packages (selective dependency installation)

&gt; **Note:** `skip_packages` is a discouraged workaround for transitive dependency conflicts; see the script repository's "Python package management" section for guidance.

```python
# Install scikit-image but skip imageio (one of its dependencies)
skipped = slicer.packaging.pip_install(
    "scikit-image",
    skip_packages=["imageio"],
    requester="ReviewTest",
)
print(f"Skipped: {skipped}")

# Or via pip_ensure:
skipped = slicer.packaging.pip_ensure(
    "scikit-image&gt;=0.20",
    skip_packages=["imageio"],
    requester="ReviewTest",
)
```

### PythonSlicer (command-line) usage

Run this from a terminal using Slicer's PythonSlicer executable (not the Slicer Python console):

```bash
/path/to/PythonSlicer -c "import slicer.packaging; slicer.packaging.pip_install('charset-normalizer')"
```

This verifies that `pip_install` works in the PythonSlicer environment where `slicer.app` and Qt are not available. The function automatically falls back to simple blocking mode.

&lt;/details&gt;

---

&lt;details&gt;
&lt;summary&gt;&lt;strong&gt;Design Rationale (click to expand)&lt;/strong&gt;&lt;/summary&gt;

### Why requirements.txt? And why also pyproject.toml?

`requirements.txt` is the primary recommended format. Slicer extensions aren't Python packages — they just need "install these things into this environment," which is exactly what `requirements.txt` is for. It's pip's native input format, every Python developer knows it, and it requires no boilerplate beyond the dependency list itself.

That said, `pyproject.toml` is the modern standard in the Python ecosystem (PEP 621). It offers structured parsing via `tomllib` (stdlib) with no ad-hoc text handling, and extensions that already have a `pyproject.toml` for other tooling (ruff, pytest, etc.) can keep dependencies in one file. So we provide `load_pyproject_dependencies` as an alternative for extensions that prefer it.

Both formats boil down to PEP 508 dependency strings. Both loader functions return the same `list[Requirement]` type, so the downstream API (`pip_check`, `pip_ensure`, `pip_install`) works identically regardless of which one you use.

`load_pyproject_dependencies` reads only the `[project.dependencies]` list. Other fields in the `[project]` table (`name`, `version`, etc.) are not read or validated — extensions aren't Python packages and shouldn't need to provide them.

### Why pure-Python pip_check instead of pip --dry-run?

Installing is not done frequently, but _checking_ may be called frequently. A pure-Python implementation using `importlib.metadata` avoids the overhead of a subprocess. If we used `pip --dry-run` it would have to be a subprocess.

### Why explicit pip_ensure instead of lazy import magic?

We considered [LazyImportGroup](https://github.com/Slicer/Slicer/issues/7707) which intercepts first use of imports to trigger installation. It is elegant, but it reduces transparency and makes debugging harder for extension developers. For now we get this pattern which has more boilerplate but is more transparent and simple to debug:

```python
slicer.packaging.pip_ensure(reqs, requester="MyExtension")
import my_dependency  # Explicit, debuggable
```

IDE support works via `TYPE_CHECKING`:
```python
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    import my_dependency  # For type hints only
```

We can still consider the lazy import ideas in the future -- the lower level tools here would still be useful.

### Why `pip_install` now defaults to showing a progress dialog

Before this PR, `pip_install` was always blocking with no progress feedback. The new defaults (`blocking=True`, `show_progress=True`) mean existing code that calls `pip_install` will now get a modal progress dialog "for free" without any code changes. This improves UX for many extensions immediately, while still allowing opt-out via `show_progress=False`.

Hopefully it doesnt' break too many extensions...

### Prevention of multiple non-blocking pip installs

When `pip_install` runs with `blocking=False`, it returns immediately while pip runs in the background. If another non-blocking `pip_install` is started before the first completes then we get chaos.

The solution adopted here is a module-level `_pip_install_in_progress` flag that raises `RuntimeError` if a second non-blocking install is attempted. Developers can check `isPipInstallInProgress()` first if they want to guard against this themselves.

### Why `no_deps_requirements` parameter

Some Python packages declare overly strict dependency requirements that conflict with other packages in Slicer's environment. The standard workaround requires two separate pip calls:

```python
pip_install("--no-deps problematic-package==1.0")  # Ignore its deps
pip_install("numpy scipy")  # Install known-good deps manually
```

The `no_deps_requirements` parameter handles this two-step process internally, making the intent self-documenting:

```python
pip_install(requirements="numpy scipy", no_deps_requirements="problematic-pkg==1.0")
```

This also correctly handles non-blocking mode by chaining the two pip calls internally.

### Why `skip_packages` parameter

`skip_packages` is a discouraged workaround, included reluctantly because it solves a real problem that has no clean alternative for some packages.

Multiple Slicer extensions (SlicerTotalSegmentator, SlicerNNUNet) independently implement ~70-90 lines of recursive selective-install code to install packages while excluding certain transitive dependencies. Common examples: SimpleITK (Slicer bundles a custom version), torch (must be installed via SlicerPyTorch for the correct CUDA/CPU build), and requests (already bundled, replacing it forces an unnecessary restart). For packages like nnUNet with deep transitive dependency trees, manually enumerating the full dependency list (the alternative `no_deps_requirements` approach) would impose a significant maintenance burden across every upstream version bump.

The `skip_packages` parameter centralizes this logic so extensions don't each reinvent it. When provided, each package is installed with `--no-deps`, its dependency tree is walked recursively, and any package matching the skip list is excluded. Package METADATA is updated after installation so that `pip check` doesn't flag skipped packages as missing.

The downsides are real: METADATA scrubbing hides genuine conflicts, `pip show` no longer reflects the true dependency graph, and skip lists drift as Slicer's bundled packages change. Documentation discourages reaching for `skip_packages` first and points developers at upstream fixes or `no_deps_requirements` where those are tractable.

### `skip_packages` vs `no_deps_requirements`

Both are available; they serve different purposes:

- **`no_deps_requirements`**: "Install these packages without any of their deps." You provide the correct deps yourself. Fast (2 pip calls), doesn't modify METADATA. Use when a specific package has broken dependency declarations *and* the dependency tree is small enough to enumerate by hand.
- **`skip_packages`**: "Install everything except these specific packages, anywhere in the dependency tree." Automatic recursive walk with METADATA scrubbing. Slower (one pip call per package). The escape hatch for cases where the dependency tree is too deep to enumerate manually.

They are mutually exclusive — providing both raises `ValueError`.

### Why `pip_install` doesn't accept `list[Requirement]`

It would feel natural to write `pip_install(load_requirements("requirements.txt"))`. The fact that you can't is a little unfortunate — it looks like it *should* work. But `pip_install` is extremely widely used in the wild (via `slicer.util.pip_install`), and we don't want to make breaking changes to its signature. It's also a low-level function that mirrors the pip CLI, taking the same kind of string arguments you'd pass on the command line, so it makes sense to leave it working the way it does.

The new structured `list[Requirement]` input type goes into the new `slicer.packaging` functions instead: `pip_check` and `pip_ensure`. In practice, `slicer.packaging.pip_ensure(load_requirements("requirements.txt"))` is the call you want anyway -- it checks what's already installed, prompts the user, installs only what's missing, and detects whether a restart is needed. So accepting `Requirement` objects at the `pip_ensure` level rather than the `pip_install` level steers developers toward the safer, idempotent workflow.

### Why `pip_` function naming

The new functions follow the existing naming convention established by `slicer.util.pip_install` and `slicer.util.pip_uninstall`. All pip-related functions now live together in `slicer.packaging` with the `pip_` prefix, providing a consistent, discoverable API.

### Why `slicer.packaging` (module naming)

`slicer.packaging` was always the preferred name -- it's descriptive and mirrors the well-known third-party `packaging` library. Getting there involved an unexpected detour.

The first attempt at the name failed: `slicer/packaging.py` shadowed the third-party `packaging` library, breaking `from packaging.requirements import Requirement` everywhere. Tracing the root cause led to CTK: `ctkAbstractPythonManager::executeFile` prepends the executed script's directory to `sys.path[0]` and never removes it. Since Slicer runs `slicerqt.py` at startup, and `slicerqt.py` lived inside `bin/Python/slicer/`, that directory landed on `sys.path[0]` -- which silently promoted every file inside the `slicer/` package to a top-level module name and shadowed any PyPI package of the same name.

The Slicer-side fix is to move `slicerqt.py` out of the `slicer/` package directory (commit 4 in this PR). With `slicerqt.py` at `bin/Python/`, CTK's prepend lands on a path that's already on `sys.path`, so the harmful side effect goes away. The CTK behavior is still a bug and worth fixing upstream separately, but the workaround on the Slicer side is good cleanup on its own merits: `slicerqt.py` is conceptually a startup script, not a member of the `slicer` package.

With `slicerqt.py` moved, `slicer.packaging` is once again a safe name and is what this PR ships.

### Why `import slicer.packaging` is explicit

You need `import slicer.packaging` to use it -- like any normal Python submodule. The reason this is even worth mentioning is that historically `slicer.util` works without an explicit import, because the interactor startup script reaches into the user's `__main__` namespace and pre-populates a handful of names from it. This PR narrows that startup pre-population from a wildcard to an explicit 5-name list (see commit 4), which is part of why the contrast is now sharper. There's no special reason `slicer.packaging` couldn't be added to that startup list; we chose not to because top-level Python module imports in `slicer.packaging` (e.g. `packaging.requirements`, `importlib.metadata`) would be paid by every Slicer session even though most never install a Python package, and "type one extra import line in your extension" is a trivial cost.

### Why `pip_uninstall` was also modified

While the focus of this work is on dependency installation, `pip_uninstall` was updated with the same non-blocking parameters (`blocking`, `logCallback`, `completedCallback`) for API consistency. Since both functions share the same underlying infrastructure (`launchConsoleProcess` and `_executePythonModule`) in `slicer.packaging`, extending non-blocking support to `pip_uninstall` required minimal additional code and ensures users have a symmetric API for both operations.

### Non-blocking implementation

The non-blocking mode uses a QTimer-based polling approach inspired by [SlicerMONAIAuto3DSeg](https://github.com/lassoan/SlicerMONAIAuto3DSeg). A background thread reads process output into a queue while QTimer polls from the main thread, keeping the Qt event loop responsive.

### How the restart prompt works

After `pip_ensure` installs packages, it snapshots all installed package versions (before and after) using `importlib.metadata`. For any packages whose version changed, it checks whether their top-level import names appear in `sys.modules` (meaning they were already imported in the current session). The distribution-to-import-name mapping uses `importlib.metadata.packages_distributions()` (Python 3.11+). If any already-imported packages were updated, a "Restart Recommended" dialog shows the affected packages with their old → new versions. The `prompt_restart=False` parameter disables this check.

&lt;/details&gt;

---

&lt;details&gt;
&lt;summary&gt;&lt;strong&gt;Interactive Feature Tour (click to expand)&lt;/strong&gt;&lt;/summary&gt;

Build Slicer from the `python-dependency-handling-improvements` branch, launch it, open the Python console, and paste the script below. A menu lets you pick which demos to run — or select "Run All" for the full walkthrough.

```python
import importlib.metadata as _md
import os
import tempfile

import qt
from packaging.requirements import Requirement

import slicer
import slicer.packaging

# ---------------------------------------------------------------------------
# Configuration — change these to try a different demo package
# ---------------------------------------------------------------------------

DEMO_PACKAGE = "scikit-image"        # pip install name
DEMO_IMPORT = "skimage"              # Python import name
DEMO_CONSTRAINT = "&gt;=0.20,&lt;0.25"     # version range for constraints demo
DEMO_SKIP_DEP = "imageio"            # dependency to skip in skip_packages demo

# ---------------------------------------------------------------------------
# State
# ---------------------------------------------------------------------------

try:
    pkg_version_before_tour = _md.version(DEMO_PACKAGE)
except _md.PackageNotFoundError:
    pkg_version_before_tour = None


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def clear_cache():
    """Purge the pip download cache so installs show real download progress."""
    slicer.packaging._executePythonModule("pip", ["cache", "purge"])


def uninstall_pkg():
    """Remove the demo package if present."""
    try:
        slicer.util.pip_uninstall(DEMO_PACKAGE)
    except Exception:
        pass


def fresh_slate():
    """Uninstall the demo package and clear the cache."""
    uninstall_pkg()
    clear_cache()


# ---------------------------------------------------------------------------
# Demo 1 — Loading Dependencies
# ---------------------------------------------------------------------------

def demo_loading_deps():
    """load_requirements() and load_pyproject_dependencies()"""

    # --- requirements.txt ---
    slicer.util.infoDisplay(
        "load_requirements(path) parses a requirements.txt file into\n"
        "Requirement objects, skipping comments, blanks, and pip options.\n"
        "\n"
        "Watch the Python console for parsed results.",
        windowTitle="Demo 1: Loading Dependencies — requirements.txt",
    )

    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write("# Example requirements file\n")
        f.write("numpy&gt;=1.20\n")
        f.write(f"{DEMO_PACKAGE}&gt;=0.20\n")
        f.write("nonexistent-package-xyz&gt;=1.0\n")
        f.write("-c constraints.txt\n")
        f.write("\n")
        path = f.name

    reqs = slicer.packaging.load_requirements(path)
    os.unlink(path)

    lines = [f"  {r.name}  {r.specifier}" for r in reqs]
    print(f"[Tour] load_requirements -&gt; {len(reqs)} requirements:\n" + "\n".join(lines))

    # --- pyproject.toml ---
    with tempfile.NamedTemporaryFile(mode="w", suffix=".toml", delete=False) as f:
        f.write("[project]\n")
        f.write("dependencies = [\n")
        f.write('    "numpy&gt;=1.20",\n')
        f.write(f'    "{DEMO_PACKAGE}&gt;=0.20",\n')
        f.write('    "nonexistent-package-xyz&gt;=1.0",\n')
        f.write("]\n")
        path = f.name

    reqs2 = slicer.packaging.load_pyproject_dependencies(path)
    os.unlink(path)

    lines2 = [f"  {r.name}  {r.specifier}" for r in reqs2]
    print(f"[Tour] load_pyproject_dependencies -&gt; {len(reqs2)} requirements:\n" + "\n".join(lines2))

    slicer.util.infoDisplay(
        f"Loaded {len(reqs)} requirements from requirements.txt\n"
        f"and {len(reqs2)} from pyproject.toml.\n"
        "\n"
        "Both return the same Requirement objects — the downstream\n"
        "API (pip_check, pip_ensure) works identically with either.",
        windowTitle="Demo 1: Loading Dependencies — result",
    )


# ---------------------------------------------------------------------------
# Demo 2 — Checking Requirements
# ---------------------------------------------------------------------------

def demo_checking_reqs():
    """pip_check() — pure-Python requirement validation"""

    slicer.util.infoDisplay(
        "pip_check(req) checks if a requirement is satisfied.\n"
        "Pure Python, no subprocess — fast enough to call frequently.\n"
        "\n"
        "We will test several cases against the current environment.",
        windowTitle="Demo 2: Checking Requirements",
    )

    checks = [
        ("numpy&gt;=1.0", "Bundled with Slicer — should be satisfied"),
        ("numpy&gt;=99999.0", "Impossibly high version — should fail"),
        ("nonexistent-xyz&gt;=1.0", "Package not installed"),
        ('foo; sys_platform == "nonexistent"', "Marker does not apply — treated as satisfied"),
    ]

    results = []
    for spec, desc in checks:
        req = Requirement(spec)
        ok = slicer.packaging.pip_check(req)
        mark = "SATISFIED" if ok else "NOT satisfied"
        results.append(f"  [{mark}]  {spec}\n      {desc}")

    slicer.util.infoDisplay(
        "pip_check results:\n"
        "\n" + "\n\n".join(results),
        windowTitle="Demo 2: Checking Requirements — results",
    )


# ---------------------------------------------------------------------------
# Demo 3 — Installing with Progress
# ---------------------------------------------------------------------------

def demo_install_progress():
    """pip_install() — modal dialog and non-blocking status bar"""

    # --- Part 1: Modal (blocking) ---
    fresh_slate()

    slicer.util.infoDisplay(
        "pip_install() — modal progress dialog (the new default).\n"
        "\n"
        "Try expanding the Details section!",
        windowTitle="Demo 3a: Modal Progress Dialog",
    )

    slicer.util.pip_install(DEMO_PACKAGE, requester="Feature Tour")

    slicer.util.infoDisplay(
        "Modal install done.\n"
        "\n"
        "Now switching to non-blocking mode: the call returns\n"
        "immediately and pip output appears in the status bar.",
        windowTitle="Demo 3a: Modal — done",
    )

    # --- Part 2: Non-blocking ---
    fresh_slate()

    slicer.util.infoDisplay(
        "pip_install() — non-blocking with status bar.\n"
        "\n"
        "Watch the STATUS BAR at the bottom. The UI stays interactive.\n"
        "isPipInstallInProgress() will be printed to the console.",
        windowTitle="Demo 3b: Status Bar Mode",
    )

    loop = qt.QEventLoop()
    _result = [None]

    def on_complete(return_code):
        _result[0] = return_code
        qt.QTimer.singleShot(0, loop.quit)

    slicer.util.pip_install(
        DEMO_PACKAGE,
        blocking=False,
        show_progress=True,
        requester="Feature Tour",
        completedCallback=on_complete,
    )

    # Check in-progress flag shortly after starting
    qt.QTimer.singleShot(500, lambda: print(
        f"[Tour] isPipInstallInProgress() = {slicer.packaging.isPipInstallInProgress()}"
    ))

    loop.exec_()

    slicer.util.infoDisplay(
        f"Non-blocking install finished (return code {_result[0]}).\n"
        "The status bar showed pip output while the UI stayed responsive.",
        windowTitle="Demo 3b: Status Bar — done",
    )


# ---------------------------------------------------------------------------
# Demo 4 — Smart Install Workflow
# ---------------------------------------------------------------------------

def demo_smart_install():
    """pip_ensure() — check, prompt, install, restart detection"""

    # --- Part 1: Normal pip_ensure ---
    fresh_slate()

    slicer.util.infoDisplay(
        "pip_ensure() — the recommended high-level API for extensions.\n"
        "Checks requirements, shows confirmation, installs with progress.\n"
        "\n"
        "You will see a confirmation dialog, then a progress dialog.",
        windowTitle="Demo 4a: pip_ensure",
    )

    reqs = [Requirement(f"{DEMO_PACKAGE}&gt;=0.20")]
    slicer.packaging.pip_ensure(reqs, requester="Feature Tour")

    slicer.util.infoDisplay(
        "pip_ensure done. Now we will call it again immediately.\n"
        "\n"
        "pip_check sees the package is already installed, so\n"
        "pip_ensure skips everything — no dialogs, instant return.",
        windowTitle="Demo 4a: pip_ensure — done",
    )

    slicer.packaging.pip_ensure(reqs, requester="Feature Tour (no-op)")

    slicer.util.infoDisplay(
        "pip_ensure returned instantly — nothing to install.\n"
        "\n"
        "Now: restart prompt demo. We will import the package, uninstall\n"
        "it, then pip_ensure again. Since it is in memory, a restart\n"
        "dialog will appear. (Click NO when asked to restart to continue the tour.)",
        windowTitle="Demo 4a: pip_ensure — no-op verified",
    )

    # --- Part 2: Restart prompt ---
    import importlib
    mod = importlib.import_module(DEMO_IMPORT)
    print(f"[Tour] Imported {DEMO_IMPORT} {mod.__version__}")

    uninstall_pkg()
    clear_cache()

    slicer.packaging.pip_ensure(reqs, requester="Feature Tour (restart demo)")

    slicer.util.infoDisplay(
        "Restart prompt demonstrated.\n"
        "\n"
        "This helps users know when a restart is needed after\n"
        "updating packages that were already imported.",
        windowTitle="Demo 4b: Restart Prompt — done",
    )


# ---------------------------------------------------------------------------
# Demo 5 — Advanced Options
# ---------------------------------------------------------------------------

def demo_advanced_options():
    """Constraints file and skip_packages"""

    # --- Part 1: Constraints ---
    fresh_slate()

    slicer.util.infoDisplay(
        "Constraints file: limits which versions pip may install.\n"
        f"\n"
        f"Installing {DEMO_PACKAGE} constrained to {DEMO_CONSTRAINT}.",
        windowTitle="Demo 5a: Constraints",
    )

    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
        f.write(f"{DEMO_PACKAGE}{DEMO_CONSTRAINT}\n")
        constraints_path = f.name

    slicer.util.pip_install(
        DEMO_PACKAGE,
        constraints=constraints_path,
        requester="Feature Tour (constrained)",
    )
    os.unlink(constraints_path)

    ver = _md.version(DEMO_PACKAGE)
    slicer.util.infoDisplay(
        f"Installed {DEMO_PACKAGE} {ver} (constrained to {DEMO_CONSTRAINT}).\n"
        "\n"
        f"Now: skip_packages demo — installing {DEMO_PACKAGE}\n"
        f"while skipping '{DEMO_SKIP_DEP}' (one of its dependencies).\n"
        f"\n"
        f"First we uninstall {DEMO_SKIP_DEP} (if present) so we can\n"
        f"verify at the end that skip_packages actually prevented it.",
        windowTitle="Demo 5a: Constraints — done",
    )

    # --- Part 2: skip_packages ---
    fresh_slate()
    try:
        slicer.util.pip_uninstall(DEMO_SKIP_DEP)
    except Exception:
        pass

    skipped = slicer.util.pip_install(
        DEMO_PACKAGE,
        skip_packages=[DEMO_SKIP_DEP],
        requester="Feature Tour (skip_packages)",
    )

    lines = [f"  {s}" for s in (skipped or [])]
    print(f"[Tour] Skipped packages:\n" + "\n".join(lines))

    # Verify the metadata scrub: re-install normally, check the skipped dep
    slicer.util.pip_install(DEMO_PACKAGE, requester="Feature Tour (verify scrub)")
    dep_installed = slicer.packaging.pip_check(Requirement(DEMO_SKIP_DEP))

    slicer.util.infoDisplay(
        f"Skipped {len(skipped or [])} package(s).\n"
        f"{DEMO_SKIP_DEP} installed after normal re-install: {dep_installed}\n"
        "\n"
        "Re-installing normally did NOT pull in the skipped dependency\n"
        "because the metadata scrub removed it.",
        windowTitle="Demo 5b: skip_packages — verified",
    )


# ---------------------------------------------------------------------------
# Cleanup
# ---------------------------------------------------------------------------

def do_cleanup():
    """Restore the user's environment."""
    if pkg_version_before_tour is not None:
        msg = (
            f"{DEMO_PACKAGE} {pkg_version_before_tour} was installed before\n"
            "the tour. Restore it now?"
        )
    else:
        msg = f"Uninstall {DEMO_PACKAGE} to leave your environment clean?"

    if slicer.util.confirmYesNoDisplay(msg, windowTitle="Feature Tour — Cleanup"):
        if pkg_version_before_tour is not None:
            uninstall_pkg()
            slicer.util.pip_install(
                f"{DEMO_PACKAGE}=={pkg_version_before_tour}",
                requester="Feature Tour (restore)",
            )
        else:
            uninstall_pkg()

    slicer.util.infoDisplay(
        "Tour complete! For full API docs:\n"
        "  help(slicer.packaging.pip_ensure)",
        windowTitle="Feature Tour — Done",
    )


# ---------------------------------------------------------------------------
# Menu and main loop
# ---------------------------------------------------------------------------

MENU_ITEMS = [
    "1. Loading Dependencies",
    "2. Checking Requirements",
    "3. Installing with Progress",
    "4. Smart Install Workflow",
    "5. Advanced Options",
    "---",
    "Run All",
    "Exit Tour",
]

DEMO_FUNCS = {
    MENU_ITEMS[0]: demo_loading_deps,
    MENU_ITEMS[1]: demo_checking_reqs,
    MENU_ITEMS[2]: demo_install_progress,
    MENU_ITEMS[3]: demo_smart_install,
    MENU_ITEMS[4]: demo_advanced_options,
}

DEMO_ORDER = MENU_ITEMS[:5]


def run_tour():
    slicer.util.infoDisplay(
        "Welcome to the PR #9010 Feature Tour!\n"
        "\n"
        "Pick demos from the menu. Uses scikit-image as a demo package\n"
        "(configurable via DEMO_PACKAGE at the top of the script).\n"
        'Select "Run All" for the full experience.',
        windowTitle="Feature Tour — Welcome",
    )

    while True:
        dialog = qt.QInputDialog(slicer.util.mainWindow())
        dialog.setWindowTitle("Feature Tour")
        dialog.setLabelText("Choose a demo:")
        dialog.setComboBoxItems(MENU_ITEMS)
        dialog.setComboBoxEditable(False)

        if dialog.exec_() != qt.QDialog.Accepted:
            break

        choice = dialog.textValue()

        if choice == "Exit Tour" or choice == "---":
            break

        if choice == "Run All":
            for key in DEMO_ORDER:
                DEMO_FUNCS[key]()
        else:
            func = DEMO_FUNCS.get(choice)
            if func:
                func()

    do_cleanup()


# ---------------------------------------------------------------------------
# Start the tour
# ---------------------------------------------------------------------------

run_tour()
```

&lt;/details&gt;

---

&lt;details&gt;
&lt;summary&gt;&lt;strong&gt;References (click to expand)&lt;/strong&gt;&lt;/summary&gt;

- This work is part of the [44th Slicer project week](https://projectweek.na-mic.org/PW44_2026_GranCanaria/Projects/PythonDependenciesInExtensions/)!
- [#7171 — Improving Support for Python Package Dependencies in Slicer Extensions](https://github.com/Slicer/Slicer/issues/7171) — This PR implements the "runtime installation" approach described in the issue: extensions declare dependencies via `requirements.txt`, and the new `slicer.packaging` module handles checking and installation with optional constraints file support for coordinating versions across extensions.
- [#7707 — Allow scripted modules to declare and lazily install pip requirements](https://github.com/Slicer/Slicer/issues/7707) — Proposes a `LazyImportGroup` context manager that intercepts imports and triggers installation on first attribute access. This PR takes a simpler, more explicit approach: developers call `pip_ensure()` at the point dependencies are needed, then import normally. The explicit pattern trades some elegance for transparency and easier debugging. The `LazyImportGroup` approach could potentially be built on top of the primitives provided by `slicer.packaging` (`load_requirements`, `pip_check`, `pip_install` with callbacks) if desired in the future. See #8181.
- At https://github.com/KitwareMedical/SlicerNNUnet/pull/21 is a demo of how some of the features here can simplify python dependency handling in the NNUnet extension.

&lt;/details&gt;</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
