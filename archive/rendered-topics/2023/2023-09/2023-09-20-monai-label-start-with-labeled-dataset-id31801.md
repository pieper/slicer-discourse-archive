---
topic_id: 31801
title: "Monai Label Start With Labeled Dataset"
date: 2023-09-20
url: https://discourse.slicer.org/t/31801
---

# Monai Label - Start with Labeled Dataset

**Topic ID**: 31801
**Date**: 2023-09-20
**URL**: https://discourse.slicer.org/t/monai-label-start-with-labeled-dataset/31801

---

## Post #1 by @nasibov_98 (2023-09-20 11:39 UTC)

<p>Hi, I would like to use my own labeled dataset to kickstart monai label training.</p>
<p>Background:<br>
Followed the youtube installation and scribbler tutorial, i was able to download  and view “Task09_Spleen” in 3D slicer using:</p>
<p>monailabel start_server --app apps/radiology --studies datasets/Task09_Spleen/imagesTr --conf models deepedit</p>
<p>Problem:</p>
<p>I have a LABELED dataset “Task013_Abdomen” set up exactly like example “Task09_Spleen”. I want to train a new model to detect liver tumours, liver, and kidney. I want to start the training procedure with existing Task013_abdomen images and labels, and then use the model to iteratively correct and add more segmentations to my model on Slicer 3D.</p>
<p>Specific issues:</p>
<ul>
<li>
<p>Slicer 3D does not see my dataset. error message “no unlabeled images found”. How do I prime it to expect an already labeled dataset for training?</p>
</li>
<li>
<p>What configuration to start monai label server in? I am currently using the following terminal prompt:<br>
monailabel start_server --app apps/radiology --studies<br>
datasets/Task013_Abdomen/imagesTr --conf models segmentation</p>
</li>
<li>
<p>How do I generate the dataset.json and datastore_v2.json that appears in example “Task09_Spleen”. I think this is required for slicer to see my MRI images and their respective labels right?</p>
</li>
</ul>
<p>Any help is appreciated, this is taking me a while to set up correctly.</p>
<p>Cheers,</p>
<p>Ulvi</p>

---

## Post #2 by @Ghazal_Danaei (2024-03-06 17:17 UTC)

<p>Hello,<br>
did you find out why slicer does not see your unlabeled data?</p>

---

## Post #3 by @magedik (2025-10-20 08:10 UTC)

<p>Hi. I have the same exact problem. What i did wrong or what is the solution? Any help is appreciated.</p>

---
