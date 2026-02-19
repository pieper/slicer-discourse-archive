---
topic_id: 31775
title: "Volume Rendering Gives Solid Box Despite Working Xyz Views A"
date: 2023-09-18
url: https://discourse.slicer.org/t/31775
---

# Volume rendering gives solid box despite working XYZ views and adjusting preset/shift

**Topic ID**: 31775
**Date**: 2023-09-18
**URL**: https://discourse.slicer.org/t/volume-rendering-gives-solid-box-despite-working-xyz-views-and-adjusting-preset-shift/31775

---

## Post #1 by @shika (2023-09-18 18:16 UTC)

<p>Hello there,<br>
I am a new user of Slicer but I have read through the wiki and other related help forums. I have been having issues with rendering from a stack of images, specifically using the SlicerMorph <a href="https://github.com/SlicerMorph/S_2020/blob/master/Day_1/ImageStacks/ImageStacks.md" rel="noopener nofollow ugc">ImageStacks</a> utility to convert a stack of png files (which were converted from full color jpg files and then scaled down to 25%)  to a volume. The data is found <a href="https://www.mediafire.com/file/bvvb1xxuayux4wi/brain-25-scale0000.nrrd/file" rel="noopener nofollow ugc">here</a>. The views of individual dimensions (X, Y, Z) operate as expected (though the interpolation could be smoother):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd4a9a0a9ae3276407de30249d5505e0e2dae759.png" data-download-href="/uploads/short-url/ti5Ik4vMgHtDSLJP4UoTDnVE32x.png?dl=1" title="Screenshot 2023-09-18 014537" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd4a9a0a9ae3276407de30249d5505e0e2dae759_2_661x500.png" alt="Screenshot 2023-09-18 014537" data-base62-sha1="ti5Ik4vMgHtDSLJP4UoTDnVE32x" width="661" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd4a9a0a9ae3276407de30249d5505e0e2dae759_2_661x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd4a9a0a9ae3276407de30249d5505e0e2dae759_2_991x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd4a9a0a9ae3276407de30249d5505e0e2dae759_2_1322x1000.png 2x" data-dominant-color="4A4A56"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-09-18 014537</span><span class="informations">1930×1458 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
However whenever I try to render a volume, I get a solid color block no matter which preset or shift I try.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36a1bf4d548dd7a740fe11cc0d3f23e03bebe7c9.png" data-download-href="/uploads/short-url/7NikaBCrULtASQnIpAr4SbN8yCt.png?dl=1" title="Screenshot 2023-09-18 014821" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36a1bf4d548dd7a740fe11cc0d3f23e03bebe7c9.png" alt="Screenshot 2023-09-18 014821" data-base62-sha1="7NikaBCrULtASQnIpAr4SbN8yCt" width="683" height="500" data-dominant-color="775371"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-09-18 014821</span><span class="informations">966×707 12.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Using crop to reveal the interior of the volume reveals no “tunnels” or anything of the sort; it is still just a solid block:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0a950a15c47453a469045115c877e19303f2450.png" data-download-href="/uploads/short-url/rumqELqcjl5UTSfSkOHfJX2ZdPG.png?dl=1" title="Screenshot 2023-09-18 015018" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0a950a15c47453a469045115c877e19303f2450.png" alt="Screenshot 2023-09-18 015018" data-base62-sha1="rumqELqcjl5UTSfSkOHfJX2ZdPG" width="683" height="500" data-dominant-color="9678A3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-09-18 015018</span><span class="informations">967×707 20.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Is there a way to fix this? I have spent many hours trying to troubleshoot this myself and it has been quite fruitless. I would greatly appreciate any help.</p>

---

## Post #2 by @muratmaga (2023-09-18 18:50 UTC)

<p>You got couple issues going on:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e00c8576d6e758f20e2d2d764b7f1f13e0ed929.png" data-download-href="/uploads/short-url/4hq032LqDSzjUYx83mhvYEhjzYt.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e00c8576d6e758f20e2d2d764b7f1f13e0ed929_2_460x500.png" alt="image" data-base62-sha1="4hq032LqDSzjUYx83mhvYEhjzYt" width="460" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e00c8576d6e758f20e2d2d764b7f1f13e0ed929_2_460x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e00c8576d6e758f20e2d2d764b7f1f13e0ed929_2_690x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e00c8576d6e758f20e2d2d764b7f1f13e0ed929_2_920x1000.png 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">963×1045 53.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>First your dataset has 3076 px in X dimension. This is probably exceeding your gpu’s max3Dtexture dimension (it did in my intel GPU, which has a cap of 2048px). So you get an empty box. If you resample to a lower resolution. It renders</p>
<p>Your dataset is not aligned (there are shifts in object position from one slice to the next) and there is huge difference in resolution (50 times less data in Z slices). so it renders very poorly.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/da9148ddb68a75e8eb8d5991da71a397c907d1d8.jpeg" data-download-href="/uploads/short-url/vbxmhIGyrZUt7r2JXCPxVzjSRO8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da9148ddb68a75e8eb8d5991da71a397c907d1d8_2_690x371.jpeg" alt="image" data-base62-sha1="vbxmhIGyrZUt7r2JXCPxVzjSRO8" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da9148ddb68a75e8eb8d5991da71a397c907d1d8_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da9148ddb68a75e8eb8d5991da71a397c907d1d8_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/a/da9148ddb68a75e8eb8d5991da71a397c907d1d8_2_1380x742.jpeg 2x" data-dominant-color="9595A1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1035 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This looks like one of the brain atlases, i don’t think it is meant to be rendered in 3D (not with labels embeded in the image). Why are you trying to render this in 3D?</p>

---

## Post #3 by @lassoan (2023-09-18 19:14 UTC)

<p>I would recommend converting this to a segmentation. It can then be nicely visualized in both 2D and 3D.</p>
<p>The simplest would be to load the the image as a segmentation by selecting “Segmentation” in the “Description” column when you load the nrrd file. You can then go to Segmentations module and click “Show 3D” to see in 3D:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cde5ac31fcbaa894777db35cac16843572fd677e.jpeg" data-download-href="/uploads/short-url/tnrX4yGnDzsH9HgIqiplAsoXA9o.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cde5ac31fcbaa894777db35cac16843572fd677e_2_690x365.jpeg" alt="image" data-base62-sha1="tnrX4yGnDzsH9HgIqiplAsoXA9o" width="690" height="365" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cde5ac31fcbaa894777db35cac16843572fd677e_2_690x365.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cde5ac31fcbaa894777db35cac16843572fd677e_2_1035x547.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cde5ac31fcbaa894777db35cac16843572fd677e_2_1380x730.jpeg 2x" data-dominant-color="4C4A4D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1016 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The problems are:</p>
<ul>
<li>Problem 1: Slices are not aligned (the position within the slice seems random)</li>
<li>Problem 2: The segments don’t have a discrete gray level (at the boundary the values are interpolated and there are labels within the segments)</li>
</ul>
<p>You could fix <strong>problem 2</strong> by segmenting the image using Segment Editor, for example using Grow from seeds effect:</p>
<ul>
<li>Specify seeds:</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bc515af2e0b813e6b001916fade3456da36cded.png" data-download-href="/uploads/short-url/8wKqdcdKFpeVlkm66Hw24be9WZ7.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bc515af2e0b813e6b001916fade3456da36cded_2_690x460.png" alt="image" data-base62-sha1="8wKqdcdKFpeVlkm66Hw24be9WZ7" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bc515af2e0b813e6b001916fade3456da36cded_2_690x460.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bc515af2e0b813e6b001916fade3456da36cded_2_1035x690.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3bc515af2e0b813e6b001916fade3456da36cded_2_1380x920.png 2x" data-dominant-color="464646"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2221×1481 436 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ul>
<li>Apply the region growing and click Show 3D:</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd42692e1026a06f0fc3b0a29095b096d38d5600.jpeg" data-download-href="/uploads/short-url/A8r5fkqvVmT5dBIhZ2HgMFB5Jdu.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd42692e1026a06f0fc3b0a29095b096d38d5600_2_690x362.jpeg" alt="image" data-base62-sha1="A8r5fkqvVmT5dBIhZ2HgMFB5Jdu" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd42692e1026a06f0fc3b0a29095b096d38d5600_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd42692e1026a06f0fc3b0a29095b096d38d5600_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd42692e1026a06f0fc3b0a29095b096d38d5600_2_1380x724.jpeg 2x" data-dominant-color="4F4D4F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1010 136 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, for <strong>problem 1</strong> (misaligned slices) Slicer does not have a good solution. You can find image stack alignment tools in ImageJ that you can use and then import the results into Slicer. Or, you can ask the authors of the atlas to provide you the atlas as a 3D image that contains the slices already aligned.</p>

---

## Post #4 by @shika (2023-09-18 23:38 UTC)

<p>Thank you for your assistance and advice. It is very helpful!</p>

---

## Post #5 by @pieper (2023-09-19 21:44 UTC)

<p>To my eye this data is not misaligned, it’s inconsistently segmented, since individual segments grow and shrink between slices rather than being consistently shifted one way or another.  So probably you won’t get a good 3D reconstruction using this data, but you may be able to use it as a guide for doing a fresh fully 3D segmentation of a volumetric scan of the same species.</p>

---
