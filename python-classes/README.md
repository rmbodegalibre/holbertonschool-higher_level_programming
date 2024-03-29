<h1>Python - Classes and Objects</h1>
<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/247/oop-meme.jpg" alt="" /></p>
<h2>Background Context</h2>
<p>OOP is a totally new concept for all of you (especially those who think they know about it :)). It&rsquo;s VERY important that you read at least all the material that is listed bellow (and skip what we recommend you to skip, you will see them later in the curriculum).</p>
<p>As usual, make sure you type (never copy and paste), test, understand all examples shown in the following links (including those in the video), test again etc. The biggest and most important takeaway of this project is: experiment by yourself OOP, play with it!</p>
<p>Read or watch the below resources in the order presented.</p>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="Object Oriented Programming" href="https://intranet.hbtn.io/rltoken/5envVBirO286MdSZgZ4DoQ" target="_blank" rel="noopener">Object Oriented Programming</a>&nbsp;(<em>Read everything until the paragraph &ldquo;Inheritance&rdquo; excluded. You do NOT have to learn about class attributes,&nbsp;<code>classmethod</code>&nbsp;and&nbsp;<code>staticmethod</code>&nbsp;yet</em>)</li>
<li><a title="Object-Oriented Programming" href="https://intranet.hbtn.io/rltoken/sCdUrEsHLFH2NpUzI5Xx8w" target="_blank" rel="noopener">Object-Oriented Programming</a>&nbsp;(<em>Please *</em>be careful*<em>: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON&rsquo;T have to learn about class attributes), Methods, The&nbsp;<code>__init__</code>&nbsp;Method, &ldquo;Data Abstraction, Data Encapsulation, and Information Hiding,&rdquo; &ldquo;Public, Protected, and Private Attributes&rdquo;</em>)</li>
<li><a title="Properties vs. Getters and Setters" href="https://intranet.hbtn.io/rltoken/3B0RWILA_kSjK5udEbFt-A" target="_blank" rel="noopener">Properties vs. Getters and Setters</a></li>
<li><a title="Learn to Program 9 : Object Oriented Programming" href="https://intranet.hbtn.io/rltoken/5u8UhnaTWX2A-G7LICKCDw" target="_blank" rel="noopener">Learn to Program 9 : Object Oriented Programming</a></li>
<li><a title="Python Classes and Objects" href="https://intranet.hbtn.io/rltoken/cwqg7Ud04LTDsatPT17CaQ" target="_blank" rel="noopener">Python Classes and Objects</a></li>
<li><a title="Object Oriented Programming" href="https://intranet.hbtn.io/rltoken/6cZhWLe083CJERYLjAM0BQ" target="_blank" rel="noopener">Object Oriented Programming</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to&nbsp;<a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/gwuqSZXS7ElRbiObQzDcTg" target="_blank" rel="noopener">explain to anyone</a>,&nbsp;<strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>Why Python programming is awesome</li>
<li>What is OOP</li>
<li>&ldquo;first-class everything&rdquo;</li>
<li>What is a class</li>
<li>What is an object and an instance</li>
<li>What is the difference between a class and an object or instance</li>
<li>What is an attribute</li>
<li>What are and how to use public, protected and private attributes</li>
<li>What is&nbsp;<code>self</code></li>
<li>What is a method</li>
<li>What is the special&nbsp;<code>__init__</code>&nbsp;method and how to use it</li>
<li>What is Data Abstraction, Data Encapsulation, and Information Hiding</li>
<li>What is a property</li>
<li>What is the difference between an attribute and a property in Python</li>
<li>What is the Pythonic way to write getters and setters in Python</li>
<li>How to dynamically create arbitrary new attributes for existing instances of a class</li>
<li>How to bind attributes to object and classes</li>
<li>What is the&nbsp;<code>__dict__</code>&nbsp;of a class and/or instance of a class and what does it contain</li>
<li>How does Python find the attributes of an object or class</li>
<li>How to use the&nbsp;<code>getattr</code>&nbsp;function</li>
</ul>
<h2>Requirements</h2>
<h3>General</h3>
<ul>
<li>Allowed editors:&nbsp;<code>vi</code>,&nbsp;<code>vim</code>,&nbsp;<code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)</li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly&nbsp;<code>#!/usr/bin/python3</code></li>
<li>A&nbsp;<code>README.md</code>&nbsp;file, at the root of the folder of the project, is mandatory</li>
<li>Your code should use the pycodestyle (version 2.7.*)</li>
<li>All your files must be executable</li>
<li>The length of your files will be tested using&nbsp;<code>wc</code></li>
<li>All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)</li>
<li>All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)</li>
<li>All your functions (inside and outside a class) should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code>&nbsp;and&nbsp;<code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)</li>
<li>A documentation is not a simple word, it&rsquo;s a real sentence explaining what&rsquo;s the purpose of the module, class or method (the length of it will be verified)</li>
</ul>
<h2>More Info</h2>
<p><strong>Documentation is now mandatory!</strong>&nbsp;Each module, class, and method must contain docstring as comments.&nbsp;<a title="Example Google Style Python Docstrings" href="https://intranet.hbtn.io/rltoken/WK6oRgAsdc3cSB4XHgE_1A" target="_blank" rel="noopener">Example Google Style Python Docstrings</a></p>