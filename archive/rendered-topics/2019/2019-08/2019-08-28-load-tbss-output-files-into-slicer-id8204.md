---
topic_id: 8204
title: "Load Tbss Output Files Into Slicer"
date: 2019-08-28
url: https://discourse.slicer.org/t/8204
---

# Load TBSS output files into Slicer?

**Topic ID**: 8204
**Date**: 2019-08-28
**URL**: https://discourse.slicer.org/t/load-tbss-output-files-into-slicer/8204

---

## Post #1 by @M.F (2019-08-28 06:05 UTC)

<p>Hello,</p>
<p>I have been using FSL’s <a href="https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/TBSS" rel="nofollow noopener">TBSS</a> to compare the FA, RD, and AD values of two different groups. The result of this analysis is a single statistics file which is in the NIFTI format (.nii.gz), highlighting voxels that are significantly different between the two groups in terms of FA/RD/AD. I am trying to load this into Slicer, to create a diagram similar to <a href="https://www.researchgate.net/figure/Results-from-the-tract-based-spatial-statistics-TBSS-analyses-depicting-the-voxels-that_fig1_262055573" rel="nofollow noopener">this one</a>, but I’m very new to the software. Could someone help me out? Is there a way to load TBSS output data into Slicer?</p>
<p>Thank you!</p>

---

## Post #2 by @ljod (2019-08-28 07:15 UTC)

<p>Hi! In general it should be possible to load nifti files in Slicer. Could you let us know what steps you followed and what happened? There are tutorials for loading data here:<br>
<a href="https://www.slicer.org/wiki/Documentation/4.10/Training" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/Training</a></p>

---

## Post #3 by @Chris_Rorden (2019-08-28 17:37 UTC)

<p>An alternative solution might be to use MRIcroGL. It has far fewer features than Slicer, but it is a simple tool that might solve your task. Assuming you have <a href="https://github.com/rordenlab/MRIcroGL12/releases" rel="noopener nofollow ugc">MRIcroGL v1.2</a> the following script would create the following image (you would want to use the ‘mni152’ template if your data was normalized, and change spmMotor to the name of your statistical map).</p>
<pre><code>import gl
gl.resetdefaults()
#open background image
gl.loadimage('spm152')
gl.overlayloadsmooth(1)
#open overlay: show positive regions
gl.overlayload('spmMotor')
gl.minmax(1, -2,-5)
gl.colorname(1,'8redyell')
gl.colorfromzero(1,1)
gl.cutout(0.5,0.6,0.5,0,1,1)
gl.shadername('OverlaySurface')
gl.backcolor(255,255,255)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/593823c65f15095a8fbe8fc8ef927d70bbc54b4f.jpeg" data-download-href="/uploads/short-url/cJgLYbdn8XpqS5EDVdL8t12aFUH.jpeg?dl=1" title="cutout" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/593823c65f15095a8fbe8fc8ef927d70bbc54b4f_2_518x500.jpeg" alt="cutout" data-base62-sha1="cJgLYbdn8XpqS5EDVdL8t12aFUH" width="518" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/593823c65f15095a8fbe8fc8ef927d70bbc54b4f_2_518x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/593823c65f15095a8fbe8fc8ef927d70bbc54b4f_2_777x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/593823c65f15095a8fbe8fc8ef927d70bbc54b4f.jpeg 2x" data-dominant-color="B2ACA4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cutout</span><span class="informations">1024×988 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @pieper (2019-08-28 18:05 UTC)

<aside class="quote no-group" data-username="Chris_Rorden" data-post="3" data-topic="8204">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/chris_rorden/48/4073_2.png" class="avatar"> Chris_Rorden:</div>
<blockquote>
<p>It has far fewer features than Slicer</p>
</blockquote>
</aside>
<p>But the rendering is cooler!</p>

---

## Post #5 by @M.F (2019-08-28 20:13 UTC)

<p>Thank you! I followed these instructions, but the output has some sort of strange cuboid tessellation pattern that I haven’t seen in other figures. Does this have something to do with the settings I’m using? Or, do you think it has to do more with the structure of the data? TBSS uses voxels for analysis, so perhaps those cuboid patterns are a result of that (?)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f7402c2c9308fac08360e78315fd381ae4f2be0.jpeg" data-download-href="/uploads/short-url/bkSgS3626NDsJ7utpSdQ0StPnRS.jpeg?dl=1" title="17%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f7402c2c9308fac08360e78315fd381ae4f2be0_2_690x388.jpeg" alt="17%20PM" data-base62-sha1="bkSgS3626NDsJ7utpSdQ0StPnRS" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f7402c2c9308fac08360e78315fd381ae4f2be0_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f7402c2c9308fac08360e78315fd381ae4f2be0_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f7402c2c9308fac08360e78315fd381ae4f2be0_2_1380x776.jpeg 2x" data-dominant-color="717282"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">17%20PM</span><span class="informations">2560×1440 1.02 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a48e34a314d6b7f5a7558596898c408f02c9874.jpeg" data-download-href="/uploads/short-url/faeLWPcEPIqTMKwAzA94gX9ekqo.jpeg?dl=1" title="44%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a48e34a314d6b7f5a7558596898c408f02c9874_2_690x388.jpeg" alt="44%20PM" data-base62-sha1="faeLWPcEPIqTMKwAzA94gX9ekqo" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a48e34a314d6b7f5a7558596898c408f02c9874_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a48e34a314d6b7f5a7558596898c408f02c9874_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6a48e34a314d6b7f5a7558596898c408f02c9874_2_1380x776.jpeg 2x" data-dominant-color="636472"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">44%20PM</span><span class="informations">2560×1440 773 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/508ac6c019ea5e05ea9c744acc5f82260e6406e9.jpeg" data-download-href="/uploads/short-url/buvwwH8f3Gwqmw8pRWT99yk5CMp.jpeg?dl=1" title="21%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/508ac6c019ea5e05ea9c744acc5f82260e6406e9_2_690x388.jpeg" alt="21%20PM" data-base62-sha1="buvwwH8f3Gwqmw8pRWT99yk5CMp" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/508ac6c019ea5e05ea9c744acc5f82260e6406e9_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/508ac6c019ea5e05ea9c744acc5f82260e6406e9_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/508ac6c019ea5e05ea9c744acc5f82260e6406e9_2_1380x776.jpeg 2x" data-dominant-color="6A6B7D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">21%20PM</span><span class="informations">2560×1440 570 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @M.F (2019-08-28 20:15 UTC)

<p>This looks very cool! I will test this out, as well. Thank you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #7 by @ljod (2019-08-28 21:14 UTC)

<p>It looks like you are volume rendering the white matter skeleton voxels from tbss. More typical displays instead overlay slices of such a stats volume over a background anatomical image, with some nicely chosen colormap to only show significant regions. (Chris gave a very cool example.)</p>

---

## Post #8 by @M.F (2019-08-28 21:20 UTC)

<p>Got it, that’s what I’m trying now. To create a cutout like in Chris’s example, would I use a mask? I can’t figure out how to hide the masked segment…</p>

---

## Post #9 by @M.F (2019-08-28 21:23 UTC)

<p><a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> is it possible to export a figure like this to a .obj file out of MRIcroGL?</p>

---

## Post #10 by @Chris_Rorden (2019-08-29 12:28 UTC)

<p><a class="mention" href="/u/m.f">@M.F</a>. I would suggest you look at the <a href="https://www.youtube.com/watch?v=GNsWRnm7gQw" rel="noopener nofollow ugc">“3D Slicer Surface Model Tutorial fMRI” YouTube video</a>. MRIcroGL handles voxelwise volumes, not meshes (like obj files). Slicer can handle both voxels and meshes.</p>
<p>For this simple task, you might also want to try <a href="https://github.com/neurolabusc/surf-ice/releases" rel="noopener nofollow ugc">Surfice</a> which only deals with meshes. If you want to apply a simple statistical threshold to your voxels (say z &gt; 4.95) you would choose the Advanced/ConvertVoxelwiseVolumeToMesh and specify your threshold. You can then save to OBJ/GIFTI/PLY/MZ3/VRML/STL format. Assuming you named your output “myMesh.obj” you could run the following script to get the following image.</p>
<pre><code>import gl
gl.resetdefaults()
gl.meshload('BrainMesh_ICBM152Right.mz3')
gl.overlayload('myMesh.obj')
gl.overlaycolorname(1, 'red')
gl.shaderxray(1.0, 0.3)
gl.azimuthelevation(110, 15)
gl.meshcurv()
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1b154be2baf5b4ce70b1ab2f13f12e3cfb81228.jpeg" data-download-href="/uploads/short-url/wczmn0nX78CvPgyO66A3FKCol96.jpeg?dl=1" title="surfice2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1b154be2baf5b4ce70b1ab2f13f12e3cfb81228_2_609x500.jpeg" alt="surfice2" data-base62-sha1="wczmn0nX78CvPgyO66A3FKCol96" width="609" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e1b154be2baf5b4ce70b1ab2f13f12e3cfb81228_2_609x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1b154be2baf5b4ce70b1ab2f13f12e3cfb81228.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1b154be2baf5b4ce70b1ab2f13f12e3cfb81228.jpeg 2x" data-dominant-color="B7B4B6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">surfice2</span><span class="informations">652×535 58.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>At the moment there are a lot of free tools, so you should be able to mix and match them for your problems. The learning curve is steeper for Slicer since it can do much more and is far more extensible.</p>

---

## Post #11 by @M.F (2019-08-30 18:01 UTC)

<p>Thank you, this worked like a charm!</p>

---
