# SlicerIMSTK build question

**Topic ID**: 30286
**Date**: 2023-06-28
**URL**: https://discourse.slicer.org/t/slicerimstk-build-question/30286

---

## Post #1 by @ffr (2023-06-28 19:52 UTC)

<p>May I ask if there is a tutorial for SlicerIMSTK? I am able to build IMSTK with CMake and successfully ran the examples with the 3DS haptic device but not sure how to build or install the SlicerIMSTK.<br>
The GitHub page says the standalone case provides IMSTK functionalities to the Slicer community through the extension manager but I can’t find it or install it from the extension manager. Building it with CMake also fails.<br>
Thank you very much for your help!</p>
<p><a href="https://github.com/KitwareMedical/SlicerIMSTK" rel="noopener nofollow ugc">GitHub - KitwareMedical/SlicerIMSTK: Extension for 3D slicer that enables user to prototype real-time multi-modal surgical simulation scenarios by leveraging iMSTK</a></p>

---

## Post #2 by @Sam_Horvath (2023-06-29 16:16 UTC)

<p>Him the SlicerIMSTK extension is based on an older version of IMSTK and requires some updates.  If you could open an issue on the GitHub repo with your build errors that would be helpful.</p>

---

## Post #3 by @ffr (2023-06-29 16:20 UTC)

<p>Thank you for the reply. Shall I build the SlicerIMSTK the same way as I build IMSTK?</p>

---

## Post #4 by @Sam_Horvath (2023-06-29 16:25 UTC)

<p>SlicerIMSTK should be built like other Slicer extensions, which requires to first do a local build of Slicer:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#build-an-extension" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/extensions.html#build-an-extension</a></p>

---
