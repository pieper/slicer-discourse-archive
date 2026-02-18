# Convert MRI from DICOM (exported by syngo.via) to NRRD

**Topic ID**: 2555
**Date**: 2018-04-10
**URL**: https://discourse.slicer.org/t/convert-mri-from-dicom-exported-by-syngo-via-to-nrrd/2555

---

## Post #1 by @Tommaso_Di_Noto (2018-04-10 09:06 UTC)

<p>Hello everyone!<br>
I have a series of MRI cardiac images (more specifically I have the most significant slice for each patient; i.e. one image for each patient). I have extracted all these images with the software Siemens Syngo Via in a DICOM format.</p>
<p>Since I want to mine these data with a machine learning approach, I wanted to use the open-source platform <a href="https://github.com/Radiomics/pyradiomics" rel="nofollow noopener">pyradiomics</a>. In order to use this package I need the images in the .nrrd format, so I followed this <a href="https://na-mic.org/w/images/6/6c/2012-SPIE-1-DICOMToNRRDConversionTutorial.pdf" rel="nofollow noopener">guide</a> and it worked well.</p>
<p>The only problem is that the new .nrrd images have a different pixel spacing from the original dicom ones. More specifically they now have a pixel spacing in microns and not in mm like before. Moreover, the spacing has been automatically re-set to (1,1) while before it was something like (0.89,0.89). Does 3D slicer automatically rescale images?</p>
<p>How could I solve this issue?</p>
<p>Thanks a lot in advance,<br>
Tommaso</p>

---

## Post #2 by @pieper (2018-04-10 11:59 UTC)

<aside class="quote no-group" data-username="Tommaso_Di_Noto" data-post="1" data-topic="2555">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tommaso_di_noto/48/6802_2.png" class="avatar"> Tommaso_Di_Noto:</div>
<blockquote>
<p>Does 3D slicer automatically rescale images?</p>
</blockquote>
</aside>
<p>Slicer will use the data from the header (in mm) but you can change this in the Volumes → Volume Information fields and resave if you want.</p>

---

## Post #3 by @Tommaso_Di_Noto (2018-04-10 12:17 UTC)

<p>Hi Pieper and thanks for answering my question!</p>
<p>Maybe I have expressed myself wrong. I know that it is possible to modify the spacing in Volumes&gt;Volume information…the fact is that if I open my DICOM image for instance in ImageJ I have a 512x512 matrix with a FOV of 460x460 mm^2 and hence a pixel spacing of about 0,89 (469/512), while both when I open the same DICOM image with 3D slicer and  I save it to .nrrd I get (1,1,1) mm as pixel spacing and not for instance (0.89, 0.89, 0)  as I would expect.</p>
<p>Is this normal?<br>
Thanks a lot again</p>

---

## Post #4 by @cpinter (2018-04-10 13:43 UTC)

<p>If you have access to the original DICOM I suggest loading that to Slicer and saving it as nrrd, without using Syngo Via’s export option. Slicer should interpret the original DICOM correctly and the nrrd file sohuld come out as expected.</p>

---

## Post #5 by @Tommaso_Di_Noto (2018-04-10 14:10 UTC)

<p>Hi Csaba!<br>
I had to go necessarily through SyngoVia because the software they are using here at the hospital for the PACS is Agfa IMPAX and, unfortunately, doesn’t allow the DICOM extraction</p>

---

## Post #6 by @cpinter (2018-04-10 15:17 UTC)

<p>I see, thanks for the clarification. I’m not familiar with SyngoVia, but maybe it has some export options to keep as much of the original DICOM metadata as possible.</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> If I remember correctly you have worked with SyngoVia. Did you have an established protocol for DICOM export that worked well with Slicer?</p>

---

## Post #7 by @fedorov (2018-04-10 15:51 UTC)

<p>On our installation, there is a standard DICOM export to file system feature. I cannot explain the discrepancy between Slicer and ImageJ that is happening in the case of <a class="mention" href="/u/tommaso_di_noto">@Tommaso_Di_Noto</a>. Not sure how to debug it without access to a sample dataset.</p>

---

## Post #8 by @pieper (2018-04-10 22:37 UTC)

<p>If Imagej is writing out the spacing as .89, .89, 0 then ITK may think it cannot read valid spacing and default to 1,1,1.</p>

---

## Post #9 by @fedorov (2018-04-11 00:59 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> the way I understood it, the issue is that image is read from DICOM both in Slicer and ImageJ, but the spacing interpreted from DICOM is different.</p>

---

## Post #10 by @pieper (2018-04-11 11:43 UTC)

<aside class="quote no-group" data-username="fedorov" data-post="9" data-topic="2555" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fedorov/48/14_2.png" class="avatar"> fedorov:</div>
<blockquote>
<p><a class="mention" href="/u/pieper">@pieper</a> the way I understood it, the issue is that image is read from DICOM both in Slicer and ImageJ, but the spacing interpreted from DICOM is different.</p>
</blockquote>
</aside>
<p>Yes, could be - <a class="mention" href="/u/tommaso_di_noto">@Tommaso_Di_Noto</a> can you clarify?</p>

---

## Post #11 by @JoostJM (2018-04-11 12:00 UTC)

<p>I’ve been helping <a class="mention" href="/u/tommaso_di_noto">@Tommaso_Di_Noto</a> on this error as well, see also <a href="https://github.com/Radiomics/pyradiomics/issues/360" rel="nofollow noopener">this</a> issue in PyRadiomics.</p>
<p>As far as I can see, ITK (ITKsnap also misinterpreted the DICOM spacing) is having troubles parsing the spacing as it is encoded in the DICOM. In an example <a class="mention" href="/u/tommaso_di_noto">@Tommaso_Di_Noto</a> sent, spacing was encoded as <code>[5.0781200E-001\5.0781200E-001]</code>, maybe there is an issue with dealing with the <code>E-001</code>?</p>

---

## Post #12 by @fedorov (2018-04-11 13:44 UTC)

<p><a class="mention" href="/u/joostjm">@JoostJM</a> no, this is a valid content for PixelSpacing (see <a href="http://dicom.nema.org/dicom/2013/output/chtml/part05/sect_6.2.html">http://dicom.nema.org/dicom/2013/output/chtml/part05/sect_6.2.html</a>). I also made a fake dataset with exact same PixelSpacing, and confirmed it is read correctly into Slicer. Must be something else.</p>
<p><a class="mention" href="/u/tommaso_di_noto">@Tommaso_Di_Noto</a> can you run  this DICOM validator on your dataset and let us know what it says: <a href="http://www.dclunie.com/dicom3tools/dciodvfy.html">http://www.dclunie.com/dicom3tools/dciodvfy.html</a></p>

---

## Post #13 by @fedorov (2018-04-11 13:54 UTC)

<p>I also checked that SimpleITK can read the dataset I created for testing, and it does not reset spacing to 1.</p>
<pre><code class="lang-auto">$ dcmdump image/IMG0001.dcm|grep Spacing                                                                                                                                                 2.3.6
(0028,0030) DS [5.0781200E-001\5.0781200E-001]          #  30, 2 PixelSpacing
...
In [3]: i=sitk.ReadImage("image/IMG0001.dcm")
In [5]: i.GetSpacing()
Out[5]: (0.507812, 0.507812, 1.0)
</code></pre>

---

## Post #14 by @JoostJM (2018-04-11 14:00 UTC)

<p>Hmm, I rechecked the testset <a class="mention" href="/u/tommaso_di_noto">@Tommaso_Di_Noto</a> sent, and I’m seeing that the ImageOrientationPatient (0020,0037) and ImagePositionPatient (0020,0032) are missing, could this cause the error perhaps?</p>

---

## Post #15 by @fedorov (2018-04-11 14:02 UTC)

<p>Yes, that very likely could be a problem. I don’t know how it is handled by the libraries, but I am pretty sure this will render the dataset non-compliant with the standard.</p>

---

## Post #16 by @Tommaso_Di_Noto (2018-04-11 14:45 UTC)

<p>Exactly, Slicer&gt;Volume shows (1,1,1), while the ImageJ&gt;Image Info says: Pixel Size: 0.8984x0.8984 mm^2</p>

---

## Post #17 by @Tommaso_Di_Noto (2018-04-11 15:13 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/fedorov">@fedorov</a>  Sorry if I’m only answering now, but my Slicer/gmail notification was turned off, so I only saw your replies now. I turned it on now! Anyway:</p>
<p><a class="mention" href="/u/joostjm">@JoostJM</a>: Yes, I’ve also checked the cardiac images and the ImageOrientationPatient (0020,0037) and ImagePositionPatient (0020,0032) are missing there too.</p>
<p>As far as the feature extraction is concerned, do you think it’s a problem if I go forward with this .dcm to .nrrd conversion done in Slicer? I though that since it rescales ALL images to (1,1,1) and the .nrrd image created is read without errors in PyRadiomics, features shouldn’t suffer from different pixel spacing issues. I tried to explain more or less the same thing <a href="https://github.com/Radiomics/pyradiomics/issues/360#issuecomment-380354094" rel="nofollow noopener">here</a>.</p>
<p>Let me know if this makes sense <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=5" title=":wink:" class="emoji" alt=":wink:"></p>

---

## Post #18 by @fedorov (2018-04-11 15:14 UTC)

<p><a class="mention" href="/u/joostjm">@JoostJM</a> shared the pointer to the dataset. It is a secondary capture, and it doesn’t have to have the position/orientation. Probably ITK resets to spacing of 1 when those are missing, since it is not possible to know the 3d geometry of the image. Since ImageJ operates purely in 2d, it does not need to worry about geometry, and so this does not trigger an issue there.</p>
<p><a class="mention" href="/u/tommaso_di_noto">@Tommaso_Di_Noto</a> I think your options are:</p>
<ol>
<li>explore if you can export the dataset as MR, not secondary capture - have you tried export to file system option in syngo.via?</li>
<li>modify the spacing manually or in a script to use the one from the secondary capture <code>PixelSpacing</code>
</li>
</ol>
<p>In-plane spacing matters for some of the radiomics features, so it can be important.</p>

---

## Post #19 by @Tommaso_Di_Noto (2018-04-11 15:39 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/3/a32599dfeb938193dfc8549be5f5652e128aa740.png" data-download-href="/uploads/short-url/nhgo1YrUwMWUyEHOQVbqDex120M.png?dl=1" title="syngo_via" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a32599dfeb938193dfc8549be5f5652e128aa740_2_690x388.png" alt="syngo_via" data-base62-sha1="nhgo1YrUwMWUyEHOQVbqDex120M" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a32599dfeb938193dfc8549be5f5652e128aa740_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a32599dfeb938193dfc8549be5f5652e128aa740_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a32599dfeb938193dfc8549be5f5652e128aa740_2_1380x776.png 2x" data-dominant-color="181923"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">syngo_via</span><span class="informations">1920×1080 222 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>In yellow I have highlighted the options I chose when I extracted the images;</p>
<p>(The white circles are just to shade the patient’s name)</p>
<p>What could I  change?</p>
<p>Eventually, if I wanted to manually change the spacing, how could I do it? I mean…with which program? And should I do it on the original .dcm extracted from SyngoVia or on the .nrrd extracted from Slicer?</p>
<p>Thanks a lot!!</p>

---

## Post #20 by @fedorov (2018-04-11 18:29 UTC)

<aside class="quote no-group" data-username="Tommaso_Di_Noto" data-post="19" data-topic="2555">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tommaso_di_noto/48/6802_2.png" class="avatar"> Tommaso_Di_Noto:</div>
<blockquote>
<p>What could I  change?</p>
</blockquote>
</aside>
<p>Indeed, that’s what I would do too. Not sure, perhaps secondary capture is what is on PACS.</p>
<aside class="quote no-group" data-username="Tommaso_Di_Noto" data-post="19" data-topic="2555">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tommaso_di_noto/48/6802_2.png" class="avatar"> Tommaso_Di_Noto:</div>
<blockquote>
<p>Eventually, if I wanted to manually change the spacing, how could I do it? I mean…with which program? And should I do it on the original .dcm extracted from SyngoVia or on the .nrrd extracted from Slicer?</p>
</blockquote>
</aside>
<pre data-code-wrap="bash"><code class="lang-bash">$ pip install SimpleITK
$ pip install pydicom
</code></pre>
<p>Then you can use something like this script:</p>
<pre data-code-wrap="python"><code class="lang-python">import SimpleITK as sitk
import pydicom, sys

i = sitk.ReadImage(sys.argv[1])
d = pydicom.read_file(sys.argv[1])
s = d.PixelSpacing[0]
i.SetSpacing([s,s,1])
sitk.WriteImage(i,sys.argv[2])
</code></pre>

---

## Post #21 by @Tommaso_Di_Noto (2018-04-12 07:25 UTC)

<p>Thanks a lot <a class="mention" href="/u/fedorov">@fedorov</a>. I’ll try to modify it manually. Just one questions:</p>
<ol>
<li>I understood that sys.argv[1] takes the first command line argument passed to my script, but how can I pass my image as first argument? Should I do it in command line or like in python IDLE?</li>
</ol>
<p>Thanks again!</p>

---

## Post #22 by @fedorov (2018-04-12 13:49 UTC)

<p>Sorry for the lack of usage instructions… You can save that code in a (for example) <code>converter.py</code> file, and then run it as follows from the command line:</p>
<pre><code class="lang-bash">$ python converter.py input_dicom_image_slice output.nrrd
</code></pre>
<p>Typically, I do not use python IDE, so I cannot give you instructions on how to run this code from an IDE.</p>

---

## Post #23 by @Tommaso_Di_Noto (2018-04-12 14:55 UTC)

<p>Thanks a lot <a class="mention" href="/u/fedorov">@fedorov</a>! It seems to work!</p>
<p>The .nrrd image that is now created has the same pixel spacing of the original dicom one. There’s still a funny fact though: while in Slicer the pixel spacing is correct and in <em>mm</em> (as the original), in ImageJ the pixel spacing is correct, the size is also correct (it was modified to 512,512,1) but the unit of measure is still in <em>microns</em>…maybe it’s really just an ImageJ bug!</p>
<p>Anyway, this leads us to my initial question I asked in PyRadiomics to <a class="mention" href="/u/joostjm">@JoostJM</a>:</p>
<p>Now that the pixel spacing is preserved during the conversion to nrrd, but my images have different pixel spacing, is there a rule to decide the resampling with <code>imageoperations.resampleImage</code>? I mean…if I have some images with a pixel spacing of (0.89, 0.89) <em>mm</em> and others with a pixel spacing of (1.2,1.2) <em>mm</em> should I just resample them to a mean pixel spacing? Should I choose the smallest spacing and resample all images to that?</p>
<p>Thanks a lot in advance for your amazing support!</p>

---

## Post #24 by @lassoan (2018-04-12 15:39 UTC)

<p>ImageJ is mostly used for microscopy imaging and ignores most DICOM metadata, so it is not surprising that it blindly assumes unit is always microns.</p>
<p>In general, in medical image computing algorithms, visualization and analysis is always performed in physical space, so it does not matter much what was the resolution of the input images. <a class="mention" href="/u/joostjm">@JoostJM</a> can confirm if pyradiomics properly takes image spacing into account when computing metrics.</p>

---

## Post #25 by @fedorov (2018-04-12 16:28 UTC)

<p>One example where units may matter in pyradiomics is smoothing filter sigma is defined in mm, which will be a problem if defaults are used and the actual units are microns.</p>
<p>I agree with <a class="mention" href="/u/lassoan">@lassoan</a> - it is likely ImageJ just assumes microns. That image is a human head, right?</p>
<aside class="quote no-group" data-username="Tommaso_Di_Noto" data-post="23" data-topic="2555">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tommaso_di_noto/48/6802_2.png" class="avatar"> Tommaso_Di_Noto:</div>
<blockquote>
<p>Now that the pixel spacing is preserved during the conversion to nrrd, but my images have different pixel spacing, is there a rule to decide the resampling with imageoperations.resampleImage? I mean…if I have some images with a pixel spacing of (0.89, 0.89) mm and others with a pixel spacing of (1.2,1.2) mm should I just resample them to a mean pixel spacing? Should I choose the smallest spacing and resample all images to that?</p>
</blockquote>
</aside>
<p>There is not really a “correct” answer to this. As a general rule you will lose information by resampling. As another general rule, harmonized acquisition protocol is recommended for this kind of studies. The rest is your decision that you need to make based on your application, your data, and your analysis of the relevant literature.</p>
<p>Welcome to the world of research with no ground truth! We are here to help you get started with the tools, but the rest is up to you.</p>

---

## Post #26 by @Tommaso_Di_Noto (2018-04-16 06:29 UTC)

<p>hehe ok sure! Thanks a lot again! <a class="mention" href="/u/fedorov">@fedorov</a></p>

---

## Post #27 by @JoostJM (2018-04-16 10:30 UTC)

<p><a class="mention" href="/u/tommaso_di_noto">@Tommaso_Di_Noto</a>, What you can also try is to <code>export stack</code> instead of <code>export image</code> in syngo via, if I’m correct, this will export the entire volume and maybe prevents the conversion to secondary capture.</p>
<p>As to your other points, I agree with <a class="mention" href="/u/fedorov">@fedorov</a>, with the small addition that, especially for texture features, ‘common’ protocols is advised. Specifically for image spacing, this means that you are looking at the same level of texture (i.e. fine or coarse) and there is some literature available that has shown that some features are dependent on the voxel size (although this is usually due to some interaction with volume, the true dependency is the number of voxel in the VOI)</p>

---

## Post #28 by @lkcl (2025-06-18 18:20 UTC)

<p>hello all,</p>
<p>i just got an MRI scan using a Siemens Tesla 1.5 and<br>
asked for CDs with the DICOM data on it. turns out it<br>
is also syngo - an autorun.exe installation of syngo is<br>
on the CD, which i extracted avoiding windows entirely<br>
with:</p>
<pre><code class="lang-auto">dd if=/dev/sr0 bs=1M of=mri1.iso
mount -o loop /mnt/cdrom ./mri1.iso
</code></pre>
<p>was able to copy the files from /mnt/cdrom,<br>
umount /mnt/cdrom, and then import the dicom<br>
data directory… which failed.</p>
<p>an hour’s investigation shows that they simply<br>
blast the JPEG2000 data onto the end of the<br>
DICOM data - no end-tag, no length indicator,<br>
nothing.</p>
<p>therefore, the simple (and absolutely dreadful)<br>
hack below was “successful” in simply assuming<br>
that the rest of the DICOM file was the JPEG2000<br>
raw data. note that i assume that the read of 10mb<br>
will succeed: there is nothing sophisticated here.</p>
<pre><code class="lang-auto">+                    logger_debug("Reading undefined length data element"
+                        f"{fp_tell():08X}")
+                value = (True, fp.read(100000000))
+                logger_debug("Read %d bytes" % len(value[1]))
+                #value = read_undefined_length_value(
+                #    fp, is_little_endian, delimiter, defer_size
+                #)

</code></pre>
<p>anyone wishing to make a similar hack to their installation<br>
of Slicer, of course taking full responsibility for doing so,<br>
would need to modify this file:</p>
<p>./lib/Python/lib/python3.12/site-packages/pydicom/filereader.py</p>
<p>p.s. note, if you have a newer version of Slicer you need this instead</p>
<pre><code class="lang-auto">                value = fp.read(100000000)
                logger_debug("Read %d bytes" % len(value))
</code></pre>

---

## Post #29 by @lkcl (2025-12-24 18:00 UTC)

<p>folks was this actioned and resolved in future releases?</p>
<p>checking Slicer-5.11.0-2025-12-15-linux-amd64 the answer is “no”</p>

---
