# Segment statistics fail in Test with no window mode

**Topic ID**: 12976
**Date**: 2020-08-13
**URL**: https://discourse.slicer.org/t/segment-statistics-fail-in-test-with-no-window-mode/12976

---

## Post #1 by @Alex_Vergara (2020-08-13 15:06 UTC)

<p>I have a case where I have several segmentations and I need to test each of them in no window mode (test mode)</p>
<p>The normal way to do this is to disable all of them and the enable just the one I am testing, this is done with</p>
<pre><code class="lang-auto">        displayNode = segmentationNode.GetDisplayNode()
        if displayNode is not None:
            displayNode.SetVisibility(1)
</code></pre>
<p>However without the qSlicerMainWindow the above code never gets executed as there are no display nodes in the first place. So the question is how to enable/disable the segmentation node without using the display nodes?</p>
<p>The problem is that when the segmentation is called by SegmenationStatistic module it is never enabled and it treats it as it were no segmentation at all.</p>
<p>This is related with the <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=Opendose" rel="nofollow noopener">failing tests here</a></p>

---

## Post #2 by @lassoan (2020-08-13 18:17 UTC)

<p>You can add display nodes to the scene, regardless of having a main window or not. The problem should be somewhere else.</p>
<p>Add a breakpoint or trace print in <code>slicer.util.lookupTopLevelWidget </code>to get a stack trace. Then we’ll know what needs the main window, and see if it is really necessary.</p>

---
