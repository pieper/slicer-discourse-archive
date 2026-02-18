# Slicer Preview Release package for Windows failed to upload

**Topic ID**: 20264
**Date**: 2021-10-20
**URL**: https://discourse.slicer.org/t/slicer-preview-release-package-for-windows-failed-to-upload/20264

---

## Post #1 by @lassoan (2021-10-20 14:42 UTC)

<p>If I try to download the latest Slicer Preview Release then I got an empty zip file of 22 bytes.</p>
<p>It seems that there was an <a href="https://slicer.cdash.org/viewBuildError.php?buildid=2443905">upload error</a>.</p>
<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/jcfr">@jcfr</a> Could you please have a look at this and remove the invalid file (or upload the correct file)? There are about 400 Windows downloads a day, so such an error makes many people unhappy (I already got complaints coming in).</p>
<p><strong>For people who come across this topic and need a workaround: you can download the Slicer release from the previous day using this link: <a href="https://download.slicer.org/?offset=-1">https://download.slicer.org/?offset=-1</a></strong></p>

---

## Post #2 by @Sam_Horvath (2021-10-20 14:58 UTC)

<p>I am working on getting the upload fixed</p>

---

## Post #3 by @Sam_Horvath (2021-10-20 15:07 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> This should be fixed now, can you confirm?</p>

---

## Post #4 by @lassoan (2021-10-20 15:09 UTC)

<p>It works perfectly now, thank you!</p>

---

## Post #5 by @jamesobutler (2021-10-21 11:15 UTC)

<p><a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> <a class="mention" href="/u/jcfr">@jcfr</a> There appears to be the same upload error again on the Windows platform.</p>
<p><a href="https://slicer.cdash.org/viewBuildError.php?buildid=2445193" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.cdash.org/viewBuildError.php?buildid=2445193</a></p>

---

## Post #6 by @Sam_Horvath (2021-10-21 14:25 UTC)

<p>Fixed again.  Not sure why this is happening, the extension packages are uploading fine.</p>

---

## Post #7 by @Sam_Horvath (2021-10-21 14:36 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> This seems to be some sort of interaction between the upload script and the server?  Does not happen with the extension packages.</p>
<pre><code class="lang-python">Traceback (most recent call last):
  File "c:\python36-x64\lib\runpy.py", line 193, in _run_module_as_main
    "__main__", mod_spec)
  File "c:\python36-x64\lib\runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "D:\Support\slicer_package_manager-venv\Scripts\slicer_package_manager_client.exe\__main__.py", line 7, in &lt;module&gt;
  File "d:\support\slicer_package_manager-venv\lib\site-packages\click\core.py", line 722, in __call__
    return self.main(*args, **kwargs)
  File "d:\support\slicer_package_manager-venv\lib\site-packages\click\core.py", line 697, in main
    rv = self.invoke(ctx)
  File "d:\support\slicer_package_manager-venv\lib\site-packages\click\core.py", line 1066, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "d:\support\slicer_package_manager-venv\lib\site-packages\click\core.py", line 1066, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "d:\support\slicer_package_manager-venv\lib\site-packages\click\core.py", line 895, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "d:\support\slicer_package_manager-venv\lib\site-packages\click\core.py", line 535, in invoke
    return callback(*args, **kwargs)
  File "d:\support\slicer_package_manager-venv\lib\site-packages\click\decorators.py", line 27, in new_func
    return f(get_current_context().obj, *args, **kwargs)
  File "d:\support\slicer_package_manager-venv\lib\site-packages\slicer_package_manager_client\cli.py", line 610, in _cli_uploadApplicationPackage
    pkg = sc.uploadApplicationPackage(*args, **kwargs)
  File "d:\support\slicer_package_manager-venv\lib\site-packages\slicer_package_manager_client\__init__.py", line 469, in uploadApplicationPackage
    progressCallback=_displayProgress)
  File "d:\support\slicer_package_manager-venv\lib\site-packages\girder_client\__init__.py", line 878, in uploadFileToItem
    return self._uploadContents(obj, f, filesize, progressCallback=progressCallback)
  File "d:\support\slicer_package_manager-venv\lib\site-packages\girder_client\__init__.py", line 994, in _uploadContents
    data=_ProgressBytesIO(chunk, reporter=reporter))
  File "d:\support\slicer_package_manager-venv\lib\site-packages\girder_client\__init__.py", line 479, in post
    data=data, json=json, headers=headers, jsonResp=jsonResp)
  File "d:\support\slicer_package_manager-venv\lib\site-packages\girder_client\__init__.py", line 465, in sendRestRequest
    response=result)
girder_client.HttpError: HTTP error 502: POST https://slicer-packages.kitware.com/api/v1/file/chunk?offset=134217728&amp;uploadId=617104b3342a877cb3d2680d
Response text: &lt;html&gt;

&lt;head&gt;&lt;title&gt;502 Bad Gateway&lt;/title&gt;&lt;/head&gt;

&lt;body bgcolor="white"&gt;

&lt;center&gt;&lt;h1&gt;502 Bad Gateway&lt;/h1&gt;&lt;/center&gt;

&lt;hr&gt;&lt;center&gt;nginx&lt;/center&gt;

&lt;/body&gt;

&lt;/html&gt;
</code></pre>

---

## Post #8 by @lassoan (2021-10-21 18:44 UTC)

<p>We could retry a few times, with increasingly longer delays (after 10sec, 30sec, 2, 5, 10 minutes), but it would be better to have a look at the nginx and girder logs to see if the root cause can be addressed. Maybe we hit some time limit (due to having more and more files stored on the server).</p>
<p>Extension packages are smaller, so maybe that’s why the issue comes up only for the Slicer installer upload.</p>

---
