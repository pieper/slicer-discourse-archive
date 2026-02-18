# ALPACA algorithm, and projection difficulties

**Topic ID**: 18231
**Date**: 2021-06-20
**URL**: https://discourse.slicer.org/t/alpaca-algorithm-and-projection-difficulties/18231

---

## Post #1 by @Alex_Tinius (2021-06-20 02:42 UTC)

<p>I would like to use the semi-automated landmarking approach ALPACA to auto-landmark clavicles.</p>
<p>However, I seem to be unable to find suitable parameters for the auto-landmarking process, and I was hoping you could point me in the right direction. As far as I can tell the surface alignment operates well. However, the output of semilandmarks is not comprehensible. If I run the algorithm with the default settings, all landmarks of all surfaces culminate in one point, i.e. the output.fcsv files contain replicates of one point in 3D space.</p>
<p>When I check the box ‘Skip projection’, all output.fcsv files contain different landmark arrays, as one would expect. I can read those with the read.fcsv() function from the Morpho package in R, but when I perform a Procrustes fit via ProcSym(), all landmark configurations are identical. The same happens when I use the GPA module in Slicer - all specimens share one set of Procrustes coordinates.</p>
<p>I was hoping that this is a common mistake in my approach of the program. I looked through the Slicer Forum and FAQ, and there seems to be nothing remotely similar to my issue. I would be grateful for any help you can offer.</p>
<p>How do I register those landmarks in a way that they actually differ?</p>

---

## Post #2 by @muratmaga (2021-06-20 04:45 UTC)

<p>I am a little surprised that landmarks are not transferred correctly, even though the alignment seems reasonable.</p>
<p>During the transfer of landmarks from the source to target mesh, sometimes landmarks can be a few voxels away from the target mesh. Projecting them to the closest point on the mesh takes care of them. Skipping projection, will disable this step. But for reasonably aligned meshes, this shouldn’t make a large difference.</p>
<p>Would be possible for you to share plys of two clavicles and a set of semi-landmarks for one of them for us to see what the issue?</p>
<p><a class="mention" href="/u/smrolfe">@smrolfe</a> <a class="mention" href="/u/agporto">@agporto</a></p>

---

## Post #3 by @agporto (2021-06-20 04:56 UTC)

<p>Hi Alex. As Murat mentioned, that is a very odd error. Never had anything like that happened. It would be really useful if you could share an example pair of meshes + landmarks. That way, we can examine more directly what the source of the problem might be. If I understood correctly, the whole pairwise alignment is working well, and you get landmarks that look reasonable on your target surface (after the deformable step). Is that correct? If so, that would suggest an issue with the exporting of landmarks to a file, which is an odd error to have since it relies on internal Slicer features. In any case, any more information you would be willing to share would be really helpful for our troubleshooting.</p>

---

## Post #4 by @Alex_Tinius (2021-06-20 09:29 UTC)

<p>Thank  You both for your swift reply.<br>
Here is some sample data: <a href="https://app.box.com/s/wl3r9ux223oketm9u4fq17tkhj9n9vg3" class="inline-onebox" rel="noopener nofollow ugc">Box</a><br>
clavR0 corresponds to the landmark set.<br>
Yes, the landmark projection looks reasonable. However, in detail it seems to eliminate all differences between specimens.</p>

---

## Post #5 by @muratmaga (2021-06-20 15:42 UTC)

<p>There are a bunch of things going on with your data:</p>
<ol>
<li>Scale of data is completely off. Values displayed are in the meters range, which is unlikely for the clavicle.</li>
<li>The coordinate system of reference mesh and LM is not the same. It is easy to see when you just to R0 sample mesh and fcsv file into Slicer. Your models appear to be in RAS coordinate. But Slicer by default assumes they are in LPS coordinate. You can manually change the coordinate when you load the model individually into Slicer, but when ALPACA is reading them, there is no way for us to know what the correct coordinate system is.</li>
</ol>
<p>The easiest solution is to transform your landmarks coordinates to match that of the models. For that you need to create a transform in which the first two diagonal values are -1 (and everything else) is untouched. When you apply and harden this transformation, your LMs appear on the surface as intended. Once I saved this transformed LM set, and rerun everything with the default settings, the landmarks transformed onto the target in a reasonable manner. The rest is for you to investigate.</p>
<p>However, before going forward too much, I would suggest where the data scale issue is coming from, and fixing it; particularly if your goal is quantitative morphology.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/0035769ad782ae620c7c9b0e2f97c74a0b5c8142.png" data-download-href="/uploads/short-url/1QxLpCjKtVIrLBDc82KocZ9qQW.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/0035769ad782ae620c7c9b0e2f97c74a0b5c8142.png" alt="image" data-base62-sha1="1QxLpCjKtVIrLBDc82KocZ9qQW" width="594" height="500" data-dominant-color="A0A0CE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">725×610 21.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @Alex_Tinius (2021-06-20 19:03 UTC)

<p>Thank You so much!<br>
The landmarks are scaled by micrometers, so I will need to reunite the new new grid values with the models. That should be straightforward, though.</p>
<p>When I multiply the x- and y-coordinates with -1, the landmarks do indeed fit to the model, and the algorithm works without difficulties.<br>
Problem solved.<br>
Thank You Murat!</p>

---

## Post #7 by @muratmaga (2021-06-20 19:58 UTC)

<p>You can try to set the units to micrometers in Slicer. However, the unit support is not consistent across the modules, so your mileage would vary. I would suggest scaling everything (both the models and fiducials) by 0.001 to bring the units to millimeters, which is default unit in Slicer.</p>
<p>Good luck.</p>

---
