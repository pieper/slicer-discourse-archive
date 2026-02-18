# Multi-raw image loading using RawImageGuess extension

**Topic ID**: 26126
**Date**: 2022-11-08
**URL**: https://discourse.slicer.org/t/multi-raw-image-loading-using-rawimageguess-extension/26126

---

## Post #1 by @seyang (2022-11-08 02:58 UTC)

<p>Can someone help us to import multi-raw images?<br>
Our system is remaining each slice image.<br>
Ex) 240 Slice = Slice0001,0002,0003, 0004…</p>
<p>As I confirm the RawImageGuess extension module, only supports one raw image.<br>
We really need this function. please help us.</p>
<p>Thanks to the 3D Slicer development team.</p>

---

## Post #2 by @muratmaga (2022-11-08 06:06 UTC)

<p>You mean, you have a sequence of raw images? If you know the xyz dimensions and voxel spacing, and data type (char, int, short etc), you can write a simple NRRD header to describe the data. I think something like this probably work. You need to replace the type and sizes with correct value.</p>
<pre><code class="lang-auto">
NRRD0004
type: uchar 
dimension: 3
sizes: 1024 1024 240
encoding: raw
datafile: ./Slice0001
./Slice0002
./Slice0003
</code></pre>
<p>…</p>

---

## Post #3 by @seyang (2022-11-11 08:25 UTC)

<p>Thanks muratmaga,</p>
<p>Yes it mean, i have a sequence of raw images.<br>
I know xyz dimensions and voxel spacing. but how to create the NRRD header?<br>
Could you please let me know?</p>
<p>I really need this method.</p>

---

## Post #4 by @muratmaga (2022-11-11 15:43 UTC)

<p>It is a simple text file that gets written. You can see the specification here. <a href="https://teem.sourceforge.net/nrrd/format.html" rel="noopener nofollow ugc">https://teem.sourceforge.net/nrrd/format.html</a></p>
<p>See the section specifically <strong>3. Detached Headers with “data file:”</strong></p>

---

## Post #5 by @seyang (2022-11-14 00:47 UTC)

<p>Hi Muratmaga.</p>
<p>Really thanks for your quick reply.<br>
I tried to make nrrd to refer your reply.<br>
But when i load the nrrd file, following error occurs.</p>
<p>Error: Loading D:/2022.09.29 CT/slice.nrrd - Failed to read node slice_2 (vtkMRMLSequenceNode1) from filename=‘D:/2022.09.29 CT/slice.nrrd’</p>
<p>^ vtkMRMLVolumeArchetypeStorageNode::ReadDataInternal: Cannot read file as a volume of type Volume [fullName = D:/2022.09.29 CT/slice.nrrd]: FileFormatError. Number of files listed in the node = 0. File reader says it was able to read 1 files. File reader used the archetype file name of D:/2022.09.29 CT/slice.nrrd [reader 0th file name = D:/2022.09.29 CT/slice.nrrd].</p>
<p>[NRRD Format]<br>
NRRD0004<br>
type: uchar<br>
dimension: 3<br>
sizes: 1024 1024 240<br>
encoding: raw<br>
datafile: ./slice0000<br>
./slice0001<br>
./slice0002</p>
<p>Nrrd file is included in the same raw sequence folder.<br>
File name : slice0000 , slice0001 , slice0002 ,slice0003 ,slice0004</p>
<p>Is it have way to correct importing nrrd file?<br>
If this code is wrong, please make sample code for me?</p>
<p>I really helpful for your advice.</p>

---

## Post #6 by @muratmaga (2022-11-14 17:30 UTC)

<p>To be perfectly honest, I never tried building a nrrd header from sequence of images, but I know it is doable. Looking at the description of detached header more carefully, you may have to use the keyword LIST or define a filename formatting (min, max, increase). Try adding <code>LIST</code> right after  data file or type</p>
<p><code>datafile: "Slice%04d 0 max_number_slices 1 </code></p>
<h2><a name="p-86091-h-3-detached-headers-with-data-file-1" class="anchor" href="#p-86091-h-3-detached-headers-with-data-file-1" aria-label="Heading link"></a>3. Detached Headers with “data file:”</h2>
<p>Detached headers allow data stored in one or more separate files, with or without headers of another format, to be accessed by a NRRD header, leaving the original file(s) intact. The line skip and byte skip fields are especially useful for these cases. Detached headers are also very useful in situations where very large amounts of data are to be read or written with direct IO, a very fast method of IO in which the device driver transfers data directly between blocks on disk and user-space memory (<a href="https://teem.sourceforge.net/nrrd/index.html" rel="noopener nofollow ugc"><strong>nrrd</strong></a> currently supports direct IO on SGIs, via the <a href="https://teem.sourceforge.net/air/index.html" rel="noopener nofollow ugc"><strong>air</strong></a> library). Direct IO requires special alignment between the data segment beginning and the block boundaries on disk, which makes using attached headers rather inconvenient. Detached headers are also the simplest way to deal with NRRD readers which do not support the optional compressed encodings, since a stand-alone program (such as “gzip/gunzip” or “bzip2/bunzip2”) will be able to process the separate data file.</p>
<p>There is one new field specification which is required in detached headers, using the “data file” identifier. This field specification can take one of three possible forms (the second and third were copied from the MetaImage format).</p>
<blockquote>
<ol>
<li>data file: &lt;<em>filename</em>&gt;</li>
<li>data file: &lt;<em>format</em>&gt; &lt;<em>min</em>&gt; &lt;<em>max</em>&gt; &lt;<em>step</em>&gt; [&lt;<em>subdim</em>&gt;]</li>
<li>data file: LIST [&lt;<em>subdim</em>&gt;]</li>
</ol>
</blockquote>

---

## Post #7 by @lassoan (2022-11-14 20:37 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> what you described works well - see</p>
<aside class="quote quote-modified" data-post="3" data-topic="26217">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/import-nrrd-format/26217/3">Import NRRD format</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I’ve just tried this and it works flawlessly. 
I’ve used this MRHead.nhdr file: 
NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: unsigned short
dimension: 3
space: left-posterior-superior
sizes: 256 256 130
space directions: (0,1,0) (0,0,-1) (-1.2999954223632812,0,0)
kinds: domain domain domain
endian: little
encoding: raw
space origin: (86.644897460937486,-133.92860412597656,116.78569793701172)
data file: MRHead%04d.raw 0 129 1

with f…
  </blockquote>
</aside>


---

## Post #8 by @seyang (2022-11-15 01:09 UTC)

<p>Really Thanks for your support.</p>

---
