def reverse_word(s):
    #将单词拆为列表
    words=s.split(' ')
    #对列表的每个单词进行反转
    reverse_word=[word[::-1] for word in words]
    #使用空格将反转后的字符连接成新的字符串
    return ' '.join(reverse_word)

input_string="Hello World"
print(reverse_word(input_string))