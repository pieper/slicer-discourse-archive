# Unable to load a segmentation encoded as .tag file

**Topic ID**: 15271
**Date**: 2020-12-29
**URL**: https://discourse.slicer.org/t/unable-to-load-a-segmentation-encoded-as-tag-file/15271

---

## Post #1 by @Maxnach (2020-12-29 15:03 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.13.0<br>
Expected behavior: Load pre-existing segmentation .tag file<br>
Actual behavior: Unable to load</p>
<p>Hello 3Dslicer community,</p>
<p>I’m just starting with this amazing software. I would like to load pre-existing segmentation mask generated from a dicom CT-image using another software and saved as .tag files. I can succesfully load the dicom file, but when I load the .tag file (segmentation mask) nothing happens. That would save me a lot of time as I have hundreds of segmented mask file already saved and would like to manipulate them in 3Dslicer with the corresponding dicom image.</p>
<p>Best,</p>
<p>Max</p>

---

## Post #2 by @pieper (2020-12-29 15:36 UTC)

<p>I’m not aware of that format or of any existing tools in Slicer that will load those files.  Usually it’s possible to reverse engineer a format like that.  Your best bet is to look for any documentation about the software that generated these files and see if you can maybe find (or write) a converter to a more common format.</p>

---

## Post #3 by @Maxnach (2020-12-29 16:29 UTC)

<p>Thank you so much for your quick reply. I’m a newbie in dev (medical background) but I know the architecture of these .tag files:</p>
<p>The TAG file format is loosely based on the university of Waterloo IM format.</p>
<p>The image file is composed of two sections:</p>
<p>•The header</p>
<p>•the image binary data.</p>
<p>The Header</p>
<p>The header is entirely composed of lines of ASCII text. Each line is  terminated by the characters  and  (0x0D and 0x0A). The header is terminated by a  character (0x0C).</p>
<p>Everything on a line following a “*” will be considered as comments and can be disregarded by the program.</p>
<p>The header is composed of a series of keywords value pairs. The keyword and values are separated by “:”. Each pair of keyword and values are separated by one or more separation characters. The recognized separators are: " " (space), “,” (comma), “\t” (tab) or “\n” (new-line). You can use lowercase or uppercase indifferently in the keywords, the program converts all the keywords characters to uppercase before parsing the header.</p>
<p>The recognized keywords and their permitted values are:</p>
<p>x:</p>
<p>“X” resolution (in pixels).</p>
<p>y:</p>
<p>“Y” resolution (in pixels).</p>
<p>z:</p>
<p>Number of images in the file.</p>
<p>type:</p>
<p>Gives the size of each pixel, the values supported by the program are BYTE or SHORT (only BYTE is used for the “.tag” files).</p>
<p>org_x:</p>
<p>Position in “x”, “y” and “z” of the center of the top left pixel of the image.</p>
<p>org_y:</p>
<p>org_z:</p>
<p>dim_x:</p>
<p>Total dimension in “x” and “y” of the image (in millimeters).</p>
<p>dim_y:</p>
<p>inc_x:</p>
<p>Distance between 2 consecutive pixels in “x” and “y” of the image (in millimeters).</p>
<p>inc_y:</p>
<p>epais:</p>
<p>Slice thickness.</p>
<p>dir_h_x:</p>
<p>X, y and z components of the horizontal direction vector (in patient system).</p>
<p>dir_h_y:</p>
<p>dir_h_z:</p>
<p>dir_v_x:</p>
<p>X, y and z components of the vertical direction vector (in patient system).</p>
<p>dir_v_y:</p>
<p>dir_v_z:</p>
<p>uid:</p>
<p>Unique number used to make sure this tag is associated with the correct GLI image.</p>
<p>chksum:</p>
<p>Checksum of the original GLI image.</p>
<p>x:256    y:256    z:9      type:BYTE</p>
<p>org_x:-204.2221  org_y:-181.8909  org_z:-250.0000</p>
<p>inc_x:0.7105     inc_y:0.7105     epais:5.0000</p>
<p>dir_h_x:1.0000     dir_h_y:0.0000     dir_h_z:0.0000</p>
<p>dir_v_x:0.0000     dir_v_y:1.0000     dir_v_z:0.0000</p>
<p>uid:AFCCCAC6 chksum:09F1588D bin:256</p>
<ul>
<li>number of echos:        0</li>
</ul>
<p>^L</p>
<p>Sample TAG header</p>
<p>The Image Data</p>
<p>The image data is written in binary form. There are X x Y x Z pixels in the image data. The values for X, Y and Z come from the header. Each pixel takes 1 or 2 bytes according to the value associated with the “type” keyword (tag files use “Byte”, so one byte per pixel). The pixels are written using the algorithm:</p>
<pre><code>      for each image k

                for each line j (starting at the top)

                          for each pixel i (starting at the left)

                                    write pixel [k][j][i] ;
</code></pre>
<p>Could that help ?</p>
<p>Best regards,</p>
<p>Max</p>

---

## Post #4 by @lassoan (2020-12-29 19:34 UTC)

<p>You can read such images using <a href="https://github.com/acetylsalicyl/SlicerRawImageGuess">RawImageGuess extension</a>. You can get image dimensions, spacing, etc. from the information in the image header. RawImageGuess can generate a nhdr header file that you can use to load the .tag file.</p>
<p>You can easily create such nhdr file automatically, using a Python script, by parsing the .tag file header. Mapping from .tag to .nrrd:</p>
<ul>
<li>x, y, z -&gt; sizes</li>
<li>type -&gt; type</li>
<li>org_* -&gt; space origin</li>
<li>inc_* and dir_* -&gt; space_directions (it is a 3x3 matrix, column norms equal inc* values, first column direction is dir_h, second column direction is dir_v, third column direction is <em>cross(dir_h, dir_v)</em>)</li>
</ul>
<p>To make eveyone’s life easier, I would recommend you to ask the developers of the software that generates these .tag files to generate standard .nrrd files instead.</p>

---

## Post #5 by @Maxnach (2020-12-30 09:18 UTC)

<p>Thank you so much, I’m indeed able to load the .tag file using the .nhdr header. I do not know how to code in Python to perform this process in batch , I will probably do it manually or a ask around.</p>
<p>I’m now trying to match the original dicom and the mask, but it seems 3D slicer considers them as separated volume. I tried loading the mask from the segmentation module using import labelmask/model nothing happens when I click on import (hence I’m not able to indicate the path of the .nhdr file)… any ideas…?</p>
<p>Best regards,</p>
<p>Max</p>

---

## Post #6 by @lassoan (2020-12-30 18:36 UTC)

<p>RawImageGuess always sets a default image orientation, while axes of your input DICOM volume may be oriented differently. To make the segmentation line up with the original DICOM images, you probably need to compute the space_directions matrix as I described above.</p>

---

## Post #7 by @Maxnach (2021-01-05 16:35 UTC)

<p>Hello,</p>
<p>Thank you very much for your answers. I almost succeeded in alignement, I computed the space direction matrix only using the inc* value and the mask is almost aligned. However, it seems my problem is to correctly indicate the number of size of header (in bytes) : how could I know it? I tried with <a href="http://bytesizematters.com/" rel="noopener nofollow ugc">http://bytesizematters.com/</a> (lol), it indicates 223 without space but it’s still not correct.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08015ed2392291aeadce295933d0e749afc33871.png" data-download-href="/uploads/short-url/18OKRnw0QrvQ5UONs4XOmWyyOGJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08015ed2392291aeadce295933d0e749afc33871_2_690x265.png" alt="image" data-base62-sha1="18OKRnw0QrvQ5UONs4XOmWyyOGJ" width="690" height="265" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08015ed2392291aeadce295933d0e749afc33871_2_690x265.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08015ed2392291aeadce295933d0e749afc33871_2_1035x397.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08015ed2392291aeadce295933d0e749afc33871_2_1380x530.png 2x" data-dominant-color="76757A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1825×701 56 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So If I get it right, I have to be sure all my parameters are ok by manually checking on 3D slicer, and when everything is ok I can creare a python loop.</p>
<p>May I ask you an advice for the next step : how can I make 3D slicer understand that this file (openned with the .nhdr header) is actually a segmention and not a volume ? In the segmentation tools, nothing happens when I click on “import” (whether I select labelmaps or model).</p>
<p>Best regards,</p>
<p>Maxime</p>
<p>Edit : Here is the .tag file : [<a href="https://drive.google.com/file/d/1ooXY464Iw3Z3FKblze0j9xLwoWnZk89e/view?usp=sharing" class="inline-onebox" rel="noopener nofollow ugc">2.tag - Google Drive</a>]</p>

---

## Post #8 by @pieper (2021-01-05 17:09 UTC)

<aside class="quote no-group" data-username="Maxnach" data-post="7" data-topic="15271">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/maxnach/48/9366_2.png" class="avatar"> Maxnach:</div>
<blockquote>
<p>how can I make 3D slicer understand that this file (openned with the .nhdr header) is actually a segmention and not a volume ?</p>
</blockquote>
</aside>
<p>You can use the Volumes → Volume Information interface to turn it into a Labelmap volume, then you can import it to a Segmentation</p>

---

## Post #9 by @Maxnach (2021-01-05 17:31 UTC)

<p>Oh gosh thanks, that indeed works !! I feel I’m almost there :</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d377b4493992c801b7139395d1d2c7ed7d04f20e.png" data-download-href="/uploads/short-url/uaJd6HzyeZnjE3e0H4CCzNdxkT4.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d377b4493992c801b7139395d1d2c7ed7d04f20e_2_690x275.png" alt="image" data-base62-sha1="uaJd6HzyeZnjE3e0H4CCzNdxkT4" width="690" height="275" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d377b4493992c801b7139395d1d2c7ed7d04f20e_2_690x275.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d377b4493992c801b7139395d1d2c7ed7d04f20e_2_1035x412.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d377b4493992c801b7139395d1d2c7ed7d04f20e_2_1380x550.png 2x" data-dominant-color="868589"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1665×665 64.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I will try to solve the byte size issue (pretty sure the header size I put is not correct) and then test whether the radiomics extension works correctly on the mask…</p>
<p>If that works, you have just saved me weeks of labour.</p>
<p>Best regards,</p>
<p>Maxime</p>

---

## Post #10 by @lassoan (2021-01-05 17:35 UTC)

<p>See some more options of how to conveniently load an image file directly as labelmap volume or segmentation: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#load-image-file-as-labelmap-volume">https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#load-image-file-as-labelmap-volume</a></p>

---

## Post #11 by @Maxnach (2021-01-05 17:53 UTC)

<p>Thank you for these tips, it seems I can load it as a labelmap volume directly, but not as a segmentation (since I load an .nhdr file and not a .nrrd)</p>
<p>I tried the radiomics analysis (even though mask is not perfectly aligned), but I have a blank sheet as a results… any ideas?</p>
<p>Maxime</p>
<p>Edit: it’s not a problem of mask/volume as I’m able to calculte segmentation statistics</p>

---

## Post #12 by @lassoan (2021-01-05 20:30 UTC)

<p>I’ve added .nhdr as an acceptable extension for segmentation files (in addition to nrrd). It will be available in Slicer Preview Release from tomorrow.</p>

---
