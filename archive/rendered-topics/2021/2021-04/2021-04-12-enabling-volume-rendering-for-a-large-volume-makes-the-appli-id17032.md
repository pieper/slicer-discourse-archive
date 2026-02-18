# Enabling volume rendering for a large volume makes the application crash

**Topic ID**: 17032
**Date**: 2021-04-12
**URL**: https://discourse.slicer.org/t/enabling-volume-rendering-for-a-large-volume-makes-the-application-crash/17032

---

## Post #1 by @evodevo (2021-04-12 01:13 UTC)

<p>Operating system: windows<br>
Slicer version:4.11.20200930<br>
Expected behavior: volume rendering<br>
Actual behavior: volume rendering freezes</p>
<p>I have datasets that are small (in dimensions) and whenever I ask slicer to do volume rendering, it produces a tiny volume in the middle of the 3d field. When I zoom in on the volume to move it, the program freezes.</p>

---

## Post #2 by @lassoan (2021-04-12 01:27 UTC)

<p>Can you take a screenshot of the Volume information section of Volumes module (to see dimensions, spacing, and scalar type of your volume)?</p>

---

## Post #3 by @evodevo (2021-04-12 01:54 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de9989353960e6a21d553fbeabf388cefb99b27f.png" data-download-href="/uploads/short-url/vLcWL5KHWpDoI5q7XjxOahVxD43.png?dl=1" title="screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de9989353960e6a21d553fbeabf388cefb99b27f_2_690x387.png" alt="screenshot" data-base62-sha1="vLcWL5KHWpDoI5q7XjxOahVxD43" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de9989353960e6a21d553fbeabf388cefb99b27f_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/e/de9989353960e6a21d553fbeabf388cefb99b27f_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de9989353960e6a21d553fbeabf388cefb99b27f.png 2x" data-dominant-color="B6B8D3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot</span><span class="informations">1366×768 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2021-04-12 02:04 UTC)

<p>Thank you. The volume rendering looks good. The image spacing is a bit too small (2 magnitudes smaller than usual), but should not cause application hang.</p>
<p>Do you use CPU or GPU volume rendering?<br>
Does the hang occur when you zoom in? Does the application crash after the hang?<br>
What graphics card do you have?</p>
<p>Please try if rendering the volume in multiple partitions (to ease the load on the GPU) solves the issue, by copy-pasting these lines to the Python console:</p>
<pre><code class="lang-python">threeDViewWidget = slicer.app.layoutManager().threeDWidget(0)
vrDisplayableManager = threeDViewWidget.threeDView().displayableManagerByClassName('vtkMRMLVolumeRenderingDisplayableManager')
vrMapper = vrDisplayableManager.GetVolumeMapper(getNode('skull'))
vrMapper.SetPartitions(1,1,2)
</code></pre>

---

## Post #5 by @evodevo (2021-04-12 02:35 UTC)

<p>Thank you lasson, for all your help.<br>
I use the gpu volume rendering. the hand occur right after i zoom in. yes it crashes after the hang<br>
my graphics card is amd radeon™ vega 3 400mhz, vram of 1009 mb and total memory of 3542 mb<br>
I tried inserting the code you sent, but i got an error message and the problem did not go away.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77e2cca78c3348035a91132dacd76d0941a78c72.png" data-download-href="/uploads/short-url/h6yJxvLNGlVQfl1cYf7nUmntrrQ.png?dl=1" title="screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77e2cca78c3348035a91132dacd76d0941a78c72_2_690x387.png" alt="screenshot" data-base62-sha1="h6yJxvLNGlVQfl1cYf7nUmntrrQ" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77e2cca78c3348035a91132dacd76d0941a78c72_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/7/77e2cca78c3348035a91132dacd76d0941a78c72_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77e2cca78c3348035a91132dacd76d0941a78c72.png 2x" data-dominant-color="C8C8DC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot</span><span class="informations">1366×768 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @muratmaga (2021-04-12 02:59 UTC)

<p>Try what <a class="mention" href="/u/lassoan">@lassoan</a> suggested with the latest stable it might work better. Also you have a very low end gpu. Even when works, performance is unlikely to be good.</p>

---

## Post #7 by @lassoan (2021-04-12 03:57 UTC)

<aside class="quote no-group" data-username="evodevo" data-post="5" data-topic="17032">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evodevo/48/10623_2.png" class="avatar"> evodevo:</div>
<blockquote>
<p>I use the gpu volume rendering. the hand occur right after i zoom in. yes it crashes after the hang</p>
</blockquote>
</aside>
<p>This indicates that you get a TDR error: the operating system shuts down applications that keep the graphics card busy for too long. This happens because the size of the volume is too large for your GPU to comfortably handle. There are several ways to work around this:</p>
<ul>
<li>Option A: Run the code snippet above to split the volume to smaller chunks (that way you have a better chance that the graphics card will not be unresponsive for too long) or increase TDR delay in the registry.</li>
<li>Option B: Crop and downsample your volume using Crop volume and volume render this smaller volume.</li>
<li>Option C: Increase TDR delay value in registry (see details <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/display/tdr-registry-keys">here</a>)</li>
<li>Option D: Use CPU volume rendering.</li>
<li>Option E: Upgrade your computer with a stronger graphics card.</li>
</ul>
<aside class="quote no-group" data-username="evodevo" data-post="5" data-topic="17032">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/evodevo/48/10623_2.png" class="avatar"> evodevo:</div>
<blockquote>
<p>I tried inserting the code you sent, but i got an error message and the problem did not go away.</p>
</blockquote>
</aside>
<p>You need to run the code after you enabled volume rendering.</p>

---
