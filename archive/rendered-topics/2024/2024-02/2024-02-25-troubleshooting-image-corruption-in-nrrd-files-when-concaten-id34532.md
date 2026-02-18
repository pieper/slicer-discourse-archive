# Troubleshooting Image Corruption in NRRD Files When Concatenating Multiple Raw Files into a Single Volume

**Topic ID**: 34532
**Date**: 2024-02-25
**URL**: https://discourse.slicer.org/t/troubleshooting-image-corruption-in-nrrd-files-when-concatenating-multiple-raw-files-into-a-single-volume/34532

---

## Post #1 by @rcapozza (2024-02-25 20:07 UTC)

<p>I am using NDDR files to load a volume, each file references a consecutively numbered raw file type from 1 to 10; my idea to avoid having to create ten NDDR files is to concatenate all the files into a single one named data.raw and read it with a single NDDR file. I believe this is possible, but when I try it, the image gets corrupted.<br>
The content of each file is as follows:<br>
NRRD0004</p>
<h1><a name="p-107447-complete-nrrd-file-format-specification-at-1" class="anchor" href="#p-107447-complete-nrrd-file-format-specification-at-1" aria-label="Heading link"></a>Complete NRRD file format specification at:</h1>
<h1><a name="p-107447-httpteemsourceforgenetnrrdformathtml-2" class="anchor" href="#p-107447-httpteemsourceforgenetnrrdformathtml-2" aria-label="Heading link"></a><a href="http://teem.sourceforge.net/nrrd/format.html" class="inline-onebox" rel="noopener nofollow ugc">Teem: nrrd: Definition of NRRD File Format</a></h1>
<p>type: short<br>
dimension: 3<br>
space: left-posterior-superior<br>
sizes: 271 271 1<br>
space directions: (0.59, 0.0, 0.0) (0.0, 0.59, 0.0) (0.0, 0.0, 2.5)<br>
kinds: domain domain domain<br>
endian: little<br>
encoding: raw<br>
space origin: (0.0, 0.0, 0.0)<br>
byte skip: 1609<br>
data file: I0024241.M0X</p>
<p>where .M0X ranges from .M01 to .M10</p>
<p>and what I want to implement with the single file is:<br>
NRRD0004</p>
<h1><a name="p-107447-complete-nrrd-file-format-specification-at-3" class="anchor" href="#p-107447-complete-nrrd-file-format-specification-at-3" aria-label="Heading link"></a>Complete NRRD file format specification at:</h1>
<h1><a name="p-107447-httpteemsourceforgenetnrrdformathtml-4" class="anchor" href="#p-107447-httpteemsourceforgenetnrrdformathtml-4" aria-label="Heading link"></a><a href="http://teem.sourceforge.net/nrrd/format.html" class="inline-onebox" rel="noopener nofollow ugc">Teem: nrrd: Definition of NRRD File Format</a></h1>
<p>type: short<br>
dimension: 3<br>
space: left-posterior-superior<br>
sizes: 271 271 10<br>
space directions: (0.59, 0.0, 0.0) (0.0, 0.59, 0.0) (0.0, 0.0, 2.5)<br>
kinds: domain domain domain<br>
endian: little<br>
encoding: raw<br>
space origin: (0.0, 0.0, 0.0)<br>
byte skip: 1609<br>
data file: data.raw</p>
<p>data.raw contains the concatenated files  I0024241.M01 to  I0024241.M10</p>
<p>Thank you in advance for any help you can provide.</p>

---

## Post #2 by @pieper (2024-02-25 23:52 UTC)

<p>There’s a lot of useful debugging advice here:</p>
<p><a href="https://teem.sourceforge.net/nrrd/format.html" class="onebox" target="_blank" rel="noopener">https://teem.sourceforge.net/nrrd/format.html</a></p>

---

## Post #3 by @rcapozza (2024-02-26 00:15 UTC)

<p>Thank you, pieper, I have based my work on that documentation to generate the NRRD file. I believe my problem lies in how to merge the image files into a single one. Should I only keep the portion corresponding to the image data, or can the complete files be concatenated with their headers? That is, is the “byte skip” command used on each of the slices stored in the file, or only at the beginning of its reading?</p>

---

## Post #4 by @pieper (2024-02-26 00:28 UTC)

<p>As I recall byte skip only refers to the start of a single file and I don’t think there’s a way to skip the headers of each of the files in a data file list, but I could be wrong about that.  As I recall there’s also an option to give a -1 for byte skip so that it figures out from the file size and expected image size how big the header is.  If you want to merge all the files into a single raw file you almost certainly need to concatenate only the image parts (uncompressed).  Also if you are working with named files be sure to check the option of giving a printf-style string to create the filenames from the number pattern.</p>
<p>I pointed to the nrrd documentation also so you would have a look at unu and the rest of the nrrd utility set.  There are lots of ways to create and manipulate nrrd files and with some experiments you can pretty much do anything.</p>

---
