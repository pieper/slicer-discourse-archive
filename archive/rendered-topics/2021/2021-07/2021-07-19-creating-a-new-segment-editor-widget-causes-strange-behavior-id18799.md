# Creating a new segment editor widget causes strange behavior in segmentation settings

**Topic ID**: 18799
**Date**: 2021-07-19
**URL**: https://discourse.slicer.org/t/creating-a-new-segment-editor-widget-causes-strange-behavior-in-segmentation-settings/18799

---

## Post #1 by @giovform (2021-07-19 14:47 UTC)

<p>Creating a new segmentation and applying works as expected (it remains visible), but if you type in the python console:</p>
<pre><code class="lang-auto">slicer.modules.segmenteditor.createNewWidgetRepresentation()
</code></pre>
<p>then, creating a new segmentation and applying, will cause the “Slice fill” and “Slice outline” to be set to zero (settings in the Segmentation module advanced area).</p>
<p>So, the steps to reproduce are (using Slicer latest stable release 4.11.20210226 revision 29738 built 2021-03-01):</p>
<ol>
<li>Load any 2D image</li>
<li>Go to the Data module, right click the image node and select “Segment this…”</li>
<li>Add a segment, click the Threshold effect and apply. It will work as expected</li>
<li>Go to the Data module and delete the segmentation node</li>
<li>In the python console type: slicer.modules.segmenteditor.createNewWidgetRepresentation()</li>
<li>Right click the image node and select “Segment this…”</li>
<li>Add a segment, click the Threshold effect and apply. The segmentation will be invisible. You can then check the segmentation advanced settings to notice that “Slice fill” and “Slice outline” are set to zero</li>
</ol>

---

## Post #2 by @lassoan (2021-07-19 14:58 UTC)

<p><code>createNewWidgetRepresentation</code> is only to be used by the application. A module or script should not ever need to duplicate the GUI of a module. You can simply instantiate a qMRMLSegmentEditorWidget and add it to your module (or just keep it hidden if you don’t need to show a GUI, as it is done in most of the segmentation examples in the script repository).</p>

---
