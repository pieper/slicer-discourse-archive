# Why slice-view can not be updated/changed with one-by-one image dimension with a small pixel-spacing?

**Topic ID**: 23223
**Date**: 2022-05-01
**URL**: https://discourse.slicer.org/t/why-slice-view-can-not-be-updated-changed-with-one-by-one-image-dimension-with-a-small-pixel-spacing/23223

---

## Post #1 by @aiden.zhu (2022-05-01 19:22 UTC)

<p>Operating system: windows<br>
Slicer version: 4.11.2210226<br>
Expected behavior: slice view updated one slice by one slice<br>
Actual behavior: only after two slices.</p>
<p>Hi all,<br>
First of all, while I increase the pixel-spacing by 1000, there is no such an issue. That is, say my original data’s pixel-spacing 0.763922um, then it is increased to 1000 times, 763.922um, while I set one-slice by one-slice, the slice-view gets updated well and correctly.</p>
<p>The issue is: with 0.763922um/pixel, the slice-view gets only updated every two-slices.<br>
My checking code through Python-Interactor is as follows after loading my data:</p>
<pre><code class="lang-auto">import numpy as np
import slicer
sliceNodeID = 'vtkMRMLSliceNodeRed'
DimsNumber = 100
sliceNode = slicer.mrmlScene.GetNodeByID(sliceNodeID)
lm = slicer.app.layoutManager()
sliceLogic = lm.sliceWidget(sliceNode.GetLayoutName()).sliceLogic()
sliceSpacing = sliceLogic.GetLowestVolumeSliceSpacing()
sliceOffsetResolution = sliceSpacing[0]
sliceBounds=np.zeros(6)
sliceLogic.GetLowestVolumeSliceBounds(sliceBounds)
sliceOffsetMin = sliceBounds[4]
sliceOffsetMax = sliceBounds[5]
</code></pre>
<p>so now I set <code>DimsNumber = 100</code></p>
<pre><code class="lang-auto">sliceLogic.SetSliceOffset(sliceOffsetMin+ (DimsNumber)*sliceOffsetResolution ) 
</code></pre>
<p>this will be working well to see updated slice-view of “Red”.</p>
<p>but then ==&gt; while DimsNumber = 100+1<br>
sliceLogic.SetSliceOffset(sliceOffsetMin+ (DimsNumber)*sliceOffsetResolution )<br>
the RED-slice-view gets NO updates (the position value of the red-view NO change either.)</p>
<p>Now then ==&gt; while <code>DimsNumber = 100+2</code></p>
<pre><code class="lang-auto">sliceLogic.SetSliceOffset(sliceOffsetMin+ (DimsNumber)*sliceOffsetResolution ) 
</code></pre>
<p>the slice-view gets changed/updated correctly.</p>
<p>So what’s the factor playing a role in this issue? Somewhere there is an extra processing like being-round?</p>

---

## Post #2 by @aiden.zhu (2022-05-01 22:28 UTC)

<p>PS: I just finished testing inside the night-version 3D-Slicer-5.0.1, there is the same issue as described above.</p>

---

## Post #3 by @pieper (2022-05-01 22:47 UTC)

<p>I don’t know why for sure in this case, but it’s not uncommon to have trouble working with small scans and multiplying the spacings so that the numbers are around 1 gives better numerical stability than using very small numbers that may lead to floating point errors.</p>

---

## Post #4 by @aiden.zhu (2022-05-01 23:20 UTC)

<p>Thanks a lot for your reply there Steve. I believe with pretty much high possibility the issue is being caused by keeping significant numbers of small float values. I hope the Slicer-Group may take some effort to dig it out.</p>

---

## Post #5 by @pieper (2022-05-01 23:33 UTC)

<p>Yes, it’s come up before and there’s been some work at generalizing the infrastructure but still there are some places where it’s safest to just rescale the data and just pretend it says um when the interface says mm.  I’m sure this will come up more as people try microscopy workflows and maybe we’ll find some resources to work on a more general solution.</p>

---

## Post #6 by @aiden.zhu (2022-05-02 13:44 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a><br>
Hi Steve,  one potentially easiest way to correct this issue may be like:<br>
Displaying the value there with 5 or 6 decimals for the position in each sliding-bar of slice-views there.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a22c56ddf3fdab12731ba1efec16d524e879fba.png" alt="image" data-base62-sha1="60Ky8ZSMO86nuj2TnSD8lzgISCK" width="287" height="75"></p>
<p>Right now default it is only 4 decimals in mm (covering only 0.1um), so while we take default units in mm, after showing 5 decimals, it will directly show 0.00001mm to directly cover 0.01um</p>

---

## Post #7 by @pieper (2022-05-02 16:34 UTC)

<p>That might be the issue, but there could be others too.</p>
<p>This is some support for setting the units to something other than mm, but I would be careful because I’m not sure it gets a lot of use.  Maybe others can comment.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Units" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Units</a></p>

---

## Post #8 by @aiden.zhu (2022-05-02 20:05 UTC)

<p>Thanks a lot, I will try based on the link you provided there to see how it goes. Based on some previous experience on units settings, something does not work smooth there. anyway I will try more.</p>

---

## Post #9 by @lassoan (2022-05-02 22:13 UTC)

<p>By adjusting Units settings in Application settings you can modify the number of displayed digits (just modify the <code>Precision</code> value of <code>Length</code>).</p>
<p>However, this increased display precision might not solve all issues and you may want to rescale your data for better numerical stability. If you rescale your data then you may switch units for correct display of physical values. However, units support is incomplete (see missing tasks <a href="https://github.com/Slicer/Slicer/issues/5040">here</a>), so depending on what operations you need to do, it may be confusing that sometimes you still see mm instead of the length unit that you have set.</p>

---
