# UKF exit abnormally

**Topic ID**: 34734
**Date**: 2024-03-06
**URL**: https://discourse.slicer.org/t/ukf-exit-abnormally/34734

---

## Post #1 by @Pranali (2024-03-06 07:40 UTC)

<p>Hello, I’m using ubuntu 20.04 , i ran following command with error:<br>
./Slicer --launch UKFTractography --dwiFile /home/inspire_lab/Downloads/IXI-DATA-nrrd/combine_conform_IXI034-HH-1260.nrrd --maskFile /home/inspire_lab/Downloads/IXI-DATA-brain_mask/combine_conform_IXI034-HH-1260_brain_mask.nrrd --tracts /home/inspire_lab/Downloads/combine_conform_IXI034-HH-1260_tract.vtk --recordFA --recordTrace<br>
Using the 2T simple model. Setting the default parameters accordingly:<br>
“*”: set by user<br>
“-”: default setting</p>
<ul>
<li>stoppingFA: 0.15</li>
</ul>
<ul>
<li>seedingThreshold: 0.18</li>
</ul>
<ul>
<li>Qm: 0.001</li>
<li>Ql: 50</li>
<li>Rs: 0.02</li>
</ul>
<ul>
<li>stepLength: 0.3</li>
<li>recordLength: 0.9</li>
<li>stoppingThreshold: 0.1</li>
</ul>
<ul>
<li>seedsPerVoxel: 1<br>
Found 20 cores on your system.<br>
Running tractography with 20 thread(s).<br>
DWMRI_b-value 1000<br>
Number of non-zero gradients: 15<br>
Number of zero gradients: 1<br>
Permuting the axis order to: 3 0 1 2<br>
Resizing the data to: 15 256 256 256<br>
Computing the baseline image<br>
Dividing the signal by baseline image<br>
Converting the world coordinate system to RAS<br>
Data normalization finished!</li>
</ul>
<p>Using 2-tensor simple model.<br>
Branching disabled</p>
<p>Using unconstrained filter<br>
<strong>error: [<a href="http://slicer.org/Extensions-32438/UKFTractography/lib/Slicer-5.6/cli-modules/./UKFTractography" rel="noopener nofollow ugc">slicer.org/Extensions-32438/UKFTractography/lib/Slicer-5.6/cli-modules/./UKFTractography</a>] exit abnormally - Report the problem.</strong><br>
what exactly is the problem?</p>

---
