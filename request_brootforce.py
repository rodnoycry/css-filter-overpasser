import requests
import json


url = "https://phl.spbu.ru/administrator/index.php?option=com_content&layout=edit&id=493"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Content-Length": "6709",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cookie": "jpanesliders_panel-sliders=0; jpanesliders_content-sliders-492=0; jpanesliders_permissions-sliders-492=0; jpanesliders_categories-sliders-14=0; jpanesliders_permissions-sliders-14=0; jpanesliders_template-sliders-9=0; jpanesliders_permissions-sliders-4=0; jpanesliders_content-sliders-8=0; jpanesliders_permissions-sliders-8=0; jpanesliders_content-sliders-9=0; jpanesliders_permissions-sliders-9=0; jpanesliders_content-sliders-251=0; jpanesliders_permissions-sliders-251=0; jpanesliders_content-sliders-126=0; jpanesliders_permissions-sliders-126=0; jpanesliders_categories-sliders-20=0; jpanesliders_permissions-sliders-20=0; jpanesliders_content-sliders-125=0; jpanesliders_permissions-sliders-125=0; jpanesliders_categories-sliders-28=0; jpanesliders_permissions-sliders-28=0; jpanesliders_content-sliders-329=0; jpanesliders_permissions-sliders-329=0; jpanesliders_content-sliders-330=0; jpanesliders_permissions-sliders-330=0; jpanesliders_content-sliders-490=0; jpanesliders_permissions-sliders-490=0; jpanesliders_content-sliders-311=0; jpanesliders_permissions-sliders-311=0; jpanesliders_content-sliders-21=0; jpanesliders_permissions-sliders-21=0; jpanesliders_menu-sliders-147=0; jpanesliders_menu-sliders-159=0; jpanesliders_content-sliders-30=0; jpanesliders_permissions-sliders-30=0; jpanesliders_content-sliders-31=0; jpanesliders_permissions-sliders-31=0; jpanesliders_content-sliders-27=0; jpanesliders_permissions-sliders-27=0; jpanesliders_content-sliders-68=0; jpanesliders_permissions-sliders-68=0; jpanesliders_content-sliders-66=0; jpanesliders_permissions-sliders-66=0; jpanesliders_content-sliders-65=0; jpanesliders_permissions-sliders-65=0; jpanesliders_content-sliders-48=0; jpanesliders_permissions-sliders-48=0; jpanesliders_content-sliders-99=0; jpanesliders_permissions-sliders-99=0; jpanesliders_content-sliders-98=0; jpanesliders_permissions-sliders-98=0; jpanesliders_content-sliders-97=0; jpanesliders_permissions-sliders-97=0; jpanesliders_content-sliders-49=0; jpanesliders_permissions-sliders-49=0; jpanesliders_content-sliders-18=0; jpanesliders_permissions-sliders-18=0; jpanesliders_content-sliders-156=0; jpanesliders_permissions-sliders-156=0; 23e010c4fd7ff72158f362f70028ca84=c4a1f3cc22ffa20544c0ab6379cb65ce; session-cookie=17934e330a9145a2a4952fd41e8084585d0e78c6a1a1fe11742758d007d2ea5ca0476ffade5d2850bf9aa62175ff22f2; c51979cc9f7648a6a0bbf279da1bf161=e73bedaf12ed3d4a2a7a566e626d3330; jpanesliders_permissions-sliders-=0; jpanesliders_content-sliders-493=0; jpanesliders_permissions-sliders-493=0; jpanesliders_menu-sliders-526=1; jpanesliders_content-sliders-=1; jpanesliders_menu-sliders-527=0; jpanesliders_content-sliders-494=0; jpanesliders_permissions-sliders-494=0; jpanesliders_content-sliders-495=0; jpanesliders_permissions-sliders-495=0; jpanesliders_menu-sliders-529=0; jpanesliders_content-sliders-496=0; jpanesliders_permissions-sliders-496=0; jpanesliders_categories-sliders-=0; jpanesliders_menu-sliders-530=0; jpanesliders_menu-sliders-528=0; jpanesliders_menu-sliders-531=0; jpanesliders_menu-sliders-=0; jpanesliders_menu-sliders-532=0; jpanesliders_menu-sliders-533=0; jpanesliders_menu-sliders-534=0; jpanesliders_menu-sliders-535=0; jpanesliders_menu-sliders-536=0; jpanesliders_menu-sliders-537=0; jpanesliders_menu-sliders-538=0; jpanesliders_menu-sliders-539=0; jpanesliders_menu-sliders-540=0; jpanesliders_categories-sliders-9=0; jpanesliders_menu-sliders-163=0; jpanesliders_menu-sliders-541=0; jpanesliders_menu-sliders-161=0; jpanesliders_menu-sliders-542=0; jpanesliders_menu-sliders-543=0; jpanesliders_plugin-sliders-410=0; jpanesliders_module-sliders=0",
    "Origin": "https://phl.spbu.ru",
    "Referer": "https://phl.spbu.ru/administrator/index.php?option=com_content&view=article&layout=edit&id=493",
    "Sec-Ch-Ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Opera GX\";v=\"102\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0"
}

payload = {
    'option': 'com_content',
    'layout': 'edit',
    'id': '493',
    'jform[title]': 'Homepage',
    'jform[alias]': 'homepage',
    'jform[catid]': 2,
    'jform[state]': 1,
    'jform[access]': 1,
    'jform[featured]': 0,
    'jform[language]': '*',
    'jform[version_note]': '',
    'jform[id]': 493,
    'jform[articletext]': """<style type="text/css">
/* Custom CSS */

/* Make titles bold */
article.uk-article > h1 {
  font-size: 30px !important;
  font-weight: bold;
}

/* Fix for :after element on main content overflowing body*/
body {
  overflow-x: hidden
}


/* Disable unnecessary margin of main content */
div.uk-grid {
  margin-left: 0 !important
}

/* Disable unnecessary padding of main content */
div.uk-grid > * {
  padding-left: 0 !important
}

/* Main content */
#tm-middle {
  min-height: 60vh;
  position: relative !important;
  padding-top: 30px !important;
  padding-bottom: 100px !important;
}

/* Main content background element */
#tm-middle::before {
  content: "";
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 100vw;
  height: 100%;
  background-color: #EDE9F6;
  border-radius: 36px 36px 0 0; /* Border radius for top corners */
  z-index: -10; /* To position behind the content */
  align-self: center;
}
</style>""",
    'jform[created_by]': 985,
    'jform[created_by_alias]': '',
    'jform[created]': "01-11-2023 01:26:06",
    'jform[publish_up]': "01-11-2023 01:26:06",
    'jform[publish_down]': '',
    'jform[modified]': '01-11-2023 10:41:53',
    'jform[version]': 6,
    'jform[hits]': 18,
    'jform[attribs][article_layout]': '', 
    'jform[attribs][show_title]': '', 
    'jform[attribs][link_titles]': '', 
    'jform[attribs][show_tags]': '', 
    'jform[attribs][show_intro]': '', 
    'jform[attribs][info_block_position]': '', 
    'jform[attribs][info_block_show_title]': '', 
    'jform[attribs][show_category]': '', 
    'jform[attribs][link_category]': '', 
    'jform[attribs][show_parent_category]': '', 
    'jform[attribs][link_parent_category]': '', 
    'jform[attribs][show_associations]': '', 
    'jform[attribs][show_author]': '', 
    'jform[attribs][link_author]': '', 
    'jform[attribs][show_create_date]': '', 
    'jform[attribs][show_modify_date]': '', 
    'jform[attribs][show_publish_date]': '', 
    'jform[attribs][show_item_navigation]': '', 
    'jform[attribs][show_icons]': '', 
    'jform[attribs][show_print_icon]': '', 
    'jform[attribs][show_email_icon]': '', 
    'jform[attribs][show_vote]': '', 
    'jform[attribs][show_hits]': '', 
    'jform[attribs][show_noauth]': '', 
    'jform[attribs][urls_position]': '', 
    'jform[attribs][alternative_readmore]': '', 
    'jform[attribs][article_page_title]': '', 
    'jform[attribs][show_publishing_options]': '', 
    'jform[attribs][show_article_options]': '', 
    'jform[attribs][show_urls_images_backend]': '', 
    'jform[attribs][show_urls_images_frontend]': '', 
    'jform[images][image_intro]': '', 
    'jform[images][float_intro]': '', 
    'jform[images][image_intro_alt]': '', 
    'jform[images][image_intro_caption]': '', 
    'jform[images][image_fulltext]': '', 
    'jform[images][float_fulltext]': '', 
    'jform[images][image_fulltext_alt]': '', 
    'jform[images][image_fulltext_caption]': '', 
    'jform[urls][urla]': '', 
    'jform[urls][urlatext]': '', 
    'jform[urls][targeta]': '', 
    'jform[urls][urlb]': '', 
    'jform[urls][urlbtext]': '', 
    'jform[urls][targetb]': '', 
    'jform[urls][urlc]': '', 
    'jform[urls][urlctext]': '', 
    'jform[urls][targetc]': '', 
    'jform[metadesc]': '', 
    'jform[metakey]': '', 
    'jform[xreference]': '',
    'jform[metadata][robots]': '', 
    'jform[metadata][author]': '', 
    'jform[metadata][rights]': '', 
    'jform[metadata][xreference]': '', 
    'jform[associations][ru-RU]': '', 
    'jform[associations][en-GB]': '', 
    'task': 'article.apply',
    'return': '',
    '7bd615b6467e84f1f5f2894c2ace773e': '1'
}

response = requests.post(url, headers=headers, data=payload)

print(response.text) 



    # jform[rules][core.delete][1]: 
    # jform[rules][core.edit][1]: 
    # jform[rules][core.edit.state][1]: 
    # jform[rules][core.delete][9]: 
    # jform[rules][core.edit][9]: 
    # jform[rules][core.edit.state][9]: 
    # jform[rules][core.delete][6]: 
    # jform[rules][core.edit][6]: 
    # jform[rules][core.edit.state][6]: 
    # jform[rules][core.delete][7]: 
    # jform[rules][core.edit][7]: 
    # jform[rules][core.edit.state][7]: 
    # jform[rules][core.delete][2]: 
    # jform[rules][core.edit][2]: 
    # jform[rules][core.edit.state][2]: 
    # jform[rules][core.delete][3]: 
    # jform[rules][core.edit][3]: 
    # jform[rules][core.edit.state][3]: 
    # jform[rules][core.delete][4]: 
    # jform[rules][core.edit][4]: 
    # jform[rules][core.edit.state][4]: 
    # jform[rules][core.delete][5]: 
    # jform[rules][core.edit][5]: 
    # jform[rules][core.edit.state][5]: 
    # jform[rules][core.delete][8]: 
    # jform[rules][core.edit][8]: 
    # jform[rules][core.edit.state][8]: 