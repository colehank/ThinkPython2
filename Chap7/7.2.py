def eval_loop():
    while True: 
        print('请输入：')
        word = input()
        if word == 'done':
            print(word)
            break
        output = eval(word)
        print(output)
        
eval_loop()

