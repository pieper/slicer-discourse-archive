# Load vol file into 3D Slicer from Morita machine

**Topic ID**: 4815
**Date**: 2018-11-20
**URL**: https://discourse.slicer.org/t/load-vol-file-into-3d-slicer-from-morita-machine/4815

---

## Post #1 by @sgbq (2018-11-20 14:44 UTC)

<p>Hi,</p>
<p>I have a volume file named *.vol from Morita machine. I am trying to convert it into a stl or obj file. It is not supported to be loaded by 3D Slicer right now. Is there any extension available? Or any other way to do it like a matlab script? Thanks in advance.</p>

---

## Post #2 by @lassoan (2018-11-20 15:37 UTC)

<p>Is there an option to export the volume in DICOM format?<br>
Can you share an example .vol file?</p>

---

## Post #3 by @sgbq (2018-11-20 15:59 UTC)

<p>Hi Andras,</p>
<p>Thanks for your reply. The .vol file can be only opened by a software named OneVolumeViewer form Morita. I have uploaded the .vol file and the software.</p>
<p><a href="https://drive.google.com/open?id=1iABWN3jzvWv7PNrMhFKZhQRxD9KyGqgV" rel="noopener nofollow ugc">https://drive.google.com/open?id=1iABWN3jzvWv7PNrMhFKZhQRxD9KyGqgV</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/677f06bdf711468707faf594c72c7993f90d2513.png" data-download-href="/uploads/short-url/eLzkAGZovUCazoJL65K1uagmWFJ.png?dl=1" title="77C3A3DB5AF54B56A741600A3E5A8000.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/677f06bdf711468707faf594c72c7993f90d2513.png" width="690" height="0" data-dominant-color="BFCDDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">77C3A3DB5AF54B56A741600A3E5A8000.png</span><span class="informations">708×1 83 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @pieper (2018-11-20 16:35 UTC)

<p>I’m not sure it’s the same file type (.vol may be an overused file extension) but here’s some code to read a .vol file from a microCT machine:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/pieper/CaseHub/blob/master/BenchtopNeuro/BenchtopNeuro.py#L378-L460" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/CaseHub/blob/master/BenchtopNeuro/BenchtopNeuro.py#L378-L460" target="_blank">pieper/CaseHub/blob/master/BenchtopNeuro/BenchtopNeuro.py#L378-L460</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="378" style="counter-reset: li-counter 377 ;">
<li>def volumeNodeFromVolArray(self, volArray, shape, vtkDataType, dimensions, volName, spacing):</li>
<li>
</li>
<li>  volArray = volArray.reshape(shape)</li>
<li>
</li>
<li>  # make a vtkImage data of the vol data</li>
<li>  image = vtk.vtkImageData()</li>
<li>  image.SetDimensions(dimensions)</li>
<li>  image.AllocateScalars(vtk.VTK_FLOAT, 1)</li>
<li>  imageArray = vtk.util.numpy_support.vtk_to_numpy(image.GetPointData().GetScalars()).reshape(shape)</li>
<li>  imageArray[:] = volArray</li>
<li>
</li>
<li>  # make a slicer volume node for the image</li>
<li>  volumeNode = slicer.vtkMRMLScalarVolumeNode()</li>
<li>  volumeNode.SetName(volName)</li>
<li>  volumeNode.SetSpacing(*spacing)</li>
<li>  volumeNode.SetAndObserveImageData(image)</li>
<li>  slicer.mrmlScene.AddNode(volumeNode)</li>
<li>  volumeNode.CreateDefaultDisplayNodes()</li>
<li>
</li>
<li>  # make this volume visible</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/pieper/CaseHub/blob/master/BenchtopNeuro/BenchtopNeuro.py#L378-L460" target="_blank">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @lassoan (2018-11-20 18:23 UTC)

<p>This .vol file has a human-readable header. From that you can determine image geometry (size, spacing, origin) and write it to a header file. You can then open that file in Slicer.</p>
<p>For example, here is the header for the file you shared:</p>
<pre><code>NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: short
dimension: 3
space: left-posterior-superior
sizes: 504 501 500
space directions: (0.08,0,0) (0,0.08,0) (0,0,0.08)
kinds: domain domain domain
endian: little
encoding: raw
space origin: (0,0,0)
byte skip: 800
data file: CT_0.vol
</code></pre>
<p>If you save the content above to a file named <code>CT_0.nhdr</code> (or download it from <a href="https://1drv.ms/u/s!Arm_AFxB9yqHtfcHIxikIM53PUb0zQ">here</a>) then you can open that file in Slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b8b7862f6801389f563d1792c036b7a485c1d48.jpeg" data-download-href="/uploads/short-url/flnTZ6iG9tyG1cxvY6cPLCp27tC.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b8b7862f6801389f563d1792c036b7a485c1d48_2_690x420.jpeg" alt="image" data-base62-sha1="flnTZ6iG9tyG1cxvY6cPLCp27tC" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b8b7862f6801389f563d1792c036b7a485c1d48_2_690x420.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b8b7862f6801389f563d1792c036b7a485c1d48_2_1035x630.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b8b7862f6801389f563d1792c036b7a485c1d48_2_1380x840.jpeg 2x" data-dominant-color="ACABAC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2256×1374 553 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @sgbq (2018-11-20 21:37 UTC)

<p>Hi Andras,</p>
<p>This really helps! I do appreciate it.</p>

---

## Post #7 by @sgbq (2018-11-21 19:18 UTC)

<p>Hi Andras,</p>
<p>I have successfully loaded the vol file, but the rendering result is different from yours. (It looks incorrectly) Is there any steps before volume rendering? Thanks for your help.</p>

---

## Post #8 by @lassoan (2018-11-21 19:24 UTC)

<p>Voxels values of the scan are uncalibrated, it is not in Hounsfield units but in tens of thousands range. So, you need to adjust the transfer functions accordingly (you need to open Advanced section and drag points outside the current default range, which are specified for Hounsfield units).</p>

---

## Post #9 by @sgbq (2018-11-26 15:33 UTC)

<p>Hi Andras,</p>
<p>Here is my result. I was trying but failed to achieve the result similar to yours.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/5600b8f29f4e9fa4e58a356512433f69cba53e9b.png" data-download-href="/uploads/short-url/cgOBQ0NZsAPaQFWHjhfUwDKqPQ7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5600b8f29f4e9fa4e58a356512433f69cba53e9b_2_690x366.png" alt="image" data-base62-sha1="cgOBQ0NZsAPaQFWHjhfUwDKqPQ7" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5600b8f29f4e9fa4e58a356512433f69cba53e9b_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5600b8f29f4e9fa4e58a356512433f69cba53e9b_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/6/5600b8f29f4e9fa4e58a356512433f69cba53e9b_2_1380x732.png 2x" data-dominant-color="96949A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1020 397 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Could you tell the details what configuration you were using for the above one you posted? Screenshots are the best if you could attach. Thank you for your time and effort.</p>

---

## Post #10 by @sgbq (2018-11-27 12:36 UTC)

<p>Hi,</p>
<p>I am confusing about the Hounsfield units. I watched several tutorals but they skip the step. Where and how can I modify this Hounsfield units or transfer functions configuration? Thanks for the help.</p>

---

## Post #11 by @lassoan (2018-11-27 13:53 UTC)

<p>I had to tune the transfer functions, which were not easy, because the points were way out of normal CT range. I would recommend to rescale voxel intensities using SimpleFilters module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5a4e512042bf7a54cf3579c71785ef3dad5e26d.png" data-download-href="/uploads/short-url/pUTHSbpuVfUVVGjegBrSyCdCNu5.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/5/b5a4e512042bf7a54cf3579c71785ef3dad5e26d.png" alt="image" data-base62-sha1="pUTHSbpuVfUVVGjegBrSyCdCNu5" width="685" height="500" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">994×725 28.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After this you can use built-in volume rendering presets, such as “CT-AAA2” or “CT-Cardiac3”, and move “Shift” slider to fine-tune what is displayed.</p>

---

## Post #12 by @Tijl (2023-05-05 21:38 UTC)

<p>I have the same kind of problem importing data from a cbct volume from a morita cbct machine</p>
<p>This is the header from the file<br>
I dont know how to proceed or what to do.</p>
<pre><code class="lang-auto">   JmVolumeVersion=1Ú  &lt;?xml version='1.0' encoding='Shift_JIS' ?&gt;&lt;JmVolume&gt;&lt;Version value="1"/&gt;&lt;Attribute&gt;&lt;tfStatRadius value="40"/&gt;&lt;tfStatZMax value="17.5"/&gt;&lt;tfStatZMin value="-17.5"/&gt;&lt;tfStatSkipLength value="0.5"/&gt;&lt;tfStatSideLength value="2"/&gt;&lt;tfStatIntervalLength value="2"/&gt;&lt;tfXGridSize value="0.25"/&gt;&lt;tfYGridSize value="0.25"/&gt;&lt;tfZGridSize value="0.25"/&gt;&lt;tfXLen value="100"/&gt;&lt;tfYLen value="100"/&gt;&lt;tfZLen value="50"/&gt;&lt;strVolumeId value="0"/&gt;&lt;tfInitialAngleInRadian value="2.26893"/&gt;&lt;tfA value="0.00492927"/&gt;&lt;tfB value="88.7966"/&gt;&lt;tfXCenter value="0"/&gt;&lt;tfYCenter value="0"/&gt;&lt;tfZCenter value="0"/&gt;&lt;iZMaxValid value="2147483647" FYI="2147483647 denotes uninitialized"/&gt;&lt;iZMinValid value="2147483647" FYI="2147483647 denotes uninisizlized"/&gt;&lt;strGuidsFromRootToThis value="{328CBBC4-3E54-4035-A6AF-6919B90EE07D}"/&gt;&lt;STITCHID value=""/&gt;&lt;STITCHNUMBER value=""/&gt;&lt;STITCHCENTER value=""/&gt;&lt;tfAntiAliasAngleInRadian value="0" FYI="This node is obsolete. See tfAntiAliasAngleInDegree instead"/&gt;&lt;tfAntiAliasAngleInDegree value="45"/&gt;&lt;tfSliceInterval value="0"/&gt;&lt;tfSliceThickness value="0"/&gt;&lt;iSliceMeanRange value="0"/&gt;&lt;tfSystemV2HuSlope value="190"/&gt;&lt;tfSystemV2HuIntercept value="0"/&gt;&lt;tfUserV2HuSlope value="+1.0000000000000000e+000"/&gt;&lt;tfUserV2HuIntercept value="+0.0000000000000000e+000"/&gt;&lt;bIsHuAvailable value="0"/&gt;&lt;bIsUserDefinedV2Hu value="0"/&gt;&lt;CAdditionalVolumeInfo&gt;&lt;bIsValid value="1"/&gt;&lt;strReconstructionFilterId value="G_001"/&gt;&lt;strAcquisitionModeId value="MCT1F17_V01_SL2_W100xH50_FR30_PR17"/&gt;&lt;tfmaTubeCurrent value="5"/&gt;&lt;tfkvTubeVoltage value="90"/&gt;&lt;/CAdditionalVolumeInfo&gt;&lt;/Attribute&gt;&lt;FYI&gt;&lt;XMin value="-200"/&gt;&lt;XMax value="200"/&gt;&lt;YMin value="-200"/&gt;&lt;YMax value="200"/&gt;&lt;ZMin value="-102"/&gt;&lt;ZMax value="101"/&gt;&lt;MinValue value="-72.7257"/&gt;&lt;MaxValue value="250.314"/&gt;&lt;/FYI&gt;&lt;/JmVolume&gt;   CArray3D8ÿÿÿÈ   8ÿÿÿÈ   šÿÿÿe
</code></pre>

---

## Post #13 by @arabikatiby (2023-10-21 14:36 UTC)

<p>how did you get the header</p>

---

## Post #14 by @cepcep (2023-10-24 17:22 UTC)

<p>Hi Andras. Please tell me, I don’t understand how you saw that data in this data? I looked in his file CT_0.vol, there is the following information:<br>
   JmVolumeVersion=1╙  &lt;?xml version='1.0' encoding='Shift_JIS' ?&gt;   CArray3D   ·      ·</p>
<p>For example, it doesn’t have sizes: 504 501 500<br>
And many other.</p>
<p>Please Andras <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=12" title=":pray:" class="emoji" alt=":pray:" loading="lazy" width="20" height="20"> teach me to see these numbers.</p>

---

## Post #15 by @Alexander_Shiryaev (2025-12-01 05:06 UTC)

<h1><a name="p-130244-instruction-to-create-nhdr-file-1" class="anchor" href="#p-130244-instruction-to-create-nhdr-file-1" aria-label="Heading link"></a>Instruction to Create <code>.nhdr</code> file</h1>
<p>Use the following template for your <code>.nhdr</code> file:</p>
<pre><code class="lang-auto">NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: signed short
dimension: 3
space: left-posterior-superior
sizes: Z Y X
space directions: (0,0,S) (S,0,0) (0,S,0)
kinds: domain domain domain
endian: little
encoding: raw
space origin: (0,0,0)
byte skip: B
data file: CT_0.vol
</code></pre>
<p>You need to fill values from your <code>.vol</code> header:<br>
<code>X</code>, <code>Y</code>, <code>Z</code>, <code>S</code>, <code>B</code></p>
<h2><a name="p-130244-voxel-size-s-2" class="anchor" href="#p-130244-voxel-size-s-2" aria-label="Heading link"></a>Voxel size (<code>S</code>)</h2>
<p>Look for the grid size in the <code>.vol</code> XML header, e.g.:</p>
<pre data-code-wrap="xml"><code class="lang-xml">&lt;tfXGridSize value="0.125"/&gt;
&lt;tfYGridSize value="0.125"/&gt;
&lt;tfZGridSize value="0.125"/&gt;
</code></pre>
<p>⇒ <code>S</code> = 0.125</p>
<h2><a name="p-130244-dimensions-x-y-z-3" class="anchor" href="#p-130244-dimensions-x-y-z-3" aria-label="Heading link"></a>Dimensions (<code>X</code>, <code>Y</code>, <code>Z</code>)</h2>
<p>Check the minimum and maximum indices:</p>
<pre data-code-wrap="xml"><code class="lang-xml">&lt;FYI&gt;
  &lt;XMin value="-352"/&gt;
  &lt;XMax value="352"/&gt;
  &lt;YMin value="-352"/&gt;
  &lt;YMax value="352"/&gt;
  &lt;ZMin value="-162"/&gt;
  &lt;ZMax value="161"/&gt;
  ..
&lt;/FYI&gt;
</code></pre>
<p><code>X</code> = <code>XMax</code> - <code>XMin</code> + 1 = 352 - (-352) + 1 = 705<br>
<code>Y</code> = <code>YMax</code> - <code>YMin</code> + 1 = 352 - (-352) + 1 = 705<br>
<code>Z</code> = <code>ZMax</code> - <code>ZMin</code> + 1 = 161 - (-162) + 1 = 324</p>
<h2><a name="p-130244-byte-skip-b-4" class="anchor" href="#p-130244-byte-skip-b-4" aria-label="Heading link"></a>Byte skip (<code>B</code>)</h2>
<p>total voxels = <code>X</code> * <code>Y</code> * <code>Z</code> = 161036100<br>
voxel size = 2 bytes (because data type in <code>.vol</code> is 16-bit integer)<br>
raw data size = total voxels * voxel size = 322072200 (bytes)</p>
<p>Raw data located at the very end of the <code>.vol</code> file, so the byte skip parameter can be calculated as:<br>
<code>B</code> = total <code>.vol</code> file size - raw data size</p>
<h2><a name="p-130244-adjust-axes-if-necessary-5" class="anchor" href="#p-130244-adjust-axes-if-necessary-5" aria-label="Heading link"></a>Adjust axes (if necessary)</h2>
<p>If after import the axes look incorrect, modify the <code>space directions</code> line, for example:</p>
<pre><code class="lang-auto">space directions: (S,0,0) (0,S,0) (0,0,S)
</code></pre>
<p>Test different permutations until the orientation matches your viewer.</p>
<h2><a name="p-130244-data-type-consideration-6" class="anchor" href="#p-130244-data-type-consideration-6" aria-label="Heading link"></a>Data type consideration</h2>
<p>Use <code>signed short</code> data type, not <code>unsigned short</code>, because in your <code>.vol</code>:</p>
<ul>
<li><code>0x8000</code> value corresponds to <em>void</em></li>
<li>and all other values correspond to actual intensities</li>
</ul>
<h2><a name="p-130244-python-parser-for-reference-7" class="anchor" href="#p-130244-python-parser-for-reference-7" aria-label="Heading link"></a>Python parser for reference</h2>
<pre data-code-wrap="py"><code class="lang-py">import struct, tempfile, subprocess
import numpy as np

def load_data (path: str, dtype = np.int16, extract_header: bool = False) -&gt; np.ndarray:
    with open(path, 'rb') as f:
        n = struct.unpack("&lt;I", f.read(4))[0]
        data = f.read(n)
        assert data.decode('ascii') == "JmVolumeVersion=1"

        # XML
        n = struct.unpack("&lt;I", f.read(4))[0]
        data = f.read(n)
        if extract_header:
            with tempfile.NamedTemporaryFile() as fht:
                fht.write(data)
                fht.flush()
                subprocess.run(["xmllint", "--format", "--output", path + ".header.xml", fht.name])

        n = struct.unpack("&lt;I", f.read(4))[0]
        data = f.read(n)
        assert data.decode('ascii') == "CArray3D"

        # X limits
        x_min, x_max = struct.unpack("&lt;ii", f.read(8))
        X = x_max - x_min + 1

        # Y limits
        y_min, y_max = struct.unpack("&lt;ii", f.read(8))
        Y = y_max - y_min + 1

        # Z limits
        z_min, z_max = struct.unpack("&lt;ii", f.read(8))
        Z = z_max - z_min + 1

        print(f"X={X} Y={Y} Z={Z}")

        # voxels
        d = np.frombuffer(f.read(), dtype=dtype)
        print(len(d))
        assert len(d) == X * Y * Z
        d = d.reshape((X, Y, Z))
        return d
</code></pre>

---

## Post #16 by @Alexander_Shiryaev (2025-12-04 01:19 UTC)

<p>I’ve created a small Python utility called <a href="https://github.com/aixp/vol2nrrd" rel="noopener nofollow ugc"><strong>vol2nrrd</strong> </a> that converts 3D Morita <code>.vol</code> medical imaging files into NRRD (<code>.nrrd</code>/<code>.nhdr</code>) format.</p>

---
