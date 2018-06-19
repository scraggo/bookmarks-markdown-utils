import pyperclip

def main():
    print('Copy your markdown links to clipboard, enter when done:')
    input('> ')
    todoTxt = pyperclip.paste()
    todoArray = todoTxt.split('\n')
    links = App(todoArray)
    links.block_encoder()

    ### encapsulate in an App method:
    headerList = list(set(links.header_list))
    headerList.sort()
    headerList = ', '.join(headerList)
    ##################################

    allLinks = links.return_sorted()
    pyperclip.copy(headerList + '\n\n' + allLinks)
    print('\n'*12)
    print('Finished!')
    print('Sorted links were copied to your clipboard.')

if __name__ == '__main__':
    main()