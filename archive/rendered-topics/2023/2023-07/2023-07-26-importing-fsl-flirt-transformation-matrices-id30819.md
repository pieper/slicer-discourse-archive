# Importing FSL FLIRT transformation matrices?

**Topic ID**: 30819
**Date**: 2023-07-26
**URL**: https://discourse.slicer.org/t/importing-fsl-flirt-transformation-matrices/30819

---

## Post #1 by @mikebind (2023-07-26 22:19 UTC)

<p>I have a colleague who uses FSL (<a href="https://fsl.fmrib.ox.ac.uk/fsl/fslwiki" rel="noopener nofollow ugc">https://fsl.fmrib.ox.ac.uk/fsl/fslwiki</a>) for processing fMRI imaging. One of the outputs generated using their registration tool (called FLIRT) is a 4x4 affine transformation matrix representing the relationship between a patient brain image and an MNI standard space.  I would like to use this transform in Slicer, but when I use the matrix as saved by FLIRT, it does not seem to match up, I’m guessing due to some differences in conventions between FSL and Slicer.  However, geometry should be universal, so there should be a way to convert between FSL’s representation and Slicer’s, and that’s what I would like to figure out.  I have access to NIFTI image volumes before and after transformation using FLIRT but I am having trouble figuring out what the difference is.  I am guessing that perhaps FLIRT transform matrices ignore or manipulate some of the properties of the moving image (e.g. discarding the origin, or ignoring the IJK axes directions, or aligning center of mass first) but my explorations have not managed to get the output of a Slicer registration to line up with the FLIRT matrix thus far.   If someone here has any experience with this or suggestions, I would greatly appreciate it, thanks!</p>

---

## Post #2 by @mikebind (2023-07-26 23:30 UTC)

<p>I think I’ve got it figured out now. The matrix output from FLIRT is an IJK to IJK transformation matrix, whereas Slicer registrations produce a RAS to RAS transformation matrix. I will do some more testing to verify, but this makes sense and seems to work on the example case I was working with.  To provide a little more explanation, this makes sense to me because FLIRT is really only going to use the transformation matrix to interpolate/resample voxel values among the moving image IJK grid relative to the fixed image IJK grid, and the fully concatenated IJK to IJK transformation matrix is the most convenient for that use case.  Slicer, on the other hand, wants you to be able to use the transform for moving things like MarkupsFiducial points and ModelNodes (so that they can move with an image in space) and not just for resampling images.  For that use case, you want to represent the transformation as happening between locations in the physical space that image voxels occupy, keeping track of the relation between physical space locations and each image’s IJK coordinates separately.</p>

---

## Post #3 by @mikebind (2023-07-27 22:53 UTC)

<p>Unfortunately, I seem to have jumped to the wrong conclusion.  When I tried to code what I thought I had figured out, it did not work on other cases, and when I went back to re-examine the case that I thought had worked, I realized that I had not looked closely enough, and it actually hadn’t worked.  Trying to dig deeper into what might be going on, I have found a few clues (<a href="https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/tutorial_packages/centos6/fsl_507/doc/wiki/FLIRT(2f)FAQ.html#What_is_the_format_of_the_matrix_used_by_FLIRT.2C_and_how_does_it_relate_to_the_transformation_parameters.3F" class="inline-onebox" rel="noopener nofollow ugc">FLIRT/FAQ</a>, <a href="https://neurostars.org/t/whats-the-relation-between-fsls-motion-parameters-and-the-affine-transformation-matrix-specifically-the-translation/3839" class="inline-onebox" rel="noopener nofollow ugc">What's the relation between FSL's motion parameters and the affine transformation matrix (specifically the translation) - neuroimaging - Neurostars</a>, and <a href="https://www.jiscmail.ac.uk/cgi-bin/wa-jisc.exe?A2=ind1910&amp;L=FSL&amp;D=0&amp;P=50308" class="inline-onebox" rel="noopener nofollow ugc">JISCMail - FSL Archives</a> ) which might be related and which suggest that FSL tools sometimes consider the center of a corner voxel as the origin of an image, sometimes use an image volume’s center of mass as a point around which transformations are applied, and sometimes apply a reflection/translation to ijk_to_space matrices to enforce handedness of a coordinate system. I will try to seek some answers in FSL forums/mailing lists since my confusion at this point primarily exists on that side, but if anyone in the Slicer community has insight into this problem, I would appreciate any help given.  Thanks!</p>

---

## Post #4 by @pieper (2023-07-28 01:11 UTC)

<p>I haven’t used FSL very much at all, so I don’t know the answer.  I know some other tools define their transforms relative to a source image geometry, so you need both the image and the transform in order to interpret the transform, and that may be the case for FSL too.  Or there could be other conventions to learn.  We hope the Slicer conventions are clear.</p>

---

## Post #5 by @mikebind (2023-07-28 02:43 UTC)

<p>Thanks, that is a good thought <a class="mention" href="/u/pieper">@pieper</a>, but, while FSL does require a reference image to set the resampled output field of view and resolution, I don’t think the transformation matrix has an asymmetric relationship to one of the images, because they say that the inverse transformation can be obtained by inverting the transform matrix, and indeed, saved transformations files from reversed registrations are matrix inverses of one another.  I think that means that whatever geometric relationship they are specifying, it treats each coordinate system symmetrically.  It could, perhaps, be something like the relationship between the center of mass of one image to the center of mass of the other image (that’s something I haven’t tried yet because it’s a little harder to set up).</p>
<p>As far as Slicer transformations are concerned, I think I understand them pretty well.  Here goes: A linear transformation with homogenous transformation matrix A which comes from registering a moving image volume M to a fixed image volume F  in Slicer relates the spatial coordinate system with 1 mm long basis vectors pointing along the IJKtoRAS directions of volume F and origin at the center of the voxel with IJK index [0,0,0] to the spatial coordinate system with 1 mm long basis vectors pointing along the IJKtoRAS directions of volume M and origin at the center of the voxel of M with IJK index [0,0,0].  If v is a vector with spatial (mm) coordinates in the coordinate system associated with M, and u =  A * v, then u is a vector with spatial coordinates in the coordinate system associated with F {it’s either that or vice versa, I do sometimes still get confused about which direction is correct for which kind of object, since I know it differs whether you are transforming points (the “forward” or “modeling” direction) or resampling images (the “resampling”  or “reverse?,backward?” direction), but since I know it’s one or the other I can just check both and use the direction which is correct.}  If you want to know voxel indices corresponding to an image volume’s spatial coordinate system, you can use (the inverse of) that image volume’s IJKtoRAS matrix.</p>

---

## Post #6 by @pieper (2023-07-28 14:43 UTC)

<p>Yes, your description of Slicer’s transforms sounds correct, but I’d state it differently.</p>
<p>The registration transform is just a mapping from x’ = f_MtoF(x) going from a moving point in RAS to a fixed point in RAS so it can either be use to move or resample the data, and generally it’s invertible (it can be linear or nonlinear).  Each volume has a homogenous affine matrix like F_ijkToRAS and M_ijkToRAS going from pixel space to world space (RAS is world space in Slicer).</p>
<p>So to go from pixel in moving to pixel ijk in fixed it would be like F_ijkToRAS_-1 * f(M_ijkToRAS * ijk).  In other words start with the ijk of a moving pixel, transform it into RAS, move it to the RAS point in the fixed volume, and then map back to fixed volume ijk with the inverse of it’s ijkToRAS matrix.  When f is linear this can be collapsed into a single 4x4 matrix.</p>

---

## Post #7 by @mikebind (2023-07-28 16:47 UTC)

<p>Thanks for the clearer description; that does match my understanding. For resampling of the moving image into the fixed image voxel space, however, you would start from fixed image ijk coordinates and find the corresponding moving image ijk coordinate that you need to interpolate from. That’s the inverse of the transform you give, so that’s where I occasionally get confused which direction to use when I have this stuff less clearly on the top of my mind. I appreciate the engagement, and will post back here if I manage to figure out the FLIRT transform matrix.</p>

---

## Post #8 by @mikebind (2023-08-03 05:14 UTC)

<h2><a name="p-98572-quick-summary-1" class="anchor" href="#p-98572-quick-summary-1" aria-label="Heading link"></a>Quick Summary</h2>
<p>It is possible to convert between Slicer registration transform matrices and FSL/FLIRT registration transform matrices.  They differ because Slicer transforms describe transformations within RAS space, whereas FLIRT transforms describe transformations between scaled (and sometimes reflected) voxel spaces.  Converting between them requires understanding exactly when FLIRT transforms performed a reflection/translation before registration, as well as what other elements of the images are included in the FLIRT transformation matrix which are not part of the Slicer transform matrix. This is not well documented and was not intuitive to me (hence the long explanation below).  If you want to skip to something which might “just work” for you, start from the code in the gist linked at the bottom of the post.</p>
<h1><a name="p-98572-detailed-explanation-2" class="anchor" href="#p-98572-detailed-explanation-2" aria-label="Heading link"></a>Detailed Explanation</h1>
<p>Slicer transformation matrices relate RAS spatial coordinates.  That is, image data for each image is first situated in the RAS spatial coordinate system, and then the Slicer transformation matrix converts a vector of RAS coordinate (for example the location of some anatomical feature in the moving image) to the corresponding RAS coordinate relative to the fixed image (the location of the same anatomical feature in the fixed image in spatial RAS space)</p>
<p>FSL/FLIRT transformation matrices relate scaled (and sometimes reflected) ijk spatial coordinates.  The units are millimeters, but the header information regarding the orientation and location of image volume axes in a world coordinate system (the qform or sform in NIFTI files, or the IJKToRASMatrix in Slicer) is almost entirely ignored. I say “almost entirely” because FSL/FLIRT does look at the IJKToRASMatrix (or equivalent), and if the determinant of that matrix is positive, before registration is carried out, the orientation of the i-axis is reversed and the origin is moved to the other corner voxel on the i-axis. This reflection-translation inverts the sign of the determinant so that it is now negative.<br>
It is possible to obtain the Slicer transformation matrix from the FSL/FLIRT transformation matrix, or vice versa, as long as you also have the two image volumes which were used in the registration which generated the matrix you have, or at the absolute minimum, image volumes which you know to have identical header data (same IJKToRASDirectionMatrix, voxel size, image array dimensions; the voxel contents are not needed) to the image volumes which were registered.</p>
<p>This was not straightforward to figure out, but I think I have it all worked out now, and am going to try to lay it out clearly enough that hopefully this can be helpful to others. In the final understanding, I found the series of coordinate systems in the table below very helpful.  Some nomenclature notes first:<br>
I use V for a generic image volume, F for the image volume used as the fixed image in the registration pair (“-ref” in the FLIRT command), and M for the moving image volume in the registration pair (“-in” in the FLIRT command).  I use ijk to refer to image voxel array coordinates.  I use hjk to refer to the image voxel array coordinates after the i-axis has been optionally flipped and shifted.  Note that hjk is sometimes identical to ijk (if the determinant of the IJKToRasDirectionMatrix is negative), that is, I use hjk notation after the flip could have been applied, even if it wasn’t actually applied (because the determinant was already negative). I use hjkMm to refer the coordinate system where hjk indices have been scaled by the voxel size and therefore the coordinate system has millimeter units rather than voxel units. The FLIRT transformation matrix transforms between the moving image’s hjkMm coordinate system to the fixed image’s hjkMm coordinate system.  The next coordinate system has the HJKToRASDirectionMatrix rotation applied to hjkMm coordinates;  I call this one hras0, where the “h” is a reminder that the voxel origin may have been switched, the “ras” is because we are in a RAS coordinate system, and the “0” is a reminder that the ”h” voxel origin has not yet been moved from [0,0,0]. That is, the transformations from hjk to hras0 involve only scaling and rotation around the origin, so [0,0,0] in hjk space is also [0,0,0] in hras0 space.  The last coordinate system is called ras and represents the completion of the transformation from ijk voxel array space to a spatial location in RAS space as defined by the image header. ras differs from hras0 only by a translation transformation which moves the location of [0,0,0] in ijk space, as represented in hras0 space, to the origin location specified in the image header. This ras coordinate system is the same one used as the 3D space RAS coordinate system in 3D Slicer. It no longer has an “h” in the notation because no element remains tying it to the h-axis flip/translation.  Between ijk and ras, if a flip/translation occurred, it happened between the ijk coordinate system and the hjk coordinate system, and then was undone by the combination of moving from the hjkMm space to the hras0 space and the translation from hras0 space to ras.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Coord System Name</th>
<th>Units</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>V_ijk</td>
<td>voxels</td>
<td>Voxel array coordinate system for volume V</td>
</tr>
<tr>
<td>V_hjk</td>
<td>voxels</td>
<td>Voxel array coordinate system for volume V, except that a h coordinate replaces the i coord, and where, Option A: h = i if the determinant of the IJKToRAS matrix for V is negative, or Option B: h = N - 1 - i if the determinant is negative.  N = the number of image array voxels in the i dimension. This effectively switches the origin of the image from one corner of the array to the opposite corner (from the original [0,0,0] voxel to the original [N-1,0,0] voxel). This is done by FSL to enforce that all images have a fixed handedness (i.e. forcing a negative determinant). I’m not totally sure why anyone would do this; perhaps because if they didn’t they would have to allow reflections in their transform matrices?</td>
</tr>
<tr>
<td>V_hjkMm</td>
<td>mm</td>
<td>scaled voxel coordinate system. Origin has not moved relative to the V_hjk coordinate system, but [1,1,1] in the V_hjk coordinate system is located at [Sp_i, Sp_j, Sp_k] in the V_hjkMm coordinate system, where Sp_i is the voxel spacing in the i direction (note Sp_h and Sp_i are the same), and likewise for Sp_j, and Sp_k. More generally, the point [h,j,k] is located at [h*Sp_i, j*Sp_j, k*Sp_k] in the V_hjkMm coordinate system.</td>
</tr>
<tr>
<td>V_hras0</td>
<td>mm</td>
<td>rotated coordinate system. Origin has not moved relative to the V_hjk coordinate system, but the axes which point in the h, j, and k directions in the V_hjk and V_hjkMm coordinate systems now point in the directions of the columns of the V_HJKDirs matrix. The V_HJKDirs matrix is the same as the IJKToRAS direction matrix of V if det(V_IJKToRASDirs) &lt; 0, but if det(V_IJKToRASDirs) &gt; 0, then V_HJKDirs = V_IJKToRASDirs @ diag([-1, 1, 1, 1]), because the h axis is reversed with respect to the i axis. Note that V_IJKToRASDirs is IJKToRAS **DIRECTIONS** matrix, not the IJKToRASMatrix (which includes scaling and origin translation).  In contrast, the IJKToRASDirection matrix (obtained by volNode.GetIJKToRASDirectionMatrix() in Slicer) has unit length columns and no translation component.</td>
</tr>
<tr>
<td>V_ras</td>
<td>mm</td>
<td>spatial coordinates in the Slicer world coordinate system.  The axis directions match those in V_hras0, but there is a translation-only difference between the two coordinate systems. In V_hras0, the V_hjk origin voxel is still at [0,0,0], but in V_ras, that voxel is located at V_hOri, and the V_ijk origin voxel is located at volNode.GetOrigin().  V_hOri is calculated to compensate for the switch of origin from i to h (if it happened; if det(V_IJKToRASDirs)&lt;0, h=i, and hOri=ori).</td>
</tr>
</tbody>
</table>
</div><p>Here is a table of what each of the stepwise transformation matrices are between adjacent coordinate systems:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Transformation</th>
<th>Calculation</th>
</tr>
</thead>
<tbody>
<tr>
<td>V_ijk_to_hjk</td>
<td>Identity matrix if det(IJKToRas) &lt; 0, or translationMatrix([N-1, 0 , 0]) @ diag([-1, 1,1,1]) if det(IJKToRas) &gt; 0, where @ means matrix multiplication (as in numpy)</td>
</tr>
<tr>
<td>V_hjk_to_hjkMm</td>
<td>diag([Sp_i, Sp_j, Sp_k, 1]) if the voxel spacing is [Sp_i, Sp_j, Sp_k] in the i, j, and k directions, respectively</td>
</tr>
<tr>
<td>V_hjkMm_to_hras0</td>
<td>IJKToRASDirectionMatrix if det(IJKToRas) &lt; 0, or IJKToRASDirectionMatrix @ diag([-1, 1, 1, 1]) if det(IJKToRas) &gt; 0</td>
</tr>
<tr>
<td>V_hras0_to_ras</td>
<td>translationMatrix(ori - ijk_origin_in_hras0), where ori is the origin listed in the header information for image volume V, and ijk_origin_in_hras0 is the location of the point with ijk=[0,0,0] in the hras0 coordinate system.  This can be calculated as V_hjkMm_to_hras0 @ V_hjk_to_hjkMm @ V_ijk_to_hjk @ [0,0,0,1].</td>
</tr>
</tbody>
</table>
</div><p>If a registration has been carried out between a moving image volume M and a fixed image volume F, then one can find the corresponding ijk coordinate in F to an ijk coordinate in M through the following chain of coordinate system transformations:</p>
<p>M_ijk to M_hjk to M_hjkMm to M_hras0 to M_ras to F_ras to F_hras0 to F_hjkMm to F_hjk to F_ijk</p>
<p>Slicer and FLIRT registrations respresent different portions of this chain. A Slicer registration transfrom matrix would represent just the M_ras to F_ras transformation, whereas a FLIRT registration transform matrix represents the M_hjkMm to M_hras0 to M_ras to F_ras to F_hras0 to F_hjkMm transformation.</p>
<p>With this knowledge, we can convert between them!</p>
<h2><a name="p-98572-flirt-transformation-matrix-from-slicer-transformation-matrix-3" class="anchor" href="#p-98572-flirt-transformation-matrix-from-slicer-transformation-matrix-3" aria-label="Heading link"></a>FLIRT transformation matrix from Slicer transformation matrix:</h2>
<p>FLIRT_Matrix = F_ras_to_F_hjkMm @ Slicer_Matrix @ M_hjkMm_to_M_ras</p>
<p>where</p>
<p>M_hjkMm_to_M_ras = M_hras0_to_ras @ M_hjkMm_to_hras0</p>
<p>F_ras_to_F_hjkMm = inv(F_hjkMm_to_hras0) @ inv(F_hras0_to_ras)</p>
<h2><a name="p-98572-slicer-transformation-matrix-from-flirt-transformation-matrix-4" class="anchor" href="#p-98572-slicer-transformation-matrix-from-flirt-transformation-matrix-4" aria-label="Heading link"></a>Slicer transformation matrix from FLIRT transformation matrix:</h2>
<p>Slicer_matrix = F_hjkMm_to_ras @ FLIRT_Matrix @ M_ras_to_hjkMm</p>
<p>where</p>
<p>F_hjkMm_to_ras = F_hras0_to_ras @ F_hjkMm_to_hras0</p>
<p>M_ras_to_hjkMm = inv(M_hjkMm_to_hras0) @ inv(M_hras0_to_ras)</p>
<h1><a name="p-98572-python-code-to-perform-conversion-5" class="anchor" href="#p-98572-python-code-to-perform-conversion-5" aria-label="Heading link"></a>Python code to perform conversion</h1>
<aside class="onebox githubgist" data-onebox-src="https://gist.github.com/mikebind/d116527e29458637602c86b1d4cd8c2c">
  <header class="source">

      <a href="https://gist.github.com/mikebind/d116527e29458637602c86b1d4cd8c2c" target="_blank" rel="noopener nofollow ugc">gist.github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://gist.github.com/mikebind/d116527e29458637602c86b1d4cd8c2c" target="_blank" rel="noopener nofollow ugc">https://gist.github.com/mikebind/d116527e29458637602c86b1d4cd8c2c</a></h4>

  <h5>Slicer_FSL-FLIRT_Transforms_Conversion.py</h5>
  <pre><code class="Python">import numpy as np
import slicer, vtk


def getVolumeCoordinateTransformMatrixDict(volNode):
    import numpy as np

    def translationMatrix(point):
        trMat = np.eye(4)
        trMat[0:3, 3] = (*point,)</code></pre>
   This file has been truncated. <a href="https://gist.github.com/mikebind/d116527e29458637602c86b1d4cd8c2c" target="_blank" rel="noopener nofollow ugc">show original</a>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #9 by @pieper (2023-08-03 14:10 UTC)

<p>Nice work <a class="mention" href="/u/mikebind">@mikebind</a> <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>I understand that FSL and FreeSurfer are used together a lot.  It might make sense to add an implementation of this work to the <a href="https://github.com/PerkLab/SlicerFreeSurfer">SlicerFreeSurfer</a> extension.</p>

---
