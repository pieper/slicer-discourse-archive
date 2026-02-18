# Submillimetric COVID-19 CT dataset and automatic lung tissue labeling extension

**Topic ID**: 16007
**Date**: 2021-02-16
**URL**: https://discourse.slicer.org/t/submillimetric-covid-19-ct-dataset-and-automatic-lung-tissue-labeling-extension/16007

---

## Post #1 by @PaoloZaffino (2021-02-16 10:23 UTC)

<p>Hi all,<br>
I apologize if I’m posting in the wrong section (if so please remove/move this post).</p>
<p>We just released a free (non commercial use) dataset made of 62 submillimetric CT scans of COVID-19 positive patients.<br>
Automatic lung tissue labeling and human-based clinical score are provided as well.<br>
Maybe in this difficult historical period, this dataset can be useful for your research.</p>
<p>Here the article:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.mdpi.com/2306-5354/8/2/26">
  <header class="source">

      <a href="https://www.mdpi.com/2306-5354/8/2/26" target="_blank" rel="noopener nofollow ugc">MDPI</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:550/413;"><img src="https://www.mdpi.com/bioengineering/bioengineering-08-00026/article_deploy/html/images/bioengineering-08-00026-ag-550.jpg" class="thumbnail" width="550" height="413"></div>

<h3><a href="https://www.mdpi.com/2306-5354/8/2/26" target="_blank" rel="noopener nofollow ugc">An Open-Source COVID-19 CT Dataset with Automatic Lung Tissue Classification...</a></h3>

  <p>The coronavirus disease 19 (COVID-19) pandemic is having a dramatic impact on society and healthcare systems. In this complex scenario, lung computerized tomography (CT) may play an important prognostic role. However, datasets released so far present...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>My 2 cents.</p>
<p>Paolo</p>

---

## Post #2 by @Justin (2021-02-19 14:59 UTC)

<p>Dear Paolo,</p>
<p>That is great, thanks for your contribution.</p>
<p>Are there other clinical data such as survival outcomes, ICU admission or other (anonymized) data available as well?</p>
<p>Best,<br>
Justin</p>

---

## Post #3 by @rbumm (2021-02-19 19:39 UTC)

<p>Hi Paolo,</p>
<p>Thank you, this looks like an amazing source.</p>
<p>We recently developed a Lung CT Analyzer extension for 3D Slicer for COVID-19 assessments. It can be installed within Slicer from the extension manager.</p>
<p>The sources can be pull from here: <a href="https://github.com/rbumm/SlicerLungCTAnalyzer" class="inline-onebox" rel="noopener nofollow ugc">GitHub - rbumm/SlicerLungCTAnalyzer: This is a 3D Slicer extension for segmentation and spatial reconstruction of infiltrated, collapsed, and emphysematous areas in chest CT examinations.</a></p>
<p>We will definitely check out your data, comments and ideas for the extension are always welcome !</p>
<p>Best regards</p>
<p>Rudolf Bumm, Chur, Switzerland</p>

---

## Post #4 by @PaoloZaffino (2021-02-22 11:12 UTC)

<p>Thanks <a class="mention" href="/u/justin">@Justin</a> !<br>
We are trying to retrive these data, but I can not promise anything.</p>
<p><a class="mention" href="/u/rbumm">@rbumm</a> I saw your extension…that’s really great!<br>
The aim of our paper was to release high quality images (on internet a lot of people published png-like images…) alongside with some clinical data and a way to automatically get some labels from CTs.<br>
Let me know if I can provide additional information (as already said we are trying to retrive additional clinical information).</p>
<p>Best,<br>
Paolo</p>

---

## Post #5 by @rbumm (2021-02-22 14:37 UTC)

<p>I would be very interested in how the community could help to enlarge the dataset.</p>

---

## Post #6 by @PaoloZaffino (2021-08-30 20:46 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> do you think it would be interesting for the community to have an extension that, given a chest CT, automatically labels lungs tissues on basis of the intensity (healthy, ground-glass opacities, and consolidation)?<br>
It can be used for pneumonia (COVID too).<br>
The methodology is explained in the paper linked in the first post (it’s a GMM strategy basically).</p>
<p>We could call it “Lung density segmentation”.</p>

---

## Post #7 by @lassoan (2021-08-30 23:47 UTC)

<p>Yes, sure, I expect that this would be useful. If you don’t want to create an entire new extension for this then it could be added to the LungCTAnalyzer or ChestImagingPlatform extensions.</p>

---

## Post #8 by @rbumm (2021-08-31 20:47 UTC)

<p>This sounds interesting, the LungCTAnalyzer does that to some extent, and it would be great if you could add ideas or add functionality yourself.</p>

---

## Post #9 by @PaoloZaffino (2021-09-01 09:15 UTC)

<p>I submitted a pull request.</p>

---

## Post #10 by @rbumm (2021-09-07 10:05 UTC)

<p>I added a python script</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/master/PythonScripts/processAllCTInDir.py">
  <header class="source">

      <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/master/PythonScripts/processAllCTInDir.py" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/master/PythonScripts/processAllCTInDir.py" target="_blank" rel="noopener nofollow ugc">rbumm/SlicerLungCTAnalyzer/blob/master/PythonScripts/processAllCTInDir.py</a></h4>


    <pre><code class="lang-py"># Windows: Open slicer and enter the command to call this script (me) 
# exec(open(r"C:\Users\Yourname\Documents\MySlicerExtensions\LungCTAnalyzer\PythonScripts\processAllCTInDir.py").read())


"""
      ProcessAllCtInDir
      
      Purpose: 
      Run this script to search a directory for CT data sets according the 
      data structure suggested by @PaoloZaffino,   
      automatically run LungCTAnalyzer on them and save the results.
      
      Prerequisites:
      - Each CT data set needs to be placed in a subdirectory "Pat x" where x is an integer
      - input volumes need to be present in each dir and named as follows: 
              "CT.nrrd", "CT_followup.nrrd", "CT_followup2.nrrd", "CT_followup3.nrrd" 
      - lung masks need to be prepated in each dir with LungCTSegmenter and named:                                                                            
             "LungMasksCT.seg.nrrd","LungMasksCTFollowup.seg.nrrd","LungMasksCTFollowup2.seg.nrrd","LungMasksCTFollowup3.seg.nrrd"
      - Up to three follow up CT's are supported
      - results will be saved as CSV to "results.csv" 
</code></pre>


  This file has been truncated. <a href="https://github.com/rbumm/SlicerLungCTAnalyzer/blob/master/PythonScripts/processAllCTInDir.py" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>on the LungCTAnalyzer GitHub that allows analyzing all of your 62 datasets in a row in ~60 minutes (gaming laptop).</p>
<p>As a prerequisite, lung masks have to be prepared once for every CT.</p>

---

## Post #11 by @rbumm (2021-09-07 11:40 UTC)

<p>My results of the initial CT’s of all 50 cases are summarized in this google spreadsheet:</p>
<aside class="onebox googledocs" data-onebox-src="https://docs.google.com/spreadsheets/d/1cuZdf1r9Lel4Az3787syDSvQ-C9igWDElcVOhbDjIco/edit?usp=sharing">
  <header class="source">

      <a href="https://docs.google.com/spreadsheets/d/1cuZdf1r9Lel4Az3787syDSvQ-C9igWDElcVOhbDjIco/edit?usp=sharing" target="_blank" rel="noopener nofollow ugc">docs.google.com</a>
  </header>

  <article class="onebox-body">
    <a href="https://docs.google.com/spreadsheets/d/1cuZdf1r9Lel4Az3787syDSvQ-C9igWDElcVOhbDjIco/edit?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-sheets-logo"></span></a>

<h3><a href="https://docs.google.com/spreadsheets/d/1cuZdf1r9Lel4Az3787syDSvQ-C9igWDElcVOhbDjIco/edit?usp=sharing" target="_blank" rel="noopener nofollow ugc">LCTA on Submillimetric COVID-19 dataset by PaoloZaffino</a></h3>

<p>Tabellenblatt1

clinical score,scanner,sex,user1,user2,user3,func+aff ml,inflated ml,inflated %,emphysema ml,emphysema %,infiltrated ml,infiltrated %,collapsed ml,collapsed %,affected ml,affected %,right func+aff ml,right inflated ml,right inflated...</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Thresholds:<br>
logic.setDefaultThresholds(-1050,-990,-650,-400,0,3000)</p>
<p>Without knowing any clinical details on the patients, LTCA predicts a severe clinical course (20-50% affected lung) in</p>

<p>D:/Patients5\45\CT.nrrd<br>
D:/Patients5\46\CT.nrrd<br>
D:/Patients5\7\CT.nrrd<br>
D:/Patients\35\CT.nrrd<br>
D:/Patients\33\CT.nrrd<br>
D:/Patients\15\CT.nrrd<br>
D:/Patients5\47\CT.nrrd<br>
D:/Patients\40\CT.nrrd<br>
D:/Patients\37\CT.nrrd<br>
D:/Patients\3\CT.nrrd<br>
D:/Patients\4\CT.nrrd<br>
D:/Patients\12\CT.nrrd<br>
D:/Patients\29\CT.nrrd</p>
<p>and a fatal one (&gt; 50 % affected lung) in</p>
<p>D:/Patients\10\CT.nrrd<br>
D:/Patients\14\CT.nrrd</p>

---

## Post #12 by @PaoloZaffino (2021-09-15 12:31 UTC)

<p>Dear all,<br>
today I updated our <a href="https://www.imagenglab.com/newsite/covid-19/" rel="noopener nofollow ugc">COVID-19 database</a>.<br>
Now it is made of 81 patients (in total 93 CTs since some patients have follow-up scan) and information about intensive care unit were added as well.</p>
<p><a class="mention" href="/u/rbumm">@rbumm</a> <a class="mention" href="/u/justin">@Justin</a></p>
<p>HTH,<br>
Paolo.</p>

---

## Post #13 by @rbumm (2021-09-20 12:38 UTC)

<p>Very interesting <a class="mention" href="/u/paolozaffino">@PaoloZaffino</a>  - would it be possible to add mortality data too?<br>
Thank you<br>
Best regards<br>
Rudolf</p>

---

## Post #14 by @PaoloZaffino (2021-09-20 14:51 UTC)

<p>Not easy to get, but I’ll do my best.</p>
<p>Paolo</p>

---
