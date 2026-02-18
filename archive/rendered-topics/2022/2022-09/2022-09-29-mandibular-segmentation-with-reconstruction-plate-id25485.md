# Mandibular segmentation with reconstruction plate

**Topic ID**: 25485
**Date**: 2022-09-29
**URL**: https://discourse.slicer.org/t/mandibular-segmentation-with-reconstruction-plate/25485

---

## Post #1 by @pinklittlelamb (2022-09-29 16:10 UTC)

<p>hello</p>
<p>new 3d slicer user here. i have a ct scan of a patient who had facial trauma who is being planned for reconstructive surgery. the patient has a pre-existing reconstruction plate, and this data is included in the scan.</p>
<p>my goal is to segment the plate and bones independently, do a “mirroring” technique across the mid-sagittal plane, and plan virtual osteotomies with a CMF extension.</p>
<p>problem <span class="hashtag">#1:</span><br>
I am having difficulty applying different thresholds to my 2 unique segmentations. I would like a segmentation for the facial bones, as well as as a segmentation for the existing reconstruction plate.</p>
<p>problem <span class="hashtag">#2</span><br>
When using the dynamic modeler extension to create a mid-sagittal plane and cut, I do not have an “input node” to select, therefore I cannot apply and execute the cute. I am stuck here.</p>
<p>problem <span class="hashtag">#3</span><br>
what is the best tool to move segments in 3D space (rotate, translate, etc) - my goal is to draw up a virtual surgical plane which involves moving bones.</p>
<p>problem <span class="hashtag">#4</span><br>
what is the best solution to create a mandibular reconstruction plate and cutting guide with 3D slicer?</p>

---

## Post #2 by @smrolfe (2022-09-29 17:41 UTC)

<p>For 1 and 2, you will want to create one segmentation with two segments (bone and plate). Then export these segments as models that can be edited in the Dynamic Modeler module. Our tutorial <a href="https://github.com/SlicerMorph/Tutorials/blob/main/Segmentation/Segmentation.md" rel="noopener nofollow ugc">here</a> has detailed examples of these steps.</p>
<p>There are also many video tutorials on <a href="https://www.youtube.com/user/PerkLabResearch/videos" rel="noopener nofollow ugc">the Perk lab channel</a> that may be helpful, including <a href="https://www.youtube.com/watch?v=F6fNMQTxD-4" rel="noopener nofollow ugc">this one on the dynamic modeler</a>.</p>

---

## Post #3 by @pinklittlelamb (2022-09-29 18:30 UTC)

<p>hi Sara. thanks for your prompt response. would you be able to advise me on the following problem: when I select my threshold tool and decide the appropriate bracket range, this range then gets applied to all of my segmentations. I am trying to isolate the different components each with different threshold ranges. please let me know if you know how to help with this. I will review the linked tutorials, thank you.</p>

---

## Post #4 by @smrolfe (2022-09-29 18:47 UTC)

<p>When you click “apply” and move to the next segment, changing the range should not alter the previous segment. If you still see this after following the steps in the tutorial, it might be helpful if you can attach a screen shot.</p>

---

## Post #5 by @mau_igna_06 (2022-09-29 18:59 UTC)

<p>May be of interest:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner" target="_blank" rel="noopener nofollow ugc">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://repository-images.githubusercontent.com/316575529/fc6f0980-7e9e-11eb-9a53-5c1e41ae1245" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/SlicerIGT/SlicerBoneReconstructionPlanner" target="_blank" rel="noopener nofollow ugc">GitHub - SlicerIGT/SlicerBoneReconstructionPlanner: 3D Slicer module for...</a></h3>

  <p>3D Slicer module for planning mandible reconstruction surgery using fibula flap - GitHub - SlicerIGT/SlicerBoneReconstructionPlanner: 3D Slicer module for planning mandible reconstruction surgery u...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #6 by @pinklittlelamb (2022-09-29 19:02 UTC)

<p>hello mr. Dominguez. I have already downloaded bone reconstruction planner, however my knowledge is still too limited at this time in the program to fully apply it.</p>

---

## Post #7 by @pinklittlelamb (2022-09-29 19:03 UTC)

<p>hi Sara. this worked for me well, thank you for clarifying. At this time, I have the 2 segmentations complete. My next step is to “subtract” the plate from the plate+mandible segmentations, to therefore isolate the mandible. I am trying to use logical operations tool for this step but am having trouble setting it up. any advise for this?</p>

---

## Post #8 by @smrolfe (2022-09-29 20:16 UTC)

<p>If you click “Show details” in the effect description in Segment Editor you will see the information for setting up each method. Can you describe what is going wrong?</p>

---

## Post #9 by @pinklittlelamb (2022-09-30 17:54 UTC)

<p>Hi Sara. I am working on doing a mirroring technique (as described in the video you linked) for a mandible. I successfully mirrored the L side, and now I have L and R models which I can toggle independently. However, now my goal is combine the L and R models into one model to be exported as STL. What is the procedure for combining 2 models?</p>

---

## Post #10 by @smrolfe (2022-09-30 20:08 UTC)

<p>You can combine multiple models into a single output using the “Append” method in the Dynamic Modeler.</p>

---

## Post #11 by @mau_igna_06 (2022-09-30 20:23 UTC)

<p>Maybe you could try union (boolean operation) from the Sandbox extension</p>

---

## Post #12 by @pinklittlelamb (2022-10-01 14:03 UTC)

<p>Hello,</p>
<p>I just downloaded the sandbox extension “combine models”. I have 1 model with bone+plate, and another model with just plate. however, when I do the A-B computation, the resulted model is not correct. My goal is to subtract the patient’s existing plate from the CT scan so I can produce a new virtual surgical plan. Any help with the combine models function would be greatly appreciated.</p>

---

## Post #13 by @Ck1312 (2025-01-10 06:32 UTC)

<p>Does anyone have the answer to problem 3?</p>

---

## Post #14 by @muratmaga (2025-01-10 07:03 UTC)

<aside class="quote no-group" data-username="pinklittlelamb" data-post="1" data-topic="25485">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/91b2a8/48.png" class="avatar"> pinklittlelamb:</div>
<blockquote>
<p>what is the best tool to move segments in 3D space (rotate, translate, etc) - my goal is to draw up a virtual surgical plane which involves moving bones.</p>
</blockquote>
</aside>
<p>If you mean moving segments/models in space, then there are quite a few. Easiest is using the Interaction widget with the transforms module. But if you describe what you want to accomplish, we might provide more detailed suggestions.</p>

---

## Post #15 by @Ck1312 (2025-01-10 13:45 UTC)

<p>I have a fractured zygoma, I have segmented the dataset and I am looking to manipulate the zygoma and associated bony fragments into a desired post op position. Can you manipulate segmentations according to the 6 degrees of rotational freedom?</p>

---

## Post #16 by @muratmaga (2025-01-10 16:32 UTC)

<aside class="quote no-group" data-username="Ck1312" data-post="15" data-topic="25485">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/c/f08c70/48.png" class="avatar"> Ck1312:</div>
<blockquote>
<p>Can you manipulate segmentations according to the 6 degrees of rotational freedom?</p>
</blockquote>
</aside>
<p>Yes, and more if you like (e.g., scaling). Use the interactive transform widget.</p>

---

## Post #17 by @Ck1312 (2025-01-10 16:34 UTC)

<p>Okay, thanks. I have managed to work out exactly how to toggle the interactive transform widget on/off. Can you please advise how to export all fragments (in their new position) as one STL file?</p>

---

## Post #18 by @muratmaga (2025-01-10 17:52 UTC)

<p>To finalize the position, you can harden the transform (in the Data module right-click on the transform object associated with the model and then choose harden transform). Then you can save the models in their new positions/orientations.</p>
<p>However, stl format format does not allow you to save more then one model. You can export them individually. If retaining them together is important, you need to use OBJ format. I believe that’s the only 3D model format in Slicer that allows having multiple 3D models in a single file.</p>

---
