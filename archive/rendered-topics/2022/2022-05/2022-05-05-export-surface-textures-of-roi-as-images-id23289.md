---
topic_id: 23289
title: "Export Surface Textures Of Roi As Images"
date: 2022-05-05
url: https://discourse.slicer.org/t/23289
---

# Export surface textures of ROI as images

**Topic ID**: 23289
**Date**: 2022-05-05
**URL**: https://discourse.slicer.org/t/export-surface-textures-of-roi-as-images/23289

---

## Post #1 by @Atomsk (2022-05-05 16:32 UTC)

<p>Hello,</p>
<p>my dataset is a stack of TIFF images which I imported into 3D slicer. I then enabled Volume Rendering of this dataset and toggled “Shade” off because I just want to browse through the dataset in the 3D viewport; I don’t need a volume rendering.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://ibb.co/PGFKqZz">
  <header class="source">
      <img src="https://simgbb.com/images/favicon.png" class="site-icon" width="300" height="300">

      <a href="https://ibb.co/PGFKqZz" target="_blank" rel="noopener nofollow ugc">ImgBB</a>
  </header>

  <article class="onebox-body">
    <img src="https://i.ibb.co/PGFKqZz/Screenshot-2022-05-05-113532.png" class="thumbnail onebox-avatar" width="180" height="180">

<h3><a href="https://ibb.co/PGFKqZz" target="_blank" rel="noopener nofollow ugc">Screenshot-2022-05-05-113532</a></h3>

  <p>Image Screenshot-2022-05-05-113532 hosted in ImgBB</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>(Let me know if there are better ways to achieve the same).</p>
<p>Because the dataset is skewed and has excessive white parts, I needed to adjust the ROI into a parallelogram. Now I am able to browse through the dataset from all 6 sides by shrinking/extending the ROI.</p>
<p>I would now like to export the current surface texture of the ROI. Basically, 6 images for all 6 planes of the current ROI. With this 6 images I can visualize a box of my current view in another 3D program.</p>
<p>To be clear, the important part is that thanks to 3D Slicer, I am able to browse through the dataset “at an angle.” If I onle browsed through the dataset in normal X, Y, Z, there is lots of blank area: <a href="https://ibb.co/Gtmn7dm" class="inline-onebox" rel="noopener nofollow ugc">Screenshot-2022-05-05-114200 — ImgBB</a></p>
<p>The crucial part for me is now getting this adjusted box into another 3D program. Either by exporting 6 images and then creating the parallelogram by hand or (if 3D Slicer supports that) exporting the current ROI as a mesh with correct textures attached to it.</p>

---

## Post #2 by @lassoan (2022-05-05 22:21 UTC)

<aside class="quote no-group" data-username="Atomsk" data-post="1" data-topic="23289">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/87869e/48.png" class="avatar"> Atomsk:</div>
<blockquote>
<p>I just want to browse through the dataset in the 3D viewport; I don’t need a volume rendering.</p>
</blockquote>
</aside>
<p>Have you tried to use slice views? That’s how usually we explore 3D volumes. Click on the eye icon in the slice view controller to show the slice in the 3D view.</p>
<p>You can rotate all the slices at arbitrary angles by <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-views">enabling slice intersections and using Ctrl+Alt+Left-click-and-drag</a>, or enabling interactive slice intersections:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3ca5836fb6631d6696c25b02914274730d5036f.png" alt="image" data-base62-sha1="udAgArZz7FnMJLnrIlGfsDDHzSn" width="501" height="496"></p>
<aside class="quote no-group" data-username="Atomsk" data-post="1" data-topic="23289">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/87869e/48.png" class="avatar"> Atomsk:</div>
<blockquote>
<p>The crucial part for me is now getting this adjusted box into another 3D program. Either by exporting 6 images and then creating the parallelogram by hand or (if 3D Slicer supports that) exporting the current ROI as a mesh with correct textures attached to it.</p>
</blockquote>
</aside>
<p>If you want to export a rectangular prism then you can simply crop your volume to that using a ROI (using <code>Crop volume</code> module) and then use the first/last slice of the volume along each axis.</p>
<p>If you want to extract arbitrarily oriented slices then you probably need to write a short Python code snippet.</p>
<p>You can position a slice view then get the image from that get the slice views as images, as it is shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#extract-randomly-oriented-slabs-of-given-shape-from-a-volume">here</a>.</p>
<p>Alternatively, you can create a polygonal mesh that stores voxel values as point data. You can create the polydata using vtkCubeSource, subdivide it to the desired resolution, add it to a model node, and set the point data using <code>Probe volume with model</code> module.</p>

---

## Post #3 by @Atomsk (2022-05-06 13:26 UTC)

<p>Hello Andras,</p>
<p>thanks for your reply and the hint about rotating slices in arbitrary angles. However, sometimes I do prefer to view the data as this “box” of planes like in my first screenshot. This way one can look “behind” the corner of the planes.</p>
<p>What I also like from the “volume rendering” (showing a box of the dataset) is that I do not have to worry about the dimension of the plane and therefore, the texture. Consider this screenshot where I rotated the problematic plane in the slice view:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://ibb.co/LnmxVRs">
  <header class="source">
      <img src="https://simgbb.com/images/favicon.png" class="site-icon" width="300" height="300">

      <a href="https://ibb.co/LnmxVRs" target="_blank" rel="noopener nofollow ugc">ImgBB</a>
  </header>

  <article class="onebox-body">
    <img src="https://i.ibb.co/LnmxVRs/Screenshot-2022-05-06-151546.png" class="thumbnail onebox-avatar" width="180" height="180">

<h3><a href="https://ibb.co/LnmxVRs" target="_blank" rel="noopener nofollow ugc">Screenshot-2022-05-06-151546</a></h3>

  <p>Image Screenshot-2022-05-06-151546 hosted in ImgBB</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Even if I am able to extract the current texture to an image, I would need to make up for the missing part in the bottom which might get a little bit complicated. Given that with the volume rendering, Slicer already constructs a suitable parallelogram mesh and interpolates the textures beautifully, is there no way to access this data in some way or another?</p>
<p>Unfortunately I’m not familiar with VTK to know its internals, but if there is some kind of API to this objects I would be able to work my way to it in Python.</p>
<p>As far as I understand, the script that you mention (“Extract randomly oriented slabs of given shape from a volume”) would give me the image data of each slice as if I was scrolling through it (at an angle). I would prefer to have the “parallelogram box textures,” but in any case I tried it out and so far only got a black image. Is this the correct usage?</p>
<pre><code class="lang-auto">volume = getNode('001') # my dataset
slice = randomSlices(
    volume,
    1, # I only want the current slice
    [1200, 800] # dimensions of the image that I later want to save
)
</code></pre>

---
