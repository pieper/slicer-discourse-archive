# Error while attempting to extract Network Properties

**Topic ID**: 37755
**Date**: 2024-08-07
**URL**: https://discourse.slicer.org/t/error-while-attempting-to-extract-network-properties/37755

---

## Post #1 by @THartman (2024-08-07 17:52 UTC)

<p>I’m working on batch processing several vessel networks to extract the network properties tables, but I am getting the following error on all of the vessels in my dataset.  Does anyone have any information on what exactly this means?  Here’s the error I’m getting:</p>
<p>[VTK] Error: can’t reconstruct new profile.</p>
<p>And here are the two lines of code that seem to be causing the error:</p>
<p>networkPropertiesTableNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLTableNode”, “Network_Table_Label_” + str(i + 1))<br>
extractLogic.addNetworkProperties(inputSurfacePolyData, networkPropertiesTableNode)</p>

---

## Post #2 by @chir.set (2024-08-08 06:08 UTC)

<aside class="quote no-group" data-username="THartman" data-post="1" data-topic="37755">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e47c2d/48.png" class="avatar"> THartman:</div>
<blockquote>
<p>extractLogic.addNetworkProperties(inputSurfacePolyData, networkPropertiesTableNode)</p>
</blockquote>
</aside>
<p>Is ‘inputSurfacePolyData’ the result of ‘extractLogic.extractNetwork()’?</p>

---

## Post #3 by @THartman (2024-08-08 10:15 UTC)

<p>It is!  I tried making it the segmentation instead and that yielded the same results.</p>

---
