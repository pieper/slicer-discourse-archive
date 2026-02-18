# Blood Flow Simulation from cardiac Cine-MRi

**Topic ID**: 20036
**Date**: 2021-10-06
**URL**: https://discourse.slicer.org/t/blood-flow-simulation-from-cardiac-cine-mri/20036

---

## Post #1 by @xiaolin (2021-10-06 12:47 UTC)

<p>Hi everyone, I’m a medical student and working on cardiac Cine-MRI. I’m gonna use the cardiac Cine-MRI to perform blood flow simulation and analysis, as well as the cardiac function. Does anyone know how to realize this in 3D Slicer?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2021-10-06 14:20 UTC)

<p>Slicer can help in this many ways.</p>
<p>What kind of cine-MRI data do you have? A single stationary cross-section imaged in time?</p>
<p>What would you like to achieve? Do you have a journal paper that describes the kind of simulation and analysis that you would like to implement?</p>

---

## Post #3 by @xiaolin (2021-10-06 14:53 UTC)

<p>Hi Prof. Andras Lasso,<br>
Thanks for your answer. I share a onedrive link of MRI.<a href="https://1drv.ms/u/s!AoRXgNKhUSkDam6khFAl3RQf6Vg?e=b9GoH1" rel="noopener nofollow ugc">https://1drv.ms/u/s!AoRXgNKhUSkDam6khFAl3RQf6Vg?e=b9GoH1</a><br>
As well as the paper: Blanken CPS, Farag ES, Boekholdt SM, Leiner T, Kluin J, Nederveen AJ, van Ooij P, Planken RN. Advanced cardiac MRI techniques for evaluation of left-sided valvular heart disease. J Magn Reson Imaging. 2018 Aug;48(2):318-329. doi: 10.1002/jmri.26204. PMID: 30134000; PMCID: PMC6667896.</p>
<p>And this is the previous issue when I loaded MRI to 3D Slicer: <a href="https://discourse.slicer.org/t/cardiac-mri-loading-erros/19926/3">https://discourse.slicer.org/t/cardiac-mri-loading-erros/19926/3</a></p>
<p>The MRI is from the post-interventional follow-up after transcatheter pulmonary valve replacement (sheep), and I want to perform the MRI analysis to get the myocardial change, ventricular functional change, and the pulmonary artery + right ventricular blood flow.</p>
<p>Could you please give me some detailed information (detailed steps will be much appreciated) to achieve this goal?</p>
<p>Thank you so much.</p>

---

## Post #4 by @lassoan (2021-10-07 05:02 UTC)

<p>You have 4D data sets that show 3-5 slice thick cross-section of the heart, and also a few flow images. Details are described in <a href="https://discourse.slicer.org/t/cardiac-mri-loading-erros/19926/7">this topic</a>.</p>
<p>For most of the analysis described in Blanken2018, you would need to interpret the flow images. Also, since these flow images only contain flow information in a single slice, if you want to analyze 3D flow then you may want to use the flow information in this slice to serve as input for a flow simulation.</p>
<p>What Slicer can do to help is to read and visualize images (for the flow images you probably need further processing), get a surface or volumetric mesh of the vessel wall that can be used as boundary condition during simulations, and visualize flow simulation results.</p>
<p>I’m not sure if anybody can help with how to do all these, but we can help with answering specific questions, mostly about how to achieve certain visualization or processing in Slicer.</p>

---

## Post #5 by @xiaolin (2021-10-08 08:07 UTC)

<p>Dear Prof. Andras Lasso,</p>
<p>Thanks for your reply. It helped a lot to load my MRI files. Could you please provide me with extensions in 3D Slicer to perform the flow simulation?</p>
<p>Thanks a lot and have a nice weekend in advance.</p>
<p>Xiaolin</p>

---

## Post #6 by @lassoan (2021-10-08 15:33 UTC)

<p>I don’t think any solution exists for simulating blood flow in the heart, with its extremely complex flow patterns, multiple valves, actively contracting walls, etc. You can aim for solving a small piece of this problem, for example, by just simulating a single valve, assuming rigid walls, specifying simplified loads, material models, properties, and boundary conditions (somewhat inspired by patient-specific measurements). Slicer can help in this with getting geometry of the valves and walls and probably making some flow measurements.</p>

---
