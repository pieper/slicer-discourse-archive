---
topic_id: 48176
title: "Best practices for more complex plots in Slicer?"
date: 2026-09-15
url: https://discourse.slicer.org/t/48176
last_bumped: 2026-10-01T18:55:56.592Z
---

# Best practices for more complex plots in Slicer?

**Topic ID**: 48176
**Date**: 2026-09-15
**URL**: https://discourse.slicer.org/t/best-practices-for-more-complex-plots-in-slicer/48176

---

## Post #1 by @mikebind (2026-09-15 22:12 UTC)

<p>The slicer.util.plot() infrastructure is pretty limited. It’s OK for basic viewing of data that is already in MRML tables, but clunky for other data and incapable of nicer data visualizations.  It would be really nice to be able to use or display more complex plots in Slicer or at least from Slicer.  However, whenever I try to find nice solutions (using matplotlib, seaborn, etc.) I run into problems.  The default backend in matplotlib crashes Slicer.  wxPython is heavy but does provide a functional (but poorly styled) interactive plot window… until you try to close the plot, which hangs and crashes Slicer. The best option I found in the forum is this suggestion using pyqtgraph <a href="https://discourse.slicer.org/t/pythonqt-properties-shadowing-methods/16992/15" class="inline-onebox">PythonQt properties shadowing methods - #15 by fbordignon</a> , but it appears like it might require a manual patch to PythonQt, and PySide2, which appears to no longer be compatible with Slicer’s python version (it requires &lt;3.10), so is not really an option any more in recent Slicer versions.  It seems likely that some options will become available when Slicer fully shifts to Qt6 (it seems like this hasn’t happened in 5.12, but I’m not sure I’m understanding the release notes).  In the meantime, what do people use?  It sounds possible to save static plots to image files and then stretch those across a qt widget.  Is that the best current option for more advanced plots in Slicer?</p>

---

## Post #2 by @pieper (2026-09-16 22:54 UTC)

<p>A couple ideas:</p>
<ul>
<li>
<p>For the reasons you pointed out, trying to force some of these python plotting packages into Slicer can lead to dependency clashes and random crashes.  Another option is to write out the data and plot independently in a subshell with a different python interpreter (being careful with the paths in the environment).  You can use the web server (and the exec endpoint) to get any data you need out of Slicer and make any changes you want to slicer in response to interactions with the plot.</p>
</li>
<li>
<p>But my personal preference is to use <a href="https://echarts.apache.org/en/index.html">Apache ECharts</a> with the qSlicerWebWidget.  Here’s a project page that describes it: <a href="https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/MultidimensionalExplorerGeneralization/">https://projectweek.na-mic.org/PW43_2025_Montreal/Projects/MultidimensionalExplorerGeneralization/</a>.  You have to feel comfortable using python and javascript together (or comfortable asking Claude to do it).</p>
</li>
</ul>
<p>Also, regarding Qt6, yes, it should be working everywhere now, we just haven’t made releases for it yet.</p>

---

## Post #3 by @mikebind (2026-09-17 16:34 UTC)

<p>Thanks for these suggestions, <a class="mention" href="/u/pieper">@pieper</a> .  The examples on the project page are very cool, and Apache ECharts does look quite capable.  Is there any example code available showing how to integrate this with Slicer?  I see the gist linked from the project page demonstrating the interactive html page, but would be curious to see an example of linking one of these plots to Slicer (like the MultiMapper module example shown in one of the linked videos), if it is possible to share that.</p>
<p>Separately, while I really enjoy being able to explore data like this in thoughtfully constructed interactive ways, it also takes an investment of time to create and develop them.  For cases where what I am looking for is closer to just displaying a static plot (but where I’d love to be able to zoom and pan), the subshell approach seems simpler and easier.  You caution that it’s necessary to be careful with the environment paths, is there an example that I could follow to try this approach as well?</p>
<p>As always, the help is much appreciated, thanks!</p>

---

## Post #4 by @pieper (2026-09-17 17:00 UTC)

<p>This code is a bit older, but it is the implementation that shows how to tie the js-based plotting to slicer features (here an older package the was pre-ECharts and an older version of Slicer, but the method is portable).</p><aside class="onebox githubrepo" data-onebox-src="https://github.com/pieper/SlicerMultiMapper">
  <header class="source">

      <a href="https://github.com/pieper/SlicerMultiMapper" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/6aafb27e95770e3012482e61709d30b9/pieper/SlicerMultiMapper" class="thumbnail">

  <h3><a href="https://github.com/pieper/SlicerMultiMapper" target="_blank" rel="noopener">GitHub - pieper/SlicerMultiMapper: Tools for creating parametric maps from...</a></h3>

    <p><span class="github-repo-description">Tools for creating parametric maps from multidimensional MRI</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The code goes both ways - you can select image intensity ranges from the plot and see the corresponding segmentation, or you can use the segmentation statistics to generate the plot.</p>
<p>I do agree that the ECharts option is “weird” since it mixes different programming worlds and may not be everyone’s favorite.  FWIW, modern coding agents don’t have much problem with mixing and matching feature from different languages, so I wouldn’t try writing from scratch as just asking the agent to adapt the code to your use case.</p>
<p>If you want to go with the two-process model and use standard python stuff I don’t have a specific plotting example, but here’s an example of how to launch a python based program (note the <code>useShartupEnvironment</code>option) and communicate using RPyC, which is actually quite powerful and convenient, but it bogs down on large data, so we use shared memory for numpy arrays.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerTMS/SlicerTMS/blob/tmsservice/Experiments/SlicerSimNIBSClient.py#L30">
  <header class="source">

      <a href="https://github.com/SlicerTMS/SlicerTMS/blob/tmsservice/Experiments/SlicerSimNIBSClient.py#L30" target="_blank" rel="noopener">github.com/SlicerTMS/SlicerTMS</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerTMS/SlicerTMS/blob/tmsservice/Experiments/SlicerSimNIBSClient.py#L30" target="_blank" rel="noopener">Experiments/SlicerSimNIBSClient.py</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/SlicerTMS/SlicerTMS/blob/tmsservice/Experiments/SlicerSimNIBSClient.py#L30" rel="noopener"><code>tmsservice</code></a>
</div>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="20" style="counter-reset: li-counter 19 ;">
          <li></li>
          <li></li>
          <li>slicer.mrmlScene.Clear()</li>
          <li></li>
          <li>try:</li>
          <li>    process.kill()</li>
          <li>except NameError:</li>
          <li>    pass</li>
          <li></li>
          <li>cmdList = [simnibs_pythonPath, SimNIBSServicePath]</li>
          <li class="selected">process = slicer.util.launchConsoleProcess(cmdList, useStartupEnvironment=True)</li>
          <li></li>
          <li>port = 18891</li>
          <li></li>
          <li>for attempt in range(10):</li>
          <li>	try:</li>
          <li>		simnibs = rpyc.connect("localhost", port,</li>
          <li>			config = {</li>
          <li>				"allow_public_attrs": True,</li>
          <li>				"allow_pickle": True,</li>
          <li>				"sync_request_timeout": None</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @mikebind (2026-09-17 17:21 UTC)

<p>Thanks, this is really helpful. I’ll probably explore some in both these directions and mark this solved.</p>

---

## Post #6 by @jamesobutler (2026-10-01 18:55 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> <a class="mention" href="/u/pieper">@pieper</a> Take a look at the following recent PR regarding making matplotlib functional in Slicer</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Slicer/Slicer/pull/9441">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/pull/9441" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Slicer/Slicer/pull/9441" target="_blank" rel="noopener nofollow ugc">ENH: Add an interactive Matplotlib backend built on PythonQt (#9441)</a>
      </h4>

    <div class="branches">
      <code>main</code> ← <code>ThomasKierski:tk/matplotlib-backend</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2026-10-01" data-time="18:45:55" data-timezone="UTC">06:45PM - 01 Oct 26 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/ThomasKierski" target="_blank" rel="noopener nofollow ugc">
            <img alt="" src="https://avatars.githubusercontent.com/u/54414492?v=4" class="onebox-avatar-inline" width="20" height="20">
            ThomasKierski
          </a>
        </div>

        <div class="lines" title="1 commits changed 5 files with 1620 additions and 2 deletions">
          <a href="https://github.com/Slicer/Slicer/pull/9441/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+1620</span>
            <span class="removed">-2</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container"># ENH: Add an interactive Matplotlib backend built on PythonQt

The following <span class="show-more-container"><a href="https://github.com/Slicer/Slicer/pull/9441" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">work was mostly written by Claude Opus 5 via the Copilot CLI. The work is motivated by the current limitations on stylizing plots in charts in the app. Matplotlib is familiar to many Python users and can generate some beautiful, interactive figures such as the ones shown in the demos below.

## Demos

### Matplotlib + Seaborn for nice looking plots
&lt;img width="1920" height="1032" alt="image" src="https://github.com/user-attachments/assets/25d7e8db-6b12-4e86-9dac-2c8380fab70c" /&gt;

### Interactive plot demo

https://github.com/user-attachments/assets/6ba8de1b-8fdc-4e98-90a1-d04582eb28bf


## Summary

Adds `slicer.matplotlibbackend`, a pure-Python Matplotlib backend that renders with Agg and
displays the result in a PythonQt `QWidget` driven by Slicer's own event loop. This gives
Slicer working interactive plots — pan, zoom, the navigation toolbar, `matplotlib.widgets`,
picking, animation and timers — without a C++ change, a new dependency, or a second Qt
binding.

```python
import slicer.matplotlibbackend
slicer.matplotlibbackend.enable()

import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
plt.show()   # interactive, and does not block the application
```

The canvas is an ordinary Qt widget, so it can also be placed in a module panel or in a
view layout:

```python
from matplotlib.figure import Figure
from slicer.matplotlibbackend import FigureCanvasSlicer, NavigationToolbar2Slicer

canvas = FigureCanvasSlicer(Figure())
self.layout.addWidget(canvas.get_widget())
```

---

## 1. What problem does this solve?

### Slicer currently has no usable interactive Matplotlib backend at all

Every interactive backend Matplotlib ships is unavailable in Slicer, for a different reason:

| Backend | Why it does not work in Slicer |
|---|---|
| `TkAgg` (Matplotlib's default) | Tcl/Tk was removed from the superbuild in `9a9c2b199d` ("ENH: Remove unsupported/deprecated tcl functionality", #4867). There is no `_tkinter`, so importing it raises `ImportError`. |
| `QtAgg` | Matplotlib's Qt backend targets PyQt or PySide. Slicer binds Qt through **PythonQt**, which those bindings cannot stand in for, and none of PyQt5/PySide2/PySide6 are shipped. |
| `WXAgg` | Requires `wxPython`, which is not shipped, and introduces a third GUI toolkit into the process. |

What was left is `Agg`: render to PNG, load into a `QPixmap`, display a static picture. That
rules out pan and zoom, the navigation toolbar, `matplotlib.widgets` (sliders, span/lasso
selectors), `pick_event`, `FuncAnimation`, and event callbacks — i.e. most of the reason to
reach for Matplotlib instead of Slicer's VTK plots.

### The documentation was stale, and steered users toward the one thing that really does crash

`Docs/developer_guide/script_repository/plots.md` claimed:

&gt; the default Tk backend locks up and crashes Slicer

That has not been true since Tk was removed. `TkAgg` now fails at import with a clean
`ImportError`; it cannot lock anything up, because it never loads.

The practical effect of that stale sentence is worse than a documentation nit. It sends users
looking for "a Qt backend that works", and the obvious move — `pip install PyQt5` into
Slicer's Python — loads a **second, independently initialized copy of Qt** into a process
that has already initialized Slicer's Qt: two `QApplication` objects, divergent plugin search
paths, duplicated static state. *That* is the instability users report and attribute to
Matplotlib. Nothing in the docs warned against it.

This PR corrects the explanation, documents why each backend fails, and states plainly that
installing PyQt/PySide into Slicer's Python is not a supported workaround.

### There was no supported way to embed a live plot in the application

Getting a Matplotlib figure into a module panel or a view layout meant re-rendering to a
`QPixmap` by hand on every change. `FigureCanvasSlicer` is a `QWidget`, so it drops into any
layout and repaints itself via `draw_idle()`.

---

## 2. What is in the change

- **`Base/Python/slicer/matplotlibbackend.py`** — the backend.
  `FigureCanvasSlicer`, `NavigationToolbar2Slicer`, `FigureManagerSlicer`, `TimerSlicer`,
  and an `enable()` convenience helper. Selected as `module://slicer.matplotlibbackend`.
- **`Base/Python/slicer/tests/test_slicer_matplotlibbackend.py`** — 15 unit tests, registered
  with CTest and skipped automatically when Matplotlib is not installed, so CI without
  Matplotlib is unaffected.
- **`Docs/developer_guide/script_repository/plots.md`** — corrected explanation plus worked
  examples: a basic interactive plot, embedding in a module panel, a live histogram wired
  into the Four-Up Plot layout, and a seaborn segment-statistics dashboard.
- **CMake registration** for the module and the test.

Verified working: pan/zoom/home, all seven toolbar actions, `matplotlib.widgets`, `pick_event`,
`FuncAnimation`, `new_timer`, key/mouse/wheel/resize event delivery with upstream-compatible
key names, `savefig`, HiDPI via `devicePixelRatioF`, blitting, the zoom rubber band, cursor
changes, and `close_event`.

---

## 3. Approaches that were considered and rejected

These are recorded because several of them look like the obvious answer.

**Restore Tcl/Tk to the superbuild so `TkAgg` works again.**
Tk was removed deliberately as unsupported/deprecated. Re-adding an entire GUI toolkit to
recover one backend would mean pumping Tk's event loop alongside Qt's, and the result is a
foreign-looking top-level window that cannot be embedded in a Slicer layout or module panel.
Large cost, poor result.

**Ship PyQt5/PySide2/PySide6 so Matplotlib's `QtAgg` works.**
Rejected, and now explicitly warned against in the docs. Two independently initialized Qt
libraries in one process is the actual source of the crashes attributed to Matplotlib. This
is a trap to close, not a path to take.

**Keep recommending `WXAgg`.**
This was the previously documented "interactive" route. It requires pip-installing wxPython,
pulls a third GUI toolkit into the process, and produces windows that cannot be embedded in
Slicer's UI. Left in the docs for continuity, but demoted in favour of the built-in backend.

**Adapt Matplotlib's existing `backend_qt` to PythonQt via a shim module.**
Superficially attractive — reuse upstream's Qt backend by presenting PythonQt as though it
were QtPy. In practice `backend_qt` depends on a large, version-specific slice of the Qt
binding surface: the `QtCore`/`QtGui`/`QtWidgets` split, enum access patterns, signal/slot
connection styles, and private helpers such as `_enum()` and `_getSaveFileName`. A shim would
have to track Matplotlib's internals release by release. Writing a small backend against the
stable, public `backend_bases` API is considerably less fragile.

**Mirror upstream's multiple inheritance, `class FigureCanvasQT(FigureCanvasBase, QWidget)`.**
PythonQt wraps C++ classes dynamically, and combining such a wrapper with a second Python
base class in one `class` statement is outside its supported surface. This PR uses composition
instead: `FigureCanvasSlicer(FigureCanvasAgg)` *owns* a `_CanvasWidget(qt.QWidget)`, reachable
via `canvas.get_widget()` (or the `widget` property). The cost is one extra indirection and a
small divergence from upstream's class shape; the benefit is staying inside documented
PythonQt behaviour.

**Intercept input with an `eventFilter` or the `event()` catch-all instead of per-event handlers.**
Both were probed and both work under PythonQt. Rejected anyway: overriding the individual
handlers (`mousePressEvent`, `wheelEvent`, `keyPressEvent`, …) is clearer, matches upstream's
structure, and probes confirmed every handler override is delivered.

**Render plots through Qt WebEngine with a JavaScript plotting library (mpld3, Plotly).**
This does not make *Matplotlib* interactive; it replaces it with a different API that has no
`matplotlib.widgets` and no `FuncAnimation`, while adding a heavy dependency and a
serialization boundary.

**Rely on SlicerJupyter's `slicernb.MatplotlibDisplay`.**
Only applies inside a notebook kernel, and still produces static images. It does not help the
desktop application.

---

## 4. Notes for reviewers

Because the backend lives inside the `slicer` package, **adding the source directory to
`sys.path` or to Slicer's "additional module paths" will not make it importable** — `slicer`
has already been imported from the install tree, and the additional-module-paths setting
scans for `ScriptedLoadableModule` classes rather than adding Python import paths. Pointing
that setting at `Base/Python/slicer` also puts the directory on `sys.path`, where
`slicer/packaging.py` shadows the real `packaging` distribution and breaks
`slicer.util.pip_install`.

To try the branch against an existing install without rebuilding, extend the package path in
`.slicerrc.py`:

```python
import slicer as _slicer
_slicerSourceDir = r"&lt;checkout&gt;/Base/Python/slicer"
if _slicerSourceDir not in _slicer.__path__:
    _slicer.__path__.insert(0, _slicerSourceDir)
```

---

## 5. Testing

Exercised on Slicer 5.130.0-2026-09-29, 5.12.1, Qt 5.15.2, Python 3.12.10, Matplotlib 3.11.2:

- 15 unit tests (`test_slicer_matplotlibbackend.py`), run under `--no-main-window`
- a 22-check functional suite driving real Qt events through pan, zoom, picking, widgets,
  animation, resize, save and close
- a 19-case probe of cursors, blitting, the rubber band, the event loop, full-screen, key
  translation and toolbar icons
- every code snippet in the updated documentation, executed verbatim as written

## 6. Known gaps

- **Qt 6 is guarded but unexercised.** The three known breaking changes are handled
  defensively — `QMouseEvent.position()` vs `x()`/`y()`, `XButton1/2` vs `BackButton`/
  `ForwardButton`, and `QEventLoop.exec_()` vs `exec()` — but no Qt 6 build was available to
  run them.
- **Linux and macOS are untested**, specifically the `xcb` scroll-event special case and
  Retina device-pixel-ratio handling.
- **`configure_subplots` calls `figure.tight_layout()`** rather than opening the subplot-tool
  dialog. Deliberate simplification; straightforward to extend later.</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
