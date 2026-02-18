# How to archive jupyter notebooks

**Topic ID**: 12239
**Date**: 2020-06-27
**URL**: https://discourse.slicer.org/t/how-to-archive-jupyter-notebooks/12239

---

## Post #1 by @ungi (2020-06-27 03:41 UTC)

<p>I use SlicerJupyter to run automated experiments with Slicer, generating snapshots of the views. Sometimes I forget to save the notebook with valuable results. For non-Slicer notebooks, I can use an external process to save my notebook as a single html file:<br>
os.system("jupyter nbconvert --to html " + notebook_name + " --output " + filename)<br>
But this doesn’t work in Slicer, because the command ‘jupyter’ is not available in the Slicer environment. Does anybody happen to know a way to automatically (triggered by notebook code) save a Slicer Jupyter notebook after running it?</p>

---

## Post #2 by @lassoan (2020-06-27 06:17 UTC)

<p>You should be able to run nbconvert utility from any python environment, just need to <a href="https://nbconvert.readthedocs.io/en/latest/install.html">pip install it</a>. I don’t think it requires jupyter, you should be able to use it directly - see API description <a href="https://nbconvert.readthedocs.io/en/latest/api/nbconvertapp.html">here</a>.</p>
<p>Slicer’s JupyterNotebooksLib has a convenience function for getting the full path of your notebook:</p>
<pre><code class="lang-python">import JupyterNotebooksLib as slicernb
notebook_path = slicernb.notebookPath()
</code></pre>

---

## Post #3 by @ungi (2020-06-27 15:57 UTC)

<p>Thanks. This pointed in the right direction. For the record, here is a solution that seems to work:</p>
<p><code>notebooks_save_path</code> – define as the folder for archived notebooks<br>
<code>save_timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')</code><br>
– this will be used to create unique filename for the saved file</p>
<p>Add a cell to save the current state of the notebook:</p>
<pre><code class="lang-python">from IPython.display import Javascript
script = '''
require(["base/js/namespace"],function(Jupyter) {
    Jupyter.notebook.save_checkpoint();
});
'''
Javascript(script)
</code></pre>
<p>And finally, this cell saves the notebook to an html file:</p>
<pre><code class="lang-python">import nbformat
from nbconvert import HTMLExporter
import json

notebook_path = slicernb.notebookPath()

with open(notebook_path, mode="r") as f:
    file_json = json.load(f)
    
notebook_content = nbformat.reads(json.dumps(file_json), as_version=4)

html_exporter = HTMLExporter()
(body, resources) = html_exporter.from_notebook_node(notebook_content)

this_notebook_name = os.path.splitext(os.path.basename(notebook_path))[0]
save_file_name = this_notebook_name + "_" + save_timestamp + ".html"
notebook_fullpath = os.path.join(notebooks_save_path, save_file_name)

f = open(notebook_fullpath, 'wb')
f.write(body.encode())
f.close()
</code></pre>

---

## Post #4 by @lassoan (2020-06-27 18:38 UTC)

<p>Thanks a lot. I’ve added convenience functions to make it these features easily accessible:</p>
<pre><code class="lang-python">import JupyterNotebooksLib as slicernb

slicernb.notebookSaveCheckpoint()
slicernb.notebookExportToHtml()
</code></pre>

---
