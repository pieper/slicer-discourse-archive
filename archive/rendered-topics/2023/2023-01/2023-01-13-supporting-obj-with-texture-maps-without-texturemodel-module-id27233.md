# Supporting OBJ with texture maps (without textureModel module)

**Topic ID**: 27233
**Date**: 2023-01-13
**URL**: https://discourse.slicer.org/t/supporting-obj-with-texture-maps-without-texturemodel-module/27233

---

## Post #1 by @muratmaga (2023-01-13 17:54 UTC)

<p>There is quite a bit of interested working with textured 3D models in Slicer/SlicerMorph. We are also going to soon publish a paper on how to generate them using an entirely open-source pipeline. Here is a sample output:  <a href="http://smc-1.slicermorph.org:8000/public/task/40fde03c-1574-449a-b70c-03c291e023e6/3d/">http://smc-1.slicermorph.org:8000/public/task/40fde03c-1574-449a-b70c-03c291e023e6/3d/</a> (use the download button on the lower right to obtain the textured model).</p>
<p>Currently we can import the texture on these OBJ models using the Texture Model from IGT extension and it works.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40815d2253dbdd8b945ba32626385fa4f0ce4e72.jpeg" data-download-href="/uploads/short-url/9cDIz04bINttErjBvwrFsSPyFge.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40815d2253dbdd8b945ba32626385fa4f0ce4e72_2_307x375.jpeg" alt="image" data-base62-sha1="9cDIz04bINttErjBvwrFsSPyFge" width="307" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40815d2253dbdd8b945ba32626385fa4f0ce4e72_2_307x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40815d2253dbdd8b945ba32626385fa4f0ce4e72_2_460x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/0/40815d2253dbdd8b945ba32626385fa4f0ce4e72_2_614x750.jpeg 2x" data-dominant-color="8F90B0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">675×822 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>But it is not quite convenient, mostly because the texture maps are huge and when loaded into the slicer scene (which is required to run the texture model module), it creates huge offset in the 3D viewer, which confuses people about why the model is not centered on the BB (it will, if you delete the texture object, after you run the Texture model).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/673c8b427c9af118f6de09679f8c17e0318672e5.png" data-download-href="/uploads/short-url/eJgTrQLZwfPibJfaM9HAaJRa1cp.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/673c8b427c9af118f6de09679f8c17e0318672e5_2_532x500.png" alt="image" data-base62-sha1="eJgTrQLZwfPibJfaM9HAaJRa1cp" width="532" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/673c8b427c9af118f6de09679f8c17e0318672e5_2_532x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/673c8b427c9af118f6de09679f8c17e0318672e5_2_798x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/7/673c8b427c9af118f6de09679f8c17e0318672e5_2_1064x1000.png 2x" data-dominant-color="A6A7D6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1237×1162 16.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>What would it take to make loading the texture (for OBJ format) automatically be supported as it is in other application like Meshlab, without requiring to load the texture and run the module.</p>

---

## Post #2 by @pieper (2023-01-13 22:26 UTC)

<p>The model storage node C++ code could be updated to detect the texture and apply it automatically.  Or the python code from the extension could be made into a custom reader plugin that implements the texturing part without going through a volume node.  Either is possible with some effort (how much effort depends on who is doing it).  It would be a good learning exercise for a new developer.</p>

---
