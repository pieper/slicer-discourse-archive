# Slicelet vs Guidelet

**Topic ID**: 18336
**Date**: 2021-06-25
**URL**: https://discourse.slicer.org/t/slicelet-vs-guidelet/18336

---

## Post #1 by @seanchoi0519 (2021-06-25 09:46 UTC)

<p>Hello</p>
<p>i’m looking to create a custom module now that I’ve established the workflow of my project. It involves connecting the functionalities of the ALPACA, then processed by Model-to-Model distance, then analyzed by ShapePopulationViewer.</p>
<p>Should I be looking at creating a slicelet or a guidelet for this project?<br>
I’d like to make a full-screen custom application similar to the one used in the LumpNav project (<a href="https://github.com/SlicerIGT/LumpNav" class="inline-onebox" rel="noopener nofollow ugc">GitHub - SlicerIGT/LumpNav: Slicer extension for ultrasound-guided breast tumor resection (lumpectomy)</a>)</p>
<p>Also, on a side note, I’m having trouble loading QtDesigner - what is the correct procedure to launch the designer? Am I supposed to download something? And how do I launch it (command line?)?</p>
<p>This is the error I get on my MacOS: Check with the developer to make sure Designer works with this version of macOS. You may need to reinstall the application. Be sure to install any available updates for the application and macOS</p>
<p>Many thanks</p>

---

## Post #2 by @lassoan (2021-06-25 17:38 UTC)

<p>Guidelet is a specific type of slicelet, for implementing surgical navigation applications where you use a real-time image and position tracking data streams. If you don’t have data streams coming in then you’ll implement a general-purpose slicelet.</p>
<p>Qt designer troubles on macOS is a known issue. Until it gets resolved you can apply the workaround described here: <a href="https://github.com/Slicer/Slicer/issues/4700#issuecomment-832792142" class="inline-onebox">QT Designer does not start on MacOS · Issue #4700 · Slicer/Slicer · GitHub</a></p>

---

## Post #4 by @pll_llq (2021-06-27 13:13 UTC)

<aside class="quote no-group" data-username="seanchoi0519" data-post="1" data-topic="18336">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/seanchoi0519/48/10354_2.png" class="avatar"> seanchoi0519:</div>
<blockquote>
<p>Also, on a side note, I’m having trouble loading QtDesigner - what is the correct procedure to launch the designer? Am I supposed to download something? And how do I launch it (command line?)?</p>
<p>This is the error I get on my MacOS: Check with the developer to make sure Designer works with this version of macOS. You may need to reinstall the application. Be sure to install any available updates for the application and macOS</p>
</blockquote>
</aside>
<p>The only way I managed to get Qt Designer to work on macOS is by building Slicer from source and launching Slicer with <code>--designer</code> flag before packaging.</p>

---
