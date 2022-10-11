<h1>Python - Everything is object</h1>
<h2>Background Context</h2>
<p>Now that we understand that everything is an object and have a little bit of knowledge, let&rsquo;s pause and look a little bit closer at how Python works with different types of objects.</p>
<p>BTW, have you ever modified a variable without knowing it or wanting to? I mean:</p>
<pre><code>&gt;&gt;&gt; a = 1
&gt;&gt;&gt; b = a
&gt;&gt;&gt; a = 2
&gt;&gt;&gt; b
1
&gt;&gt;&gt; 
</code></pre>
<p>OK. But what about this?</p>
<pre><code>&gt;&gt;&gt; l = [1, 2, 3]
&gt;&gt;&gt; m = l
&gt;&gt;&gt; l[0] = 'x'
&gt;&gt;&gt; m
['x', 2, 3]
&gt;&gt;&gt; 
</code></pre>
<p><img src="https://media.giphy.com/media/wAjfQ9MLUfFjq/giphy.gif" alt="" /><br /><br /></p>
<p>This project is a little bit different than the usual projects. The first part is only questions about Python&rsquo;s specificity like &ldquo;What would be the result of&hellip;&rdquo;. You should&nbsp;<strong>read all documentation first (as usual :))</strong>, then take the time to&nbsp;<strong>think and brainstorm with your peers</strong>&nbsp;about what you think and why.&nbsp;<strong>Try to do this without coding anything for a few hours</strong>.</p>
<p>Trying examples in the Python interpreter will give you most of the answers without having to think about it.&nbsp;<strong>Don&rsquo;t go this route</strong>. First read, then think, then brainstorm together. Only then you can test in the interpreter.</p>
<p>It&rsquo;s important that you truly understand the reasons behind the answers of all those tasks so that you can apply the same logic to other variables and other variable types. The biggest mandatory task is the blog post and it will count for 50% of the total score of the project.</p>
<p>Note that during interviews for Python positions,&nbsp;<strong>you will most likely have to answer to these type of questions</strong>.</p>
<p>All your answers should be only one line in a file. No space before or after the answer.</p>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="9.10. Objects and values" href="https://intranet.hbtn.io/rltoken/vu0q2rKj3XKGyDoqvx72sA" target="_blank" rel="noopener">9.10. Objects and values</a></li>
<li><a title="9.11. Aliasing" href="https://intranet.hbtn.io/rltoken/MOP1Saf_C2E_eHxKnZggHw" target="_blank" rel="noopener">9.11. Aliasing</a></li>
<li><a title="Immutable vs mutable types" href="https://intranet.hbtn.io/rltoken/vvV3pDEliqja6aAI7XFNiA" target="_blank" rel="noopener">Immutable vs mutable types</a></li>
<li><a title="Mutation" href="https://intranet.hbtn.io/rltoken/xyElfrO9KowD4p5UqhQG8A" target="_blank" rel="noopener">Mutation</a>&nbsp;(<em>Only this chapter</em>)</li>
<li><a title="9.12. Cloning lists" href="https://intranet.hbtn.io/rltoken/2tqD3FclxPgvlTC70KQApw" target="_blank" rel="noopener">9.12. Cloning lists</a></li>
<li><a title="Python tuples: immutable but potentially changing" href="https://intranet.hbtn.io/rltoken/OXG9J_vBEWtpxuX2hnF-dQ" target="_blank" rel="noopener">Python tuples: immutable but potentially changing</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/SYBqBafJ9K7-vindoYatpA" target="_blank" rel="noopener">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>Why Python programming is awesome</li>
<li>What is an object</li>
<li>What is the difference between a class and an object or instance</li>
<li>What is the difference between immutable object and mutable object</li>
<li>What is a reference</li>
<li>What is an assignment</li>
<li>What is an alias</li>
<li>How to know if two variables are identical</li>
<li>How to know if two variables are linked to the same object</li>
<li>How to display the variable identifier (which is the memory address in the CPython implementation)</li>
<li>What is mutable and immutable</li>
<li>What are the built-in mutable types</li>
<li>What are the built-in immutable types</li>
<li>How does Python pass variables to functions</li>
</ul>
<h2>Requirements</h2>
<h3>Python Scripts</h3>
<ul>
<li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/python3</code></li>
<li>A&nbsp;<code>README.md</code>&nbsp;file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.7.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using&nbsp;<code>wc</code></li>
</ul>
<h3><code>.txt</code>&nbsp;Answer Files</h3>
<ul>
<li>Only one line</li>
<li>No Shebang</li>
<li>All your files should end with a new line</li>
</ul>