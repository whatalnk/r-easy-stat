# r-easy-stat
## About
『[Rによるやさしい統計学](http://shop.ohmsha.co.jp/shopdetail/000000001781/)』（オーム社）のnotebooks

## 目次
第I部

* [1章](http://whatalnk.github.io/r-easy-stat/Chap01.html)  
    * [hawks.csv](https://github.com/whatalnk/r-easy-stat/raw/master/hawks.csv)
    * [varp.r](https://github.com/whatalnk/r-easy-stat/raw/master/varp.r)
* [2章](http://whatalnk.github.io/r-easy-stat/Chap02.html)  
* [3章](http://whatalnk.github.io/r-easy-stat/Chap03.html)  
    * [Chap03_food.xlsx](https://github.com/whatalnk/r-easy-stat/raw/master/Chap03_food.xlsx)
* [4章](http://whatalnk.github.io/r-easy-stat/Chap04.html)  
* [5章](http://whatalnk.github.io/r-easy-stat/Chap05.html) 
    * [teaching_methods.csv](https://github.com/whatalnk/r-easy-stat/raw/master/teaching_methods.csv)，fileEncodhing = "UTF-8"
* [6章](http://whatalnk.github.io/r-easy-stat/Chap06.html)  
* [7章](http://whatalnk.github.io/r-easy-stat/Chap07.html)    
    * [chap07_2.csv](https://github.com/whatalnk/r-easy-stat/raw/master/chap07_2.csv)，fileEncodhing = "cp932"
    * [chap07_3.csv](https://github.com/whatalnk/r-easy-stat/raw/master/chap07_3.csv)，fileEncodhing = "cp932"
    * [chap07_ex1.csv](https://github.com/whatalnk/r-easy-stat/raw/master/chap07_ex1.csv)，fileEncodhing = "cp932"
    * [chap07_ex2.csv](https://github.com/whatalnk/r-easy-stat/raw/master/chap07_ex2.csv)，fileEncodhing = "cp932"  

第II部
* 8章，9章: 省略
      * [Advanced R.](http://adv-r.had.co.nz/) の Foundations の [Data structures](http://adv-r.had.co.nz/Data-structures.html)，[Subsetting](http://adv-r.had.co.nz/Subsetting.html)，[Vocabulary](http://adv-r.had.co.nz/Vocabulary.html) など
      * 日本語版: [R言語徹底解説](http://www.kyoritsu-pub.co.jp/bookdetail/9784320123939)  

...

## 日本語を含んだcsvファイルを読み込んだ時に文字化けする or 読み込めない場合
* `fileEncoding` を指定する
      * Excel で作ったcsvファイルはエンコーディングが cp932 なので，`read.csv("your-file-name.csv", fileEncodhing = "cp932")`
      
### Macの人でRを起動したときに下のようなエラーメッセージが出る場合
```
During startup - Warning messages:
1: Setting LC_CTYPE failed, using "C"
2: Setting LC_COLLATE failed, using "C"
3: Setting LC_TIME failed, using "C"
4: Setting LC_MESSAGES failed, using "C"
5: Setting LC_PAPER failed, using "C"
```

* 下のリンクを見る（OSがUS の場合．OSが日本語の場合は，`en_US.UTF-8` を `ja_JP.UTF-8` に変える．）  

> * [osx - Installing R on Mac - Warning messages: Setting LC_CTYPE failed, using "C" - Stack Overflow](http://stackoverflow.com/questions/9689104/installing-r-on-mac-warning-messages-setting-lc-ctype-failed-using-c)

## Rを[Jupyter notebook](http://jupyter.org/) で使う

* Rのインストール
* Pythonのインストール
  * [Miniconda](http://conda.pydata.org/miniconda.html) をインストールする
* Jupyter インストール
  * コマンドプロンプト（Macの人はTerminal等）から
```
conda install jupyter
```
* [IRkernel](http://irkernel.github.io/)インストール
  * R を起動して，
```
install.packages(c('repr', 'pbdZMQ', 'devtools')) 
devtools::install_github('irkernel/IRdisplay')
devtools::install_github('irkernel/IRkernel')
IRkernel::installspec()
```
* 起動
  * コマンドプロンプト（or Terminal）から，
```
jupyter notebook
```
