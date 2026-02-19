---
topic_id: 25500
title: "Is It Possible To Run Cfd Simulation In Slicer"
date: 2022-09-30
url: https://discourse.slicer.org/t/25500
---

# Is it possible to run CFD simulation in Slicer?

**Topic ID**: 25500
**Date**: 2022-09-30
**URL**: https://discourse.slicer.org/t/is-it-possible-to-run-cfd-simulation-in-slicer/25500

---

## Post #1 by @jay1987 (2022-09-30 11:20 UTC)

<p>now i can use vmtk to build vascular mesh and extract centerline<br>
is it possible to run CFD simulation with the data vmtk generated and show simulation in the sequence module?</p>

---

## Post #2 by @pieper (2022-09-30 13:03 UTC)

<p>I don’t think anyone has implemented CFD in Slicer, but it’s definitely possible to do with some programming.  Probably you can find an existing python or C++ package that will fit in nicely.</p>

---

## Post #3 by @jay1987 (2022-09-30 13:25 UTC)

<p>thank you pieper.<br>
i think i need to find if there has a third party program to invoke using  slicer multi process extension.</p>

---

## Post #4 by @pll_llq (2022-10-01 21:52 UTC)

<p>Do you want to <strong>run</strong> the simulation inside Slicer or do you want to have the ability to start/monitor/control the simulation from the Slicer UI?</p>

---

## Post #5 by @jay1987 (2022-10-05 01:27 UTC)

<p>thank you Theodore<br>
I want to run the simulation inside Slicer,to have the ability to start/monitor/control the simulation from the Slicer UI is awesome,too.Do you have a good solution to do this?</p>

---

## Post #6 by @pll_llq (2022-10-14 07:19 UTC)

<p>We used OpenFOAM for CFD<br>
We didn’t integrate it into slicer as the most convenient way was to use the docker containers that are provided by OF developers. For the work you mention I would probably only use slicer to have a convenient UI to set up the simulation and visualize the results (both logs and models), but would not actually run the simulation inside slicer.<br>
I can invite a CFD engineer to this forum if you’d like to ask more about doing simulations with OF</p>

---

## Post #7 by @jay1987 (2022-10-14 12:18 UTC)

<p>thank you very much Aptekarev!!<br>
is it possible to run simulations in sub process listened by Slicer Main Process,when simulation completes,show result with slicer ui?</p>

---

## Post #8 by @pll_llq (2022-10-15 13:05 UTC)

<p>Technically that would be possible, but that would involve an amount of engineering efforts to both make OF available on the system natively and to make it available inside slicer that IMO makes the returns on the time invested pretty low.<br>
Unless you have a particular reason to build an extension that would do that I would advice to “cut the corners” and take a more easy path</p>

---

## Post #9 by @pll_llq (2022-10-15 13:09 UTC)

<p>You might want to have a look at the PyFoam python package. It has some Qt based GUIs and might be the easiest way, although I haven’t used it myself and don’t know it’s capabilities<br>
<a href="https://openfoamwiki.net/index.php/Contrib/PyFoam" class="onebox" target="_blank" rel="noopener nofollow ugc">https://openfoamwiki.net/index.php/Contrib/PyFoam</a></p>

---

## Post #10 by @lassoan (2022-10-16 05:44 UTC)

<p>Typically, Slicer is used for segmentation and surface mesh generation. Sometimes for volumetric mesh generation (using SegmentMesher extension).</p>
<p>However, setting up materials, boundary conditions, loads, and simulation parameters is usually done in the CFD simulation preparation tools. It would be a lot of effort to redevelop (and maintain) a general-purpose GUI for setting up CFD simulation in Slicer and only engineers experienced in CFD simulation could use it. Therefore, I agree with <a class="mention" href="/u/pll_llq">@pll_llq</a> that it is quite unlikely anyone would implement this.</p>
<p>I would recommend using the CFD simulation tool’s GUI to set up the simulation for a few dozens of cases. After you set up all these cases manually, run the simulation, verify the results, and everything works well, you may be ready to make the simulation available to end users. You would do that by generating all the inputs for the simulation automatically. You would not need to develop or maintain a complex GUI, because the user would only need to provide the segmentation as input, and maybe a few basic parameters. You can use VTK and VMTK filters for this automation. If you need help with any specific steps then let us know, we should be able to give some tips - but only start thinking on automation after you processed many cases manually.</p>

---

## Post #11 by @jay1987 (2022-10-17 03:16 UTC)

<p>thank you for reply so detail <a class="mention" href="/u/lassoan">@lassoan</a><br>
I have a doctor friend who wants to simulate the hemodynamics of blood vessels in the brain to initially judge where to insert the optical fiber. Now I can segment the blood vessels of the brain through vmtk, but now I don’t know how to simulate<br>
in my poor knowledge ,i want to use some CFD simulation tool’s in sub process,and use a button of slicer  to invoke the sub process and set paras,listen for the process to get output,but i don’t if there exists any CFD simulation tool’s to Invode;</p>

---
