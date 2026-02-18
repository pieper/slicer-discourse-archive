# MONAILabel module should allow user to select different volumes in current scene

**Topic ID**: 28522
**Date**: 2023-03-22
**URL**: https://discourse.slicer.org/t/monailabel-module-should-allow-user-to-select-different-volumes-in-current-scene/28522

---

## Post #1 by @slicer365 (2023-03-22 14:33 UTC)

<p>this selector bar is gray.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4998210ef3d345646383d793788f90620b76e80.png" data-download-href="/uploads/short-url/wChKFIkx2J2GVC7GCERQJGAB6dG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4998210ef3d345646383d793788f90620b76e80_2_517x297.png" alt="image" data-base62-sha1="wChKFIkx2J2GVC7GCERQJGAB6dG" width="517" height="297" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4998210ef3d345646383d793788f90620b76e80_2_517x297.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4998210ef3d345646383d793788f90620b76e80_2_775x445.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/4/e4998210ef3d345646383d793788f90620b76e80_2_1034x594.png 2x" data-dominant-color="A4A3A2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1441×830 247 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-03-22 16:26 UTC)

<p>This is probably intentional. You can submit a feature request to <a href="https://github.com/Project-MONAI/MONAILabel/" class="inline-onebox">GitHub - Project-MONAI/MONAILabel: MONAI Label is an intelligent open source image labeling and learning tool.</a> to discuss this with the developers of the extension.</p>

---

## Post #3 by @rbumm (2023-03-23 08:05 UTC)

<p>This seems to be normal behavior, if you start your MONAILabel server and press “Next Sample” in the MONAILabel extension, the “Source Volume” will be automatically set, but remain greyed out.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf6b2817530af5595de1fb6a7e0f2cc7efc099d1.png" data-download-href="/uploads/short-url/rjmMhNPggQrWSosJUhdsh4fYACZ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf6b2817530af5595de1fb6a7e0f2cc7efc099d1_2_690x311.png" alt="image" data-base62-sha1="rjmMhNPggQrWSosJUhdsh4fYACZ" width="690" height="311" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf6b2817530af5595de1fb6a7e0f2cc7efc099d1_2_690x311.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bf6b2817530af5595de1fb6a7e0f2cc7efc099d1_2_1035x466.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf6b2817530af5595de1fb6a7e0f2cc7efc099d1.png 2x" data-dominant-color="989694"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1246×563 157 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @rbumm (2023-03-23 08:31 UTC)

<p>The MONAILabel extension accepts that you open a different volume in 3D Slicer, run inference (“Autosegmentation → Run”), optimize the labels via the integrated “Segment editor”, then “Submit Label” to the MONAILabel server.</p>

---

## Post #5 by @slicer365 (2023-03-23 14:43 UTC)

<p>for example, I am training the model ,I fond the accuracy is very good ,now I want to use a new volume to test the model ,then how to do?</p>
<p>One way is to finish training all the data of datasets. I will continue clicking next sample until the last one.</p>
<p>In fact ,the source volume means the current volume that I want to process .if I want to use the pretrained model to segment my data anytime,how to do ?</p>

---

## Post #6 by @pieper (2023-03-23 14:47 UTC)

<p>In my experience what you do is close the scene, load a new volume, and then it becomes the selected target for running the inference.</p>

---

## Post #7 by @slicer365 (2023-03-23 14:55 UTC)

<p>Yes ,right! But this is not convenient，and I can only load a volume into the scene, I want to load different volumes into the scene.</p>
<p>for example, I have many volumes ,I want to label them one by one and submit the volume with label . I can chose different volumes in source volume bar. The button next sample can just help load data from datasets.</p>

---

## Post #8 by @rbumm (2023-03-23 17:38 UTC)

<p>You probably will need to do some data preparation and bring the files exactly into the data file structure that MONAILabell uses, then connect MONAILabel server to your own dataset.<br>
Call your volumes by “Next sample”, label 4-5 volumes this way, “Submit label” each time, then train.<br>
Depending on your purpose, the “segmentation” model is probably better than “deepedit”.</p>

---

## Post #9 by @lassoan (2023-03-24 04:28 UTC)

<p><a class="mention" href="/u/slicer365">@slicer365</a> Do you feel that the model works well already and so instead of training you just want to use it conveniently for segmenting your images?</p>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/rbumm">@rbumm</a> What is the recommended method for deploying models trained by MONAILabel? Creating a MONAI bundle? Should we create a Segment Editor effect that can run MONAI bundles locally? Is there an inference server for MONAI bundles?</p>

---

## Post #10 by @slicer365 (2023-03-24 04:45 UTC)

<p>I have some brain hemorrhage CT data, I want to segment the hematoma, then I used the pre-training model of spleen, I just use 4 sets of data to modify and submit the label, and then train it, the result is amazing, it performs very well.</p>

---

## Post #11 by @rbumm (2023-03-24 09:01 UTC)

<p>The segment editor effect is an interesting idea! I am not aware of a public inference server, but maybe bundles are already part of the MONAI Model Zoo, <a class="mention" href="/u/diazandr3s">@diazandr3s</a> could you comment?</p>
<p>Here is how inference can be made with a running MONAILabel Server, specifying a trained model (tested code):</p>
<pre><code class="lang-auto">logic = slicer.util.getModuleLogic('MONAILabel')
# connect to server
try:
    #check if Monailabel is connected correctly
    server_add = "http://127.0.0.1:8000"
    logic.setServer(server_url=server_add)
    MONAILabelClient = logic.info()
except Exception as e:
    slicer.util.errorDisplay("Unable to connect to MONAILabel server on http://127.0.0.1:8000"+str(e))
    import traceback
    traceback.print_exc()
else:
    # save the volume and get the path
    # inputVolume is a previously generated scalar volume
    tempVolDir, image_id, in_file = self.saveVolTemp(inputVolume)
    model = "segmentation"
    params = {'largest_cc': True}
    # make inference
    result_file, params = logic.infer(model, in_file, params)
    # load the segmentation file in Slicer
    tempResultSegmentation = slicer.util.loadSegmentation(result_file)
</code></pre>
<p>The model is a *.pt file that can be found in the MONAILabel app directory (Windows example):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3432449d6c6921c5cc836781b1a56971f4136bf3.png" data-download-href="/uploads/short-url/7rKwGC1s4bDlcI0vZxZ953mxbgL.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/3432449d6c6921c5cc836781b1a56971f4136bf3.png" alt="image" data-base62-sha1="7rKwGC1s4bDlcI0vZxZ953mxbgL" width="690" height="249" data-dominant-color="FAFAFA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">822×297 11.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @rbumm (2023-03-24 09:09 UTC)

<p>Here is what ChatGPT suggests to make inferences with a trained MONAILabel model and using Pytorch (untested code):</p>
<pre><code class="lang-auto">import torch
import monai

# Load the saved model from MONAILabel
model_path = "path/to/saved/model"
model = torch.load(model_path)

# Set the model to evaluation mode
model.eval()

# Load the image data you want to make predictions on
image_path = "path/to/image"
image = monai.utils.load_nifti(image_path)[0]

# Convert the image to a PyTorch tensor
image_tensor = torch.tensor(image)

# Make predictions using the model
with torch.no_grad():
    predictions = model(image_tensor)

# Process the predictions as needed
# ...

# Save the output to a file
output_path = "path/to/output"
monai.utils.save_nifti(output_path, predictions)

</code></pre>

---

## Post #13 by @diazandr3s (2023-03-24 13:20 UTC)

<p>This is amazing, <a class="mention" href="/u/rbumm">@rbumm</a></p>

---

## Post #14 by @diazandr3s (2023-03-24 13:33 UTC)

<p>Hi <a class="mention" href="/u/slicer365">@slicer365</a>,</p>
<p>Thanks for posting these questions/comments.</p>
<p>Just to clarify, you could fetch the Next Sample even if training is happening. No need to stop the training process. You could also run inference and training if you have enough GPU memory to do it.</p>
<p>If you want to run batch inference on more than one volume, you could run MONAI Label without starting it as a server. For this, just update the folder here (<a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/main.py#L286" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/main.py at main · Project-MONAI/MONAILabel · GitHub</a>), model name here (<a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/main.py#L290" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel/main.py at main · Project-MONAI/MONAILabel · GitHub</a> - it should be “segmentation” or “deepedit” depending on the model you’re using) and then run the main file within the docker or virtual env like a standard python script: python main.py</p>
<p>This will run inference on all the unlabelled volumes.</p>
<p>For other users, here is a similar discussion: <a href="https://github.com/Project-MONAI/MONAILabel/discussions/1354" class="inline-onebox" rel="noopener nofollow ugc">MONAILabel module should allow user to select different volumes in current scene · Project-MONAI/MONAILabel · Discussion #1354 · GitHub</a></p>
<p>Hope this helps</p>

---

## Post #15 by @rbumm (2023-03-24 14:11 UTC)

<p>The above, ChatGPT suggested code seems to be based on a previous version of MONAI and is not working.</p>
<p><a class="mention" href="/u/diazandr3s">@diazandr3s</a> how would you suggest loading a trained MONAILabel model (*.pt) in Python directly if you just want to create inference on a given scalar volume and not start a server? I see it is party answered in your previous post, but is there an easy elegant solution?</p>
<p>If we succeed in establishing such a mechanism in a 3D Slicers Segment Editor effect we could probably make MONAILabel models or other MONAI models from the impressively growing Zoo much easier to use and popular.</p>

---

## Post #16 by @diazandr3s (2023-03-24 15:05 UTC)

<p>This is a very good question, <a class="mention" href="/u/rbumm">@rbumm</a>.</p>
<p>Each MONAI Label App has a <strong>main.py</strong> file. You could run the <strong>main.py</strong> file of each app as a standard python script and without starting the MONAI Label server. Just provide the arguments needed such as the folder that contains the images you want to run inference on, and the model name.</p>
<p>Here are the main.py files:</p>
<p>MONAI Label Radiology app: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/main.py" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/main.py</a></p>
<p>MONAI Label Bundle app (for the model zoo): <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/monaibundle/main.py" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/monaibundle/main.py</a></p>
<p>Let’s say I have my segmentation model in MONAI Label trained and want to run inference on one CT image in a folder called “/home/user/CT-test/”</p>
<p>I can run the main.py file of the radiology app in the monai label virtual env like this:</p>
<blockquote>
<p>python main.py --studies “/home/user/CT-test/” --model “segmentation” --test “infer”</p>
</blockquote>
<p>This command will run inference on the CT images you have in folder “/home/user/CT-test/”</p>
<p>Happy to clarify this in a call if needed <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #17 by @rbumm (2023-03-27 08:57 UTC)

<aside class="quote no-group" data-username="diazandr3s" data-post="16" data-topic="28522">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/diazandr3s/48/9973_2.png" class="avatar"> diazandr3s:</div>
<blockquote>
<p>python main.py --studies “/home/user/CT-test/” --model “segmentation” --test “infer”</p>
</blockquote>
</aside>
<p>I have tested for many hours and combinations (from powershell, from Slicer Python Console etc)  but do not get this yet working  <a class="mention" href="/u/diazandr3s">@diazandr3s</a> .<br>
Running your above script line in a otherwise working monailabel server environment throws:</p>
<pre><code class="lang-auto">File "C:\Users\Rudolf\apps\radiology\lib\activelearning\last.py", line 14, in &lt;module&gt;
    from monailabel.interfaces.datastore import Datastore
ModuleNotFoundError: No module named 'monailabel'
</code></pre>

---

## Post #18 by @diazandr3s (2023-03-27 09:26 UTC)

<p>Hi <a class="mention" href="/u/rbumm">@rbumm</a>,</p>
<p>Are you running the command on the python virtual env that has monai label installed? It seems it is not the case as it doesn’t find the monailabel module.</p>
<p>Please let us know,</p>

---

## Post #19 by @rbumm (2023-03-27 09:55 UTC)

<p>I am running this in a powershell now following our <a href="https://projectweek.na-mic.org/PW37_2022_Virtual/Projects/MONAILabelLung/MONAILabel_Installation.html">instructions from last year</a></p>
<pre><code class="lang-auto">monailabel start_server --app apps/radiology --studies datasets/Task06_Lung/imagesTr --conf models segmentation`
</code></pre>
<p>works as expected.</p>
<p>How should I install the module?</p>

---

## Post #20 by @diazandr3s (2023-03-27 12:43 UTC)

<p>It is strange. If this command runs as expected, this means the monailabel module is installed:</p>
<pre><code class="lang-auto">monailabel start_server --app apps/radiology --studies datasets/Task06_Lung/imagesTr --conf models segmentation`
</code></pre>
<p>Can you please show what you see after running?</p>
<blockquote>
<p>monailabel -h</p>
</blockquote>
<p>Can you also share what you see when entering the python command and then running import monailabel?</p>
<p>Something like this:</p>
<p><code>python</code></p>
<p>then</p>
<p><code>import monailabel</code></p>

---

## Post #21 by @rbumm (2023-03-27 13:21 UTC)

<p>I´ll contact you on Discord, maybe we can post a solution later not to push this thread up too often.</p>

---

## Post #22 by @njeffery123 (2023-10-04 11:52 UTC)

<p>hi <a class="mention" href="/u/diazandr3s">@diazandr3s</a><br>
I can get this code to work nicely<br>
python main.py --studies “/home/user/CT-test/” --model “segmentation” --test “infer”</p>
<p>but only on the first dataset in the directory “/home/user/CT-test/”, it then stops. Is there are way to process all datasets in a directory using this approach? I have a good model and I just want it to run through all the datasets in a directory, generating label maps. Very laborious in 3Dslicer using the server and next button.</p>
<p>cheers<br>
nathan</p>

---

## Post #23 by @diazandr3s (2023-10-04 23:56 UTC)

<p>Hi <a class="mention" href="/u/njeffery123">@njeffery123</a>,</p>
<p>This is what’s happening when you run infer: <a href="https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/main.py#L304-L327" rel="noopener nofollow ugc">https://github.com/Project-MONAI/MONAILabel/blob/main/sample-apps/radiology/main.py#L304-L327</a></p>
<p>You could modify the code (add a for loop) to run inference on all the unlabelled images OR by starting the server and running batch inference using the APIs from the browser. This will run inference on all the unlabelled volumes in the folder.</p>
<p>Hope this helps,</p>

---

## Post #24 by @njeffery123 (2023-10-05 06:55 UTC)

<p>Thank you, I did try a loop but couldn’t get it to work because the --studies flag references a directory not a file. Will give the API approach a try</p>

---

## Post #25 by @njeffery123 (2023-10-05 07:32 UTC)

<p>Just to a note to anyone else - the API approach works well. Start the server with the location of the files you want to batch infer, pop the server address in firefox and use “Run Batch Inference Task”. 100+ in a few minutes. Thanks <a class="mention" href="/u/diazandr3s">@diazandr3s</a></p>

---

## Post #26 by @diazandr3s (2023-10-06 22:26 UTC)

<p>Thanks for reporting back, <a class="mention" href="/u/njeffery123">@njeffery123</a> <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
