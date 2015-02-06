#!/usr/bin/python
import re
import os
from os import path
import xml.etree.ElementTree as ET
import datetime as DT
import urllib

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

#For xml
TITLE = "WLIU"
HOST = "http://localhost/"
PIC_FILE_PATH = HOST + "from_love_school/"
EMAIL = "weichih654@gmail.com"
FIRSTNAME = "Weichih"
LASTNAME = "Liu"

#Local path for downloaded pictures.
PIC_LOCAL_PATH = "./from_love_school/"

class ArticleType1Factory:
    def __init__ (self, content):
        self.__content = content
        self.__type = ""

    @property
    def type(self):
        self.__type = "Type1"
        return self.__type

    @property
    def title(self):
        if self.title is not None:
            return self.title
        m = re.search(r'<img src.*?\.gif\"><strong>(.*?)\n</strong>', self.__content, re.MULTILINE|re.DOTALL);
        if m is None:
            return None
        else:
            return m.groups()[0]

    @property
    def year(self):
        if self.year is not None:
            return self.year
        m = re.search(r'<td width="30%">.*?([0-9]{4,4})-[0-9]{1,2}-[0-9]{1,2} [0-9]{1,2}:[0-9]{1,2}.*?</td>', self.__content, re.MULTILINE|re.DOTALL);
        if m is None:
            return 0
        else:
            return int(m.groups()[0])

    @property
    def month(self):
        if self.month is not None:
            return self.month
        m = re.search(r'<td width="30%">.*?[0-9]{4,4}-([0-9]{1,2})-[0-9]{1,2} [0-9]{1,2}:[0-9]{1,2}.*?</td>', self.__content, re.MULTILINE|re.DOTALL);
        if m is None:
            return 0
        else:
            return int(m.groups()[0])

    @property
    def day(self):
        if self.day is not None:
            return self.day
        m = re.search(r'<td width="30%">.*?[0-9]{4,4}-[0-9]{1,2}-([0-9]{1,2}) [0-9]{1,2}:[0-9]{1,2}.*?</td>', self.__content, re.MULTILINE|re.DOTALL);
        if m is None:
            return 0
        else:
            return int(m.groups()[0])

    @property
    def hour(self):
        if self.hour is not None:
            return self.hour
        m = re.search(r'<td width="30%">.*?[0-9]{4,4}-[0-9]{1,2}-[0-9]{1,2} ([0-9]{1,2}):[0-9]{1,2}.*?</td>', self.__content, re.MULTILINE|re.DOTALL);
        if m is None:
            return 0
        else:
            return int(m.groups()[0])

    @property
    def minute(self):
        if self.minute is not None:
            return self.minute
        m = re.search(r'<td width="30%">.*?[0-9]{4,4}-[0-9]{1,2}-[0-9]{1,2} [0-9]{1,2}:([0-9]{1,2}).*?</td>', self.__content, re.MULTILINE|re.DOTALL);
        if m is None:
            return 0
        else:
            return int(m.groups()[0])

    @property
    def seconds(self):
        return 0

    @property
    def categories(self):
        if self.categories is not None:
            return self.categories
        categories = []
        return cagetories
    
    @property
    def content(self):
        if self.content is not None:
            return self.content
        m = re.search(r'<td width=\"80%\" colsspan=10>.*?<font style=\'line-height:150%\'.*?>(.*?)</td', self.__content, re.MULTILINE|re.DOTALL);
        if m is None:
            return None
        else:
            links = self.pic_links
            linksContent = ""
            for l in links:
                linksContent = "<img src = \"" + l + "\"><br>"
            return linksContent + m.groups()[0]

    @property
    def pic_links(self):
        links = []

        m = re.findall(r'<img src=.*?LoveSchool_xfile.*?GRAPH/(.*?\.jpg)', self.__content, re.MULTILINE|re.DOTALL);
        if m is None:
            return None

        for l in m:
            links.append(PIC_FILE_PATH + "/" + l)
        return links 

    @property
    def pic_src_links(self):
        links = []

        m = re.findall(r'<img src=.*?(LoveSchool_xfile.*?\.jpg)', self.__content, re.MULTILINE|re.DOTALL);
        if m is None:
            return None

        for l in m:
            links.append("http://love.youthwant.com.tw/" + l)
        return links 

class ArticleType2Factory:
    def __init__ (self, content):
        self.__content = content
        self.__type = ""

    @property
    def type(self):
        self.__type = "Type2"
        return self.__type

    @property
    def title(self):
        m = re.search(r'<input type="hidden" name="ctitle" value="(.*?)">', self.__content, re.MULTILINE|re.DOTALL);
        if m is None:
            return None
        else:
            return m.groups()[0]

    @property
    def year(self):
        m = re.search(r'<img src=".*?>([0-9]{4,4})/[0-9]{1,2}/[0-9]{1,2} [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}', self.__content, re.MULTILINE|re.DOTALL);
        if m is None:
            return 0
        else:
            return int(m.groups()[0])

    @property
    def month(self):
        m = re.search(r'<img src=".*?>[0-9]{4,4}/([0-9]{1,2})/[0-9]{1,2} [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}', self.__content, re.MULTILINE|re.DOTALL);
        if m is None:
            return 0
        else:
            return int(m.groups()[0])

    @property
    def day(self):
        m = re.search(r'<img src=".*?>[0-9]{4,4}/[0-9]{1,2}/([0-9]{1,2}) [0-9]{1,2}:[0-9]{1,2}:[0-9]{1,2}', self.__content, re.MULTILINE|re.DOTALL);
        if m is None:
            return 0
        else:
            return int(m.groups()[0])

    @property
    def hour(self):
        m = re.search(r'<img src=".*?>[0-9]{4,4}/[0-9]{1,2}/[0-9]{1,2} ([0-9]{1,2}):[0-9]{1,2}:[0-9]{1,2}', self.__content, re.MULTILINE|re.DOTALL);
        if m is None:
            return 0
        else:
            return int(m.groups()[0])

    @property
    def minute(self):
        m = re.search(r'<img src=".*?>[0-9]{4,4}/[0-9]{1,2}/[0-9]{1,2} [0-9]{1,2}:([0-9]{1,2}):[0-9]{1,2}', self.__content, re.MULTILINE|re.DOTALL);
        if m is None:
            return 0
        else:
            return int(m.groups()[0])

    @property
    def seconds(self):
        m = re.search(r'<img src=".*?>[0-9]{4,4}/[0-9]{1,2}/[0-9]{1,2} [0-9]{1,2}:[0-9]{1,2}:([0-9]{1,2})', self.__content, re.MULTILINE|re.DOTALL);
        if m is None:
            return 0
        else:
            return int(m.groups()[0])

    @property
    def categories(self):
        categories = []
        return cagetories
    
    @property
    def content(self):
        m = re.search('<font class=\"post-content\"><div.*?>(.*?)</div>', self.__content, re.MULTILINE|re.DOTALL);
        if m is None:
            return None
        else:
            links = self.pic_links
            linksContent = ""
            for l in links:
                linksContent = "<img src = \"" + l + "\"><br>"
            return linksContent + m.groups()[0]

    @property
    def pic_links(self):
        links = []

        m = re.findall(r'<img src=.*?LoveSchool_xfile.*?GRAPH/(.*?\.jpg)', self.__content, re.MULTILINE|re.DOTALL);
        if m is None:
            return None

        for l in m:
            links.append(PIC_FILE_PATH + "/" + l)
        return links 

    @property
    def pic_src_links(self):
        links = []

        m = re.findall(r'<img src=.*?(LoveSchool_xfile.*?\.jpg)', self.__content, re.MULTILINE|re.DOTALL);
        if m is None:
            return None

        for l in m:
            links.append("http://love.youthwant.com.tw/" + l)
        return links 

class ArticleParse:
    def __init__ (self, content):
        self.__content = content
        self.__type = ""
        self.__parseFactory = ArticleType1Factory(content)
        if self.__parseFactory.content is None:
            self.__parseFactory = ArticleType2Factory(content)

    @property
    def type(self):
        return self.__parseFactory.type

    @property
    def title(self):
        return self.__parseFactory.title

    @property
    def year(self):
        return self.__parseFactory.year

    @property
    def month(self):
        return self.__parseFactory.month

    @property
    def day(self):
        return self.__parseFactory.day

    @property
    def hour(self):
        return self.__parseFactory.hour

    @property
    def minute(self):
        return self.__parseFactory.minute

    @property
    def seconds(self):
        return self.__parseFactory.seconds

    @property
    def categories(self):
        return self.__parseFactory.categories
    
    @property
    def content(self):
        return self.__parseFactory.content

    @property
    def pic_links(self):
        return self.__parseFactory.pic_links

    @property
    def pic_src_links(self):
        return self.__parseFactory.pic_src_links

    def download_pics(self, pics):
        file = urllib.URLopener()
        for l in pics:
            m = re.search('.*/(.*)', l);
            if m is None:
                return None
            file.retrieve(l, PIC_LOCAL_PATH + "/" + m.groups()[0])


def get_content_from_file(filePath):
    data = ""
    with open (filePath, "r") as myfile:
        data += myfile.read()

    udata = data.decode("big5", errors='ignore').encode("utf8").replace('\r\n','').replace('\r','')
    #sometimes `cp950'
    if udata is None:
        udata = data.decode("cp950").encode("utf8").replace('\r\n','').replace('\r','')
    return udata

#This method override the ET._escape_cdata
def new_escape_cdata(text, encoding):
    try:
        return text.encode(encoding, "xmlcharrefreplace")
    except (TypeError, AttributeError):
        _raise_serialization_error(text)

ET._escape_cdata = new_escape_cdata

class ArticleMgr:
    def __init__ (self):
        self.fileArticleDict = {}

    def __CDATA__ (self, text):
        return '<![CDATA[' + unicode(text) + ']]>'

    def get_alticles_from_dir(self, fileDirectory, Articles):
        files = os.listdir(fileDirectory)

        i = 0
        for f in files:
            m = re.search('.*\.html', f)
            article = ArticleParse(get_content_from_file(fileDirectory + "/" + f))
            self.fileArticleDict[f] = article
            Articles.append(article)
            i += 1

    def export_xml(self, Articles, toFile=None):
        defaultTitle = TITLE 
        defaultLink = HOST
        defaultPubDate = 'Thu, 15 Jan 2015 02:44:37 +0000'
        defaultLanguage = 'zh-TW'
        defaultWxrVersion = '1.2'
        defaultEmail = EMAIL
        defaultGenerator = 'http://wordpress.org/?v=4.0.1'

        rss = ET.Element('rss', {'version': '2.0', 
            'xmlns:excerpt': 'http://wordpress.org/export/1.2/excerpt/', 
            'xmlns:content': 'http://purl.org/rss/1.0/modules/content/',
            'xmlns:wfw': 'http://wellformedweb.org/CommentAPI/',
            'xmlns:dc': 'http://purl.org/dc/elements/1.1/',
            'xmlns:wp': 'http://wordpress.org/export/1.2/'})
        channel = ET.SubElement(rss, 'channel')

        title = ET.SubElement(channel, 'title')
        title.text = defaultTitle

        link = ET.SubElement(channel, 'link')
        link.text = defaultLink

        pubDate = ET.SubElement(channel, 'pubDate')
        pubDate.text = defaultPubDate

        language = ET.SubElement(channel, 'language')
        language.text = defaultLanguage

        wxrVersion = ET.SubElement(channel, 'wp:wxr_version')
        wxrVersion.text = defaultWxrVersion

        baseSiteUrl = ET.SubElement(channel, 'wp:base_site_url')
        baseSiteUrl.text = defaultLink

        baseBlogUrl = ET.SubElement(channel, 'wp:base_blog_url')
        baseBlogUrl.text = defaultLink

        wpAuthor = ET.SubElement(channel, 'wp:author')

        wpAuthorId = ET.SubElement(wpAuthor, 'wp:author_id')
        wpAuthorId.text = '1'

        wpAuthorLogin = ET.SubElement(wpAuthor, 'wp:author_login')
        wpAuthorLogin.text = 'admin'

        wpAuthorEmail = ET.SubElement(wpAuthor, 'wp:author_email')
        wpAuthorEmail.text = defaultEmail

        wpAuthorAuthorDisplayName = ET.SubElement(wpAuthor, 'wp:author_display_name')

        wpAuthorAuthorFirstName = ET.SubElement(wpAuthor, 'wp:author_first_name')
        wpAuthorAuthorFirstName.text = self.__CDATA__(FIRSTNAME)

        wpAuthorAuthorLastName = ET.SubElement(wpAuthor, 'wp:author_last_name')
        wpAuthorAuthorLastName.text = self.__CDATA__(LASTNAME)

        generator = ET.SubElement(channel, 'generator')
        generator.text = defaultGenerator

        i = 0
        for a in Articles:
            print ("Processing `%s'..." % a.title)
            if a.title is None or a.content is None:
                for key, value in self.fileArticleDict.iteritems():
                    if value is a:
                        print ("Error, the file is `%s'" % key)
                        break
                print ("Error, dict not found")
                break

            dt = DT.datetime(a.year, a.month, a.day, a.hour, a.minute, a.seconds, tzinfo=None)
            utcTime = dt - DT.timedelta(hours=8)

            aItem = ET.SubElement(channel, 'item')
            aTitle = ET.SubElement(aItem, 'title')
            aTitle.text = self.__CDATA__(a.title)
            aDatetime = ET.SubElement(aItem, 'pubDate')
            aDatetime.text = dt.isoformat(' ')
            aContent = ET.SubElement(aItem, 'content:encoded')
            aContent.text = self.__CDATA__(a.content) 
            aPostDate = ET.SubElement(aItem, 'wp:post_date')
            aPostDate.text = dt.isoformat(' ')
            aPostDateGmt = ET.SubElement(aItem, 'wp:post_date_gmt')
            aPostDateGmt.text = utcTime.isoformat(' ')
            aCommentStatus = ET.SubElement(aItem, 'wp:comment_status')
            aCommentStatus.text = 'open'
            aPingStatus = ET.SubElement(aItem, 'wp:ping_status')
            aPingStatus.text = 'open'
            aPostName = ET.SubElement(aItem, 'wp:post_name')
            aPostName.text = self.__CDATA__(a.title)

            aPostParent = ET.SubElement(aItem, 'wp:post_parent')
            aPostParent.text = '0'
            aMenuOrder = ET.SubElement(aItem, 'wp:menu_order')
            aMenuOrder.text = '0'
            aPostType = ET.SubElement(aItem, 'wp:post_type')
            aPostType.text = 'post'
            aPostPassword = ET.SubElement(aItem, 'wp:post_password')
            aIsSticky = ET.SubElement(aItem, 'wp:is_sticky')
            aIsSticky.text = '0'
            aCategory = ET.SubElement(aItem, 'category')
            aCategory.text = '<![CDATA[Uncategorized]]>'

            aPostStatus = ET.SubElement(aItem, 'wp:status')
            aPostStatus.text = 'publish'
            a.download_pics(a.pic_src_links)
            i += 1

        if toFile is not None:
            f = open(toFile, 'w')
            f.write(ET.tostring(rss, encoding="UTF-8"))
            f.close()
        else:
            print ET.tostring(rss, encoding="UTF-8")
