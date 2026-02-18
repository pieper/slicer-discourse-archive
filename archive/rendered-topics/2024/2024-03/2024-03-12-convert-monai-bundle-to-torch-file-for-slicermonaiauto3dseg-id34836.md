# Convert Monai bundle to torch file for SlicerMONAIAuto3DSeg

**Topic ID**: 34836
**Date**: 2024-03-12
**URL**: https://discourse.slicer.org/t/convert-monai-bundle-to-torch-file-for-slicermonaiauto3dseg/34836

---

## Post #1 by @slava (2024-03-12 01:25 UTC)

<p>Hi,</p>
<p>I am trying to use my network trained using Monai Auto3Dseg in the SlicerMONAIAuto3DSeg plugin. SlicerMONAIAuto3DSeg imports the torch file with a list including config information and the network weights. Monai outputs the project directory after the training, which is called the Monai bundle. Where can I find a script that converts the Monai bundle to a torch file to import in SlicerMONAIAuto3DSeg? Or do I have to write my converter?</p>
<p>Thanks,<br>
Slava</p>

---

## Post #2 by @lassoan (2024-03-12 04:29 UTC)

<p>I think there is current work towards making this easier to do. <a class="mention" href="/u/diazandr3s">@diazandr3s</a> may be able to provide more details.</p>

---

## Post #3 by @diazandr3s (2024-03-12 15:16 UTC)

<p>Hi <a class="mention" href="/u/slava">@slava</a>,</p>
<p>Great question!</p>
<p>If you have already trained Auto3DSeg and it is for a single modality/sequence, using the model in SlicerMONAIAuto3DSeg is straightforward - you don’t need to convert anything.</p>
<p>Can you please provide more details of the network architecture you used? Is it SegResNet? Which image modality and region does it segment?</p>
<p>Just two steps: 1/ take the model.pt and 2/ create the labels.csv file.</p>
<p>If yes, you need to take the <strong>model.pt</strong> from the <strong>segresnet_0</strong> folder and create the labels.csv file as I show here in these two videos:</p>
<ul>
<li>
<p>Taking the model.pt:<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8611039ee02d69e0205e66c7e114929cdff7ff1.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/6541e8b1c7bcf25c2cb9d91f6b2a08e1f0b3e8e0.jpeg">
  </div><p></p>
</li>
<li>
<p>Add the labels.csv file to the custom model:<br>
</p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e66fc88364326f143b3c8f1509bf27137e1964f7.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/143d3837155ea85025bd5fb49e5386965d206625.jpeg">
  </div><p></p>
</li>
</ul>
<p>To create the labels.csv file, you may find this list useful: <a href="https://github.com/lassoan/SlicerTotalSegmentator/blob/main/TotalSegmentator/Resources/totalsegmentator_snomed_mapping.csv" class="inline-onebox" rel="noopener nofollow ugc">SlicerTotalSegmentator/TotalSegmentator/Resources/totalsegmentator_snomed_mapping.csv at main · lassoan/SlicerTotalSegmentator · GitHub</a></p>
<ul>
<li>Modify the models.json in the SlicerMONAIAuto3DSeg and place the model in the cache folder:</li>
</ul>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b2e0e2cb7608871e8d7eef86fa6094fd99e3616.mp4" data-thumbnail-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/daa62991d0536d961beab784aeda815ddd8e0801.jpeg">
  </div><p></p>
<p>Hope this helps,</p>
<p>Please let us know.</p>

---

## Post #4 by @slava (2024-03-12 17:25 UTC)

<p>Hi Andres,</p>
<p>Thank you for jumping in. I trained DiNTS so far. The problem is that the .pt file Monai output does not have a config key inside, which triggers the error below. The config key the plugin tries to read has all the information about the data’s pre- and post-processing. I believe Monai changed the structure of the .pt file since they use bundles, and all pre- and post-processing information is in the configs folder.</p>
<p>Thanks,<br>
Slava</p>
<p>if ‘config’ not in checkpoint:<br>
raise ValueError(‘Config not found in checkpoint (not a auto3dseg/segresnet model):’+str(model_file))</p>

---

## Post #5 by @slava (2024-03-12 17:40 UTC)

<p>Hi Andres,</p>
<p>I want to confirm that Moani outputs strictly network weights into a torch file. The torch files provided with the plugin have the structure dict_keys([‘state_dict’, ‘config’, ‘epoch’, ‘best_metric’]), where ‘state_dict’ is the weights and ‘config’ has all information about roi_size, etc.</p>
<p>Thanks,<br>
Slava</p>

---

## Post #6 by @slava (2024-03-12 18:29 UTC)

<p>It is easy to change the plugin code to make it compatible with the Monai Bandle; you just need to parse YAML files in the config folder and read network weight from torch file. Please let me know if you plan to do it in the next few days. I can do it myself, but I don’t want to duplicate the effort if you plan to do it.</p>

---

## Post #7 by @diazandr3s (2024-03-13 21:12 UTC)

<p>Hi <a class="mention" href="/u/slava">@slava</a>,</p>
<p>Thanks for the update.</p>
<p>Would it be possible for you to train the Auto3DSeg using SegResNet instead of DiNTS?</p>
<p>It should be something like this:</p>
<p><code>python -m monai.apps.auto3dseg AutoRunner run --input ./configs/input_task.yaml --algos segresnet --work_dir ./output_folder</code></p>
<p>Then it’ll be straightforward to use on this module.</p>
<p>I know there are still some discrepancies between the Bundle created by MONAI Auto3DSeg and the one available in the model zoo. But you don’t need to create any bundle to use the <strong>SlicerMONAIAuto3DSeg</strong></p>
<p>A further analysis should be done before starting any PR. I’d strongly suggest you comment on your experience here: <a href="https://github.com/Project-MONAI/MONAILabel/discussions/1591" class="inline-onebox" rel="noopener nofollow ugc">Using one Bundle generated model in Auto3DSeg in MONAI Label · Project-MONAI/MONAILabel · Discussion #1591 · GitHub</a></p>
<p>or here: <a href="https://github.com/Project-MONAI/MONAI/issues/7467" class="inline-onebox" rel="noopener nofollow ugc">Unification of auto3dseg algorithm template format and MONAI bundle format · Issue #7467 · Project-MONAI/MONAI · GitHub</a></p>
<p>I hope this helps,</p>

---

## Post #8 by @nmod (2024-07-10 19:47 UTC)

<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a> This is very helpful! Thank you.</p>
<p>I’m new to Auto3DSeg and was wondering if it’s possible to get a .pt file of the ensemble itself. I could only find the .pt files for the individual models in the bundle generated.</p>

---

## Post #9 by @curtislisle (2024-07-10 21:32 UTC)

<p>Hi <a class="mention" href="/u/nmod">@nmod</a>,<br>
As far as I am aware, each Pytorch neural network is saved as its own checkpoint (.pt) file. Therefore, since the Auto3DSeg ensemble is not a single neural network, the ensemble results cannot be used directly in the Slicer extension without software coding changes. The SlicerMONAIAuto3DSeg extension code uses only the SegResNet model, so you could follow <a href="mailto:andres.diaz-pinto@kcl.ac.uk">@Diaz-Pinto, Andres</a> previous advice and use the .pt file corresponding to the trained SegResNet model, but not the entire ensemble. Or you could retrain with only the segresnet model and use that .pt as Andres also mentioned. I hope this helps.</p>
<p>Curt</p>

---

## Post #10 by @nmod (2024-07-10 21:44 UTC)

<p>Thank you so much! This is very helpful</p>

---
