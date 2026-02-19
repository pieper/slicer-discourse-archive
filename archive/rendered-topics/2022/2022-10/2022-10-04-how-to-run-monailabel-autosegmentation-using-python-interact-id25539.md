---
topic_id: 25539
title: "How To Run Monailabel Autosegmentation Using Python Interact"
date: 2022-10-04
url: https://discourse.slicer.org/t/25539
---

# How to run monailabel autosegmentation using python interactor

**Topic ID**: 25539
**Date**: 2022-10-04
**URL**: https://discourse.slicer.org/t/how-to-run-monailabel-autosegmentation-using-python-interactor/25539

---

## Post #1 by @hourglassnam (2022-10-04 06:20 UTC)

<p>Dear community,<br>
I am trying to run the monailabel autosegmentation for many samples so I would like to learn how to run infer using the python interactor.<br>
I found <a href="https://github.com/Project-MONAI/MONAILabel/discussions/1004#discussioncomment-3684524" rel="noopener nofollow ugc">this discussion</a> on github answered by wonderful <a class="mention" href="/u/lassoan">@lassoan</a>, informing how logic can be used to run the module on python interactor.</p>
<p>With the <a href="https://github.com/Project-MONAI/MONAILabel/blob/5a7cbd8d5de945a99085d0f6495de21485c47415/plugins/slicer/MONAILabel/MONAILabel.py#L2068-L2167" rel="noopener nofollow ugc">given information</a>, I was able to connect to the server but I could not make the autosegmentation to work.</p>
<p>I guess the infer can be done with following line but I was not able to figure out what image_in is for.<br>
<code>result_file, params = infer(model, image_in)</code></p>
<p>I tried putting my session folder as the image_in address but it did not worked.</p>
<pre><code class="lang-auto">#MONAILABEL
logic = slicer.util.getModuleLogic('MONAILabel')

# connect to server
server_add = "http://127.0.0.1:8000"
logic.setServer(server_url=server_add)

#check if Monailabel is connected correctly
MONAILabelClient = logic.info()
print(MONAILabelClient)

# &lt;FAILED&gt;
# def infer(self, model, image_in, params={}, label_in=None, file=None, session_id=None):
session_image = "C:/Users/username/.cache/monailabel/sessions"
result_file, params = logic.infer("deepedit_seg", image_in = session_image)
</code></pre>
<p>Can somebody kindly explain to me what the image_in is supposed to be?</p>
<p>I am always greatful for all your help and thank you in advance.</p>

---

## Post #3 by @hourglassnam (2022-10-06 08:21 UTC)

<p>I figured it out!!</p>
<p>I got confused what image_in was because I misread <a href="https://docs.monai.io/projects/label/en/latest/apidocs/monailabel.client.client.html" rel="noopener nofollow ugc">this</a> and thought the <em>image_in</em> was supposed to be different from the <em>file</em>.</p>
<blockquote>
<p>infer(<em>model</em>, <em>image_id</em>, <em>params</em>, <em>label_in=None</em>, <em>file=None</em>, <em>session_id=None</em> )<a href="https://docs.monai.io/projects/label/en/latest/_modules/monailabel/client/client.html#MONAILabelClient.infer" rel="noopener nofollow ugc">[source]</a></p>
<p>Run Infer</p>
<p>Parameters</p>
<ul>
<li><strong>model</strong> – Name of Model</li>
<li><strong>image_id</strong> – Image Id</li>
<li><strong>params</strong> – Additional configs/json params as part of Infer request</li>
<li><strong>label_in</strong> – File path for label mask which is needed to run Inference (e.g. In case of Scribbles)</li>
<li><strong>file</strong> – File path for Image (use raw image instead of image_id)</li>
<li><strong>session_id</strong> – Session ID (use existing session id instead of image_id)</li>
</ul>
<p>Returns</p>
<p>response_file (label mask), response_body (json result/output params)</p>
</blockquote>
<p>After all, image_in represented the path to my volume. (Thank you so much <a class="mention" href="/u/rbumm">@rbumm</a>!!)<br>
So something like this would be image_in,</p>
<blockquote>
<p>image_in = “C:/Users/username/Desktop/sampleFile.nrrd”</p>
</blockquote>
<p>Now, if you want your processed volume to be autosegmented, not the original volume, you have to save currently edited volume as a temporary file.</p>
<p>Monailabel does that for you when you use it on Slicer, but you have to do <a href="https://github.com/Project-MONAI/MONAILabel/blob/5a7cbd8d5de945a99085d0f6495de21485c47415/plugins/slicer/MONAILabel/MONAILabel.py#L1302" rel="noopener nofollow ugc">this part</a> manually when using the python interactor.</p>
<p>So, after having the server ready, you can get the server address and do as following.</p>
<pre><code class="lang-auto"># Save currently working scene
import time
import tempfile

def saveVolTemp():
	# Temporary folder path
	tempVolDir = logic.tmpdir
	# Select the volume node you are trying to work with
	volNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
	image_id = volNode.GetName()
	# Absolute path of the temporary volume file
	in_file = tempfile.NamedTemporaryFile(suffix= '.nrrd', dir = tempVolDir).name
	logic.reportProgress(5)
	# save the volume node
	start = time.time()
	slicer.util.saveNode(volNode, in_file)
	logging.info(f"Saved Input Node into {in_file} in {time.time() - start:3.1f}s")
	logic.reportProgress(30)
	return tempVolDir, image_id, in_file

# get MONAILABEL logic
logic = slicer.util.getModuleLogic('MONAILabel')

# connect to server
server_add = "http://127.0.0.1:8000"
logic.setServer(server_url=server_add)

# check if Monailabel is connected correctly
MONAILabelClient = logic.info()
print(MONAILabelClient)

# Save the volume and get the path
tempVolDir, image_id, in_file = saveVolTemp()

# infer
result_file, params = logic.infer("deepedit_seg", in_file)

# load the autosegmented segmentation file onto Slicer
slicer.util.loadSegmentation(result_file)
</code></pre>
<p>I not good at python so please feel free to correct me if there is anything wrong or if this is a hard way aroud.<br>
Thank you always, and I really hope this can help somebody.</p>

---

## Post #4 by @rbumm (2022-10-06 10:12 UTC)

<p>Great, <a class="mention" href="/u/hourglassnam">@hourglassnam</a>, I tested this and it works fine.</p>
<p>Just needed to remove <code>logic.reportProgress</code> calls from saveVolTemp() and make a change for  <code>tempVolDir</code>:</p>
<pre><code class="lang-auto"> # Save currently working scene
import time
import tempfile
def saveVolTemp():
	# Temporary folder path
	tempVolDir = slicer.app.temporaryPath + "/YourProgramName/"
	# Select the volume node you are trying to work with
	volNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
	image_id = volNode.GetName()
	# Absolute path of the temporary volume file
	in_file = tempfile.NamedTemporaryFile(suffix= '.nrrd', dir = tempVolDir).name

	# save the volume node
	start = time.time()
	slicer.util.saveNode(volNode, in_file)
	logging.info(f"Saved Input Node into {in_file} in {time.time() - start:3.1f}s")
	return tempVolDir, image_id, in_file

# get MONAILABEL logic
logic = slicer.util.getModuleLogic('MONAILabel')

# connect to server
server_add = "http://127.0.0.1:8000"
logic.setServer(server_url=server_add)

# check if Monailabel is connected correctly
MONAILabelClient = logic.info()
print(MONAILabelClient)

# Save the volume and get the path
tempVolDir, image_id, in_file = saveVolTemp()

# infer
result_file, params = logic.infer("deepedit_seg", in_file)

# load the autosegmented segmentation file onto Slicer
slicer.util.loadSegmentation(result_file)
</code></pre>

---

## Post #5 by @hourglassnam (2022-10-06 11:42 UTC)

<p>Great!! Thank you so much for checking it:))</p>

---
