---
topic_id: 5436
title: "Volume Reslicing Slow Insome Cases"
date: 2019-01-21
url: https://discourse.slicer.org/t/5436
---

# Volume Reslicing slow insome cases

**Topic ID**: 5436
**Date**: 2019-01-21
**URL**: https://discourse.slicer.org/t/volume-reslicing-slow-insome-cases/5436

---

## Post #1 by @mcfly3001 (2019-01-21 08:34 UTC)

<p>Hi everyone,</p>
<p>I am using slicer to visualize a tracked tool in the MPR planes and found some performance issues where the framerate drops down to ~13 FPS. Using Slicer 4.10, I load the CT-Chest volume, add a coordinate system via the CreateModels plugin and then start receiving transforms via OpenIGTLink interface (with 40 FPS). The loaded model is attached to this transform and thus moves accordingly in the 3D view.</p>
<ul>
<li>The rendering at the beginning runs smoothly at ~33FPS. The model though at this point is not rendered in the MPR planes</li>
<li>To activate the model in the MPRs I first have to click hide and then show. Now the model also shows up in the MPR views but the frame rate drops to ~13FPS. If I deactivate some of the views, e.g. green and yellow, the frame rate goes up again.</li>
<li>When I switch to the Volume Reslice Driver (IGT Plugin) and set the driver to be the received transform, the frame rate also increases to ~20 FPS. In this case, the loaded model is also shown in all MPR views</li>
</ul>
<p>I am running Slicer on my mobile Workstation (i7-7820HQ and NVIDIA Quadro M2200). Anyone has an idea where the drop in the framerate can come from? For me it seems strange that the FPS are higher when using the reslice driver.<br>
How could the framerate be increased? I actually do not need the 3D view (just currently use it for showing the FPS). Can I deactivate the 3D view (programmatically in python)? Can I somehow also show the FPS in the MPR views?</p>
<p>Thanks for any help!</p>

---

## Post #2 by @lassoan (2019-01-27 13:26 UTC)

<aside class="quote no-group" data-username="mcfly3001" data-post="1" data-topic="5436">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcfly3001/48/6437_2.png" class="avatar"> mcfly3001:</div>
<blockquote>
<p>Can I deactivate the 3D view (programmatically in python)?</p>
</blockquote>
</aside>
<p>You can <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout">customize the view layout</a> or choose not to show certain nodes in certain views (e.g., to not show a model in 3D view, go to Models module and uncheck “View1” in Display/Visibility/View.</p>
<aside class="quote no-group" data-username="mcfly3001" data-post="1" data-topic="5436">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcfly3001/48/6437_2.png" class="avatar"> mcfly3001:</div>
<blockquote>
<p>Can I somehow also show the FPS in the MPR views?</p>
</blockquote>
</aside>
<p>You can show FPS in a slice viewer by typing this to the Python console:</p>
<pre><code>slicer.app.layoutManager().sliceWidget('Red').sliceView().fpsVisible=True
</code></pre>
<p>You can also use <em>Node modified statistics</em> module of <em>DebuggingTools</em> extension to analyze update rate of various nodes.</p>

---
