# Can I automate just importing files, changing their type, and then saving them?

**Topic ID**: 36501
**Date**: 2024-05-30
**URL**: https://discourse.slicer.org/t/can-i-automate-just-importing-files-changing-their-type-and-then-saving-them/36501

---

## Post #1 by @tryingToCode (2024-05-30 15:15 UTC)

<p>I am trying to write a Python script that imports .msg files into 3D Slicer and saves them as nii files. I’ve never automated anything and I am having a bit of a hard time understanding how to write scripts and run them. Thanks.</p>

---

## Post #2 by @mikebind (2024-05-30 19:51 UTC)

<p>If you don’t need to do anything interactive with the files, then you probably don’t need to load them into Slicer at all.  You might take a look at the slicerio python package and see if you can use that to just load and save the data formats you need.</p>

---

## Post #3 by @tryingToCode (2024-05-30 23:54 UTC)

<p>Thanks so much!!! I will check it out!</p>

---

## Post #4 by @tryingToCode (2024-06-03 19:41 UTC)

<p>I ended up using freesurfer’s mri_convert command and wrote a BASH script to loop through all the files in a directory and convert them. Here’s the code:</p>
<pre><code class="lang-auto">#!/bin/bash 

#ask user for filepath and change directory to filepath 
read -p "Enter filepath: " fp  
cd $fp 

#loop through files 
for FILE in * 
do 
        #seperate file extentsion and name 
        filepath="${fp}${FILE}" 
        filename_with_ext=$(basename $filepath) 
        filename="${filename_with_ext%.*}" 
        extension="${filename_with_ext##*.}" 

        #concatinate filename with new extension         
        ni_file="${filename}.nii" 

        #convert to nii using now seperated file name concaqtinated with .nii 
        mri_convert --in_type mgz --out_type nii ${FILE} ${ni_file} 
done 

 #switch back to home directory 
cd ~ 
</code></pre>

---
