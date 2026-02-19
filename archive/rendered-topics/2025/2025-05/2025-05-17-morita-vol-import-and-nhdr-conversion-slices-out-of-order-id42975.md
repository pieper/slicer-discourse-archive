---
topic_id: 42975
title: "Morita Vol Import And Nhdr Conversion Slices Out Of Order"
date: 2025-05-17
url: https://discourse.slicer.org/t/42975
---

# Morita .Vol import and nhdr conversion - slices out of order

**Topic ID**: 42975
**Date**: 2025-05-17
**URL**: https://discourse.slicer.org/t/morita-vol-import-and-nhdr-conversion-slices-out-of-order/42975

---

## Post #1 by @ChrisMak (2025-05-17 02:09 UTC)

<p>Hello!</p>
<p>I am trying to import Morita .vol files into slicer, but I am getting out of order slices.<br>
I have followed the instructions found here as best as i can</p><aside class="quote" data-post="1" data-topic="4815">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sgbq/48/80231_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/load-vol-file-into-3d-slicer-from-morita-machine/4815">Load vol file into 3D Slicer from Morita machine</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hi, 
I have a volume file named *.vol from Morita machine. I am trying to convert it into a stl or obj file. It is not supported to be loaded by 3D Slicer right now. Is there any extension available? Or any other way to do it like a matlab script? Thanks in advance.
  </blockquote>
</aside>

<p>Could somebody help me troubleshoot this?</p>
<p>problem - this slice has a part of it moved over left to right<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b652eedc24ffd089265230947bbeb2ef40a3159.jpeg" data-download-href="/uploads/short-url/d2wevK5myB1sEzHGkBscOkBf7L3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b652eedc24ffd089265230947bbeb2ef40a3159_2_503x500.jpeg" alt="image" data-base62-sha1="d2wevK5myB1sEzHGkBscOkBf7L3" width="503" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b652eedc24ffd089265230947bbeb2ef40a3159_2_503x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b652eedc24ffd089265230947bbeb2ef40a3159.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b652eedc24ffd089265230947bbeb2ef40a3159.jpeg 2x" data-dominant-color="60635F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">652×647 59.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>problem - this slice looks ok but it should be in the middle of the order, not the first<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d43638b1fa65097e24738f93114e9add0875faaa.jpeg" data-download-href="/uploads/short-url/uhjoluXQQUh2tehaHuV5PPBHBOy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d43638b1fa65097e24738f93114e9add0875faaa_2_534x500.jpeg" alt="image" data-base62-sha1="uhjoluXQQUh2tehaHuV5PPBHBOy" width="534" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/4/d43638b1fa65097e24738f93114e9add0875faaa_2_534x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d43638b1fa65097e24738f93114e9add0875faaa.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d43638b1fa65097e24738f93114e9add0875faaa.jpeg 2x" data-dominant-color="595855"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">708×662 63.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am pasting my original header and the nhdr I wrote. Btw why is the Z axis first in the “sizes” property?</p>
<p>OG Header</p>
<pre><code class="lang-auto">&lt;JmVolume&gt;&lt;Version value="1"/&gt;
&lt;Attribute&gt;
&lt;tfStatRadius value="20"/&gt;
&lt;tfStatZMax value="20"/&gt;
&lt;tfStatZMin value="-20"/&gt;
&lt;tfStatSkipLength value="0.5"/&gt;
&lt;tfStatSideLength value="2"/&gt;
&lt;tfStatIntervalLength value="2"/&gt;
&lt;tfXGridSize value="0.125"/&gt;
&lt;tfYGridSize value="0.125"/&gt;
&lt;tfZGridSize value="0.125"/&gt;
&lt;tfXLen value="60"/&gt;
&lt;tfYLen value="60"/&gt;
&lt;tfZLen value="60"/&gt;
&lt;strVolumeId value="0"/&gt;
&lt;tfInitialAngleInRadian value="2.26893"/&gt;
&lt;tfA value="0.00291905"/&gt;
&lt;tfB value="57.86"/&gt;
&lt;tfXCenter value="0"/&gt;
&lt;tfYCenter value="0"/&gt;
&lt;tfZCenter value="0"/&gt;
&lt;iZMaxValid value="2147483647"/&gt;
&lt;iZMinValid value="2147483647"/&gt;
&lt;tfAntiAliasAngleInRadian value="0"/&gt;
&lt;tfAntiAliasAngleInDegree value="45"/&gt;
&lt;tfSliceInterval value="0"/&gt;
&lt;tfSliceThickness value="0"/&gt;
&lt;iSliceMeanRange value="0"/&gt;
&lt;/Attribute&gt;&lt;FYI&gt;
&lt;XMin value="-240"/&gt;
&lt;XMax value="240"/&gt;
&lt;YMin value="-240"/&gt;
&lt;YMax value="240"/&gt;
&lt;ZMin value="-242"/&gt;
&lt;ZMax value="241"/&gt;
&lt;MinValue value="-37.7915"/&gt;
&lt;MaxValue value="153.509"/&gt;
&lt;/FYI&gt;
&lt;/JmVolume&gt;
</code></pre>
<p>my nhdr</p>
<pre><code class="lang-auto">NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: short
dimension: 3
space: left-posterior-superior
sizes: 484 481 481
space directions: (0.125,0,0) (0,0.125,0) (0,0,0.125)
kinds: domain domain domain
endian: little
encoding: raw
#space origin: (0,0,0)
#space origin: (-30.0, -30.0, -30.1875)
byte skip: 800
data file: CT_0.vol
</code></pre>

---

## Post #3 by @ChrisMak (2025-05-19 00:06 UTC)

<p>After some thought, the only problem I see is the Z axis wraparound. In total there are 484 layers. Instead of starting at layer 1, it starts at layer 444, goes up to 484 and then comes back at 1.<br>
I tried exporting it as dicom, but the ImagePositionPatient is written in the same manner.</p>
<p>Any idea why that is happening and how this could be addressed?</p>

---

## Post #5 by @Alexander_Shiryaev (2025-12-02 20:29 UTC)

<p><a class="mention" href="/u/chrismak">@ChrisMak</a>, see <a href="https://discourse.slicer.org/t/load-vol-file-into-3d-slicer-from-morita-machine/4815/15">here</a>.</p>
<p>It’s possible the “byte skip” parameter is incorrect.</p>
<p>Also, I can see your data rotated 45° around vertical (I→S) axis.</p>
<pre data-code-wrap="xml"><code class="lang-xml">&lt;tfAntiAliasAngleInDegree value="45"/&gt;
</code></pre>
<p>You can use the following Python script to apply transform to align axes:</p>
<pre data-code-wrap="py"><code class="lang-py">import numpy as np
from scipy.ndimage import rotate

import read_vol import load_data

path_input = "CT_0.vol"
path_output = "CT_0_rotated.raw"

def main () -&gt; None:
    d = load_data(path_input)

    print("shape before rotation:", d.shape, d.dtype)

    # rotate around last axis (2), relative to center
    d_rot = rotate(d, angle=45, axes=(0, 1), reshape=False, order=1, cval=-32768)
    # flip very first (0) axis
    d_rot = d_rot[::-1, :, :]

    print("shape after rotation:", d_rot.shape)

    with open(path_output, "wb") as f:
        f.write(d_rot.tobytes())

if __name__ == '__main__':
    main()
</code></pre>
<p>Then use the following <code>CT_0_rotated.nhdr</code> file:</p>
<pre><code class="lang-auto">NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: signed short
dimension: 3
space: left-posterior-superior
sizes: Z Y X
space directions: (0,0,S) (0,S,0) (S,0,0)
kinds: domain domain domain
endian: little
encoding: raw
space origin: (0,0,0)
byte skip: 0
data file: CT_0_rotated.raw
</code></pre>
<p>Fill <code>X</code>, <code>Y</code> and <code>Z</code> values from “shape after rotation” script output, <code>S</code> is voxel size.<br>
In your case:</p>
<ul>
<li><code>X</code> = <code>Y</code> = 240 - (-240) + 1 = 481, <code>Z</code> = 241 - (-242) + 1 = 484</li>
<li><code>S</code> = 0.125</li>
</ul>

---

## Post #6 by @ChrisMak (2025-12-02 21:45 UTC)

<p>It was byte skip! Thank you so much!</p>

---
