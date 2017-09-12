while True :
    mystr=input('请输入字符:')
    if mystr in ['exit','tuichu']:
        with open('record.txt', 'r', encoding='utf-8') as f:
          for k in f:
            print(k,end=' ')
        break
    with open('record.txt','a+',encoding='utf-8') as f:
        f.write(mystr+'\n')

