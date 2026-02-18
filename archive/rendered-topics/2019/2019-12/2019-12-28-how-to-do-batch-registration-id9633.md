# How to do batch registration?

**Topic ID**: 9633
**Date**: 2019-12-28
**URL**: https://discourse.slicer.org/t/how-to-do-batch-registration/9633

---

## Post #1 by @Scorbinwen (2019-12-28 07:47 UTC)

<p>I want to register a  batch of CT and MR volumes automatically using 3DSlicer.For example:<br>
A1——&gt;B1<br>
A2——&gt;B2<br>
A3——&gt;B3<br>
A4——&gt;B4<br>
…<br>
I’ve briefly read the description for Sequence Registration,but that seems more like 4D registration(i.e. registrate intra-patient), which is different with my problem.<br>
Is there any module in 3DSlicer can satisfy my requirement ?<br>
Thank you very much if anyone can provide some advice~~~ <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=9" title=":grinning:" class="emoji" alt=":grinning:"> <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=9" title=":grinning:" class="emoji" alt=":grinning:"> <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=9" title=":grinning:" class="emoji" alt=":grinning:"></p>

---

## Post #2 by @lassoan (2019-12-29 02:16 UTC)

<p>You can write a short Python script that loads each image pair, runs registration (e.g., using SlicerElastix), and save the result. What would you like to achieve with these registrations?</p>

---

## Post #3 by @Scorbinwen (2019-12-29 08:10 UTC)

<p>Thank you for your quik reply, lassoan!<br>
I find the registerVolumes method in the Elastix.ElastixLogic:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1ac02fd5dd133fc653fbaeec2be7c4fc6c1b975.png" data-download-href="/uploads/short-url/rDiGtASJSmHJLlt7QFtHsbQzaBf.png?dl=1" title="Elastix_Module" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c1ac02fd5dd133fc653fbaeec2be7c4fc6c1b975.png" alt="Elastix_Module" data-base62-sha1="rDiGtASJSmHJLlt7QFtHsbQzaBf" width="690" height="242" data-dominant-color="F5F9F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Elastix_Module</span><span class="informations">849×298 7.22 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Next time</p>
<ol>
<li>I will try to write a script to call this registerVolumes method to batch process the CT-MR pairs  and output its corresponding registered CT-MR pairs.</li>
<li>Add my script into 3DSlicer as a Module.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/2623419643b56c8e7efffcd51a28b46cc8cd2432.png" data-download-href="/uploads/short-url/5rnG9FC5Z0VU58mZpSthVDgJfai.png?dl=1" title="LoadDIYModule" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/2623419643b56c8e7efffcd51a28b46cc8cd2432_2_529x500.png" alt="LoadDIYModule" data-base62-sha1="5rnG9FC5Z0VU58mZpSthVDgJfai" width="529" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/2623419643b56c8e7efffcd51a28b46cc8cd2432_2_529x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/2623419643b56c8e7efffcd51a28b46cc8cd2432_2_793x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/2623419643b56c8e7efffcd51a28b46cc8cd2432.png 2x" data-dominant-color="F1F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">LoadDIYModule</span><span class="informations">800×755 50.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
<li>Run this Module.</li>
</ol>
<p>Is this procedure right? Or there’re other easier ways?<br>
Again,thank you for your kind reply !! <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"> <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=12" title=":grinning:" class="emoji" alt=":grinning:" loading="lazy" width="20" height="20"></p>

---

## Post #4 by @lassoan (2019-12-29 16:58 UTC)

<p>If you don’t need GUI for the processing in Slicer then it may be simpler to run scripts directly from Slicer’s Python console or from the command line or use Slicer from a Jupyter notebook (using SlicerJupyter extension).</p>

---

## Post #5 by @Scorbinwen (2019-12-30 02:05 UTC)

<p>In fact,I don’t know what’re the functions to call  in Slicer’s Python console for batch registration. Any tutorials for this ?<br>
Thank you~~~</p>

---

## Post #6 by @lassoan (2019-12-30 15:57 UTC)

<p>Sequence Registration module is a good (but somewhat complex) example of how SlicerElastix module can be used for registration from a script or another module:</p>
<p><a href="https://github.com/moselhy/SlicerSequenceRegistration/blob/e9ac5c24e30ecee6a0f8dfee472aa54ff11497cf/SequenceRegistration/SequenceRegistration.py#L557-L562" class="onebox" target="_blank">https://github.com/moselhy/SlicerSequenceRegistration/blob/e9ac5c24e30ecee6a0f8dfee472aa54ff11497cf/SequenceRegistration/SequenceRegistration.py#L557-L562</a></p>

---

## Post #7 by @Scorbinwen (2019-12-31 06:09 UTC)

<p>Thank you ,yes it’s really somewhat complex for me a newbee… <img src="https://emoji.discourse-cdn.com/twitter/joy.png?v=9" title=":joy:" class="emoji" alt=":joy:">I’ve solved the batch registration problem in windows:</p>
<ol>
<li>Write a batch registration script: example</li>
</ol>
<pre><code class="lang-auto">## Run the following command in Python Console.
# execfile("path\to\BatchRegister.py")
def Register(Fixedfilename,Movingfilename,OutVolumefilename,ind):
    Nodename = 'Volume_{:02d}'.format(ind)
    RegistrationPresets_ParameterFilenames = 5
    # Load Volume
    [ success,movingVolumeNode ] = slicer.util.loadVolume(Movingfilename,returnNode=True)
    [ success, fixedVolumeNode] = slicer.util.loadVolume(Fixedfilename,returnNode=True)
    

    from Elastix import ElastixLogic
    logic = ElastixLogic()
    parameterFilenames = logic.getRegistrationPresets()[0][RegistrationPresets_ParameterFilenames]
    outputVolume = slicer.vtkMRMLScalarVolumeNode()
    slicer.mrmlScene.AddNode(outputVolume)
    outputVolume.CreateDefaultDisplayNodes()
    outputVolume.SetName(Nodename)
    logic.registerVolumes(fixedVolumeNode, movingVolumeNode, parameterFilenames = parameterFilenames , outputVolumeNode = outputVolume)

    # Create OutputVolume Node.
    myNode = getNode(Nodename)
    myStorageNode = myNode.CreateDefaultStorageNode()
    myStorageNode.SetFileName(OutVolumefilename)
    myStorageNode.WriteData(myNode)
    slicer.mrmlScene.Clear(0)



def BatchRegister():
    path2subjects = 'path\to\dataset_directory'
    import os
    for ind,dir in enumerate(os.listdir(path2subjects)):
        Fixedfilename = os.path.join(path2subjects,dir,'Fixed.ext')
        print(Fixedfilename)
        Movingfilename = os.path.join(path2subjects,dir,'Moving.ext')
        OutVolumefilename = os.path.join(path2subjects,dir,'OutVolume.ext')
        Register(Fixedfilename, Movingfilename, OutVolumefilename,ind)
BatchRegister()

</code></pre>
<p>2.Execute the Python script in the Slicer’s Python command as follow:<br>
<code>&gt;&gt;execfile("path\to\BatchRegister.py")</code></p>

---

## Post #8 by @lassoan (2019-12-31 14:55 UTC)

<p>Very nice. You can also launch your script from the command-line using <code>Slicer.exe path\to\BatchRegister.py</code>. You can also pass arguments to the script from the command-line (so that you don’t need to hardcode paths or file names) and access them in the script using <code>sys.argv</code>.</p>

---

## Post #9 by @Scorbinwen (2020-01-01 08:54 UTC)

<p>Oh,Thank you,that’s a good programming habit.<br>
And thank you for your patient replies recently.<br>
Happy New Year~~~ <img src="https://emoji.discourse-cdn.com/twitter/grinning.png?v=9" title=":grinning:" class="emoji" alt=":grinning:"></p>

---

## Post #10 by @dokay1 (2022-07-11 15:51 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/scorbinwen">@Scorbinwen</a> for this thread. I’m trying to write a script that co-registers all loaded images to a template image of the same patient and this thread is the closest to such solution.</p>
<p>So my problem is more like:<br>
A1 (3D T1 brain MRI) ← A2 (FLAIR) ← A3 (T1) ← A4 etc…</p>
<p>For simplicity, I’d just add the string FIXEDVOL to the fixed image as I’d identify this images manually anyway (highest res, least motion artifact, etc).</p>
<p>FixedVol = getNodes(‘*<em>FIXEDVOL</em> *’)<br>
PoolOfVolumes = getNodes(‘*<em>vtkMRMLScalarVolumeNode</em> *’)</p>
<p>and I would just run a for loop to process each line in PoolOfVolumes as MovingVolume with new co-regidstered volumes generated named as ‘MovingVolume’&amp;‘_COREG’</p>
<p>What lines should I specify for Elastix to do this coregistration? How can I ensure that the new volume follows the above naming scheme?</p>
<p>(I’m a total noob to python:( )</p>
<p>Thanks/Köszönöm!</p>
<p>Dave</p>

---

## Post #11 by @dokay1 (2022-07-12 13:04 UTC)

<p>Never mind. Here’s the script using BRAINSfit:</p>
<p>Requires you to add the string FIXED (case sensitive) to the volume you want to use as the Fixed volume.</p>
<pre><code class="lang-auto">PoolOfVolumes = getNodesByClass('vtkMRMLScalarVolumeNode')
FixedVol = getNode('*FIXED*')
for MovingVol in PoolOfVolumes:
    slicer.util.selectModule('BRAINSFit')
    brainsFit = slicer.modules.brainsfit   
    parametersRigid = {}
    parametersRigid["fixedVolume"] = FixedVol.GetID()
    parametersRigid["movingVolume"] = MovingVol.GetID()
    parametersRigid["outputVolume"] = MovingVol.GetID()
    parametersRigid["useRigid"] = True
    parametersRigid["initializeTransformMode"] = "useGeometryAlign"
    parametersRigid["samplingPercentage"] = 0.02
    cliBrainsFitRigidNode = slicer.cli.run(brainsFit, None, parametersRigid)

</code></pre>
<p>Tested in Slicer 5.0.2 r30822 / a4420c3 on MacOS 12.4, YMMY.</p>
<p>Best,</p>
<p>Dave</p>

---
