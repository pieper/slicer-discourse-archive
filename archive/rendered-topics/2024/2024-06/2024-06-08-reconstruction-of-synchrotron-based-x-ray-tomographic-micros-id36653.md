# Reconstruction of synchrotron-based X-ray tomographic microscopy (SRXTM) images

**Topic ID**: 36653
**Date**: 2024-06-08
**URL**: https://discourse.slicer.org/t/reconstruction-of-synchrotron-based-x-ray-tomographic-microscopy-srxtm-images/36653

---

## Post #1 by @Trung_L_i_Quang (2024-06-08 05:53 UTC)

<p>Dear community,</p>
<p>I am a newbie to 3D Slicer and I’m hoping to get some advice. I have a set of Synchrotron-based X-ray tomographic microscopy (SRXTM) images including 1700 slices (2D). I would like to visualize its 3D volume according to the grey value range of 0 to 256 (attached example image).</p>
<p>Is 3D Slicer software suitable for this task? Does anyone have experience visualizing SRXTM data in 3D Slicer?</p>
<p>Any assistance you can provide would be greatly appreciated!</p>
<p>Best regards,<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a426780ecc5f5d0dda0acff65c2eb896d9778ec2.png" alt="Picture1" data-base62-sha1="nq8IVbybGZ82icgRDtwvmbEMwaS" width="605" height="215"></p>

---

## Post #2 by @pieper (2024-06-08 23:11 UTC)

<p>Yes, that should be something you can do in Slicer.  Please have a look at the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#3D_Visualization">tutorials and examples</a>, maybe the ones from <a href="https://slicermorph.github.io/">SlicerMorph</a> and let us know if you hit any specific issues.  It may depend on the resolution and format of the images, so you could report that info here if you have trouble.</p>

---

## Post #3 by @Trung_L_i_Quang (2024-06-09 08:32 UTC)

<p>Dear Mr. Steve Pieper,</p>
<p>Thanks for your response!</p>
<p>Here is some information related to my work.</p>
<ul>
<li>Operating system: Windows 10, Intel(R) Core™ i7-6820HQ CPU @ 2.70GHz 2.71 GHz, 32GB RAM.</li>
<li>Slicer version: 5.6.2</li>
<li>Data information: My data consists of 1700 JPEG slices (5120 x 3840) that were converted from TIFF original format. Its resolution is 2.4014755 μm.</li>
</ul>
<p>I have opened 1700 slices of JPEG format using SlicerMorph extension and reconstruct its 3D volume (enclosed image).</p>
<p>Now, I want to create segments from whole tomographic volume based on predefined intensity ranges, which are high grey values from 210 to 255 (silica), low grey values from 110 to 200 (high organic matter), intermediate grey values from 50 to 110 (low organic matter), and &lt; 50 (air).</p>
<p>I tried utilizing the Segment Editors module’s Threshold option to accomplish it. However, the threshold value range is limited to 0 to 9 rather than 0 to 256.</p>
<p>Could you please advise me on how to proceed?</p>
<p>Any assistance you can provide would be greatly appreciated!</p>
<p>Best regards,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33842c89fc4c8319404fe84eb8b33df592ead04a.jpeg" data-download-href="/uploads/short-url/7lJx0HnDk6fu8fe1KlGR8fjG82K.jpeg?dl=1" title="1.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33842c89fc4c8319404fe84eb8b33df592ead04a_2_690x346.jpeg" alt="1.PNG" data-base62-sha1="7lJx0HnDk6fu8fe1KlGR8fjG82K" width="690" height="346" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33842c89fc4c8319404fe84eb8b33df592ead04a_2_690x346.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33842c89fc4c8319404fe84eb8b33df592ead04a_2_1035x519.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33842c89fc4c8319404fe84eb8b33df592ead04a_2_1380x692.jpeg 2x" data-dominant-color="B5B8D6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1.PNG</span><span class="informations">1920×964 98.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2024-06-09 17:58 UTC)

<p>Segment editor simply displays whatever intensity values are provided by your dataset. Are you sure you have 8 bit intensity values (0-255)? You can use the data probe (hover over individual voxels and see) and volumes module (for whole dataset) to obtain what the range of values are:<br>
For data probe see: <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#application-overview" class="inline-onebox">User Interface — 3D Slicer documentation</a></p>
<p>For volumes: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html" class="inline-onebox">Volumes — 3D Slicer documentation</a></p>

---
