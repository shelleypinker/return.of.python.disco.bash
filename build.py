print('hello_world!')

top = open('templates/top.html').read()
middle = open('content/homepage.html').read()
bottom = open('templates/bottom.html').read()
full_page = top + middle + bottom
open('docs/homepage.html', 'w+').write(full_page)

top = open('templates/top.html').read()
middle = open('content/resume.html').read()
bottom = open('templates/bottom.html').read()
full_page = top + middle + bottom
open('docs/resume.html', 'w+').write(full_page)

top = open('templates/top.html').read()
middle = open('content/about.me.html').read()
bottom = open('templates/bottom.html').read()
full_page = top + middle + bottom
open('docs/about.me.html', 'w+').write(full_page)

