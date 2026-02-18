# Slices are displayed non-orthogonally when using Controller Transform

**Topic ID**: 36070
**Date**: 2024-05-10
**URL**: https://discourse.slicer.org/t/slices-are-displayed-non-orthogonally-when-using-controller-transform/36070

---

## Post #1 by @Beatriz_2 (2024-05-10 15:54 UTC)

<p>Operating System: Windows<br>
Slicer Version: Slicer 5.6.1<br>
Headset: Meta Quest 2<br>
Problem: Sometimes slices are displayed non-orthogonally when using VirtualReality.RightController or VirtualReality.LeftController as well as SlicerIGT and SlicerVirtualReality extensions.</p>
<p>Hi,</p>
<p>I’ve experimented the SlicerVirtualReality and SlicerIGT extensions to change the slice I observe in Virtual Reality, by using the controllers. I have followed these steps:</p>
<ol>
<li>I checked the option “controllers transform” from the SlicerVirtualReality extension and used the Volume Reslice Driver from the SlicerIGT extensions.</li>
<li>I used the Volume Reslice Driver from the SlicerIGT extension and then selected VirtualReality.RightController as the driver and “axial” as a mode.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/598a1396cca14578ad7e13bd39cae7552ee6b60c.png" alt="SlicerIGT" data-base62-sha1="cM6jZuG1EBE7QKhQ3uQ52mfOZTC" width="546" height="498"></li>
</ol>
<p>Result: Sometimes I observed a slice’s rotation, as shown in the image. It also happened for the other planes - coronal and sagittal - and I don’t know why. In this cases, the anatomical structures visualized in the slice doens’t match with the model (in terms of localization).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7415f1debeba13f5f02b2de7b5fc844de6bdac8.png" alt="3D Slicer view" data-base62-sha1="zhjZztTSVU5xyDhgwRvyyDey05y" width="686" height="427"></p>
<p>I checked the Transform called VirtualReality.RightController and I observed that the “Transformed Matrix” indexs constantly changes, even when the controllers and the headset are static.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9cf30473b63c2ebfd2e966cbd3376cc1182465f.png" data-download-href="/uploads/short-url/zDUMXnO1xeKckWDwFjchIfeAxiv.png?dl=1" title="Right Controller Transform" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9cf30473b63c2ebfd2e966cbd3376cc1182465f_2_317x500.png" alt="Right Controller Transform" data-base62-sha1="zDUMXnO1xeKckWDwFjchIfeAxiv" width="317" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9cf30473b63c2ebfd2e966cbd3376cc1182465f_2_317x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f9cf30473b63c2ebfd2e966cbd3376cc1182465f_2_475x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9cf30473b63c2ebfd2e966cbd3376cc1182465f.png 2x" data-dominant-color="F4F6F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Right Controller Transform</span><span class="informations">539×848 25.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Can someone help me overcome this issue?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2024-05-10 19:28 UTC)

<p>Can you share the scene that shows such a misalignment? Do you see misalignment only in rotation-constrained modes (axial, sagittal, coronal)?</p>

---

## Post #3 by @Beatriz_2 (2024-05-15 12:32 UTC)

<p>Thanks for the fast response!</p>
<p>I can´t share the scene since when I try to share it here, appears a message saying only .jpeg and other image extensions are allowed. Anyways when I saved it, it doesn’t show the misalignment between the model and the correspondent slice. In this case, after I save the scene, the model and the slice are aligned as they should, but, as you can see from the picture, in the original Slicer scene where the Meta Quest are connected to, the problem still happens:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d706ab86fad1703530690b9c7f9f1aa08dfd2835.jpeg" data-download-href="/uploads/short-url/uGcWGNcyFTmkWaEB6JRX1C9lDrD.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d706ab86fad1703530690b9c7f9f1aa08dfd2835_2_690x297.jpeg" alt="image" data-base62-sha1="uGcWGNcyFTmkWaEB6JRX1C9lDrD" width="690" height="297" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d706ab86fad1703530690b9c7f9f1aa08dfd2835_2_690x297.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d706ab86fad1703530690b9c7f9f1aa08dfd2835_2_1035x445.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d706ab86fad1703530690b9c7f9f1aa08dfd2835_2_1380x594.jpeg 2x" data-dominant-color="6F6E6F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1914×825 185 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I checked and the VirtualRealithy.RightController transform was the same in both files (the original one connected to Meta Quest 2 and the saved file).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc237026bed9ad906fdc749d4972f3617f95e6c4.png" data-download-href="/uploads/short-url/vpqY5Pzhj7XSkwc3yLvWKvYZ2y8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc237026bed9ad906fdc749d4972f3617f95e6c4.png" alt="image" data-base62-sha1="vpqY5Pzhj7XSkwc3yLvWKvYZ2y8" width="323" height="500" data-dominant-color="F1F3F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">435×672 16.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Regarding the second question, I only tested for 3 modes, but they all showed the same problem (which only happens sometimes).</p>
<p>Thanks for the help!</p>

---
