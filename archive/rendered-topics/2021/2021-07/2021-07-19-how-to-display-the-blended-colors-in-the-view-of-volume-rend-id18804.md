---
topic_id: 18804
title: "How To Display The Blended Colors In The View Of Volume Rend"
date: 2021-07-19
url: https://discourse.slicer.org/t/18804
---

# How to display the blended colors in the view of 'volume rendering'?

**Topic ID**: 18804
**Date**: 2021-07-19
**URL**: https://discourse.slicer.org/t/how-to-display-the-blended-colors-in-the-view-of-volume-rendering/18804

---

## Post #1 by @CharlesChen (2021-07-19 20:11 UTC)

<p>Hello,<br>
I am using the ‘volume rendering’ module of Slicer to visualize the image data of a cell composed of red and green channels.<br>
The rendering method I chose is: ‘VTK GPU Ray Casting’<br>
However, as shown in Figure 1, the intersection of the red channel and the green channel in the view window cannot be displayed as a blended yellow.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/5/c575b874876560971064507cff7f819c6b9055b4.png" alt="Figure1" data-base62-sha1="saOh9Ou6YHSDEffHzFrln0EnCNS" width="322" height="241"><br>
But it seems that only when I turn on the ‘display clipping box’ under the ‘ROI’ tab, the blended color can be displayed. As shown in Figure 2, the intersection of the red channel and the green channel is displayed in yellow.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5bfb6b5c154374fb50dc222e49c7f0fe9c1ba3c.png" alt="Figure2" data-base62-sha1="z3ZIWRHImtUkAhJCPtawnd1510M" width="281" height="194"></p>
<p>At the same time, however, even in the view window in the desktop mode, the blended color can be displayed(as shown above), but the blended color is still can not be displayed in the 3D view created in the VR mode(SlicerVirtualReality). As shown in Figure 3.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd1220ba6164f67b9aa4c7e5d006a47520070f4f.png" alt="Figure3" data-base62-sha1="tg8IEkkPYYPmEkf6xhYxZDenKeH" width="273" height="186"></p>
<p>On the other hand, when I change the rendering method to ‘VTK Multi-Volume’, no matter whether I turn on the ‘display clipping box’ or not, the blended colors will not be displayed.</p>
<p>Therefore, in a situation similar to the above, how to display the blended colors of different color channels in the view of ‘volume rendering’(both in desktop mode and the VR mode) correctly?</p>
<p>Appreciate any help! Thank you so much in advance!</p>

---

## Post #2 by @CharlesChen (2021-07-22 16:27 UTC)

<blockquote>
<p>Therefore, in a situation similar to the above, how to display the blended colors of different color channels in the view of ‘volume rendering’(both in desktop mode and the VR mode) correctly?</p>
</blockquote>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Hello Dr. Andras Lasso, Could you please give me some suggestions on the above issues?<br>
Thank you so much!</p>

---

## Post #3 by @lassoan (2021-07-22 21:32 UTC)

<p>If these are two independent image acquisitions then I would recommend to render them as separate volumes: extract each component using “Vector to scalar volume” module, using “Single component extraction” conversion method; then render each volume separately. Make sure to choose “VTK multi-volume” rendering (otherwise one volume will be always in front of another volume, instead of being blended in 3D).</p>

---

## Post #4 by @CharlesChen (2021-07-22 23:30 UTC)

<p>Hello Dr. Andras Lasso,<br>
Thank you so much for your reply!</p>
<blockquote>
<p>If these are two independent image acquisitions</p>
</blockquote>
<p>Yes, the red and green channels shown in the figures above are two independent <strong>16-bit</strong> TIFF images(named ‘cell-new-red.tif’ and ‘cell-new-green.tif’), as shown in Figure1 and 2(I got them from FIJI).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/5/156ad2adbdf08b54e3f978dcb1b545ead8e10cee.jpeg" data-download-href="/uploads/short-url/33sTqCOaLylfgxKrio5tqgr91XU.jpeg?dl=1" title="16 bit red channel" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/156ad2adbdf08b54e3f978dcb1b545ead8e10cee_2_474x375.jpeg" alt="16 bit red channel" data-base62-sha1="33sTqCOaLylfgxKrio5tqgr91XU" width="474" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/156ad2adbdf08b54e3f978dcb1b545ead8e10cee_2_474x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/156ad2adbdf08b54e3f978dcb1b545ead8e10cee_2_711x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/156ad2adbdf08b54e3f978dcb1b545ead8e10cee_2_948x750.jpeg 2x" data-dominant-color="6F6D6C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">16 bit red channel</span><span class="informations">996×787 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d1efa29fa21d5d5197ff9e4bf77a644f4f95f0b.png" data-download-href="/uploads/short-url/49CdkrbydTRWvOPfB2DTSPksNhF.png?dl=1" title="16 bit Green Channel" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d1efa29fa21d5d5197ff9e4bf77a644f4f95f0b_2_517x346.png" alt="16 bit Green Channel" data-base62-sha1="49CdkrbydTRWvOPfB2DTSPksNhF" width="517" height="346" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d1efa29fa21d5d5197ff9e4bf77a644f4f95f0b_2_517x346.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d1efa29fa21d5d5197ff9e4bf77a644f4f95f0b_2_775x519.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d1efa29fa21d5d5197ff9e4bf77a644f4f95f0b_2_1034x692.png 2x" data-dominant-color="706E6D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">16 bit Green Channel</span><span class="informations">1061×711 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After I followed the method you suggested, in the view of ‘Volume rendering’, the blended colors of the two channels still cannot be displayed.</p>
<p>I’m not sure if the steps I performed are correct, could you please check them? if there are errors, please point out:</p>
<ol>
<li>First, according to your guide, in order to get the ‘Input vector volume’, I used FIJI to convert the image type of these two TIFF images <strong>from 16 bit to RGB color type</strong>, since from the 'Documentation/4.10/Modules/VectorToScalarVolume ’ I learned that:</li>
</ol>
<blockquote>
<p>The “Vector to scalar volume” module is useful for converting RGB (vector) volumes to one component (scalar) grayscale volumes.</p>
</blockquote>
<ol start="2">
<li>
<p>I saved the converted red and green channel images (both are RGB colors) as: ‘cell-new-red-RGB.tif’ and ‘cell-new-red-RGB.tif’</p>
</li>
<li>
<p>In the ‘Vector to scalar volume’ module, I used the two files obtained from the 2nd step as ‘Input Vector Volume’, set the ‘Output Scalar Volume’ to ‘Scalar Volume RED’ and ‘Scalar Volume GREEN’, and I chose the ‘Single component extraction’ method as you said. As shown in Figure 3 and Figure 4 below.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/706e687eeddc06e104d8ea02b583534edf2f4116.png" alt="Scalar Volume RED" data-base62-sha1="g2C1yDs9FOUqR31I4gOzt61SWbA" width="409" height="184"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7ab849a1813369196b030aaacfd258c72614646.png" alt="Scalar Volume GREEN" data-base62-sha1="uLU8ajBmlqVjcnAg0gNAuFDUrIy" width="411" height="192"></p>
</li>
<li>
<p>In the ‘Volume rendering’ module, I loaded the ‘Scalar Volume RED’ and ‘Scalar Volume GREEN’ obtained from the 3rd step into the view (I open both eye icons in front of the ‘Volume’, and loaded them into the view), and set the rendering method to ‘VTK Multi-Volume’, as shown in Figure 5 and Figure 6 below.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2cc61ac8bcb1c606e56e07197768467206335f3a.jpeg" data-download-href="/uploads/short-url/6o5rE31Y3mZ7W4IoXROgKXw1DiG.jpeg?dl=1" title="volume rendering1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2cc61ac8bcb1c606e56e07197768467206335f3a_2_516x290.jpeg" alt="volume rendering1" data-base62-sha1="6o5rE31Y3mZ7W4IoXROgKXw1DiG" width="516" height="290" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2cc61ac8bcb1c606e56e07197768467206335f3a_2_516x290.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2cc61ac8bcb1c606e56e07197768467206335f3a_2_774x435.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2cc61ac8bcb1c606e56e07197768467206335f3a_2_1032x580.jpeg 2x" data-dominant-color="786C69"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volume rendering1</span><span class="informations">1181×663 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/4733aa69af58092a9e4206b160627d3ffda90637.png" data-download-href="/uploads/short-url/a9SANNzQyG9jmnwY2xA1HI9UNAH.png?dl=1" title="Volume rendering2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/4733aa69af58092a9e4206b160627d3ffda90637_2_517x277.png" alt="Volume rendering2" data-base62-sha1="a9SANNzQyG9jmnwY2xA1HI9UNAH" width="517" height="277" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/4733aa69af58092a9e4206b160627d3ffda90637_2_517x277.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/4733aa69af58092a9e4206b160627d3ffda90637_2_775x415.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/7/4733aa69af58092a9e4206b160627d3ffda90637_2_1034x554.png 2x" data-dominant-color="71776B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Volume rendering2</span><span class="informations">1164×625 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
</ol>
<p>As you can see, after performing the above steps, the blended colors of the two channels still cannot be displayed in the view.</p>
<p>Could you please point out which step is incorrect or what should I do?</p>
<p>Thank you very much!</p>

---

## Post #5 by @lassoan (2021-07-23 01:44 UTC)

<p>What Slicer displays looks correct. This is a 3D rendering, therefore if you have a piece of red blob in front of a green blob, you will only see the red blob if you make Scalar Opacity Mapping function ramp up to 1.0. Even if you make the opacity plateau at a lower level (e.g., 0.3), whatever is in front will have larger influence on the color.</p>
<p>Another thing that you may not expect that when you render multiple volumes independently then the colors are combined using additive averaging (similar to a spinning colorwheel - brightness of colors are not added), and not using additive averaging (like in fluorescent imaging when you sum the intensities of multiple light beams).</p>
<p>As a result, you will not see bright yellow if you use multi-volume rendering (1. the yellow may be occluded, 2. if you crop the images to make the mixed yellow visible, that the yellow will be relatively dark).</p>
<p>If you want to see bright yellows then the best is to display the image as an RGBA stack. You can enable direct RGBA volume rendering as described here: <a href="https://discourse.slicer.org/t/merge-colored-images-and-show-them-as-1-volume/6472/6" class="inline-onebox">Merge colored images and show them as 1 volume - #6 by lassoan</a>.</p>
<p>If you only have RGB channels then you can generate an A (alpha = opacity) channel by averaging the RGB channels and generate an RGBA image by appending this A channel to the RGB image.</p>

---

## Post #6 by @CharlesChen (2021-07-23 01:52 UTC)

<p>Thank you for your kind and patient reply!<br>
I will try the method you mentioned.<br>
Thank you so much! <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #7 by @lassoan (2021-07-25 13:57 UTC)

<p>I’ve made an improvement in Slicer core that makes it much simpler to render color volumes. You don’t need any Python scripting anymore, you can simply load a color volume (with RGB or RGBA voxels) and enable volume rendering. Alpha channel is computed automatically as needed; independent components in the volume rendering properties is enabled/disabled automatically. This improvement will be available in the latest Slicer Preview Release that you download tomorrow or later.</p>

---

## Post #8 by @CharlesChen (2021-07-25 16:57 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="7" data-topic="18804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>latest Slicer</p>
</blockquote>
</aside>
<p>Hello Dr.Andras Lasso,<br>
Thank you very much for your reminder, I will try the latest version to verify it <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---

## Post #9 by @PieterTack (2022-02-09 13:03 UTC)

<p>Dear Dr. Andras Lasso,</p>
<p>Many thanks for your great assistance in this topic!<br>
I have a similar issue, where I want to display two separately acquired volumes, and display them on top of each other in order to identify overlapping points.<br>
Preferably I would do this with a true RGB representation (where the blue channel is empty, so only red and green, with overlapping voxels as shades of yellow)</p>
<p>I have tried several approaches:</p>
<ul>
<li>importing the two separate volumes and then visualising them in the volume renderer with VTK multi-volume. This does sort of indentifies the overlapping voxels, however the volume(s) itself becomes increasingly transparent and sometimes displays some strange mirroring/echoing effect. In other words, the volume is not really representative of the sample any more.</li>
<li>importing the volumes directly as a RGB volume. This gives me clear success in the slice windows, however in the volume renderer view the volume is invisible (even after activating its visibility). When selecting VTK GPU raycasting in this case does display something that looks like a volume, but it appears monocolored and as such also does not provide the info I’m looking for.</li>
</ul>
<p>Do you perhaps have any suggestions on how I could better obtain the volume renders of the two separate volumes, and the mixing/overlapping thereof? It would be of paramount importance! I’ve looked at different volume rendering softwares as well, but never have I come so close to an actual good result as with Slicer…</p>
<p>Many thanks in advance for your great help!</p>

---

## Post #10 by @lassoan (2022-02-09 23:16 UTC)

<p>In recent Slicer Preview Releases, RGB volume rendering is set up automatically - you just need to drag-and-drop the volume from the Data module to a 3D view and the full color image should be visible. However, the experimental multi-volume renderer has a number of limitations, so it may not be able to display RGB volumes.</p>
<p>Are your images acquired as RGB or you just apply a lookup table to the scalar values to make them colorful?</p>
<ul>
<li>If lookup table is used:, then you can apply that color table in Slicer and use multi-volume rendering.</li>
<li>If you actually acquired 3D RGB volumes (e.g., by cryosectioning): then you can merge them into a single volume (resample them using the same grid using Crop volumes module, and then <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#modify-voxels-in-a-volume">blend them into a single volume using numpy</a>)</li>
</ul>

---

## Post #11 by @PieterTack (2022-02-10 08:49 UTC)

<p>So the method I followed for the true RGB is indeed the second one you mention: I added the volumes into a single RGB volume using numpy, and then saved them as a tif file (using the python tifffile.imwrite functionality). Loading this in Slicer gives this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e569da4c06ac00277a204ed6b84ca118825f9cdc.png" data-download-href="/uploads/short-url/wJu80qROexUePe10X4XKfo3ZQFm.png?dl=1" title="afbeelding" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e569da4c06ac00277a204ed6b84ca118825f9cdc_2_517x291.png" alt="afbeelding" data-base62-sha1="wJu80qROexUePe10X4XKfo3ZQFm" width="517" height="291" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e569da4c06ac00277a204ed6b84ca118825f9cdc_2_517x291.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e569da4c06ac00277a204ed6b84ca118825f9cdc_2_775x436.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e569da4c06ac00277a204ed6b84ca118825f9cdc_2_1034x582.png 2x" data-dominant-color="9E989F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">afbeelding</span><span class="informations">1920×1080 423 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>As you see… a whole lot a bright yellow. Which surprises me, as if you look at the slice panels, the slices don’t show that much yellow. I understand this may be a projection thing, where the yellow voxels are simply ‘blocking’ the view of the other voxels? If so, is there a way to make them partly transparent?<br>
Not that this is using the GPU ray casting. If I toggle to the multi-volume the 3D rendering simply disappears (completely invisible <img src="https://emoji.discourse-cdn.com/twitter/person_shrugging.png?v=12" title=":person_shrugging:" class="emoji" alt=":person_shrugging:" loading="lazy" width="20" height="20"> ).</p>
<p>If I on the other hand just load the volumes separately I have this with GPU ray casting:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52e3d47e7c95b10ab673f12d02b6533bccdde5d0.jpeg" data-download-href="/uploads/short-url/bPhh7MBNdJXadPSwLg03n0mTbMs.jpeg?dl=1" title="afbeelding" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52e3d47e7c95b10ab673f12d02b6533bccdde5d0_2_517x291.jpeg" alt="afbeelding" data-base62-sha1="bPhh7MBNdJXadPSwLg03n0mTbMs" width="517" height="291" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52e3d47e7c95b10ab673f12d02b6533bccdde5d0_2_517x291.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52e3d47e7c95b10ab673f12d02b6533bccdde5d0_2_775x436.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/52e3d47e7c95b10ab673f12d02b6533bccdde5d0_2_1034x582.jpeg 2x" data-dominant-color="8D889A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">afbeelding</span><span class="informations">1920×1080 117 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
and this when switching on the multi-volume:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d809c02f84665d819075a1e30eabb59aa19ed78.png" data-download-href="/uploads/short-url/4cZofdpNFqN1SHNzQOoTT6OuZwk.png?dl=1" title="afbeelding" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d809c02f84665d819075a1e30eabb59aa19ed78_2_517x291.png" alt="afbeelding" data-base62-sha1="4cZofdpNFqN1SHNzQOoTT6OuZwk" width="517" height="291" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d809c02f84665d819075a1e30eabb59aa19ed78_2_517x291.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d809c02f84665d819075a1e30eabb59aa19ed78_2_775x436.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/1/1d809c02f84665d819075a1e30eabb59aa19ed78_2_1034x582.png 2x" data-dominant-color="928FA8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">afbeelding</span><span class="informations">1920×1080 338 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I think it is clear that the multivolume didn’t quite give the result I was hoping for <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"><br>
So if you have further suggestions/hints that would be great… I’m quite at a loss here. But then again, perhaps I’m just asking ‘too much’ in the sense that what I eventually want to see is perhaps not readily visible in any 3D rendered volume. Perhaps a better approach would be to actually group (with PCA or similar) the voxels based on their respective intensities of the red and green channel, and then display the cluster ids? Something to think on <img src="https://emoji.discourse-cdn.com/twitter/thinking.png?v=12" title=":thinking:" class="emoji" alt=":thinking:" loading="lazy" width="20" height="20"></p>

---

## Post #12 by @lassoan (2022-02-10 13:07 UTC)

<p>I this all looks very promising. You have multiple options to make this work and they just need a little tuning.</p>
<p>Is your acquisition true RGB or you just acquire a scalar volume and apply a lookup table to make it colordul?</p>

---

## Post #13 by @PieterTack (2022-02-11 09:41 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="12" data-topic="18804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Is your acquisition true RGB or you just acquire a scalar volume and apply a lookup table to make it colordul?</p>
</blockquote>
</aside>
<p>My acquisition is indeed a scalar volume (or indeed 2 volumes) to which I applied a lookup table (being the RGB colourisation) to make it colourful.</p>

---

## Post #14 by @lassoan (2022-02-11 19:50 UTC)

<p>In that case it is very easy: you can load the volumes separately and use “VTK multi-volume” renderer. You can adjust the opacity transfer function to make parts of the volume more or less transparent. You can set your lookup table in the color transfer function.</p>

---

## Post #15 by @PieterTack (2022-02-12 06:52 UTC)

<p>I was hoping for the same, but unfortunately changing the opacity doesn’t change much <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"> Perhaps I’m changing some wrong opacity somewhere?<br>
In each attempt I get something similar to the last image in my message from 2 days ago. It appears as if the multi-volume rendering in this case wrongfully adds certain voxels to average to zero, even though there should be signal present… Maybe because the surrounding voxels do contain (noise) data that I made invisible using the Volume Threshold values?</p>

---

## Post #16 by @lassoan (2022-02-12 13:54 UTC)

<p>Can you share a data set (the one with scalar values, not RGB) so that I can have a look? You can upload it to dropbox, onedrive, etc. and post the link here.</p>

---

## Post #17 by @PieterTack (2022-02-15 14:05 UTC)

<p>Hi Andras, I’m unfortunately not comfortable to share a link to the dataset online <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"> I tried to send you a mail a few days ago, but perhaps I sent it to wrong address. Can you think of a secure way I could send you alone a link? I see no private messaging option on this forum <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>

---

## Post #18 by @mikebind (2022-02-15 16:01 UTC)

<p>You can send a private message by clicking on the user’s photo/icon and clicking the “Message” button.</p>

---

## Post #19 by @PieterTack (2022-02-15 19:00 UTC)

<p>Yeah, that doesn’t show up anywhere <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7a179a6a2b260c57b7e0397a4708348a5881716.png" data-download-href="/uploads/short-url/qctkQ0uxVJ12E8GwXYfAcCsEgtg.png?dl=1" title="afbeelding" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7a179a6a2b260c57b7e0397a4708348a5881716_2_690x388.png" alt="afbeelding" data-base62-sha1="qctkQ0uxVJ12E8GwXYfAcCsEgtg" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7a179a6a2b260c57b7e0397a4708348a5881716_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7a179a6a2b260c57b7e0397a4708348a5881716_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b7a179a6a2b260c57b7e0397a4708348a5881716_2_1380x776.png 2x" data-dominant-color="F7F7F7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">afbeelding</span><span class="informations">1920×1080 227 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Perhaps I’m too new to have the rights to do it or something?</p>

---

## Post #20 by @mikebind (2022-02-15 19:24 UTC)

<p>I see, sorry about that; the button shows for me.  I would guess it’s an anti-spam feature that it takes some time or activity to get that right.</p>

---
