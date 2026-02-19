---
topic_id: 14246
title: "Dmri Extension Files Where Do They End Up"
date: 2020-10-26
url: https://discourse.slicer.org/t/14246
---

# dMRI Extension Files -- Where do they end up?

**Topic ID**: 14246
**Date**: 2020-10-26
**URL**: https://discourse.slicer.org/t/dmri-extension-files-where-do-they-end-up/14246

---

## Post #1 by @mgc26 (2020-10-26 01:19 UTC)

<p>I’ve been trying to complete the whitematteranalysis, but stuck on the last step as I cannot locate the SlicerDMRI extension files on my Ubuntu box.</p>
<p>The step I’m stuck on:</p>
<h1><a name="p-49117-h-8-fiber-tract-diffusion-measurements-1" class="anchor" href="#p-49117-h-8-fiber-tract-diffusion-measurements-1" aria-label="Heading link"></a>8. Fiber tract diffusion measurements</h1>
<blockquote>
<pre><code>wm_diffusion_measurements.py ./FiberClustering/SeparatedClusters/tracts_left_hemisphere/ ./DiffusionMeasurements/left_hemisphere_clusters.csv /Applications/Slicer4p10realease.app/Contents/Extensions-27501/SlicerDMRI/lib/Slicer-4.10/cli-modules/FiberTractMeasurements

wm_diffusion_measurements.py ./FiberClustering/SeparatedClusters/tracts_right_hemisphere/ ./DiffusionMeasurements/right_hemisphere_clusters.csv /Applications/Slicer4p10realease.app/Contents/Extensions-27501/SlicerDMRI/lib/Slicer-4.10/cli-modules/FiberTractMeasurements

wm_diffusion_measurements.py ./FiberClustering/SeparatedClusters/tracts_commissural/ ./DiffusionMeasurements/commissural_clusters.csv /Applications/Slicer4p10realease.app/Contents/Extensions-27501/SlicerDMRI/lib/Slicer-4.10/cli-modules/FiberTractMeasurements
</code></pre>
</blockquote>
<p>Anyone know where the I can find FiberTractMeasurements with the 3D Slicer linux installation?</p>

---

## Post #2 by @zhangfanmark (2020-10-26 17:28 UTC)

<p>Hi <a class="mention" href="/u/mgc26">@mgc26</a></p>
<p>Here you are using the cli module path under a Mac OS, which is for demonstration in the tutorial you followed.</p>
<p>For Linux, you will need to install both 3D slicer and SlicerDMRI extension. See here for SlicerDMRI installation instructions: <a href="http://dmri.slicer.org/download/" rel="noopener nofollow ugc">http://dmri.slicer.org/download/</a></p>
<p>Then, you should be find the module under your 3D Slicer folder, like this: Extensions-XXX/SlicerDMRI/lib/Slicer-4.XX/cli-modules/FiberTractMeasurements</p>
<p>Please let me know how it works for you.</p>
<p>PS: for any further issues related to WMA, you can directly create an issue in the WMA repository.</p>

---

## Post #3 by @mgc26 (2020-10-26 17:38 UTC)

<p>Thanks for getting back to me, Fan.<br>
I do have 3D Slicer installed as well as SlicerDMRI per the instructions. I was able to run the WMA whole tutorial up through the last step.<br>
The issue is that in the Linux 3D Slicer directory there is no extensions folder containing SlicerDMRI.<br>
In my 3D Slicer GUI, I am able to see that SlicerDMRI is installed and can use it. The installation appears to have worked just fine.<br>
However, when I try to do the WMA tutorial at the CLI there SlicerDMRI extension files don’t exist in the 3D Slicer application directory.</p>
<p>Hopefully that clarifies the issue I’ve run in to.</p>

---

## Post #4 by @zhangfanmark (2020-10-26 17:54 UTC)

<p>Have you tried to search within the Slicer folder to see if you can find FiberTractMeasurements? Unfortunately, I don’t have a linux machine to check the path.</p>
<p>Another way, if you run the FiberTractMeasurements using GUI, in the “log message” (right bottom red), you can see how the cli is being called. From there, you will see the path of the cli module.</p>
<p>Regards,<br>
Fan</p>

---

## Post #5 by @mgc26 (2020-11-02 20:16 UTC)

<p>Hi Fan,<br>
Thanks for your reply. I used your log message trick and it did indicate how the CLI is being called, but it appears to be in a hidden location:</p>
<blockquote>
<p>/home/**/.config/NA-MIC/Extensions-29402/SlicerDMRI/lib/Slicer-4.11/cli-modules/FiberTractMeasurements</p>
</blockquote>
<p>Unfortunately, the script to run the measurements does not work as the .config folder is ‘hidden’ in Ubuntu. Thus, it appears Slicer3D stores the extension cli-modules in a hidden config file.</p>
<p>As a workaround, I tried downloading the DMRI source code from Github and tried to source FiberTractMeasurements directly</p>
<blockquote>
<p>/home/**/SlicerDMRI-master/Modules/CLI/FiberTractMeasurements</p>
</blockquote>
<p>Now, I’m getting an error on permissions:</p>
<blockquote>
<p>sh: 1: /home/**/SlicerDMRI-master/Modules/CLI/FiberTractMeasurements: Permission denied</p>
</blockquote>
<p>I’ve tried to unlock the files using chmod +x * but to no avail.</p>
<p>Any suggestions beyond this?</p>

---

## Post #6 by @zhangfanmark (2020-11-03 18:58 UTC)

<p>For the FiberTractMeasurements, can you try to run “/home/**/.config/NA-MIC/Extensions-29402/SlicerDMRI/lib/Slicer-4.11/cli-modules/FiberTractMeasurements -h” from your terminal and see if it works?</p>
<p>Not sure why it does not work in the script. Perhaps also try adding parentheses to the module path “/home/**/.config/NA-MIC/Extensions-29402/SlicerDMRI/lib/Slicer-4.11/cli-modules/FiberTractMeasurements”</p>
<p>Directly from the source code should not work. You will need to compile in order to have the binary executable file.</p>
<p>Regards,<br>
Fan</p>

---

## Post #7 by @mgc26 (2020-11-04 02:00 UTC)

<p>Hi Fan – thanks for your continued support.</p>
<p>Unfortunately, it appears that the script still cannot find FiberTractMeasurements with adding “-h” or putting the command in parentheses as you suggested.</p>
<p>I was able to generate the measurements using the GUI, so the dMRI module works. Seems the issue here is that when 3D Slicer installs extensions into the hidden .config folder they are not accessible with the terminal call supplied in the WMA tutorial. The remainder of the tutorial executed perfectly…</p>

---
