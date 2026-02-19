---
topic_id: 10847
title: "Gel Dosimetry Analysis"
date: 2020-03-26
url: https://discourse.slicer.org/t/10847
---

# Gel dosimetry analysis

**Topic ID**: 10847
**Date**: 2020-03-26
**URL**: https://discourse.slicer.org/t/gel-dosimetry-analysis/10847

---

## Post #1 by @Fritta (2020-03-26 13:20 UTC)

<p>Hi,<br>
I’m trying to analyze my 3D gel dosimetry image ( MRI image) by using the 3D gel dosimetry analysis tool. I want to obtain a gamma index map comparing the MRI image with the dose map obtained by my tps. I didn’t receive any calibration data about my gel and so I would like to perform only a relative comparison. I co-registered the MRI image and the dose map. Then I extracted a line profile along gel volume from both the co-registered images and I have created a graph to relate MRI intensity value with Rtdose volume intensity value. I used this data as calibration equation but it seems not to work well , because there is not a univocal correspondence between the two images intensity value.</p>
<p>Anyone here have faced with similar problem? Maybe I have to perform something more on my images such as histogram matching or something similar ?</p>
<p>Thank you for the attention</p>

---

## Post #2 by @cpinter (2020-03-26 15:24 UTC)

<p>I’m not too familiar with MRI-based gel dosimetry, but once you have a polynomial calibration function the rest of the comparison should work the same. I guess you’ll need to plot the intensity values of the two modalities in two functions, then fit the calibration polynomial like it is done <a href="https://github.com/SlicerRt/GelDosimetryAnalysis/blob/master/GelDosimetryAnalysis/GelDosimetryAnalysisLogic/GelDosimetryAnalysisLogic.py#L464-L477">here</a>.</p>

---

## Post #3 by @kmalexander (2020-03-26 15:40 UTC)

<p><a class="mention" href="/u/fritta">@Fritta</a> Can you paste a copy of your calibration data/plot?  Maybe the coincident data (TPS profile and MR profile) are just too noisy to create a reliable calibration function.  What kind of gel are you using?  Can you irradiate a separate gel with a well characterized beam to be used for calibration?  That would be the best way to do this to get absolute dose.</p>
<p>Regardless - dose profiles for a relative comparison should be sufficient.  A gamma comparison is much more meaningful when you have an absolute dose.  Otherwise you’re more or less just looking at spatial alignment (distance to agreement).</p>

---

## Post #4 by @Fritta (2020-03-26 17:28 UTC)

<p>I used a polymer gel. In order to lower the noise I smooth my MRI image first … I think that the problem is that I use as input a single spin echo MRI image instead of combining the 4 series acquired at differente TE with a turbo spin echo sequence in order to generate a R2 map (is there a simple wayin Slicer to combine the 4 MRI series in order to obtain my MRI R2 map ?). This is an example of the calibration curve obtained with profile extraction <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbc28b697b6d113e06468423bcb3c3d3d5365435.jpeg" data-download-href="/uploads/short-url/zVaEBvCFb7PPZWXVpMakDvQHCAt.jpeg?dl=1" title="mri" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbc28b697b6d113e06468423bcb3c3d3d5365435_2_689x499.jpeg" alt="mri" data-base62-sha1="zVaEBvCFb7PPZWXVpMakDvQHCAt" width="689" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbc28b697b6d113e06468423bcb3c3d3d5365435_2_689x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fbc28b697b6d113e06468423bcb3c3d3d5365435_2_1033x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbc28b697b6d113e06468423bcb3c3d3d5365435.jpeg 2x" data-dominant-color="F9FAFC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mri</span><span class="informations">1286×932 84.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @kmalexander (2020-03-26 17:50 UTC)

<p>Can you not get the R2 map from your scanner?</p>

---

## Post #6 by @Fritta (2020-03-26 18:12 UTC)

<p>No I just received 4 series images acquired with different TE</p>

---

## Post #7 by @Rollo_Moore (2020-03-30 11:51 UTC)

<p>Hi Fritta<br>
we performed some analysis on a nice product range of Gels supplied by RTSafe and I’ll loook for the abstraact /poster written.<br>
Essentially the graph of 1/T2 is required as a function of dose or calibration. I don;t think the graph you posted contains these data, but let me know if i misinterpreted<br>
best wishes<br>
Rollo<br>
RTPhysics/London.</p>

---

## Post #8 by @Fritta (2020-03-30 15:29 UTC)

<p>Thank you for your reply. I’m just analyzing the RTSafe gel supplied with a 3D printed head phantom.<br>
Thanks to a 3D Slicer tool named T2 mapping I converted the multi spin echo sequences in a T2 and 1/T2 map. Now in order to compare in relative terms the T2 map of the gel with my planned dose I need to input  the calibration dose parameters into the 3D Slicer tool for gel dosimetry. To obtain these parameters I used the tool line profile : I extracted line profile values from both T2 map and RTdose volume and graph them as shown in the previous graph. Maybe I failed in something because the relationship beetween the two values profiles seems to be not in a univocal relationship. Is it correct to perform the calibration in this way?</p>

---

## Post #9 by @Rollo_Moore (2020-03-30 16:28 UTC)

<p>Hi Francesca</p>
<p>we tried to do a separate calibration box of gel, and that was ‘noisy’.<br>
what i am not sure of in your data is if you have found the relaxation time or one of the t2 image values. this is what kmalexander refers to in post above i think.</p>
<p>it is made even harder a task if you cannot easily coregister the images very well, and voxel size makes a difference.<br>
I paste in some of the paragraphs on our poster to try and describe our process, but we concluded tha relative dosimetry worked ok, absolute was very much less certain because of the scanner characteristic and phantom temperature to name only 2 influences,<br>
regards<br>
Rollo</p>
<p>MRI data acquisition<br>
The gel phantom was scanned in the RT treatment position at 1.5T (Siemens, Aera, body array and spine coil) before and one day after irradiation (2D fast spin echo sequence with multiple echo times TR/TE = 2000ms/36,436,835,1230ms, voxel size= 1.4 x 1.4 x 2mm3, bandwidth=780Hz/px).<br>
Additional scans performed one week and a month post irradiation in order to investigate measurement stability.<br>
T2 relaxation time was calculated on a pixel-by-pixel basis (Siemens workstation).</p>
<p>Data analysis<br>
Pre-irradiation gel R2 =(1/T2) maps were scrutinized for imperfections and drifts in 3D and post-irradiation R2 measurements from different time points were compared.<br>
An independent dosimetric analysis was performed in-house: Registration was performed between the CT images and the T2 maps of the irradiated phantom (3D slicer) and the TPS calculated (relative) dose was compared with the measured R2 values (Matlab R2015b).<br>
The acquired raw images of the irradiated phantom were also separately processed by RTsafe for dosimetry.</p>

---

## Post #10 by @Fritta (2020-03-31 17:28 UTC)

<p>Thank you very much for the information. Now the module seems to work well and gamma analysis start to show good results … however I have to optimize the T2-map CT image co-registration … what kind of co-registration algorithm do you suggest ?</p>

---

## Post #11 by @lassoan (2020-04-04 20:44 UTC)

<p>Could you submit this question as a separate topic, with some more details, including a few screenshots.</p>

---
