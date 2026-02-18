# New feature: Support of 5D images and transforms

**Topic ID**: 45588
**Date**: 2025-12-23
**URL**: https://discourse.slicer.org/t/new-feature-support-of-5d-images-and-transforms/45588

---

## Post #1 by @lassoan (2025-12-23 06:21 UTC)

<p>3D Slicer has expanded its capabilities to support reading and writing images, image sequences, and transform sequences with dimensionality up to 5D. This is a significant enhancement that enables users to work with larger and more complex imaging data, and do it more efficiently.</p>
<p>The following data types can now be stored in NRRD file format and loaded into Slicer for visualization and analysis:</p>
<ul>
<li><strong>3D</strong>
<ul>
<li>Volumetric image (xyz)</li>
<li>2D image time sequence (xyt)</li>
<li>2D color image (cxy)</li>
</ul>
</li>
<li><strong>4D</strong>
<ul>
<li>Color volumetric image (cxyz) - for example cryosection images (such as the visible human data set) or multichannel/multimodal images (such as B-mode + Color Doppler)</li>
<li>Displacement fields (vxyz) - warping transforms</li>
<li>Flow fields (vxyz) - such as 4D flow MRI</li>
<li>Sequence of volumetric images (xyzt) - commonly used in cardiac echo, CT, MR or dynamic imaging <img src="https://emoji.discourse-cdn.com/twitter/new_button.png?v=15" title=":new_button:" class="emoji" alt=":new_button:" loading="lazy" width="20" height="20"></li>
<li>Sequence of 2D color images (cxyt) - color video recording <img src="https://emoji.discourse-cdn.com/twitter/new_button.png?v=15" title=":new_button:" class="emoji" alt=":new_button:" loading="lazy" width="20" height="20"></li>
</ul>
</li>
<li><strong>5D</strong>
<ul>
<li>Sequence of color volumetric images (cxyzt) <img src="https://emoji.discourse-cdn.com/twitter/new_button.png?v=15" title=":new_button:" class="emoji" alt=":new_button:" loading="lazy" width="20" height="20"></li>
<li>Sequence of displacement fields (vxyzt) - sequence registration results <img src="https://emoji.discourse-cdn.com/twitter/new_button.png?v=15" title=":new_button:" class="emoji" alt=":new_button:" loading="lazy" width="20" height="20"></li>
<li>Sequence of flow fields (vxyzt) - such as sequence of 4D flow MRI images <img src="https://emoji.discourse-cdn.com/twitter/new_button.png?v=15" title=":new_button:" class="emoji" alt=":new_button:" loading="lazy" width="20" height="20"></li>
</ul>
</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f4dde5d4f9a8ae0f79e10deed701ccf43e813974.png" data-download-href="/uploads/short-url/yWbUPnIExo0qJJnX2yrDtv7pWRK.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4dde5d4f9a8ae0f79e10deed701ccf43e813974_2_690x334.png" alt="image" data-base62-sha1="yWbUPnIExo0qJJnX2yrDtv7pWRK" width="690" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4dde5d4f9a8ae0f79e10deed701ccf43e813974_2_690x334.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4dde5d4f9a8ae0f79e10deed701ccf43e813974_2_1035x501.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4dde5d4f9a8ae0f79e10deed701ccf43e813974_2_1380x668.png 2x" data-dominant-color="F6F5F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2640×1281 230 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h2><a name="p-130864-new-use-cases-1" class="anchor" href="#p-130864-new-use-cases-1" aria-label="Heading link"></a>New use cases</h2>
<p>The following use cases are enabled by these new developments.</p>
<h3><a name="p-130864-efficient-storage-of-deformable-image-sequence-registration-results-2" class="anchor" href="#p-130864-efficient-storage-of-deformable-image-sequence-registration-results-2" aria-label="Heading link"></a>Efficient storage of deformable image sequence registration results</h3>
<p>Modules such as “Sequence Registration” have been available for motion tracking or motion compensation in 3D image sequences. However, after they computed a deformable transformation sequence, the only option to store it was a zip file containing several displacement field files. This was very inflexible and inefficient, as it was not possible to access a random item in the sequence and files were large.</p>
<p>In the current version of 3D Slicer, 4D displacement fields are stored by default as a single standard 5D NRRD file. The file can be saved as uncompressed raw data for fastest access; or compressed for maximum storage space efficiency.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa6d48ee9e66a750bcf30b0fcd66401553373f38.jpeg" data-download-href="/uploads/short-url/zJnvAb0LJMVdx23LH30nU3ywXNK.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa6d48ee9e66a750bcf30b0fcd66401553373f38_2_690x174.jpeg" alt="image" data-base62-sha1="zJnvAb0LJMVdx23LH30nU3ywXNK" width="690" height="174" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa6d48ee9e66a750bcf30b0fcd66401553373f38_2_690x174.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa6d48ee9e66a750bcf30b0fcd66401553373f38_2_1035x261.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa6d48ee9e66a750bcf30b0fcd66401553373f38_2_1380x348.jpeg 2x" data-dominant-color="565950"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×486 357 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3><a name="p-130864-h-4d-flow-mri-3" class="anchor" href="#p-130864-h-4d-flow-mri-3" aria-label="Heading link"></a>4D flow MRI</h3>
<p>Some recent MRI systems allow real-time recording of 4D+t flow images, which store a 3D velocity vector at each voxel position, for tens of timepoints in the cardiac cycle. Previously, the only way to save such data sets was to save multiple 4D volumes in a zip file. These can now be saved as 5D vector field files.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e56b3b159e23a3d38acce85a17a0c99c752d0ce.jpeg" data-download-href="/uploads/short-url/4ko55I5DYs58eZ4VRMPHrDoK9xY.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e56b3b159e23a3d38acce85a17a0c99c752d0ce_2_690x358.jpeg" alt="image" data-base62-sha1="4ko55I5DYs58eZ4VRMPHrDoK9xY" width="690" height="358" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e56b3b159e23a3d38acce85a17a0c99c752d0ce_2_690x358.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e56b3b159e23a3d38acce85a17a0c99c752d0ce_2_1035x537.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/e/1e56b3b159e23a3d38acce85a17a0c99c752d0ce_2_1380x716.jpeg 2x" data-dominant-color="49524C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1468×762 350 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3><a name="p-130864-color-video-storage-4" class="anchor" href="#p-130864-color-video-storage-4" aria-label="Heading link"></a>Color video storage</h3>
<p>3D Slicer has been supporting storage of color video recordings, but only at certain resolutions and only in 2D. The new infrastructure allows color images and image sequences to be stored efficiently in a single 5D image file.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32b794a8e380f31ff40f8765605c40eb69a13c36.jpeg" data-download-href="/uploads/short-url/7eFbZhIFHB65gTH95DKYwP4ajm6.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32b794a8e380f31ff40f8765605c40eb69a13c36_2_690x388.jpeg" alt="image" data-base62-sha1="7eFbZhIFHB65gTH95DKYwP4ajm6" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32b794a8e380f31ff40f8765605c40eb69a13c36_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/2/32b794a8e380f31ff40f8765605c40eb69a13c36_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/2/32b794a8e380f31ff40f8765605c40eb69a13c36.jpeg 2x" data-dominant-color="51616B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1280×720 92.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3><a name="p-130864-multi-modality-image-storage-5" class="anchor" href="#p-130864-multi-modality-image-storage-5" aria-label="Heading link"></a>Multi-modality image storage</h3>
<p>Cardiac ultrasound systems can acquire 3D B-mode ultrasound image time sequences, which were stored as 4D image volumes. Some systems can simultaneously acquire B-mode and Color Doppler (velocity) images. Since the resolution and field of view of these images are very similar, they can be robustly and efficiently displayed in 3D as a multi-component volumetric image. However, previously there was no way of storing a sequence of these fused multi-component volumetric images efficiently in one data file.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c969ee55a685e914cf07e6a4723dc072ecdab82c.jpeg" data-download-href="/uploads/short-url/sJMVvXwjvCvwPtTxZFYXecTzgFC.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c969ee55a685e914cf07e6a4723dc072ecdab82c_2_690x322.jpeg" alt="image" data-base62-sha1="sJMVvXwjvCvwPtTxZFYXecTzgFC" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c969ee55a685e914cf07e6a4723dc072ecdab82c_2_690x322.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c969ee55a685e914cf07e6a4723dc072ecdab82c_2_1035x483.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c969ee55a685e914cf07e6a4723dc072ecdab82c_2_1380x644.jpeg 2x" data-dominant-color="3B3828"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×896 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h2><a name="p-130864-usage-examples-6" class="anchor" href="#p-130864-usage-examples-6" aria-label="Heading link"></a>Usage examples</h2>
<h3><a name="p-130864-using-3d-slicer-7" class="anchor" href="#p-130864-using-3d-slicer-7" aria-label="Heading link"></a>Using 3D Slicer</h3>
<p>Slicer’s Python API makes it easy to load, manipulate, and save high-dimensional data.</p>
<p>Load any data type of any dimension (image, transform, image sequence, transform sequence):</p>
<pre><code class="lang-auto">node = slicer.util.loadNodeFromFile('path/to/file.nrrd')
</code></pre>
<p>Save any data type of any dimension (image, transform, image sequence, transform sequence):</p>
<pre><code class="lang-auto">slicer.util.saveNode(node, 'path/to/file.nrrd')
</code></pre>
<p>For sequences of images or transforms a common convention in Slicer is to use the composite file extension <code>.seq.nrrd</code>. This is not required by the data reader, but makes it easier for users to distinguish sequences from simple 3D files.</p>
<h3><a name="p-130864-using-itk-python-8" class="anchor" href="#p-130864-using-itk-python-8" aria-label="Heading link"></a>Using ITK Python</h3>
<p>The new features are available in ITK Python 6.x.</p>
<p>Read a 5D displacement field vector file:</p>
<pre><code class="lang-auto">filename = "path/to/file.nrrd"

import itk

nrrd_io = itk.NrrdImageIO.New()
nrrd_io.SetAxesReorderToUseNonListRangeAxisAsPixel()
nrrd_io.SetFileName(filename)
nrrd_io.ReadImageInformation()
PixelType = itk.Vector[itk.F, nrrd_io.GetNumberOfComponents()]
dimension = nrrd_io.GetNumberOfDimensions()
ImageType = itk.Image[PixelType, dimension]

reader = itk.ImageFileReader[ImageType].New()
reader.SetFileName(filename)
reader.SetImageIO(nrrd_io)
reader.Update()

image = reader.GetOutput()
print(image.shape)
print(meta["NRRD_kinds[pixel]"])
</code></pre>
<p>Write the displacement field vector to file:</p>
<pre><code class="lang-auto">filename = "path/to/file.nrrd"

nrrd_io = itk.NrrdImageIO.New()
writer = itk.ImageFileWriter[ImageType].New()
writer.SetFileName(filename)
writer.SetImageIO(nrrd_io)
writer.SetInput(image)
writer.Update()
</code></pre>
<h3><a name="p-130864-using-python-with-pynrrd-9" class="anchor" href="#p-130864-using-python-with-pynrrd-9" aria-label="Heading link"></a>Using Python with pynrrd</h3>
<p>Writing high-dimensional numpy arrays with correct metadata is fairly straightforward. Example for writing a time sequence of 3D volumes:</p>
<pre><code class="lang-auto">import numpy as np
import nrrd

img = np.zeros([201,201,201, 2])

header = {
    'space': 'left-posterior-superior',
    'kinds': ['domain', 'domain', 'domain', 'list'],
    'labels': ["", "", "", "time"],
    'units': ["", "", "", "s"],
    'space origin': [-137.16099548, -36.80649948, -309.71899414],
    'space directions': [[1.953125, 0., 0.], [0., 1.953125, 0.], [0., 0., 1.953125], [np.nan, np.nan, np.nan]],
    'axis 3 index type': 'numeric',
    'axis 3 index values': "1.2 1.4"
}

nrrd.write("c:/tmp/test.seq.nhdr", img, header)
</code></pre>
<p>The resulting image header:</p>
<pre><code class="lang-auto">NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: double
dimension: 4
space: left-posterior-superior
sizes: 201 201 201 2
space directions: (-1.9531249999999998,0,0) (0,-1.9531249999999998,0) (0,0,1.9531249999999998) none
kinds: domain domain domain list
labels: "" "" "" "time"
units: "" "" "" "s"
endian: little
encoding: gzip
space origin: (137.16099548000003,36.806499479999999,-309.71899414000001)
data file: test.seq.raw.gz
DataNodeClassName:=vtkMRMLScalarVolumeNode
axis 3 index type:=numeric
axis 3 index values:=1.2 1.4
</code></pre>
<h2><a name="p-130864-information-for-developers-10" class="anchor" href="#p-130864-information-for-developers-10" aria-label="Heading link"></a>Information for developers</h2>
<p>We chose NRRD file format for storage of 5D information, because this format provides standard fields for specifying the meaning of each axis, it is a very simple file format, and it allows storing any number of custom fields for describing any details of the data that cannot be captured by standard fields.</p>
<p>To make it easy to read/write these higher-dimension files correctly in a wide variety of software, not just in 3D Slicer, we decided to implement this functionality in the ITK toolkit. This allows any software that uses ITK to read/write such files without any custom development. All Python developers can use this implementation, too, since ITK is available as a Python package. It is feasible to use the file format for any software that cannot use ITK, as writing of valid 5D files is fairly straightforward; and reading of specific variants can be implemented with not too much effort.</p>
<h3><a name="p-130864-itk-c-implementation-11" class="anchor" href="#p-130864-itk-c-implementation-11" aria-label="Heading link"></a>ITK C++ implementation</h3>
<p>An ITK image can be an <code>Image</code> object that can store scalar, RGB, CovariantVector, etc. pixels in an arbitrarily high dimensional array. If the number of components of the pixel has to be dynamic then the ITK image has to be a <code>VectorImage</code> object that can store multi-component pixels in an arbitrarily high dimensional array.</p>
<p>NRRD file can contain domain (space, time) axes and range (list, RGB, covariant-vector, etc.) axes in an arbitrary order. Therefore, axes of the NRRD file may have to be reordered to be able to read the NRRD file into an ITK image. In general, NRRD domain axes are mapped to ITK image axes then all range axes are used as additional image dimensions. The only exception is that it makes sense to pick one range axis and use that as pixel component.</p>
<h4><a name="p-130864-file-reading-12" class="anchor" href="#p-130864-file-reading-12" aria-label="Heading link"></a>File Reading</h4>
<p>Previously, a rigid, arbitrary logic was used for mapping higher-dimensional array to ITK data type. Now NRRD IO allows having more than one non-spatial axis and a few different strategies are avaialable to map them to ITK image types via the new <code>AxesReorder</code> property in <code>NrrdImageIO</code>.<br>
The non-spatial axes of the NRRD file can be used in the ITK image as pixel components or as additional image dimensions.</p>
<p>The default strategy (<code>UseAnyRangeAxisAsPixel</code>) implements the same behavior as before (first non-spatial NRRD axis always becomes pixel component).<br>
If the NRRD file contains a non-list type (e.g., RGB, point, covariant-vector) range axis then the first one is used as pixel component; the image is read into an <code>Image</code> object. If the NRRD file only contains list-type range axis then it is used as pixel component; the image is read into a <code>VectorImage</code> object. However, this resulted in more complicated application code (developers had to instantiate an <code>Image</code> or <code>VectorImage</code> depending on what kind of axes are in the NRRD file) and potential unnecessary reordering of axes (e.g., sequence of 3D images was always converted into a single multi-component 3D image).</p>
<p>The new <code>UseNonListRangeAxisAsPixel</code> option allows “list” dimension (e.g., time points) to always mapped to additional image dimension.<br>
This new option simplifies application implementation, as time sequences are loaded the same way for scalar and vector volumes.</p>
<p>An additional <code>UseScalarPixel</code> option was introduced that is useful for cases when developers always want scalar pixel type. In this case, The image is always read into an ITK <code>Image</code> object, and all range (i.e., non-domain) axes of the NRRD file are added as additional domain axes.</p>
<p>Examples:</p>
<p>NRRD file with these axes kinds: <code>list domain domain domain RGB-Color</code> (or: <code>domain domain domain list RGB-Color</code>)</p>
<ul>
<li><code>UseAnyRangeAxisAsPixel</code>: <code>Image&lt;RGBPixel&lt;double&gt;,4&gt;</code> with axes: domain domain domain list</li>
<li><code>UseNonListRangeAxisAsPixel</code>: <code>Image&lt;RGBPixel&lt;double&gt;,4&gt;</code> with axes: domain domain domain list</li>
<li><code>UseScalarPixel</code>: <code>Image&lt;double,5&gt;</code> with axes: domain domain domain list RGB-Color</li>
</ul>
<p>NRRD file with these axes kinds: <code>list domain domain domain</code> (or: <code>domain domain domain list</code>)</p>
<ul>
<li><code>UseAnyRangeAxisAsPixel</code>: <code>VectorImage&lt;double,3&gt;</code> with axes: domain domain domain</li>
<li><code>UseNonListRangeAxisAsPixel</code>: <code>Image&lt;double,4&gt;</code> with axes: domain domain domain list</li>
<li><code>UseScalarPixel</code>: <code>Image&lt;double,4&gt;</code> with axes: domain domain domain list</li>
</ul>
<h4><a name="p-130864-file-writing-13" class="anchor" href="#p-130864-file-writing-13" aria-label="Heading link"></a>File writing</h4>
<p>Previously the NRRD writer handled one component axis, and all the other dimensions were space.<br>
Now it is possible to designate one of the axes as a list, by setting <code>NRRD_kinds[i]=list</code> metadata.</p>
<p>Example:</p>
<p>Previously, the file header for a 5D array was written as follows (4 domain axes):</p>
<pre><code class="lang-auto">  dimension: 5
  space dimension: 4
  sizes: 4 320 320 1 5
  space directions: none (1,0,0,0) (0,1,0,0) (0,0,1,0) (0,0,0,1)
  kinds: RGBA-color domain domain domain domain
  encoding: gzip
  space origin: (0,0,0,1)
</code></pre>
<p>We can now write a file header like this (with 3 domain axes + 1 list axis):</p>
<pre><code class="lang-auto">  dimension: 5
  space: left-posterior-superior
  sizes: 4 320 320 1 5
  space directions: none (-1,0,0) (0,-1,0) (0,0,1) none
  kinds: vector domain domain domain list
  encoding: gzip
  space origin: (0,0,0)
</code></pre>
<h4><a name="p-130864-axis-units-14" class="anchor" href="#p-130864-axis-units-14" aria-label="Heading link"></a>Axis units</h4>
<p>NRRD IO did not support the “units” metadata for axes, now it is added both for reading and writing.<br>
Per-axis metadata (kinds, labels, units) was only saved for spatial axes, now it is added for all axes.<br>
For pixel components, <code>pixel</code> is used instead of axis index (<code>NRRD_labels[pixel]</code> and <code>NRRD_units[pixel]</code> fields).</p>
<h4><a name="p-130864-transforms-15" class="anchor" href="#p-130864-transforms-15" aria-label="Heading link"></a>Transforms</h4>
<p>If only standard NRRD file fields are used, then displacement fields may not be distinguishable from other kind of vector fields.<br>
To give a hint to applications that a NRRD file is intended to be used as a displacement field, the custom <code>intent_code</code> field is set to the value of <code>1006</code>. This field and enumerated value comes from NIFTI file format specification. It simplifies applications that may read displacement fields from either NRRD or NIFTI formats.</p>
<h3><a name="p-130864-implementation-in-slicer-16" class="anchor" href="#p-130864-implementation-in-slicer-16" aria-label="Heading link"></a>Implementation in Slicer</h3>
<p>The ITK classes described above are used in 3D Slicer in volume and transform storage nodes. Since 3D Slicer uses VTK pipelines, a new pair of classes, <code>vtkITKImageSequenceReader</code> and <code>vtkITKImageSequenceWriter</code> were implemented to wrap the ITK classes in a VTK interface. These classes are used in <code>vtkMRMLVolumeSequenceStorageNode</code> and <code>vtkMRMLTransformSequenceStorageNode</code> for image and transform storage.</p>
<h2><a name="p-130864-acknowledgments-17" class="anchor" href="#p-130864-acknowledgments-17" aria-label="Heading link"></a>Acknowledgments</h2>
<p>This work has been funded in part by CHOP Frontier Program - Children’s Hospital of Philadelphia Frontier Programs conduct visionary research that translates to cutting-edge care; Additional Ventures 993932 - Computational Modelling of the Atrioventricular Valve Repair Single Ventricle Patients with Atrioventricular Canal, and NIH 1R01HL153166-01 - Computer Modeling of the Tricuspid Valve in Hypoplastic Left Heart Syndrome (PI: Matthew Jolley) driven by the <a href="https://slicerheart.org/">SlicerHeart project</a>.</p>

---

## Post #2 by @rkikinis (2025-12-23 11:46 UTC)

<p>Hi,<br>
This is super cool. Thanks for doing this work.<br>
Is there a post on LinkedIn about this feature?<br>
How will this infrastructure work with diffusion MRI?<br>
Congratulations on this important progress.<br>
Ron</p>

---

## Post #3 by @mattjolley (2025-12-23 15:22 UTC)

<p>Yes.  We are incredibly thankful for the foundational contributions of the SlicerHeart development team including Andras Lasso, Csaba Pinter, Kyle Sunderland, and Christian Herz.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://www.linkedin.com/feed/update/urn:li:activity:7409250409602519041">
  <header class="source">
      <img src="https://static.licdn.com/aero-v1/sc/h/al2o9zrvru7aqj8e1x2rzsrca" class="site-icon" alt="" width="64" height="64">

      <a href="https://www.linkedin.com/feed/update/urn:li:activity:7409250409602519041" target="_blank" rel="noopener nofollow ugc">linkedin.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/388;"><img src="https://dms.licdn.com/playlist/vid/v2/D4E05AQFJcPVxnFRLSg/thumbnail-with-play-button-overlay-high/B4EZtLx8CWIgDU-/0/1766502948479?e=2147483647&amp;v=beta&amp;t=ciwAX40URKmr_7fBY5dS24s5z-zroub6Euc4sga4AbA" class="thumbnail" alt="" width="690" height="388"></div>

<h3><a href="https://www.linkedin.com/feed/update/urn:li:activity:7409250409602519041" target="_blank" rel="noopener nofollow ugc">The SlicerHeart(www.slicerheart.org) development team has significantly...</a></h3>

  <p>The SlicerHeart(www.slicerheart.org) development team has significantly expanded the core capabilities of 3D Slicer(www.slicer.org), enabling robust reading and writing of image and transform sequences with dimensionality up to 5D—including support...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
