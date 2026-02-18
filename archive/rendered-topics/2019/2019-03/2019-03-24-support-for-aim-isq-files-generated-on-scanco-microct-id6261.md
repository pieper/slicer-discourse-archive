# Support for .AIM/.isq files generated on Scanco microCT

**Topic ID**: 6261
**Date**: 2019-03-24
**URL**: https://discourse.slicer.org/t/support-for-aim-isq-files-generated-on-scanco-microct/6261

---

## Post #1 by @BhanuPetla (2019-03-24 14:23 UTC)

<p>I might be the odd one out here working on plants. I am new to Slicer and trying to use Scanco microCT 50 for scanning my plant root samples. Would like to know if you are planning to give support for direct import of .AIM/other formats that Scanco imagers generate.</p>

---

## Post #2 by @adamrankin (2019-03-24 14:38 UTC)

<p>Very cool.</p>
<p>I’m not sure if you’re familiar with open-source projects, but support is usually given by the people who need a particular feature. You’re correct that we don’t have a lot of people using Slicer for plants, but there could be a lot of useful tools for image analysis here for you.</p>
<p>With regards to file loading support, your two options are to ask the community to implement it for you (someone might say yes, more likely if you can provide a document describing the file format, or any other libraries that already load the file), or to implement it yourself, with the community’s help (you’ll find lots of development support here).</p>
<p>If you’re interested in having a go at it yourself, this is a good start<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/IO" rel="nofollow noopener">IO in Slicer</a><br>
<a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/Models" rel="nofollow noopener">3D models module</a>, which is a fine example of loading 3D model data in Slicer</p>
<p>Edit: closing bracket</p>

---

## Post #3 by @pieper (2019-03-24 15:58 UTC)

<p>Hi <a class="mention" href="/u/bhanupetla">@BhanuPetla</a> - I’ll second what <a class="mention" href="/u/adamrankin">@adamrankin</a> said, and just add that you might also get some help if in addition to documentation you could share some cool example data for people to experiment with.</p>

---

## Post #4 by @lassoan (2019-03-24 18:37 UTC)

<p>There are many options to build a workflow where you annotate and analyze CT images.</p>
<p>Most often you just acquire images there and then later annotate the images in other software. Do you annotate images on the scanner console? What other software do you use for visualization, annotation, and analysis?</p>
<p>What kind of annotations do you use (points, lines, curves, angles, 3D segmentations, …)?</p>
<p>What would you like to do with the annotations? Just show them, or also edit them, analyze them, compute metrics, etc.?</p>

---

## Post #5 by @muratmaga (2019-03-24 21:02 UTC)

<p>We might eventually provide a more convenient way to do the import, meanwhile you can look at my tutorial on how to use the metadata from .aim to write a slicer compatible header (.NHDR) and import load it into Slicer:<br>
<a href="https://blogs.uw.edu/maga/2018/09/importing-microct-data-from-scanco-into-slicer/" class="onebox" target="_blank" rel="nofollow noopener">https://blogs.uw.edu/maga/2018/09/importing-microct-data-from-scanco-into-slicer/</a></p>

---

## Post #6 by @BhanuPetla (2019-03-24 22:40 UTC)

<p><a class="mention" href="/u/adamrankin">@adamrankin</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/muratmaga">@muratmaga</a>    Thank you for all your responses and suggestions. I am a plant molecular biologist, very new to CT imaging and have absolutely no experience with coding.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> Our goal is to trace the vascular bundles (pointed with green arrows) in soybean root nodules, look at their organization and be able to quantify their distribution (area, volume, etc) and branching patterns. We would like to then compare these with the mutants and quantify the differences.</p>
<p>The scanner is located off campus and we decided to use Slicer for feature extraction and constructing vascular models. We are still working on the workflow for quantification. Any suggestions are welcome.<br>
We are installed Linux version of Slicer on visualization node running Centos 7.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I could not access the sample files on the box folder. Can you make them available?</p>
<p>I have included a link to AIM file and a few sample pictures.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8be7d3e2519bdf42d07b2c2cbf2d5f239a9393c.jpeg" data-download-href="/uploads/short-url/o4MkQQf0qc9o41htfaMwZj3KaD2.jpeg?dl=1" title="Nodule%20vasculature%20model" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8be7d3e2519bdf42d07b2c2cbf2d5f239a9393c_2_589x500.jpeg" alt="Nodule%20vasculature%20model" data-base62-sha1="o4MkQQf0qc9o41htfaMwZj3KaD2" width="589" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8be7d3e2519bdf42d07b2c2cbf2d5f239a9393c_2_589x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a8be7d3e2519bdf42d07b2c2cbf2d5f239a9393c_2_883x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8be7d3e2519bdf42d07b2c2cbf2d5f239a9393c.jpeg 2x" data-dominant-color="D7CDB9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Nodule%20vasculature%20model</span><span class="informations">1104×936 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f491e05ee432392f7e81927ac1bb1898e1dc7dd3.jpeg" data-download-href="/uploads/short-url/yTz2A3sIAYXJWYnqJqcTjqNdrQD.jpeg?dl=1" title="54%20Vascular%20bundles" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f491e05ee432392f7e81927ac1bb1898e1dc7dd3_2_445x499.jpeg" alt="54%20Vascular%20bundles" data-base62-sha1="yTz2A3sIAYXJWYnqJqcTjqNdrQD" width="445" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f491e05ee432392f7e81927ac1bb1898e1dc7dd3_2_445x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f491e05ee432392f7e81927ac1bb1898e1dc7dd3_2_667x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f491e05ee432392f7e81927ac1bb1898e1dc7dd3_2_890x998.jpeg 2x" data-dominant-color="323332"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">54%20Vascular%20bundles</span><span class="informations">1650×1852 314 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<a href="https://sdsu.box.com/s/ie5tqhv1lcxsazaqp7fdblcwvppm7tin" rel="noopener nofollow ugc">Root nodule .AIM file </a><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/4/24d44cea83da47db3981b00396fad132d356e489.jpeg" data-download-href="/uploads/short-url/5fO2vUy3ySNCrdTWdXSKuVSCi2R.jpeg?dl=1" title="54%20PTA%202%25%20EtOH%2070%25%20NO_750-1500" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24d44cea83da47db3981b00396fad132d356e489_2_353x500.jpeg" alt="54%20PTA%202%25%20EtOH%2070%25%20NO_750-1500" data-base62-sha1="5fO2vUy3ySNCrdTWdXSKuVSCi2R" width="353" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24d44cea83da47db3981b00396fad132d356e489_2_353x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24d44cea83da47db3981b00396fad132d356e489_2_529x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/4/24d44cea83da47db3981b00396fad132d356e489_2_706x1000.jpeg 2x" data-dominant-color="656565"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">54%20PTA%202%25%20EtOH%2070%25%20NO_750-1500</span><span class="informations">2481×3509 1.08 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @muratmaga (2019-03-24 22:51 UTC)

<p>Link must have expired. Try this one. I will update the link later.<br>
<a href="https://app.box.com/s/6hee33dgmqp7l4o9k96mk5w7yogaoul6" class="onebox" target="_blank" rel="nofollow noopener">https://app.box.com/s/6hee33dgmqp7l4o9k96mk5w7yogaoul6</a></p>

---

## Post #8 by @BhanuPetla (2019-03-24 22:55 UTC)

<p>Link doesn’t work. Thanks<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98e2aadc27d1ff12006f5b856540e1fa17cc2d0b.png" alt="34%20PM" data-base62-sha1="lOucUoBbKxAIgnOzSKi8GyUGJAL" width="536" height="430"></p>

---

## Post #9 by @muratmaga (2019-03-25 00:14 UTC)

<p>Ok. There is something wrong with sharing options.<br>
You really don’t need the files. What you need is the xyz dimension, voxel spacing, data type and the byteskip fields from the log file.</p>

---

## Post #10 by @muratmaga (2019-03-25 01:34 UTC)

<p>I dont use scanco. In a sample a collaborator provided, there is a section just before Processing Log section that contains all relevant information. See below.</p>
<pre><code>Image data starts at byte offset: 3196
!-------------------------------------------------------------------------------
Volume                        PERCIVAL_370.AIM                                  
AIM Version                                    1.6
!
dim                                  622     642    1085
off                                    0       0       0
pos                                  150     212       4
element size in mm                0.0200  0.0200  0.0200
phys dim in mm                   12.4400 12.8400 21.7000
!
Type of data                        short (16 bit)
!-------------------------------------------------------------------------------
!
! Processing Log
!
!-------------------------------------------------------------------------------
Created by                    ISQ_TO_AIM (IPL)                                  
Time                           9-JAN-2018 09:25:49.87                           
Original file                 dk0:[microct.data.00002195.00006898]c0012945.isq; 
Original Creation-Date         8-JAN-2018 15:07:57.39                           
Orig-ISQ-Dim-p                                   1024       1024       1126
Orig-ISQ-Dim-um                                 20480      20480      22520
!-------------------------------------------------------------------------------
Patient Name                  Percival_370                                      
Index Patient                                    2195
Index Measurement                                6898
!-------------------------------------------------------------------------------
Site                                                4
Scanner ID                                       4241
Scanner type                                       10
Position Slice 1 [um]                           52685
No. samples                                      1024
No. projections per 180                           500
Scan Distance [um]                              20480
Integration time [us]                          300000
Reference line [um]                             52685
Reconstruction-Alg.                                 3
Energy [V]                                      55000
Intensity [uA]                                    145
Angle-Offset [mdeg]                                 0
Default-Eval                                     2060
!-------------------------------------------------------------------------------
Mu_Scaling                                       4096
Calibration Data              55 kV, 1200 mg HA/ccm BH-corr, Scaling 4096</code></pre>

---

## Post #11 by @BhanuPetla (2019-03-25 01:53 UTC)

<p>I could not run nrrd file in slicer. Can you give me some more pointers for generating .nrrd file? I am including screenshots of AIM file and NRRD file. Can you point me where to get voxel data, data type and byteskip from this? Thank you so much.</p>
<p>My AIM files do not have that data.<br>
I will generate them again and see if this is resolved.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/207c6893e0514f9d09ba4b701f094dadaf80f923.png" alt="nrrd" data-base62-sha1="4DnP1NSnVUHT8S6gf88XC4Z8pYD" width="365" height="170"></p>

---

## Post #12 by @muratmaga (2019-03-25 05:30 UTC)

<p>Looks like something is different between these two log files. Since I don’t have access to a Scanco system, I cannot help you any further. But if you figure it out, please post it here, as it may help other people in future.</p>
<p>As a temporary solution, I think bioformats has some support for .aim format (<a href="https://docs.openmicroscopy.org/bio-formats/5.9.2/formats/aim.html" rel="nofollow noopener">https://docs.openmicroscopy.org/bio-formats/5.9.2/formats/aim.html</a>). You might be able to use Fiji and then save it as a nrrd, which will work with Slicer.  Although figuring out why those fields in the metadata is missing might be a better overall solution.</p>

---

## Post #13 by @lassoan (2019-03-25 15:50 UTC)

<p>There is an <a href="https://github.com/KitwareMedical/ITKIOScanco">ITK reader for Scanco isq/rsq/rad/aim files</a>, which should be quite easy to enable in Slicer. <a class="mention" href="/u/jcfr">@jcfr</a> can you confirm?</p>
<p><a href="http://www.scanco.ch/en/support/customer-login/faq-customers/faq-customers-import-export.html">According to Scanco’s website, you can also export images in DICOM format</a>. Have you tried to export in DICOM format and load that into Slicer?</p>
<p>In the meantime, you can use <a class="mention" href="/u/nagy.attila">@nagy.attila</a>’s <a href="https://github.com/lassoan/SlicerRawImageGuess">RawImageGuess module</a> (not in the Extension manager yet, you need to download and add to module paths manually) to find out image parameters by trial and error. Once you learn what to look for, it takes a only few minutes to determine parameters for any image. It generated this <a href="https://1drv.ms/u/s!Arm_AFxB9yqHt5BnNqgDzRCtUv86oQ">NRRD header file</a> for your data set. If you place this file into the same folder as your C0000156.AIM data file then you can load the image by drag-and-dropping C0000156.nhdr file into Slicer.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/a/1a13dab897d1bf1c5b39d4c81aa770afee6d8f67.png" data-download-href="/uploads/short-url/3IGX1Et8IvcykRF0hqVM2cmhl0X.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a13dab897d1bf1c5b39d4c81aa770afee6d8f67_2_690x373.png" alt="image" data-base62-sha1="3IGX1Et8IvcykRF0hqVM2cmhl0X" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a13dab897d1bf1c5b39d4c81aa770afee6d8f67_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a13dab897d1bf1c5b39d4c81aa770afee6d8f67_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/a/1a13dab897d1bf1c5b39d4c81aa770afee6d8f67_2_1380x746.png 2x" data-dominant-color="8F8E95"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 349 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #14 by @BhanuPetla (2019-03-29 23:03 UTC)

<p>I was able to load dicom files on Slicer for my data set. But could not do much as the files are too big. I am running slicer on linux, Centos 7, with 188Gb RAM and 100Gb swap. When I try volume rendering, slicer uses up all the memory and swap and crashes. Is there a workaround for this? My dicom stack is 71Gb in size. Is there a way to load a subset of slices? I got following error message.<br>
I couldn’t instal the RawImageGuess module following the instructions.</p>
<p>Thank you all for your responses!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/ab91da13ed147bc57c6450f19ac424b84bab3dc9.jpeg" data-download-href="/uploads/short-url/otM8hFHifyb3rUUqU2YYcTMLiZj.jpeg?dl=1" title="03%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab91da13ed147bc57c6450f19ac424b84bab3dc9_2_690x431.jpeg" alt="03%20PM" data-base62-sha1="otM8hFHifyb3rUUqU2YYcTMLiZj" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab91da13ed147bc57c6450f19ac424b84bab3dc9_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab91da13ed147bc57c6450f19ac424b84bab3dc9_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/ab91da13ed147bc57c6450f19ac424b84bab3dc9_2_1380x862.jpeg 2x" data-dominant-color="B2B2BA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">03%20PM</span><span class="informations">1920×1200 362 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #15 by @pieper (2019-03-30 00:27 UTC)

<p>Yes, the std::bad_alloc message means you ran out of memory (usually you need several times more available memory than the size of your volume).  You can use the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/CropVolume" rel="nofollow noopener">CropVolume</a> module to select a subset and/or resample your data.</p>

---

## Post #16 by @muratmaga (2019-03-30 03:43 UTC)

<p>While I crop volume can help, I think a general purpose import time data reduction method would be a useful feature to have in Slicer. Not just for dicom, but for all supported image stacks and volume formats.<br>
<a class="mention" href="/u/smrolfe">@smrolfe</a> was testing a prototype type for image sequences but performance was a bit slow.</p>

---

## Post #17 by @BhanuPetla (2019-03-30 14:22 UTC)

<p>It couldn’t complete crop volume either. Is there a way to reduce the file size? AIM file is 700Mb.</p>

---

## Post #18 by @muratmaga (2019-03-30 16:31 UTC)

<p>There is a disconnect here. I thought you are trying to load the AIM file from scanco. If that’s 700MB, then that should perfectly fine with the method <a class="mention" href="/u/lassoan">@lassoan</a> suggested. You should be able to do everything you need to do with your system.<br>
Where is the 71GB dicom stack coming from, is that a separate dataset? Or 700MB aim file becomes 71GB when you convert it to a dicom from their format?</p>

---

## Post #19 by @BhanuPetla (2019-03-30 17:08 UTC)

<p>sorry for the confusion! I could not load AIM file to slicer, because of the missing information in AIM file (parameters before the processing log). Using Scanco program I generated DICOM stack which is 71Gb from AIM file (700Mb).</p>
<p>I couldn’t instal the RawImageGuess module following the instructions.</p>

---

## Post #20 by @muratmaga (2019-03-30 17:17 UTC)

<p>that is a 100X difference in volume size, which is hard to explain, unless you are setting a volume of interest during the generation of AIM file but not during the DICOM export.</p>
<p>There is really not much in the way of install RawImageGuess. You either clone the repository, or if you don’t know what that means click the green download button and choose as the ZIP file option. Then uncompress the zip file to folder and add that to the slicer modules path (Edit-&gt; Application Settings-&gt; Modules)</p>
<p>We are organizing a week-long workshop on using 3D Slicer in context of biological research in late August. It is free, you may want to consider attending it. You can find more information at <a href="https://slicermorph.github.io/2019_Summer_Workshop/" rel="nofollow noopener">https://slicermorph.github.io/2019_Summer_Workshop/</a></p>

---

## Post #21 by @BhanuPetla (2019-05-01 16:10 UTC)

<p>Thank you <a class="mention" href="/u/muratmaga">@muratmaga</a> for the information on 3D Slicer workshop. I am planning to attend.</p>

---

## Post #23 by @BhanuPetla (2019-05-01 16:30 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="12" data-topic="6261" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Looks like something is different between these two log files. Since I don’t have access to a Scanco system, I cannot help you any further. But if you figure it out, please post it here, as it may help other people in future.</p>
<p>As a temporary solution, I think bioformats has some support for .aim format (<a href="https://docs.openmicroscopy.org/bio-formats/5.9.2/formats/aim.html" rel="noopener nofollow ugc">https://docs.openmicroscopy.org/bio-formats/5.9.2/formats/aim.html</a>). You might be able to use Fiji and then save it as a nrrd, which will work with Slicer. Although figuring out why those fields in the metadata is missing might be a better overall solution.</p>
</blockquote>
</aside>
<p>Even Scanco was confused about missing header information in the main AIM file. We can access correct AIM header information displayed as .AIX from microCT web server. I was also able to load AIM and .ISQ files on imageJ using import .AIM and .ISQ plugin downloaded from here <a href="http://wiki.xn--davidhaberthr-7ob.ch/microct/working_with_isq_files" class="inline-onebox" rel="noopener nofollow ugc">microct:working_with_isq_files 			[wiki.davidhaberthuer.ch]</a><br>
Now I use .nhdr method you described for loading my data.<br>
I was able to load my data and extract the features I wanted and generate models. I used grow from seeds tool in segment editor module. <a class="mention" href="/u/lassoan">@lassoan</a> tutorial was super helpful. Thank you! Now I am looking at methods to quantify this data. My sample is 1-2mm and when I place Fudicial it is much bigger than my sample. How can I get around that?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7fc3d83e0f03c596593ad2260d568bdeec9b6d0.jpeg" data-download-href="/uploads/short-url/sx9rdlu1086WQ6ZalKx1p36oTJe.jpeg?dl=1" title="2019-04-24-Scene" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7fc3d83e0f03c596593ad2260d568bdeec9b6d0_2_690x484.jpeg" alt="2019-04-24-Scene" data-base62-sha1="sx9rdlu1086WQ6ZalKx1p36oTJe" width="690" height="484" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7fc3d83e0f03c596593ad2260d568bdeec9b6d0_2_690x484.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c7fc3d83e0f03c596593ad2260d568bdeec9b6d0_2_1035x726.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7fc3d83e0f03c596593ad2260d568bdeec9b6d0.jpeg 2x" data-dominant-color="B0AFAA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2019-04-24-Scene</span><span class="informations">1332×935 277 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #24 by @stephan (2019-05-02 00:18 UTC)

<aside class="quote no-group" data-username="BhanuPetla" data-post="23" data-topic="6261">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bhanupetla/48/3282_2.png" class="avatar"> BhanuPetla:</div>
<blockquote>
<p>My sample is 1-2mm and when I place Fudicial it is much bigger than my sample. How can I get around that?</p>
</blockquote>
</aside>
<p>You can set the display size of the fiducial in the Markup fiducials module. Select the fiducials list you are working on (size, color and the like is set per fiducials list, not per single markup point), display the “Advanced” section, and change the Glyph scale.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/9772d51f2c27f25477b414bd5cbfc13f3d3bdf1b.png" data-download-href="/uploads/short-url/lBM7MBSUt0ndpFlI2IvkObFqGiT.png?dl=1" title="Untitled-1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9772d51f2c27f25477b414bd5cbfc13f3d3bdf1b_2_690x431.png" alt="Untitled-1" data-base62-sha1="lBM7MBSUt0ndpFlI2IvkObFqGiT" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9772d51f2c27f25477b414bd5cbfc13f3d3bdf1b_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9772d51f2c27f25477b414bd5cbfc13f3d3bdf1b_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9772d51f2c27f25477b414bd5cbfc13f3d3bdf1b_2_1380x862.png 2x" data-dominant-color="38363D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled-1</span><span class="informations">1920×1200 176 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #25 by @muratmaga (2019-05-02 02:54 UTC)

<p><a class="mention" href="/u/bhanupetla">@BhanuPetla</a><br>
Slicer fiducial scaling is a bit problematic for datasets with small voxel sizes (around tens of microns or smaller) going between slice views and 3d rendering. There are plans to address that in near future.</p>

---

## Post #26 by @lassoan (2019-05-17 04:18 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="25" data-topic="6261">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Slicer fiducial scaling is a bit problematic for datasets with small voxel sizes</p>
</blockquote>
</aside>
<p>I’ve completely reworked markup scaling in latest nightly build (revision 28258). By default, markup size is set relative to the screen size (does not change if you zoom in/out in a view), in both 2D and 3D views. Therefore scale is always reasonable, regardless of the size or spacing of the volume. I’ve also added an option to specify absolute physical size - then the markup size remains physically the same, so it changes as you zoom in/out in a view.</p>

---

## Post #27 by @TravisBurgers (2019-11-08 16:21 UTC)

<p>I imported the uCT .aim files from a Scanco system using this technique too. I want to lay out a few more details from the RawImageGuess method because I struggled a little even after reading this thread.</p>
<p>First note, I also had to load RawImageGuess slightly differently from the ReadMe.md file for RawImageGuess. Slicer must have updated since it was generated. I went through the Customize Slicer menu on the home screen (it opened the Settings window). Go to Modules, and add the RawImageGuess directory to the Additional Module Paths box and reset Slicer.</p>
<ol>
<li>I used ImageJ and the plugin listed above for the Scanco way (<a href="http://wiki.xn--davidhaberthr-7ob.ch/microct/working_with_isq_files" rel="nofollow noopener">http://wiki.davidhaberthür.ch/microct/working_with_isq_files</a>). Using that plugin I imported the .aim files. ImageJ indicates the X and Y dimensions are of each image and how many slices (Z dimension) there are. I had to do this because it differed from the XXAIM.aix file that I downloaded from the same screen as the .aim file on the microCT server. It may have been different because I tried to do some segmenting in the Scanco software.</li>
<li>Back in the Slicer RawImageGuess module, I input the following values:<br>
a. Pixel type is 16 bit signed and Endianness is big endian.<br>
b. The header size can be found in the XXAIM.aix file. It is one less than the “Image Data starts at byte offset”.<br>
c. The X, Y, Z dimensions are those that I found from ImageJ.<br>
d. The X, Y, Z spacing is the voxel size. These can be found form the “element size in mm” in the XXAIM.aix file. I used a multiplication factor of 1000 (i.e., 14.8 instead of 0.0148) because Slicer wouldn’t take more than three decimals places and I didn’t want to lose the last decimal of resolution.</li>
<li>After I generated the .nhdr image header I used a text editor to modify the file by my previous scale factor (i.e., I changed 14.8 back to 0.0148).</li>
<li>I dragged the .nhdr file into Slicer and my .aim file loaded successfully!</li>
</ol>

---

## Post #28 by @muratmaga (2019-11-08 17:31 UTC)

<p><a class="mention" href="/u/travisburgers">@TravisBurgers</a><br>
Do you really need the Fiji/ImageJ step? Doesn’t the .aix file (or whatever you used to get the header size and the spacing, contain the XY dimensions and number of slices?</p>

---

## Post #29 by @TravisBurgers (2019-11-08 17:40 UTC)

<p>You’re right, the ImageJ step may not be required. I must have been looking at the .aix of another scan when I saw the XY and slices didn’t match.</p>

---

## Post #30 by @lassoan (2019-11-08 18:11 UTC)

<aside class="quote no-group" data-username="TravisBurgers" data-post="27" data-topic="6261">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/c6cbf5/48.png" class="avatar"> TravisBurgers:</div>
<blockquote>
<p>had to load RawImageGuess slightly differently from the ReadMe.md file for RawImageGuess. Slicer must have updated since it was generated. I went through the Customize Slicer menu on the home screen (it opened the Settings window). Go to Modules, and add the RawImageGuess directory to the Additional Module Paths box and reset Slicer.</p>
</blockquote>
</aside>
<p>Application settings should be available in menu, under Edit. Can you find it there?</p>
<aside class="quote no-group" data-username="TravisBurgers" data-post="27" data-topic="6261">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/c6cbf5/48.png" class="avatar"> TravisBurgers:</div>
<blockquote>
<p>I used a multiplication factor of 1000 (i.e., 14.8 instead of 0.0148) because Slicer wouldn’t take more than three decimals places and I didn’t want to lose the last decimal of resolution.</p>
</blockquote>
</aside>
<p>To increase number of decimal digits in a numeric input box, click <kbd>Ctrl</kbd> + <kbd>+</kbd>. I’ll add it to the documentation page.</p>
<p><a class="mention" href="/u/travisburgers">@TravisBurgers</a> If you find the extension useful then it would be great if you could draw an icon for it (one for the module, one for the extension). That’s the only reason why the extension still has to be installed manually and not available for download via Extension manager.</p>

---

## Post #31 by @TravisBurgers (2019-11-11 13:53 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="30" data-topic="6261">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Application settings should be available in menu, under Edit. Can you find it there?</p>
</blockquote>
</aside>
<p>Yes, I found it there.</p>
<aside class="quote no-group" data-username="lassoan" data-post="30" data-topic="6261">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>To increase number of decimal digits in a numeric input box, click <kbd>Ctrl</kbd> + <kbd>+</kbd>. I’ll add it to the documentation page.</p>
</blockquote>
</aside>
<p>This works for me too. It did not occur to me that more decimals would need to be manually added.</p>
<aside class="quote no-group" data-username="lassoan" data-post="30" data-topic="6261">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/travisburgers">@TravisBurgers</a> If you find the extension useful then it would be great if you could draw an icon for it (one for the module, one for the extension). That’s the only reason why the extension still has to be installed manually and not available for download via Extension manager.</p>
</blockquote>
</aside>
<p>What are the pixel requirements for this image?</p>

---

## Post #32 by @lassoan (2019-11-11 14:36 UTC)

<p>These are the placeholder icons for the <a href="https://github.com/lassoan/SlicerRawImageGuess/blob/master/RawImageGuess.png">extension</a> and <a href="https://github.com/lassoan/SlicerRawImageGuess/blob/master/RawImageGuess/Resources/Icons/RawImageGuess.png">module</a>. The actual icons should have the same aspect ratio (square) and approximately the same size (the icons are rescaled, so absolute size is not critical). If you use third-party images then make sure they can be used with modification and without attribution (it would be hard to ensure proper acknowledgment of the artwork).</p>

---

## Post #33 by @TravisBurgers (2019-11-11 15:04 UTC)

<p>I’m still not really sure what the difference between the extension and module are, but can the same image be used for both? How is this?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d8a89cb77f5ec9e40c24e5803a78502fa14205f6.png" alt="RawImageGuess" data-base62-sha1="uUEnMjjfCaNGgL6WAo7iPaHvwSG" width="128" height="128"><br>
The left side is the noise shown on RawImageGuess when the wrong header size is input. The right side is from a <a href="https://commons.wikimedia.org/wiki/File:Computed_tomography_of_human_brain_-_large.png" rel="noopener nofollow ugc">public domain CT scan of a brain</a>.</p>

---

## Post #34 by @lassoan (2019-11-11 16:41 UTC)

<p>Extension icon shows up in the extension manager. It typically has rounded border (see for example an editable Gimp image <a href="https://github.com/SlicerIGT/SlicerIGT/blob/master/SlicerIGTLogoDesign.xcf">here</a>) and often has short name of the extension written on it. Module icon shows up in the module list (icon height is the height of a single text line).</p>
<p>The unorganized/organized image content looks good, but don’t use a random noise but loading the same image using incorrect parameters. For example, Slicer’s MRHead sample data looks like this when RawImageGuess loads it with incorrect parameters:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de2455cbec970a68767b010d0b46e537e7030b42.jpeg" data-download-href="/uploads/short-url/vH9Qsv6R9dc3xe1ZdGklcYqE3Au.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de2455cbec970a68767b010d0b46e537e7030b42_2_507x500.jpeg" alt="image" data-base62-sha1="vH9Qsv6R9dc3xe1ZdGklcYqE3Au" width="507" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/de2455cbec970a68767b010d0b46e537e7030b42_2_507x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de2455cbec970a68767b010d0b46e537e7030b42.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/de2455cbec970a68767b010d0b46e537e7030b42.jpeg 2x" data-dominant-color="8A8A8A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">577×569 200 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Also, maybe make the split using a diagonal line instead of a vertical line, it may look a bit more interesting and distinctive.</p>

---

## Post #35 by @TravisBurgers (2019-11-11 22:09 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Here’s a pair of images that uses the MR Head data set any user can download in Slicer. I didn’t see any attribution requirements for that data set and it looks like some other extensions made use of it for their icons.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0dca30ed4f6e8210bd2c0a283f6ea312cfc13de.png" alt="RawImageGuessText" data-base62-sha1="tNG1DcIAeBUTYa7vd0wJz9RFmdU" width="256" height="256"></p>

---

## Post #36 by @lassoan (2019-11-12 00:40 UTC)

<p>I like this icon. Just one comment: Could you replace the strong red/green/blue colors with colors with a bit more subtle contrast? You can generate color schemes using online tools, such as <a href="https://coolors.co/fce1d6-f9c1a7-e2cbb1-cdceaf-8aa08f">this</a>. Can you upload the editable gimp file as well (upload somewhere and post the link here)? Thank you.</p>

---
