# Syntax parameter file

**Topic ID**: 16907
**Date**: 2021-04-01
**URL**: https://discourse.slicer.org/t/syntax-parameter-file/16907

---

## Post #1 by @Marion (2021-04-01 13:10 UTC)

<p>Operating system: macOS High Sierra (10.13.6)<br>
Slicer version: 4.11.20200930<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi everyone,</p>
<p>I have a problem with the syntax of the parameter file for the Radiomics module. I attach the .yaml file that I have already created.</p>
<pre><code class="lang-auto"># It is written according to the YAML-convention (www.yaml.org) and is checked by the code for consistency.

imageType:
  Original: {} # unfiltered image

setting:
  binWidth: 2

#distances between the center voxel and the neighbor, for which angles should be generated.
  distance: [[3]]		

#z-score normalisation 
  normalize: True


# Featureclasses, from which features must be calculated. If a feature class is not mentioned, no features are calculated


featureClass:
  
  shape:
  firstorder: 
  glcm:  
  glrlm: 
  glszm:
  gldm:  
</code></pre>
<p>I have two questions, the first one is about standardization. I saw on the documentation that if I set “true” for normalization, we use z-score normalization. I would like to know how to set the +/- 3 sigma normalization, i.e. what sentence to write to access this normalization ?</p>
<p>My second question is about the distance between the neighbors for the calculation of the texture parameters. The syntax indicated in my code does not work, I tried several possibilities but they do not work either. What should I write ?</p>
<p>Thank you so much for your answers,</p>
<p>Marion</p>

---

## Post #3 by @Marion (2021-04-02 07:52 UTC)

<p>edit: miss a letter, “distances” seems correct with this syntax : distances: [3]</p>
<p>But I have a new question : I don’t have a value for each direction or distance ? It’s an average ?</p>

---

## Post #4 by @JoostJM (2021-04-12 07:53 UTC)

<p>Distances, default [1] is the distance from the center voxel, according to infinity norm. This is used to automatically generate the offsets (aka angles). So there are no values for different directions. The reason the value is a list is that each unique distance can be mentioned. E.g. if you want to include all offsets up to distance 3, specify <code>distances = [1, 2, 3]</code>. If you want offsets for distance up to 3, but exlude the innermost ring (distance 1), specify <code>distances = [2, 3]</code>.</p>
<p>Be aware that this does not affect GLRLM and GLSZM, which are hardcoded to use distance 1 when seeking out neighbors, as it is a region growing algorithm.</p>

---

## Post #5 by @Marion (2021-04-12 10:33 UTC)

<p>Thank you so much for your answer!</p>
<p>How can I implement the +/- 3 sigma normalization, which syntax should I use ?</p>
<p>And I saw that the normalization was made on the image, is it possible to do it on the ROI ?</p>

---

## Post #6 by @JoostJM (2021-04-12 13:09 UTC)

<p>with +/- 3 sigma normalization, do you mean that you want the range in the image to be about [-3, 3]? In that case, just set <code>normalize=True</code>, this subtracts the mean and divides by standard deviation. The result is that the image has mean = 0 and standard deviation = 1. You can the expect most values to fall within the range [-3, 3].</p>
<p>This is enforced on the image, as applying it just to the ROI will make the normalization dependent on the ROI, and result in loss of signal (e.g. the firstorder mean feature will then allway be 0). The goal of normalization is to remove systematic differences due to differences in acquisition, this is best achieved when using the entire image. It stems from the assumption that the same sequence from different patients will have more or less the same range in intensity values, and normalization ensures this is so. This assumption does not and should not hold true for the individual ROIs (otherwise there would be no signal to build a model on).</p>
<p>Is there a specific reason you want to normalize on just the ROI instead of the entire image?</p>

---

## Post #7 by @Marion (2021-04-12 14:01 UTC)

<p>When I set normalize=True, it’s the z-score normalization. I want to implement the +/- 3σ normalization which is an other method used very often in publications. With this normalization, the values go from µ-3σ to µ+3σ. So is it possible to do so ?</p>
<p>I used MRI images and ROI which are small (subcortical regions). The normalization on the ROI allows to get rid of the inhomogeneities of the B0 field. . Is it possible to do it ?</p>

---

## Post #8 by @JoostJM (2022-01-11 12:06 UTC)

<p>You can exclude outliers by setting the resegmentation range to [-3, 3]. This excludes voxels that differ more than 3 sigma from the mean.</p>
<p>Normalization based on the ROI is not possible, as this would be based on the assumption that the gray value distribution inside the ROI should be comparable. But if this is true, the you’d assume that all lesions have the same distribution, which is the opposite of the assumption that there exist phenotypic differences between lesions (on which the radiomics hypothesis is based).</p>

---
