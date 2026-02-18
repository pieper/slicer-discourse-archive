# Connecting NDI aurora tracking system to 3D slicer

**Topic ID**: 34226
**Date**: 2024-02-09
**URL**: https://discourse.slicer.org/t/connecting-ndi-aurora-tracking-system-to-3d-slicer/34226

---

## Post #1 by @angelinabarsoum (2024-02-09 14:57 UTC)

<p>Hi!</p>
<p>I have been trying to do some research online to find out how to connect the NDI aurora EM tracking system into 3D slicer to show a live feed of the sensors but I haven’t had much luck. I have downloaded the Plus tool kit but I am also not sure how to import the data into there. I am relatively new to both the NDI software and 3D slicer I just need help getting started.</p>
<p>If anyone has any experience with this and can provide a good explanation on how to do this step by step it would be greatly appreciated!</p>

---

## Post #2 by @Sam_Horvath (2024-02-09 16:07 UTC)

<p>So, on the Slicer side you will likely need the SlicerOpenIGTLink  and SlicerIGT extensions, this will allow you to connect to a running PLUS server that is connected to the NDI tracker.</p>
<p>There is an excellent set of tutorials on the SlicerIGT website: <a href="https://www.slicerigt.org/wp/user-tutorial/" class="inline-onebox">User tutorial | SlicerIGT</a></p>
<p>The U-03 tutorial covers the hardware connection basics.</p>

---
