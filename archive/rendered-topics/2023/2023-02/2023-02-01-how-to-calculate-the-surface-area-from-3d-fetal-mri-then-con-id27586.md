---
topic_id: 27586
title: "How To Calculate The Surface Area From 3D Fetal Mri Then Con"
date: 2023-02-01
url: https://discourse.slicer.org/t/27586
---

# How to calculate the surface area from 3D fetal MRI, then convert to Python

**Topic ID**: 27586
**Date**: 2023-02-01
**URL**: https://discourse.slicer.org/t/how-to-calculate-the-surface-area-from-3d-fetal-mri-then-convert-to-python/27586

---

## Post #1 by @Jaleblanc (2023-02-01 18:27 UTC)

<p>Hi all,</p>
<p>I’m relatively new to both Python and 3D Slicer, but I am trying to calculate the surface area of the human placenta through 3D Slicer and then convert this into Python code for an automatic calculation of the placental surface area. I have a data set of NIfTI files of already segmented placentas, but I’m unsure how to get the surface area through 3D Slicer. Any help would be appreciated. Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cff42aae9314b6e16d1935d8831f581f6f099a2c.jpeg" data-download-href="/uploads/short-url/tFDXAMrA23yFDwFVDJNY2TGsDxO.jpeg?dl=1" title="Screen Shot 2023-02-01 at 9.44.04 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cff42aae9314b6e16d1935d8831f581f6f099a2c_2_690x418.jpeg" alt="Screen Shot 2023-02-01 at 9.44.04 AM" data-base62-sha1="tFDXAMrA23yFDwFVDJNY2TGsDxO" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cff42aae9314b6e16d1935d8831f581f6f099a2c_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cff42aae9314b6e16d1935d8831f581f6f099a2c_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cff42aae9314b6e16d1935d8831f581f6f099a2c_2_1380x836.jpeg 2x" data-dominant-color="33333A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-02-01 at 9.44.04 AM</span><span class="informations">1798×1091 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @Jaleblanc (2023-02-01 18:37 UTC)

<p>Here’s my update:</p>
<ul>
<li>I’ve rendered the 3D volume in the top right corner through Volume Rendering</li>
<li>I’ve added my segment under Segment Editor</li>
<li>I’ve applied only the ‘Closed Surface Statistics’ option under Segment Statistics after choosing my segment as my input, but I am not given the surface area for some reason - this is where I’m currently stuck</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/b/bbfe71d4f83eb73fd4c0e9d0ce6fac9ad76dde26.jpeg" data-download-href="/uploads/short-url/qP4qN7T65oaxGQvndvfqP1nBADY.jpeg?dl=1" title="Screen Shot 2023-02-01 at 1.32.49 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbfe71d4f83eb73fd4c0e9d0ce6fac9ad76dde26_2_690x360.jpeg" alt="Screen Shot 2023-02-01 at 1.32.49 PM" data-base62-sha1="qP4qN7T65oaxGQvndvfqP1nBADY" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbfe71d4f83eb73fd4c0e9d0ce6fac9ad76dde26_2_690x360.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbfe71d4f83eb73fd4c0e9d0ce6fac9ad76dde26_2_1035x540.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/b/bbfe71d4f83eb73fd4c0e9d0ce6fac9ad76dde26_2_1380x720.jpeg 2x" data-dominant-color="323231"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-02-01 at 1.32.49 PM</span><span class="informations">1920×1003 88.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @lassoan (2023-02-08 20:04 UTC)

<p>You need to have closed surface representation to compute “Closed surface statistics”. You can compute it by clicking the “Show 3D” button in Segment Editor module or by choosing “Create closed surface representation” in the right-click menu in Data module.</p>
<p>I would not recommend using Volume Rendering module for 3D rendering of a segmentation because it does not do an accurate reconstruction of the original smooth, continuous surface, but it just shows each voxel as a cube. Instead, load the file as a segmentation (choose <code>Segmentation</code> in “Add data” window’s “Description” column) and then create the closed surface representation to see it in 3D.</p>

---

## Post #4 by @Jaleblanc (2023-02-08 20:40 UTC)

<p>Thank you, it worked!</p>

---

## Post #5 by @Jaleblanc (2023-02-08 23:53 UTC)

<p>Would you know how to create a Python code resembling how to calculate surface area similar to 3D Slicer?</p>

---

## Post #6 by @lassoan (2023-02-09 00:10 UTC)

<p>You can run any Python code in Slicer. You can use all Slicer application features and any other Python packages. What is your overall goal?</p>

---

## Post #7 by @Jaleblanc (2023-02-09 00:31 UTC)

<p>My goal is to write a Python code that can automatically calculate the surface area of a large dataset of placentas from 3D MRI images. With 3D Slicer, I was aiming to integrate it into my python code and get the surface area information directly that way</p>

---

## Post #8 by @lassoan (2023-02-09 03:03 UTC)

<p>That sounds very easily doable. Probably the simplest is to run all your Python code in Slicer’s Python environment. You can automate everything that you did in Slicer GUI using Python scripting and you can add any additional processing in the same script. This <a href="https://github.com/PerkLab/PerkLabBootcamp/raw/master/Doc/day3_2_SlicerProgramming.pptx">PerkLab Bootcamp Slicer Programming tutorial</a> is a good starting point, you can find many examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a> and if you don’t find any answer then you can ask on this forum.</p>

---

## Post #9 by @Jaleblanc (2023-02-09 17:05 UTC)

<p>Thank you for the resources. I looked through the steps in the PerkLab tutorial on slides 36-49 and tried slides 36-43 myself before I got stuck. I’m wondering, is the .py file in 3D Slicer what I need to focus on to help me get Python code to calculate surface area? Is it something that automatically updates after I run 3D Slicer and get the surface area that way, or do I need to manually update the .py file? I want first to understand how I need to go about this, as I’m still somewhat new to Python</p>

---

## Post #10 by @lassoan (2023-02-09 17:37 UTC)

<aside class="quote no-group" data-username="Jaleblanc" data-post="9" data-topic="27586">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/85e7bf/48.png" class="avatar"> Jaleblanc:</div>
<blockquote>
<p>is the .py file in 3D Slicer what I need to focus on to help me get Python code to calculate surface area?</p>
</blockquote>
</aside>
<p>For this task you don’t need to develop a new Slicer module, just write a short code snippet that uses existing modules. However, the exercises, examples, links to resources, etc. are all applicable to a simple Python script the same way as to a Slicer module.</p>
<aside class="quote no-group" data-username="Jaleblanc" data-post="9" data-topic="27586">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/85e7bf/48.png" class="avatar"> Jaleblanc:</div>
<blockquote>
<p>Is it something that automatically updates after I run 3D Slicer and get the surface area that way, or do I need to manually update the .py file?</p>
</blockquote>
</aside>
<p>Since you will not develop a new Slicer module, you’ll just write a Python script and start it using <code>Slicer.exe --python-script /path/to/myscript.py</code>. If you modify the script, save it, and launch it with this command then the modified script will run.</p>

---

## Post #11 by @Jaleblanc (2023-02-09 19:20 UTC)

<p>I’m sorry, I’m still a little lost with starting this process, would I need to write more code to calculate surface area if Slicer already has code written? I’m just unsure what code I have to write.</p>
<p>If so, would this be where I write the Python script?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/415d0e7b81a0a80e6cbfc2674da787e6057b82af.jpeg" data-download-href="/uploads/short-url/9kepjKTeSqsnfTE708EWxPqxXyf.jpeg?dl=1" title="Screen Shot 2023-02-09 at 2.16.09 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/415d0e7b81a0a80e6cbfc2674da787e6057b82af_2_517x321.jpeg" alt="Screen Shot 2023-02-09 at 2.16.09 PM" data-base62-sha1="9kepjKTeSqsnfTE708EWxPqxXyf" width="517" height="321" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/415d0e7b81a0a80e6cbfc2674da787e6057b82af_2_517x321.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/415d0e7b81a0a80e6cbfc2674da787e6057b82af_2_775x481.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/415d0e7b81a0a80e6cbfc2674da787e6057b82af_2_1034x642.jpeg 2x" data-dominant-color="3E3D3E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-02-09 at 2.16.09 PM</span><span class="informations">1920×1196 170 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @Jaleblanc (2023-02-15 22:19 UTC)

<p>Would you please let me know which Python parameter I need to use to get the surface area? Thank you</p>

---

## Post #13 by @lassoan (2023-02-16 00:37 UTC)

<p>You can work out what code you need by using the interactive Python console in Slicer:</p>
<ul>
<li>load the NIFTI file as segmentation</li>
<li>create closed surface representation</li>
<li>use Segment Statistics module to compute surface area</li>
</ul>
<p>For each of these steps, you can find the necessary code snippets in the script repository (1-2 lines of Python code each):</p>
<ul>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-a-3d-image-or-model-file-as-segmentation">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-a-3d-image-or-model-file-as-segmentation</a></li>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-segmentation-in-3d">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-segmentation-in-3d</a></li>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-of-each-segment">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-of-each-segment</a></li>
</ul>

---

## Post #15 by @Jaleblanc (2023-02-28 19:15 UTC)

<p>From the first link, “slicer.util.loadSegmentation” is not working on PyCharm for me, I have imported ‘slicer,’ but I can’t find anything on ‘util’</p>
<p>I tried ‘pip install util’ in the command window, but I was getting another error with util:</p>
<p><code>ERROR: Could not find a version that satisfies the requirement util (from versions: none)</code><br>
<code>ERROR: No matching distribution found for util</code></p>
<p>Would you happen to know if there’s an alternative to this line of code from the script repository or how to find the download for util? I have looked on <a href="http://pypi.org" rel="noopener nofollow ugc">pypi.org</a>, but I don’t know which one is the correct one.</p>

---

## Post #16 by @muratmaga (2023-02-28 19:52 UTC)

<p>You need to run your python code inside the Slicer Python console. Sounds like you are trying to use an external python.</p>

---

## Post #17 by @Jaleblanc (2023-02-28 20:00 UTC)

<p>Is that why the code won’t work in PyCharm?</p>
<p>Here’s what I get when I run it in the Slicer Python Console:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00496aea4aadd2c09d0b06be86dc6309029e9154.png" data-download-href="/uploads/short-url/2xinZfiFnC0XNECtO8VuoQP1vC.png?dl=1" title="Screen Shot 2023-02-28 at 2.58.24 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00496aea4aadd2c09d0b06be86dc6309029e9154_2_690x385.png" alt="Screen Shot 2023-02-28 at 2.58.24 PM" data-base62-sha1="2xinZfiFnC0XNECtO8VuoQP1vC" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00496aea4aadd2c09d0b06be86dc6309029e9154_2_690x385.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00496aea4aadd2c09d0b06be86dc6309029e9154_2_1035x577.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00496aea4aadd2c09d0b06be86dc6309029e9154_2_1380x770.png 2x" data-dominant-color="2C2724"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-02-28 at 2.58.24 PM</span><span class="informations">2063×1152 317 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #18 by @pieper (2023-02-28 20:39 UTC)

<p>That error looks like just an incorrect path.  Try forward slashes.</p>

---

## Post #19 by @Jaleblanc (2023-02-28 20:50 UTC)

<p>Thank you, I added the forward slashes, but now get this error:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/089c407e5a232636e351488f6ab6067b344c1929.png" data-download-href="/uploads/short-url/1eaAsaZpiXu7qCQOVk94Pbil8tH.png?dl=1" title="Screen Shot 2023-02-28 at 3.48.58 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/089c407e5a232636e351488f6ab6067b344c1929_2_690x346.png" alt="Screen Shot 2023-02-28 at 3.48.58 PM" data-base62-sha1="1eaAsaZpiXu7qCQOVk94Pbil8tH" width="690" height="346" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/089c407e5a232636e351488f6ab6067b344c1929_2_690x346.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/089c407e5a232636e351488f6ab6067b344c1929_2_1035x519.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/089c407e5a232636e351488f6ab6067b344c1929_2_1380x692.png 2x" data-dominant-color="282323"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-02-28 at 3.48.58 PM</span><span class="informations">2027×1019 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #20 by @muratmaga (2023-02-28 21:03 UTC)

<p>Try putting your data to a simpler path (e.g., C:/data) and try. that’s is a path error. Read cannot find the file, either path provided is not correct or spaces are causing an issue.</p>

---

## Post #21 by @Jaleblanc (2023-02-28 21:29 UTC)

<p>Would this be considered a simpler file path: slicer.util.loadSegmentation(“C:/Users/jaleesaleblanc/Desktop/FMS0078.labels.nii”)</p>
<p>I don’t know how to make it simpler, but somehow I’m getting the same error</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f547dfda835a10fb45ab3382217fa1c727baf01.png" data-download-href="/uploads/short-url/2bCbvFg1RKtZmKNrBncXHHaMcV3.png?dl=1" title="Screen Shot 2023-02-28 at 4.26.53 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f547dfda835a10fb45ab3382217fa1c727baf01_2_690x298.png" alt="Screen Shot 2023-02-28 at 4.26.53 PM" data-base62-sha1="2bCbvFg1RKtZmKNrBncXHHaMcV3" width="690" height="298" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f547dfda835a10fb45ab3382217fa1c727baf01_2_690x298.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f547dfda835a10fb45ab3382217fa1c727baf01_2_1035x447.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0f547dfda835a10fb45ab3382217fa1c727baf01_2_1380x596.png 2x" data-dominant-color="272222"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-02-28 at 4.26.53 PM</span><span class="informations">1988×861 145 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #22 by @pieper (2023-02-28 21:40 UTC)

<p>Be sure to confirm that the file works if you just drag-and-drop it on slicer from that location.  You can also check the path by getting the file properties (right click on the desktop icon and check the path - confirm that it’s the same but with just the slashes different).</p>

---

## Post #23 by @Jaleblanc (2023-02-28 22:22 UTC)

<p>Ok, I checked the file properties, and the path name matches my code. When I dragged and dropped the file into the console, I got this message:</p>
<p>[Qt] &lt;QNSPanel: 0x7fd441a08ba0; contentView=&lt;QNSView: 0x7fd441a088e0; QCocoaWindow(0x60000024c8f0, window=QWidgetWindow(0x60000115d440, name=“qSlicerDataDialogWindow”))&gt;&gt; has active key-value observers (KVO)! These will stop working now that the window is recreated, and will result in exceptions when the observers are removed. Break in QCocoaWindow::recreateWindowIfNeeded to debug.</p>

---

## Post #24 by @pieper (2023-02-28 22:24 UTC)

<p>I don’t know if that message is related but were you able to load the data?  If drag and drop doesn’t work you can browse to the file with the Add Data option.</p>

---

## Post #25 by @Jaleblanc (2023-02-28 22:29 UTC)

<p>When I drag and drop, this is the window that opens (I have the description set to Segmentation, not Transform) and then I am able to add the data</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1151edff7d5d0c5601b154a1667826740ea59fb.jpeg" data-download-href="/uploads/short-url/mZ07EsLRNYyJ7PxGeSA1bNhCx1V.jpeg?dl=1" title="Screen Shot 2023-02-28 at 5.27.31 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1151edff7d5d0c5601b154a1667826740ea59fb_2_690x399.jpeg" alt="Screen Shot 2023-02-28 at 5.27.31 PM" data-base62-sha1="mZ07EsLRNYyJ7PxGeSA1bNhCx1V" width="690" height="399" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1151edff7d5d0c5601b154a1667826740ea59fb_2_690x399.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1151edff7d5d0c5601b154a1667826740ea59fb_2_1035x598.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1151edff7d5d0c5601b154a1667826740ea59fb_2_1380x798.jpeg 2x" data-dominant-color="2A2725"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-02-28 at 5.27.31 PM</span><span class="informations">1920×1111 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #26 by @muratmaga (2023-02-28 22:35 UTC)

<p>C:/ is windows syntax, but apparently you are on Mac.</p>
<p>Just use the path as shown in your data dialog screenshot /Users/…</p>

---

## Post #27 by @Jaleblanc (2023-02-28 22:48 UTC)

<p>I’m sorry I should’ve mentioned that before. It no longer gives me the error message about reading the file; thank you!</p>
<p>When I run the Python Console, it says ‘Segmentation’ is not defined (I highlighted the area it is referring to). I got this line of code from the script repository, but do you know how I would define it?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33cdc974fccbbdddea53088677e825b575a11c0e.png" data-download-href="/uploads/short-url/7ohfljJcn2NU88oWJN0UybKPfuC.png?dl=1" title="Screen Shot 2023-02-28 at 5.46.10 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33cdc974fccbbdddea53088677e825b575a11c0e_2_690x322.png" alt="Screen Shot 2023-02-28 at 5.46.10 PM" data-base62-sha1="7ohfljJcn2NU88oWJN0UybKPfuC" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33cdc974fccbbdddea53088677e825b575a11c0e_2_690x322.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33cdc974fccbbdddea53088677e825b575a11c0e_2_1035x483.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33cdc974fccbbdddea53088677e825b575a11c0e_2_1380x644.png 2x" data-dominant-color="262625"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-02-28 at 5.46.10 PM</span><span class="informations">1611×752 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #28 by @pieper (2023-02-28 23:52 UTC)

<p>Probably it’s unclear in the script repository, and if so it would be great if you could submit a pull request with a suggestion how to make it clearer to new users (if you don’t know how we can guide you), but this script is missing the first part of the first line.  It should say:</p>
<pre><code class="lang-auto">segmentationNode = slicer.util.loadSegmentation("...")
</code></pre>
<p>and then the second line would be:</p>
<pre><code class="lang-auto">segmentationNode.CreateClosedSurfaceRepresentation()
</code></pre>
<p>(note the capitalization matters on the variable <code>segmentationNode</code>)</p>
<p>From there you can use <code>segmentationNode</code> and you don’t need the <code>getNode</code> call since you get the loaded node as the return value from <code>loadSegmentation</code>.</p>

---

## Post #29 by @Jaleblanc (2023-03-01 00:17 UTC)

<p>Thank you so much, this makes more sense, and I don’t get that error anymore. I don’t mind submitting a pull request to help others, I’ve never made one before, but any help would be appreciated thank you!</p>
<p>And I’m really hoping this is the last error. In my last section of code, I retrieved it from: “Quantifying segments - Get volume of each segment” (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-of-each-segment" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>)</p>
<p>I changed the volume to the surface area, as this is the measurement I need, but my 3rd last line has a KeyError</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f4e46a40f0ffd5d3551a7e2e5f3b5a976452ee6b.png" data-download-href="/uploads/short-url/yWpSxTib968lrNaNfvO81ZGkmmv.png?dl=1" title="Screen Shot 2023-02-28 at 7.10.28 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4e46a40f0ffd5d3551a7e2e5f3b5a976452ee6b_2_690x286.png" alt="Screen Shot 2023-02-28 at 7.10.28 PM" data-base62-sha1="yWpSxTib968lrNaNfvO81ZGkmmv" width="690" height="286" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4e46a40f0ffd5d3551a7e2e5f3b5a976452ee6b_2_690x286.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4e46a40f0ffd5d3551a7e2e5f3b5a976452ee6b_2_1035x429.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4e46a40f0ffd5d3551a7e2e5f3b5a976452ee6b_2_1380x572.png 2x" data-dominant-color="262323"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-02-28 at 7.10.28 PM</span><span class="informations">1670×694 99.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #30 by @pieper (2023-03-01 00:35 UTC)

<p>Here you need to be sure you access the right name of the calculated statistic.  In this case it’s:</p>
<pre><code class="lang-auto">stats[segmentId, "ClosedSurfaceSegmentStatisticsPlugin.surface_mm2"]
</code></pre>
<p>One of the nice things about the python console is that you can do things step by step and check the values.  For example, you could run this command to see all the values in the stats array so you know the valid keys:</p>
<pre><code class="lang-auto">for key in stats.keys():
  print(key)
</code></pre>
<p>looking at the variables like this can help you debug.</p>
<p>It would be great if you could make improvements to the documentation based on your experience and what you have learned.  Mostly we use the github process that is very standard and there are lots of documents.  I didn’t search a lot, but <a href="https://docs.joomla.org/Using_the_Github_UI_to_Make_Pull_Requests">this tutorial</a> might be useful.</p>
<p>The things that are specific to Slicer are <a href="https://slicer.readthedocs.io/en/latest/developer_guide/contributing.html">described here</a>.  Much of the complexity is when you suggest code changes, but documentation changes are much easier and can be completed entirely using the web interface.</p>

---

## Post #31 by @Jaleblanc (2023-03-01 01:15 UTC)

<p>Thank you so much, Steve; it worked! (And thank you <a class="mention" href="/u/muratmaga">@muratmaga</a> and <a class="mention" href="/u/lassoan">@lassoan</a> for your help)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f4ddb33371915de174fd5044cad3213af278aae0.png" data-download-href="/uploads/short-url/yWbuyxBc6KtRCpsEvgGOt4WJTgI.png?dl=1" title="Screen Shot 2023-02-28 at 8.08.56 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4ddb33371915de174fd5044cad3213af278aae0_2_517x262.png" alt="Screen Shot 2023-02-28 at 8.08.56 PM" data-base62-sha1="yWbuyxBc6KtRCpsEvgGOt4WJTgI" width="517" height="262" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4ddb33371915de174fd5044cad3213af278aae0_2_517x262.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4ddb33371915de174fd5044cad3213af278aae0_2_775x393.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/4/f4ddb33371915de174fd5044cad3213af278aae0_2_1034x524.png 2x" data-dominant-color="2B2A27"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2023-02-28 at 8.08.56 PM</span><span class="informations">1690×858 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I will look into those sources as a starting point and see what I can do regarding the pull request, thank you for your help!</p>
<p>I do have one last question if that’s alright. Is it possible to load multiple segmentations at once in my code? I wanted to use my code for a large data set of placentas, and my current code only takes one at a time.</p>

---

## Post #32 by @lassoan (2023-03-01 04:51 UTC)

<aside class="quote no-group" data-username="Jaleblanc" data-post="31" data-topic="27586">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/85e7bf/48.png" class="avatar"> Jaleblanc:</div>
<blockquote>
<p>I do have one last question if that’s alright. Is it possible to load multiple segmentations at once in my code? I wanted to use my code for a large data set of placentas, and my current code only takes one at a time.</p>
</blockquote>
</aside>
<p>You can load any number of segmentations. To conserve memory, it probably makes sense to process them one by one (load, process, save results, close scene).</p>

---

## Post #33 by @Jaleblanc (2023-03-02 01:40 UTC)

<p>Thank you, I will stick to processing them one at a time.</p>

---
