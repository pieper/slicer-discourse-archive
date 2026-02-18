# Getting started with MONAIlabel

**Topic ID**: 38559
**Date**: 2024-09-26
**URL**: https://discourse.slicer.org/t/getting-started-with-monailabel/38559

---

## Post #1 by @gendex (2024-09-26 13:01 UTC)

<p>Dear Slicer Community,</p>
<p>I have been working with Slicer for a while now and have recently started using the MONAI module in Slicer. However, I’m having some issues getting the output that I’m looking for.</p>
<p>I’ve managed to run the segmentation model to train an initial dataset that I have previously segmented using TotalSegmentator. However, when testing the model there is a large offset in the output as seen below.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a608243f9f1d6a1021755e7db2fa9536b0f01e5.png" data-download-href="/uploads/short-url/62SP1FIafwoPfDEsTmFvlhhXSWF.png?dl=1" title="output_offset" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a608243f9f1d6a1021755e7db2fa9536b0f01e5_2_690x221.png" alt="output_offset" data-base62-sha1="62SP1FIafwoPfDEsTmFvlhhXSWF" width="690" height="221" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a608243f9f1d6a1021755e7db2fa9536b0f01e5_2_690x221.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a608243f9f1d6a1021755e7db2fa9536b0f01e5_2_1035x331.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a608243f9f1d6a1021755e7db2fa9536b0f01e5_2_1380x442.png 2x" data-dominant-color="2E2A25"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">output_offset</span><span class="informations">1474×474 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried to recreate this by training the segmentation model on a subset of the publicly available TotalSegmentator dataset and encountered different errors. It seems that MONAI is struggling with applying a transform (see below):</p>
<p><em>[2024-09-24 12:20:25,830] [17576] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:876) - Engine run resuming from iteration 0, epoch 0 until 1 epochs</em><br>
<em>[2024-09-24 12:32:03,933] [17576] [MainThread] [ERROR] (ignite.engine.engine.SupervisedEvaluator:1086) - Current run is terminating due to exception: applying transform &lt;monai.transforms.compose.Compose object at 0x000001D6A6078CD0&gt;</em><br>
<em>2024-09-24 12:32:03,933 - ERROR - Exception: applying transform &lt;monai.transforms.compose.Compose object at 0x000001D6A6078CD0&gt;</em></p>
<p><em>…</em></p>
<p><em>torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 3.16 GiB. GPU</em></p>
<p><em>…</em></p>
<p><em>RuntimeError: applying transform &lt;monai.transforms.post.dictionary.AsDiscreted object at 0x000001D6A60781C0&gt;</em></p>
<p>What kind of transform is MONAI trying to perform?<br>
Could it be a driver issue that CUDA is running out of memory at 3.16GiB? The  used GPU is an Nvidia RTX 4090 (24GiB).<br>
Do I need to manually clear the GPU cache?</p>
<p>When I tried to train a different subset of my own data afterwards it would take about a minute after every epoch to resume the engine run (see below).</p>
<p><em>[2024-09-24 13:45:26,169] [16008] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:876) - Engine run resuming from iteration 0, epoch 0 until 1 epochs</em><br>
<em>[2024-09-24 13:46:12,469] [16008] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:259) - Got new best metric of val_mean_dice: 0.0</em><br>
<em>2024-09-24 13:46:12,469 - INFO - Epoch[1] Metrics – val_mean_dice: 0.0000 val_skeletal_muscle_mean_dice: 0.0000 val_subcutaneous_fat_mean_dice: 0.0000 val_torso_fat_mean_dice: 0.0000</em></p>
<p>During the first training that generated the offset, training was a lot quicker. Eventually, the offset was recreated regardless of training and testing both only left shoulder scans and also using mixed unilateral scans.</p>
<p>Finally, is there a way to compare the outputs of different models? Auto Segmentation/Models only shows “segmentation” as an option, even though the different models (all producing offset) have been saved with unique names. Could I even be testing on a wrong model?</p>
<p>I would highly appreciate any inputs. Thank you!</p>
<p>Best regards,<br>
Dennis</p>

---

## Post #2 by @gendex (2024-10-03 14:19 UTC)

<p>Hello again, I’d like to provide an update on the situation, give some more background info, reorganize the issues that I’ve encountered and pose more concise questions.</p>
<p>I have recently started using MONAI for a research project that involves automating the segmentation of the scapula to extract bone density values that then could potentially be used for surgical planning. My background is in biomechanics with some but limited programming skills. However, I have been using 3D Slicer for almost a year now.</p>
<p>I have a dataset of shoulder CT scans that are cropped in a way that the crop axis is not aligned with the scanning axis and when loading them into 3D Slicer, some scans appear rotated. I used TotalSegmentator to segment the scapula and other structures of interest, and the different orientations of the scans did not seem to be a problem.</p>
<p>Since MONAI seems to be preprocessing the data with transforms etc., I assume that the differently oriented scans should not cause any issues when training a segmentation model in MONAI. Is that correct?</p>
<p>To get to know how MONAI works, I tested segmenting the spleen dataset on the pretrained spleen model and that worked fine.</p>
<p>As a first test using my own data, I trained a subset of 7 scans (average dimensions: 1000x500x150, average spacing: 0.25x0.25x1mm) with 3 segments each (adjusted segmentation.py in configs accordingly) using the segmentation model for 500 epochs on an Nvidia RTX 4090 with 24GiB. The training was successfully completed in about an hour.</p>
<p>Does this training duration fall into the expected time range?</p>
<p>I then wanted to test the performance of the trained model using the Auto Segmentation tab. The dropdown menu in that tab had “segmentation” as the only option. I loaded the next sample that didn’t have any ground truth segmentations and hit run. The resulting segmentations had roughly the desired shape, but they were offset so much, that they lay outside the body (see image below).</p>
<p>Am I testing on my own model?</p>
<p>How can I specify which model I want to test on?</p>
<p>Are these results to be expected or is that sufficient training to expect better results?</p>
<p>Do I need to increase the number of scans and epochs to get better results?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a608243f9f1d6a1021755e7db2fa9536b0f01e5.png" data-download-href="/uploads/short-url/62SP1FIafwoPfDEsTmFvlhhXSWF.png?dl=1" title="output_offset" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a608243f9f1d6a1021755e7db2fa9536b0f01e5_2_690x221.png" alt="output_offset" data-base62-sha1="62SP1FIafwoPfDEsTmFvlhhXSWF" width="690" height="221" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a608243f9f1d6a1021755e7db2fa9536b0f01e5_2_690x221.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a608243f9f1d6a1021755e7db2fa9536b0f01e5_2_1035x331.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/a/2a608243f9f1d6a1021755e7db2fa9536b0f01e5_2_1380x442.png 2x" data-dominant-color="2E2A25"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">output_offset</span><span class="informations">1474×474 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After restarting the server in the same app with a different dataset loaded, I trained another segmentation model giving it a different name in the options tab. After successful training, there still is only the same single model (“segmentation”) available in the Auto Segmentation tab.</p>
<p>Which model am I testing on if I load the next unlabeled scan and hit run?</p>
<p>How can I choose which model I want to test on?</p>
<p>Is it even possible to have multiple segmentation models in the same app or do I have to create a new app for every model?</p>
<p>Is there a way to visualize the segmentation outputs from the validation scans when val_split is &gt;0 / when there are scans used for validation?</p>
<p>To check if there is something wrong with my dataset I tried to reproduce the offset results. I used a subset (16 chest CT scans) of the TotalSegmentator dataset and ran TotalSegmentator on those scans to get the needed segmentations. Then, I loaded the data into the same app and started training, again with the segmentation model. After the first epoch, it timed out giving the following error message:</p>
<p><em>[2024-09-24 12:20:11,585] [17576] [MainThread] [INFO] (monailabel.tasks.train.basic_train:264) - 0 - Records for Training: 16</em><br>
<em>[2024-09-24 12:20:11,588] [17576] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:876) - Engine run resuming from iteration 0, epoch 0 until 100 epochs</em><br>
<em>2024-09-24 12:20:13,821 - INFO - Epoch: 1/100, Iter: 1/16 – train_loss: 2.7914</em><br>
<em>2024-09-24 12:20:14,936 - INFO - Epoch: 1/100, Iter: 2/16 – train_loss: 2.2761</em><br>
<em>2024-09-24 12:20:15,729 - INFO - Epoch: 1/100, Iter: 3/16 – train_loss: 1.9255</em><br>
<em>2024-09-24 12:20:16,620 - INFO - Epoch: 1/100, Iter: 4/16 – train_loss: 1.9023</em><br>
<em>2024-09-24 12:20:17,308 - INFO - Epoch: 1/100, Iter: 5/16 – train_loss: 1.9119</em><br>
<em>2024-09-24 12:20:18,056 - INFO - Epoch: 1/100, Iter: 6/16 – train_loss: 2.3988</em><br>
<em>2024-09-24 12:20:18,838 - INFO - Epoch: 1/100, Iter: 7/16 – train_loss: 1.9958</em><br>
<em>2024-09-24 12:20:19,639 - INFO - Epoch: 1/100, Iter: 8/16 – train_loss: 1.9923</em><br>
<em>2024-09-24 12:20:20,427 - INFO - Epoch: 1/100, Iter: 9/16 – train_loss: 2.3822</em><br>
<em>2024-09-24 12:20:21,259 - INFO - Epoch: 1/100, Iter: 10/16 – train_loss: 2.1640</em><br>
<em>2024-09-24 12:20:22,024 - INFO - Epoch: 1/100, Iter: 11/16 – train_loss: 1.8334</em><br>
<em>2024-09-24 12:20:22,963 - INFO - Epoch: 1/100, Iter: 12/16 – train_loss: 1.8153</em><br>
<em>2024-09-24 12:20:23,869 - INFO - Epoch: 1/100, Iter: 13/16 – train_loss: 1.9521</em><br>
<em>2024-09-24 12:20:24,715 - INFO - Epoch: 1/100, Iter: 14/16 – train_loss: 1.7093</em><br>
<em>2024-09-24 12:20:25,162 - INFO - Epoch: 1/100, Iter: 15/16 – train_loss: 2.0465</em><br>
<em>2024-09-24 12:20:25,813 - INFO - Epoch: 1/100, Iter: 16/16 – train_loss: 2.4063</em><br>
<em>[2024-09-24 12:20:25,819] [17576] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:259) - Got new best metric of train_mean_dice: 0.04801511764526367</em><br>
<em>2024-09-24 12:20:25,819 - INFO - Epoch[1] Metrics – train_mean_dice: 0.0480 train_skeletal_muscle_mean_dice: 0.1105 train_subcutaneous_fat_mean_dice: 0.0133 train_torso_fat_mean_dice: 0.0000</em><br>
<em>2024-09-24 12:20:25,819 - INFO - Key metric: train_mean_dice best value: 0.04801511764526367 at epoch: 1</em><br>
<em>[2024-09-24 12:20:25,830] [17576] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:876) - Engine run resuming from iteration 0, epoch 0 until 1 epochs</em><br>
<em>[2024-09-24 12:32:03,933] [17576] [MainThread] [ERROR] (ignite.engine.engine.SupervisedEvaluator:1086) - Current run is terminating due to exception: applying transform &lt;monai.transforms.compose.Compose object at 0x000001D6A6078CD0&gt;</em><br>
<em>2024-09-24 12:32:03,933 - ERROR - Exception: applying transform &lt;monai.transforms.compose.Compose object at 0x000001D6A6078CD0&gt;</em></p>
<p>I don’t understand this error.</p>
<p>Is MONAI struggling to transform the scans?</p>
<p>Or is the GPU struggling to process that amount of data?</p>
<p>How much data can a single Nvidia RTX 4090 (24GiB) handle?</p>
<p>Is there a buildup of cache when training multiple models in the same app?</p>
<p>With this comparison failed, I set out to train another model with a different subset of my own data. This time I loaded 13 scans with roughly the same dimensions and spacing (as the original dataset) and trained again. Training took a lot longer this time. After every epoch training seemed to pause for about one minute at this point (same as where the error happened previously):</p>
<p><em>[2024-09-24 13:45:24,528] [16008] [MainThread] [INFO] (monailabel.tasks.train.basic_train:264) - 0 - Records for Training: 13</em><br>
<em>[2024-09-24 13:45:24,530] [16008] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:876) - Engine run resuming from iteration 0, epoch 0 until 100 epochs</em><br>
<em>2024-09-24 13:45:24,786 - INFO - Epoch: 1/100, Iter: 1/13 – train_loss: 2.4122</em><br>
<em>2024-09-24 13:45:24,878 - INFO - Epoch: 1/100, Iter: 2/13 – train_loss: 2.3242</em><br>
<em>2024-09-24 13:45:24,992 - INFO - Epoch: 1/100, Iter: 3/13 – train_loss: 2.0153</em><br>
<em>2024-09-24 13:45:25,109 - INFO - Epoch: 1/100, Iter: 4/13 – train_loss: 1.6996</em><br>
<em>2024-09-24 13:45:25,225 - INFO - Epoch: 1/100, Iter: 5/13 – train_loss: 2.2290</em><br>
<em>2024-09-24 13:45:25,340 - INFO - Epoch: 1/100, Iter: 6/13 – train_loss: 1.4649</em><br>
<em>2024-09-24 13:45:25,456 - INFO - Epoch: 1/100, Iter: 7/13 – train_loss: 1.4484</em><br>
<em>2024-09-24 13:45:25,570 - INFO - Epoch: 1/100, Iter: 8/13 – train_loss: 1.4148</em><br>
<em>2024-09-24 13:45:25,686 - INFO - Epoch: 1/100, Iter: 9/13 – train_loss: 1.3817</em><br>
<em>2024-09-24 13:45:25,802 - INFO - Epoch: 1/100, Iter: 10/13 – train_loss: 2.7751</em><br>
<em>2024-09-24 13:45:25,925 - INFO - Epoch: 1/100, Iter: 11/13 – train_loss: 2.1342</em><br>
<em>2024-09-24 13:45:26,040 - INFO - Epoch: 1/100, Iter: 12/13 – train_loss: 1.7436</em><br>
<em>2024-09-24 13:45:26,153 - INFO - Epoch: 1/100, Iter: 13/13 – train_loss: 1.3803</em><br>
<em>[2024-09-24 13:45:26,157] [16008] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:259) - Got new best metric of train_mean_dice: 0.0</em><br>
<em>2024-09-24 13:45:26,157 - INFO - Epoch[1] Metrics – train_mean_dice: 0.0000 train_skeletal_muscle_mean_dice: 0.0000 train_subcutaneous_fat_mean_dice: 0.0000 train_torso_fat_mean_dice: 0.0000</em><br>
<em>2024-09-24 13:45:26,157 - INFO - Key metric: train_mean_dice best value: 0.0 at epoch: 1</em><br>
<em>[2024-09-24 13:45:26,169] [16008] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:876) - Engine run resuming from iteration 0, epoch 0 until 1 epochs</em><br>
<em>[2024-09-24 13:46:12,469] [16008] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:259) - Got new best metric of val_mean_dice: 0.0</em><br>
<em>2024-09-24 13:46:12,469 - INFO - Epoch[1] Metrics – val_mean_dice: 0.0000 val_skeletal_muscle_mean_dice: 0.0000 val_subcutaneous_fat_mean_dice: 0.0000 val_torso_fat_mean_dice: 0.0000</em><br>
<em>2024-09-24 13:46:12,469 - INFO - Key metric: val_mean_dice best value: 0.0 at epoch: 1</em><br>
<em>[2024-09-24 13:46:12,553] [16008] [MainThread] [INFO] (monailabel.tasks.train.handler:86) - New Model published: C:\Users\Eva\radiologyBoneDensity\model\segmentation\test_rem_pat\model.pt =&gt; C:\Users\Eva\radiologyBoneDensity\model\segmentation.pt</em><br>
<em>[2024-09-24 13:46:12,554] [16008] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:972) - Epoch[1] Complete. Time taken: 00:00:46.368</em><br>
<em>[2024-09-24 13:46:12,555] [16008] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:988) - Engine run complete. Time taken: 00:00:46.386</em><br>
<em>[2024-09-24 13:46:12,607] [16008] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:972) - Epoch[1] Complete. Time taken: 00:00:48.035</em><br>
<em>2024-09-24 13:46:12,835 - INFO - Epoch: 2/100, Iter: 1/13 – train_loss: 1.7215</em><br>
<em>2024-09-24 13:46:13,029 - INFO - Epoch: 2/100, Iter: 2/13 – train_loss: 1.3821</em><br>
<em>2024-09-24 13:46:13,217 - INFO - Epoch: 2/100, Iter: 3/13 – train_loss: 1.6698</em><br>
<em>2024-09-24 13:46:13,416 - INFO - Epoch: 2/100, Iter: 4/13 – train_loss: 1.7367</em><br>
<em>2024-09-24 13:46:13,609 - INFO - Epoch: 2/100, Iter: 5/13 – train_loss: 1.7043</em><br>
<em>2024-09-24 13:46:13,824 - INFO - Epoch: 2/100, Iter: 6/13 – train_loss: 1.6097</em><br>
<em>2024-09-24 13:46:14,019 - INFO - Epoch: 2/100, Iter: 7/13 – train_loss: 2.4585</em><br>
<em>2024-09-24 13:46:14,211 - INFO - Epoch: 2/100, Iter: 8/13 – train_loss: 1.6047</em><br>
<em>2024-09-24 13:46:14,419 - INFO - Epoch: 2/100, Iter: 9/13 – train_loss: 1.8360</em><br>
<em>2024-09-24 13:46:14,642 - INFO - Epoch: 2/100, Iter: 10/13 – train_loss: 1.3524</em><br>
<em>2024-09-24 13:46:14,860 - INFO - Epoch: 2/100, Iter: 11/13 – train_loss: 1.7037</em><br>
<em>2024-09-24 13:46:15,045 - INFO - Epoch: 2/100, Iter: 12/13 – train_loss: 1.4732</em><br>
<em>2024-09-24 13:46:15,241 - INFO - Epoch: 2/100, Iter: 13/13 – train_loss: 1.3968</em><br>
<em>[2024-09-24 13:46:15,256] [16008] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:259) - Got new best metric of train_mean_dice: 0.04763128608465195</em><br>
<em>2024-09-24 13:46:15,257 - INFO - Epoch[2] Metrics – train_mean_dice: 0.0476 train_skeletal_muscle_mean_dice: 0.0953 train_subcutaneous_fat_mean_dice: 0.0000 train_torso_fat_mean_dice: 0.0000</em><br>
<em>2024-09-24 13:46:15,257 - INFO - Key metric: train_mean_dice best value: 0.04763128608465195 at epoch: 2</em><br>
<em>[2024-09-24 13:46:15,259] [16008] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:876) - Engine run resuming from iteration 0, epoch 1 until 2 epochs</em><br>
<em>[2024-09-24 13:47:01,627] [16008] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:259) - Got new best metric of val_mean_dice: 0.024709107354283333</em><br>
<em>2024-09-24 13:47:01,627 - INFO - Epoch[2] Metrics – val_mean_dice: 0.0247 val_skeletal_muscle_mean_dice: 0.0741 val_subcutaneous_fat_mean_dice: 0.0000 val_torso_fat_mean_dice: 0.0000</em></p>
<p>I expected training to take longer in a somewhat exponential way, but I didn’t expect such a big difference (around 5secs per epoch in the first training with 7 samples vs 1min per epoch with 13 samples).</p>
<p>What is happening in that step?</p>
<p>Is this increase in training time expected?</p>
<p>Any input would be greatly appreciated.</p>

---

## Post #3 by @pieper (2024-10-04 13:56 UTC)

<aside class="quote no-group" data-username="gendex" data-post="2" data-topic="38559">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/g/ea5d25/48.png" class="avatar"> gendex:</div>
<blockquote>
<p>Since MONAI seems to be preprocessing the data with transforms etc., I assume that the differently oriented scans should not cause any issues when training a segmentation model in MONAI. Is that correct?</p>
</blockquote>
</aside>
<p>I would guess not and that you need to resample the volumes and labelmaps to the same pixel space for MONAI.</p>
<p>As for your other questions, they may get resolved after you get past this first issue. But if not, maybe try asking one small question per post.</p>

---
