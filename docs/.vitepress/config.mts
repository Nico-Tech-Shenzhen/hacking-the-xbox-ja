import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'ja',
  title: 'Hacking the Xbox 日本語訳',
  description:
    'Hacking the Xbox の日本語訳。ニコ技深圳コミュニティ / 高須正和（@tks）による翻訳コントリビューション。',

  base: '/hacking-the-xbox-ja/',

  head: [
    ['meta', { name: 'robots', content: 'noindex' }],
    ['meta', { name: 'author', content: 'Andrew "bunnie" Huang (原著); 翻訳: ニコ技深圳コミュニティ / 高須正和 / TAKASU Masakazu' }],
    [
      'script',
      {
        async: '',
        src: 'https://www.googletagmanager.com/gtag/js?id=G-E0N88X4QBG',
      },
    ],
    [
      'script',
      {},
      `window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-E0N88X4QBG');`,
    ],
  ],

  themeConfig: {
    siteTitle: 'Hacking the Xbox 日本語訳',

    nav: [
      { text: 'ホーム', link: '/' },
      { text: '翻訳プロジェクト', link: '/translation-ci-cd' },
      { text: 'クレジット', link: '/credits' },
      { text: 'ライセンス', link: '/license' },
      { text: '翻訳方針', link: 'https://github.com/Nico-Tech-Shenzhen/hacking-the-xbox-ja/blob/main/TRANSLATION_GUIDE.md' },
    ],

    sidebar: [
      {
        text: '前書き',
        items: [
          { text: '読者のみなさんへ', link: '/ja/dear-reader' },
          { text: '謝辞', link: '/ja/acknowledgments' },
          { text: 'プロローグ', link: '/ja/prologue' },
        ],
      },
      {
        text: '本文',
        items: [
          { text: '第1章 リバースエンジニアリング入門', link: '/ja/ch01' },
          { text: '第2章 箱の中で考える', link: '/ja/ch02' },
          { text: '第3章 青色LEDを取り付ける', link: '/ja/ch03' },
          { text: '第4章 USBアダプタを作る', link: '/ja/ch04' },
          { text: '第5章 壊れた電源を交換する', link: '/ja/ch05' },
          { text: '第6章 最高のXboxゲーム：セキュリティハッキング', link: '/ja/ch06' },
          { text: '第7章 セキュリティ入門', link: '/ja/ch07' },
          { text: '第8章 Xboxセキュリティのリバースエンジニアリング', link: '/ja/ch08' },
          { text: '第9章 裏口から忍び込む', link: '/ja/ch09' },
          { text: '第10章 さらなるハードウェアプロジェクト', link: '/ja/ch10' },
          { text: '第11章 Xbox向けソフトウェア開発', link: '/ja/ch11' },
          { text: '第12章 注意せよ、ハッカーよ', link: '/ja/ch12' },
          { text: '第13章 前進！', link: '/ja/ch13' },
        ],
      },
      {
        text: '付録',
        items: [
          { text: '付録A ハッキング機器の入手先', link: '/ja/appendix-a' },
          { text: '付録B はんだ付け技術', link: '/ja/appendix-b' },
          { text: '付録C PCBレイアウト入門', link: '/ja/appendix-c' },
          { text: '付録D FPGA入門', link: '/ja/appendix-d' },
          { text: '付録E デバッグ：ヒントとコツ', link: '/ja/appendix-e' },
          { text: '付録F Xboxハードウェアリファレンス', link: '/ja/appendix-f' },
        ],
      },
      {
        text: '情報',
        items: [
          { text: '翻訳にもCI/CDを（高須正和）', link: '/translation-ci-cd' },
          { text: 'クレジット・謝辞', link: '/credits' },
          { text: 'コンテンツライセンス', link: '/license' },
          { text: '翻訳方針', link: 'https://github.com/Nico-Tech-Shenzhen/hacking-the-xbox-ja/blob/main/TRANSLATION_GUIDE.md' },
        ],
      },
    ],

    footer: {
      message:
        'ニコ技深圳コミュニティ / 高須正和（@tks）による日本語訳コントリビューションです。著者 bunnie からも歓迎のコメントをいただいています。原著は Andrew \'bunnie\' Huang および No Starch Press に帰属します。',
      copyright:
        '翻訳テキスト © 翻訳者 | 原著 © 2003 Xenatera LLC (著者: Andrew \'bunnie\' Huang) | CC BY-NC-SA 1.0',
    },

    editLink: {
      pattern: 'https://github.com/Nico-Tech-Shenzhen/hacking-the-xbox-ja/edit/main/docs/:path',
      text: 'このページを編集',
    },
  },

  markdown: {
    lineNumbers: false,
  },
})
