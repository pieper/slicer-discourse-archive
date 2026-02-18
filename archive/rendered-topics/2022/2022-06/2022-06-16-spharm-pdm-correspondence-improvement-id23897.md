# SPHARM PDM Correspondence improvement

**Topic ID**: 23897
**Date**: 2022-06-16
**URL**: https://discourse.slicer.org/t/spharm-pdm-correspondence-improvement/23897

---

## Post #1 by @lili-yu22 (2022-06-16 04:09 UTC)

<p>Slicer salt3.0，windows10<br>
when I use“ spharm-pdm correspondence improvement ”the python show  "OSError：Invalid argument：“C：//users//…//2022—06—16T11:51:18.762701.csv”.<br>
the input models directory: i use the*SPHARM.vtk.<br>
the input fiducial files directory :i use the makeup model to define the landmark on the "SPHARM.vtk"model<br>
Common unit sphere directory：i use only one “para.vtk”file<br>
can anyone tell me what’s wrong，thank you</p>

---

## Post #2 by @SAO (2022-07-20 12:19 UTC)

<p>Hello everyone.</p>
<p><strong>I am facing the same issue - unfortunately.</strong><br>
Currently, I am using SlicerSALT software version 3.0.0-2022 - GUI. Operating system: Windows 10</p>
<p>I have already generated the correspondence for all shapes; however, further improvement to the correspondence is needed before running “Covariant significant testing” and “Population Analysis” modules.</p>
<p>After uploading the required material into the <em>SPHARM PDM Correspondence improvement module</em> [I got no response - and no error message].</p>
<p><strong>The material uploaded into the "<em>SPHARM PDM Correspondence improvement" module</em> include:</strong></p>
<pre><code>*Input models directory*: all models with *SPHARM.vtk extension.
*Input fiducial files directory*: I used the markeup module along with ALPACA module to automate the process of generating of landmarks for "SPHARM.vtk" models in my sample. The landmark files was saved as (.FCSV file).
*Common unit sphere directory*：I used one of the “para.vtk” file generated after running the SPHARM-PDM generator module.
</code></pre>
<p>It will be helpful if someone can share with us his knowledge regarding this pipeline, and how to correct it.</p>
<p>Thanks in advance.</p>

---

## Post #3 by @bpaniagua (2022-07-20 12:25 UTC)

<p><a class="mention" href="/u/connor-bowley">@Connor-Bowley</a> could you please take a look into this problem? Thank you!</p>

---

## Post #4 by @Connor-Bowley (2022-07-20 12:43 UTC)

<p>I will look into this, but I may not have something until next week.</p>

---

## Post #5 by @SAO (2022-07-20 12:48 UTC)

<p>Thanks for your prompt response <a class="mention" href="/u/bpaniagua">@bpaniagua</a> and <a class="mention" href="/u/connor-bowley">@Connor-Bowley</a>.</p>

---

## Post #6 by @Connor-Bowley (2022-07-26 21:00 UTC)

<p>Still looking into this, but I noticed the tutorial wasn’t linked properly. There is a tutorial <a href="https://bit.ly/2WsFiun" rel="noopener nofollow ugc">here</a> that may be of some use.</p>

---

## Post #7 by @Connor-Bowley (2022-07-27 20:42 UTC)

<p>I have found and fixed a couple problems with this module on Windows and am working to get the fixes into the mainline SlicerSALT build.</p>
<p>Next steps (for me):</p>
<ol>
<li>Pull request into RigidAlignment: <a href="https://github.com/NIRALUser/RigidAlignment/pull/8" class="inline-onebox" rel="noopener nofollow ugc">Run on windows by Connor-Bowley · Pull Request #8 · NIRALUser/RigidAlignment · GitHub</a>
</li>
<li>Open a pull request into <a href="https://github.com/NIRALUser/GROUPS" rel="noopener nofollow ugc">GROUPS</a> with the branch <a href="https://github.com/Connor-Bowley/GROUPS/tree/run-on-windows" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Connor-Bowley/GROUPS at run-on-windows</a>, updated to to include the RigidAlignment change</li>
<li>Open a pull request into <a href="https://github.com/Kitware/SlicerSALT" rel="noopener nofollow ugc">SlicerSALT</a> with the updates from above.</li>
</ol>

---

## Post #8 by @SAO (2022-08-01 14:33 UTC)

<p>Thanks for your informative feedback <a class="mention" href="/u/connor-bowley">@Connor-Bowley</a>.</p>
<p>Additionally, I also noticed that “Correspondance Improvment” section in the <em>SHARM-PDM Generator</em> module is not working properly even after uploading the required material !</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d16fab4bd0f498ef5421561ab1576afd40d4579b.jpeg" data-download-href="/uploads/short-url/tSL2yQcNCNTU6o4qoh3ZFNAXtxx.jpeg?dl=1" title="Screenshot (668)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d16fab4bd0f498ef5421561ab1576afd40d4579b_2_388x500.jpeg" alt="Screenshot (668)" data-base62-sha1="tSL2yQcNCNTU6o4qoh3ZFNAXtxx" width="388" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d16fab4bd0f498ef5421561ab1576afd40d4579b_2_388x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d16fab4bd0f498ef5421561ab1576afd40d4579b_2_582x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d16fab4bd0f498ef5421561ab1576afd40d4579b.jpeg 2x" data-dominant-color="373735"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot (668)</span><span class="informations">765×984 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>We will be able to proceed with our data processing - using SlicerSALT modules - in Windows - once these issues is fixed. Hopefully soon.</p>
<p>Thanks again for your hard work.</p>

---

## Post #9 by @Connor-Bowley (2022-09-16 13:01 UTC)

<p>I opened the following pull request into the SlicerSALT repo that should fix this problem.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Kitware/SlicerSALT/pull/278">
  <header class="source">

      <a href="https://github.com/Kitware/SlicerSALT/pull/278" target="_blank" rel="noopener nofollow ugc">github.com/Kitware/SlicerSALT</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Kitware/SlicerSALT/pull/278" target="_blank" rel="noopener nofollow ugc">Groups windows fix</a>
    </h4>

    <div class="branches">
      <code>Kitware:master</code> ← <code>Connor-Bowley:groups-windows-fix</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2022-09-16" data-time="12:59:49" data-timezone="UTC">12:59PM - 16 Sep 22 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/Connor-Bowley" target="_blank" rel="noopener nofollow ugc">
          <img alt="Connor-Bowley" src="https://avatars.githubusercontent.com/u/14840636?v=4" class="onebox-avatar-inline" width="20" height="20">
          Connor-Bowley
        </a>
      </div>

      <div class="lines" title="2 commits changed 1 files with 2 additions and 2 deletions">
        <a href="https://github.com/Kitware/SlicerSALT/pull/278/files" target="_blank" rel="noopener nofollow ugc">
          <span class="added">+2</span>
          <span class="removed">-2</span>
        </a>
      </div>
    </div>
  </div>
</div>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #10 by @Connor-Bowley (2022-09-20 15:32 UTC)

<p>This issue should be fixed in <code>SlicerSALT-3.0.0-2022-09-16</code> which can be downloaded by going to <a href="http://salt.slicer.org/download/" class="inline-onebox" rel="noopener nofollow ugc">Download • SlicerSALT</a>, clicking <code>Visit Girder -&gt; Nightly -&gt; SlicerSALT-3.0.0-2022-09-16-win-amd64.exe</code>. Please try it out and let me know if you are still having problems.</p>

---

## Post #11 by @SAO (2022-11-01 05:50 UTC)

<p>Thanks alot for your hard work <a class="mention" href="/u/connor-bowley">@Connor-Bowley</a><br>
I will use SlicerSALT (latest version), and let you know if there is a problem.</p>

---

## Post #12 by @Hoai-Nam_Bui (2023-01-16 21:37 UTC)

<p>Hello!</p>
<p><a class="mention" href="/u/sao">@SAO</a> I was wondering if you were able to get your Correspondence improvement module to work with the latest version of SlicerSalt? It seems I am running into a problem similar to yours.</p>
<p>I have about 50 shapes but was forerunning with two to figure out the workflow.</p>
<p>I pathed:</p>
<p>Input Models Directory: a folder with the 2 models with the vtk extension<br>
Fiducial files directory: a folder with 2 separate fcsv’s (should I be merging them?)<br>
Common unit sphere: a folder with one of the para.vtk files</p>
<p>Upon running, I also get no response nor an error message. I’m wondering if I need to format/name the fcsv’s with the same name as my models? Or change something within the file itself?</p>
<p>I’ve also been using the tutorial that <a class="mention" href="/u/connor-bowley">@Connor-Bowley</a> had linked above. Thank you!</p>

---

## Post #13 by @SAO (2023-01-18 08:12 UTC)

<p>Dear  <a class="mention" href="/u/connor-bowley">@Connor-Bowley</a>, <a class="mention" href="/u/hoai-nam_bui">@Hoai-Nam_Bui</a>, and <a class="mention" href="/u/bpaniagua">@bpaniagua</a>,<br>
I hope you all doing well.</p>
<p>Actually, I am still facing the same issue - even with the latest version of <a href="https://discourse.slicer.org/t/slicersalt-4-0-1-summary-highlights-and-changelog/26197">SlicerSALT 4.0.1</a>.</p>
<p><strong>After uploading the required material [I got no response - and no error message].</strong></p>
<p>I agree with you that there is a need for detailed-tutorial, with a case, that outline the pipeline for the “correspondence improvement module”.</p>
<p>All the best.</p>
<p>Regards,<br>
Sultan</p>

---

## Post #14 by @Connor-Bowley (2023-01-18 16:44 UTC)

<p>So I am looking into this again and have found a problem which I am looking into resolving. The problem did not occur on my original data I was using to test the module because that data was generated with an old version of SALT.</p>
<p>Hopefully I will have a resolution in the next couple of days.</p>

---

## Post #15 by @Connor-Bowley (2023-01-23 22:29 UTC)

<p>I have a fix and have the started the work to integrate it into SlicerSALT. In short, there was a bug when reading the newer file format verison for <code>.vtk</code> files. My data I used to test during the original fix was an old enough version of the <code>.vtk</code> format that it didn’t cause the problem.</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/NIRALUser/GROUPS/pull/41">
  <header class="source">

      <a href="https://github.com/NIRALUser/GROUPS/pull/41" target="_blank" rel="noopener nofollow ugc">github.com/NIRALUser/GROUPS</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/NIRALUser/GROUPS/pull/41" target="_blank" rel="noopener nofollow ugc">BUG: Fix running with new vtk files</a>
      </h4>

    <div class="branches">
      <code>NIRALUser:master</code> ← <code>Connor-Bowley:fix-newer-vtk-file-versions</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-01-23" data-time="22:26:26" data-timezone="UTC">10:26PM - 23 Jan 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/Connor-Bowley" target="_blank" rel="noopener nofollow ugc">
            <img alt="Connor-Bowley" src="https://avatars.githubusercontent.com/u/14840636?v=4" class="onebox-avatar-inline" width="20" height="20">
            Connor-Bowley
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 4 additions and 3 deletions">
          <a href="https://github.com/NIRALUser/GROUPS/pull/41/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+4</span>
            <span class="removed">-3</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">Updates MeshLib to version that fixes a bug where newer .vtk files would be read<span class="show-more-container"><a href="https://github.com/NIRALUser/GROUPS/pull/41" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden"> incorrectly, causing a segfault in RigidAlignment.

Pointing this to the new slicersalt fork of MeshLib so we can get this fix into SALT while https://github.com/ilwoolyu/MeshLib/issues/12 is being sorted out.

cc @vicory</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #16 by @Connor-Bowley (2023-01-25 13:32 UTC)

<p>Found another small bug that is working its way through reviews. Will let you know when everything is through and SALT gets updated.</p>
<p>To answer some questions <a class="mention" href="/u/hoai-nam_bui">@Hoai-Nam_Bui</a> asked about naming:</p>
<p>When using the SPHARM-PDM Correspondence Improvement module:</p>
<ul>
<li>The models <strong>must</strong> be named <code>&lt;some-name&gt;_pp_surf_SPHARM.vtk</code>
</li>
<li>The corresponding fiducials <strong>must</strong> be named <code>&lt;some-name&gt;_fid.fcsv</code>
</li>
<li>The spheres folder only needs 1 sphere and it <strong>must</strong> be named <code>&lt;something&gt;_surf_para.vtk</code>
</li>
</ul>
<p>The <code>&lt;some-name&gt;</code> for a model and its corresponding fiducial should match exactly.<br>
(e.g. <code>subject1_pp_surf_SPHARM.vtk</code> and <code>subject1_fid.fcsv</code>)</p>
<p>The <code>&lt;something&gt;</code> for the sphere is not required to match any of the <code>&lt;some-name&gt;</code>s.</p>
<p>When using SPHARM-PDM / Shape Analysis Module with the <code>Correspondence Improvement -&gt; Enable Correspondence Improvement</code> checkbox checked, SPHARM will make sure the models and sphere are named correctly, you just need to worry about the fiducials.</p>
<p>The tutorial is definitely not clear about this. I had to go look at the <a href="https://github.com/NIRALUser/GROUPS/blob/71daa95a831e35b3995db64a82a2c7f8646c9148/Modules/Scripted/RigidAlignmentModule/RigidAlignmentModule.py#L101-L103" rel="noopener nofollow ugc">source code</a> to understand the naming requirements. I think the assumption is because SPHARM outputs the files in this way and this is SPHARM correspondence improvement the files should just be named appropriately. I have added <a href="https://github.com/NIRALUser/GROUPS/issues/43" rel="noopener nofollow ugc">this issue</a> to track this problem.</p>

---

## Post #17 by @Connor-Bowley (2023-01-27 14:10 UTC)

<p>The bugs were fixed and those fixes are incorporated in the latest nightly build of SlicerSALT, SlicerSALT-4.0.1-2023-01-25, which can be found on Girder <a href="https://data.kitware.com/#collection/586fbb7b8d777f05f44a5c7b/folder/5bd85a568d777f06b9402dad" rel="noopener nofollow ugc">here</a>.</p>
<p><a class="mention" href="/u/hoai-nam_bui">@Hoai-Nam_Bui</a> <a class="mention" href="/u/sao">@SAO</a> Please try downloading this updated version of SALT and see if it works for your data (keeping the naming requirements detailed above in mind). If it does not work, please go to the “SPHARM-PDM Generator” module, click <code>Tutorials -&gt; Correspondence Improvement (this will download sample data) -&gt; Run ShapeAnalysisModule</code> let run (it may take ~45 minutes) and see if produces any errors.</p>
<p>For reference, here is the pull request bringing the fixes into SALT:</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/Kitware/SlicerSALT/pull/292">
  <header class="source">

      <a href="https://github.com/Kitware/SlicerSALT/pull/292" target="_blank" rel="noopener nofollow ugc">github.com/Kitware/SlicerSALT</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/Kitware/SlicerSALT/pull/292" target="_blank" rel="noopener nofollow ugc">BUG: Update GROUPS</a>
      </h4>

    <div class="branches">
      <code>Kitware:master</code> ← <code>Connor-Bowley:fix-groups-bugs</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-01-25" data-time="13:54:10" data-timezone="UTC">01:54PM - 25 Jan 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/Connor-Bowley" target="_blank" rel="noopener nofollow ugc">
            <img alt="Connor-Bowley" src="https://avatars.githubusercontent.com/u/14840636?v=4" class="onebox-avatar-inline" width="20" height="20">
            Connor-Bowley
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 1 additions and 1 deletions">
          <a href="https://github.com/Kitware/SlicerSALT/pull/292/files" target="_blank" rel="noopener nofollow ugc">
            <span class="added">+1</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">GROUPS changes: git shortlog --no-merges 1263afc12..387bc83ad

Connor Bowley (<span class="show-more-container"><a href="https://github.com/Kitware/SlicerSALT/pull/292" target="_blank" rel="noopener nofollow ugc" class="show-more">…</a></span><span class="excerpt hidden">2):
      BUG: Fix running with new vtk files
      BUG: Update RigidAlignment</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #18 by @SAO (2023-01-29 04:31 UTC)

<p>Thanks for your hard work <span class="mention">@Connor-Bowley.Your</span> informative response is highly appreciated.<br>
I will download the updated version of SALT(SlicerSALT-4.0.1-2023-01-25), and see if it works for my data, soon.</p>
<p>All the best to everyone.</p>
<p>Regards,<br>
Sultan</p>

---

## Post #19 by @Hoai-Nam_Bui (2023-02-05 18:17 UTC)

<p>Hi <a class="mention" href="/u/connor-bowley">@Connor-Bowley</a>, thanks so much for your hard work. I believe your fixes are running successfully!</p>
<p>I have a relatively large sample to align, but here are the results of two shapes with 9 landmarks.<br>
I was hoping that 9 landmarks would be sufficient but I am assuming that due to their non-aligned alignment that I most likely need more? Your thoughts would be greatly appreciated!</p>
<p>Thanks again for everything.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21f3df22c9b1b57df433dd63fe8abba354b4f75a.jpeg" data-download-href="/uploads/short-url/4Qmfrqx7cGxqJmYsPRVDnqaXd9M.jpeg?dl=1" title="Screenshot 2023-02-05 at 1.14.05 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21f3df22c9b1b57df433dd63fe8abba354b4f75a_2_690x367.jpeg" alt="Screenshot 2023-02-05 at 1.14.05 PM" data-base62-sha1="4Qmfrqx7cGxqJmYsPRVDnqaXd9M" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21f3df22c9b1b57df433dd63fe8abba354b4f75a_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21f3df22c9b1b57df433dd63fe8abba354b4f75a_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21f3df22c9b1b57df433dd63fe8abba354b4f75a_2_1380x734.jpeg 2x" data-dominant-color="645E83"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-02-05 at 1.14.05 PM</span><span class="informations">1920×1023 94 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #20 by @Connor-Bowley (2023-02-13 16:31 UTC)

<p>Hi <a class="mention" href="/u/hoai-nam_bui">@Hoai-Nam_Bui</a>,</p>
<p><code>SPHARM-PDM Correspondence improvement</code> is a module that improves point-wise correspondence between meshes. It takes a unit sphere from the <code>SPHARM-PDM/Shape Analysis Module</code> work and rigidly aligns the sphere-mapped landmarks from each mesh onto the input sphere, and remeshes the models based on that. This has the effect of changing the point numbering and cell numbering of the different meshes to be in correspondence <em>without</em> changing the actual geometries or any of the actual point locations.</p>
<p>For doing the physical alignment after the correspondence improvement, you could take the output of the <code>SPHARM-PDM Correspondence improvement</code> and run it through something like the <code>Procrustes Registration</code> module (under <code>Shape Analysis</code>).  Note that for the <code>Procrustes Registration</code> module to work, the meshes must be in point correspondence (which they will be coming out of the <code>SPHARM-PDM Correspondence improvement</code> module).</p>
<p>I hope this helps.</p>

---

## Post #21 by @Hoai-Nam_Bui (2023-04-20 22:06 UTC)

<p>Dear <a class="mention" href="/u/connor-bowley">@Connor-Bowley</a>,<br>
I’ve been able to run both Spharm Correspondence improvement and the Procrustes registration module with 3 samples, however in my attempts to increase my sample size I am unable to attain aligned specimens. They seem to be just slightly-off from one another in terms of alignment.</p>
<p>I’m also wondering-- if I can align them manually in a separate program, is there a way to deal with scaling prior to running a PCA?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/7578ba08ffb53517259b19673bb2c75936454996.jpeg" data-download-href="/uploads/short-url/gLcwe7QeAJiCU75TZH9XlHCnr0y.jpeg?dl=1" title="Screenshot 2023-04-20 at 3.55.24 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/7578ba08ffb53517259b19673bb2c75936454996_2_690x367.jpeg" alt="Screenshot 2023-04-20 at 3.55.24 PM" data-base62-sha1="gLcwe7QeAJiCU75TZH9XlHCnr0y" width="690" height="367" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/7578ba08ffb53517259b19673bb2c75936454996_2_690x367.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/7578ba08ffb53517259b19673bb2c75936454996_2_1035x550.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/7578ba08ffb53517259b19673bb2c75936454996_2_1380x734.jpeg 2x" data-dominant-color="768189"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-04-20 at 3.55.24 PM</span><span class="informations">1920×1023 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac3c637f4daa51965ee241eaef440695649065cc.jpeg" data-download-href="/uploads/short-url/ozFvr0N1Q8tw6QKJIt44bwaqurW.jpeg?dl=1" title="Screenshot 2023-04-20 at 4.05.47 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac3c637f4daa51965ee241eaef440695649065cc_2_690x361.jpeg" alt="Screenshot 2023-04-20 at 4.05.47 PM" data-base62-sha1="ozFvr0N1Q8tw6QKJIt44bwaqurW" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac3c637f4daa51965ee241eaef440695649065cc_2_690x361.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac3c637f4daa51965ee241eaef440695649065cc_2_1035x541.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac3c637f4daa51965ee241eaef440695649065cc_2_1380x722.jpeg 2x" data-dominant-color="AEBFD9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-04-20 at 4.05.47 PM</span><span class="informations">1920×1007 115 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #22 by @lili-yu22 (2024-12-20 07:53 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/5/45ba029a73721af2f861fc4d8a9589463b484ffb.jpeg" data-download-href="/uploads/short-url/9WPtag0YhAc8D1RYNI9PMTAulQv.jpeg?dl=1" title="Screenshot_20241219_151735" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45ba029a73721af2f861fc4d8a9589463b484ffb_2_690x493.jpeg" alt="Screenshot_20241219_151735" data-base62-sha1="9WPtag0YhAc8D1RYNI9PMTAulQv" width="690" height="493" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45ba029a73721af2f861fc4d8a9589463b484ffb_2_690x493.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45ba029a73721af2f861fc4d8a9589463b484ffb_2_1035x739.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/5/45ba029a73721af2f861fc4d8a9589463b484ffb_2_1380x986.jpeg 2x" data-dominant-color="AABFBB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot_20241219_151735</span><span class="informations">1600×1144 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f85d86e5a4855b051aa1c6c5ec6be9f0bc77116c.jpeg" data-download-href="/uploads/short-url/zr8Nb8qjCQgjxK7kQ1Em401BBgg.jpeg?dl=1" title="IMG_20241220_155543_edit_8092433669597" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f85d86e5a4855b051aa1c6c5ec6be9f0bc77116c_2_384x500.jpeg" alt="IMG_20241220_155543_edit_8092433669597" data-base62-sha1="zr8Nb8qjCQgjxK7kQ1Em401BBgg" width="384" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f85d86e5a4855b051aa1c6c5ec6be9f0bc77116c_2_384x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f85d86e5a4855b051aa1c6c5ec6be9f0bc77116c_2_576x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f85d86e5a4855b051aa1c6c5ec6be9f0bc77116c_2_768x1000.jpeg 2x" data-dominant-color="B7B9B8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20241220_155543_edit_8092433669597</span><span class="informations">1920×2498 321 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>when I open a mesh.then open it’s fiducial.the slicersalt 5.0 crash.how I can put the fiducial on the mesh in the shape population viewer like the picture.please help me</p>

---

## Post #23 by @anasmh101 (2025-07-12 20:51 UTC)

<p>Hello,<br>
I’m using the latest version of SlicerSALT (version 6), but the Correspondence Improvement module isn’t responding. what could be causing this issue?</p>
<p>Thanks in Advance</p>

---

## Post #24 by @anasmh101 (2025-07-12 20:54 UTC)

<p>Hello,<br>
I just wanted to check if you’ve managed to resolve the correspondence alignment issue. Have you found a solution or workaround?</p>

---
