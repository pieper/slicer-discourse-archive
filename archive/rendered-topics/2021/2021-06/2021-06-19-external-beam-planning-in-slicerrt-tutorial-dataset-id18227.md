# External Beam Planning in SlicerRT Tutorial Dataset

**Topic ID**: 18227
**Date**: 2021-06-19
**URL**: https://discourse.slicer.org/t/external-beam-planning-in-slicerrt-tutorial-dataset/18227

---

## Post #1 by @edwardwang1 (2021-06-19 19:13 UTC)

<p>Hi all,</p>
<p>For a bit of context, I am toying around with the idea of building an extension in Slicer that would use reinforcement learning to determine optimum dose volumes. The state would be the dose volume at a given point, and actions would be the addition/movement of beams. I would need a way to transition from a previous state to a new state given a specific action, and it seems to me that the math behind this is included in the External Beam Planning module in SlicerRT (which I know is based on EGSnrc).</p>
<p>This brings me to my question. I want to play with the module to get a feel for it, but I am having trouble following the tutorial found <a href="https://github.com/SlicerRt/SlicerRtDoc/blob/master/tutorials/SlicerRT_Tutorial_OrthovoltageDoseEngine.pptx" rel="noopener nofollow ugc">here</a>. I am running into an error (Failed to load node from file: C:/EGSnrc/egs_home/dosxyznrc\20210619_120333_dosxyznrc.3ddos) which I suspect is related to my EGSnrc installation (I am running Windows 10, Slicer 4.11 installed from the executable). I am following the tutorial on my own dataset as I was unable to find where to download the data used in the tutorial.</p>
<p>Could someone point me to where I can find the sample dataset? I suspect it won’t help the error, but it might help me isolate causes.</p>
<p>Thank you,<br>
Ed</p>

---

## Post #2 by @cpinter (2021-06-21 09:30 UTC)

<p>Hi Ed,</p>
<p>Sounds like a cool project!</p>
<p>I couldn’t say that External Beam Planning (EBP) is based on EGSnrc. It is a generic framework for forward EBRT planning, and one of its plugins uses EGSnrc. So in order to use EBP, you do not need EGSnrc. What is the dose calculation engine that you are planning to use to get from beam configuration to dose volume at each given state?</p>

---

## Post #3 by @edwardwang1 (2021-06-21 15:52 UTC)

<p>Hi Csaba,</p>
<p>Thanks for the reply! I see what you mean about EBP not being based on EGSnrc. If I’m understanding correctly, EBP is a framework that can make use of arbitrary dose engines (of which EGSnrc is one?). I’m still in the very early stages of my research, so I’m looking into EGSnrc, as well as a Matlab based dose engine called <a href="https://github.com/e0404/matRad/wiki/about-matRad" rel="noopener nofollow ugc">matRad</a>.</p>
<p>Could you point me to some documentation about how to integrate dose engines with EBP? There are some <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/ExternalBeamPlanning" rel="noopener nofollow ugc">links</a> at the bottom of the extension website but they appear to be broken.</p>
<p>Thank you,<br>
Ed</p>

---

## Post #4 by @cpinter (2021-06-21 16:13 UTC)

<p>I fixed the links on the wiki (thanks for letting me know). Please take a look at those and then we can continue from there. These files basically show how your dose engine can access the inputs in C++ or Python, and then provide the output. What happens between the two is completely up to the dose engine, as shown by these “mock” examples.</p>
<p>The EGSnrc approach is tried as a proof of concept but we cannot consider it stable, but at least you have an example of that. The matRad integration has been on the table for several years now, but we did not have the chance to get into it (the matRad developers were not interested in Slicer integration and we did not have the resources alone) while there was funding for SlicerRT infrastructure development, which we do not have any more. So although I think using matRad from Slicer would be great, it is something the support of which needs to be added (i.e. send the inputs via SlicerMatlabBridge to matRad in a way it can use it, and then receive and interpret the output).</p>

---

## Post #5 by @edwardwang1 (2021-06-21 18:44 UTC)

<p>Thank you for the detailed response. I think what I need initially is a dose engine to perform the learning experiments, and I can do that outside of Slicer. If I am successful, then I would like to integrate it into Slicer, and I will be sure to reach out then.</p>
<p>Thanks!</p>

---
