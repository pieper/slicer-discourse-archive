---
topic_id: 25651
title: "Input Function Writing On Wrong Line"
date: 2022-10-12
url: https://discourse.slicer.org/t/25651
---

# Input function writing on wrong line

**Topic ID**: 25651
**Date**: 2022-10-12
**URL**: https://discourse.slicer.org/t/input-function-writing-on-wrong-line/25651

---

## Post #1 by @hourglassnam (2022-10-12 09:53 UTC)

<p>Hello, Slicer community!</p>
<p>I was trying to make the python process wait for me while I manually edit the segmentation.</p>
<p>I thought of using the input function for this.<br>
But somehow, the python interacter keep makes me to write on wrong line and the function would not work properly…</p>
<p>I tested the same script on VS code and it worked as it supposed to.<br>
So I do not understand why slicer is making me write on wrong line.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d2e71222c006711a35cb6828e721b0c985583b9.jpeg" data-download-href="/uploads/short-url/k8WP8aaa1M1sAfl29xlThNa2npv.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d2e71222c006711a35cb6828e721b0c985583b9_2_690x496.jpeg" alt="image" data-base62-sha1="k8WP8aaa1M1sAfl29xlThNa2npv" width="690" height="496" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d2e71222c006711a35cb6828e721b0c985583b9_2_690x496.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d2e71222c006711a35cb6828e721b0c985583b9_2_1035x744.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d2e71222c006711a35cb6828e721b0c985583b9.jpeg 2x" data-dominant-color="F9F8FA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1040×748 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c084f8466a05c873e8cf8207cc1456a33ad67bf.jpeg" data-download-href="/uploads/short-url/mgki1Pqa9TC0YLfnYQn8uFtiDmL.jpeg?dl=1" title="KakaoTalk_Photo_2022-10-12-15-46-19" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c084f8466a05c873e8cf8207cc1456a33ad67bf_2_345x94.jpeg" alt="KakaoTalk_Photo_2022-10-12-15-46-19" data-base62-sha1="mgki1Pqa9TC0YLfnYQn8uFtiDmL" width="345" height="94" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c084f8466a05c873e8cf8207cc1456a33ad67bf_2_345x94.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c084f8466a05c873e8cf8207cc1456a33ad67bf_2_517x141.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c084f8466a05c873e8cf8207cc1456a33ad67bf_2_690x188.jpeg 2x" data-dominant-color="F8F8FA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">KakaoTalk_Photo_2022-10-12-15-46-19</span><span class="informations">1644×452 50 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Can anyone give me advice on why this problem may occur and how to I can solve this?<br>
below is my script and thank you always for your help.</p>
<pre><code class="lang-auto">import os
import sys

def moveOn():
	toPass = ["y", "Y"]
	while True:
		try:
			value = input("Do you want to move on?(Y/N) : ")
		except ValueError:
			print("Sorry, I didn't understand that.")
			return moveOn()
		if value not in toPass:
			print("Sorry, you typed wrong value.")
			return moveOn()
		else:
			return value

nrrdDir = "F:/inputTesting"
nrrdList = [file for file in os.listdir(nrrdDir) if file.endswith(r'.nrrd')]
for volFile in nrrdList:
	volName = str(volFile).strip(".nrrd")
	volDir = nrrdDir + "/" + volFile
	print("____" + volName + " Polishing...\n")
	value = moveOn()
	print("If this is printed, then input worked")
</code></pre>

---

## Post #2 by @lassoan (2022-10-19 21:17 UTC)

<p>Showing the user some messages on some text console in a GUI application would be highly unusual and inconvenient for users. Instead, you can quickly create a nice and convenient GUI in Qt designer. See for example <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx">this tutorial</a>. You can put a Segment Editor widget inside your module, so your users don’t need to switch to a different module during segmentation. Having your python script in a Slicer module also takes care of selecting inputs, outputs, installation, distribution to users, updates, etc.</p>
<p>If you don’t need very smooth user experience just some very quick way to run a python script somewhat interactively, then you can add a button anywhere on the GUI, for example in the status bar, and continue with the processing when the user clicked the button. For example:</p>
<pre data-code-wrap="python"><code class="lang-python">def onNextStep():
    print("Editing completed.")

nextStepButton = qt.QPushButton("Finish segmentation")
slicer.util.mainWindow().statusBar().insertPermanentWidget(0, nextStepButton)
nextStepButton.connect('clicked()', onNextStep)

# To remove the button:
# slicer.util.mainWindow().statusBar().removeWidget(nextStepButton)
</code></pre>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3ce1f01f12f68a6316939a2518a62db1b0f7db2.png" alt="image" data-base62-sha1="wvfZTjO4ZN3hX44SebRQZwq1XJ8" width="590" height="243"></p>

---

## Post #3 by @lassoan (2022-10-21 12:12 UTC)

<p>About the original issue of the unexpected behavior of the console: I’ve <a href="https://github.com/commontk/CTK/pull/1045">submitted a fix for the issue</a>, it should be integrated into the Slicer Preview Release within a few days. I would still recommend to use buttons, widgets, etc. on a module GUI to communicate with end users, instead of via messages in a text console.</p>

---

## Post #4 by @hourglassnam (2022-11-09 06:29 UTC)

<p>This is so awesome!! <img src="https://emoji.discourse-cdn.com/twitter/laughing.png?v=12" title=":laughing:" class="emoji" alt=":laughing:" loading="lazy" width="20" height="20"><br>
I did tried to make a button but just could not figure out how to make it work properly!<br>
So thank you so much for providing this awesome script!!<br>
This is way better than what I have been doing!!<br>
And thank you for fixing the console as well!!!</p>

---
