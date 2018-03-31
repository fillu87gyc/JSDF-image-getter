# JSDF*image*getter

## 説明

* 海上自衛隊と陸上自衛隊の公開している画像をダウンロードしてきます
* 名前の通りNavy=>海自、airforce=>空自の画像をダウンロードできます

## 対応表

* [ ] 陸上自衛隊
* [x] 海上自衛隊
* [x] 航空自衛隊

## 動作確認した環境

Windows 10  
python ver3.6

## 使い方

### navy.pyの場合

![操作画面](/pic/capture.jpg)

* nameに何型なのか(ship class)
* start numにその型の最も数字が若い番号を入れる
  * あぶくま型 -> [229 あぶくま]
  * はつゆき型 -> [124 みねゆき]
  * あたご型 -> [177 あたご]  などなど海自のHPに行けばわかります
* あとは艦級ごとに自動DLします。

### airforce.pyの場合

* airforce.pyの場合は何もせずにすべてDLしてくれます

---

## 参照ページ

![海上自衛隊のHP](http://www.mod.go.jp/msdf/index.html)  
![海上自衛隊の番号確認できるところ](http://www.mod.go.jp/msdf/formal/gallery/ships/dd/index.html)  
![航空自衛隊のHP](http://www.mod.go.jp/asdf/)  

壁紙とかもHPで配布してるのでHP覗いてみてはいかがでしょうか