# Control Slicer using Surface Dial controller

**Topic ID**: 362
**Date**: 2017-05-23
**URL**: https://discourse.slicer.org/t/control-slicer-using-surface-dial-controller/362

---

## Post #1 by @lassoan (2017-05-23 13:35 UTC)

<p>In case you were wondering if you can use <a href="https://www.microsoft.com/en-us/store/d/Surface-Dial/925R551SKTGN">Surface Dial</a> to control Slicer - yes, you can. See 1-minute demo here:</p>
<div class="lazyYT" data-youtube-id="wbIhZoKNgTg" data-youtube-title="Controlling 3D Slicer using Surface Dial" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>No change in 3D Slicer is necessary. Scrolling through slices, zooming in/out, traversing through the undo/redo stack of Segment Editor work out-of-the-box. You can configure additional tools by specifying application-specific keyboard shortcuts.</p>
<p>Feel free to post here if you have questions, suggestions, or has any experience to share.</p>

---

## Post #2 by @lassoan (2017-05-23 13:35 UTC)

<p>How to configure additional tools: click Windows icon, enter “Wheel Settings”, click “Add an app” in in App Tools section, select “SlicerApp-real.exe”, and click “Add a tool”. Examples for adding tools for Segment Editor (see <a href="http://slicer.readthedocs.io/en/latest/user_guide/module_segmenteditor.html">complete list of Segment Editor keyboard shortcuts</a>):</p>
<p>Segment select:</p>
<ul>
<li>Custom tool name: Segment Select</li>
<li>Rotate right: None + W</li>
<li>Rotate left: None + Q</li>
<li>Click shortcut: None + Space (space switches between the last two effects in the latest nightly version, it’s useful to toggle between paint/erase; scissors/none; …)</li>
</ul>
<p>Brush size:</p>
<ul>
<li>Custom tool name: Brush Size</li>
<li>Rotate right: Ctrl + +</li>
<li>Rotate left: Ctrl + -</li>
<li>Click shortcut: None + Space</li>
</ul>

---
