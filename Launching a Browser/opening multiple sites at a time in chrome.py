import webbrowser
urL='https://www.google.com'
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome',None,webbrowser.Chrome(chrome_path))
c=webbrowser.get('chrome')
c.open_new_tab(urL)
c.open('https://www.google.com')
c.open('https://read.amazon.in')
c.open('https://www.udemy.com')

