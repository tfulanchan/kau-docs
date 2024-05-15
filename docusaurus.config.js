// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion
const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'King Abdulaziz University',
  tagline: 'Faculty of Computing & Information Technology',
  customFields: {
    more:'Bachelor in Information Systems',
  },
  favicon: 'img/kau_square.jpg',

  // Set the production url of your site here
  url: 'https://your-docusaurus-test-site.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'facebook', // Usually your GitHub org/user name.
  projectName: 'docusaurus', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/kau_logo.jpg',
      docs: {
        sidebar: {
          hideable: true,
        },
      },
      navbar: {
        title: '主頁',
        logo: {
          alt: '主頁',
          src: 'img/kau_square.jpg',
        },
        items: [
          {
            position: "left",
            label: "正信原則",
            to: 'docs/iimaan',
            items: [
              {
                label: "開始閱讀",
                to: "docs/iimaan",
              },
              {
                label: "關於譯者",
                to: "blog/suJiYuan",
              },             
            ],
          },
          {
            position: "left",
            label: "古蘭經注",
            to: 'docs/tafseer',
            items: [
              {
                label: "開始閱讀",
                to: "docs/tafseer",
              },
              {
                label: "關於譯者",
                to: "blog/kongDeJun",
              },
            ],
          },
          {
            position: "right",
            href: "https://qurancomplex.gov.sa/kfgqpc/about/",
            label:'關於印刷局',
          },
          {
            position: "right",
            href: "#",
            label: '附註',
          },
          {
            position: "right",
            to: "contact",
            label:'聯繫站長',
          },
        ],
      },
      footer: {
        style: 'dark',
        copyright: `版權所有 © ${new Date().getFullYear()} 法赫德國王《古蘭經》印刷局  `,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
    themes: [
      [
        "@easyops-cn/docusaurus-search-local",
        {
          hashed: true,
          language: ["en", "zh"],
          highlightSearchTermsOnTargetPage: true,
          explicitSearchResultPath: true,
          // indexDocs: false,
        },
      ],
    ],
};

module.exports = config;
