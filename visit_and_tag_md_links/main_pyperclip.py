import pyperclip

from visit_and_tag_md_links import App

def main():
    print('Copy your markdown links to clipboard, enter when done:')
    input('> ')
    todoTxt = pyperclip.paste()
    todoArray = todoTxt.split('\n')
    links = App(todoArray)
    links.block_encoder()
    headerList = links.get_sorted_headers()
    allLinks = links.return_sorted()
    pyperclip.copy(headerList + '\n\n' + allLinks)
    print('\n'*12)
    print('Finished!')
    print('Sorted links were copied to your clipboard.')

if __name__ == '__main__':
    main()