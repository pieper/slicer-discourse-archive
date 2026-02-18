# Unable to open SEG Modality file

**Topic ID**: 19881
**Date**: 2021-09-27
**URL**: https://discourse.slicer.org/t/unable-to-open-seg-modality-file/19881

---

## Post #1 by @kaushikdasroy (2021-09-27 14:32 UTC)

<p>Operating system: Windows 10 Pro<br>
Slicer version: 4.11.20210226 r29738 / 7a593c8<br>
Expected behavior: Open the segmentation file<br>
Actual behavior: Error message</p>
<p>I am trying to open a DICOM SEG file in the slicer and getting an error. The log and the SEG file in the drive -<br>
<a href="https://drive.google.com/drive/folders/1_Us1UQf6RsQw6Do_qU605uEVWNPosPDk?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1_Us1UQf6RsQw6Do_qU605uEVWNPosPDk?usp=sharing</a></p>
<p>Please suggest what might be the problem.<br>
Thanks!</p>

---

## Post #2 by @pieper (2021-09-27 19:53 UTC)

<p>Did you try installing the Quantitative Reporting extension?  This is where the SEG plugin is provided.</p>

---

## Post #3 by @kaushikdasroy (2021-09-27 20:21 UTC)

<p>I have the following extensions - Quantitative reporting, slicerRT, slicerRadiomics, slicerDevelopmentToolbox and few more (DCMQI, longitudinalPETCT, petDicomExtension)</p>
<p>Thanks for checking this!</p>

---

## Post #4 by @lassoan (2021-09-27 22:06 UTC)

<p>The problem is that the segment contains an invalid color. See <code>recommendedDisplayRGBValue</code> in the metadata extracted by DCMQI tool:</p>
<pre><code class="lang-auto">{
   "BodyPartExamined" : "",
   "ClinicalTrialSeriesID" : "",
   "ClinicalTrialTimePointID" : "",
   "ContentCreatorName" : "",
   "InstanceNumber" : "1",
   "SeriesDescription" : "CAUTION: Research Use Only. NVIDIA Clara generated DICOM SEG for Axial Chest CT COVID-19",
   "SeriesNumber" : "4516",
   "segmentAttributes" : [
      [
         {
            "SegmentAlgorithmName" : "AI Organ Segmentation",
            "SegmentAlgorithmType" : "AUTOMATIC",
            "SegmentDescription" : "",
            "SegmentLabel" : "Lung-seg",
            "SegmentedPropertyCategoryCodeSequence" : {
               "CodeMeaning" : "Anatomical Structure",
               "CodeValue" : "T-D0050",
               "CodingSchemeDesignator" : "SRT"
            },
            "SegmentedPropertyTypeCodeSequence" : {
               "CodeMeaning" : "Organ",
               "CodeValue" : "T-D0050",
               "CodingSchemeDesignator" : "SRT"
            },
            "labelID" : 1,
            "recommendedDisplayRGBValue" : [ 4294966216, 74, 193 ]
         }
      ]
   ]
}
</code></pre>
<p>Please report this error to NVidia Clara developers! Thank you.</p>
<p>Problems with this segmentation object:</p>
<ul>
<li>Probably they thought that the color is specified as RGB value, but actually it is encoded as CIELab.</li>
<li>The segment type is just “Organ”, which is useless. The proper term would have been “Lung”.</li>
<li>Old SRT codes are used instead of SCT.</li>
<li>Clara version number is not included. This is important, because it allows fixing up problems in DICOM files retrospectively without relying on any heuristics. For example, we could determine that segment color “looks like” RGB and then interpret it as RGB, but it would be much better if we could tell it from the <a href="https://dicom.innolitics.com/ciods/segmentation/general-equipment/00181020">software version</a>.</li>
</ul>

---

## Post #5 by @kaushikdasroy (2021-09-28 17:12 UTC)

<p>This is response from clara :</p>
<p>As for the Clara DICOM Seg Writer, it actually does NOT set the <strong>optional</strong> attribute for recommended color for the label(s). It is likely DCMQI was generating default for the absent optional attribute, which then caused you to think Clara was providing it. Please use DCMDUMP or others to inspect and compare.</p>
<p>Also, the attributed that you mentioned has been retired and replaced with the recommended CIELab value attribute, per <a href="http://dicom.nema.org/medical/Dicom/2018d/output/chtml/part03/sect_C.10.7.html" rel="noopener nofollow ugc">DICOM Part 3</a>,</p>
<p><code>Graphic Layer Recommended Display RGB Value (0070,0067) was previously used in this Module, but has been retired and its function replaced by Graphic Layer Recommended Display CIELab Value (0070,0401). See PS3.3-2004.</code></p>
<p>Other viewer can handle the the absence of this attribute, as it is NOT a Type 1 attribute at all.</p>

---

## Post #6 by @lassoan (2021-09-28 18:28 UTC)

<aside class="quote no-group" data-username="kaushikdasroy" data-post="5" data-topic="19881">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/bc8723/48.png" class="avatar"> kaushikdasroy:</div>
<blockquote>
<p>As for the Clara DICOM Seg Writer, it actually does NOT set the <strong>optional</strong> attribute for recommended color for the label(s).</p>
</blockquote>
</aside>
<p>In the file that you shared, the segment color was specified, so either the Clara DICOM Seg Writer actually does set the attribute, or the file was reprocessed with some other software before given to you. The value that is stored in the file looks like an RGB value, so most likely Clara developers did not know that they had to use CIELab color space:</p>
<pre><code class="lang-auto">[0062,0002]	SegmentSequence		SQ	266
	[fffe,e000]	Item		na	250
		[0062,000d]	RecommendedDisplayCIELabValue	[3] 128, 174, 128	US	6
</code></pre>
<p>In segmentation objects you cannot specify color in RGB color space, but only CIELab is allowed, in <a href="https://dicom.innolitics.com/ciods/segmentation/segmentation-image/00620002/0062000d">Recommended Display CIELab Value Attribute (0062,000D)</a>. I don’t think that the (0070,0067) and (0070,0401) attributes that you referenced are related to DICOM Segmentation Object IOD.</p>
<p>Slicer can handle the missing value without any problem, but we have not came across a corrupted color before and the out-of-range value caused a GUI update issue. I’ve fixed this issue yesterday, so today’s Slicer Preview Release can open DICOM Segmentation Objects even if RecommendedDisplayCIELabValue does not correspond to a valid RGB value:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/764b4323ef4c64c62bc5a518b9a16512ab3063bc.png" data-download-href="/uploads/short-url/gStAADAvJgMkYpToPVHWRtE9x5G.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/764b4323ef4c64c62bc5a518b9a16512ab3063bc_2_690x419.png" alt="image" data-base62-sha1="gStAADAvJgMkYpToPVHWRtE9x5G" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/764b4323ef4c64c62bc5a518b9a16512ab3063bc_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/764b4323ef4c64c62bc5a518b9a16512ab3063bc_2_1035x628.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/764b4323ef4c64c62bc5a518b9a16512ab3063bc_2_1380x838.png 2x" data-dominant-color="3F3340"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1371 446 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you contact Clara developers about the above described issues then please copy here the link to the bug report link so that we can follow up.</p>

---

## Post #7 by @lassoan (2021-09-29 05:12 UTC)

<p>I’ve found the discussion with Clara developers: <a href="https://forums.developer.nvidia.com/t/invalid-color-in-segmentation-not-opening-segmentation-in-slicer/190271" class="inline-onebox">Invalid color in segmentation - not opening segmentation in slicer - Clara Deploy SDK - NVIDIA Developer Forums</a></p>

---

## Post #8 by @kaushikdasroy (2021-10-01 02:34 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> , thanks for taking this up with Clara team and the slicer release. I saw your response. It is helpful.</p>

---

## Post #9 by @lassoan (2021-10-01 02:51 UTC)

<p>Also note that I’ve updated Slicer a few days ago, so the current Slicer Preview Release can load the the file (even though the segment color is invalid).</p>

---

## Post #10 by @BrianOBrien (2024-03-06 00:11 UTC)

<p>I noticed this thread today as I am a new user here.<br>
I noticed this thread is quite old but the data looked interesting.<br>
I uploaded it and dumped the dicom and found this:</p>
<p>Odd the pixel module seems,</p>
<p>Samples per pixel is 256<br>
Number of frames is 320<br>
Rows 2<br>
Cols 2<br>
Bits Allocated 256</p>

---
