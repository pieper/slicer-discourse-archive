---
topic_id: 1754
title: "Slicerigt Pathexplorer"
date: 2018-01-01
url: https://discourse.slicer.org/t/1754
---

# SlicerIGT pathexplorer

**Topic ID**: 1754
**Date**: 2018-01-01
**URL**: https://discourse.slicer.org/t/slicerigt-pathexplorer/1754

---

## Post #1 by @shellyverde (2018-01-01 23:32 UTC)

<p>Hi，<br>
I am new to Slicer and SlicerIGT. Trying to use the SlicerIGT pathexplorer function. When pressing the ‘+’ in the Plan section, I couldn’t add a point. I think there is something missing. Could you please help?<br>
Thanks!<br>
-Shelly</p>

---

## Post #2 by @lassoan (2018-01-01 23:45 UTC)

<p>That is quite an old module and indeed it is not easy to use. SlicerIGT extension evolved a lot since this module has been added, so you may find other modules that can fulfill your needs and easier to use. Could you describe your clinical application (anatomy, procedure, imaging modality) and what you would like to achieve?</p>
<p>To answer your question about PathExplorer:</p>
<ul>
<li>Open “Advanced” section and click on each of the 3 listboxes and click on “Create new…”</li>
<li>Click on <code>+</code> icon in the top fiducial list in Planning section then click in the image to define entry point(s)</li>
<li>Click on <code>+</code> icon in the bottom fiducial list in Planning section then click in the image to define target point(s)</li>
<li>Select an entry and a target point in the two lists in Planning section then click on <code>+</code> icon in the Visualization section</li>
<li>Select a trajectory in Visualization section</li>
<li>Click on the red/yellow/green button on the left side of sliders to allow reslicing in that slice view</li>
</ul>

---

## Post #3 by @shellyverde (2018-01-02 03:15 UTC)

<p>It worked. Thanks a lot for the help and quick response!<br>
I need to create a trajectory for a pedicle screw planning on CT data. Do you have any recommendation for the other modules that I can use?<br>
Thanks,<br>
-Shelly</p>

---

## Post #4 by @lassoan (2018-01-02 03:35 UTC)

<p>There is a pedicle screw planning extension for Slicer:</p>
<div class="lazyYT" data-youtube-id="XN3Tp8jaYdQ" data-youtube-title="3D Slicer - Pedicle Screw Surgical Simulator" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>It is not listed in the extension manager but you have to download it from <a href="https://github.com/smclach/PedicleScrewSimulator/archive/master.zip">here</a> and unzip all files to a folder on your computer. Then start Slicer and in Application settings / Modules, add to “Additional module paths” the directory that contains <code>PedicleScrewSimulator.py</code>.</p>
<p>See also this discussion: <a href="https://discourse.slicer.org/t/how-to-install-pedicle-screws-simulator-extension/1073">How to install pedicle screws simulator extension?</a>.</p>

---

## Post #5 by @lassoan (2018-01-02 03:35 UTC)

<p><a class="mention" href="/u/smclachlin">@smclachlin</a>: It would be great if you could finalize the PedicleScrewSimulator extension and submit to the extension manager. Let me know if you need any help with it.</p>

---

## Post #6 by @shellyverde (2018-01-02 04:37 UTC)

<p>Great -:). Will do!<br>
Thanks,<br>
-Shelly</p>

---
