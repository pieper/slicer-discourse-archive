---
topic_id: 25254
title: "Is It Possible To Load Mitk File Into Slicer Project Or Load"
date: 2022-09-14
url: https://discourse.slicer.org/t/25254
---

# Is it possible to load .mitk file into slicer project or load .mrb file into mitk project?

**Topic ID**: 25254
**Date**: 2022-09-14
**URL**: https://discourse.slicer.org/t/is-it-possible-to-load-mitk-file-into-slicer-project-or-load-mrb-file-into-mitk-project/25254

---

## Post #1 by @jay1987 (2022-09-14 07:57 UTC)

<p>one of my friend use mitk to develop project , and i use slicer , i want to find some ways to communicate with out output files</p>

---

## Post #2 by @pieper (2022-09-14 12:12 UTC)

<p>Slicer and MITK share a lot of the same underlying libraries but are different at the application level so many of the data structures will be different.  You can probably share data objects like models and volumes, but things like transforms and markups may need converter code.  They are both open source so it would be possible but I don’t recall anyone working on that kind of generic code.</p>

---

## Post #3 by @jay1987 (2022-09-15 13:17 UTC)

<p>thanks pieper,<br>
i discussed with my friend with MITK and Slicer,they share a lot of libraries like ITK,VTK,CTK,DCMTK etc,but it’s different at the middle layer,we can unzip the Slicer .MRB file and unzip the MITK .mitk file to analyse the config file and load the volume and model etc, according to the config file , it’s realy a hard work!</p>

---

## Post #4 by @lassoan (2022-09-15 13:33 UTC)

<p>Implementing a universal converter between the two scene file formats would not be practically feasible, because there are a lot of features and by the time you completed a converter, things would change in both applications.</p>
<p>However, it would be straightforward to create a converter for specific data types. Display properties are stored in xml files, which you can parse with a short Python script and write out in the other application’s format. Bulk image, mesh, etc. data are stored in the same standard file formats in both applications, so they don’t need any conversion.</p>
<p>What is the task you are trying to accomplish?</p>

---

## Post #5 by @jay1987 (2022-09-15 13:40 UTC)

<p>thanks lassoan<br>
thank you for your advice,your method is obviously better than mine,if needed,i will take your advice , my friend has written a program use MITK old version ,it’s hard to complete complex task,so he want me to use Slicer to complete the surgical plan and export the result to his program.<br>
finaly , thank you very much <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #6 by @lassoan (2022-09-15 13:48 UTC)

<p>What kind of data you want to bring over from the old .mitk files?</p>
<p>If you only need to bring over segmentations then probably all you need is to extract the segment names and colors from the MITK-created file and write them back to the image header in Slicer-compatible format. You can read/write nrrd files using pynrrd and the whole processing should not take more than 20-30 lines of code. If you provide an example file then we can give tips on how to do it.</p>
<p>Alternatively, if you don’t want to write any custom script, you can export the segmentation in MITK to DICOM Segmentation Object. You can import these DICOM files into Slicer. This conversion should preserve segment names and colors.</p>

---

## Post #7 by @jay1987 (2022-09-15 13:55 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="25254">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>bring over</p>
</blockquote>
</aside>
<p>thanks <a class="mention" href="/u/lassoan">@lassoan</a><br>
we don’t want to bring over from the old .mitk files, we want to use mitk to analyse slicer files , the mitk project is a old project linked with other hardware tasks ,so we need to write code in the old mitk project ,what we can do in slicer is what we can export .</p>

---

## Post #8 by @lassoan (2022-09-15 13:58 UTC)

<p>What kind of analysis would you like to do? If that is already supported in Slicer then we can help with that.</p>
<p>If you want to export data from Slicer then you can find the list of supported file formats <a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#supported-data-formats">here</a>.</p>

---

## Post #9 by @jay1987 (2022-09-15 14:04 UTC)

<p>we want to extract the brain from T1 and get DTI model from DMRI plugin ,it can’t be done well in MITK Porject,we want export the nrrd volume ,model file and color ,position ,direction position config file from slicer and load them in MITK project,but it need many times to accomplish that <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #10 by @lassoan (2022-09-15 15:53 UTC)

<p>The saved nrrd image and model files can be loaded into MITK directly. I’m not sure what you mean by “color, position, direction position config file”.</p>

---

## Post #11 by @jay1987 (2022-09-16 01:08 UTC)

<p>yes,nrrd image and model files can be loaded into MITK directly,but the color of image,the position of image and direction of the image in slicer is represented in ColorNode and ScalarVolumeNode,in MITK represented in the DataNode Attribute,so i think it needed a config file to bridges these representations</p>

---

## Post #12 by @lassoan (2022-09-16 01:24 UTC)

<p>Orientation of the image is stored in the nrrd file. What do you mean by color? The chosen lookup table or window/level?</p>

---

## Post #13 by @jay1987 (2022-09-16 02:09 UTC)

<p>thanks lassoan<br>
volume color is window/level and chosen lookup table,i don’t known what the color represent in the dti model.</p>

---

## Post #14 by @lassoan (2022-09-16 03:47 UTC)

<p>It may not be that important to reproduce the exact same colors. If you do want to reproduce exactly the same colors then you need to convert the color table from the text format that Slicer uses into the XML format that is used in MITK; and get the displayed scalar range from the Slicer scene (it is in the model display node) and save it in the MITK properties file.</p>

---

## Post #15 by @jay1987 (2022-09-16 05:13 UTC)

<p>i’am agreed with you<br>
we will try these method you mentioned above,thank you very much</p>

---
