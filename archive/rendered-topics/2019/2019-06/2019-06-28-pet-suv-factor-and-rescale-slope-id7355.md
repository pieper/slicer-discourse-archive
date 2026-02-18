# PET SUV factor and rescale slope

**Topic ID**: 7355
**Date**: 2019-06-28
**URL**: https://discourse.slicer.org/t/pet-suv-factor-and-rescale-slope/7355

---

## Post #1 by @pocolya (2019-06-28 14:58 UTC)

<p>I am working on PET images and I’d like to convert DICOM PET images into SUV factorised images on the data that took into account rescale slope and intercept. I can’t find any sure evidence that the SUV calculated with PETDICOMExtension uses the data AFTER the rescale slope and intercept calculation. Except a mention here which is not obvious enough to me :</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/QIICR/Slicer-PETDICOMExtension/blob/master/SUVFactorCalculatorCLI/SUVFactorCalculator.cxx" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/QIICR/Slicer-PETDICOMExtension/blob/master/SUVFactorCalculatorCLI/SUVFactorCalculator.cxx" target="_blank" rel="nofollow noopener">QIICR/Slicer-PETDICOMExtension/blob/master/SUVFactorCalculatorCLI/SUVFactorCalculator.cxx</a></h4>
<pre><code class="lang-cxx">
#include "SUVFactorCalculatorCLP.h"

// VTK includes
#include &lt;vtkGlobFileNames.h&gt;
#include &lt;vtksys/Directory.hxx&gt;

// ITK includes
#include &lt;itkGDCMSeriesFileNames.h&gt;
#include &lt;itkImageSeriesReader.h&gt;
#include &lt;itkImageFileReader.h&gt;
#include &lt;itkNrrdImageIO.h&gt;
#include &lt;itkImageFileWriter.h&gt;
#include &lt;itkImageRegionConstIterator.h&gt;
#include &lt;itkImageDuplicator.h&gt;
#include "itkGDCMImageIO.h"
#include "itkNumericTraits.h"

#undef HAVE_SSTREAM
#include "itkDCMTKFileReader.h"
</code></pre>

  This file has been truncated. <a href="https://github.com/QIICR/Slicer-PETDICOMExtension/blob/master/SUVFactorCalculatorCLI/SUVFactorCalculator.cxx" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>Other than that, the extension does the job for me for one or few images. If I want to convert few hundreds of them, how do you recommend to proceed? I can’t seem to find a proper python library for this.</p>

---

## Post #2 by @lassoan (2019-06-28 23:22 UTC)

<p>See how to run CLI modules from Python here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python</a></p>

---

## Post #3 by @fedorov (2019-06-29 03:42 UTC)

<p>That extension is using ITK reader to read the DICOM dataset, and then applies SUV correction to the voxel intensities. ITK reader will apply rescale/slope, so you won’t see it in the code of the extension. That’s the way I think it works. <a class="mention" href="/u/chribaue">@chribaue</a> can you comment?</p>

---

## Post #4 by @chribaue (2019-07-01 13:24 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a>. You are right, the standard ITK readers already apply rescale slope and intercept.</p>

---

## Post #5 by @pocolya (2019-07-01 13:54 UTC)

<p>Thank you, I am glad to have this confirmed.</p>

---

## Post #6 by @pocolya (2019-07-01 14:19 UTC)

<p>I’ve looked into using CLI from Python, but it does not seem to be straightforward. I am going to try Nipet for this purpose.<br>
Thank you for the answer!</p>

---

## Post #7 by @pocolya (2019-07-09 10:01 UTC)

<p>The CLI does not seem straightforward to me, so I’ve recoded my Python SUV factor calculation according to this pseudo-code <a href="https://qibawiki.rsna.org/index.php/Standardized_Uptake_Value_(SUV)" rel="nofollow noopener">https://qibawiki.rsna.org/index.php/Standardized_Uptake_Value_(SUV)</a>. Well, for some examples it gives just the same results as I had before with a simpler DICOM tags verification.</p>
<p>My trouble is that my suv image is not corresponding to the one with PETDICOM extension in Slicer. For the reference, I am using DCM2Niix to convert my dicoms to Nifti or to Analyze, Nibabel to extract the data. Does anyone have an idea what might be wrong?</p>
<p>Also, I can’t jsut extract the SUV factor for the whole image? Otherwise I have to measure the statistics from the image to compare the results.</p>

---

## Post #8 by @ni-wei (2019-07-18 06:55 UTC)

<p><a class="mention" href="/u/pocolya">@pocolya</a> I also intend to programmatically calculate the SUV_bw values of DICOM PET images. My efforts so far are not successful. Could you kindly share with me your progress? Thank you!</p>

---

## Post #9 by @fedorov (2019-07-18 14:58 UTC)

<aside class="quote no-group" data-username="pocolya" data-post="7" data-topic="7355">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pocolya/48/4067_2.png" class="avatar"> pocolya:</div>
<blockquote>
<p>The CLI does not seem straightforward to me</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/pocolya">@pocolya</a> can you tell us more precisely - what does not seem straightforward to you about the Slicer SUV calculator CLI? Is it about using CLI from command line, running it programmatically, specifying arguments, interpreting output, understanding documentation?</p>

---

## Post #10 by @ni-wei (2019-07-19 01:44 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> Could you kindly show me an example on programmatically (i) load a few PET DICOM series, (ii) call the SUV calculator CLI to compute them in the batch mode (as mentioned in <a href="http://qiicr.org/tool/PETDICOM/" rel="nofollow noopener">http://qiicr.org/tool/PETDICOM/</a>), and (iii) save them as NIFTI files?</p>
<p>Thank you very much!</p>

---

## Post #11 by @fedorov (2019-07-19 14:53 UTC)

<p>Do you want to do it in a Slicer module, or in another batch script where you want to minimize dependencies on Slicer?</p>

---

## Post #12 by @pocolya (2019-07-19 15:24 UTC)

<p>Thank you for your replies.</p>
<p>I would like to do it efficiently for many patients.</p>
<p>CLI didn’t seem straightforward to me as I would need to create an environment as in Slicer, considering I already had a python code, I preferred not to invest my time right now in making it work this way. However, I might need using PETSUV conversion module in future. I will check it next week, but it seemed like it does not give the same SUV values as my code written according to the above cited link.</p>
<p>One thing I noticed when applying a mask on a SUV image, and then converting it label image is that I would loose the original image dimension. I found how to get over it (by exporting from the Segmentation module), however I just notice that there are so many not straightforward things with Slicer. Like, when editing a segmentation (in segmentation editor), for some reason, some parts are not accessible for painting, even though I checked using all the visible parts and so on. Any idea of how to overcome it?</p>

---

## Post #13 by @pocolya (2019-07-19 15:25 UTC)

<p>If you want my Python SUV code, write me a private message with your email.</p>

---

## Post #14 by @fedorov (2019-07-19 16:19 UTC)

<p>Based on your question, I think you want to do it outside of Slicer. If this is indeed the case, here are the steps, which will not depend on Slicer environment or any Slicer-specific python functionality.</p>
<p><strong>Step 1</strong>: Sort your DICOM files into series, and identify PET series. I recommend you use <a href="https://github.com/pieper/dicomsort" rel="nofollow noopener">dicomsort</a> for this task. You can run it, for example, with the following parameters to include modality in the name of the sorted series folder:</p>
<pre><code class="lang-bash">$ python dicomsort.py &lt;input folder&gt;  &lt;sorted_folder&gt;/%PatientID/%StudyDate/%SeriesNumber-%Modality-%SeriesDescription/%SOPInstanceUID.dcm
</code></pre>
<p><strong>Step 2</strong>: Run SUV calculator command line tool. You can install it as an extension, and then navigate to the folder with the installed extensions to locate it. Instructions how to run a Slicer CLI will vary depending on the operating system you use. On Mac, you can run the CLI executable directly. CLI will take as input directory with the DICOM PET files, and will output a <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_A.46.html" rel="nofollow noopener">DICOM Real World Value Mapping IOD</a> instance (the macro that contains the SUV factor is described <a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.16.2.html#table_C.7.6.16-12" rel="nofollow noopener">here</a>) saved into a new file and a text file with the computed SUV factor(s):</p>
<pre><code class="lang-bash">$ /Applications/Slicer.app/Contents/Extensions-28390/PETDICOMExtension/lib/Slicer-4.11/cli-modules/SUVFactorCalculator -p sorted/QIN-HEADNECK-01-0366/19860303/UnknownSeriesNumber-PT-PET_WB_0 -r . --returnparameterfile output_parameters.txt
saving numbers to
Input parameters okay...
ATTN/DECAY correction detected.
Decay correction START detected.
                  INJECTED DOSE: 3.8591e+08
                  RAD. START TIME: 39180
                  SERIES TIME: 44254.7
                  DECAYED DOSE: 226226
Warning: No patient height detected.  Cannot determine SUVbsa, SUVlbm, and SUVibw conversion factors.
227 files total
Inserted: QIN-HEADNECK-01-0366
Inserted: QIN-HEADNECK-01-0366
Inserted: M
Inserted: YES
Inserted: DCM:113100/113105/113107/113108/113109/113111
Inserted: 1.3.6.1.4.1.14519.5.2.1.2744.7002.103466790444463274538008985123
Inserted: 19860303
Inserted: 120336.292000
Inserted:
Inserted: 2076699673350889
Inserted: Thorax^1HEAD_NECK_PETCT
Inserted: 059Y
Inserted: 63.2
saving to ./1.2.276.0.7230010.3.1.4.0.86172.1563548276.147671.dcm
0 0.000279366 0 0
</code></pre>
<p>The last line of the console will actually output various SUV factors calculated by the CLI (and I should add more descriptive printout on the console).</p>
<p>The <code>output_parameters.txt</code> file will contain the following lines with the SUV factor(s):</p>
<pre><code class="lang-nohighlight">SUVbwConversionFactor = 0.000279366
SUVlbmConversionFactor = 0
SUVbsaConversionFactor = 0
SUVibwConversionFactor = 0
</code></pre>
<p>The relevant part of the DICOM RWVM instance created by the CLI are below (output produced by the DCMTK <a href="https://support.dcmtk.org/docs/dcmdump.html" rel="nofollow noopener"><code>dcmdump</code> tool</a>, also available via the <a href="https://atom.io/packages/dicom-dump" rel="nofollow noopener"><code>dicom-dump</code> package of Atom</a>):</p>
<pre><code class="lang-nohighlight">    (0040,9096) SQ (Sequence with undefined length #=1)     # u/l, 1 RealWorldValueMappingSequence
      (fffe,e000) na (Item with undefined length #=8)         # u/l, 1 Item
        (0028,3003) LO [Standardized Uptake Value body weight]  #  38, 1 LUTExplanation
        (0040,08ea) SQ (Sequence with undefined length #=1)     # u/l, 1 MeasurementUnitsCodeSequence
          (fffe,e000) na (Item with undefined length #=3)         # u/l, 1 Item
            (0008,0100) SH [{SUVbw}g/ml]                            #  12, 1 CodeValue
            (0008,0102) SH [UCUM]                                   #   4, 1 CodingSchemeDesignator
            (0008,0104) LO [Standardized Uptake Value body weight]  #  38, 1 CodeMeaning
          (fffe,e00d) na (ItemDelimitationItem)                   #   0, 0 ItemDelimitationItem
        (fffe,e0dd) na (SequenceDelimitationItem)               #   0, 0 SequenceDelimitationItem
        (0040,9210) SH [{SUVbw}g/ml]                            #  12, 1 LUTLabel
        (0040,9211) US 26403                                    #   2, 1 RealWorldValueLastValueMapped
        (0040,9216) SS 0                                        #   2, 1 RealWorldValueFirstValueMapped
        (0040,9220) SQ (Sequence with undefined length #=2)     # u/l, 1 QuantityDefinitionSequence
          (fffe,e000) na (Item with undefined length #=3)         # u/l, 1 Item
            (0040,a040) CS [CODE]                                   #   4, 1 ValueType
            (0040,a043) SQ (Sequence with undefined length #=1)     # u/l, 1 ConceptNameCodeSequence
              (fffe,e000) na (Item with undefined length #=3)         # u/l, 1 Item
                (0008,0100) SH [G-C1C6]                                 #   6, 1 CodeValue
                (0008,0102) SH [SRT]                                    #   4, 1 CodingSchemeDesignator
                (0008,0104) LO [Quantity]                               #   8, 1 CodeMeaning
              (fffe,e00d) na (ItemDelimitationItem)                   #   0, 0 ItemDelimitationItem
            (fffe,e0dd) na (SequenceDelimitationItem)               #   0, 0 SequenceDelimitationItem
            (0040,a168) SQ (Sequence with undefined length #=1)     # u/l, 1 ConceptCodeSequence
              (fffe,e000) na (Item with undefined length #=3)         # u/l, 1 Item
                (0008,0100) SH [126400]                                 #   6, 1 CodeValue
                (0008,0102) SH [DCM]                                    #   4, 1 CodingSchemeDesignator
                (0008,0104) LO [Standardized Uptake Value]              #  26, 1 CodeMeaning
              (fffe,e00d) na (ItemDelimitationItem)                   #   0, 0 ItemDelimitationItem
            (fffe,e0dd) na (SequenceDelimitationItem)               #   0, 0 SequenceDelimitationItem
          (fffe,e00d) na (ItemDelimitationItem)                   #   0, 0 ItemDelimitationItem
          (fffe,e000) na (Item with undefined length #=3)         # u/l, 1 Item
            (0040,a040) CS [CODE]                                   #   4, 1 ValueType
            (0040,a043) SQ (Sequence with undefined length #=1)     # u/l, 1 ConceptNameCodeSequence
              (fffe,e000) na (Item with undefined length #=3)         # u/l, 1 Item
                (0008,0100) SH [G-C036]                                 #   6, 1 CodeValue
                (0008,0102) SH [SRT]                                    #   4, 1 CodingSchemeDesignator
                (0008,0104) LO [Measurement Method]                     #  18, 1 CodeMeaning
              (fffe,e00d) na (ItemDelimitationItem)                   #   0, 0 ItemDelimitationItem
            (fffe,e0dd) na (SequenceDelimitationItem)               #   0, 0 SequenceDelimitationItem
            (0040,a168) SQ (Sequence with undefined length #=1)     # u/l, 1 ConceptCodeSequence
              (fffe,e000) na (Item with undefined length #=3)         # u/l, 1 Item
                (0008,0100) SH [126410]                                 #   6, 1 CodeValue
                (0008,0102) SH [DCM]                                    #   4, 1 CodingSchemeDesignator
                (0008,0104) LO [SUV body weight calculation method]     #  34, 1 CodeMeaning
              (fffe,e00d) na (ItemDelimitationItem)                   #   0, 0 ItemDelimitationItem
            (fffe,e0dd) na (SequenceDelimitationItem)               #   0, 0 SequenceDelimitationItem
          (fffe,e00d) na (ItemDelimitationItem)                   #   0, 0 ItemDelimitationItem
        (fffe,e0dd) na (SequenceDelimitationItem)               #   0, 0 SequenceDelimitationItem
        (0040,9224) FD 0                                        #   8, 1 RealWorldValueIntercept
        (0040,9225) FD 0.000279366                              #   8, 1 RealWorldValueSlope
      (fffe,e00d) na (ItemDelimitationItem)                   #   0, 0 ItemDelimitationItem
    (fffe,e0dd) na (SequenceDelimitationItem)               #   0, 0 SequenceDelimitationItem
</code></pre>
<p>The SUV factor is stored in the <code>RealWorldValueSlope</code> attribute, and the preceeding <code>QuantityDefinitionSequence</code> can be used to get the SUV calculation method and units. Other parts of the DICOM RWVM instance store patient information, references to the PET instances to which the SUV factor applies, etc.</p>
<p>Over-simplifying things, you can easily access the SUV factor (the same that you will find in the text file, but with a lot more detailed metadata) using <a href="https://pydicom.github.io/" rel="nofollow noopener"><code>pydicom</code></a> as follows:</p>
<pre><code class="lang-python">import pydicom
d = pydicom.read_file('&lt;RWVM file name&gt;')
suv = d.ReferencedImageRealWorldValueMappingSequence[0].RealWorldValueMappingSequence[0].RealWorldValueSlope
</code></pre>
<p><strong>Step 3</strong>: you can use <code>dcm2niix</code> to generate a 3d PET volume from the files in the PET series folder you prepared in Step 1 by running <code>dcm2niix .</code> in the folder with the PET series files.</p>
<p><strong>Step 4</strong>: you can load the reconstructed PET volume using <code>itk-python</code> or <code>SimpleITK</code> and apply the SUV factor by multiplying the image by the SUV constant. You can then save the resulting image as a new NIfTI file - see examples on file IO for SimpleITK <a href="http://insightsoftwareconsortium.github.io/SimpleITK-Notebooks/Python_html/03_Image_Details.html#Reading-and-Writing" rel="nofollow noopener">here</a>.</p>

---

## Post #15 by @ni-wei (2019-07-20 09:09 UTC)

<p>Hi Andrey,</p>
<p>I want to it in a batch script with minimal Slicer dependencies. Really appeciate your step-by-step guidance and recommendations in your latest reply. Thank you very much!</p>

---
