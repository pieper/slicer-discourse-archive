# Incorrect volume information when loading .nrrd

**Topic ID**: 33907
**Date**: 2024-01-22
**URL**: https://discourse.slicer.org/t/incorrect-volume-information-when-loading-nrrd/33907

---

## Post #1 by @mns.larsson (2024-01-22 14:13 UTC)

<p>When I load a .nrrd file I believe the direction matrix under volume information might be incorrect. In my example, the space directions in the .nrrd file is:</p>
<p><code>space directions: (1.99900970198094,0.0716907704748626,-1.35699601564168E-07) (-0.0357263945043087,0.996186852455139,-0.079595185816288) (-0.00285263080149889,0.0795440226793289,0.996827244758606)</code></p>
<p>,which would by my calculations give<br>
image spacing 1.9993, 1.0019, 1.0000<br>
and IJK to RAS Direction Matrix</p>
<pre><code class="lang-auto">-9.99839316e-01, -7.15529825e-02,  1.35699605e-07,
 1.78691748e-02, -9.94272205e-01,  7.95951878e-02,
-1.42679269e-03,  7.93911410e-02,  9.96827270e-01
</code></pre>
<p>The only calculations I’ve done here is extract the spacing and convert from LPS to RAS</p>
<p>However, slicer shows the following:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d311262054db52d0b7cf5bff436273cf8fc9bb6.png" alt="slicer_example" data-base62-sha1="mqA67uQs5Zqv1i7DNRvqhuh0tb8" width="576" height="117"></p>
<p>I can match the values shown in slicer by transposing the original space direction matrix but the way I interpret the .nrrd-file format specification that should not be necessary.</p>

---

## Post #2 by @lassoan (2024-01-22 15:04 UTC)

<p>There is no need for any transpose. The <code>space directions</code> field contains the I, J, K vectors in the physical space, which are the columns of the IJK to RAS matrix.</p>
<p>Note that you may find sign differences between the IJK to RAS matrix displayed in Slicer and the <code>space directions</code> field in the NRRD file header. NRRD file header can use various physical image coordinate systems, specified by the <code>space</code> field. Usually it contains <code>left-posterior-superior</code>, which means that the space direction stores IJK to LPS.</p>

---

## Post #3 by @mns.larsson (2024-01-23 07:32 UTC)

<p>Thank you for the answer!<br>
I’ve converted the space_directions matrix to <code>IJK_toLPS</code> and then to <code>IJK_to_RAS</code>.<br>
In my application I load an annotations in python and extract some point, I then use the slicer API to plot annotations with points. The points are added using <code>vtkMRMLMarkupsFiducialNode</code> which, as I understand, needs coordinates in RAS directly.</p>
<p>If I compare the IJK_to_RAS matrixes when loading the .nrrd file with pynrrd they are not consistent (I need to transpose one of them for it to be consistent). This caused an error when plotting the points.</p>
<p>Note that I do not compare the <code>space_directions</code> directly with the <code>IJK_to_RAS</code> matrix but convert using the code below</p>
<blockquote>
<p>spacing = affine_to_spacing(space_direction_matrix) #  affine_to_spacing from MONAI<br>
IJK_to_LPS = space_direction_matrix/spacing<br>
IJK_to_RAS = np.array([-1, -1, 1]) @ IJK_to_LPS</p>
</blockquote>
<p>However, looking at the format specification of .nrrd I believe it might be pynrrd that might do the loading incorrectly (<a href="https://teem.sourceforge.net/nrrd/format.html#spacedirections" class="inline-onebox" rel="noopener nofollow ugc">Teem: nrrd: Definition of NRRD File Format</a>)</p>

---

## Post #4 by @lassoan (2024-01-23 15:11 UTC)

<p>It makes sense for pynrrd to store the vectors as they do now, because you want <code>nrrd.read_header('myimage.nrrd')['space directions'][0]</code> to return the first vector, <code>...[1]</code> the second vector, etc.</p>
<p>However, it was probably not good choice of pynrrd developers to store the vectors in a 2D numpy array, because as your example shows, somebody may be tempted to interpret this matrix as the matrix transform that the nrrd documentation describes. It would have been more clear storing the vectors in a Python list. At this point, probably the best is to clarify this in the pynnrd documentation. If you have time, it would be nice if you could send a pull request to the <a href="https://github.com/mhe/pynrrd">pynrrd repository</a> to improve its documentation.</p>

---

## Post #5 by @mns.larsson (2024-01-23 15:37 UTC)

<p>Makes sense, thank you for your help!<br>
I’ll contact the pynrrd people and make them aware that this might be confusing. In this case, I guess it’s how MONAI reads the header and converts to an affine matrix that is incorrect.</p>

---
