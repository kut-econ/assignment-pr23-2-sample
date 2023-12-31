# 以下のブロック1-6のうち、ブロック3、5を編集して
# プログラムを完成させてください。
# %%
# ブロック1 [読み込み]
#
# ファイルoz_cleaned.mdを読み込むコード
with open('./oz_cleaned.md','r') as file:
    text = file.read()

# %%
# ブロック2 [単語への分割]
#
# 読み込んだテキストを単語に分割して単語の
# リストwordsを作成するコード
words = text.split()

# %%
# ブロック3 [単語出現回数の計算]
# 
# ここに、リストwords内に含まれている各単語
# の出現回数を計算し、単語をキー、その出現回数を
# 値とする辞書を作成するコードを書いてください。
# 作成した辞書は変数countに代入してください。
# ヒント1：出現回数の計算は、リストのメソッド
# であるcountを使うと楽です(教科書6.1.7)。
# ヒント2：単語の重複を取り除きたいときは、集合
# を使うことができます。
count = dict()
for w in set(words):
    count[w] = words.count(w)

# %%
# ブロック4 [出力する行のリストの作成]
#
# 出力内容となるテキストの各行を格納したリスト
# output_linesをここで作成します。
# ここでは、最初の4行だけ格納しておきます。
output_lines = [
    '# Word frequencies in chapter 1\n',
    '\n',
    '|word|count|\n',
    '|--|--|\n'
    ]

# %%
# ブロック5 [4行目以降の作成]
#
# ここに、output_linesの5行目以降を追加するコード
# を書いてください。ブロック6でこのリストはファイルの
# writelinesメソッド(教科書7.2.1)を使って出力されます
# ので、各行の末尾には、改行('\n')を追加するようにして
# ください。
#
# ヒント1：リストへの要素の追加にはappendメソッドを
# 使います。ループ処理等を活用して、すべての出力行
# をoutput_linesに追加してください。
# ヒント2: キーをアルファベット順に並べ替えるには、
# ビルトイン関数のsortedを使うことができます。
# ヒント3: 数字を文字列に変換するには、関数strを使う
# ことができます。
for k in sorted(count.keys()):
    line = '|' + k + '|' + str(count[k]) + '|\n'
    output_lines.append(line)
# %%
# ブロック6 [書き込み]
# 
# output_linesの内容をファイルword_count.mdに
# 書き込むコード
# 注)writelinesメソッドについては教科書7.2.1を
# 参照してください。
with open('./word_count.md','w') as file:
    file.writelines(output_lines)

# %%
