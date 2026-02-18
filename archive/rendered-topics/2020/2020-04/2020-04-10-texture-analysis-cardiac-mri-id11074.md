# Texture analysis Cardiac MRI

**Topic ID**: 11074
**Date**: 2020-04-10
**URL**: https://discourse.slicer.org/t/texture-analysis-cardiac-mri/11074

---

## Post #1 by @sarvpriya1985 (2020-04-10 22:00 UTC)

<p>Hi all,<br>
I am looking to extract texture features using radiomics extension for cardiac mri images. For this I would segment LV myocardium (single slice) and run texture features on that.</p>
<p>I am looking to resample the image to isotropic resolution and do preprocessing- Intensity normalization, gray scale normalization and denoising. What parameters should I add in “setting column in this code”.</p>
<p>Also, what padding and bibwidth should I employ. Anything else should I change for this task.</p>
<p>I ran into paraametrics file on github and would like the help to modify the same.</p>
<p>This is a code I got from github.</p>
<p>Thanks,<br>
Sarv</p>
<pre><code class="lang-auto"># #############################  Extracted using PyRadiomics version: &lt;version&gt;  ######################################

imageType:
  Original: {}
  LoG:
    sigma: [2.0, 3.0, 4.0, 5.0]
  Wavelet: {}

featureClass:
  shape2D:
  firstorder:
  glcm:
    - 'Autocorrelation'
    - 'JointAverage'
    - 'ClusterProminence'
    - 'ClusterShade'
    - 'ClusterTendency'
    - 'Contrast'
    - 'Correlation'
    - 'DifferenceAverage'
    - 'DifferenceEntropy'
    - 'DifferenceVariance'
    - 'JointEnergy'
    - 'JointEntropy'
    - 'Imc1'
    - 'Imc2'
    - 'Idm'
    - 'Idmn'
    - 'Id'
    - 'Idn'
    - 'InverseVariance'
    - 'MaximumProbability'
    - 'SumEntropy'
    - 'SumSquares'
  glrlm:
  glszm:
  gldm:

setting:
  # Normalization:
  normalize: true
  normalizeScale: 100
  
  # Resampling:
  # first dimensions always correspond to in-plane resolution.
  # Z-plane resolution should not be modified to avoid mask errors (&gt; than 1 slice after resampling)
  interpolator: 'sitkBSpline'
  resampledPixelSpacing: [2, 2, 0]
  padDistance: 10
  preCrop: true


  # 2D settings
  # force2Ddimension setting is relative to the acquisition plane.
  #For example, the axial plane (0) corresponds to the acquisition plane (axial, sagittal or coronal) of the MRI volume.
  # Therefore, in most cases this setting should not be modified.
  force2Ddimension: 0
  
  # Image discretization:
  binWidth: 5

  # first order specific settings:
  voxelArrayShift: 300

  # Misc:
  label: 1
</code></pre>

---

## Post #2 by @JoostJM (2020-04-16 14:24 UTC)

<p>This script is certainly a good place to start. It already has normalization of intensity values, with a more-or-less appropriate bin-width (I don’t know the distribution in your dataset, so I’m not sure).</p>
<p>You could add <code>force2D: True</code> under <code>setting:</code>, as you are working with single slicer (2D) images. In that case, it also makes sense to replace featureclass <code>shape</code> for <code>shape2D</code>, which has equivalent features for 2D input (e.g. surface area instead of volume, perimiter instead of surface area)</p>

---

## Post #3 by @sarvpriya1985 (2020-04-17 18:14 UTC)

<p>Hi,<br>
Thanks for getting back.<br>
Regarding distribution of dataset- Is it regarding MRI scanner specifics? All these scans were on 1.5 T Siemens (three different Siemens scanners). I am not exactly sure what bin width refers to.</p>
<p>Also,<br>
regarding normalization- What is the type of normalization used in this script (for cardiac MRI- I could not find any literature for type of normalization so thinking of going with MRI brain literature that says mean+/- 3sd normalization.<br>
Secondly, the resampling given is [2,2,0]. The dataset I have has slice thickness of 6-8 mm. What should be the optimum resampling in your opinion.</p>
<p>Regarding the script that I copied here- I could not see a downloadable link in GitHub. I found from Pyradiomics discussion.</p>
<p>Would again appreciate your input.</p>
<p>Thanks,<br>
Sarv</p>

---

## Post #4 by @JoostJM (2020-04-27 16:02 UTC)

<blockquote>
<p>Regarding distribution of dataset- Is it regarding MRI scanner specifics?</p>
</blockquote>
<p>Not realy, I just mean the range of gray-value intensities found inside the ROIs of the cases in your dataset (regardless of which scanner)</p>
<blockquote>
<p>I am not exactly sure what bin width refers to.</p>
</blockquote>
<p>For several reasons, texture features should not be calculated on the original gray values, there are too many different ones. Therefore we discretize them (group them) so we’re left with less distinct gray values. Bin width controls how many gray values are grouped together. I.e. a binwidth of 25 means that gray value 0 - 24 gets assigned to the first bin, 25-49 to the second, etc. (N.B. the actual edges of the bins are shifted using the minimum gray value in the ROI, so the lowest binned value is always 1).</p>
<blockquote>
<p>regarding normalization- What is the type of normalization used in this script (for cardiac MRI- I could not find any literature for type of normalization so thinking of going with MRI brain literature that says mean+/- 3sd normalization.</p>
</blockquote>
<p>This is what PyRadiomics does: It subtracts the mean and divides by the standard deviation. You can enhance this by resegmenting, removing the outliers (i.e. if normalization is true, and scale is one, you could set resegmentRange to [-3, 3] to remove outliers &gt; 3 sd from the mean)</p>
<blockquote>
<p>Secondly, the resampling given is [2,2,0]. The dataset I have has slice thickness of 6-8 mm. What should be the optimum resampling in your opinion.</p>
</blockquote>
<p>If you want 3D extraction, you need isotropic voxels, i.e resampling to [2, 2, 2] or [3, 3, 3]. However, if you enable force2D, you can keep resampling at [2, 2, 0] (i.e. don’t resample the slice thickness)</p>
<blockquote>
<p>Regarding the script that I copied here- I could not see a downloadable link in GitHub. I found from Pyradiomics discussion.</p>
</blockquote>
<p>There are several example settings files on the PyRadiomics github. They are located in /examples/exampleSettings.</p>

---

## Post #5 by @Bassam (2020-05-22 20:09 UTC)

<p>Hi,<br>
Kindly, regarding the fixed bin width, does it possible to extract features without intensity discretization ? In the parameter file, I omitted the bin width and I extract the features, and then when I set the bin width = 25, it gave me the exact same results, that’s mean the default setting for bin width is 25.</p>
<p>So, please is there any way to extract features without intensity discretization ? In other words, does bin width = 1, represent that case ? and thank you very much</p>

---

## Post #6 by @JoostJM (2020-05-23 13:59 UTC)

<p><a class="mention" href="/u/bassam">@Bassam</a>, More or less, it still shifts the value so, that the minimum gray value in the ROI starts at 1. What exactly is the reason you’d like to skip the discretization step? This is an integral part of radiomic feature extraction and should not be omitted.</p>

---

## Post #7 by @Bassam (2020-05-23 20:47 UTC)

<p><a class="mention" href="/u/joostjm">@JoostJM</a> Appreciate your kind reply. The reason behind that is for studying the impact of binning the intensity values in a complex organ structure (extract features from original gray values and as well as from discretized values). Thanks again</p>

---

## Post #8 by @Valentina_Nepi (2021-12-19 19:11 UTC)

<p>sorry for the intrusion but I need some suggests for my dataset situation cause I am confused…<br>
all my mri are generated from the same scanner. Also the database images have been provided with same image dimensions and spacing for all sequences and for a given lesion segmentation. In this condition (I suppose) a normalization is not required. Neverthless analyzing radiomics features extracted from some segments (obtained from the given segmentation applying “islands effect”) I’ve obtained for some segments several glszm or glcm negative or equal 1 or 0.<br>
Do you think that a normalization:true and a scale:1 could resolve?</p>
<p>thank you in advance for an answer</p>

---

## Post #9 by @JoostJM (2022-01-18 12:46 UTC)

<p>No, I don’t think the issue of your problem is in any form of normalization, but with the application of the islands effect. Be careful that your resulting segmentations are not too small, resulting in a range of gray values &lt;&lt; bin width. This then results in a “flat region” (segmentation containing only 1 gray value after discretization). This then results in the values you are seeing…</p>
<p>The best way to analyze what is happening is to take a look at the diagnostic features which are a part of the standard PyRadiomics output. It should give you some idea on what is fed into the PyRadiomics pipeline and what kind of data is being analyzed.</p>

---
