# Sequence of many vtk files

**Topic ID**: 9788
**Date**: 2020-01-13
**URL**: https://discourse.slicer.org/t/sequence-of-many-vtk-files/9788

---

## Post #1 by @jeonb (2020-01-13 01:01 UTC)

<p>Hi 3D Slicer community members,</p>
<p>I am new to 3D slicer, and any advice will be appreciated.<br>
I am trying to play animation of many vtk files (*.vtu), made from ParaView. Each VTU file contains x/y/z nodes, grids (structured grids) and density data.<br>
I loaded them in Sequence extension and tried to run animation from Sequence browser but I found that all of them overlapped in the space, not showing any difference b/w frames.</p>
<p>In ParaView, when I load many VTK files, they are arranged along time steps of file names, and animation is relatively automatic. In 3DSlicer, will I need extra pre-steps or VTK is not recommended for making animations? Any comments are appreciated.</p>
<p>Thanks,</p>
<p>Byoungseon</p>

---

## Post #2 by @lassoan (2020-01-13 05:06 UTC)

<p>After you loaded all the files into the scene, you can create a sequence from them by following these steps: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences#Creating_sequences_from_a_set_of_nodes">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/Sequences#Creating_sequences_from_a_set_of_nodes</a></p>

---

## Post #3 by @jeonb (2020-01-14 03:37 UTC)

<p>Dear Andras,</p>
<p>Thanks for the instruction. I followed those steps but still they don’t show animation - just overlapped grids or cells. Following images are the steps I used - they match with the instruction, I guess:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/872616b7384a21feee4c4d549eca0cf9b8ee1130.png" data-download-href="/uploads/short-url/jhA3V75Xnra9G0fDs3TeE4HqDhm.png?dl=1" title="sample01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/872616b7384a21feee4c4d549eca0cf9b8ee1130_2_690x77.png" alt="sample01" data-base62-sha1="jhA3V75Xnra9G0fDs3TeE4HqDhm" width="690" height="77" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/872616b7384a21feee4c4d549eca0cf9b8ee1130_2_690x77.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/872616b7384a21feee4c4d549eca0cf9b8ee1130_2_1035x115.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/872616b7384a21feee4c4d549eca0cf9b8ee1130.png 2x" data-dominant-color="CACBDC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sample01</span><span class="informations">1174×132 13.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e40348847c1519693a48ba6eba78170b8f05bca8.png" data-download-href="/uploads/short-url/wx5TEwzaQ4r91SRKp25CDUPZZfa.png?dl=1" title="sample02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e40348847c1519693a48ba6eba78170b8f05bca8_2_690x145.png" alt="sample02" data-base62-sha1="wx5TEwzaQ4r91SRKp25CDUPZZfa" width="690" height="145" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e40348847c1519693a48ba6eba78170b8f05bca8_2_690x145.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e40348847c1519693a48ba6eba78170b8f05bca8_2_1035x217.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e40348847c1519693a48ba6eba78170b8f05bca8.png 2x" data-dominant-color="CDCDE0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sample02</span><span class="informations">1159×245 30.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffa4ec80fdb084d2c41087c936750e6c4588831e.png" data-download-href="/uploads/short-url/Atx6mEUflSpFGkPCGCUfKSaacuq.png?dl=1" title="sample03" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffa4ec80fdb084d2c41087c936750e6c4588831e_2_690x162.png" alt="sample03" data-base62-sha1="Atx6mEUflSpFGkPCGCUfKSaacuq" width="690" height="162" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffa4ec80fdb084d2c41087c936750e6c4588831e_2_690x162.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/ffa4ec80fdb084d2c41087c936750e6c4588831e_2_1035x243.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ffa4ec80fdb084d2c41087c936750e6c4588831e.png 2x" data-dominant-color="D0CFDE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">sample03</span><span class="informations">1171×275 36 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Other details are:</p>
<ul>
<li>They are VTU files (produced from ParaView), and loaded as model. If I try to load as volume, it is not recognized.</li>
<li>From Models module, all models are visible, and this might be why all grids are overlapped - to make animations, sequence may have to make each one visible while others are not visible. Such changes are done automatically or need to be done manually? If manual, how I can adjust each sequence? I tried to record from ModelDisplay in Proxy node of SequenceBrowser, but it is not clear to me how each frame (or snapshot) can be adjusted.</li>
<li>The OS is ubuntu 16 and I am using 3DSlicer 4.10.2.<br>
Any comments are appreciated.</li>
</ul>
<p>Best regards,</p>
<p>Byoungseon</p>

---
