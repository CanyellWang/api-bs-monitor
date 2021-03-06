# vim: fileencoding=utf-8 ts=4 sw=4 sts=4 et

from base import TesterBase, leaders
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class SocialTester(TesterBase):
    def u_get_friendlist(self):
        o = self.user_get_v1('im/get_friendlist.json?')
        return self.ret(o, lambda: True)

    def u_get_fanslist(self):
        o = self.user_get_v1('im/get_fanslist.json?')
        return self.ret(o, lambda: True)

    def u_myrelation_group(self):
        o = self.user_get_v1('socialGroup/myrelation_group.json?')
        return self.ret(o, lambda: 'imember' in o['data'])

#    def u_my_lovelife_list(self):
#        o = self.user_get_v1('lovelife/my_lovelife_list.json?')
#        return self.ret(o, lambda: True)

#    def u_get_interestedgroup(self):
#        o = self.user_get_v1('socialGroup/get_interestedGroup.json?imId={gimid}&', gimid=self.cfg['gimid'])
#       return self.ret(o, lambda: int(o['data'][0]['groupId']) > 0)

    def u_get_groupinfo_byperson(self):
        o = self.user_get_v1('socialGroup/get_groupInfo_byPerson.json?imId={gimid}&groupId={gid}&',
                             gimid=self.cfg['gimid'], gid=self.cfg['gid'])
        return self.ret(o, lambda: o['data']['maxUsers'] > 0)

    def u_get_topic_details(self):
        o = self.user_get_v1('socialTopic/get_topic_details.json?topicId={topicid}&', topicid=self.cfg['topicId'])
        return self.ret(o, lambda: o['data']['groupId'] == self.cfg['gid'])

    def get_home_page(self):
        o = self.comm_get_v1('socialGroup/home_page.json?')
        return self.ret(o, lambda: True)

    def get_page_query_topic_reply(self):
        o = self.comm_get_v1('socialTopic/page_query_topic_reply.json?topicId={topicid}&',
                             topicid=self.cfg['topicId'])
        return self.ret(o, lambda: o['data']['topicReplyList'][0]['groupId'] == self.cfg['gid'])

    def get_category_list(self):
        o = self.comm_get_v1('socialGroup/get_category_list.json?')
        return self.ret(o, lambda: True)

    def get_find_owner_topic_list(self):
        o = self.comm_get_v1('socialTopic/find_owner_topic_list.json?beUserId={userId}&',
                             userId=self.cfg['userId'])
        return self.ret(o, lambda: True)

    def get_find_owner_group_list(self):
        o = self.comm_get_v1('socialGroup/find_owner_group_list.json?beUserId={userId}&',
                             userId=self.cfg['userId'])
        return self.ret(o, lambda: True)

mojianli =     [(u"莫建利", "18311073279"),]
chaizhilei =   [(u"柴志磊", "18810851851"),]
liyan =        [(u"李燕",   "15210719136"),]

social_cases_v1 = [
    ('u_get_friendlist',         u'*193_好友列表', leaders + mojianli),
    ('u_get_fanslist',           u'*195_粉丝列表', leaders + mojianli),
    ('u_myrelation_group',       u'+405_我的群组列表', leaders + chaizhilei),
    ('u_get_topic_details',      u'410_话题详情页', leaders + liyan),
    ('u_get_groupinfo_byperson', u'408_用户查看群组主页', leaders + liyan),
    ('get_home_page',           u'434 圈子首页（复合接口）', leaders + mojianli),
    ('get_page_query_topic_reply', u'*418 话题详情页分页查询回复', leaders + chaizhilei),
    ('get_category_list',       u'423_分类集合接口查询', leaders + chaizhilei),
    ('get_find_owner_topic_list', u'440 个人主页--我的话题列表', leaders + liyan),
    ('get_find_owner_group_list', u'444_个人主页--我的圈子列表', leaders + liyan),
]