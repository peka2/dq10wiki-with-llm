<?php
require_once "simple_html_dom.php";

// $html = file_get_html("https://wikiwiki.jp/dq10dic2nd/?cmd=list");

// $aTags = $html->find("li a");

$html = file_get_contents("https://wikiwiki.jp/dq10dic2nd/?cmd=list");

// $htmlから<li><a href="/dq10dic2nd/%E3 から始まって %91" class="rel-wiki-page"> で終わるリンクのhrefのみを取得する
preg_match_all('/<li><a href="(\/dq10dic2nd\/%E3.*?%91)" class="rel-wiki-page">/', $html, $matches);
$paths = $matches[1];

// 4090くらいは保存してるので、それ以降のデータを取得する（スマイリーキラーで失敗）
$paths = array_slice($paths, 4090);

// 1つずつ取得する
foreach ($paths as $key => $path) {
    // 1つだけデータを取得する
    $html = file_get_html("https://wikiwiki.jp{$path}");

    // <div id="content">の中身を取得する
    $content = $html->find("#content", 0)->plaintext;

    // <title>取得
    $title = $html->find("title", 0)->plaintext;
    // 【】の中身だけを取得する
    $title = preg_replace("/^.*【/", "", $title);
    $title = preg_replace("/】.*$/", "", $title);

    // 余分な改行と空白を削除する
    $content = preg_replace("/\n/", "", $content);
    $content = preg_replace("/\s+/", " ", $content);

    // dataフォルダに保存する
    file_put_contents("data/{$title}.txt", $content);

    var_dump($key, $title);

    // 1.0秒待つ しないとBOT扱いで403になる
    usleep(1000000);
}
