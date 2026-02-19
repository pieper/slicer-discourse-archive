---
topic_id: 30689
title: "Training And Validation Dice Values Are 0"
date: 2023-07-19
url: https://discourse.slicer.org/t/30689
---

# Training and Validation Dice Values are 0

**Topic ID**: 30689
**Date**: 2023-07-19
**URL**: https://discourse.slicer.org/t/training-and-validation-dice-values-are-0/30689

---

## Post #1 by @Dexter_Luth (2023-07-19 20:11 UTC)

<p>Hi,<br>
When training a model all training and validation dice values are zero. configs segmentation module has been tailored to our needs by changing label titles and setting pretrained model loading to false.<br>
Here is some terminal output: <a href="https://github.com/Project-MONAI/MONAILabel/files/12099668/terminal.txt" rel="noopener nofollow ugc">terminal.txt</a></p>
<p>GPU: NVIDIA GeForce RTX 4090<br>
MONAILabel version: 0.7.0<br>
Numpy version: 1.24.1<br>
Pytorch version: 2.1.0.dev20230523+cu117<br>
MONAILabel rev id: <a href="https://github.com/Project-MONAI/MONAILabel/commit/bfb4f8cda6a82d3d6e3d26dbf35980d5ed42f335" rel="noopener nofollow ugc">bfb4f8c</a></p>
<p>Any help is appreciated!<br>
Thanks!</p>

---

## Post #2 by @njeffery (2023-09-13 08:20 UTC)

<p>Hi,<br>
Noticed you had posted this on git too. Did you get an answer? I am having a similar problem. Trained monai task of finding an eyeball on T2 MR images and all works well server wise (no error messages). Appears to go through the process of creating a segmentation (terminal output below), which then doesn’t appear in slicer (nor in the tmp directory). Looking back I can see that the dice values are always zero (see terminal text below), and the accuracy bar in 3Dslicer doesn’t change. Anyone any ideas?<br>
thanks<br>
nat</p>
<p>Sorry had to crop the terminal output due to char limit</p>
<pre><code class="lang-auto">[2023-09-13 08:31:58,103] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:972) - Epoch[45] Complete. Time taken: 00:00:00.672
[2023-09-13 08:31:58,232] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:294) - Epoch: 46/50, Iter: 1/3 -- train_loss: 0.6210
[2023-09-13 08:31:58,363] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:294) - Epoch: 46/50, Iter: 2/3 -- train_loss: 0.6227
[2023-09-13 08:31:58,490] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:294) - Epoch: 46/50, Iter: 3/3 -- train_loss: 0.6205
[2023-09-13 08:31:58,497] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:223) - Epoch[46] Metrics -- train_Left_Eye_mean_dice: 0.0000 train_mean_dice: 0.0000
[2023-09-13 08:31:58,497] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:234) - Key metric: train_mean_dice best value: 0.003613139037042856 at epoch: 1
[2023-09-13 08:31:58,503] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:876) - Engine run resuming from iteration 0, epoch 45 until 46 epochs
[2023-09-13 08:31:58,766] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:223) - Epoch[46] Metrics -- val_Left_Eye_mean_dice: 0.0000 val_mean_dice: 0.0000
[2023-09-13 08:31:58,766] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:234) - Key metric: val_mean_dice best value: 0.0 at epoch: 1
[2023-09-13 08:31:58,781] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:972) - Epoch[46] Complete. Time taken: 00:00:00.074
[2023-09-13 08:31:58,785] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:988) - Engine run complete. Time taken: 00:00:00.282
[2023-09-13 08:31:58,785] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:972) - Epoch[46] Complete. Time taken: 00:00:00.682
[2023-09-13 08:31:58,914] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:294) - Epoch: 47/50, Iter: 1/3 -- train_loss: 0.6229
[2023-09-13 08:31:59,042] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:294) - Epoch: 47/50, Iter: 2/3 -- train_loss: 0.6196
[2023-09-13 08:31:59,169] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:294) - Epoch: 47/50, Iter: 3/3 -- train_loss: 0.6192
[2023-09-13 08:31:59,177] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:223) - Epoch[47] Metrics -- train_Left_Eye_mean_dice: 0.0000 train_mean_dice: 0.0000
[2023-09-13 08:31:59,177] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:234) - Key metric: train_mean_dice best value: 0.003613139037042856 at epoch: 1
[2023-09-13 08:31:59,182] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:876) - Engine run resuming from iteration 0, epoch 46 until 47 epochs
[2023-09-13 08:31:59,434] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:223) - Epoch[47] Metrics -- val_Left_Eye_mean_dice: 0.0000 val_mean_dice: 0.0000
[2023-09-13 08:31:59,434] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:234) - Key metric: val_mean_dice best value: 0.0 at epoch: 1
[2023-09-13 08:31:59,448] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:972) - Epoch[47] Complete. Time taken: 00:00:00.072
[2023-09-13 08:31:59,451] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:988) - Engine run complete. Time taken: 00:00:00.269
[2023-09-13 08:31:59,451] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:972) - Epoch[47] Complete. Time taken: 00:00:00.666
[2023-09-13 08:31:59,582] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:294) - Epoch: 48/50, Iter: 1/3 -- train_loss: 0.6222
[2023-09-13 08:31:59,710] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:294) - Epoch: 48/50, Iter: 2/3 -- train_loss: 0.6218
[2023-09-13 08:31:59,838] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:294) - Epoch: 48/50, Iter: 3/3 -- train_loss: 0.6183
[2023-09-13 08:31:59,845] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:223) - Epoch[48] Metrics -- train_Left_Eye_mean_dice: 0.0000 train_mean_dice: 0.0000
[2023-09-13 08:31:59,846] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:234) - Key metric: train_mean_dice best value: 0.003613139037042856 at epoch: 1
[2023-09-13 08:31:59,851] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:876) - Engine run resuming from iteration 0, epoch 47 until 48 epochs
[2023-09-13 08:32:00,109] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:223) - Epoch[48] Metrics -- val_Left_Eye_mean_dice: 0.0000 val_mean_dice: 0.0000
[2023-09-13 08:32:00,109] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:234) - Key metric: val_mean_dice best value: 0.0 at epoch: 1
[2023-09-13 08:32:00,125] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:972) - Epoch[48] Complete. Time taken: 00:00:00.073
[2023-09-13 08:32:00,128] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:988) - Engine run complete. Time taken: 00:00:00.277
[2023-09-13 08:32:00,128] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:972) - Epoch[48] Complete. Time taken: 00:00:00.677
[2023-09-13 08:32:00,260] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:294) - Epoch: 49/50, Iter: 1/3 -- train_loss: 0.6210
[2023-09-13 08:32:00,388] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:294) - Epoch: 49/50, Iter: 2/3 -- train_loss: 0.6210
[2023-09-13 08:32:00,516] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:294) - Epoch: 49/50, Iter: 3/3 -- train_loss: 0.6205
[2023-09-13 08:32:00,524] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:223) - Epoch[49] Metrics -- train_Left_Eye_mean_dice: 0.0000 train_mean_dice: 0.0000
[2023-09-13 08:32:00,524] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:234) - Key metric: train_mean_dice best value: 0.003613139037042856 at epoch: 1
[2023-09-13 08:32:00,529] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:876) - Engine run resuming from iteration 0, epoch 48 until 49 epochs
[2023-09-13 08:32:00,796] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:223) - Epoch[49] Metrics -- val_Left_Eye_mean_dice: 0.0000 val_mean_dice: 0.0000
[2023-09-13 08:32:00,797] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:234) - Key metric: val_mean_dice best value: 0.0 at epoch: 1
[2023-09-13 08:32:00,812] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:972) - Epoch[49] Complete. Time taken: 00:00:00.073
[2023-09-13 08:32:00,815] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:988) - Engine run complete. Time taken: 00:00:00.285
[2023-09-13 08:32:00,815] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:972) - Epoch[49] Complete. Time taken: 00:00:00.687
[2023-09-13 08:32:00,944] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:294) - Epoch: 50/50, Iter: 1/3 -- train_loss: 0.6169
[2023-09-13 08:32:01,072] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:294) - Epoch: 50/50, Iter: 2/3 -- train_loss: 0.6198
[2023-09-13 08:32:01,198] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:294) - Epoch: 50/50, Iter: 3/3 -- train_loss: 0.6196
[2023-09-13 08:32:01,206] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:223) - Epoch[50] Metrics -- train_Left_Eye_mean_dice: 0.0000 train_mean_dice: 0.0000
[2023-09-13 08:32:01,206] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:234) - Key metric: train_mean_dice best value: 0.003613139037042856 at epoch: 1
[2023-09-13 08:32:01,211] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:876) - Engine run resuming from iteration 0, epoch 49 until 50 epochs
[2023-09-13 08:32:01,475] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:223) - Epoch[50] Metrics -- val_Left_Eye_mean_dice: 0.0000 val_mean_dice: 0.0000
[2023-09-13 08:32:01,475] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:234) - Key metric: val_mean_dice best value: 0.0 at epoch: 1
[2023-09-13 08:32:01,490] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:972) - Epoch[50] Complete. Time taken: 00:00:00.074
[2023-09-13 08:32:01,493] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:988) - Engine run complete. Time taken: 00:00:00.282
[2023-09-13 08:32:01,494] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:972) - Epoch[50] Complete. Time taken: 00:00:00.679
[2023-09-13 08:32:01,726] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:280) - Train completed, saved final checkpoint: C:\Users\userName\apps\radiology\model\segmentation\train_01\checkpoint_final.pt
[2023-09-13 08:32:01,726] [19180] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:988) - Engine run complete. Time taken: 00:00:32.478
[2023-09-13 08:32:01,741] [19180] [MainThread] [INFO] (monailabel.tasks.train.basic_train:608) - Running cleanup...
[2023-09-13 08:32:01,741] [19180] [MainThread] [INFO] (__main__:61) - Result: {"rank": 0, "current_epoch": 50, "current_iteration": 150, "total_epochs": 50, "total_iterations": 3, "epoch": 50, "start_ts": 1694590286, "total_time": "0:00:35", "best_metric": 0.0, "train": {"metrics": {"train_mean_dice": 0.0, "train_Left_Eye_mean_dice": 0.0}, "key_metric_name": "train_mean_dice", "best_metric": 0.003613139037042856, "best_metric_epoch": 1}, "eval": {"metrics": {"val_mean_dice": 0.0, "val_Left_Eye_mean_dice": 0.0}, "key_metric_name": "val_mean_dice", "best_metric": 0.0, "best_metric_epoch": 1}}
[2023-09-13 08:32:02,472] [10904] [ThreadPoolExecutor-2_0] [INFO] (monailabel.utils.async_tasks.utils:83) - Return code: 0
[2023-09-13 08:33:16,219] [10904] [MainThread] [INFO] (monailabel.endpoints.activelearning:44) - Active Learning Request: {'strategy': 'random', 'client_id': 'user-xyz'}
[2023-09-13 08:33:16,236] [10904] [MainThread] [INFO] (monailabel.tasks.activelearning.random:47) - Random: Selected Image: sub-OAS30676_sess-d5558_T2w; Weight: 47183
[2023-09-13 08:33:16,243] [10904] [MainThread] [INFO] (monailabel.endpoints.activelearning:60) - Next sample: {'id': 'sub-OAS30676_sess-d5558_T2w', 'weight': 47183, 'path': 'C:\\Users\\userName\\Desktop\\Monai-test\\sub-OAS30676_sess-d5558_T2w.nii.gz', 'ts': 1694526916, 'name': 'sub-OAS30676_sess-d5558_T2w.nii.gz'}
[2023-09-13 08:34:01,985] [10904] [MainThread] [INFO] (monailabel.endpoints.infer:161) - Infer Request: {'model': 'segmentation', 'image': 'sub-OAS30676_sess-d5558_T2w', 'largest_cc': False, 'device': 'NVIDIA RTX A5000', 'result_extension': '.nrrd', 'result_dtype': 'uint8', 'client_id': 'user-xyz'}
[2023-09-13 08:34:01,986] [10904] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:277) - Infer Request (final): {'largest_cc': False, 'device': 'cuda', 'model': 'segmentation', 'image': 'C:\\Users\\userName\\Desktop\\Monai-test\\sub-OAS30676_sess-d5558_T2w.nii.gz', 'result_extension': '.nrrd', 'result_dtype': 'uint8', 'client_id': 'user-xyz', 'description': 'A pre-trained model for volumetric (3D) Segmentation from CT image'}
monai.transforms.io.dictionary LoadImaged.__init__:image_only: Current default value of argument `image_only=False` has been deprecated since version 1.1. It will be changed to `image_only=True` in version 1.3.
[2023-09-13 08:34:01,988] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:76) - PRE - Run Transform(s)
[2023-09-13 08:34:01,988] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:77) - PRE - Input Keys: ['largest_cc', 'device', 'model', 'image', 'result_extension', 'result_dtype', 'client_id', 'description', 'image_path']
[2023-09-13 08:34:02,093] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (LoadImaged): Time: 0.1046; image: torch.Size([176, 240, 256])(torch.float32)
[2023-09-13 08:34:02,219] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (EnsureTyped): Time: 0.126; image: torch.Size([176, 240, 256])(torch.float32)
[2023-09-13 08:34:02,220] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (EnsureChannelFirstd): Time: 0.001; image: torch.Size([1, 176, 240, 256])(torch.float32)
[2023-09-13 08:34:02,222] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (Orientationd): Time: 0.002; image: torch.Size([1, 176, 240, 256])(torch.float32)
[2023-09-13 08:34:05,067] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (Spacingd): Time: 2.8434; image: torch.Size([1, 141, 169, 180])(torch.float32)
[2023-09-13 08:34:05,094] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (NormalizeIntensityd): Time: 0.027; image: torch.Size([1, 141, 169, 180])(torch.float32)
[2023-09-13 08:34:06,606] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (GaussianSmoothd): Time: 1.5112; image: torch.Size([1, 141, 169, 180])(torch.float32)
[2023-09-13 08:34:06,612] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - PRE - Transform (ScaleIntensityd): Time: 0.006; image: torch.Size([1, 141, 169, 180])(torch.float32)
[2023-09-13 08:34:06,612] [10904] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:480) - Inferer:: cuda =&gt; SlidingWindowInferer =&gt; {'roi_size': (96, 96, 96), 'sw_batch_size': 2, 'overlap': 0.4, 'mode': gaussian, 'sigma_scale': 0.125, 'padding_mode': 'replicate', 'cval': 0.0, 'sw_device': None, 'device': None, 'progress': False, 'cpu_thresh': None, 'buffer_steps': None, 'buffer_dim': -1, 'roi_weight_map': None}
[2023-09-13 08:34:06,613] [10904] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:418) - Infer model path: C:\Users\userName\apps\radiology\model\segmentation.pt
[2023-09-13 08:34:07,424] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:76) - INV - Run Transform(s)
[2023-09-13 08:34:07,424] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:77) - INV - Input Keys: ['largest_cc', 'device', 'model', 'image', 'result_extension', 'result_dtype', 'client_id', 'description', 'image_path', 'image_meta_dict', 'latencies', 'pred']
[2023-09-13 08:34:07,432] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - INV - Transform (Spacingd): Time: 0.006; image: torch.Size([2, 176, 240, 256])(torch.float32); pred: torch.Size([2, 141, 169, 180])(torch.float32)
[2023-09-13 08:34:07,434] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - INV - Transform (Orientationd): Time: 0.002; image: torch.Size([2, 176, 240, 256])(torch.float32); pred: torch.Size([2, 141, 169, 180])(torch.float32)
[2023-09-13 08:34:07,434] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:76) - POST - Run Transform(s)
[2023-09-13 08:34:07,434] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:77) - POST - Input Keys: ['largest_cc', 'device', 'model', 'image', 'result_extension', 'result_dtype', 'client_id', 'description', 'image_path', 'image_meta_dict', 'latencies', 'pred']
[2023-09-13 08:34:07,435] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (EnsureTyped): Time: 0.0; image: torch.Size([1, 141, 169, 180])(torch.float32); pred: torch.Size([2, 176, 240, 256])(torch.float32)
[2023-09-13 08:34:07,435] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (Activationsd): Time: 0.0; image: torch.Size([1, 141, 169, 180])(torch.float32); pred: torch.Size([2, 176, 240, 256])(torch.float32)
[2023-09-13 08:34:07,437] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (AsDiscreted): Time: 0.0; image: torch.Size([1, 141, 169, 180])(torch.float32); pred: torch.Size([1, 176, 240, 256])(torch.float32)
[2023-09-13 08:34:07,437] [10904] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (Restored): Time: 0.0; image: torch.Size([1, 141, 169, 180])(torch.float32); pred: torch.Size([176, 240, 256])(torch.float32)
[2023-09-13 08:34:07,437] [10904] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:580) - Writing Result...
[2023-09-13 08:34:07,438] [10904] [MainThread] [INFO] (monailabel.transform.writer:196) - Result ext: .nrrd; write_to_file: True; dtype: uint8
[2023-09-13 08:34:11,559] [10904] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:332) - ++ Latencies =&gt; Total: 9.5728; Pre: 4.6262; Inferer: 0.8112; Invert: 0.0110; Post: 0.0030; Write: 4.1214
[2023-09-13 08:34:11,559] [10904] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:356) - Result File: C:\Users\userName\AppData\Local\Temp\tmpniwrvdyt.nrrd
[2023-09-13 08:34:11,560] [10904] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:357) - Result Json Keys: ['label_names', 'latencies']
</code></pre>

---

## Post #3 by @dh221811 (2024-06-06 11:04 UTC)

<p>Hi<br>
I’m currently experiencing the exact same problem with the dice values always being zero after each epoch and I am unsure of the cause.<br>
I trained the model now with 37 CT-datasets with 10 epochs. Basically, the train loss goes down a little with each epoch but after each epoch the dice value is still zero. Same thing with the accuracy bar in 3D Slicer, it still remains at 0%.<br>
Have there been any updates or progress in understanding why this might be happening? Any insights or solutions would be greatly appreciated, as I’m quite stuck at the moment.<br>
Thank you!<br>
J.</p>

---
