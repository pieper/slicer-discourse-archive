# CreateLabelVolumeFromVolume fails on Linux but not on Windows 10

**Topic ID**: 17890
**Date**: 2021-05-31
**URL**: https://discourse.slicer.org/t/createlabelvolumefromvolume-fails-on-linux-but-not-on-windows-10/17890

---

## Post #1 by @geoffkfleee (2021-05-31 22:54 UTC)

<p>I am currently running this function in my code in my Python script:</p>
<p><code>slicer.vtkSlicerVolumesLogic().CreateLabelVolumeFromVolume(slicer.mrmlScene, labelVolumeNode, loadedScalarNode)</code></p>
<p>On Windows 10 it properly works, and my code later uses the label volume to convert an NRRD into an OBJ with some segmentation settings.</p>
<p>However, in a Linux machine I’m tripping over the following error:</p>
<p><code>SetAndObserveColorToDisplayNode failed: invalid Colors module logic.</code></p>
<p>I’ve never seen this error in any discussion, bug tracker, or ticket that exists in Git or in this forum and so I was wondering if anyone had any ideas what might be causing this? <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Volumes/Logic/vtkSlicerVolumesLogic.cxx#L436" rel="noopener nofollow ugc">A look into the VTK library finds that this is an error triggered by a null pointer in the color information node</a>.</p>
<p>Any pointers?</p>
<p>Cheers.</p>

---

## Post #2 by @lassoan (2021-05-31 23:03 UTC)

<blockquote>
<p>SetAndObserveColorToDisplayNode failed: invalid Colors module logic.</p>
</blockquote>
<p>You get this error because you instantiate new module logics. Instead, you need to use the existing, properly initialized module logic. For example: <code>colorLogic = slicer.modules.colors.logic()</code> .</p>
<blockquote>
<p>WriteData: removing old version of file /root/output/52591e24-6ccd-4ae5-afd9-b689d1375291/4_ISOCENTER_VERIFICATION.nrrd</p>
</blockquote>
<p>This is because you don’t have write access to that file. It is either because you don’t have write access to that folder or something locks that particular file. On linux a common issue was that sharing a single slicer instance between multiple users could result in having a read-only temporary folder. You can set the temporary folder path manually to fix this, or use the latest Slicer Preview Release, which automatically requests a new temporary folder from the operating system if the current folder is read-only.</p>

---

## Post #3 by @geoffkfleee (2021-06-01 00:39 UTC)

<p>Your advice was exactly what was needed.</p>
<ul>
<li>
<p>Using the existing, properly initialized modules instead of instantiating my own removed the Colors module error.</p>
</li>
<li>
<p>Either using the newest Slicer version or enforcing write-access on folders will remove the warning that there’s an old version of a file when there is none.</p>
</li>
</ul>
<p>Thanks! I’ll leave this post up in case anyone else faces a similar issue.</p>

---

## Post #4 by @lassoan (2021-07-22 11:44 UTC)

<p>A post was split to a new topic: <a href="/t/what-are-the-underlying-methods-used-in-segment-editor/18871">What are the underlying methods used in Segment Editor?</a></p>

---
