# View controller module doesnt check whether the orientation exist or not

**Topic ID**: 21820
**Date**: 2022-02-06
**URL**: https://discourse.slicer.org/t/view-controller-module-doesnt-check-whether-the-orientation-exist-or-not/21820

---

## Post #1 by @keri (2022-02-06 11:39 UTC)

<p>Hi,</p>
<p><a href="https://github.com/Slicer/Slicer/blob/4d756f0ef57832d654df7a8dc1a8b10e38b8fba9/Modules/Loadable/ViewControllers/qSlicerViewControllersModule.cxx#L238-L246" rel="noopener nofollow ugc">qSlicerViewControllersModule::writeDefaultSliceViewSettings</a> function tries to determine the patient position based on <code>Axial</code> slice orientation preset. But in custom applications it is possible to redefine presets (to <code>XYZ</code> for example) and in this case an error is shown in the log.</p>
<p>I propose to modify that part to preliminary check whether the orientation preset exist or not:</p>
<pre><code class="lang-cpp">if (defaultViewNode-&gt;HasSliceOrientationPreset("Axial")){
  // do the check and write settings
}
</code></pre>
<p>May I create a PR?</p>

---
