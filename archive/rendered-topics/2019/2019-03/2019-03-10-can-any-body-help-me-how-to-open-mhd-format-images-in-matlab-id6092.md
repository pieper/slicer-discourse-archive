# can any body help me how to open .mhd format images in matlab with .raw header

**Topic ID**: 6092
**Date**: 2019-03-10
**URL**: https://discourse.slicer.org/t/can-any-body-help-me-how-to-open-mhd-format-images-in-matlab-with-raw-header/6092

---

## Post #1 by @hira (2019-03-10 18:33 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @jamesobutler (2019-03-10 18:47 UTC)

<p>There is a Matlab toolbox called <a href="https://www.mathworks.com/matlabcentral/fileexchange/29344-read-medical-data-3d" rel="nofollow noopener">Read Medical 3D Data</a> that can help reading mha/mhd+raw files.</p>
<p>There is also a <a href="https://github.com/PlusToolkit/PlusMatlabUtils/blob/master/MatlabMetafileIO/mha_read_volume.m" rel="nofollow noopener">reader</a> within the PlusMatlabUtils repo within the PlusToolkit github organization.</p>

---

## Post #3 by @cpinter (2019-03-10 19:30 UTC)

<p>The fact that you wrote to this forum suggests that you want to do at least some of your workflow in Slicer. Can I ask what is that?</p>
<p>Also you can use the Matlab Bridge extension to do some of your processing in Matlab from Slicer:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/MatlabBridge</a></p>

---
