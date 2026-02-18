# Google Health API

**Topic ID**: 12927
**Date**: 2020-08-10
**URL**: https://discourse.slicer.org/t/google-health-api/12927

---

## Post #1 by @howardlander (2020-08-10 14:11 UTC)

<p>Has anyone tried to feed DICOM data to the Slicer from the Google Health API? If so, any advice on how to do so?</p>
<p>Thanks<br>
Howard</p>

---

## Post #2 by @pieper (2020-08-10 14:36 UTC)

<p>Hi <a class="mention" href="/u/howardlander">@howardlander</a> - I’ve tinkered with this.  The <a href="https://pypi.org/project/dicomweb-client/">dicomweb-client</a> python package bundled with Slicer.  To talk with Google’s DICOMweb one needs to include the authentication token, which can be obtained either through the <code>gcloud auth print-access-token</code> once you have logged in.</p>

---

## Post #3 by @pieper (2020-08-10 14:37 UTC)

<p>It would be good to add an example to the script repository for this.  I can work on it with someone if needed.</p>

---

## Post #4 by @lassoan (2020-08-10 14:41 UTC)

<p>I have added an example here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_import_DICOM_files_using_DICOMweb" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_import_DICOM_files_using_DICOMweb</a></p>

---

## Post #5 by @howardlander (2020-08-10 14:57 UTC)

<p>Hi Andras: I’ve looked at your example.  In the case of Google Health, how would I specify the project, region, dataset that I would like to download? Also, I guess there is nothing in the slicer GUI that would let you login to to Google and get the token without the command line?</p>

---

## Post #6 by @pieper (2020-08-10 15:06 UTC)

<p>Here’s an example that works in a colab notebook.  We’d need to port the gcloud syntax to work with Slicer.</p>
<pre><code class="lang-auto">!pip install dicomweb-client

token = !gcloud auth print-access-token
token = token[0]

PROJECT_ID="chc-tcia"
REGION="us-central1"

DATASET_ID="qin-headneck"
DICOM_STORE_ID=DATASET_ID

url = f"https://healthcare.googleapis.com/v1beta1/projects/{PROJECT_ID}/locations/{REGION}/datasets/{DATASET_ID}/dicomStores/{DICOM_STORE_ID}/dicomWeb"
headers = {
    "Authorization" : "Bearer %s" % token
}

import dicomweb_client

client = dicomweb_client.api.DICOMwebClient(url, headers=headers)
studies = client.search_for_studies()

print(f"\n{len(studies)} studies to query\n")

for study in studies:
  studyMetadata = dicomweb_client.api.load_json_dataset(study)
  if hasattr(studyMetadata, "ModalitiesInStudy"):
    print(f"Modalities: {studyMetadata.ModalitiesInStudy}")
  else:
    print("Modalities not defined")
  series = client.search_for_series(studyMetadata.StudyInstanceUID)
  print(f"  {len(series)} series")
  for serie in series:
    seriesMetadata = dicomweb_client.api.load_json_dataset(serie)
    instances = client.search_for_instances(
      study_instance_uid=studyMetadata.StudyInstanceUID,
      series_instance_uid=seriesMetadata.SeriesInstanceUID
    )
    print(f"    {len(instances)} instances ", end="", flush=True)
  print()
</code></pre>

---

## Post #7 by @lassoan (2020-08-10 15:09 UTC)

<aside class="quote no-group" data-username="howardlander" data-post="5" data-topic="12927">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/howardlander/48/5881_2.png" class="avatar"> howardlander:</div>
<blockquote>
<p>In the case of Google Health, how would I specify the project, region, dataset that I would like to download?</p>
</blockquote>
</aside>
<p>We developed and tested <code>importFromDICOMWeb</code> helper function with Kheops, but it is just a <a href="https://github.com/Slicer/Slicer/blob/47c291530bb37f4687eb7a9cfbc7a76f5685bd3e/Modules/Scripted/DICOMLib/DICOMUtils.py#L746-L803">short Python code snippet</a>, so it should be easy to change the API to work with Google Health API, too. Or, maybe we should add a more generic version of this function (which does not download a complete study but selected series only). <a class="mention" href="/u/pieper">@pieper</a>’s example above probably contains all the necessary pieces.</p>
<p>It would be great if you could create this function and contribute it back to Slicer.</p>

---

## Post #8 by @pieper (2020-08-10 15:10 UTC)

<p>The other option for doing the login and getting the token would be to use the browser.  We looked at this at the last project week.</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://projectweek.na-mic.org/assets/favicons/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://projectweek.na-mic.org/PW33_2020_GranCanaria/Projects/OHIFSlicerBridge/" target="_blank" rel="noopener">ProjectWeek</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://projectweek.na-mic.org/PW33_2020_GranCanaria/Projects/OHIFSlicerBridge/" target="_blank" rel="noopener">ProjectWeek</a></h3>

<p>Website for NA-MIC Project Weeks</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #9 by @pieper (2020-08-10 15:16 UTC)

<p>The qSlicerWebWidget could be used to do the login and then we can uses the python/javascript interoperability to pull pass the token into Slicer to use with dicomweb_client.</p>

---

## Post #10 by @howardlander (2020-08-10 15:25 UTC)

<p>This is all interesting and useful to me, though I will have to spend some time with it, as I am a Slicer novice. One thing is that I suppose this would be easier if I had all of the DICOM urls in advance.  Since we are planning to build a cohort selection tool, that is a real possibility.</p>

---

## Post #11 by @lassoan (2020-08-10 16:06 UTC)

<p>Probably the simplest is to just use Slicer’s built-in Pyhon console (Ctrl/Cmd-3). That is a standard Python environment that should already have all the Python packages that you need preinstalled (but you can install more, if needed) and also has all Slicer features available. Let us know if you make progress or get stuck at any point.</p>

---

## Post #12 by @howardlander (2020-08-10 16:57 UTC)

<p>Steve: how would I try the qSlicerWebWidget?</p>

---

## Post #13 by @pieper (2020-08-10 18:48 UTC)

<p>Hi Howard -</p>
<p>This is something I’ve known was possible for a while but hadn’t had a driving use case to make an example, so thanks for the push to sort out the details.  I’ll be needing this soon myself.</p>
<p>First, you can use the web widget (which is basically Chrome) to access an installation of OHIF with the Google API enabled.  In my case I have one in firebase, but any https static server on a domain name you control will work for OIDC (unless you explicitly accept it, mine will give a warning about being unverified, so you can choose to try it or not at your peril).</p>
<p>Paste this in the python console:</p>
<pre><code class="lang-auto">ww = slicer.qSlicerWebWidget()
ww.show()
ww.url = "https://idc-sandbox-000.firebaseapp.com/"
</code></pre>
<p>Then, when you have logged in, use this to get the access token and current page info:</p>
<pre><code class="lang-auto">import json
ww.connect("evalResult(QString,QString)", lambda statement, result: print (json.loads(result)))

ww.evalJS("JSON.stringify([window.store.getState().oidc.user.access_token, window.location.href])")
</code></pre>
<p>Here’s an example output (with a few characters changed in the token to make it invalid).</p>
<pre><code class="lang-auto">['', 'https://idc-sandbox-000.firebaseapp.com/projects/chc-tcia/locations/us-central1/datasets/ct-lymph-nodes/dicomStores/ct-lymph-nodes/study/61.7.276186995443132562163463641799779941762']
</code></pre>
<p>This should be all the ingredients needed to use the dicomweb_client code from within Slicer to read and write via dicomweb.</p>
<p>The Google mirror of TCIA requires approval to access, but you can also access any dicom store, such as one you create under your own account.</p>

---
