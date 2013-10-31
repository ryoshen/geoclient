#!/usr/bin/python

# Copyright 2013 Xu Shen
#

"""
Unit tests for 
    <?php
    /*
        sexoffice
        CopyRight 2013  baronyang
    */
    define("TOKEN", "sexoffice");
    $wechatObj = new wechatCallbackapiTest();
    $wechatObj->responseMsg();
    class wechatCallbackapiTest
    {
      private $fromUsername;
      private $toUsername;
      private $keywordl;
      private $time;
      private $MsgType;
      private $EventType;
      //回复文本信息 XML是回复的格式
      private function  ReplyTextMsg($sendmsg){
                $textTpl = "<xml>
                            <ToUserName><![CDATA[%s]]></ToUserName>
                            <FromUserName><![CDATA[%s]]></FromUserName>
                            <CreateTime>%s</CreateTime>
                            <MsgType><![CDATA[%s]]></MsgType>
                            <Content><![CDATA[%s]]></Content>
                            <FuncFlag>0</FuncFlag>
                            </xml>";
             $resultStr = sprintf($textTpl, $this->fromUsername, $this->toUsername, $this->time, 'text', $sendmsg);
             echo $resultStr;
      }
       //关注后回复图文信息
      private function AttentionReply1(){
         $textTpl=" <xml>
                        <ToUserName><![CDATA[%s]]></ToUserName>
                        <FromUserName><![CDATA[%s]]></FromUserName>
                        <CreateTime>%s</CreateTime>
                        <MsgType><![CDATA[news]]></MsgType>
                        <ArticleCount>1</ArticleCount>
                        <Articles>
                            <item>
                                <Title><![CDATA[%s]]></Title>
                                <Description><![CDATA[%s]]></Description>
                                <PicUrl><![CDATA[%s]]></PicUrl>
                                <Url><![CDATA[%s]]></Url>
                            </item>
                        </Articles>
                        <FuncFlag>1</FuncFlag>
                    </xml>";
            $title1="道具研究所欢迎您";
            $Description1="亲，欢迎您关注道具研究所，本研究所将于每天18:00-22:00点发布精品图文，";
            $Description1.="大部份内容会涉及夫妻生活及情趣讨论，成人道具介绍，情趣内衣欣赏，AV女优推荐，性生活故事，道具使用感受分享，等敏感话题......。";
            $PicUrl1="http://mmsns.qpic.cn/mmsns/q3PibibJOcnbtgicUHMlbnaKwufAUw4SrvY6nlwlu3PhQXtkn4FoIytmg/0";
            $Url1="http://mp.weixin.qq.com/mp/appmsg/show?__biz=MjM5OTkxNjIwMw==&appmsgid=10000050&itemidx=1&sign=cf074e4612e18689a0c79d8f5555f791#wechat_redirect";
            $resultStr = sprintf($textTpl, $this->fromUsername, $this->toUsername, $this->time,$title1,$Description1,$PicUrl1,$Url1);
            echo $resultStr;
      }
      //关注后回复图文信息
      private function AttentionReply2(){
         $textTpl=" <xml>
                        <ToUserName><![CDATA[%s]]></ToUserName>
                        <FromUserName><![CDATA[%s]]></FromUserName>
                        <CreateTime>%s</CreateTime>
                        <MsgType><![CDATA[news]]></MsgType>
                        <ArticleCount>3</ArticleCount>
                        <Articles>
                            <item>
                                <Title><![CDATA[%s]]></Title>
                                <Description><![CDATA[%s]]></Description>
                                <PicUrl><![CDATA[%s]]></PicUrl>
                                <Url><![CDATA[%s]]></Url>
                            </item>
                            <item>
                                <Title><![CDATA[%s]]></Title>
                                <Description><![CDATA[%s]]></Description>
                                <PicUrl><![CDATA[%s]]></PicUrl>
                                <Url><![CDATA[%s]]></Url>
                            </item>
                            <item>
                                <Title><![CDATA[%s]]></Title>
                                <Description><![CDATA[%s]]></Description>
                                <PicUrl><![CDATA[%s]]></PicUrl>
                                <Url><![CDATA[%s]]></Url>
                            </item>
                        </Articles>
                        <FuncFlag>1</FuncFlag>
                    </xml>";
            $title1="女人巧用口与舌头让男人忍不住叫喊起来";
            $Description1="1";
            $PicUrl1="http://mmsns.qpic.cn/mmsns/q3PibibJOcnbtCk2sdBRPzrMAjSicIDzt8dXxdeMjsYOr4ErOPErpSsRA/0";
            $Url1="http://mp.weixin.qq.com/mp/appmsg/show?__biz=MjM5OTkxNjIwMw==&appmsgid=10000044&itemidx=1&sign=e888bafa310611f0d8ad9c5f979316f0#wechat_redirect";
            $title2="让男人欲罢不能的内衣";
            $Description2="2";
            $PicUrl2="http://mmsns.qpic.cn/mmsns/q3PibibJOcnbtCk2sdBRPzrMAjSicIDzt8d58pYI850oAn7ibjWib8IhyGg/0";
            $Url2="http://mp.weixin.qq.com/mp/appmsg/show?__biz=MjM5OTkxNjIwMw==&appmsgid=10000044&itemidx=2&sign=85285c0119705e81b75055315953563f#wechat_redirect";
            $title3="我用身体记录我们相识的记忆";
            $Description3="3";
            $PicUrl3="http://mmsns.qpic.cn/mmsns/q3PibibJOcnbtCk2sdBRPzrMAjSicIDzt8dcYUh7OKCuCvicTQaSOicypwg/0";
            $Url3="http://mp.weixin.qq.com/mp/appmsg/show?__biz=MjM5OTkxNjIwMw==&appmsgid=10000044&itemidx=3&sign=e615e719436cb3efc6d61d2dcb938dd5#wechat_redirect";
            $resultStr = sprintf($textTpl, $this->fromUsername, $this->toUsername, $this->time,$title1,$Description1,$PicUrl1,$Url1,
                                 $title2,$Description2,$PicUrl2,$Url2,$title3,$Description3,$PicUrl3,$Url3);
            echo $resultStr;
      }
      //定制回复信息
      public function responseMsg()  {  //取用户数据
            $postStr = $GLOBALS["HTTP_RAW_POST_DATA"];
            if (!empty($postStr)){
                $postObj = simplexml_load_string($postStr, 'SimpleXMLElement', LIBXML_NOCDATA);
                $this->fromUsername = $postObj->FromUserName;//用户的微信号加密ID
                $this->toUsername = $postObj->ToUserName;    //开发者ID
                $this->keyword = trim($postObj->Content);
                $this->MsgType=utf8_decode($postObj->MsgType);            //消息类型
                if (property_exists($postObj,"Event")==true) {
                    $this->EventType=utf8_decode($postObj->Event);
                }
                $this->time = time();
                if($this->MsgType == "text"){
                  if (utf8_decode(trim($this->keyword))=="?"){
                      $contentStr=" 亲!您想了解哪个哪类型的问题呢?A情趣内衣、B成人玩具还是其他?";
                      $this->ReplyTextMsg($contentStr);
                      exit;
                  }
                  if (utf8_decode(trim($this->keyword))=="A"){
                      $contentStr =$this->fromUsername." 情趣内衣让您的生活更有情趣，详情请了解";
                      $this->ReplyTextMsg($contentStr);
                      $this->ReplyTextMsg("test");
                      exit;
                  }
                }
              if ($this->MsgType=='event'){
                //当公众账号被关注后，自动回复图文信息
                if ($this->EventType=='subscribe'){
                  //$this->AttentionReply2(); 本来想回复两条的，结果微信只能回复一条，屏蔽了这一条
                   $this->AttentionReply1();
                   exit;
                }
              }
            }
        }
     }
    ?>


"""

import unittest
from geoclient import GeoClient

APP_KEY = "You should have an app_key."
APP_ID = "You should have an app_id, too."


class Test(unittest.TestCase):

    """Unit tests for geoclient"""

    def test_address(self):
        """Test geoclient address()"""

        house_number = "314"
        street = "WEST  100 STREET"
        borough = "manhattan"
        gclient = GeoClient(APP_KEY, APP_ID)
        result = gclient.address(house_number, street, borough)
        self.assertEquals(result['address']['bbl'], '1018887502')
        self.assertEquals(result['address']['buildingIdentificationNumber'],
                          '1057093')
        self.assertEquals(result['address']['firstStreetNameNormalized'], street)
        self.assertEquals(result['address']['houseNumber'], house_number)

    def test_bbl(self):
        """Test geoclient bbl()"""

        borough = "manhattan"
        lot = "1"
        block = "1889"
        gclient = GeoClient(APP_KEY, APP_ID)
        result = gclient.bbl(borough, lot, block)
        self.assertEquals(result['bbl']['bbl'], '1000011889')
        self.assertEquals(result['bbl']['bblTaxBlock'], '00001')

    def test_bin(self):
        """Test geoclient bin()"""

        building_identification_number = '1079043'
        gclient = GeoClient(APP_KEY, APP_ID)
        result = gclient.bin(bin=building_identification_number)
        self.assertEquals(result['bin']['bbl'], '1000670001')
        self.assertEquals(result['bin']['buildingIdentificationNumber'], '1079043')

if __name__ == '__main__':
    unittest.main()
