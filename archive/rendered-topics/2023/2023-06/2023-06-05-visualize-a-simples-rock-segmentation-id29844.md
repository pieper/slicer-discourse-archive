---
topic_id: 29844
title: "Visualize A Simples Rock Segmentation"
date: 2023-06-05
url: https://discourse.slicer.org/t/29844
---

# Visualize a Simples Rock Segmentation

**Topic ID**: 29844
**Date**: 2023-06-05
**URL**: https://discourse.slicer.org/t/visualize-a-simples-rock-segmentation/29844

---

## Post #1 by @edwin (2023-06-05 13:27 UTC)

<p>I work with CT images from rocks. I perform a segmentation in a CT volume then I have a 3d Numpy array with 3 labels (1,2,3) this numpy array is np.unit8. Then I transform this numpy array to ndrr format with this code?:</p>
<pre><code class="lang-auto">filename = 'post_process_fabrics_seg.nrrd'
# Write to a NRRD file
nrrd.write(filename, arr_seg)
</code></pre>
<p>I read the file as a volume using a 3D slicer. But I need to see the 3D volume label by label I only can visualize with 2d View. I apply some of the presets it seems that it only works for medical data.<br>
Here is what I see:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55dee1e1e25212a68f4e8884ace9984dc6620efd.png" data-download-href="/uploads/short-url/cfE6I1xOYS6F3nTZe710SlmOH6J.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55dee1e1e25212a68f4e8884ace9984dc6620efd.png" alt="image" data-base62-sha1="cfE6I1xOYS6F3nTZe710SlmOH6J" width="690" height="448" data-dominant-color="544735"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1407×915 60.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Can you please point me to what I must do to visualize the volume label by label, please</p>
<p>Best.</p>

---

## Post #2 by @lassoan (2023-06-05 13:28 UTC)

<p>You can load the volume as segmentation if you choose “Description” → “Segmentation” in the “Add data” window. You can also rename the file to <code>post_process_fabrics.seg.nrrd</code> to load it as segmentation by default.</p>

---

## Post #3 by @edwin (2023-06-05 14:12 UTC)

<p>Thanks a lot, <a class="mention" href="/u/lassoan">@lassoan</a>  I apply what you said and now have this, still can view the 3d volume, I am really new to 3D slicer:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa1a659516f2a24901d10dcbe3879d05f3a679c1.png" data-download-href="/uploads/short-url/ogNIWptfgWPkopN5WAvikgqUcQp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa1a659516f2a24901d10dcbe3879d05f3a679c1_2_690x352.png" alt="image" data-base62-sha1="ogNIWptfgWPkopN5WAvikgqUcQp" width="690" height="352" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa1a659516f2a24901d10dcbe3879d05f3a679c1_2_690x352.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa1a659516f2a24901d10dcbe3879d05f3a679c1_2_1035x528.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa1a659516f2a24901d10dcbe3879d05f3a679c1_2_1380x704.png 2x" data-dominant-color="645860"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×980 69.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Are there more steps to visualize the 3d volume or it suppose to appear when I load the segmented data?</p>
<p>Best,</p>

---

## Post #4 by @edwin (2023-06-05 14:59 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>  finally I get how to visualize the segmentation:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e82b398fa93be7db5e77c1f2b9ee994577b8869a.png" data-download-href="/uploads/short-url/x7RnGeufauHR36N8Wc8vhh0K7q2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e82b398fa93be7db5e77c1f2b9ee994577b8869a_2_690x363.png" alt="image" data-base62-sha1="x7RnGeufauHR36N8Wc8vhh0K7q2" width="690" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e82b398fa93be7db5e77c1f2b9ee994577b8869a_2_690x363.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e82b398fa93be7db5e77c1f2b9ee994577b8869a_2_1035x544.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e82b398fa93be7db5e77c1f2b9ee994577b8869a_2_1380x726.png 2x" data-dominant-color="555D6E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1906×1004 277 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>For segments that have a small number of voxels it is ok we can see it as you see above.</p>
<p>For segments that have more voxels, it has a lot of voxels in the wall of the image and it does not permit to see inside the image. I try opacity but is there another way to do this? like to empathize more with the voxels that are the interior of the image?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a7eb9e4eca849228362439aadd367767f7b0834.jpeg" data-download-href="/uploads/short-url/m2J2tErf9P8tM7sqg9vKwGyTITa.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a7eb9e4eca849228362439aadd367767f7b0834_2_682x500.jpeg" alt="image" data-base62-sha1="m2J2tErf9P8tM7sqg9vKwGyTITa" width="682" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a7eb9e4eca849228362439aadd367767f7b0834_2_682x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a7eb9e4eca849228362439aadd367767f7b0834_2_1023x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/a/9a7eb9e4eca849228362439aadd367767f7b0834_2_1364x1000.jpeg 2x" data-dominant-color="7E7F83"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1367×1002 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Best,</p>

---

## Post #5 by @lassoan (2023-06-05 15:33 UTC)

<p>You can try volume rendering for visualization. For that, you can either load the image as labelmap volume (as you did originally) or export the segmentation to binary labelmap. You can then drag-and-drop the labelmap from the tree in Data module to a 3D view to show volume rendering. It is easier to dynamically crop a volume rendering and opacity adjusts the volumetric density (and not the opacity of the boundary surface as for segmentation visualization).</p>

---
