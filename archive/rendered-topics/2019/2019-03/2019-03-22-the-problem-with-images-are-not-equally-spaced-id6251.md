---
topic_id: 6251
title: "The Problem With Images Are Not Equally Spaced"
date: 2019-03-22
url: https://discourse.slicer.org/t/6251
---

# The problem with images are not equally spaced

**Topic ID**: 6251
**Date**: 2019-03-22
**URL**: https://discourse.slicer.org/t/the-problem-with-images-are-not-equally-spaced/6251

---

## Post #1 by @Burak_Furkan_Kose (2019-03-22 22:58 UTC)

<p>Hi,<br>
I was trying to import patient image then i got a warning and it says “Images are not equally spaced (a difference of -0,4375 vs 1 in spacing was detected). If loaded image appears distorted, enable “Acquisition geometry regularization” in Aplication settings …”. Even tho i enabled that option when i press load, this time i get " Could not load: 001001002: Unnamed series as a Scalar Volume" error. I am new to the program and i looked at other topics aswell but unfotunately i could not find a working solution for my problem. I will be realy happy if you can help me with my problem.</p>
<p>Many thanks!</p>

---

## Post #2 by @lassoan (2019-03-22 23:02 UTC)

<p>Most probably the input data set is corrupted. Where did you get the data from? Are there any errors in the application log?</p>
<p>Try the steps described here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#I_try_to_import_a_directory_of_DICOM_files.2C_but_nothing_shows_up_in_the_browser" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#I_try_to_import_a_directory_of_DICOM_files.2C_but_nothing_shows_up_in_the_browser</a></p>

---

## Post #3 by @Burak_Furkan_Kose (2019-03-23 12:06 UTC)

<p>First of all thank you for replying my topic,</p>
<p>Secondly kinda find a solution to my problem. After i changed some of the settings by following the steps from the link you gave the program start giving me errors like “the plugin could not working” or something like that. Since i got this type of problem with other programs aswell before, i created a new user in windows that’s name doesnt contains letters like" ö,ç,ğ" so it work for now. I still get “images are not equally spaced” error when i click examine in advanced section however now i can see the image.</p>

---
