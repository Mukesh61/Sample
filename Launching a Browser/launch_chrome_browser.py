import webbrowser

urL='https://www.google.com'
#provide the path of chrome browser installed in your machine. Otherwise it will
#default browser
chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
webbrowser.register('chrome',None,webbrowser.Chrome(chrome_path))
c=webbrowser.get('chrome')

#opening google 
c.open_new_tab(urL)
