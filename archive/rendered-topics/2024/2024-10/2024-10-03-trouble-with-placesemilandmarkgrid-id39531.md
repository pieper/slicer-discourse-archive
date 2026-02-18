# Trouble with PlaceSemilandmarkGrid

**Topic ID**: 39531
**Date**: 2024-10-03
**URL**: https://discourse.slicer.org/t/trouble-with-placesemilandmarkgrid/39531

---

## Post #1 by @Sumouria (2024-10-03 20:30 UTC)

<p>Hi everybody! I’m sorting out how to place surface semilandmarks on some inner ear endocasts, in order to be able to patch a batch of them (I have 29 specimens, so I need to be able to patch rather than place each specimen individually). I was troubleshooting something with the CreateSemiLMPatches module when I saw a mention of a new(?) module, PlaceSemilandmarkGrid, which seems much more intuitive and useful for my purposes than needing to create triangles everywhere.</p>
<p>However, I’m having difficulty actually getting the grids to place onto the mesh properly. A grid placed where there’s no other structures near it works fine, but I need to capture the edges of the structure, not just the middle, and grids placed towards the edges keep snapping onto the other structures nearby.</p>
<p>I know that with the CreateSemiLMPatches module, there was an option to adjust the projection distance to prevent the patch from projecting onto other structures, but I don’t see any way to modify any of the functions for PlaceSemilandmarkGrid beyond just inverting the grid and changing the sampling density within the grid.</p>
<p>Any help would be much appreciated!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e44edfb66fae663d01c443be7bdb29da7e6d13fc.png" data-download-href="/uploads/short-url/wzHQGuVMZ1Bo5E9itbilFzw6IgY.png?dl=1" title="Screenshot 2024-10-03 143228" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e44edfb66fae663d01c443be7bdb29da7e6d13fc_2_690x442.png" alt="Screenshot 2024-10-03 143228" data-base62-sha1="wzHQGuVMZ1Bo5E9itbilFzw6IgY" width="690" height="442" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e44edfb66fae663d01c443be7bdb29da7e6d13fc_2_690x442.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e44edfb66fae663d01c443be7bdb29da7e6d13fc_2_1035x663.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e44edfb66fae663d01c443be7bdb29da7e6d13fc.png 2x" data-dominant-color="AFAF56"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-10-03 143228</span><span class="informations">1186×761 303 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-10-03 21:09 UTC)

<p>Thanks for testing the <code>PlaceLandmarkGrid</code> functionality. This is still in development, and make sure you are using the preview version of Slicer to make sure you are using the latest version.</p>
<p>From your screenshot it doesn’t appear that the grid points were affected from the outline being stretched, so I wouldn’t worry about that.</p>
<p>However, if that’s a concern, you can nudge the corner points (grid outline points) just a bit to bring the outline back on the surface.</p>

---
