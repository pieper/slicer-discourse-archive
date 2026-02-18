# Slicer v. 5.6.0. Radiomics-module error while extracting features?

**Topic ID**: 33280
**Date**: 2023-12-07
**URL**: https://discourse.slicer.org/t/slicer-v-5-6-0-radiomics-module-error-while-extracting-features/33280

---

## Post #1 by @Magnus (2023-12-07 08:23 UTC)

<p>Hello,</p>
<p>Updated slicer to the latest version (5.6.0). Now I get an error while trying to extract radiomic features using the Radiomics module. See following error message. What can I do?</p>
<p>[2023-12-07 09:15:38] I: radiomics.script: Starting PyRadiomics (version: v3.1.0)<br>
[2023-12-07 09:15:38] I: radiomics.script: Processing input…<br>
[2023-12-07 09:15:38] E: radiomics.script: Error extracting features!<br>
Traceback (most recent call last):<br>
File “C:\Users\magnu\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts_<em>init</em>_.py”, line 135, in run<br>
results = self.<em>processCases(caseGenerator)<br>
File "C:\Users\magnu\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts_<em>init</em></em>.py", line 233, in _processCases<br>
setting_overrides = self.<em>parseOverrides()<br>
File "C:\Users\magnu\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts_<em>init</em></em>.py", line 353, in _parseOverrides<br>
settingsSchema = yaml.safe_load(schema)[‘mapping’][‘setting’][‘mapping’]<br>
File “C:\Users\magnu\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\ruamel\yaml\main.py”, line 1105, in safe_load<br>
error_deprecation(‘safe_load’, ‘load’, arg=“typ=‘safe’, pure=True”)<br>
File “C:\Users\magnu\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\ruamel\yaml\main.py”, line 1037, in error_deprecation<br>
raise AttributeError(s)<br>
AttributeError:<br>
“safe_load()” has been removed, use</p>
<p>yaml = YAML(typ=‘safe’, pure=True)<br>
yaml.load(…)</p>
<p>instead of file “C:\Users\magnu\AppData\Local\slicer.org\Slicer 5.6.0\slicer.org\Extensions-32390\SlicerRadiomics\Lib\site-packages\radiomics\scripts_<em>init</em>_.py”, line 353</p>
<pre><code>  settingsSchema = yaml.safe_load(schema)['mapping']['setting']['mapping']
</code></pre>

---

## Post #2 by @pieper (2023-12-07 12:25 UTC)

<p>Thanks for reporting - the same issue is being tracked here with a proposed change.  Maybe you could test the fix?</p>
<aside class="onebox githubpullrequest" data-onebox-src="https://github.com/AIM-Harvard/pyradiomics/pull/857">
  <header class="source">

      <a href="https://github.com/AIM-Harvard/pyradiomics/pull/857" target="_blank" rel="noopener">github.com/AIM-Harvard/pyradiomics</a>
  </header>

  <article class="onebox-body">
    <div class="github-row">



    <div class="github-icon-container" title="Pull Request">
      <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
    </div>

  <div class="github-info-container">



      <h4>
        <a href="https://github.com/AIM-Harvard/pyradiomics/pull/857" target="_blank" rel="noopener">SafeLoadRemove Error in Slicer</a>
      </h4>

    <div class="branches">
      <code>AIM-Harvard:master</code> ← <code>DanXieJY:SafeLoadRemove</code>
    </div>

      <div class="github-info">
        <div class="date">
          opened <span class="discourse-local-date" data-format="ll" data-date="2023-12-06" data-time="19:28:57" data-timezone="UTC">07:28PM - 06 Dec 23 UTC</span>
        </div>

        <div class="user">
          <a href="https://github.com/DanXieJY" target="_blank" rel="noopener">
            <img alt="DanXieJY" src="https://avatars.githubusercontent.com/u/113625444?v=4" class="onebox-avatar-inline" width="20" height="20">
            DanXieJY
          </a>
        </div>

        <div class="lines" title="1 commits changed 1 files with 3 additions and 1 deletions">
          <a href="https://github.com/AIM-Harvard/pyradiomics/pull/857/files" target="_blank" rel="noopener">
            <span class="added">+3</span>
            <span class="removed">-1</span>
          </a>
        </div>
      </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">I recently found the SlicerRadiomics extension does not work in 3D Slicer and be<span class="show-more-container"><a href="https://github.com/AIM-Harvard/pyradiomics/pull/857" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">low is the issue that I decribed in.
https://github.com/AIM-Harvard/SlicerRadiomics/issues/80

I tried to modify the code with the help of @pieper :
1. Add the code below to the top of the file:
`from ruamel.yaml import YAML`
2. Add the code below before line 353:
`yaml = YAML(typ='safe', pure=True) `
3. Change what was in line 353 to:
`settingsSchema = yaml.load(schema)['mapping']['setting']['mapping']`</span></p>
  </div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Magnus (2023-12-07 13:08 UTC)

<p>Thank you. Good to know it might not be my fault.</p>

---

## Post #4 by @Magnus (2023-12-07 13:41 UTC)

<p>However, I will have to wait for a fix, since I can’t edit any sourcecode myself (if I understood the fix correctly).</p>

---

## Post #5 by @Magnus (2023-12-07 14:06 UTC)

<p>I can extract the features when not specifying the binWidth or binCount in the settings, when running pyradiomics from the command-prompt. However it returns a lot of 0 or 1 indicating problems with the binWidth, but when I try to change the size or count of the bin, it returns the above mentioned error.</p>

---

## Post #6 by @pieper (2023-12-07 14:26 UTC)

<p>If you aren’t able to apply/test the fix, you should be able to use older versions of Slicer and SlicerRadiomics.</p>

---
