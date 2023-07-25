# 以下のブロック1-3のうち、ブロック2,3を
# 編集してプログラムを完成させなさい。
# %%
# ブロック1 [読み込み]
#
# ファイルoz.mdを読み込むコード
with open('./oz.md','r') as file:
    text = file.read()

# %%
# ブロック2 [置換]
# 
# 上記で読み込んだテキストtextに対し、
# translateメソッドで7種の特殊記号
# (#.,":;!)をカラ文字('')に置換する
# コードをここに書いてください。
# 置換した結果はtext_cleanedという
# 変数に代入してください。
trans_rule = dict.fromkeys('#.,":;!','')
trans = str.maketrans(trans_rule)
text_cleaned = text.translate(trans).casefold()
# %%
# ブロック3 [書き込み]
#
# 上記で作成したtext_cleanedの内容を、
# ファイルoz_cleaned.mdに出力する
# コードをここに書いてください。
# withブロックを使うこと。
with open('oz_cleaned.md','w') as file:
    file.write(text_cleaned)
# %%
