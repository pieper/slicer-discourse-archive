# Load MRML V1.0 scene in Slicer 4

**Topic ID**: 1570
**Date**: 2017-12-01
**URL**: https://discourse.slicer.org/t/load-mrml-v1-0-scene-in-slicer-4/1570

---

## Post #1 by @benzwick (2017-12-01 04:42 UTC)

<p>Operating system: Debian 9.2<br>
Slicer version: 4.8.0<br>
Expected behavior: Scene is loaded in Slicer<br>
Actual behavior: Error parsing XML in stream at line 1, column 0, byte index 0: syntax error</p>
<p>Hello,</p>
<p>I have some old MRML V1.0 scenes which I am unable to load into Slicer 4.</p>
<p>The files begin with the following lines:</p>
<pre><code>MRML V1.0
Volume (
</code></pre>
<p>When I try to open the file in Slicer 4.8 I get the following error:</p>
<pre><code>Error parsing XML in stream at line 1, column 0, byte index 0: syntax error
</code></pre>
<p>The MRML files I have are obviously not XML files so I’m guessing that they were created with an older version of Slicer (circa 1999).</p>
<p>Is there any way to open these files in newer versions of Slicer? Otherwise, is there a script available that can be used to convert the MRML V1.0 files to the newer XML MRML format?</p>

---

## Post #2 by @fedorov (2017-12-01 04:43 UTC)

<p>There is no script to port 1999 versions of MRML into the modern Slicer.</p>

---

## Post #3 by @benzwick (2017-12-01 06:32 UTC)

<p>Thanks Andrey. I might try to translate the files manually or write my own script. Do you know if there is a description of the MRML format that lists the allowable XML elements? All I have found so far is the documentation on the wiki:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/MRML" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/MRML</a></p>
<p>and the class documentation:</p>
<p><a href="http://apidocs.slicer.org/master/classvtkMRMLNode.html" class="onebox" target="_blank" rel="nofollow noopener">http://apidocs.slicer.org/master/classvtkMRMLNode.html</a></p>
<p>Are there any other references that might help with this?</p>

---

## Post #4 by @lassoan (2017-12-01 12:23 UTC)

<p>Both old and new scene is human-readable, so writing a converter should be possible just by looking at the files. If you are not sure about what is a corresponding element or atrribute in current Slicer scenes then you can ask it here.</p>

---

## Post #5 by @ihnorton (2017-12-01 16:59 UTC)

<p>A quick <a href="https://www.google.com/search?hl=en&amp;q=%22MRML+V1.0%22">google</a> suggests there was a MRML1 importer in Slicer 2, which I have been able to run semi-recently (Windows might be the best bet, actually). This could provide an import pathway or possibly example code to start from.</p>
<p>(it’s going to be really tricky to go from 2-&gt;3-&gt;4 so if you have a lot of data then a custom importer directly to Slicer 4 probably makes sense).</p>

---

## Post #6 by @pieper (2017-12-01 17:25 UTC)

<p>FWIW slicer3 could import slicer2 mrml scenes (at least most of the data) and there’s a docker image that can run slicer3.</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/pieper/SlicerDockers/tree/master/slicer3">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/pieper/SlicerDockers/tree/master/slicer3" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/pieper/SlicerDockers/tree/master/slicer3" target="_blank" rel="noopener">SlicerDockers/slicer3 at master · pieper/SlicerDockers</a></h3>

  <p><a href="https://github.com/pieper/SlicerDockers/tree/master/slicer3" target="_blank" rel="noopener">master/slicer3</a></p>

  <p><span class="label1">docker config files for slicer. Contribute to pieper/SlicerDockers development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>(I haven’t tried a slicer2 docker, but that might be good to do for historical reasons).</p>
<p>Here’s the slicer3 importer code for reference:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/pieper/Slicer3/blob/master/Base/GUI/Tcl/Slicer2Import.tcl">
  <header class="source">

      <a href="https://github.com/pieper/Slicer3/blob/master/Base/GUI/Tcl/Slicer2Import.tcl" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/Slicer3/blob/master/Base/GUI/Tcl/Slicer2Import.tcl" target="_blank" rel="noopener">pieper/Slicer3/blob/master/Base/GUI/Tcl/Slicer2Import.tcl</a></h4>


      <pre><code class="lang-tcl">
#
# test of importing a slicer2 mrml scene using the 
# vtk xml data parser mechanism
#

#######
#
# for debugging - run the command when the script is read...
#
#after idle {
#  puts -nonewline "importing..."
#  ImportSlicer2Scene c:/data/tutorial/tutorial.xml
#  set viewer [$::slicer3::ApplicationGUI GetActiveViewerWidget] 
#  [$viewer GetMainViewer] Reset
#  puts "done"
#}

# main entry point...
proc ImportSlicer2Scene {sceneFile} {
</code></pre>



  This file has been truncated. <a href="https://github.com/pieper/Slicer3/blob/master/Base/GUI/Tcl/Slicer2Import.tcl" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #7 by @benzwick (2017-12-05 03:55 UTC)

<p>Thank you for all your suggestions.</p>
<p>Below is an example of one of the scenes I have tried to convert manually. I can load the XML file into Slicer 4.8 without errors but the image is not loaded. However, in the Data module, the node “brain1st” is created with the correct image spacing. Are there any obvious mistakes in the MRML file, or could it be that Slicer does not recognise the file format of the volume data? There are 60 slices named brain1st.001, brain1st.002 etc.</p>
<p>Original MRML v1.0 (Slicer 1 or 2):</p>
<pre><code>MRML V1.0
Volume (
        name brain1st
        labelMap 1
        filePrefix brain1st
        headerSize 0
        imageRange 1 60
        spacing 0.9375 0.9375 2.5
        rasToIjkMatrix 0 1.06667 0 122.773 -1.06667 0 -0 140.8 0 -0 0.4 23.14 -0 0 -0 1
        rasToVtkMatrix -0 1.06667 -0 122.773 1.06667 -0 0 115.2 -0 0 0.4 23.14 0 -0 0 1
        options slicer interpolate 0 lutID 6
)
</code></pre>
<p>Converted MRML v2.0 (Slicer 4):</p>
<pre><code>&lt;?xml version="1.0" standalone="no"?&gt;
&lt;!DOCTYPE MRML SYSTEM "mrml20.dtd"&gt;
&lt;MRML&gt;
&lt;Volume
        name="brain1st"
        labelMap="1"
        filePrefix="brain1st"
        headerSize="0"
        imageRange="1 60"
        spacing="0.9375 0.9375 2.5"
        rasToIjkMatrix="0 1.06667 0 122.773 -1.06667 0 -0 140.8 0 -0 0.4 23.14 -0 0 -0 1"
        rasToVtkMatrix="-0 1.06667 -0 122.773 1.06667 -0 0 115.2 -0 0 0.4 23.14 0 -0 0 1"
        interpolate="no"&gt;
        &lt;!-- Not used: --&gt;
        &lt;!-- options slicer interpolate 0 lutID 6 --&gt;
&lt;/Volume&gt;
&lt;/MRML&gt;
</code></pre>
<p>When I load the new MRML file in Slicer 4.8 I get the following output in the terminal:</p>
<pre><code>"MRML Scene" Reader has successfully read the file ".../brain1st/brain1st.xml.mrml" "[0.34s]" 

Input port 0 of algorithm vtkImageMapToColors(0x2ed5040) has 0 connections but is not optional.

No scalar values found for texture input!
</code></pre>
<p>If I try to load the image data alone (without the MRML scene file) I get the following error:</p>
<pre><code>ReadData: This is not a nrrd file

ReadData: Failed to instantiate a file reader

ReadData: Cannot read file as a volume of type Volume[fullName = .../brain1st/brain1st.001]
        Number of files listed in the node = 0.
        File reader says it was able to read 0 files.
        File reader used the archetype file name of .../brain1st/brain1st.001 []
ITK exception info: error in unknown
Could not create IO object for reading file .../brain1st/brain1st.001
Tried to create one of the following:
    NiftiImageIO
    NrrdImageIO
    GiplImageIO
    JPEGImageIO
    GDCMImageIO
    BMPImageIO
    LSMImageIO
    PNGImageIO
    TIFFImageIO
    VTKImageIO
    StimulateImageIO
    BioRadImageIO
    MetaImageIO
    MRCImageIO
    MINCImageIO
    MGHImageIO
    MRMLIDImageIO
You probably failed to set a file suffix, or
    set the suffix to an unsupported type.
</code></pre>
<p>Is there a way to set the file type without changing the file extension? If not with the GUI, perhaps using Python?</p>
<p>Isaiah, I did find some similar code in my search so I got the Slicer2 source from Steve’s github page but ran into some trouble trying to compile it. I fixed a lot of the errors but eventually gave up hoping to find a better way to import the files into the new Slicer. Did you compile Slicer2 from source or did you use a precompiled binary for Windows?</p>
<p>Steve, I tried to load the scene and image in Slicer 3.6.3 but this did not work either. I will try again to compile Slicer 2. Would you expect there to be any problems building Slicer 2 or 3 on Debian 9 (stretch)?</p>

---

## Post #8 by @lassoan (2017-12-05 04:41 UTC)

<p>Slicer uses ITK’s file readers to read images and they determine what reader to use based on the file extension. You could probably instantiate a specific reader using Python scripting, but it would be easier to just set the proper extension for your image (and a good idea in general).</p>
<p>What is the file format of brain1st.001?</p>

---

## Post #9 by @pieper (2017-12-05 12:57 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> slicer2 used a (bad) convention of “.%03d” as the names of uncompressed raw images.  The imageRange field tells what files are expected.</p>
<p><a class="mention" href="/u/benzwick">@benzwick</a> if you writing a script to process these it would probably be easiest to implement a new parser for the old MRML files and populate the slicer4 MRML scene.  Are there other data objects in the old scenes or just image volumes?</p>

---

## Post #10 by @benzwick (2017-12-05 17:09 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I agree that changing the extension is a better idea although there are a large number of files that will need to be renamed. I don’t know the file format of brain1st.001 etc. I searched and tried using a few different tools and image viewers to open the files. If anyone has any suggestions for how to determine the file type that would help a lot!</p>
<p><a class="mention" href="/u/pieper">@pieper</a> If the images files are uncompressed raw images as you suggest what would be the correct file extension? Also, is NRRD still the recommended image format? If so, is there a way to convert the images to NRRD format? This might make it a bit easier to manage the data in the long term.</p>
<p>The only other data objects in the scene files that I have found so far are models e.g:</p>
<pre><code>Model (
        name brain
        fileName .../brain.vtk
)</code></pre>

---

## Post #11 by @lassoan (2017-12-05 17:17 UTC)

<p>Files without extension may be headerless raw file but it may be DICOM as well. The first task should be to find out what the format is.</p>
<p>If they are raw files then they can be read as nrrd file. To load that file, you just create a NRRD header file: a text file with .nhdr extension that describes image size, spacing, orientation, and name of the raw file that contains voxel data.</p>
<p>Large number of files is not an issue, as you would process them using a Python script anyway.</p>

---

## Post #12 by @pieper (2017-12-05 17:33 UTC)

<p>Yes, the slicer2 convention was headerless raw files.  Creating a .nhdr file to point to the originals is a good way to approach the problem.</p>
<p><a href="http://teem.sourceforge.net/nrrd/format.html#detached" class="onebox" target="_blank">http://teem.sourceforge.net/nrrd/format.html#detached</a></p>

---

## Post #13 by @benzwick (2017-12-12 06:40 UTC)

<p>I have created a NRRD header file as suggested (see below). I now have the following questions:</p>
<ul>
<li>
<p>Can I put the transformation matrix in the NRRD header or do I need to put it in the new MRML scene file?</p>
</li>
<li>
<p>Are the type (short), endian (little) and byte skip (-1) correct for reading Slicer 1/2 raw data?</p>
</li>
<li>
<p>When I save the image as NRRD or NHDR in Slicer (see example below) the saved NRRD header uses the ‘left-posterior-superior’ (LPS) space instead of the ‘right-anterior-superior’ (RAS) space. Is this the expected behaviour? The wiki (<a href="https://www.slicer.org/wiki/Coordinate_systems" rel="nofollow noopener">https://www.slicer.org/wiki/Coordinate_systems</a>) states that Slicer uses the RAS coordinate system. Is there a way to keep the original basis when saving the image or is it better to use LPS?</p>
</li>
<li>
<p>Is there a way to determine the image sizes (number of pixels in each direction) from the raw data? (I used trial and error based on some knowledge of the expected image size)</p>
</li>
</ul>
<p>Volume object in original MRML file:</p>
<pre><code>MRML V1.0
Volume (
        name 1st
        filePrefix ./0021stSPGR/I
        imageRange 1 60
        spacing 0.937500 0.937500 2.5
        rasToIjkMatrix 0 1.06667 0 122.773 -1.06667 0 -0 140.8 0 -0 0.4 23.14 -0 0 -0 1
        rasToVtkMatrix -0 1.06667 -0 122.773 1.06667 -0 0 115.2 -0 0 0.4 23.14 0 -0 0 1
        scanOrder OB
        scanOrigin 132 -115.1 -57.85
        scanOrientation 0 1 0 0 1 0 0 0 0 0 1 0 0 0 0 1
)
</code></pre>
<p>NHDR created manually:</p>
<pre><code>NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: short
dimension: 3
space: right-anterior-superior
sizes: 256 256 60
space directions: (0.9375,0,0) (0,0.9375,0) (0,0,2.5)
kinds: domain domain domain
endian: little
byte skip: -1
encoding: raw
space origin: (-132,-115.1,-57.85)
# TODO:
# rasToIjkMatrix 0 1.06667 0 122.773 -1.06667 0 -0 140.8 0 -0 0.4 23.14 -0 0 -0 1
# rasToVtkMatrix -0 1.06667 -0 122.773 1.06667 -0 0 115.2 -0 0 0.4 23.14 0 -0 0 1
# scanOrder OB
# scanOrientation 0 1 0 0 1 0 0 0 0 0 1 0 0 0 0 1
data file: I.%03d 1 60 1
</code></pre>
<p>NHDR saved using Slicer 4.8:</p>
<pre><code>NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: short
dimension: 3
space: left-posterior-superior
sizes: 256 256 60
space directions: (-0.9375,0,0) (0,-0.9375,0) (0,0,2.5)
kinds: domain domain domain
endian: little
encoding: gzip
space origin: (132,115.09999999999997,-57.850000000000001)
data file: 0021stSPGR.raw.gz</code></pre>

---

## Post #14 by @lassoan (2017-12-12 14:28 UTC)

<aside class="quote no-group" data-username="benzwick" data-post="13" data-topic="1570">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/benzwick/48/80521_2.png" class="avatar"> benzwick:</div>
<blockquote>
<p>Can I put the transformation matrix in the NRRD header or do I need to put it in the new MRML scene file?</p>
</blockquote>
</aside>
<p>Put it in the NRRD header.</p>
<aside class="quote no-group" data-username="benzwick" data-post="13" data-topic="1570">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/benzwick/48/80521_2.png" class="avatar"> benzwick:</div>
<blockquote>
<p>Are the type (short), endian (little) and byte skip (-1) correct for reading Slicer 1/2 raw data?</p>
</blockquote>
</aside>
<p>I don’t think skip (-1) is correct. If there is no image header then use skip: 0.<br>
If you don’t get short or endian correct then you can see very characteristic striping artifacts. There are not too many combination, so you can do trial and error.</p>
<aside class="quote no-group" data-username="benzwick" data-post="13" data-topic="1570">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/benzwick/48/80521_2.png" class="avatar"> benzwick:</div>
<blockquote>
<p>When I save the image as NRRD or NHDR in Slicer (see example below) the saved NRRD header uses the ‘left-posterior-superior’ (LPS) space instead of the ‘right-anterior-superior’ (RAS) space.</p>
</blockquote>
</aside>
<p>Yes, this is expected. Slicer uses ITK image readers and ITK uses LPS coordinate system (it is converted to to/from RAS when writing/reading the file in Slicer).</p>
<aside class="quote no-group" data-username="benzwick" data-post="13" data-topic="1570">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/benzwick/48/80521_2.png" class="avatar"> benzwick:</div>
<blockquote>
<p>Is there a way to determine the image sizes (number of pixels in each direction) from the raw data? (I used trial and error based on some knowledge of the expected image size)</p>
</blockquote>
</aside>
<p>You should be able to find image size in the scene file (maybe in storage node, if there was such thing at that time). It seems that the old importer code used slice size of 256x256 if no “dimensions” tag was present. You can get the number of slices from the total file length divided by slice size and voxel size.</p>

---

## Post #15 by @benzwick (2017-12-13 08:31 UTC)

<p>How can I put the transformation/orientation information in the header? In other words, how do I specify the following MRMLv1.0 data in the NRRD header:</p>
<pre><code>rasToIjkMatrix 0 1.06667 0 122.773 -1.06667 0 -0 140.8 0 -0 0.4 23.14 -0 0 -0 1
rasToVtkMatrix -0 1.06667 -0 122.773 1.06667 -0 0 115.2 -0 0 0.4 23.14 0 -0 0 1
scanOrder OB
scanOrigin 132 -115.1 -57.85
scanOrientation 0 1 0 0 1 0 0 0 0 0 1 0 0 0 0 1
</code></pre>
<p>Does <code>scanOrigin</code> in the MRML correspond to <code>space origin</code> in the NRRD file? I assume that the <code>rasToIjkMatrix</code> is what I need to include but I couldn’t even apply the transform manually in Slicer (the image is squashed and not rotated correctly).</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> When I use <code>byte skip: 0</code> the image is split down the middle and the two halves are swapped. I checked the data files for this case and they all contain some header data (not all of my images have these headers). Each raw slice file begins with <code>IMGF</code>. I guess it might be GE MR Signa 5.x Image data (<a href="http://www.dclunie.com/medical-image-faq/html/part4.html" rel="nofollow noopener">http://www.dclunie.com/medical-image-faq/html/part4.html</a>) as it is most likely that a GE Signa system was used to acquire the images. The size of the image is 256 x 256 x 2 = 131072 but the file size is 138976 bytes so the additional 7904 bytes must be the header. When I use <code>byte skip: 7904</code> the image loads and looks OK. If I use <code>byte skip: -1</code> the image appears the same as when using the actual header size. It seems easier to use the latter. Would there be any benefit in specifying the actual header length (7904) instead of reading the file backwards (-1)?</p>
<p>Changing the endianness does not have an obvious effect on the appearance of the image (especially if the data type is <em>unsigned</em> short) but the data probe confirms it is actually big-endian.</p>

---

## Post #16 by @lassoan (2017-12-13 19:38 UTC)

<aside class="quote no-group" data-username="benzwick" data-post="15" data-topic="1570">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/benzwick/48/80521_2.png" class="avatar"> benzwick:</div>
<blockquote>
<p>I guess it might be GE MR Signa 5.x Image data</p>
</blockquote>
</aside>
<p>It seems that you’ve found the file format description!</p>
<ul>
<li>4   - int      - byte displacement to pixel data =&gt; this tells you the <code>byte skip</code> value (but if you know that the image data is at the end of the file then <code>byte skip: -1</code> should work, too)</li>
<li>8   - int      - width =&gt; first component of <code>sizes</code></li>
<li>12  - int      - height =&gt; second component of <code>sizes</code></li>
<li>16  - int      - depth (bits) =&gt; you can use this for determining <code>type</code></li>
</ul>
<aside class="quote no-group" data-username="benzwick" data-post="15" data-topic="1570">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/benzwick/48/80521_2.png" class="avatar"> benzwick:</div>
<blockquote>
<p>Does scanOrigin in the MRML correspond to space origin in the NRRD file?</p>
</blockquote>
</aside>
<p>Yes.</p>
<aside class="quote no-group" data-username="benzwick" data-post="15" data-topic="1570">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/benzwick/48/80521_2.png" class="avatar"> benzwick:</div>
<blockquote>
<p>I assume that the rasToIjkMatrix is what I need to include</p>
</blockquote>
</aside>
<pre><code>rasToVtkMatrix  =
  -0 1.06667 -0 122.773
  1.06667 -0 0 115.2
  -0 0 0.4 23.14
  0 -0 0 1
</code></pre>
<p>The top-left 3x3 part of this matrix goes into <code>space directions</code>. The first 3 values in the last column goes to <code>space origin</code>.</p>

---

## Post #17 by @ihnorton (2017-12-13 19:58 UTC)

<p>FWIW, dcm2nii supports some variant of this file format. Might be worth trying as a point of reference.</p>
<p><a href="https://www.nitrc.org/projects/dcm2nii/" class="onebox" target="_blank">https://www.nitrc.org/projects/dcm2nii/</a></p>
<p>(that’s the old pascal version, not the new <code>dcm2niix</code>)</p>

---

## Post #18 by @benzwick (2017-12-14 10:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="16" data-topic="1570">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The top-left 3x3 part of this matrix goes into space directions. The first 3 values in the last column goes to space origin.</p>
</blockquote>
</aside>
<p>I assumed something along those lines. However, in the MRML file there is <code>rasToIjkMatrix</code> as well as <code>scanOrigin</code>. My guess is that only <code>scanOrigin</code> would be used by Slicer and <code>rasToIjkMatrix</code> would be ignored - is this correct? The <code>spacing</code> and <code>rasToIjkMatrix</code> values in the MRML file seem to be related by 1/1.06667 = 0.9375 and 1/0.4 = 2.5. Also, can I ignore <code>scanOrder</code> and <code>scanOrientation</code> as well?</p>
<p>The following header seems to work now and the image orientation roughly matches some of the related VTK models:</p>
<pre><code>NRRD0004
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
type: short
dimension: 3
space: right-anterior-superior
sizes: 256 256 60
kinds: domain domain domain
endian: big
byte skip: -1
encoding: raw
space directions: (0,0.9375,0) (-0.9375,0,0) (0,0,2.5) 
space origin: (132,-115.1,-57.85)
data file: I.%03d 1 60 1
</code></pre>
<aside class="quote no-group quote-modified" data-username="ihnorton" data-post="17" data-topic="1570" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ihnorton/48/9_2.png" class="avatar"> ihnorton:</div>
<blockquote>
<p>FWIW, dcm2nii supports some variant of this file format. Might be worth trying as a point of reference.</p>
<p><a href="https://www.nitrc.org/projects/dcm2nii/" class="inline-onebox" rel="noopener nofollow ugc">NITRC: dcm2nii: Tool/Resource Info</a></p>
<p>(that’s the old pascal version, not the new dcm2niix)</p>
</blockquote>
</aside>
<p>Through trial and error using the NRRD format I established that the data is big-endian. It seems that dcm2nii interprets the data as little-endian. When I load the converted NIfTI image into Slicer some pixels have negative values which appear as black spots in bright areas such as the skull, and the values in dark areas are 0, 256, 512, 768 etc. (the same happens if I specify little-endian in the NRRD header). If I specify big-endian in the NRRD header there are no negative pixels and the dark areas are 0, 1, 2, 3 etc. I couldn’t find an option for dcm2nii to change this. Also, the orientation of the image is different than using the above NRRD header.</p>
<p>By the way, the link above appears to refer to the newer dcm2niix. The old dcm2nii can be found here: <a href="http://people.cas.sc.edu/rorden/mricron/dcm2nii.html" class="inline-onebox" rel="noopener nofollow ugc">dcm2nii DICOM to NIfTI conversion</a>. Both dcm2niix and dcm2nii (packaged with mricron) are also available in the NeuroDebian repository.</p>

---
