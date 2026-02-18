# Linear transform not appearing anymore as a driver in IGT Volume Reslicer Driver

**Topic ID**: 45497
**Date**: 2025-12-15
**URL**: https://discourse.slicer.org/t/linear-transform-not-appearing-anymore-as-a-driver-in-igt-volume-reslicer-driver/45497

---

## Post #1 by @spichardo (2025-12-15 17:45 UTC)

<p>Hi,</p>
<p>I got this new issue in r5.10.0 of 3DSlicer and SlicerIGT (Revision: <a href="https://github.com/SlicerIGT/SlicerIGT/commit/71e2153" rel="noopener nofollow ugc">71e2153</a>).</p>
<p>I create a new linear transformation to be used in the IGT Volume Reslicer Driver, but the linear transform does not appear in the list of drivers. See screenshot</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52a3b9ea24ac054521c8cf2e57e83d9282193d34.png" data-download-href="/uploads/short-url/bN3VVQN4t1UxDw7UZqH9fXTF4S8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52a3b9ea24ac054521c8cf2e57e83d9282193d34_2_690x455.png" alt="image" data-base62-sha1="bN3VVQN4t1UxDw7UZqH9fXTF4S8" width="690" height="455" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52a3b9ea24ac054521c8cf2e57e83d9282193d34_2_690x455.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52a3b9ea24ac054521c8cf2e57e83d9282193d34_2_1035x682.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52a3b9ea24ac054521c8cf2e57e83d9282193d34.png 2x" data-dominant-color="D4CDC9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1052×694 58.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I do this in r5.8.1, the linear transform appears as expected:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/819d2c1db9f2811b521ea4121b660c8ff1d5a12f.png" data-download-href="/uploads/short-url/iuCkHjxvnR9K4qoxZo9bSm7OifB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/819d2c1db9f2811b521ea4121b660c8ff1d5a12f_2_690x463.png" alt="image" data-base62-sha1="iuCkHjxvnR9K4qoxZo9bSm7OifB" width="690" height="463" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/819d2c1db9f2811b521ea4121b660c8ff1d5a12f_2_690x463.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/819d2c1db9f2811b521ea4121b660c8ff1d5a12f_2_1035x694.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/819d2c1db9f2811b521ea4121b660c8ff1d5a12f.png 2x" data-dominant-color="D9CFCD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1048×704 67.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If I save the scene in r5.8.1 and then I load it in r5.10.0, the Volume Reslicer Driver shows the linear transform in the list of drivers.</p>
<p>I noticed the Linear Transform widget changed a little compared to r5.8.1. So not sure if I’m missing to do something extra. Overall, the linear transformation seems to be working as expected if, for example, applied to a 3D model such as the IGT’s Needle model.</p>
<p>Tested in MacOS 15.7.2,  iMacPro 2017 Intel x64.</p>
<p>Is this a bug that is preventing to show the linear transform in the  Volume Reslicer Driver? Or do I need to do something else in r.5.10.0 of 3DSlicer to make a new linear transform to appear in the list of drivers?</p>
<p>Thanks for any help,</p>
<p>Sam</p>

---

## Post #2 by @lassoan (2025-12-16 05:35 UTC)

<p>Good point. The Transforms module was updated to create <code>vtkMRMLTransformNode</code> on right-click, which node selectors in several SlicerIGT modules did not accept. I’ve updated SlicerIGT now to no longer user <code>vtkMRMLLinearTransformNode</code> anymore, which should fix the issue.</p>

---
