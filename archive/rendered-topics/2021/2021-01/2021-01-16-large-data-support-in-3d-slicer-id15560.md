# Large data support in 3D Slicer

**Topic ID**: 15560
**Date**: 2021-01-16
**URL**: https://discourse.slicer.org/t/large-data-support-in-3d-slicer/15560

---

## Post #1 by @muratmaga (2021-01-16 19:59 UTC)

<p>While volume sizes of the medical imaging (CT/MR) datasets haven’t changed in much in almost a decade, research imaging methods such as tiled microscopy, synchrotron, and nanoCT is pushing larger and larger datasets, any where from 10s of gigavoxels to terabyte of voxels. Even with common desktop microCT scanner, biology labs routinely generate 10GB+ volumes. I only see this trend getting stronger with time.</p>
<p>As the leading open-source biomedical visualization suite, I would like to see better support for such datasets in 3D Slicer. Our typical advise to  downsample or crop to specific region is not always helpful, as one reason to create such large datasets in first place is to visualize/analyze entire specimen, not a specific region. Another reason is that structures of interests can only be a few voxel thick, but scattered across the entire volume (for inspiration see this <a href="https://twitter.com/MarySalcedo/status/1348982176923217923" rel="noopener nofollow ugc">tweet for 40GB stack of grasshopper wings scanned in Lawrence Livermore synchrotron</a>).</p>
<p>I would like to initiate a shopping list of features that will make Slicer more efficient working with such large dataset, and identify ways/funding to incorporate this into Slicer. One assumption I have that users will be using desktops dozens of cores, and powerful GPUs and large RAM, but not necessarily clusters or parallel infrastructures common at supercomputing centers.</p>
<p>My minimum list of features consists of:</p>
<ol>
<li>
<strong>Rapid I/O:</strong> parallel read/writes, efficient multi-threaded compression (as importing a 10GB stack with 2000-3000 slicer into Slicer right now takes in the order of minutes. Writing a compressed nrrd of this takes tens of minutes).</li>
<li>Automatically down sample data to volume render within GPU HW capability (currently an invalid texture dimension error is thrown, if a single texture dimension exceeds the capability of the HW, and don’t render anything).</li>
<li>Being able to display regional data in full resolution</li>
<li>Segmentation tools and other working as if this is a normal sized data (e.g., support for OOM execution of datasets).</li>
</ol>
<p>Feel free to contribute your asks and inputs to this thread.</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/thewtex">@thewtex</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>(there was a previous thread that I accidentally delete now is removed. So I started a new one).</p>

---

## Post #2 by @pieper (2021-01-29 19:44 UTC)

<p>Somewhat related to the topic of large data, I gave a presentation about 3D Slicer to the <a href="https://csbconsortium.org/">CSBC</a> imaging working group in response to their inquiries about using it for large microscopy datasets.</p>
<p>The slides are <a href="https://docs.google.com/presentation/d/1grPMGPHnPRr1NSi2Mij4Uu2Fk_72wNJZOIaM4b6WZZw/edit#slide=id.p1">here</a> and recording of the event can be found <a href="https://www.synapse.org/#!Synapse:syn24201938">here</a>.  You will need a Synapse account to download it. Anybody can sign up at <a href="http://www.synapse.org/">www.synapse.org</a></p>
<p>Also in this recording is a talk by Kristen Browne from NIAID talking about her work on <a href="https://portal.hubmapconsortium.org/ccf-eui">HuBMAP anatomy modes</a> from visible human data and other sources using a pipeline that includes Slicer and other modeling software.</p>

---

## Post #3 by @mvine (2023-05-25 18:42 UTC)

<p>Just wanted to cross reference a <a href="https://github.com/Slicer/Slicer/issues/6982" rel="noopener nofollow ugc">GitHub issue</a> I just created about the memory usage during segmentation of large volumes. I would love to see some features and optimizations implementing into Slicer to solve these crazy memory usages often 10x the size of the dataset.</p>

---
