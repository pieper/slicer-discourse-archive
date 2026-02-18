# Cannot get a second vtkMRMLNodeComboBox to show nodes

**Topic ID**: 18204
**Date**: 2021-06-18
**URL**: https://discourse.slicer.org/t/cannot-get-a-second-vtkmrmlnodecombobox-to-show-nodes/18204

---

## Post #1 by @atracsys-sbt (2021-06-18 12:58 UTC)

<p>Hi,<br>
I’m trying to develop a module in which I can choose model nodes as two inputs.<br>
I started from the module automatically created from the Extension Wizard and after setting vtkMRMLModelNode as the nodeType for the vtkMRMLNodeComboBox already included in the example, it works fine. However, I created a second vtkMRMLNodeComboBox with the same attributes (beside the name) underneath and that one cannot list any of the loaded models.<br>
Please find attached some images showing the layout and options.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/9633d90b0d519cd28e5a0d3ee3fdfd34127344a9.png" data-download-href="/uploads/short-url/lqKHEfEdr8iZESLrjyNbSfHetEB.png?dl=1" title="ComboBox1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9633d90b0d519cd28e5a0d3ee3fdfd34127344a9_2_433x499.png" alt="ComboBox1" data-base62-sha1="lqKHEfEdr8iZESLrjyNbSfHetEB" width="433" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9633d90b0d519cd28e5a0d3ee3fdfd34127344a9_2_433x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/6/9633d90b0d519cd28e5a0d3ee3fdfd34127344a9_2_649x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/9633d90b0d519cd28e5a0d3ee3fdfd34127344a9.png 2x" data-dominant-color="CCD4BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ComboBox1</span><span class="informations">816×941 35.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36e9eaac491e877a9e7cc7794c5f0977f20c07e1.png" data-download-href="/uploads/short-url/7PMWKABwRbOibRkCUm2CJuYFwuB.png?dl=1" title="ComboBox2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36e9eaac491e877a9e7cc7794c5f0977f20c07e1_2_430x500.png" alt="ComboBox2" data-base62-sha1="7PMWKABwRbOibRkCUm2CJuYFwuB" width="430" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36e9eaac491e877a9e7cc7794c5f0977f20c07e1_2_430x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36e9eaac491e877a9e7cc7794c5f0977f20c07e1_2_645x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36e9eaac491e877a9e7cc7794c5f0977f20c07e1.png 2x" data-dominant-color="CCD5BC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ComboBox2</span><span class="informations">813×944 36.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b8e6df8905040b7ad497fedcc72c5a02b66eb11f.png" alt="Module" data-base62-sha1="qnIuSCcUctqW99ALXzWRtwvV30H" width="320" height="240"></p>
<p>Thank you for any help</p>

---

## Post #2 by @cpinter (2021-06-18 13:30 UTC)

<p>You need to connect the MRML scene changed signal. In Qt Designer press F4 to go to signals and slots mode, then drag&amp;drop a new signal from the very edge of your widget to the MRML node combobox.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d3f7f95533d697e68b9e3fa86520b4851c6e0a67.png" data-download-href="/uploads/short-url/ufa1JGZbO0s4FS8C5p9zf0SN1Cn.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3f7f95533d697e68b9e3fa86520b4851c6e0a67_2_369x500.png" alt="image" data-base62-sha1="ufa1JGZbO0s4FS8C5p9zf0SN1Cn" width="369" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3f7f95533d697e68b9e3fa86520b4851c6e0a67_2_369x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3f7f95533d697e68b9e3fa86520b4851c6e0a67_2_553x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/3/d3f7f95533d697e68b9e3fa86520b4851c6e0a67_2_738x1000.png 2x" data-dominant-color="C6C7D8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">838×1133 67.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then make these selections:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbc515267330e6343bef471081bca3642ee17585.png" data-download-href="/uploads/short-url/t4DaN61ohjmF7mi64pIdTMtQwn3.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbc515267330e6343bef471081bca3642ee17585.png" alt="image" data-base62-sha1="t4DaN61ohjmF7mi64pIdTMtQwn3" width="690" height="463" data-dominant-color="EFF0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1174×789 22.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @lassoan (2021-06-18 13:40 UTC)

<p>You need to set the scene into MRML widgets, such as the qMRMLNodeComboBox. We typically do this by connecting the <em>mrmlSceneChanged</em> signal of the module widget to the <em>setMRMLScene</em> slot of the MRML node selector widget. See details on slide 44 of the <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx">PerkLab bootcamp Slicer programming tutorial</a>:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8b808fd6afe2f26819d6d7bc78c39cb0cf5f98a.png" data-download-href="/uploads/short-url/sDDMPbuzmNhg804prx9xvEQ2sYy.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8b808fd6afe2f26819d6d7bc78c39cb0cf5f98a_2_667x500.png" alt="image" data-base62-sha1="sDDMPbuzmNhg804prx9xvEQ2sYy" width="667" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8b808fd6afe2f26819d6d7bc78c39cb0cf5f98a_2_667x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8b808fd6afe2f26819d6d7bc78c39cb0cf5f98a_2_1000x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8b808fd6afe2f26819d6d7bc78c39cb0cf5f98a_2_1334x1000.png 2x" data-dominant-color="E5E4E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1594×1194 228 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @atracsys-sbt (2021-06-18 13:44 UTC)

<p>Thank you both for your help !</p>

---

## Post #5 by @WilliamDaniel (2022-04-02 00:21 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
I am a beginner learning Slicer module development.<br>
Now, I’d like to add a <em><strong>qMRMLVolumeThresholdWidget</strong></em> to my UI. However, when I try to connect the <em>mrmlSceneChanged</em> signal to the <em>setMRMLScene</em> slot. I found there’s seems no <em>setMRMLScene</em> slot:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9d9a09d12c36fbe50c5f584c530712ab918458b.png" data-download-href="/uploads/short-url/zEh9ACI1sDlT0G7B3nqtPnykoyf.png?dl=1" title="Figure1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f9d9a09d12c36fbe50c5f584c530712ab918458b.png" alt="Figure1" data-base62-sha1="zEh9ACI1sDlT0G7B3nqtPnykoyf" width="453" height="375" data-dominant-color="EAE7E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Figure1</span><span class="informations">649×537 10.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Could you please tell me what to do with that?<br>
Thank you so much!</p>

---

## Post #6 by @lassoan (2022-04-02 00:39 UTC)

<p>Enable the <code>Show signals and slots inherited...</code> checkbox. If there is still no <code>setMRMLScene</code> slot then it means that the widget does not need setting of the MRML scene, it is enough to set the volume node using <code>setMRMLVolumeNode</code>. If you connect your volume node selector’s node selected signal to the volume setting slot of the threshold widget then everything should work.</p>

---
