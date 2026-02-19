---
topic_id: 26311
title: "Issues With Loadtransform Saving Transforms"
date: 2022-11-18
url: https://discourse.slicer.org/t/26311
---

# Issues with loadTransform, saving transforms

**Topic ID**: 26311
**Date**: 2022-11-18
**URL**: https://discourse.slicer.org/t/issues-with-loadtransform-saving-transforms/26311

---

## Post #1 by @nrex45 (2022-11-18 20:21 UTC)

<p>Hey there,</p>
<p>2 questions / inqueries regarding transforms:</p>
<ol>
<li>I’m having issues loading transforms using the slicer.util.loadtransform() method. No matter what file type I save in slicer (.txt, .tfm, .h5, etc…) I have thus been unable to save a transform file and then reopen it the “conventional” way. Note than I can still drag and drop the transform into slicer and it will open properly, so I know it is not a file type issue.</li>
</ol>
<p>I have no issues loading segmentations or volumes using similar slicer.util.loadVolume() etc…</p>
<ol start="2">
<li>In the past I have written some code that parses the text file and then “recreates” a transform node in Slicer, but I’m getting some very, very strange results where, when I load the raw text file into Slicer, it is seemingly changing the values of the transform.</li>
</ol>
<p>I have attached a screenshot, showing the raw text file I saved (using slicer! Note that the format in which it saves isn’t perfecly aligned with what slicer displays, but I’ve highlited 2 of the numerous discrepencies between what was saved and what is opened) and the transform when loaded back into slicer… Why are the values different? Clearly there is some rounding going on, but surely this wouldnt explain a 5mm difference between two values.</p>
<p>Any idea what’s going on here?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e57ab241719d0753d3acea7484b584091db4cae.png" data-download-href="/uploads/short-url/6BXN8FmzUUOS5oL61TTD6j8d6sm.png?dl=1" title="Screen Shot 2022-11-18 at 1.17.29 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e57ab241719d0753d3acea7484b584091db4cae_2_690x315.png" alt="Screen Shot 2022-11-18 at 1.17.29 PM" data-base62-sha1="6BXN8FmzUUOS5oL61TTD6j8d6sm" width="690" height="315" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e57ab241719d0753d3acea7484b584091db4cae_2_690x315.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/e/2e57ab241719d0753d3acea7484b584091db4cae_2_1035x472.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e57ab241719d0753d3acea7484b584091db4cae.png 2x" data-dominant-color="262726"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-11-18 at 1.17.29 PM</span><span class="informations">1249×571 66.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Any help would be greatly appreciated.</p>
<p>Edit: Also probably worth noting that Slicer’s interpretation of the data is “correct”, i.e. a perfect overlap (top) when I “manually recreate” the transform using the raw numbers from the text file, I get the “wrong” answer (not a perfect overlap) (bottom)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c007e5974ddbc4280bf992b3f9db5a94f3636dd.png" alt="Screen Shot 2022-11-18 at 1.56.38 PM" data-base62-sha1="hGYglV4iDCiCmxHT9GZDaQ0x2CF" width="357" height="311"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/58b2d107c124cf40c557e1e2cf6a1bcc332d955f.png" alt="Screen Shot 2022-11-18 at 1.58.00 PM" data-base62-sha1="cEF83RliQQby9tJc4I2AlgPrbDF" width="373" height="413"></p>

---

## Post #2 by @muratmaga (2022-11-18 21:52 UTC)

<aside class="quote no-group" data-username="nrex45" data-post="1" data-topic="26311">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nrex45/48/7664_2.png" class="avatar"> nrex45:</div>
<blockquote>
<p>Why are the values different? Clearly there is some rounding going on, but surely this wouldnt explain a 5mm difference between two values.</p>
</blockquote>
</aside>
<p>That always confused me until I understood that the conventions are different. So here is one random translartion I created in Slicer:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbca58c41136b00e5bad97a69f64827e92cc3c15.png" alt="image" data-base62-sha1="t4Os30CCMuDUrvYbPF34dEvvXZH" width="370" height="234"></p>
<p>That got written into the file as:</p>
<pre><code class="lang-auto">#Insight Transform File V1.0
#Transform 0
Transform: AffineTransform_double_3_3
Parameters: 1 0 0 0 1 0 0 0 1 -12 14 -6
FixedParameters: 0 0 0
</code></pre>
<p>You can see the sign change for 6 to (-6). That because the file written into ITK is the inverse transform of what Slicer is displaying. So actually if you scroll down on the Transform module and click the <code>Invert</code> button, you will see that the displayed transform will now match the file (Slicer now displays a negatove sign (-) to indicate transform:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/214673f6a4c2572f84ee83eb3745b484cf71c730.png" alt="image" data-base62-sha1="4KmHtXHk8mRjQhOsYgHx0ZAqZRm" width="334" height="305"></p>
<p>I never tried loading the transform from Python into Slicer, but I suggest inverting the transform and then applying it might be a fix.</p>

---

## Post #3 by @lassoan (2022-11-19 17:32 UTC)

<p>The Slicer GUI shows modelling transform in RAS coordinate system. ITK transformation file convention is resampling transform in LPS coordinate system. See detailed explanation and link to conversion scripts in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/transforms.html#transform-files">Transforms module’s developer documentation</a>.</p>
<p>Please copy here the code snippets that you use for saving and loading transforms and we’ll have look why they don’t work as you expect.</p>

---

## Post #4 by @Lohi (2022-11-20 20:16 UTC)

<p>Andras&lt;<br>
hello to <img src="https://emoji.discourse-cdn.com/twitter/canada.png?v=12" title=":canada:" class="emoji" alt=":canada:" loading="lazy" width="20" height="20">from a <img src="https://emoji.discourse-cdn.com/twitter/canada.png?v=12" title=":canada:" class="emoji" alt=":canada:" loading="lazy" width="20" height="20"> in <img src="https://emoji.discourse-cdn.com/twitter/de.png?v=12" title=":de:" class="emoji" alt=":de:" loading="lazy" width="20" height="20"></p>
<p>I’m feeling particularly dense, at the moment [waiting for admission for deeper diagnosis of SIH/CSF leak…]<br>
i just can’t seem to get my foggy brain wrapped around 3DSlicer, and i would really like to be able to do a good skull/c-spine ‘picture’, using several MRI/DSA/CTA/MRIcontrast, sources.<br>
have clear spinal stenosis, probable CSF leak in c-spine, and a very tricky positional ‘insult’/compression of RVA…<br>
is there any really, really good help/tutorial? i’ve looked at the tutorials from the Wiki, and have used Horos quite a bit, but there is just <em>something</em> in the 3DSlicer UI, and ‘philosophy’, that are defeating me… not a doctor, but, sadly, getting better at reading MRIs than i would have dreamed. if you want to contact me off-list, that’s dandy, don’t want to waste the bandwidth of all if you experts!</p>

---

## Post #5 by @lassoan (2022-11-20 21:13 UTC)

<p>3D Slicer is more flexible than typical medical image review applications, because it says designed to deal with one-of-a-kind cases. Since there are no guide rails, it can be more complicated to figure out what you can do and how to do it.</p>
<p>If you write here any specific question then we should be able to help with either pointing to an existing tutorial or describe the steps that you can follow.</p>

---

## Post #6 by @Lohi (2022-11-20 21:33 UTC)

<p>thanks, sir…I’ll try to come up with specifics, but right now, just getting a series loaded, and a 3D up, tough enough …maybe i should start with register, first, on 2D, since that’s probably the first step in the process of building a more detailed/‘deeper’ image set.<br>
cheers</p>

---

## Post #7 by @nrex45 (2022-11-21 16:15 UTC)

<p>As always, thanks for the insightful comment Andras! I think that I will be able to reverse engineer a solution that works for my problem from the code example provided.</p>
<p>W/R/T code snippets for saving an loading transforms, some brief snippets of code are attached. Not much to the loadTransform code, which really has me scratching my head.</p>
<pre><code class="lang-auto">####creating and saving a transform node	
LR = 10 ### 
PA = 20 ###
IS = 15 ###
transformNode = slicer.vtkMRMLLinearTransformNode()
slicer.mrmlScene.AddNode(transformNode) 

transformMatrixNP = np.array(
    [
        [1,0,0, LR],
        [0,1,0, PA],
        [0,0,1, IS],
        [0,0,0,1] 
    ]
    )
        # Update matrix in transform node
    transformNode.SetAndObserveMatrixTransformToParent(slicer.util.vtkMatrixFromArray(transformMatrixNP))
        #print(transformNode)
tmax.SetAndObserveTransformNodeID(transformNode.GetID())
tmax.HardenTransform()

myTransformStorageNode = transformNode.CreateDefaultStorageNode()
myTransformStorageNode.SetFileName("temp_tmax_in_ctp0.txt")
myTransformStorageNode.WriteData(transformNode)

##### loading a transform node (doesn't work with any saved file type, whether I save it via code or GUI)

fu_xform = slicer.util.loadTransform("temp_tmax_in_ctp0.txt")
</code></pre>

---

## Post #8 by @nrex45 (2022-11-21 17:54 UTC)

<p>Confirmed the LPS to RAS cordinate system worked <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> so that part is officially resolved, thank you so much!</p>
<p>Still troubles with loading transforms with slicer.util.loadTransform, but now that I can properly generate them from a 4x4 array I should be all set.</p>

---

## Post #9 by @lassoan (2022-11-22 03:36 UTC)

<p>I’ve tested your code snippet and everything works well, except that you haven’t specified a full path for saving and loading and used APIs at different levels.</p>
<p>The two different APIs use a different path prefix for relative paths:</p>
<ul>
<li>MRML storage node: lower-level API, uses the current working directory (Slicer.exe location) as a basis for resolving relative paths</li>
<li>slicer.util.loadTransform: higher-level API, uses the scene path as path prefix</li>
</ul>
<p>I would recommend using full paths when saving or loading data to avoid ambiguity.</p>

---
