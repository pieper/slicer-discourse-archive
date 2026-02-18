# Only black slices upon importing nrrd from 3DSlicer

**Topic ID**: 7400
**Date**: 2019-07-03
**URL**: https://discourse.slicer.org/t/only-black-slices-upon-importing-nrrd-from-3dslicer/7400

---

## Post #1 by @6ramr (2019-07-03 16:48 UTC)

<p>Hello there,</p>
<p>For a project I need to disassamble a nrrd-stack to separate tifs. I tried to accomplish this using Fiji (ImageJ2). Upon the import of said nrrd showing the segmenation-mask of tissue generated with 3DSlicer, I get a stack of all-black slices. The problem persists with other nrrds from the same project.</p>
<p>Importing <a href="http://teem.sourceforge.net/nrrd/files/foolc.nrrd" rel="nofollow noopener">foolc.nrrd</a> gives a 3-pixel-wide gray-scale stack, which viewed orthogonally depicts a person. So I guess this is a 3DSlicer specific issue.</p>
<p>Thanks in advance for any help!</p>

---

## Post #2 by @lassoan (2019-07-03 17:05 UTC)

<p>I don’t see any issue here. You provided a 3D volume (all dimensions are spatial) and Slicer loaded it as a 3D volume.</p>
<p>If you want to load it as an RGB image then you need to specify the number and kind of dimensions accordingly:</p>
<pre><code>NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: unsigned char
dimension: 4
space: left-posterior-superior
sizes: 3 128 128 1
space directions: none (1,0,0) (0,1,0) (0,0,1)
kinds: vector domain domain domain
encoding: gzip
space origin: (0,0,0)
data file: foolc.raw.gz
</code></pre>
<p>Note that you can directly load TIFF files to Slicer (single file or entire stack) - see <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ#How_to_load_data_from_a_sequence_of_jpg.2C_tif.2C_or_png_files.3F" rel="nofollow noopener">here</a>.</p>

---

## Post #3 by @6ramr (2019-07-03 17:18 UTC)

<p>SOLVED: I had to change the Look-Up-Table to 3-3-2 RGB.</p>

---
