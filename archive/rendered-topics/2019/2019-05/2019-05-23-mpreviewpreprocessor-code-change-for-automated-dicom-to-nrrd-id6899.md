# mpReviewPreprocessor code change for automated DICOM to NRRD conversion 

**Topic ID**: 6899
**Date**: 2019-05-23
**URL**: https://discourse.slicer.org/t/mpreviewpreprocessor-code-change-for-automated-dicom-to-nrrd-conversion/6899

---

## Post #1 by @Kramer84 (2019-05-23 16:06 UTC)

<p>Dear Dr. Fedorov and 3DSlicer support,</p>
<p>for an academic project, we are building a database out of anonymized DICOM files (only the directory of the DICOM contains information about age and sex, the metadata is not usable), and we would first have liked to convert them into easier manageable NRRD files.<br>
The Idea is to loop over all the DICOM files with the mpReviewPreprocessor in batch mode, for further batch processing with registration and segmentation.</p>
<p>I would have liked to change the code of the mpReviewPreprocessor script to use the name of the input directory to name the NRRD file by using something like:</p>
<p><code>(filepath, filename) = os.path.split(inputDir)</code><br>
<code> nrrdName = os.path.join(dirName, filename + ".nrrd")</code></p>
<p>But not being a software developper, I have still difficulties with classes methods and attributes, and even just trying to insert a string called <code>tempName</code> in the <code>convertData()</code> function to change the dir, xml and nrrd names, which could be changed by an other script later, makes the code crash.<br>
I also tried to add one more variable called inputDir in the convertData function, and all parent functions, but it made also the code unusable.<br>
I added a picture of the part of the code that I think needs to be changed for my problem, and one of my non working solution.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3f11b3636a7c8e4c2fc9d09ea0a6f91d411eb11.png" data-download-href="/uploads/short-url/pFQ2aNtNIAalZGFyYdLIxTcwEq5.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3f11b3636a7c8e4c2fc9d09ea0a6f91d411eb11_2_690x450.png" alt="image" data-base62-sha1="pFQ2aNtNIAalZGFyYdLIxTcwEq5" width="690" height="450" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b3f11b3636a7c8e4c2fc9d09ea0a6f91d411eb11_2_690x450.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3f11b3636a7c8e4c2fc9d09ea0a6f91d411eb11.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b3f11b3636a7c8e4c2fc9d09ea0a6f91d411eb11.png 2x" data-dominant-color="F6F5F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">903×590 77 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d901cb3e1845aa9dcb7778c0540db95fead40c53.png" data-download-href="/uploads/short-url/uXJsbetOS3nV8RoFTozytkOrHzB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d901cb3e1845aa9dcb7778c0540db95fead40c53_2_690x356.png" alt="image" data-base62-sha1="uXJsbetOS3nV8RoFTozytkOrHzB" width="690" height="356" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d901cb3e1845aa9dcb7778c0540db95fead40c53_2_690x356.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d901cb3e1845aa9dcb7778c0540db95fead40c53.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d901cb3e1845aa9dcb7778c0540db95fead40c53.png 2x" data-dominant-color="F6F5F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1011×522 73.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Adding the temporary file names seemed to be the easiest way to change the data tree, and after conversion to change the file names, but even after disabling everything involving the creation of the xml file the code is unable to create the nrrd.<br>
Here is the error message :<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c2c2905039d1f4286b64a24bc7b83f4815604ed.png" alt="image" data-base62-sha1="hItOMZPbFBULrjW1lU6pek2rJH7" width="637" height="265"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6dfe8b14fc426996d838b41c451c780ae432521c.png" alt="image" data-base62-sha1="fH3oQwqaYej4zdoZBSmiXAjQSPq" width="641" height="133"></p>
<p>I know I made a lot of mistakes trying to modify the script nor had I respect to the art of writing good code, but I would be really greatfull if  you could help me out on this issue.</p>
<p>I thank you in advance,</p>
<p>Kristof S.</p>

---

## Post #2 by @fedorov (2019-05-23 17:21 UTC)

<p>Kristof, does it work for your data if you do not change anything at all in the code?</p>
<p>There are multiple issues with using Slicer for generating volume-reconstructed files in batch mode: indexing the database and running DICOM plugins is slow, with the current code, if one series fails, it is not easy to track down what happened. I ran into those issues again for the latest project where I was using this code, and am now thinking to explore switching to <a href="https://github.com/rordenlab/dcm2niix" rel="nofollow noopener">dcm2niix</a> for volume reconstruction (at least for scalar volumes, if not multivolumes). The idea is to leave mpReviewPreprocessor as is, but add an option to use dcm2niix in place of the DICOM scalar volume plugin (and perhaps avoid indexing the data into the database, hopefully eventually cutting the dependency on the Slicer application for this task).</p>
<p>I have multiple deadlines this week, and I am traveling next week, but I will look into this hopefully sometime soon.</p>
<p>If you want to explore the use of dcm2niix in this script for generating the reconstructed volumes, your contributions are most welcomed!</p>

---

## Post #3 by @Kramer84 (2019-05-24 06:44 UTC)

<p>Dr. Fedorov, thank you very much for your answer.</p>
<p>Yes, the code is working when I leave it as it was, and I tried it again after cleaning up the code involved in the creation of the xml file and fixing some of my syntax errors it seems to generate working NRRD files even with the error message.<br>
But as you warned me about the potential issues involved in the use of mpReviewPreprocessor and it’s relative slowness I will follow your advice and explore dcm2niix.</p>
<p>This project will last a few more month, so there will be time to explore, understand and maybe contribute some code if the project is viable.</p>

---

## Post #4 by @fedorov (2019-05-29 16:55 UTC)

<p><a class="mention" href="/u/kramer84">@Kramer84</a> I added mpReviewPreprocessor2 script, which assumes the data was first sorted using <a href="https://github.com/pieper/dicomsort" rel="nofollow noopener">dicomsort</a> into the hierarchy used by mpReview, and then uses dcm2niix for generating volume reconstructions in NIfTI format. I also updated mpReview to recognize NIfTI files as acceptable input. This new preprocessor should be faster, a lot easier to use, and a lot easier to understand and modify.</p>
<p>One feature that is missing from the new processor at this point is that it does not process multivolumes. Slicer default volume reader is not able to read NIfTI 4d images, and so they will require special handling.</p>
<p>I committed this new code to the repo - it would be great if you could take a look, test and give feedback if it works for your data.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerProstate/mpReview/blob/master/mpReviewPreprocessor2.py" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerProstate/mpReview/blob/master/mpReviewPreprocessor2.py" target="_blank" rel="nofollow noopener">SlicerProstate/mpReview/blob/master/mpReviewPreprocessor2.py</a></h4>
<pre><code class="lang-py">'''

First sort instances with dicomsort Using

dicomsort.py -k &lt;input directory with DICOM data&gt; &lt;output directory for mpReview&gt;/%PatientID_%StudyDate_%StudyTime/RESOURCES/%SeriesNumber/DICOM/%SOPInstanceUID.dcm

Then run this script to generate volume reconstructions:

python mpReviewPreprocessor2.py -i &lt;output directory for mpReview&gt;

'''

import os, shutil, sys, subprocess, logging, glob, tqdm, argparse
import nibabel

#logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("mpReviewPreprocessor2")


def main(argv):
</code></pre>

  This file has been truncated. <a href="https://github.com/SlicerProstate/mpReview/blob/master/mpReviewPreprocessor2.py" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Kramer84 (2019-06-01 23:07 UTC)

<p><a class="mention" href="/u/fedorov">@fedorov</a> I have taken a look at the different parts of your script and the manual, and have just yet understood the way <code> mpReview</code>  works. We are actually working in the field of maxilla-cranial surgery, with head MRIs where only the skull has to be extracted, and we didn’t really bothered nor knew about multi-parametric reviewing. So at was at the beginning surprised of seeing that much variation between the number of NIfTI files in <code>Reconstructions</code>  folders. But after verification we indeed have variations in the X-Ray exposure for some MRIs.</p>
<p>Does it make a difference in the process of extracting the bones to have MRIs with different exposure? Or would it make segmentation or metallic artifact reduction easier?</p>
<p><strong>For the testing on our files on mpReviewpreprocessor2 :</strong></p>
<p>When running  <code>dicomsort</code> , as all the DICOM files are anonymized, the file path tends to be relatively unreliable, as it takes empty or encrypted metadata. But mpReviewpreprocessor 2 does convert the files in the chosen output directory in the Reconstructions folder, and constructs readable NifTI files.</p>
<p><em>Here the path organized by dicomsort and the Reconstructions folder made by mpReviewpreprocessor2:</em><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a92571641a94745aa4d12ebc2d34a5b170598f1.png" alt="image" data-base62-sha1="cVevid1mHacDIlw50IH4SE7othL" width="320" height="189"></p>
<p><em>While walking through the files I saw that indeed some of the head MRIs that were multiparametric with a separate NIfTI file for each parameter</em><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa45c0d4b195b652612eab6da4386086ed84a07f.png" alt="image" data-base62-sha1="zI0Oq8zWdwsB172N9Y9Ec3GZpEj" width="575" height="303"><br>
The way your script was working is interesting because it allows us to treat DICOMs in bulks, and so to be a first step to automate the extraction process of the skulls and metallic artifacts, so we can eliminate human input in our data and keep consistency.</p>
<p>But I also tried to use dcm2niix to make something more problem specific, as it is possible to batch convert whole DICOM directories with the  <code>dcm2niixbatch batch_config.yaml</code> command and to chose the file name in the YAML script.</p>
<p>I tried to write a function that allows me to create the  <code>batch_config.yaml</code>  file and that takes as inputs the directory containing the DICOM files and the empty directory where we want the NIfTl files to be created, also giving the name of the directory containing the DICOM images to the NIfTI files.<br>
The function also creates the new directories containing the NIfTI files, and organize the <code>batch_config.yaml</code> file.</p>
<p>After some tests, the function returned a  <code>batch_config.yaml</code>  file, and creates the empty directories for the NifTI files, but the YAML file itself has still some issues, with the inversion of the Files and Options dictionary, and bad indentation.<br>
<em>Empty directories, and non-conform yaml file:</em><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/49e2cba49db69c11bf438b55fc5e4a1882638a12.png" alt="image" data-base62-sha1="axCLgJMRIi83OsCm7S9j4y1hssi" width="317" height="77"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/726af7e9509c7504976dbb2d1a30bc2debeef243.png" alt="image" data-base62-sha1="gkbBQiwmrWHIVqPLQ7EEopFJuIr" width="291" height="223"><br>
Here is the code involved in the creation of the YAML file:</p>
<pre><code>!/usr/bin/python3
import argparse, sys, shutil, os, logging	
import ruamel.yaml as ry
from ast import literal_eval
from pathlib import Path

def batch_creator(inputDir , outputDir):
	
	#options have to be (for now) manually changed
	optionStr = "{'Options': {'isGz': False, 'isFlipY': False, 'isVerbose': False, 'isCreateBIDS': False, 'isOnlySingleFile': False},"

	#dirIn contains all the dicom files, dirOut is empty, the yaml file is created in the dirOut directory (for testing purposes)

	dirIn   = inputDir
	dirOut  = outputDir
	yamlDir = outputDir		#for testing issues the yaml file is also in the output directory

	listDicomDir = os.listdir(dirIn)
	n = len(listDicomDir)

	#FileArray represents the dictionary (in string format) that has to be further converted into yaml

	FileArray = []

	#while iterating through the whole directory containing the Dicom files, we create for each Dicom a corresponding folder @ dirOut
	for i in range (0,n): 
		tempName = listDicomDir[i]
		outPathName = dirOut+"/"+tempName+"_dcm2niix"	
		os.mkdir(Path(outPathName))  
		FileArray.extend([{'in_dir': dirIn+"/"+tempName ,'out_dir': outPathName , 'filename': tempName+"_dcm2niix" }]) #dictionary in string format
    
    
    
	
	AlmostYaml = optionStr+" 'Files':"+str(FileArray)+"}"		 #here we join the Options and Files part of the yaml file

	dict_batchFile = literal_eval(AlmostYaml)			 #this should convert the string into a python dictionary
	
	save_path = Path(yamlDir)					 #then we create the empty yaml file in the Out directory
	batch_config = open(os.path.join(save_path,"batch_config.yaml"),"w+")
	
	ry.dump(dict_batchFile,batch_config, default_flow_style=False) #and dump our finished yaml
</code></pre>
<p>I will try to find the mistakes that I made in the function and yaml syntax, and update it here later. The conversion should then be done relatively easy.</p>
<p>In the end, the database should be (it’s utopic) consistent enough to train the convolutional neural network based metal artifact reduction algorithm presented <a href="https://arxiv.org/pdf/1709.01581.pdf" rel="noopener nofollow ugc">here</a> , or to make statistical analysis on the maxillofacial framework.</p>

---

## Post #6 by @fedorov (2019-11-05 17:20 UTC)

<p><a class="mention" href="/u/kramer84">@Kramer84</a> how is your progress? Do you have any specific questions about this?</p>

---
