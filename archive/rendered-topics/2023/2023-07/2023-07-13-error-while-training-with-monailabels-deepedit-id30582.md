# Error while training with MONAILabel's deepedit

**Topic ID**: 30582
**Date**: 2023-07-13
**URL**: https://discourse.slicer.org/t/error-while-training-with-monailabels-deepedit/30582

---

## Post #1 by @lukasvanderstricht (2023-07-13 12:34 UTC)

<p>Dear all</p>
<p>I am currently using 3D Slicer and its MONAILabel extension to train a segmentation model using the DeepEdit model from the predefined radiology app. Both manual segmentation and training have been going smoothly up till now and the automatic segmentation functionality seems to be doing its job.<br>
However, when I want to further train the model at this point, without having added any new labels (so just starting the training process again), I always get one of the two following errors</p>
<ol>
<li>Exit code -9</li>
</ol>
<blockquote>
<p>[2023-07-13 08:52:08,765] [24408] [MainThread] [INFO] (monailabel.utils.sessions:51) - Session Path: /home/dellxpsazdelta/.cache/monailabel/sessions<br>
[2023-07-13 08:52:08,765] [24408] [MainThread] [INFO] (monailabel.utils.sessions:52) - Session Expiry (max): 3600<br>
[2023-07-13 08:52:08,765] [24408] [MainThread] [INFO] (monailabel.tasks.train.basic_train:353) - Train Request (input): {‘model’: ‘deepedit’, ‘name’: ‘train_01’, ‘pretrained’: 1, ‘device’: ‘cuda’, ‘max_epochs’: 50, ‘early_stop_patience’: -1, ‘val_split’: 0.2, ‘train_batch_size’: 1, ‘val_batch_size’: 1, ‘multi_gpu’: True, ‘gpus’: ‘all’, ‘dataset’: ‘CacheDataset’, ‘dataloader’: ‘ThreadDataLoader’, ‘client_id’: ‘user-xyz’, ‘local_rank’: 0}<br>
[2023-07-13 08:52:08,766] [24408] [MainThread] [INFO] (monailabel.tasks.train.basic_train:363) - CUDA_VISIBLE_DEVICES: 0,1<br>
[2023-07-13 08:52:08,767] [24408] [MainThread] [INFO] (monailabel.tasks.train.basic_train:368) - Distributed/Multi GPU is limited<br>
[2023-07-13 08:52:08,767] [24408] [MainThread] [INFO] (monailabel.tasks.train.basic_train:381) - Distributed Training = FALSE<br>
[2023-07-13 08:52:08,767] [24408] [MainThread] [INFO] (monailabel.tasks.train.basic_train:408) - 0 - Train Request (final): {‘name’: ‘train_01’, ‘pretrained’: 1, ‘device’: ‘cuda’, ‘max_epochs’: 50, ‘early_stop_patience’: -1, ‘val_split’: 0.2, ‘train_batch_size’: 1, ‘val_batch_size’: 1, ‘multi_gpu’: False, ‘gpus’: ‘all’, ‘dataset’: ‘CacheDataset’, ‘dataloader’: ‘ThreadDataLoader’, ‘model’: ‘deepedit’, ‘client_id’: ‘user-xyz’, ‘local_rank’: 0, ‘run_id’: ‘20230713_0852’}<br>
[2023-07-13 08:52:08,768] [24408] [MainThread] [INFO] (monailabel.tasks.train.basic_train:504) - 0 - Using Device: cuda; IDX: None<br>
[2023-07-13 08:52:08,768] [24408] [MainThread] [INFO] (monailabel.tasks.train.basic_train:331) - Total Records for Training: 5<br>
[2023-07-13 08:52:08,768] [24408] [MainThread] [INFO] (monailabel.tasks.train.basic_train:332) - Total Records for Validation: 1<br>
Loading dataset:   0%|          | 0/1 [00:00&lt;?, ?it/s]<br>
Loading dataset: 100%|██████████| 1/1 [00:10&lt;00:00, 10.10s/it]<br>
Loading dataset: 100%|██████████| 1/1 [00:10&lt;00:00, 10.10s/it]<br>
[2023-07-13 08:53:05,649] [24408] [MainThread] [INFO] (monailabel.tasks.train.basic_train:275) - 0 - Records for Validation: 1<br>
[2023-07-13 08:53:05,748] [24408] [MainThread] [INFO] (monailabel.tasks.train.basic_train:265) - 0 - Adding Validation to run every ‘1’ interval<br>
[2023-07-13 08:53:05,749] [24408] [MainThread] [INFO] (monailabel.tasks.train.basic_train:591) - 0 - Load Path /home/dellxpsazdelta/radiology_psoas_azd/model/deepedit_dynunet/train_01/model.pt<br>
Loading dataset:   0%|          | 0/5 [00:00&lt;?, ?it/s]<br>
Loading dataset:  20%|██        | 1/5 [00:05&lt;00:20,  5.20s/it]<br>
Loading dataset:  40%|████      | 2/5 [00:10&lt;00:15,  5.05s/it]<br>
Loading dataset:  60%|██████    | 3/5 [00:13&lt;00:08,  4.37s/it]<br>
Loading dataset:  80%|████████  | 4/5 [00:18&lt;00:04,  4.36s/it]<br>
Loading dataset: 100%|██████████| 5/5 [00:23&lt;00:00,  4.62s/it]<br>
Loading dataset: 100%|██████████| 5/5 [00:23&lt;00:00,  4.63s/it]<br>
[2023-07-13 08:53:29,092] [24408] [MainThread] [INFO] (monailabel.tasks.train.basic_train:227) - 0 - Records for Training: 5<br>
[2023-07-13 08:53:29,098] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:697) - Engine run resuming from iteration 0, epoch 0 until 50 epochs<br>
[2023-07-13 08:53:30,700] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:138) - Restored all variables from /home/dellxpsazdelta/radiology_psoas_azd/model/deepedit_dynunet/train_01/model.pt<br>
[2023-07-13 08:53:38,945] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:269) - Epoch: 1/50, Iter: 1/5 – train_loss: 0.8791<br>
2023-07-13 08:53:40,341 - INFO - Number of simulated clicks: 11<br>
[2023-07-13 08:53:41,639] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:269) - Epoch: 1/50, Iter: 2/5 – train_loss: 0.8105<br>
[2023-07-13 08:53:42,155] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:269) - Epoch: 1/50, Iter: 3/5 – train_loss: 0.8015<br>
[2023-07-13 08:53:42,632] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:269) - Epoch: 1/50, Iter: 4/5 – train_loss: 0.8339<br>
2023-07-13 08:53:45,352 - INFO - Number of simulated clicks: 9<br>
[2023-07-13 08:53:46,177] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:269) - Epoch: 1/50, Iter: 5/5 – train_loss: 0.8071<br>
[2023-07-13 08:53:46,433] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:265) - Got new best metric of train_dice: 0.678305447101593<br>
[2023-07-13 08:53:46,434] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:85) - Current learning rate: 0.0001<br>
[2023-07-13 08:53:46,434] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:199) - Epoch[1] Metrics – left psoas_dice: 0.7228 right psoas_dice: 0.6338 train_dice: 0.6783<br>
[2023-07-13 08:53:46,434] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:209) - Key metric: train_dice best value: 0.678305447101593 at epoch: 1<br>
[2023-07-13 08:53:46,435] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:697) - Engine run resuming from iteration 0, epoch 0 until 1 epochs<br>
2023-07-13 08:53:48,278 - INFO - Number of simulated clicks: 10<br>
[2023-07-13 08:53:49,005] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:265) - Got new best metric of val_mean_dice: 0.6918515563011169<br>
[2023-07-13 08:53:49,005] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:199) - Epoch[1] Metrics – left psoas_dice: 0.7021 right psoas_dice: 0.6816 val_mean_dice: 0.6919<br>
[2023-07-13 08:53:49,005] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:209) - Key metric: val_mean_dice best value: 0.6918515563011169 at epoch: 1<br>
[2023-07-13 08:53:51,338] [24408] [MainThread] [INFO] (monailabel.tasks.train.handler:86) - New Model published: /home/dellxpsazdelta/radiology_psoas_azd/model/deepedit_dynunet/train_01/model.pt =&gt; /home/dellxpsazdelta/radiology_psoas_azd/model/deepedit_dynunet.pt<br>
[2023-07-13 08:53:51,339] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:765) - Epoch[1] Complete. Time taken: 00:00:05<br>
[2023-07-13 08:53:51,339] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:778) - Engine run complete. Time taken: 00:00:05<br>
[2023-07-13 08:53:52,354] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:765) - Epoch[1] Complete. Time taken: 00:00:22<br>
2023-07-13 08:53:54,353 - INFO - Number of simulated clicks: 3<br>
[2023-07-13 08:53:55,735] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:269) - Epoch: 2/50, Iter: 1/5 – train_loss: 0.7936<br>
[2023-07-13 08:53:56,209] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:269) - Epoch: 2/50, Iter: 2/5 – train_loss: 0.8046<br>
2023-07-13 08:53:57,274 - INFO - Number of simulated clicks: 8<br>
[2023-07-13 08:53:58,583] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:269) - Epoch: 2/50, Iter: 3/5 – train_loss: 0.7968<br>
[2023-07-13 08:53:59,060] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:269) - Epoch: 2/50, Iter: 4/5 – train_loss: 0.8337<br>
[2023-07-13 08:53:59,851] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:269) - Epoch: 2/50, Iter: 5/5 – train_loss: 0.8011<br>
[2023-07-13 08:53:59,853] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:265) - Got new best metric of train_dice: 0.8020626306533813<br>
[2023-07-13 08:53:59,853] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:85) - Current learning rate: 0.0001<br>
[2023-07-13 08:53:59,853] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:199) - Epoch[2] Metrics – left psoas_dice: 0.7723 right psoas_dice: 0.8318 train_dice: 0.8021<br>
[2023-07-13 08:53:59,853] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:209) - Key metric: train_dice best value: 0.8020626306533813 at epoch: 2<br>
[2023-07-13 08:53:59,854] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:697) - Engine run resuming from iteration 0, epoch 1 until 2 epochs<br>
2023-07-13 08:54:01,733 - INFO - Number of simulated clicks: 9<br>
[2023-07-13 08:54:02,684] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:265) - Got new best metric of val_mean_dice: 0.709175705909729<br>
[2023-07-13 08:54:02,685] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:199) - Epoch[2] Metrics – left psoas_dice: 0.7219 right psoas_dice: 0.6965 val_mean_dice: 0.7092<br>
[2023-07-13 08:54:02,685] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:209) - Key metric: val_mean_dice best value: 0.709175705909729 at epoch: 2<br>
[2023-07-13 08:54:05,116] [24408] [MainThread] [INFO] (monailabel.tasks.train.handler:86) - New Model published: /home/dellxpsazdelta/radiology_psoas_azd/model/deepedit_dynunet/train_01/model.pt =&gt; /home/dellxpsazdelta/radiology_psoas_azd/model/deepedit_dynunet.pt<br>
[2023-07-13 08:54:05,116] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:765) - Epoch[2] Complete. Time taken: 00:00:05<br>
[2023-07-13 08:54:05,116] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedEvaluator:778) - Engine run complete. Time taken: 00:00:05<br>
[2023-07-13 08:54:05,418] [24408] [MainThread] [INFO] (ignite.engine.engine.SupervisedTrainer:765) - Epoch[2] Complete. Time taken: 00:00:13<br>
[2023-07-13 08:54:14,842] [26118] [ThreadPoolExecutor-0_0] [INFO] (monailabel.utils.async_tasks.utils:76) - Return code: -9</p>
</blockquote>
<ol start="2">
<li>Exit code 1</li>
</ol>
<blockquote>
<p>[2023-07-13 12:20:04,630] [23149] [MainThread] [INFO] (monailabel.utils.async_tasks.task:36) - Train request: {‘model’: ‘deepedit’, ‘name’: ‘train_01’, ‘pretrained’: 1, ‘device’: ‘cuda’, ‘max_epochs’: 50, ‘early_stop_patience’: -1, ‘val_split’: 0.2, ‘train_batch_size’: 1, ‘val_batch_size’: 1, ‘multi_gpu’: True, ‘gpus’: ‘all’, ‘dataset’: ‘CacheDataset’, ‘dataloader’: ‘ThreadDataLoader’, ‘client_id’: ‘user-xyz’}<br>
[2023-07-13 12:20:04,632] [23149] [ThreadPoolExecutor-0_0] [INFO] (monailabel.utils.async_tasks.utils:58) - COMMAND:: /opt/conda/bin/python -m monailabel.interfaces.utils.app -m train -r {“model”:“deepedit”,“name”:“train_01”,“pretrained”:1,“device”:“cuda”,“max_epochs”:50,“early_stop_patience”:-1,“val_split”:0.2,“train_batch_size”:1,“val_batch_size”:1,“multi_gpu”:true,“gpus”:“all”,“dataset”:“CacheDataset”,“dataloader”:“ThreadDataLoader”,“client_id”:“user-xyz”}<br>
[2023-07-13 12:20:05,144] [5998] [MainThread] [INFO] (<strong>main</strong>:38) - Initializing App from: /home/dellxpsazdelta/radiology_psoas_azd; studies: /home/dellxpsazdelta/psoas-azd-images/train-images; conf: {‘models’: ‘deepedit’}<br>
[2023-07-13 12:20:30,698] [5998] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for MONAILabelApp Found: &lt;class ‘main.MyApp’&gt;<br>
[2023-07-13 12:20:30,748] [5998] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.segmentation.Segmentation’&gt;<br>
[2023-07-13 12:20:30,749] [5998] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.deepgrow_3d.Deepgrow3D’&gt;<br>
[2023-07-13 12:20:30,770] [5998] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.deepedit.DeepEdit’&gt;<br>
[2023-07-13 12:20:30,771] [5998] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.segmentation_spleen.SegmentationSpleen’&gt;<br>
[2023-07-13 12:20:30,772] [5998] [MainThread] [INFO] (monailabel.utils.others.class_utils:36) - Subclass for TaskConfig Found: &lt;class ‘lib.configs.deepgrow_2d.Deepgrow2D’&gt;<br>
[2023-07-13 12:20:30,773] [5998] [MainThread] [INFO] (main:83) - +++ Adding Model: deepedit =&gt; lib.configs.deepedit.DeepEdit<br>
[2023-07-13 12:20:32,241] [5998] [MainThread] [INFO] (lib.configs.deepedit:145) - EPISTEMIC Enabled: 0; Samples: 5<br>
[2023-07-13 12:20:32,241] [5998] [MainThread] [INFO] (lib.configs.deepedit:149) - TTA Enabled: 0; Samples: 5<br>
[2023-07-13 12:20:32,241] [5998] [MainThread] [INFO] (main:87) - +++ Using Models: [‘deepedit’]<br>
[2023-07-13 12:20:32,241] [5998] [MainThread] [INFO] (monailabel.interfaces.app:126) - Init Datastore for: /home/dellxpsazdelta/psoas-azd-images/train-images<br>
[2023-07-13 12:20:32,242] [5998] [MainThread] [INFO] (monailabel.datastore.local:125) - Auto Reload: False; Extensions: [‘<em>.nii.gz’, '</em>.nii’, ‘<em>.nrrd’, '</em>.jpg’, ‘<em>.png’, '</em>.tif’, ‘<em>.svs’, '</em>.xml’]<br>
[2023-07-13 12:20:32,300] [5998] [MainThread] [INFO] (monailabel.datastore.local:540) - Invalidate count: 0<br>
[2023-07-13 12:20:32,300] [5998] [MainThread] [INFO] (main:112) - +++ Adding Inferer:: deepedit =&gt; &lt;lib.infers.deepedit.DeepEdit object at 0x7f395c5280d0&gt;<br>
[2023-07-13 12:20:32,300] [5998] [MainThread] [INFO] (main:112) - +++ Adding Inferer:: deepedit_seg =&gt; &lt;lib.infers.deepedit.DeepEdit object at 0x7f395c12b990&gt;<br>
[2023-07-13 12:20:32,301] [5998] [MainThread] [INFO] (main:161) - +++ Adding Trainer:: deepedit =&gt; &lt;lib.trainers.deepedit.DeepEdit object at 0x7f395c12b7d0&gt;<br>
[2023-07-13 12:20:32,301] [5998] [MainThread] [INFO] (monailabel.utils.sessions:51) - Session Path: /home/dellxpsazdelta/.cache/monailabel/sessions<br>
[2023-07-13 12:20:32,301] [5998] [MainThread] [INFO] (monailabel.utils.sessions:52) - Session Expiry (max): 3600<br>
[2023-07-13 12:20:32,301] [5998] [MainThread] [INFO] (monailabel.tasks.train.basic_train:353) - Train Request (input): {‘model’: ‘deepedit’, ‘name’: ‘train_01’, ‘pretrained’: 1, ‘device’: ‘cuda’, ‘max_epochs’: 50, ‘early_stop_patience’: -1, ‘val_split’: 0.2, ‘train_batch_size’: 1, ‘val_batch_size’: 1, ‘multi_gpu’: True, ‘gpus’: ‘all’, ‘dataset’: ‘CacheDataset’, ‘dataloader’: ‘ThreadDataLoader’, ‘client_id’: ‘user-xyz’, ‘local_rank’: 0}<br>
[2023-07-13 12:20:32,301] [5998] [MainThread] [INFO] (monailabel.tasks.train.basic_train:363) - CUDA_VISIBLE_DEVICES: None<br>
[2023-07-13 12:20:32,302] [5998] [MainThread] [INFO] (monailabel.tasks.train.basic_train:368) - Distributed/Multi GPU is limited<br>
[2023-07-13 12:20:32,302] [5998] [MainThread] [INFO] (monailabel.tasks.train.basic_train:381) - Distributed Training = FALSE<br>
[2023-07-13 12:20:32,302] [5998] [MainThread] [INFO] (monailabel.tasks.train.basic_train:408) - 0 - Train Request (final): {‘name’: ‘train_01’, ‘pretrained’: 1, ‘device’: ‘cuda’, ‘max_epochs’: 50, ‘early_stop_patience’: -1, ‘val_split’: 0.2, ‘train_batch_size’: 1, ‘val_batch_size’: 1, ‘multi_gpu’: False, ‘gpus’: ‘all’, ‘dataset’: ‘CacheDataset’, ‘dataloader’: ‘ThreadDataLoader’, ‘model’: ‘deepedit’, ‘client_id’: ‘user-xyz’, ‘local_rank’: 0, ‘run_id’: ‘20230713_1220’}<br>
[2023-07-13 12:20:32,302] [5998] [MainThread] [INFO] (monailabel.tasks.train.basic_train:504) - 0 - Using Device: cuda; IDX: None<br>
[2023-07-13 12:20:32,303] [5998] [MainThread] [INFO] (monailabel.tasks.train.basic_train:331) - Total Records for Training: 7<br>
[2023-07-13 12:20:32,303] [5998] [MainThread] [INFO] (monailabel.tasks.train.basic_train:332) - Total Records for Validation: 2<br>
Loading dataset:   0%|          | 0/2 [00:00&lt;?, ?it/s]<br>
Loading dataset:  50%|█████     | 1/2 [00:09&lt;00:09,  9.83s/it]<br>
Loading dataset: 100%|██████████| 2/2 [00:13&lt;00:00,  6.29s/it]<br>
Loading dataset: 100%|██████████| 2/2 [00:13&lt;00:00,  6.82s/it]<br>
[2023-07-13 12:21:44,249] [5998] [MainThread] [INFO] (monailabel.tasks.train.basic_train:275) - 0 - Records for Validation: 2<br>
[2023-07-13 12:21:44,258] [5998] [MainThread] [INFO] (monailabel.tasks.train.basic_train:265) - 0 - Adding Validation to run every ‘1’ interval<br>
[2023-07-13 12:21:44,258] [5998] [MainThread] [INFO] (monailabel.tasks.train.basic_train:591) - 0 - Load Path /home/dellxpsazdelta/radiology_psoas_azd/model/deepedit_dynunet/train_01/model.pt<br>
Loading dataset:   0%|          | 0/7 [00:00&lt;?, ?it/s]<br>
Loading dataset:  14%|█▍        | 1/7 [00:04&lt;00:25,  4.25s/it]<br>
Loading dataset:  29%|██▊       | 2/7 [00:08&lt;00:21,  4.35s/it]<br>
Loading dataset:  43%|████▎     | 3/7 [00:12&lt;00:16,  4.16s/it]<br>
Loading dataset:  57%|█████▋    | 4/7 [00:16&lt;00:11,  3.93s/it]<br>
Loading dataset:  71%|███████▏  | 5/7 [00:25&lt;00:11,  5.88s/it]<br>
Loading dataset:  71%|███████▏  | 5/7 [00:29&lt;00:11,  5.87s/it]<br>
Traceback (most recent call last):<br>
File “/opt/conda/lib/python3.7/site-packages/monai/transforms/transform.py”, line 89, in apply_transform<br>
return _apply_transform(transform, data, unpack_items)<br>
File “/opt/conda/lib/python3.7/site-packages/monai/transforms/transform.py”, line 53, in _apply_transform<br>
return transform(parameters)<br>
File “/opt/conda/lib/python3.7/site-packages/monai/apps/deepedit/transforms.py”, line 99, in <strong>call</strong><br>
label = np.zeros(d[key].shape)<br>
numpy.core._exceptions.MemoryError: Unable to allocate 502. MiB for an array with shape (512, 512, 251) and data type float64<br>
The above exception was the direct cause of the following exception:<br>
Traceback (most recent call last):<br>
File “/opt/conda/lib/python3.7/runpy.py”, line 193, in _run_module_as_main<br>
“<strong>main</strong>”, mod_spec)<br>
File “/opt/conda/lib/python3.7/runpy.py”, line 85, in _run_code<br>
exec(code, run_globals)<br>
File “/opt/conda/lib/python3.7/site-packages/monailabel/interfaces/utils/app.py”, line 132, in <br>
run_main()<br>
File “/opt/conda/lib/python3.7/site-packages/monailabel/interfaces/utils/app.py”, line 117, in run_main<br>
result = a.train(request)<br>
File “/opt/conda/lib/python3.7/site-packages/monailabel/interfaces/app.py”, line 380, in train<br>
result = task(request, self.datastore())<br>
File “/opt/conda/lib/python3.7/site-packages/monailabel/tasks/train/basic_train.py”, line 382, in <strong>call</strong><br>
res = self.train(0, world_size, req, datalist)<br>
File “/opt/conda/lib/python3.7/site-packages/monailabel/tasks/train/basic_train.py”, line 428, in train<br>
context.trainer = self._create_trainer(context)<br>
File “/opt/conda/lib/python3.7/site-packages/monailabel/tasks/train/basic_train.py”, line 575, in _create_trainer<br>
train_data_loader=self.train_data_loader(context),<br>
File “/opt/conda/lib/python3.7/site-packages/monailabel/tasks/train/basic_train.py”, line 226, in train_data_loader<br>
dataset, datalist = self._dataset(context, context.train_datalist)<br>
File “/opt/conda/lib/python3.7/site-packages/monailabel/tasks/train/basic_train.py”, line 200, in _dataset<br>
if context.dataset_type == “CacheDataset”<br>
File “/opt/conda/lib/python3.7/site-packages/monai/data/dataset.py”, line 723, in <strong>init</strong><br>
self.set_data(data)<br>
File “/opt/conda/lib/python3.7/site-packages/monai/data/dataset.py”, line 748, in set_data<br>
self._cache = _compute_cache()<br>
File “/opt/conda/lib/python3.7/site-packages/monai/data/dataset.py”, line 737, in _compute_cache<br>
return self._fill_cache()<br>
File “/opt/conda/lib/python3.7/site-packages/monai/data/dataset.py”, line 761, in _fill_cache<br>
desc=“Loading dataset”,<br>
File “/opt/conda/lib/python3.7/site-packages/tqdm/std.py”, line 1195, in <strong>iter</strong><br>
for obj in iterable:<br>
File “/opt/conda/lib/python3.7/multiprocessing/pool.py”, line 748, in next<br>
raise value<br>
File “/opt/conda/lib/python3.7/multiprocessing/pool.py”, line 121, in worker<br>
result = (True, func(*args, **kwds))<br>
File “/opt/conda/lib/python3.7/site-packages/monai/data/dataset.py”, line 777, in _load_cache_item<br>
item = apply_transform(_xform, item)<br>
File “/opt/conda/lib/python3.7/site-packages/monai/transforms/transform.py”, line 113, in apply_transform<br>
raise RuntimeError(f"applying transform {transform}") from e<br>
RuntimeError: applying transform &lt;monai.apps.deepedit.transforms.NormalizeLabelsInDatasetd object at 0x7f393a2fdfd0&gt;<br>
[2023-07-13 12:22:24,359] [23149] [ThreadPoolExecutor-0_0] [INFO] (monailabel.utils.async_tasks.utils:76) - Return code: 1</p>
</blockquote>
<p>It seems weird to me that without changing anything (such as adding new labels), the training suddenly starts to systematically fail while it was working fine before.<br>
Does anyone have any clue as to why these errors occur?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @rbumm (2023-07-14 06:36 UTC)

<p>It is probably better to open an issue on <a href="https://github.com/Project-MONAI/MONAILabel">MonaiLabel Github</a> or maybe <a class="mention" href="/u/diazandr3s">@diazandr3s</a> can comment.</p>

---

## Post #3 by @lukasvanderstricht (2023-07-14 06:46 UTC)

<p>Okay, I will open an issue there, thank you!</p>

---

## Post #4 by @diazandr3s (2023-07-14 09:07 UTC)

<p>Many thanks for the ping, <a class="mention" href="/u/rbumm">@rbumm</a>.<br>
I will comment on the issue opened by <a class="mention" href="/u/lukasvanderstricht">@lukasvanderstricht</a> in the MONAI Label repo: <a href="https://github.com/Project-MONAI/MONAILabel/issues/1489" class="inline-onebox" rel="noopener nofollow ugc">Error while training with MONAILabel's deepedit · Issue #1489 · Project-MONAI/MONAILabel · GitHub</a></p>

---

## Post #5 by @rbumm (2023-07-14 10:56 UTC)

<p>Would be great <a class="mention" href="/u/lukasvanderstricht">@lukasvanderstricht</a> if you could in the end add a short comment here if you were able to solve the problem - and how.</p>

---

## Post #6 by @lukasvanderstricht (2023-07-14 11:05 UTC)

<p>This problem can be solved by switching from CacheDataset to Dataset in the Slicer MONAILabel GUI. This however entails that the training process will go slower. For the full discussion, I refer to <a href="https://github.com/Project-MONAI/MONAILabel/issues/1489" class="inline-onebox" rel="noopener nofollow ugc">Error while training with MONAILabel's deepedit · Issue #1489 · Project-MONAI/MONAILabel · GitHub</a>.</p>

---
