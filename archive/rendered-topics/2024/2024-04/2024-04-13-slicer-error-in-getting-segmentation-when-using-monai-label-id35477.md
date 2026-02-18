# Slicer error in getting segmentation when using monai label

**Topic ID**: 35477
**Date**: 2024-04-13
**URL**: https://discourse.slicer.org/t/slicer-error-in-getting-segmentation-when-using-monai-label/35477

---

## Post #1 by @Sheng-xc (2024-04-13 15:43 UTC)

<p>Hi,</p>
<p>I am working with Slicer5.6.2 and MONAILabel on my mac, using port forwarding  from a Ubuntu server.<br>
The connection, server log, and client interface seem pretty good, but a slicer error raises everytime I try to get a result. No matter I use the function autoseg or scribble annotation, the last line in details of the error will always be:<br>
"ERROR: Unable to determine ImageIO writer for “slicer:…<span class="hashtag-raw">#vtkMRMLLabelMapVolumeNode</span>…”<br>
The problem persists whether I was running the exemplary app or a custom app.</p>
<p>Server log:</p>
<blockquote>
<p>Blockquote</p>
</blockquote>
<pre><code class="lang-auto">[2024-04-13 13:11:30,113] [87952] [MainThread] [INFO] (monailabel.interfaces.utils.transform:77) - POST - Input Keys: ['device', 'model', 'image', 'result_extension', 'result_dtype', 'client_id', 'description', 'image_path', 'image_meta_dict', 'latencies', 'pred']
[2024-04-13 13:11:30,120] [87952] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (EnsureTyped): Time: 0.0008; image: torch.Size([9, 128, 128, 128])(torch.float32); pred: torch.Size([8, 512, 512, 90])(torch.float32)
[2024-04-13 13:11:30,145] [87952] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (Activationsd): Time: 0.0228; image: torch.Size([9, 128, 128, 128])(torch.float32); pred: torch.Size([8, 512, 512, 90])(torch.float32)
[2024-04-13 13:11:30,161] [87952] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (AsDiscreted): Time: 0.0142; image: torch.Size([9, 128, 128, 128])(torch.float32); pred: torch.Size([1, 512, 512, 90])(torch.float32)
[2024-04-13 13:11:30,165] [87952] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (SqueezeDimd): Time: 0.0016; image: torch.Size([9, 128, 128, 128])(torch.float32); pred: torch.Size([512, 512, 90])(torch.float32)
[2024-04-13 13:11:30,594] [87952] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (ToNumpyd): Time: 0.4269; image: torch.Size([9, 128, 128, 128])(torch.float32); pred: (512, 512, 90)(float32)
[2024-04-13 13:11:30,596] [87952] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (Restored): Time: 0.0007; image: torch.Size([9, 128, 128, 128])(torch.float32); pred: (512, 512, 90)(float32)
[2024-04-13 13:11:57,518] [87952] [MainThread] [INFO] (monailabel.interfaces.utils.transform:122) - POST - Transform (GetCentroidsd): Time: 26.9163; image: torch.Size([9, 128, 128, 128])(torch.float32); pred: (512, 512, 90)(float32)
[2024-04-13 13:11:57,522] [87952] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:604) - Writing Result...
[2024-04-13 13:11:57,532] [87952] [MainThread] [INFO] (monailabel.transform.writer:196) - Result ext: .nrrd; write_to_file: True; dtype: uint8
[2024-04-13 13:11:59,297] [87952] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:335) - ++ Latencies =&gt; Total: 41.1608; Pre: 11.5325; Inferer: 0.3257; Invert: 0.1006; Post: 27.4148; Write: 1.7746
[2024-04-13 13:11:59,299] [87952] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:370) - Result File: /tmp/tmp6mf0gp4b.nrrd
[2024-04-13 13:11:59,300] [87952] [MainThread] [INFO] (monailabel.tasks.infer.basic_infer:371) - Result Json Keys: ['label_names', 'latencies', 'centroids']
</code></pre>
<p>Slicer error:<br>
When using autoseg —— Failed to run inference in MONAI Label Server.<br>
When using scribble —— Failed to post process label on MONAI Label Sever using Histogram+GraphCut.<br>
Details of the error using autoseg:</p>
<blockquote>
<p>Blockquote</p>
</blockquote>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/Applications/Slicer.app/Contents/Extensions-32448/MONAILabel/lib/Slicer-5.6/qt-scripted-modules/MONAILabel.py", line 1553, in onClickSegmentation
    self.updateSegmentationMask(result_file, labels)
  File "/Applications/Slicer.app/Contents/Extensions-32448/MONAILabel/lib/Slicer-5.6/qt-scripted-modules/MONAILabel.py", line 1755, in updateSegmentationMask
    labelmapVolumeNode = sitkUtils.PushVolumeToSlicer(labelImage, None, className="vtkMRMLLabelMapVolumeNode")
  File "/Applications/Slicer.app/Contents/bin/Python/sitkUtils.py", line 25, in PushVolumeToSlicer
    sitk.WriteImage(sitkimage, myNodeFullITKAddress)
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/SimpleITK/extra.py", line 425, in WriteImage
    return writer.Execute(image)
  File "/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/SimpleITK/SimpleITK.py", line 7907, in Execute
    return _SimpleITK.ImageFileWriter_Execute(self, *args)
RuntimeError: Exception thrown in SimpleITK ImageFileWriter_Execute: /Users/runner/work/1/sitk/Code/IO/src/sitkImageFileWriter.cxx:206:
sitk::ERROR: Unable to determine ImageIO writer for "slicer:0x7fabb9c9c2e0#vtkMRMLLabelMapVolumeNode3"
</code></pre>
<p>Is there anyway I can fix the problem? Thanks in advance.</p>

---

## Post #2 by @lassoan (2024-04-13 15:44 UTC)

<p>It seems that one of the extensions that you installed replaced SimpleITK package that is bundled with Slicer. To restore SimpleITK, you can reinstall Slicer into a new folder and avoid the extension that replaced SimpleITK.</p>

---

## Post #3 by @Sheng-xc (2024-04-14 04:29 UTC)

<p>Thank you for the prompt reply! It worked!</p>

---

## Post #4 by @lassoan (2024-04-14 15:49 UTC)

<p>Do you know which extension was the culprit?</p>

---

## Post #5 by @Xiaojie_Guo (2025-10-24 02:39 UTC)

<blockquote>
<p>If the SimpleITK package that is bundled with Slicer has been replaced by some extensions, is it possible to reinstall this specified SimpleITK? Because I have installed many extensions. It seems that this SimpleITK package has sitkUtils.py file and registered Slicer image IO.  Can I copy sitkUtils.py to the Slicer folder and register Slicer image IO with some codes?</p>
</blockquote>

---
