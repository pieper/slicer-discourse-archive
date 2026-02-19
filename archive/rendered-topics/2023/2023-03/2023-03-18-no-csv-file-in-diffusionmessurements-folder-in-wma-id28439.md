---
topic_id: 28439
title: "No Csv File In Diffusionmessurements Folder In Wma"
date: 2023-03-18
url: https://discourse.slicer.org/t/28439
---

# No CSV file in DiffusionMessurements folder in WMA

**Topic ID**: 28439
**Date**: 2023-03-18
**URL**: https://discourse.slicer.org/t/no-csv-file-in-diffusionmessurements-folder-in-wma/28439

---

## Post #1 by @Fumi (2023-03-18 05:22 UTC)

<p>Hi there, I am doing whitematteranalysis along with WMA tutorial: <a href="https://github.com/SlicerDMRI/whitematteranalysis/blob/master/doc/subject-specific-tractography-parcellation.md" rel="noopener nofollow ugc">https://github.com/SlicerDMRI/whitematteranalysis/blob/master/doc/subject-specific-tractography-parcellation.md</a>. In the last step of tutorial, " 8. Fiber tract diffusion measurements", I could not get any CSV file in the created new DiffusionMeasurements folder with error message of below:</p>
<blockquote>
<p>brain@l4n:~/Desktop/WMA_tutorial_data$ wm_diffusion_measurements.py ./FiberClustering/SeparatedClusters/tracts_commissural/ ./DiffusionMeasurements/commissural_clusters.csv /home/brain/Downloads/Slicer-5.2.2-linux-amd64/NA-MIC/Extensions-31382/SlicerDMRI/lib/Slicer-5.2/cli-modules/FiberTractMeasurements<br>
Importing whitematteranalysis package.<br>
&lt;wm_diffusion_measurements&gt;. Starting scalar measurement extraction.</p>
<h1>=====input directory======<br>
./FiberClustering/SeparatedClusters/tracts_commissural/<br>
=====output directory=====<br>
./DiffusionMeasurements<br>
=====3D Slicer====<br>
/home/brain/Downloads/Slicer-5.2.2-linux-amd64/NA-MIC/Extensions-31382/SlicerDMRI/lib/Slicer-5.2/cli-modules/FiberTractMeasurements</h1>
<p>/home/brain/Downloads/Slicer-5.2.2-linux-amd64/NA-MIC/Extensions-31382/SlicerDMRI/lib/Slicer-5.2/cli-modules/FiberTractMeasurements: error while loading shared libraries: libSlicerBaseLogic.so: cannot open shared object file: No such file or directory<br>
&lt;wm_diffusion_measurements&gt; Measurements done at: ./DiffusionMeasurements/commissural_clusters.csv</p>
</blockquote>
<p>This is happened to both tutorial data and my own DTI data, and either input is SeparatedClusters or AnatomicalTracts. I think the folder structure for SlicerDMRI in my PC is correct.<br>
Anyone who has advice on this issue?</p>
<p>Thank you,<br>
Fumi</p>

---

## Post #2 by @zhangfanmark (2023-03-18 05:39 UTC)

<p>Hi,</p>
<p>Please try Slicer launcher to call the fiber measurement module:</p>
<p>wm_diffusion_measurements.py ./FiberClustering/SeparatedClusters/tracts_commissural/ ./DiffusionMeasurements/commissural_clusters.csv “/home/brain/Downloads/Slicer-5.2.2-linux-amd64/Slicer --launch FiberTractMeasurements”</p>
<p>Regards,<br>
Fan</p>

---

## Post #3 by @Fumi (2023-03-18 06:04 UTC)

<p>Hi Fan, thank you for a very quick reply. I tried your command, but it was error again:</p>
<p>wm_diffusion_measurements.py ./FiberClustering/SeparatedClusters/tracts_commissural/ ./DiffusionMeasurements/commissural_clusters.csv “/home/brain/Downloads/Slicer-5.2.2-linux-amd64/Slicer --launch FiberTractMeasurements”<br>
Importing whitematteranalysis package.<br>
usage: wm_diffusion_measurements.py [-h] [-v] inputDirectory outputCSV Slicer<br>
wm_diffusion_measurements.py: error: unrecognized arguments: --launch FiberTractMeasurements”</p>
<p>Do you know why this is happen?</p>
<p>Thanks a lot!</p>
<p>Fumi</p>

---

## Post #4 by @jhlegarreta (2023-06-29 14:43 UTC)

<p>Hi,<br>
experiencing the very same error using Slicer 5.2.2 on Ubuntu 22.04 and when calling the measurement module through the <code>wm_apply_ORG_atlas_to_subject.sh</code> WMA script:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerDMRI/whitematteranalysis/blob/master/bin/wm_apply_ORG_atlas_to_subject.sh">
  <header class="source">

      <a href="https://github.com/SlicerDMRI/whitematteranalysis/blob/master/bin/wm_apply_ORG_atlas_to_subject.sh" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerDMRI/whitematteranalysis/blob/master/bin/wm_apply_ORG_atlas_to_subject.sh" target="_blank" rel="noopener nofollow ugc">SlicerDMRI/whitematteranalysis/blob/master/bin/wm_apply_ORG_atlas_to_subject.sh</a></h4>


      <pre><code class="lang-sh">#!/bin/bash

function Usage {
    cat &lt;&lt;USAGE
Usage:
`basename $0` -i InputTractography -o OutputDirectory -a ORGAtlasFolder -s PathTo3DSlicer
Compulsory arguments:
     -i:  Input tractography data stored in VTK (.vtk or .vtp). Note: fiber streamlines need to be in the RAS coordinates.
     -o:  Output directory to save all fiber clustering outputs.
     -a:  Path to the ORG atlas (the anatomically curated atlas ORG-800FC-100HCP), within which there should be 
          two folders named: ORG-RegAtlas-100HCP and ORG-800FC-100HCP 
     -s:  Path to 3D Slicer, e.g., under MacOS, it is /Applications/Slicer.app/Contents/MacOS/Slicer
Optional arguments:
     -r:  whole brain tractography registration mode (default = 'rig')
            rig: rigid_affine_fast : this enables a rough tractography registraion. This mode in general 
                                   applicable to tractography data generated from different dMRI 
                                   acquisitions and different populations (such as babies)
            nonrig: affine + nonrigid (2 stages) : this enables nonrigid deformations of the fibers. This mode
                                              needs the input tractography to be similar to the atals tractography, 
                                              e.g. two-tensor UKF tractography + HCP dMRI acquisiton. 
</code></pre>



  This file has been truncated. <a href="https://github.com/SlicerDMRI/whitematteranalysis/blob/master/bin/wm_apply_ORG_atlas_to_subject.sh" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>as</p>
<pre><code class="lang-auto">wm_apply_ORG_atlas_to_subject.sh -i my_tractogram.vtk -o WMA -a /path/to/org_atlas/ORG-Atlases-1.2 -s /opt/Slicer-5.2.2-linux-amd64/Slicer -d 1 -m /opt/Slicer-5.2.2-linux-amd64/NA-MIC/Extensions-31382/SlicerDMRI/lib/Slicer-5.2/cli-modules/FiberTractMeasurements -c 2 -n 4
</code></pre>
<p>The library is there of course,</p>
<pre><code class="lang-auto">/opt/Slicer-5.2.2-linux-amd64/lib/Slicer-5.2/libSlicerBaseLogic.so
</code></pre>
<p>but the script/Slicer is unable to locate it.</p>
<p>Instead, if I try to call the Python module directly from the command line, Slicer is unable to load the tractography data:</p>
<pre><code class="lang-auto">wm_diffusion_measurements.py /path/to/AnatomicalTracts /path/to/clusters.csv /opt/Slicer-5.2.2-linux-amd64/Slicer
Importing whitematteranalysis package.
&lt;wm_diffusion_measurements&gt;. Starting scalar measurement extraction.

=====input directory======
 /path/to/AnatomicalTracts
=====output directory=====
 /path/to/
=====3D Slicer====
 /opt/Slicer-5.2.2-linux-amd64/Slicer
==========================
Switch to module:  "Welcome"
Ignore argument received via command-line (not a valid URL or existing local file):  "--inputtype"
Ignore argument received via command-line (not a valid URL or existing local file):  "Fibers_File_Folder"
Ignore argument received via command-line (not a valid URL or existing local file):  "--format"
Ignore argument received via command-line (not a valid URL or existing local file):  "Column_Hierarchy"
Ignore argument received via command-line (not a valid URL or existing local file):  "--separator"
Ignore argument received via command-line (not a valid URL or existing local file):  "Comma"
Ignore argument received via command-line (not a valid URL or existing local file):  "--inputdirectory"
Local filepath received via command-line:  " /path/to/AnatomicalTracts"
Ignore argument received via command-line (not a valid URL or existing local file):  "--outputfile"
Ignore argument received via command-line (not a valid URL or existing local file):  " /path/to/clusters.csv"
static void qSlicerIOManager::showLoadNodesResultDialog(bool, vtkMRMLMessageCollection*) Errors occurred while loading nodes: "Error: Loading /path/to//AnatomicalTracts -  load failed.\n"
Switch to module:  ""
Switch to module:  ""
&lt;wm_diffusion_measurements&gt; Measurements done at: /path/to/clusters.csv
</code></pre>
<p>Any suggestion to make this work one way or the other?</p>

---

## Post #5 by @Fumi (2023-07-06 01:56 UTC)

<p>Hi, this issue is very similar to my problem. I tried many things on this topic, using some version of slicer, even on Mac and Windows. I noticed even I tried TractographyMeasurement on GUI, I couldn’t get any CSV file in folder like you mentioned in another topic.</p>
<p>Bacause I was running of time, I gave up using Slicer for my tract study.<br>
Hope you can solve this issue!</p>

---

## Post #6 by @zhangfanmark (2023-07-06 04:28 UTC)

<p>Hi <a class="mention" href="/u/fumi">@Fumi</a> <a class="mention" href="/u/jhlegarreta">@jhlegarreta</a></p>
<p>I looked in the the issue that you were facing.</p>
<p>On MacOS (mine is Ventura 13.2.1), it is working properly for me as it is. Please see the below screenshot for my setting to run the wm_diffusion_measurements script using Slicer 5.2.2 stable release:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45d477da36fe3176a0cdca20725cf2a02f4e2a61.jpeg" data-download-href="/uploads/short-url/9XK9Hi1qKqNTNS1tnbtUIP1UrsZ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45d477da36fe3176a0cdca20725cf2a02f4e2a61_2_690x152.jpeg" alt="image" data-base62-sha1="9XK9Hi1qKqNTNS1tnbtUIP1UrsZ" width="690" height="152" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45d477da36fe3176a0cdca20725cf2a02f4e2a61_2_690x152.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45d477da36fe3176a0cdca20725cf2a02f4e2a61_2_1035x228.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45d477da36fe3176a0cdca20725cf2a02f4e2a61_2_1380x304.jpeg 2x" data-dominant-color="0F2F7A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×425 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>On Ubuntu (mine is 20.04.4 LTS), I also saw the issue about missing lib files when using  Slicer 5.2.2 when directly call the FiberTractMeasurements module in the CLI mode. In this case, we would need to use Slicer Launcher to call the module so the program can set all the required libs. Please see the following screenshot for how this is being set. Please be noted of the red underline part. One change to what we did before is that the full path of the FiberTractMeasurements module is needed rather than the name of the module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5784dfd34c024973f827b9037d91ef85110cabe.jpeg" data-download-href="/uploads/short-url/usrs4fvgrFaHp4tuB0YHyqI4CEm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5784dfd34c024973f827b9037d91ef85110cabe_2_517x138.jpeg" alt="image" data-base62-sha1="usrs4fvgrFaHp4tuB0YHyqI4CEm" width="517" height="138" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5784dfd34c024973f827b9037d91ef85110cabe_2_517x138.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5784dfd34c024973f827b9037d91ef85110cabe_2_775x207.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5784dfd34c024973f827b9037d91ef85110cabe_2_1034x276.jpeg 2x" data-dominant-color="EBEAEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1342×361 159 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hope this will fix the issue you have here. Please let us know if you have further questions.</p>
<p>Thank you!</p>
<p>Regards,<br>
Fan</p>

---

## Post #7 by @jhlegarreta (2023-07-06 14:34 UTC)

<aside class="quote no-group" data-username="zhangfanmark" data-post="6" data-topic="28439">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zhangfanmark/48/4451_2.png" class="avatar"> zhangfanmark:</div>
<blockquote>
<p>Hope this will fix the issue you have here. Please let us know if you have further questions.</p>
</blockquote>
</aside>
<p>That worked <a class="mention" href="/u/zhangfanmark">@zhangfanmark</a> ! Thanks.</p>
<p>I will propose a PR to cover the Linux case in the <a href="https://github.com/SlicerDMRI/whitematteranalysis/blob/6d93b6452b32ebedbee29674766abfe752dd1d04/doc/subject-specific-tractography-parcellation.md" rel="noopener nofollow ugc">related documentation</a> as the only difference is the contents of the argument related to the module.</p>

---

## Post #8 by @jhlegarreta (2023-07-06 14:40 UTC)

<blockquote>
<p>I noticed even I tried TractographyMeasurement on GUI, I couldn’t get any CSV file in folder like you mentioned in another topic.</p>
</blockquote>
<p>True, the above does not solve the file not being computed using the GUI. I will open an issue in the <a href="https://github.com/SlicerDMRI/SlicerDMRI" rel="noopener nofollow ugc">SlicerDMRI repository</a>.</p>

---

## Post #9 by @jhlegarreta (2023-07-06 16:18 UTC)

<aside class="quote no-group" data-username="jhlegarreta" data-post="8" data-topic="28439">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>True, the above does not solve the file not being computed using the GUI. I will open an issue in the <a href="https://github.com/SlicerDMRI/SlicerDMRI" rel="noopener nofollow ugc">SlicerDMRI repository</a>.</p>
</blockquote>
</aside>
<p>OK, I figured out how to obtain the bundle stats using the GUI when specifying a folder (using the <code>Fibers_File_Folder</code> mode):</p>
<p></p><div class="video-placeholder-container" data-video-src="/404" data-orig-src="upload://m6sPeEwEOCbnvBikGbosQ2gPtnN.mp4">
  </div><p></p>
<p>The stats are computed and written to the specified CSV file.</p>
<p>I could not make it work when trying to compute the stats using the <code>Fiber_Hierarchy</code> mode: a 0-sized file is written: <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/zhangfanmark">@zhangfanmark</a> Am I correct when assuming that if I load a number of bundles (or an MRML created out of them) the <code>Fibers_Hierarchy</code> mode should work as fine as when using the <code>Fibers_File_Folder</code> option? Is there something else we should do to actually “create a hierachy”? The<code>Fibers Hierarchy</code> mode has the options <code>Rename current ModelHierarchy</code> and <code>Delete current ModelHierarchy</code> but when clicking no actions seems to be taken.</p>

---

## Post #10 by @pieper (2023-07-06 19:09 UTC)

<p>I’m not sure - maybe <a class="mention" href="/u/zhangfanmark">@zhangfanmark</a> or <a class="mention" href="/u/ljod">@ljod</a> knows if the <code>Fibers_Hierarchy</code> option is still valid.  My guess is that the feature was added in an older Slicer version (there used to be a Model Hierarchy concept that has been replaced by the more general Subject Hierarchy in current Slicer versions).  Unless there’s a strong need and some resources to investigate updating this feature, the easiest option would be to just remove the XML and C++ code.</p>
<p>As a side note, this module is an example of an older style of Slicer module that tried to abstract the GUI in XML and it made certain features like this one kind of clunky.  In modern Slicer we’d try to create a more convenient interface using python scripting and then call the C++ code with all the arguments managed by the python code.</p>

---

## Post #11 by @zhangfanmark (2023-07-07 02:28 UTC)

<p>Hi <a class="mention" href="/u/jhlegarreta">@jhlegarreta</a></p>
<p>As Steve said the Fibers_Hierarchy is an old style of Slicer module. It is helpful when we created the atlas where multiple clusters form a tract. In this case, we can compute measure from not only tracts but also individual clusters. Currently, our use case is mostly Fibers_File_Folder, so you don’t need to worry about this. We want to keep this option so we can track back what we did before. To use this function, yes, you need to create a hierarchy or use an existing defined in a mrml file.</p>
<p>Regards,<br>
Fan</p>

---

## Post #12 by @jhlegarreta (2023-07-07 12:36 UTC)

<aside class="quote no-group" data-username="zhangfanmark" data-post="11" data-topic="28439">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zhangfanmark/48/4451_2.png" class="avatar"> zhangfanmark:</div>
<blockquote>
<p>As Steve said the Fibers_Hierarchy is an old style of Slicer module. It is helpful when we created the atlas where multiple clusters form a tract. In this case, we can compute measure from not only tracts but also individual clusters. Currently, our use case is mostly Fibers_File_Folder, so you don’t need to worry about this. We want to keep this option so we can track back what we did before.</p>
</blockquote>
</aside>
<p>Not sure I understand the difference: whenever I load a number of tractograms in a SW, I would tend to think that I can compute features out of these. If within the Slicer realm a hierarchy must be created in order to do this, does it make sense to create a default one (e.g. including all loaded data)? I understand that computing measurements for individual clusters or at different levels is relevant, but IMHO the same principle applies if I consider that my clusters are those files that I loaded into Slicer. I am happy to help fixing this.</p>
<aside class="quote no-group" data-username="zhangfanmark" data-post="11" data-topic="28439">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zhangfanmark/48/4451_2.png" class="avatar"> zhangfanmark:</div>
<blockquote>
<p>To use this function, yes, you need to create a hierarchy or use an existing defined in a mrml file.</p>
</blockquote>
</aside>
<p>Yesterday I tried loading a number of tractography data into Slicer, created what seemed to be a hierarchy by creating a subject, then saved the scene as an MRML and the CSV written had still no contents. So there is something else that must be done.</p>

---

## Post #13 by @pieper (2023-07-07 14:40 UTC)

<p>I don’t believe there is a way to create the deprecated Model Hierarchy via the GUI anymore.</p>
<p>There’s some discussion here:</p>
<aside class="quote" data-post="1" data-topic="11707">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/vtkmrmlmodelhierarchynode-nodes-imported-as-subject-hierarchies/11707">vtkMRMLModelHierarchyNode nodes imported as subject hierarchies</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hello, 
I create a model hierarchy (based on vtkMRMLModelHierarchyNode objects) and save the mrml scene. When I open that scene, the model hierarchy has been turned into a subject hierarchy. Is that the expected behaviour? 
Thanks you in advance.
  </blockquote>
</aside>

<aside class="quote" data-post="1" data-topic="11706">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rafaelpalomar/48/1436_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/passing-hierarchies-to-clis/11706">Passing hierarchies to CLIs</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hello. 
I’m trying to develop a CLI module which takes a set of models as input and gives a set of models as output. It seems to be possible to use vtkMRMLModelHierarchy nodes for this, but is it possible to use vtkMRMLSubjectHierarchy nodes instead? 
Thanks in advance.
  </blockquote>
</aside>

<aside class="quote" data-post="1" data-topic="11700">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sam_horvath/48/3092_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/2020-05-26-hangout/11700">2020.05.26 Hangout</a> <a class="badge-category__wrapper " href="/c/community/hangout/20"><span data-category-id="20" data-parent-category-id="12" data-drop-close="true" class="badge-category --has-parent" title="This category is used to announce hangouts and organize associated notes."><span class="badge-category__name">Weekly meetings</span></span></a>
  </div>
  <blockquote>
    Tomorrow, we will be having our weekly hangout at 10:00 AM EST until 11 AM EST. 
Anyone is welcome to join to ask questions at <a href="https://bit.ly/slicer-googlemeet-hosted-by-kitware" rel="nofollow noopener">https://bit.ly/slicer-googlemeet-hosted-by-kitware </a> 
Agenda: 

Slicer 5 progress check-in

Feel free to post to this thread to request/suggest a topic! 
Thanks 
Sam
  </blockquote>
</aside>

<p>I don’t recall that anyone worked on adding Subject Hierarchy support to the CLIs, probably because, as I mentioned, writing the CLI GUI in XML always resulted in clunky interfaces for anything other than the simplest workflows.  I don’t think it would be hard to write a better GUI for the tractography measurements module (at least that’s what I’d do if I wanted to work on this).</p>
<p><a class="mention" href="/u/jhlegarreta">@jhlegarreta</a> note that with the Data Module you can right-click on a folder and choose Export to file and save all contents to a temp folder and then run the tractography analysis on them.</p>

---

## Post #14 by @jhlegarreta (2023-07-18 15:02 UTC)

<aside class="quote no-group" data-username="pieper" data-post="13" data-topic="28439">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p><a class="mention" href="/u/jhlegarreta">@jhlegarreta</a> note that with the Data Module you can right-click on a folder and choose Export to file and save all contents to a temp folder and then run the tractography analysis on them.</p>
</blockquote>
</aside>
<p>Not sure I understand: if trying to launch the analysis on the loaded tractography data does not work, users should be warned about it or the feature should direct/force users to choose a directory. I still think that, as it is the case with other features, one would expect any processing/analysis to be applied to the data loaded into Slicer without needing to first export it to a folder.</p>

---

## Post #15 by @pieper (2023-07-18 20:53 UTC)

<p>Yes, I agree - I was just suggesting a workraound.</p>

---
