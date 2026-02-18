# How does slicer determine when referenced datasets are found?

**Topic ID**: 31885
**Date**: 2023-09-25
**URL**: https://discourse.slicer.org/t/how-does-slicer-determine-when-referenced-datasets-are-found/31885

---

## Post #1 by @Justin_Kirby (2023-09-25 13:51 UTC)

<p>When I load DICOM segmentation data from the Slicer DICOM module I will sometimes be told that it has found referenced datasets, and with other SEG objects I am not.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/6/a6c0dc2753e4bf94bb81e77be0871840027f270c.png" alt="image" data-base62-sha1="nNasySg1tzMsLvPsOi6XnM40uxm" width="542" height="456"></p>
<p>Can someone explain what tags are being evaluated to determine this?</p>

---

## Post #2 by @pieper (2023-09-25 14:01 UTC)

<p>Hi <a class="mention" href="/u/justin_kirby">@Justin_Kirby</a> - These would come from the <code>ReferencedSeriesSequence</code>, if the segmentation has one.  Slicer is just offering to load this so you can look at both together as a background with segmentatio overlay.  The <a href="https://github.com/QIICR/QuantitativeReporting/blob/8a6e61262f2b942ab8edc743418368167595bd98/DICOMPlugins/base/DICOMPluginBase.py#L59-L82">code is here</a>.  I believe you only get the option dialog if the referenced series or instances are in the current slicer database.</p>

---

## Post #3 by @Justin_Kirby (2023-09-25 15:09 UTC)

<p>Thanks Steve.  We had someone provide DICOM SEG data created with dcmqi to TCIA recently.  For some reason the relevant tags in their data were empty (perhaps <a class="mention" href="/u/fedorov">@fedorov</a> would know about this?).  When I noticed the issue and asked if this could be populated they did so via a custom python script (see below). However, Slicer still doesn’t prompt to open the related MR series after filling this in and I do have both the original MR and SEG series in my DICOM database.  If you see anything in their code that would explain this please let me know.  And thanks for the link to the relevant code in Slicer.  I’ll pass that along to our developers to see if we can implement some checks to ensure the relevant fields are populated in future data submissions.</p>
<pre><code class="lang-auto">from pydicom.dataset import Dataset
from pydicom.sequence import Sequence 

import os
import pydicom
import pandas as pd

import os
import pydicom
import pandas as pd


path_remind = '/Users/reubendo/Documents/data/ReMIND TCIA/manifest-1695134609823/ReMIND'
cases = [case for case in os.listdir(path_remind) if os.path.isdir(os.path.join(path_remind,case))]
len(cases)
dictionn = {'Seg 0x0020, 0x000E':[], 'MR 0x08,0x16':[], 'MR 0x08,0x18':[], 'MR 0x0020, 0x000E':[]}
for case in sorted(cases):
    path_case = os.path.join(path_remind, case)
    studies = [k for k in os.listdir(path_case) if os.path.isdir(os.path.join(path_case,k))]
    for study in studies:
        path_study = os.path.join(path_case, study)
        segmentations = [k for k in os.listdir(path_study) if 'seg' in k]
        images = [k for k in os.listdir(path_study) if not 'seg' in k and os.path.isdir(os.path.join(path_study, k))]
        for seg in segmentations:
            dcm_seg = pydicom.dcmread(os.path.join(path_study, seg, '1-1.dcm'))
            dcm_seg_framereference = dcm_seg[0x20,0x52].value
           
            candidates = []
            for i in images:
                path_i = os.path.join(path_study, i)
                dcms_i = [k for k in os.listdir(path_i) if 'dcm' in k]
                dcm_i = pydicom.dcmread(os.path.join(path_study, i, dcms_i[0]))
                if dcm_seg_framereference == dcm_i[0x20,0x52].value:
                    dictionn['Seg 0x0020, 0x000E'].append(dcm_seg[0x0020, 0x000E].value)
                    dictionn['MR 0x08,0x16'].append(dcm_i[0x08,0x16].value)
                    dictionn['MR 0x08,0x18'].append(dcm_i[0x08,0x18].value)
                    dictionn['MR 0x0020, 0x000E'].append(dcm_i[0x0020, 0x000E].value)
                    candidates.append(i)
                   
                    ds11 = Dataset()
                    ds11.add_new((0x0008,0x1150), 'UI',  dcm_i[0x08,0x16].value)
                    ds12 = Dataset()
                    ds12.add_new((0x0008,0x1155), 'UI',  dcm_i[0x08,0x18].value)
                    ds1 =  Sequence([ds11,ds12])

                    ds21 = Dataset()
                    ds21.add_new((0x0020, 0x000E), 'UI',  dcm_i[0x0020, 0x000E].value)
                    ds22 = Dataset()
                    ds22.add_new((0x0008,0x114A), 'SQ',  ds1)
                    ds2 = Sequence([ds22,ds21])

                    dcm_seg.add_new((0x0008,0x1115), 'SQ', ds2)

                    os.makedirs(f'./output/{case}/{study}/{seg}/', exist_ok=True)
                    pydicom.dcmwrite(f'./output/{case}/{study}/{seg}/1-1.dcm', dcm_seg)

            assert len(candidates)==1
</code></pre>

---

## Post #4 by @pieper (2023-09-25 15:31 UTC)

<p>I see <a class="mention" href="/u/fedorov">@fedorov</a> is responding.  I’ll just mention that since this is the REMIND data, I could work with Reuben and have a look at the datasets to troubleshoot if that’s easier than guessing.</p>

---

## Post #5 by @fedorov (2023-09-25 15:32 UTC)

<aside class="quote no-group" data-username="Justin_Kirby" data-post="3" data-topic="31885">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/justin_kirby/48/66502_2.png" class="avatar"> Justin_Kirby:</div>
<blockquote>
<p>We had someone provide DICOM SEG data created with dcmqi to TCIA recently. For some reason the relevant tags in their data were empty (perhaps <a class="mention" href="/u/fedorov">@fedorov</a> would know about this?</p>
</blockquote>
</aside>
<p>In order for the references to be populated by <code>dcmqi</code> the user should pass the pointer to the folder with the source DICOM series as an optional parameter to the converter. “We used dcmqi” is not enough, there should be review of how it was used, and what was the result to ensure they used it as recommended to enable features like this one.</p>
<aside class="quote no-group" data-username="Justin_Kirby" data-post="3" data-topic="31885">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/justin_kirby/48/66502_2.png" class="avatar"> Justin_Kirby:</div>
<blockquote>
<p>When I noticed the issue and asked if this could be populated they did so via a custom python script (see below).</p>
</blockquote>
</aside>
<p>I have to say I do not know DICOM well enough to remember what numeric tags mean, so it’s hard for me to check whether the result meets the expectations of the code referenced by <a class="mention" href="/u/pieper">@pieper</a> above. I am always impressed by people who know those by heart! <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>
<p>I would take the resulting file and compare DICOM dump against the organization of a SEG file where loading of the referenced series works, and try to find differences. Maybe you can share the relevant part of the dump of the output file (<code>ReferencedSeriesSequence</code> and <code>ReferencedImageSequence</code>). It is also always good to run <code>dciodvfy</code> on the output of any code that messes with the DICOM tags.</p>

---

## Post #6 by @Justin_Kirby (2023-09-25 16:00 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> if you’re able to work with them to resolve this I think they’d be very appreciative.  I know they are quite anxious to publish the data.  If it is not a simple fix we could potentially do a “version 2” release later on with the revised data.</p>
<p><a class="mention" href="/u/fedorov">@fedorov</a> thanks for the clarifications.  Sounds like they missed the optional parameter.</p>

---

## Post #7 by @pieper (2023-09-25 16:05 UTC)

<p>Yes, I’ve reached out and should be able to help as needed.  But the team is quite good so maybe it’ll get resolved by following the advice from <a class="mention" href="/u/fedorov">@fedorov</a> .</p>

---

## Post #8 by @reubendo (2023-09-25 16:40 UTC)

<p>Hi,</p>
<p>Following up on this, the problem is related to the order of the ReferencedSeriesSequence:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/QIICR/QuantitativeReporting/blob/8a6e61262f2b942ab8edc743418368167595bd98/DICOMPlugins/base/DICOMPluginBase.py#L70">
  <header class="source">

      <a href="https://github.com/QIICR/QuantitativeReporting/blob/8a6e61262f2b942ab8edc743418368167595bd98/DICOMPlugins/base/DICOMPluginBase.py#L70" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/QIICR/QuantitativeReporting/blob/8a6e61262f2b942ab8edc743418368167595bd98/DICOMPlugins/base/DICOMPluginBase.py#L70" target="_blank" rel="noopener nofollow ugc">QIICR/QuantitativeReporting/blob/8a6e61262f2b942ab8edc743418368167595bd98/DICOMPlugins/base/DICOMPluginBase.py#L70</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="60" style="counter-reset: li-counter 59 ;">
          <li>  """Puts a list of the referenced UID into the loadable for use</li>
          <li>  in the node if this is loaded."""</li>
          <li>  dcm = pydicom.read_file(loadable.files[0])</li>
          <li>  loadable.referencedInstanceUIDs = []</li>
          <li>  self._addReferencedSeries(loadable, dcm)</li>
          <li>  self._addReferencedImages(loadable, dcm)</li>
          <li>  loadable.referencedInstanceUIDs = list(set(loadable.referencedInstanceUIDs))</li>
          <li></li>
          <li>def _addReferencedSeries(self, loadable, dcm):</li>
          <li>  if hasattr(dcm, "ReferencedSeriesSequence"):</li>
          <li class="selected">    if hasattr(dcm.ReferencedSeriesSequence[0], "SeriesInstanceUID"):</li>
          <li>      for f in slicer.dicomDatabase.filesForSeries(dcm.ReferencedSeriesSequence[0].SeriesInstanceUID):</li>
          <li>        refDCM = pydicom.read_file(f)</li>
          <li>        loadable.referencedInstanceUIDs.append(refDCM.SOPInstanceUID)</li>
          <li>      loadable.referencedSeriesUID = dcm.ReferencedSeriesSequence[0].SeriesInstanceUID</li>
          <li></li>
          <li>def _addReferencedImages(self, loadable, dcm):</li>
          <li>  if hasattr(dcm, "ReferencedImageSequence"):</li>
          <li>    for item in dcm.ReferencedImageSequence:</li>
          <li>      if hasattr(item, "ReferencedSOPInstanceUID"):</li>
          <li>        loadable.referencedInstanceUIDs.append(item.ReferencedSOPInstanceUID)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Inspired by this <a href="https://dicom.innolitics.com/ciods/segmentation/common-instance-reference/00081115/0008114a" rel="noopener nofollow ugc">convention</a><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33caefcfe9ac568f88f11cf0cef731999f1b8c8d.png" alt="image" data-base62-sha1="7ob8K2tDc4gFSZnmdfluLQmwpeB" width="650" height="220"></p>
<p>I considered that the SeriesInstanceUID was the second element of the sequence. It seems that it should be the first element in slicer.</p>
<p>If we want to stick to the first element, then the code just needs to be modify but changing<br>
<code>ds2 = Sequence([ds22,ds21])</code> into <code>ds2 = Sequence([ds21,ds22])</code>.</p>

---

## Post #9 by @pieper (2023-09-25 17:02 UTC)

<p>This is great Reuben <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<aside class="quote no-group" data-username="reubendo" data-post="8" data-topic="31885">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/35a633/48.png" class="avatar"> reubendo:</div>
<blockquote>
<p>convention</p>
</blockquote>
</aside>
<p>yes, it’s a bit arbitrary at some level, but it’s not just a convention, it’s dicom, which is an ISO standard.  So if we stick to that we can just refer to the standard and never have to document things like this.  We don’t want <a href="https://xkcd.com/2830/">to live in a world without global standards!</a></p>
<aside class="quote no-group" data-username="reubendo" data-post="8" data-topic="31885">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/35a633/48.png" class="avatar"> reubendo:</div>
<blockquote>
<p>I considered that the SeriesInstanceUID was the second element of the sequence. It seems that it should be the first element in slicer.</p>
</blockquote>
</aside>
<p>Yes, I would think so too, that the class UID should go first, and the Instance UID should go second in the sequence.  Do we think that’s a bug in the Quantitative Reporting extension code?</p>

---

## Post #10 by @fedorov (2023-09-25 18:43 UTC)

<aside class="quote no-group" data-username="pieper" data-post="9" data-topic="31885">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Yes, I would think so too, that the class UID should go first, and the Instance UID should go second in the sequence. Do we think that’s a bug in the Quantitative Reporting extension code?</p>
</blockquote>
</aside>
<p>I didn’t quite understand the details in the above, but I did look at a sample output from <code>dcmqi</code> and confirmed that the order is what I would expect.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/459c53fb69f570d4250ed4f40b3ad2e17aa6346b.png" alt="image" data-base62-sha1="9VNSmjPUmbRLxXRXnmkaB8Hm5Wb" width="536" height="178"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c19c1c4f4a92ba201a3f20b9d07c0c5efe6a62db.png" alt="image" data-base62-sha1="rCKCgrOmLv7WpU2Rf8oic8eYoaf" width="469" height="114"></p>
<p>The snippets above are from a SEG generated using <code>dcmqi</code> for the C4KC-KiTS collection. I looked at the segmentations for the subject KiTS-00001 study, which is here: <a href="https://viewer.imaging.datacommons.cancer.gov/viewer/1.3.6.1.4.1.14519.5.2.1.6919.4624.138299679445949029090789149621">https://viewer.imaging.datacommons.cancer.gov/viewer/1.3.6.1.4.1.14519.5.2.1.6919.4624.138299679445949029090789149621</a>.</p>

---

## Post #11 by @pieper (2023-09-25 19:49 UTC)

<p>Ah, maybe we are getting down to this real issue.</p>
<p>Looking at the earlier version of the data, it looks like the structure of the files is a bit different.  Rather than an item with two tags like <a class="mention" href="/u/fedorov">@fedorov</a>’s example and the innolitics figure, the REMIND file has two items each with one tag.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/684c3eea4031233bdf3e30eaf7b9b69125dd20c4.png" data-download-href="/uploads/short-url/eSF0MT5BAQUziw37zDnL6rEMUu0.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/684c3eea4031233bdf3e30eaf7b9b69125dd20c4_2_690x122.png" alt="image" data-base62-sha1="eSF0MT5BAQUziw37zDnL6rEMUu0" width="690" height="122" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/684c3eea4031233bdf3e30eaf7b9b69125dd20c4_2_690x122.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/684c3eea4031233bdf3e30eaf7b9b69125dd20c4_2_1035x183.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/684c3eea4031233bdf3e30eaf7b9b69125dd20c4.png 2x" data-dominant-color="D8E1EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1090×193 33 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So now I"m not sure why changing the order of the sequence statement worked for <a class="mention" href="/u/reubendo">@reubendo</a>.</p>

---

## Post #12 by @fedorov (2023-09-25 19:57 UTC)

<p>Yes, I did notice that, but since <a class="mention" href="/u/reubendo">@reubendo</a> said the problem is solved, decided not to raise it.</p>
<p>Clearly, that sequence is not populated the way it should be populated. It should list all of the instances of the series that were segmented - not just one (unless only one slice was segmented). And yes, it should list <code>ReferencedSOPClassUID</code> and <code>ReferencedSOPInstanceUID</code> as siblings within the sequence item.</p>
<p>As I mentioned earlier, it is <strong>always</strong> a good idea to run <a href="https://www.dclunie.com/dicom3tools/dciodvfy.html"><code>dciodvfy</code></a> if one manipulates DICOM metadata. I am pretty sure this issue will be flagged by the validator.</p>

---

## Post #13 by @Justin_Kirby (2023-09-25 20:11 UTC)

<p>I am not sure what errors may exist in this latest version of the data, but I do know our team ran dciodvfy against the original version of the data generated by dcmqi and dciodvfy did not complain about the absence of this information.  That’s why it wasn’t until I went to load the data into Slicer that we uncovered the issue.  Could these fields be optional per the official DICOM rules?</p>
<p>On a related note, is that why the parameter in dcmqi that <a class="mention" href="/u/fedorov">@fedorov</a> mentioned earlier is optional instead of mandatory?</p>
<p>Should we be requesting a change to the DICOM standard and/or updating tools like dcmqi to require it?  Or are there legitimate reasons why one should be able to create segmentation data without this reference info?</p>

---
