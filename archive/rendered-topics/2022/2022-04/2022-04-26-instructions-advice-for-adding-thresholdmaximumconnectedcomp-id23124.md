---
topic_id: 23124
title: "Instructions Advice For Adding Thresholdmaximumconnectedcomp"
date: 2022-04-26
url: https://discourse.slicer.org/t/23124
---

# Instructions/Advice for adding ThresholdMaximumConnectedComponentsImageFilter or AutomaticThresholdImageFilter as a segment editor effect

**Topic ID**: 23124
**Date**: 2022-04-26
**URL**: https://discourse.slicer.org/t/instructions-advice-for-adding-thresholdmaximumconnectedcomponentsimagefilter-or-automaticthresholdimagefilter-as-a-segment-editor-effect/23124

---

## Post #1 by @mau_igna_06 (2022-04-26 10:53 UTC)

<p>I’m interested in using this filter since it allows to get the threshold value that maximizes the number of islands in an image. I want to use this value as input for another filter. So I was thinking in adding this filter to Slicer as an effect for those who are interested in using it.</p>
<p>Here is the related publication: <a href="https://insight-journal.org/browse/publication/40" rel="noopener nofollow ugc">https://insight-journal.org/browse/publication/40</a><br>
Although <a href="https://itk.org/Doxygen/html/classitk_1_1ThresholdMaximumConnectedComponentsImageFilter.html" rel="noopener nofollow ugc">it is already implemented on itk</a> I don’t know if it lacks some flexibility since the source code of the publication says:</p>
<blockquote>
<p>This algorithm optimizes hollow myofibers (ie white doughnuts). If you want to automatically threshold a picture of white islands (ie dapi nuclei, a solid cell) should invert the threshold inside (m_InsideValue) and outside (m_OutsideVaalue) values in the cons</p>
</blockquote>
<p>I would want to have an option to switch between both modes: solid-islands and donut-islands.<br>
Also I want the optimal threshold value to be accesible from the effect and performing the segmentation should be optional. Or maybe the user should instantiate the filter and get those values through code</p>
<p>For these reasons I would like to add the filter to vktITK folder. I’m looking for instructions because I’m new to C++. I added the cxx to the source files on cmakefile and also added the itkModules it uses to the list that was on the cmakefile, but probably itkModuleNames have changed after more than 15 years. I don’t expect it to work. I’m building right now.</p>
<p>Some guidance regarding this endeavour would be appreciated. Thank you</p>

---

## Post #2 by @lassoan (2022-04-26 12:23 UTC)

<p>In extensions, we usually create a CLI module to make available ITK filters in Slicer. CLI modules have a basic GUI, so it is already accessible for end users, but often a Python scripted module is added that provides a more convenient user interface.</p>
<p>That said, I’m not sure if it is worth spending much time with such ad hoc methods. The main idea of tuning processing parameters to obtain maximum number of islands is questionable, as noise, image texture, artifacts, and irrelevant image parts may influence the results. You can reduce the effect of these by adding pre and post processing steps, but then you end up with a slow, complex, hard-to-control method and you need to optimize it by running it on many data sets. Until about 5 years ago it was pretty standard to do this manually: you could write a masters or PhD thesis out of it, regardless of how well the method worked in practice. Today, you would only need to do the testing data collection and you would let the GPU find a optimal processing method and parameters via deep learning.</p>
<p>Important additional advantages of using deep learning (regardless of performance):</p>
<ul>
<li>you don’t have to defend your decision of investing time into testing and optimizing a classic method when “AI” is the default today</li>
<li>you obtain more experience in a marketable skill (using “AI” for medical image computing)</li>
<li>achieving the same results using “AI” is often worth more than solving it with a classic method, because investors, companies, funding agencies believe that AI is the future and want to invest into that, while they are anxious if their money is spent on developing classic methods; this is not rational and in a few years this may change but I stillbregularly experience that this bias - hype - towards AI.</li>
</ul>

---
