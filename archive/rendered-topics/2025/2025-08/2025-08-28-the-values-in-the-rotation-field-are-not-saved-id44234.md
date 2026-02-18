# The values in the rotation field are not saved

**Topic ID**: 44234
**Date**: 2025-08-28
**URL**: https://discourse.slicer.org/t/the-values-in-the-rotation-field-are-not-saved/44234

---

## Post #1 by @Konstantin (2025-08-28 15:01 UTC)

<p>Hello everyone. I have a task - to record the displacement of fragments in all planes when they move. I use the transforms module. But I encountered the following problem: all values ​​in the “rotation” field are reset to zero as soon as I click somewhere. This problem does not arise with the “translation”: all values ​​in this field are saved. How can I make the values ​​in the “ratation” field be saved (like in video guides)?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1fa645d208a6f39e9e3d9fd5b7236f9331463276.png" data-download-href="/uploads/short-url/4vZ2qZ4eEQrOeOFgRqsa1L99f2m.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1fa645d208a6f39e9e3d9fd5b7236f9331463276_2_690x361.png" alt="2" data-base62-sha1="4vZ2qZ4eEQrOeOFgRqsa1L99f2m" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1fa645d208a6f39e9e3d9fd5b7236f9331463276_2_690x361.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1fa645d208a6f39e9e3d9fd5b7236f9331463276_2_1035x541.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1fa645d208a6f39e9e3d9fd5b7236f9331463276_2_1380x722.png 2x" data-dominant-color="C3C2DE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1910×1002 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05dc9d46a280f8fe2eed499e1d525670709fd272.png" data-download-href="/uploads/short-url/PR3bIMCoh95bdH6espC2ydpd86.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05dc9d46a280f8fe2eed499e1d525670709fd272_2_690x368.png" alt="1" data-base62-sha1="PR3bIMCoh95bdH6espC2ydpd86" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05dc9d46a280f8fe2eed499e1d525670709fd272_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05dc9d46a280f8fe2eed499e1d525670709fd272_2_1035x552.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05dc9d46a280f8fe2eed499e1d525670709fd272_2_1380x736.png 2x" data-dominant-color="C4C3DE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1910×1019 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2025-08-28 15:09 UTC)

<p>That’s normal and expected.  The rotation sliders don’t uniquely define the transform so they are applied incrementally.</p>

---

## Post #3 by @Konstantin (2025-08-28 15:35 UTC)

<p>There is an example in the video instruction on YouTube where they are saved.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67ff9675bc6ee7746c8e6c3ccfa5b12d83ebeec5.jpeg" data-download-href="/uploads/short-url/eQ0LXUFvTab9FMfhRQJNX6YZ6T3.jpeg?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67ff9675bc6ee7746c8e6c3ccfa5b12d83ebeec5_2_690x388.jpeg" alt="3" data-base62-sha1="eQ0LXUFvTab9FMfhRQJNX6YZ6T3" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67ff9675bc6ee7746c8e6c3ccfa5b12d83ebeec5_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67ff9675bc6ee7746c8e6c3ccfa5b12d83ebeec5_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/67ff9675bc6ee7746c8e6c3ccfa5b12d83ebeec5_2_1380x776.jpeg 2x" data-dominant-color="57575F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1920×1080 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2025-08-28 15:48 UTC)

<p>That’s an older version of Slicer.</p>
<p>The behavior has be clarified <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#:~:text=Note%253A%2520Linear%2520transform,familiar%2520with%2520it.">as described here</a>:</p>
<ul>
<li>Note: Linear transform edit sliders only show relative translation and rotation because a transformation can be achieved using many different series of transforms. To make this clear to users, only one transform slider can be non-zero at a time (all previously modified sliders are reset to 0 when a slider is moved). The only exception is translation sliders in “translate first” mode (i.e., when translation in global/local coordinate system button is not depressed): in this case there is a only one way how a specific translation can be achieved, therefore transform sliders are not reset to 0. An rotating dial widget would be a more appropriate visual representation of the behavior than sliders, but slider is chosen because it is a standard widget and users are already familiar with it.</li>
</ul>

---

## Post #5 by @Konstantin (2025-08-28 16:11 UTC)

<p>Thanks for the detailed answer. As far as I know, the widget does not show the displacement values ​​in degrees (as, for example, it happens in Autodesk Netfabb).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/676c3e771bc6a288e81270b9cc069d4cbaf47cdf.png" data-download-href="/uploads/short-url/eKV5ErIAJWAhoeVXruAWbhFVjxJ.png?dl=1" title="4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/676c3e771bc6a288e81270b9cc069d4cbaf47cdf_2_690x316.png" alt="4" data-base62-sha1="eKV5ErIAJWAhoeVXruAWbhFVjxJ" width="690" height="316" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/676c3e771bc6a288e81270b9cc069d4cbaf47cdf_2_690x316.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/676c3e771bc6a288e81270b9cc069d4cbaf47cdf_2_1035x474.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/676c3e771bc6a288e81270b9cc069d4cbaf47cdf_2_1380x632.png 2x" data-dominant-color="BEBDD0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4</span><span class="informations">1916×879 293 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a776665598105f30eac7de349fd7cb439d16681.png" data-download-href="/uploads/short-url/jKVHEYrxGWvF5x07kJ8GpnqQhIR.png?dl=1" title="5" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a776665598105f30eac7de349fd7cb439d16681_2_690x308.png" alt="5" data-base62-sha1="jKVHEYrxGWvF5x07kJ8GpnqQhIR" width="690" height="308" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a776665598105f30eac7de349fd7cb439d16681_2_690x308.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a776665598105f30eac7de349fd7cb439d16681_2_1035x462.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a776665598105f30eac7de349fd7cb439d16681_2_1380x616.png 2x" data-dominant-color="EEE9E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">5</span><span class="informations">1877×839 99.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @cpinter (2025-08-29 10:25 UTC)

<p>If you really want to get the angles for a single linear transform, you can use this python snippet</p>
<pre><code class="lang-auto">import numpy as np

def rotationMatrixToEulerZYX(R):
    if R[2,0] &lt; 1:
        if R[2,0] &gt; -1:
            pitch = np.arcsin(-R[2,0])
            roll = np.arctan2(R[2,1], R[2,2])
            yaw = np.arctan2(R[1,0], R[0,0])
        else:
            # R[2,0] = -1
            pitch = np.pi / 2
            roll = -np.arctan2(-R[1,2], R[1,1])
            yaw = 0
    else:
        # R[2,0] = +1
        pitch = -np.pi / 2
        roll = np.arctan2(-R[1,2], R[1,1])
        yaw = 0
    return np.degrees([roll, pitch, yaw])

m = slicer.util.arrayFromTransformMatrix(tn)

tn = getNode('Transform')
rotationMatrixToEulerZYX(m)
</code></pre>
<p>The output is an array with the angles, e.g. <code>array([10., 20., 30.])</code></p>

---

## Post #7 by @Konstantin (2025-08-29 16:08 UTC)

<p>Thank you very much.</p>

---

## Post #8 by @lassoan (2025-08-29 17:38 UTC)

<p>If you want to avoid Python scripting, you can also use <a href="https://github.com/PerkLab/SlicerSandbox?tab=readme-ov-file#characterize-transform-matrix">Characterize transform matrix</a> module (in Sandbox extension). It decomposes the transformation into a few rotations and other operations and provides a detailed description. Decompositions are always arbitrary (there are infinite ways a transform can be put together from elementary operations), but it might happen to be suitable for what you want to achieve.</p>

---

## Post #9 by @Konstantin (2025-08-30 05:44 UTC)

<h3><a name="p-128047-thank-you-it-is-very-useful-extension-1" class="anchor" href="#p-128047-thank-you-it-is-very-useful-extension-1" aria-label="Heading link"></a>Thank you. It is very useful extension.</h3>

---
