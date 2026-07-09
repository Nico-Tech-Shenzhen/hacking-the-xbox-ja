import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'ja',
  title: 'Hacking the Xbox — 非公式日本語訳',
  description:
    'Andrew "bunnie" Huang 著『Hacking the Xbox: An Introduction to Reverse Engineering』の非公式日本語訳。CC BY-NC-SA 1.0 ライセンスに基づく非営利翻訳です。',

  base: '/hacking-the-xbox-ja/',

  head: [
    ['meta', { name: 'robots', content: 'noindex' }],
    ['meta', { name: 'author', content: 'Andrew "bunnie" Huang (原著); 翻訳: 有志' }],
  ],

  themeConfig: {
    siteTitle: 'Hacking the Xbox 非公式日本語訳',

    nav: [
      { text: 'ホーム', link: '/' },
      { text: 'クレジット', link: '/credits' },
      { text: 'ライセンス', link: '/license' },
      { text: '翻訳方針', link: '/translation-policy' },
    ],

    sidebar: [
      {
        text: '前書き',
        items: [
          { text: 'プロローグ', link: '/ja/prologue' },
        ],
      },
      {
        text: '本文',
        items: [
          { text: '第1章 リバースエンジニアリング入門', link: '/ja/ch01' },
        ],
      },
      {
        text: '情報',
        items: [
          { text: 'クレジット・謝辞', link: '/credits' },
          { text: 'コンテンツライセンス', link: '/license' },
          { text: '翻訳方針', link: '/translation-policy' },
        ],
      },
    ],

    footer: {
      message:
        '本サイトは非公式・非営利の翻訳プロジェクトです。原著は Andrew "bunnie" Huang および No Starch Press に帰属します。',
      copyright:
        '翻訳テキスト © 翻訳者 | 原著 © 2003 Xenatera LLC (著者: Andrew "bunnie" Huang) | CC BY-NC-SA 1.0',
    },

    editLink: {
      pattern: 'https://github.com/YOUR_USERNAME/hacking-the-xbox-ja/edit/main/docs/:path',
      text: 'このページを編集',
    },
  },

  markdown: {
    lineNumbers: false,
  },
})
