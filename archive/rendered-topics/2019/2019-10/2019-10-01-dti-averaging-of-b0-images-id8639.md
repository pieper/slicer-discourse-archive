---
topic_id: 8639
title: "Dti Averaging Of B0 Images"
date: 2019-10-01
url: https://discourse.slicer.org/t/8639
---

# DTI, averaging of b0 images

**Topic ID**: 8639
**Date**: 2019-10-01
**URL**: https://discourse.slicer.org/t/dti-averaging-of-b0-images/8639

---

## Post #1 by @JohnK (2019-10-01 17:11 UTC)

<p>Hi, I have been performing tractography with Slicer 4.10.2 (Windows). I have to say the results have been super impressive.I would like to know how slicer deals with multiple b0 scans.<br>
I have 63 volumes. Under “Volumes” module with the “DWI Component” slider,  I see the b0 volumes are at <span class="hashtag">#0</span>, 31, and 62. The scans were done under sedation and there is no clearly detectable movement or eddy artifact.</p>
<p>– Does slicer average these b0 volumes?<br>
If not, how can I do that?</p>
<p>– I am new to DTI, and I hope to publish my data. Is there a reference to the standard methodology that 3Dslicer uses? I am guessing it is not TBSS? I will also be checking my results with UKF, but should I just go right to UKF? My subjects have known white matter disease in the context of metabolic / mitochondrial disorders.</p>
<p>Lastly (and  not a big issue) when converting exported DICOM diffusion volumes from the NilRead viewer, I get a lot of these errors:</p>
<p>Diffusion-weighted DICOM Import (DWIConvert) standard error:<br>
E: can’t change to unencapsulated representation for pixel data<br>
E: can’t determine ‘PhotometricInterpretation’ of decompressed image<br>
E: mandatory attribute ‘PhotometricInterpretation’ is missing or can’t be determined…</p>
<p>Is that because the DICOM download needs a special header for 3DSlicer?</p>
<p>Thanks very much for your help.<br>
John Kelly</p>

---

## Post #2 by @ljod (2019-10-01 17:37 UTC)

<p>Hi! There’s no need to average the b0 images. SlicerDMRI can use them all.</p>
<p>The use of DTI vs UKF tractography depends on your goal and on the type of scan. Let us know the b-values and number of gradient directions.</p>
<p>No Slicer does not use TBSS. Give us more of an idea of the goal and we can help with methods description.</p>
<p>Please try the dcm2nii module and let us know if the DICOM reading works better for you.</p>

---

## Post #3 by @JohnK (2019-10-01 17:49 UTC)

<p>Thanks for the quick reply.</p>
<p>b-value is 1000 and 30 directions. Unfortunately Other scans will be at 10 directions, but still appears to have good results</p>
<p>The details of the study are complex, but the simple story is that we suspect there is near anatomical absence vs complete dysfunction of superior fasciculus pathways from the occipital lobe (based on volume loss in anatomical T1 /t2 imaging with additional evoked potential recordings). So the issue is providing evidence that the pathway is present (or not).  With the same parameters (start and stopping thresholds modified to be lowered), we get excellent results for occipital lobe to temporal lobe, corpus callosum, cortico-spinal, even cerebellum looks great. So sensitivity is important here.</p>
<p>With Dcm2nii I get an error (I have replaced subjectID stuff with XXXXXXX)</p>
<p>Command ‘[u’C:/Users/jkelly/AppData/Roaming/NA-MIC/Extensions-28257/SlicerDcm2nii/lib/Slicer-4.10/qt-scripted-modules\\Resources\\bin\\dcm2niix’, ‘-1’, ‘-d’, ‘0’, ‘-f’, ‘tmp7jvaws’, ‘-o’, ‘C:/Users/jkelly/AppData/Local/Temp/Slicer/__SlicerTemp__’, ‘-e’, ‘y’, ‘-z’, ‘y’, ‘O:\\Slicer\\SM_Disconnect\XXXXXXX’]’ returned non-zero exit status 2</p>
<p>fyi, tried DICOM patcher - gives me<br>
Examining .\xxxxxxxxxxxxxxxxx.dcm…<br>
Patching…<br>
Writing DICOM…<br>
Unexpected error: Invalid tag (0000, 0000): Unknown Value Representation ‘Po’ in tag (0000, 0000)</p>
<p>I’ll try other things…</p>
<p>You guys provide awesome support!</p>

---

## Post #4 by @ljod (2019-10-01 18:35 UTC)

<p>Thanks!<br>
Let us know if you could import the DICOM despite the errors?</p>
<p>Also sensitivity varies dramatically from DTI to multi fiber UKF. It’s not possible to truly prove the absence of a tract using tractography. Certainly it can be compared to contralateral and statements about asymmetry can be made.</p>

---

## Post #5 by @JohnK (2019-10-01 18:44 UTC)

<p>Yes, we are using the tractography  as supporting evidence only. The controls under identical scan conditions are forthcoming. All of this is messy data as we retrospectively made an interesting discovery in these very unique subjects.</p>
<p>As for DCM conversion I am getting a little farther with MRIcron plugin, but for the most part will will likely skip using NilRead.</p>
<p>Thanks again.</p>

---

## Post #6 by @Chris_Rorden (2019-10-04 16:03 UTC)

<p><a class="mention" href="/u/ljod">@ljod</a> and <a class="mention" href="/u/ihnorton">@ihnorton</a> I also had problems running the Dcm2niixGUI module in Slicer 4.10.2 on Windows. I downloaded the 17mb DWI dataset from <a href="https://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage#Diffusion_Tensor_Imaging" rel="nofollow noopener">nitrc</a>. After selecting the folder with the module and selecting “Apply” I was told to check the log for errors. The log reported:</p>
<p><code>('running: ', [u'C:/Users/rorde/AppData/Roaming/NA-MIC/Extensions-28257/SlicerDcm2nii/lib/Slicer-4.10/qt-scripted-modules\\Resources\\bin\\dcm2niix', '-1', '-d', '0', '-f', 'tmpa0_jyf', '-o', 'C:/Users/rorde/AppData/Local/Temp/Slicer/__SlicerTemp__', '-e', 'y', '-z', 'y', 'C:/Users/rorde/Desktop/Prisma'])</code></p>
<p>From the command line I could successfully run the same command:</p>
<p><code>C:/Users/rorde/AppData/Roaming/NA-MIC/Extensions-28257/SlicerDcm2nii/lib/Slicer-4.10/qt-scripted-modules\\Resources\\bin\\dcm2niix -1 -d 0 -f tmpa0_jyf -o C:/Users/rorde/AppData/Local/Temp/Slicer/__SlicerTemp__ -e y -z y C:/Users/rorde/Desktop/Prisma</code></p>
<p>With the following output</p>
<pre><code>Chris Rorden's dcm2niiX version v1.0.20190927  MSC1900 (64-bit Windows)
Found 105 DICOM file(s)
Convert 21 DICOM as C:/Users/rorde/AppData/Local/Temp/Slicer/__SlicerTemp__\tmpa0_jyfo (72x72x36x21)
NRRD writer is experimental
Convert 21 DICOM as C:/Users/rorde/AppData/Local/Temp/Slicer/__SlicerTemp__\tmpa0_jyfp (72x72x36x21)
NRRD writer is experimental
Convert 21 DICOM as C:/Users/rorde/AppData/Local/Temp/Slicer/__SlicerTemp__\tmpa0_jyfq (72x72x36x21)
NRRD writer is experimental
Convert 21 DICOM as C:/Users/rorde/AppData/Local/Temp/Slicer/__SlicerTemp__\tmpa0_jyfr (72x72x36x21)
NRRD writer is experimental
Convert 21 DICOM as C:/Users/rorde/AppData/Local/Temp/Slicer/__SlicerTemp__\tmpa0_jyfs (72x72x36x21)
NRRD writer is experimental
Conversion required 1.059000 seconds.</code></pre>

---

## Post #7 by @lassoan (2019-10-04 16:45 UTC)

<p>Is it possible that dcm2niix returns non-zero exit status?</p>
<p>Does it work well in latest Slicer Preview release?</p>
<p>Is this image that you tested with? <a href="http://people.cas.sc.edu/rorden/SW/dcm2niix/dtitest_Siemens_SC.zip" rel="nofollow noopener">McCausland Center 3T Prisma (17mb)</a></p>
<p>Is there a problem only with this data set or with every data sets?</p>
<p>I’ve tested with <code>McCausland Center 3T Prisma (17mb)</code> data set and confirm that an error reported and no data was loaded. The issue is that dcm2niix created inconsistent header (data file refers to a subdirectory that does not exist; the .raw.gz file is in the same folder as the .nhdr):</p>
<pre><code class="lang-nohighlight">NRRD0005
# Complete NRRD file format specification at:
# http://teem.sourceforge.net/nrrd/format.html
# dcm2niix v1.0.20190927 NRRD export transforms by Tashrif Billah
type: int16
dimension: 4
space: right-anterior-superior
sizes: 72 72 36 21
thicknesses:  NaN  NaN 3 NaN
endian: little
encoding: gzip
data file: __SlicerTemp__\tmpminz0bd.raw.gz
space units: "mm" "mm" "mm"
space origin: (108,-84.4189,-56.132)
...
</code></pre>
<p>Slicer uses latest “development” branch version of dcm2niix. <a class="mention" href="/u/chris_rorden">@Chris_Rorden</a> it would be great if you could check if Slicer uses dcm2niix somehow incorrectly or a fix is needed in dcm2niix nrrd writer.</p>

---

## Post #8 by @Chris_Rorden (2019-10-08 16:20 UTC)

<p>The latest <a href="https://github.com/rordenlab/dcm2niix/commit/ec20e50a7efbcc98915e4d18c77f0c2a861d8628" rel="nofollow noopener">development</a> build of dcm2niix fixes this issue. It was specific with NRRD files saved with Gzipped images on Windows and using ‘/’ rather than ‘’ in the file path.</p>

---

## Post #9 by @ljod (2019-10-18 15:53 UTC)

<p>Thank you for all of your fantastic and helpful responses on the discourse, Chris!!! It looks like we need to update the tag in our build process.</p>
<p>This tag will need to be updated twice, once for the dcm2nii module in the nightly and also in the same module for the release version of Slicer. (Ideally the release version would point to some stable version of dcm2niix. In Slicer 4.10, we are now using one of the releases that had been previously recommended.) This tag is currently handled in the extension description files documented here <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Extensions/DescriptionFile" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Extensions/DescriptionFile</a>. The github for these is here</p>
<p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/ExtensionsIndex/blob/4.10/SlicerDcm2nii.s4ext" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/ExtensionsIndex/blob/4.10/SlicerDcm2nii.s4ext" target="_blank" rel="nofollow noopener">Slicer/ExtensionsIndex/blob/4.10/SlicerDcm2nii.s4ext</a></h4>
<pre><code class="lang-s4ext">#
# First token of each non-comment line is the keyword and the rest of the line
# (including spaces) is the value.
# - the value can be blank
#

# This is source code manager (i.e. svn)
scm git
scmurl https://github.com/SlicerDMRI/SlicerDcm2nii.git
scmrevision 1c45a54

# list dependencies
# - These should be names of other modules that have .s4ext files
# - The dependencies will be built first
depends NA

# Inner build directory (default is ".")
build_subdirectory inner-build

# homepage
</code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/ExtensionsIndex/blob/4.10/SlicerDcm2nii.s4ext" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
Currently the release 4.10 branch is using:<br>
scm git<br>
scmurl <a href="https://github.com/SlicerDMRI/SlicerDcm2nii.git" rel="nofollow noopener">https://github.com/SlicerDMRI/SlicerDcm2nii.git</a><br>
scmrevision 1c45a54</p>
<p>and also the master branch (nightly) is using<br>
scm git<br>
scmurl <a href="https://github.com/SlicerDMRI/SlicerDcm2nii.git" rel="nofollow noopener">https://github.com/SlicerDMRI/SlicerDcm2nii.git</a><br>
scmrevision master</p>
<p>Apologies for my slow responses. I am about to begin maternity leave for a few months. Isaiah has moved to an industry job now. Hopefully this information helps you or others test out what works best in my absence. Steve Pieper will be able to address some SlicerDMRI needs during my leave. <a class="mention" href="/u/pieper">@pieper</a></p>
<p>Thanks again for being a great part of this community, Chris!</p>

---

## Post #10 by @ljod (2019-10-18 15:55 UTC)

<p>Please disregard this last post–this is the revision for SlicerDMRI (not dcm2niix). That does seem to be pointing to development, though I thought I remembered pointing to a particular revision of dcm2niix. Apologies for pregnancy brain over here. Trying to wrap things up on my end quickly. Thanks again though.</p>

---
