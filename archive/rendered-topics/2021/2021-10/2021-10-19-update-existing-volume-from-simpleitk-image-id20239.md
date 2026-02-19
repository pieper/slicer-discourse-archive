---
topic_id: 20239
title: "Update Existing Volume From Simpleitk Image"
date: 2021-10-19
url: https://discourse.slicer.org/t/20239
---

# Update existing volume from SimpleITK image

**Topic ID**: 20239
**Date**: 2021-10-19
**URL**: https://discourse.slicer.org/t/update-existing-volume-from-simpleitk-image/20239

---

## Post #1 by @Karthik (2021-10-19 10:07 UTC)

<p>Thank you simonoxen. It worked for me.<br>
I need guidance with one other issue. I use the method sitkUtils.PushVolumeToSlicer each time I want to display a volume node on screen. I have a button and whenever this button is clicked, some operation is performed internally and the resulting volume is pushed to screen with the name ‘XYZ’. In general, I keep varying the parameters and clicking the button multiple times in order to get the right output. But, this creates multiple nodes all named ‘XYZ’.</p>
<p>Is there any way to overwrite or delete the previous node named ‘XYZ’ before creating the new one. That way I won’t get confused with the names of the nodes while saving.</p>

---

## Post #2 by @simonoxen (2021-10-19 11:26 UTC)

<p>You can specify to which node the volume is pushed. If you specify an existing node you can overwrite it. See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#running-an-itk-filter-in-python-using-simpleitk" rel="noopener nofollow ugc">script repository: simple itk</a></p>

---
