---
topic_id: 38217
title: "Mri Ct Registration"
date: 2024-09-04
url: https://discourse.slicer.org/t/38217
---

# MRI/CT registration

**Topic ID**: 38217
**Date**: 2024-09-04
**URL**: https://discourse.slicer.org/t/mri-ct-registration/38217

---

## Post #1 by @Kowsar_Sheikhi (2024-09-04 19:14 UTC)

<p>Hi,</p>
<p>Do you have any suggestions for MRI/CT image registration?<br>
Both images are in DICOM format and have been cropped to focus on the ROI. I have tried using the Brain and Elastix methods, but they didn’t work well (perhaps I made a mistake, as they finished with errors).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5df7dbeef96495bfc09ae441bd5685287001dc12.jpeg" data-download-href="/uploads/short-url/dphrj7emkkOi995AvKm2yHBPjAS.jpeg?dl=1" title="registraton-3dslicer.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5df7dbeef96495bfc09ae441bd5685287001dc12_2_690x363.jpeg" alt="registraton-3dslicer.PNG" data-base62-sha1="dphrj7emkkOi995AvKm2yHBPjAS" width="690" height="363" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5df7dbeef96495bfc09ae441bd5685287001dc12_2_690x363.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5df7dbeef96495bfc09ae441bd5685287001dc12_2_1035x544.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5df7dbeef96495bfc09ae441bd5685287001dc12.jpeg 2x" data-dominant-color="52515A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">registraton-3dslicer.PNG</span><span class="informations">1341×706 97.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-09-04 20:52 UTC)

<p>It’s a bit hard to tell from the screenshot, but they look like they should be able to be registered.  Perhaps you can post the error messages (use the Help-&gt;report a bug dialog to get the full log file).</p>
<p>A registration issue could be the knee angle being different in which case you may need to do the bones independently or something.</p>

---

## Post #3 by @Kowsar_Sheikhi (2024-09-05 12:42 UTC)

<p>I manually created the transformations for them and centralized both. All transformations have been saved as LinearTransform. I tried using Elastix with the LinearTransform and received the following error:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/2/a28fb9690a087fe6ef5cf1b321d95cbbb5b2c2b2.jpeg" data-download-href="/uploads/short-url/nc5heHmKl7XHt4PppQNgJq78OrM.jpeg?dl=1" title="Elastix.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a28fb9690a087fe6ef5cf1b321d95cbbb5b2c2b2_2_690x265.jpeg" alt="Elastix.PNG" data-base62-sha1="nc5heHmKl7XHt4PppQNgJq78OrM" width="690" height="265" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a28fb9690a087fe6ef5cf1b321d95cbbb5b2c2b2_2_690x265.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a28fb9690a087fe6ef5cf1b321d95cbbb5b2c2b2_2_1035x397.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/2/a28fb9690a087fe6ef5cf1b321d95cbbb5b2c2b2_2_1380x530.jpeg 2x" data-dominant-color="7E7981"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Elastix.PNG</span><span class="informations">1920×738 150 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I also tried the general registration (Brains) with the same LinearTransform, but the result was not the clear registration I wanted:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63e32342d3ce2ae5f0bd90b5207139c0ab467791.png" data-download-href="/uploads/short-url/efDUpMVmSdxPMBO3CPCSHzwaN33.png?dl=1" title="Brains" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63e32342d3ce2ae5f0bd90b5207139c0ab467791_2_690x302.png" alt="Brains" data-base62-sha1="efDUpMVmSdxPMBO3CPCSHzwaN33" width="690" height="302" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63e32342d3ce2ae5f0bd90b5207139c0ab467791_2_690x302.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63e32342d3ce2ae5f0bd90b5207139c0ab467791_2_1035x453.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63e32342d3ce2ae5f0bd90b5207139c0ab467791_2_1380x604.png 2x" data-dominant-color="82817F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Brains</span><span class="informations">2560×1124 389 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>They are human knees, and because they are changing, I used the MomentsAlign transform mode.</p>
<p>3DSlicer 5.6.2</p>

---

## Post #4 by @pieper (2024-09-05 13:09 UTC)

<p>You’ll need to look at the error messages (the full details are not visible in these screenshots).  I suggest you practice with other datasets (e.g. sample data from the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Registration/RegistrationLibrary">registration library</a>) and then apply what you learn to these.</p>

---

## Post #5 by @Kowsar_Sheikhi (2024-09-05 13:15 UTC)

<p>Thanks! I have done some registrations before, but all of them were from the same modality (MRI/MRI or CT/CT). Now, when I try CT/MRI registration, it doesn’t work.</p>
<p>Do you know if there is any SOP or document available for CT/MRI registration?</p>

---

## Post #6 by @pieper (2024-09-05 13:20 UTC)

<p>Well it should “just work” for many situations as you can see from the examples I sent you.  Please be sure to study the <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">documentation</a> and try to see what’s different with your data.</p>

---

## Post #7 by @Kowsar_Sheikhi (2024-09-09 14:55 UTC)

<p>I have tried all the registration modes based on the documentation page, but the problem persists, and I still couldn’t register my images.</p>
<p>I would appreciate it if anyone could help me with this issue.<br>
Thanks!</p>

---

## Post #8 by @pieper (2024-09-09 15:00 UTC)

<p>If the examples work correctly, but your data doesn’t work then you’ll need to figure out what’s different about your data.  Is it data you can share publicly?</p>

---

## Post #9 by @Matteboo (2024-09-09 15:39 UTC)

<p>You can get a more detailled error message by looking at the elastix log. To do this:</p>
<ul>
<li>check “Keep temporary files” in the “Advanced” tab</li>
<li>Launch your registration</li>
<li>Once it failed, click on “show temp folder”</li>
<li>Open the elastix.txt file and scroll down to find the error</li>
</ul>

---

## Post #11 by @pieper (2024-09-11 19:22 UTC)

<p>Okay, thanks for sharing the data - I can see now what’s going on and give you some suggestions.</p>
<p>First there’s a big difference in both resolution and field of view.  So with the default settings BRAINSFit was giving this kind of message (you can see them in the python console).</p>
<pre><code class="lang-auto">[VTK] All samples map outside moving image buffer. The images do not sufficiently overlap. They need to be initialized to have more overlap before this metric will work. For instance, you can align the image centers by translation.
[VTK] General Registration (BRAINS) completed with errors
</code></pre>
<p>This is because the MR covers a lot of anatomy above and below the join space, while the microCT only covers the joint area.  Also the microCT is about 10x smaller pixels than the MR.  So I used the CropVolume module with an 8x spacing multiplier to get a low res version, than use the microCT’s ROI to crop the MR with a 1x multiplier.</p>
<p>Then in the BRAINSFit it completed but with a poor result, so I changed the percentage of sample from the default of 0.002 to 1.  This uses more of the image to do the optimization and can really impact the result (although with big images it will take longer.</p>
<p>I also tried setting the Max Iterations in the Advanced Optimization Settings to 15000 from 1500 but I don’t think this had as much impact.</p>
<p>After that things look reasonable to me:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aa7730ebcad81da6e6ca5dca5a2caa9364f18a9d.jpeg" data-download-href="/uploads/short-url/ok0xdktqLmvkRwl8KHkntbKCuxn.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa7730ebcad81da6e6ca5dca5a2caa9364f18a9d_2_690x190.jpeg" alt="image" data-base62-sha1="ok0xdktqLmvkRwl8KHkntbKCuxn" width="690" height="190" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa7730ebcad81da6e6ca5dca5a2caa9364f18a9d_2_690x190.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa7730ebcad81da6e6ca5dca5a2caa9364f18a9d_2_1035x285.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aa7730ebcad81da6e6ca5dca5a2caa9364f18a9d_2_1380x380.jpeg 2x" data-dominant-color="605E58"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×531 97.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>For reference here’s what the cropped volumes looked like before registration:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e97d3dfadd0ac7efd4157e2c8262ac8288e607d9.jpeg" data-download-href="/uploads/short-url/xjxzZOg5D1GSHa1yGHxsR3eYPBT.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e97d3dfadd0ac7efd4157e2c8262ac8288e607d9_2_690x191.jpeg" alt="image" data-base62-sha1="xjxzZOg5D1GSHa1yGHxsR3eYPBT" width="690" height="191" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e97d3dfadd0ac7efd4157e2c8262ac8288e607d9_2_690x191.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e97d3dfadd0ac7efd4157e2c8262ac8288e607d9_2_1035x286.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e97d3dfadd0ac7efd4157e2c8262ac8288e607d9_2_1380x382.jpeg 2x" data-dominant-color="5E5C56"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×533 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @Kowsar_Sheikhi (2024-09-12 12:46 UTC)

<p>Thank you so much for your help!! Now I can see the registered images! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Another question:<br>
Is it now possible to see the Python code and functions behind the registration process?</p>

---

## Post #13 by @pieper (2024-09-12 13:45 UTC)

<p>You can perform all these operations in python, and there are lots of examples of how this works.  <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#registration" class="inline-onebox">Script repository — 3D Slicer documentation</a></p>

---
